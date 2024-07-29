from __future__ import annotations

from itertools import groupby
from typing import Any, List, Optional

import requests
import yaml
from github import Github
from jinja2.environment import Template
from pydantic import BaseModel, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False, env_file=".env")

    template_path: str
    output_path: str
    data_path: str

    github_token: str
    gitlab_token: str


settings = Settings()  # type: ignore
g = Github(settings.github_token)


class Repository(BaseModel):
    name: str | None = None
    repo: HttpUrl
    description: str | None = None
    stars: int | None = None
    category: str


class RepositoriesData(BaseModel):
    repositories: List[Repository]


def read_awesome() -> RepositoriesData:
    with open(settings.data_path, "r") as file:
        repos = RepositoriesData(**yaml.safe_load(file))
    return repos


def render_readme(data: dict[str, Any]) -> str:
    with open(settings.template_path, "r") as readme_template:
        template = Template(readme_template.read())
    return template.render({"data": data})


def write_readme(text: str) -> None:
    with open(settings.output_path, "w") as readme_file:
        readme_file.write(text)


def load_repo_data(data: RepositoriesData):
    for repository in data.repositories:
        if "github" in repository.repo.host:
            repo = g.get_repo(repository.repo.path.strip("/"))
            repository.stars = repo.stargazers_count
            if not repository.name:
                repository.name = repo.name
            if not repository.description:
                repository.description = repo.description
        elif "gitlab" in repository.repo.host:
            name = repository.repo.path.strip("/").replace("/", "%2F")
            url = f"https://gitlab.com/api/v4/projects/{name}"
            res = requests.get(url, params={"access_token": settings.gitlab_token})
            assert "star_count" in res.json(), "Invalid GitLab repository"
            star_count = res.json()["star_count"]
            repository.stars = star_count
            if not repository.name:
                repository.name = res.json()["name"]
            if not repository.description:
                repository.description = res.json()["description"]



def run():
    awesome = read_awesome()
    load_repo_data(awesome)
    repos = awesome.model_dump()["repositories"]
    repos.sort(key=lambda x: x["category"])
    data = {
        category: sorted(repo, key=lambda x: -x["stars"])
        for category, repo in groupby(
            repos, key=lambda x: x["category"]
        )
    }

    text_readme = render_readme(data)
    write_readme(text_readme)


if __name__ == "__main__":
    run()

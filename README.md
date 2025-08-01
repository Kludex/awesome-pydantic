# Awesome Pydantic [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)

> A curated list of awesome things related to [Pydantic](https://pydantic-docs.helpmanual.io/).

These packages have not been vetted or approved by the pydantic team.


## Command-Line Interface
  
- [Tyro](https://github.com/brentyi/tyro) 🌟(737) - Tyro is a tool for generating command-line interfaces and configuration objects in Python. Generates CLI interfaces, populates helptext automatically from defaults, annotations and docstrings, understand nesting of `dataclasses`, `pydantic`, and `attrs` structures, and it supports subcommands and fine-grained configuration via runtime annotations.
  
- [Pydantic Argparse](https://github.com/SupImDos/pydantic-argparse) 🌟(128) - Pydantic Argparse provides declarative typed argument parsing using Pydantic models. (Compatibility with Pydantic V2 still pending)
  
- [Clipstick](https://github.com/sander76/clipstick) 🌟(37) - Clipstick creates your cli using Pydantic models. Define a Pydantic model as you would normally do, pass it to `clipstick` and you get a cli including subcommands, nice docstrings and validations based on `typing` and `pydantic` validators.
  

## Data Engineering
  
- [sparkdantic](https://github.com/mitchelllisle/sparkdantic) 🌟(99) - A library that converts Pydantic models to PySpark schemas (StructType), facilitating schema validation in PySpark pipelines.
  
- [Laktory](https://github.com/opencubes-ai/laktory) 🌟(51) - A DataOps framework for building Databricks lakehouse.
  

## Machine Learning
  
- [Transformers](https://github.com/huggingface/transformers) 🌟(147724) - State-of-the-art Natural Language Processing for PyTorch and TensorFlow 2.0.
  
- [ray](https://github.com/ray-project/ray) 🌟(38259) - Ray provides a simple, universal API for building distributed applications.
  
- [spaCy](https://github.com/explosion/spaCy) 🌟(32075) - spaCy is a free open-source library for Natural Language Processing in Python. It features NER, POS tagging, dependency parsing, word vectors and more.
  
- [jina](https://github.com/jina-ai/jina) 🌟(21680) - Jina is geared towards building search systems for any kind of data, including text, images, audio, video and many more. With the modular design & multi-layer abstraction, you can leverage the efficient patterns to build the system by parts, or chaining them into a Flow for an end-to-end experience.
  
- [Instructor](https://github.com/jxnl/instructor) 🌟(11095) - Controlling OpenAI Function Calling via Pydantic Models
  
- [ZenML](https://github.com/zenml-io/zenml) 🌟(4771) - MLOps framework to create reproducible ML pipelines for production machine learning.
  
- [Opyrator](https://github.com/ml-tooling/opyrator) 🌟(3131) - Turns your machine learning code into microservices with web API, interactive GUI, and more.
  
- [DocArray](https://github.com/docarray/docarray) 🌟(3085) - Represent, send, store and search multimodal data based on Pydantic. Compatible with Multiple Vector Databases
  
- [FastMRI](https://github.com/facebookresearch/fastMRI) 🌟(1453) - fastMRI is a collaborative research project from Facebook AI Research (FAIR) and NYU Langone Health to investigate the use of AI to make MRI scans faster.
  
- [ContextGem](https://github.com/shcherbak-ai/contextgem) 🌟(1285) - A free, open-source LLM framework that makes it radically easier to extract structured data and insights from documents with minimal code.
  
- [Mirascope](https://github.com/Mirascope/mirascope) 🌟(1237) - Pythonic prompt engineering for developers built on Pydantic
  
- [BoFire](https://github.com/experimental-design/bofire) 🌟(301) - Bayesian Optimization Framework Intended for Real Experiments.
  

## Object Mapping
  
- [SQLModel](https://github.com/tiangolo/sqlmodel) 🌟(16468) - SQLModel is a library for interacting with SQL databases from Python code, with Python objects.
  
- [Beanie](https://github.com/roman-right/beanie) 🌟(2395) - Beanie - is an Asynchronous Python object-document mapper (ODM) for MongoDB, based on Motor and Pydantic.
  
- [Ormar](https://github.com/collerek/ormar) 🌟(1761) - Ormar is an async ORM that was written with FastAPI in mind and uses pydantic validation. It bridges FastAPI with pydantic, as ormar models can be used directly in FastAPI requests and responses so you are left with only one set of models to maintain. Alembic migrations included.
  
- [Piccolo](https://github.com/piccolo-orm/piccolo) 🌟(1655) - An async query builder and ORM, which can auto generate Pydantic models from database tables.
  
- [Redis-OM-Python](https://github.com/redis/redis-om-python) 🌟(1237) - Redis OM Python makes it easy to model Redis data in your Python applications.
  
- [ODMantic](https://github.com/art049/odmantic) 🌟(1122) - Asynchronous ODM(Object Document Mapper) for MongoDB based on standard python type hints. It's built on top of pydantic for model definition and validation.
  
- [Djantic](https://github.com/jordaneremieff/djantic) 🌟(465) - Pydantic model support for Django.
  
- [FastDepends](https://github.com/Lancetnik/FastDepends) 🌟(395) - FastDepends - FastAPI Dependency Injection system extracted from FastAPI and cleared of all HTTP logic.
  
- [Edgy](https://github.com/tarsil/edgy) 🌟(299) - Edgy is a modern, full suite complete ORM fully built on the top of Pydantic v2. All you need in a ORM in one place. From migrations, to automatic validations.
  
- [django-pydantic-field](https://github.com/surenkov/django-pydantic-field) 🌟(168) - Django JSONField with Pydantic models as a Schema. DRF supported.
  
- [Mongox](https://github.com/aminalaee/mongox) 🌟(121) - Familiar async MongoDB ODM based on Pydantic and Motor.
  
- [pydantic-aioredis](https://github.com/andrewthetechie/pydantic-aioredis) 🌟(60) - A simple Declarative ORM for Redis using Pydantic Models and aioredis
  
- [pydantic-numpy](https://github.com/caniko/pydantic-numpy) 🌟(45) - NumPy typing for Pydantic; `NumpyModel` Pydantic model for numpy arrays for saving and loading numpy files
  
- [pydantic-sqs](https://github.com/andrewthetechie/pydantic-sqs) 🌟(4) - Send and receive pydantic models via AWS SQS
  

## Utilities
  
- [Strawberry GraphQL](https://github.com/strawberry-graphql/strawberry) 🌟(4345) - Python GraphQL library based on dataclasses.
  
- [HttpRunner](https://github.com/httprunner/httprunner) 🌟(4170) - HttpRunner is a simple & elegant, yet powerful HTTP(S) testing framework.
  
- [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator) 🌟(3352) - Pydantic model generator for easy conversion of JSON, OpenAPI, JSON Schema, GraphQL Schema, and YAML data sources.
  
- [Robusta](https://github.com/robusta-dev/robusta) 🌟(2828) - Open source Kubernetes troubleshooting and automation platform.
  
- [Pydantic-Factories](https://github.com/Goldziher/pydantic-factories) 🌟(1260) - Pydantic based factories to generate testing data.
  
- [Pydantic PyCharm Plugin](https://github.com/koxudaxi/pydantic-pycharm-plugin) 🌟(505) - A JetBrains PyCharm plugin for pydantic.
  
- [erdantic](https://github.com/drivendataorg/erdantic) 🌟(382) - Entity relationship diagrams for Python data model classes like Pydantic.
  
- [Pydantic-resolve](https://github.com/allmonday/pydantic-resolve) 🌟(254) - A small yet powerful tool to extend your pydantic schema, and resolve all descendants automatically.
  
- [pydantic-xml](https://github.com/dapper91/pydantic-xml) 🌟(213) - Pydantic xml extension
  
- [AioClock](https://github.com//ManiMozaffar/aioclock) 🌟(212) - Scheduler framework asyncio-based designed for execution of periodic task with dependency injection
  
- [jsf](https://github.com/ghandic/jsf) 🌟(184) - Creates fake JSON files from a JSON schema.
  
- [autodoc_pydantic](https://github.com/mansenfranzen/autodoc_pydantic) 🌟(169) - Seamlessly integrate pydantic models in your Sphinx documentation.
  
- [Goodconf](https://github.com/lincolnloop/goodconf) 🌟(144) - A thin wrapper over Pydantic's settings management. Allows you to define configuration variables and load them from environment or JSON/YAML file. Also generates initial configuration files and documentation for your defined configuration.
  
- [pydantic-i18n](https://github.com/boardpack/pydantic-i18n) 🌟(96) - An extension to support an i18n for the pydantic error messages.
  
- [Settings Doc](https://github.com/radeklat/settings-doc) 🌟(50) - A command line tool for generating Markdown documentation and .env files from pydantic_settings.BaseSettings.
  
- [Flake8 Pydantic](https://github.com/Viicos/flake8-pydantic) 🌟(17) - A Flake8 plugin to check Pydantic related code.
  
- [fodantic](https://github.com/jpsca/fodantic) 🌟(17) - Pydantic-based HTTP forms
  
- [easyconfig](https://github.com/spacemanspiff2007/easyconfig) 🌟(8) - Easy application configuration with yaml files and pydantic models. Allows automatic creation of default configuration files with value descriptions as comments. Additionally has environment variable expansion and support for docker secrets. Can also has support for reloading values on the fly e.g. in combination with a file watcher. Works with normal pydantic models and pydantic settings.
  
- [Settus](https://github.com/okube-ai/settus) 🌟(5) - Settings management using Pydantic Settings and extended to secrets from Azure Keyvault, Databricks secrets, AWS Secrets Manager and GCP Secrets Manager
  

## Web
  
- [FastAPI](https://github.com/tiangolo/fastapi) 🌟(87871) - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
  
- [Django Ninja](https://github.com/vitalik/django-ninja) 🌟(8411) - Django + Pydantic = Fast, Async-ready, OpenAPI, type hints based framework for building APIs.
  
- [Litestar (before Starlite)](https://github.com/litestar-org/litestar) 🌟(7011) - Flexible ASGI API framework built on top of Starlette and pydantic.
  
- [FastStream](https://github.com/airtai/faststream) 🌟(4287) - FastStream simplifies the process of writing producers and consumers for message queues, handling all the parsing, networking and documentation generation automatically.
  
- [BlackSheep](https://github.com/Neoteroi/BlackSheep) 🌟(2205) - BlackSheep is an asynchronous web framework to build event based web applications with Python. It is inspired by Flask, ASP.NET Core, and the work by Yury Selivanov.
  
- [Propan](https://github.com/Lancetnik/Propan) 🌟(501) - Propan is a powerful and easy-to-use Python framework for building event-driven applications that interact with any MQ Broker.
  
- [Flask Pydantic](https://github.com/bauerji/flask_pydantic) 🌟(398) - Flask extension for integration of the awesome pydantic package with Flask.
  
- [Piccolo Admin](https://github.com/piccolo-orm/piccolo_admin) 🌟(367) - An admin interface powered by Pydantic. Automatically generate forms using Pydantic models.
  
- [Esmerald](https://github.com/dymmond/esmerald) 🌟(357) - Full suite python web framework with results and design in mind based on Python type hints and pydantic.
  
- [SpecTree](https://github.com/0b01001001/spectree) 🌟(342) - API spec validator and OpenAPI document generator for Python web frameworks (Flask, Falcon, Starlette).
  
- [RichAPI](https://github.com//ManiMozaffar/richapi) 🌟(155) - Find HTTPExceptions and turn them into documented responses!
  
- [Quart-Schema](https://github.com/pgjones/quart-schema) 🌟(95) - Quart-Schema is a Quart extension that provides schema validation and auto-generated API documentation.
  
- [turms](https://github.com/jhnnsrs/turms) 🌟(68) - GraphQL code generator that generates pydantic models from GraphQL documents
  
- [graphql-query](https://github.com/denisart/graphql-query) 🌟(66) - The package to build GraphQL queries from pydantic classes
  
- [PydanticRPC](https://github.com/i2y/pydantic-rpc) 🌟(29) - PydanticRPC enables you to quickly expose your Pydantic models via gRPC/Connect RPC services without having to manually write any protobuf files.
  
- [pydantic-enhanced-serializer](https://github.com/adamsussman/pydantic-enhanced-serializer) 🌟(9) - Better pydantic object output for apis including selectable fields and smart object expansions.
  


## Contributing

Feel free to add your own package here by creating a PR. You just need to add an entry to the end line of [awesome.yaml](./awesome.yaml) file.
For example:

```yaml
- repo: https://github.com/tiangolo/fastapi
  category: Web
  # optional
  name: FastAPI
  description: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
```

Then it will automate reordered by repository stars and category.
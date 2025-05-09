# Awesome Pydantic [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)

> A curated list of awesome things related to [Pydantic](https://pydantic-docs.helpmanual.io/).

These packages have not been vetted or approved by the pydantic team.


## Command-Line Interface
  
- [Tyro](https://github.com/brentyi/tyro) 🌟(627) - Tyro is a tool for generating command-line interfaces and configuration objects in Python. Generates CLI interfaces, populates helptext automatically from defaults, annotations and docstrings, understand nesting of `dataclasses`, `pydantic`, and `attrs` structures, and it supports subcommands and fine-grained configuration via runtime annotations.
  
- [Pydantic Argparse](https://github.com/SupImDos/pydantic-argparse) 🌟(124) - Pydantic Argparse provides declarative typed argument parsing using Pydantic models. (Compatibility with Pydantic V2 still pending)
  
- [Clipstick](https://github.com/sander76/clipstick) 🌟(37) - Clipstick creates your cli using Pydantic models. Define a Pydantic model as you would normally do, pass it to `clipstick` and you get a cli including subcommands, nice docstrings and validations based on `typing` and `pydantic` validators.
  

## Data Engineering
  
- [sparkdantic](https://github.com/mitchelllisle/sparkdantic) 🌟(86) - A library that converts Pydantic models to PySpark schemas (StructType), facilitating schema validation in PySpark pipelines.
  
- [Laktory](https://github.com/opencubes-ai/laktory) 🌟(50) - A DataOps framework for building Databricks lakehouse.
  

## Machine Learning
  
- [Transformers](https://github.com/huggingface/transformers) 🌟(144024) - State-of-the-art Natural Language Processing for PyTorch and TensorFlow 2.0.
  
- [ray](https://github.com/ray-project/ray) 🌟(36937) - Ray provides a simple, universal API for building distributed applications.
  
- [spaCy](https://github.com/explosion/spaCy) 🌟(31525) - spaCy is a free open-source library for Natural Language Processing in Python. It features NER, POS tagging, dependency parsing, word vectors and more.
  
- [jina](https://github.com/jina-ai/jina) 🌟(21552) - Jina is geared towards building search systems for any kind of data, including text, images, audio, video and many more. With the modular design & multi-layer abstraction, you can leverage the efficient patterns to build the system by parts, or chaining them into a Flow for an end-to-end experience.
  
- [Instructor](https://github.com/jxnl/instructor) 🌟(10375) - Controlling OpenAI Function Calling via Pydantic Models
  
- [ZenML](https://github.com/zenml-io/zenml) 🌟(4573) - MLOps framework to create reproducible ML pipelines for production machine learning.
  
- [Opyrator](https://github.com/ml-tooling/opyrator) 🌟(3118) - Turns your machine learning code into microservices with web API, interactive GUI, and more.
  
- [DocArray](https://github.com/docarray/docarray) 🌟(3056) - Represent, send, store and search multimodal data based on Pydantic. Compatible with Multiple Vector Databases
  
- [FastMRI](https://github.com/facebookresearch/fastMRI) 🌟(1426) - fastMRI is a collaborative research project from Facebook AI Research (FAIR) and NYU Langone Health to investigate the use of AI to make MRI scans faster.
  
- [Mirascope](https://github.com/Mirascope/mirascope) 🌟(1101) - Pythonic prompt engineering for developers built on Pydantic
  
- [BoFire](https://github.com/experimental-design/bofire) 🌟(281) - Bayesian Optimization Framework Intended for Real Experiments.
  

## Object Mapping
  
- [SQLModel](https://github.com/tiangolo/sqlmodel) 🌟(15878) - SQLModel is a library for interacting with SQL databases from Python code, with Python objects.
  
- [Beanie](https://github.com/roman-right/beanie) 🌟(2318) - Beanie - is an Asynchronous Python object-document mapper (ODM) for MongoDB, based on Motor and Pydantic.
  
- [Ormar](https://github.com/collerek/ormar) 🌟(1735) - Ormar is an async ORM that was written with FastAPI in mind and uses pydantic validation. It bridges FastAPI with pydantic, as ormar models can be used directly in FastAPI requests and responses so you are left with only one set of models to maintain. Alembic migrations included.
  
- [Piccolo](https://github.com/piccolo-orm/piccolo) 🌟(1592) - An async query builder and ORM, which can auto generate Pydantic models from database tables.
  
- [Redis-OM-Python](https://github.com/redis/redis-om-python) 🌟(1214) - Redis OM Python makes it easy to model Redis data in your Python applications.
  
- [ODMantic](https://github.com/art049/odmantic) 🌟(1117) - Asynchronous ODM(Object Document Mapper) for MongoDB based on standard python type hints. It's built on top of pydantic for model definition and validation.
  
- [Djantic](https://github.com/jordaneremieff/djantic) 🌟(462) - Pydantic model support for Django.
  
- [FastDepends](https://github.com/Lancetnik/FastDepends) 🌟(368) - FastDepends - FastAPI Dependency Injection system extracted from FastAPI and cleared of all HTTP logic.
  
- [Edgy](https://github.com/tarsil/edgy) 🌟(270) - Edgy is a modern, full suite complete ORM fully built on the top of Pydantic v2. All you need in a ORM in one place. From migrations, to automatic validations.
  
- [django-pydantic-field](https://github.com/surenkov/django-pydantic-field) 🌟(148) - Django JSONField with Pydantic models as a Schema. DRF supported.
  
- [Mongox](https://github.com/aminalaee/mongox) 🌟(121) - Familiar async MongoDB ODM based on Pydantic and Motor.
  
- [pydantic-aioredis](https://github.com/andrewthetechie/pydantic-aioredis) 🌟(60) - A simple Declarative ORM for Redis using Pydantic Models and aioredis
  
- [pydantic-numpy](https://github.com/caniko/pydantic-numpy) 🌟(43) - NumPy typing for Pydantic; `NumpyModel` Pydantic model for numpy arrays for saving and loading numpy files
  
- [pydantic-sqs](https://github.com/andrewthetechie/pydantic-sqs) 🌟(4) - Send and receive pydantic models via AWS SQS
  

## Utilities
  
- [Strawberry GraphQL](https://github.com/strawberry-graphql/strawberry) 🌟(4253) - Python GraphQL library based on dataclasses.
  
- [HttpRunner](https://github.com/httprunner/httprunner) 🌟(4136) - HttpRunner is a simple & elegant, yet powerful HTTP(S) testing framework.
  
- [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator) 🌟(3162) - Pydantic model generator for easy conversion of JSON, OpenAPI, JSON Schema, GraphQL Schema, and YAML data sources.
  
- [Robusta](https://github.com/robusta-dev/robusta) 🌟(2754) - Open source Kubernetes troubleshooting and automation platform.
  
- [Pydantic-Factories](https://github.com/Goldziher/pydantic-factories) 🌟(1197) - Pydantic based factories to generate testing data.
  
- [Pydantic PyCharm Plugin](https://github.com/koxudaxi/pydantic-pycharm-plugin) 🌟(491) - A JetBrains PyCharm plugin for pydantic.
  
- [erdantic](https://github.com/drivendataorg/erdantic) 🌟(371) - Entity relationship diagrams for Python data model classes like Pydantic.
  
- [Pydantic-resolve](https://github.com/allmonday/pydantic-resolve) 🌟(238) - A small yet powerful tool to extend your pydantic schema, and resolve all descendants automatically.
  
- [pydantic-xml](https://github.com/dapper91/pydantic-xml) 🌟(195) - Pydantic xml extension
  
- [jsf](https://github.com/ghandic/jsf) 🌟(180) - Creates fake JSON files from a JSON schema.
  
- [AioClock](https://github.com//ManiMozaffar/aioclock) 🌟(180) - Scheduler framework asyncio-based designed for execution of periodic task with dependency injection
  
- [autodoc_pydantic](https://github.com/mansenfranzen/autodoc_pydantic) 🌟(166) - Seamlessly integrate pydantic models in your Sphinx documentation.
  
- [Goodconf](https://github.com/lincolnloop/goodconf) 🌟(141) - A thin wrapper over Pydantic's settings management. Allows you to define configuration variables and load them from environment or JSON/YAML file. Also generates initial configuration files and documentation for your defined configuration.
  
- [pydantic-i18n](https://github.com/boardpack/pydantic-i18n) 🌟(92) - An extension to support an i18n for the pydantic error messages.
  
- [Settings Doc](https://github.com/radeklat/settings-doc) 🌟(45) - A command line tool for generating Markdown documentation and .env files from pydantic_settings.BaseSettings.
  
- [Flake8 Pydantic](https://github.com/Viicos/flake8-pydantic) 🌟(17) - A Flake8 plugin to check Pydantic related code.
  
- [fodantic](https://github.com/jpsca/fodantic) 🌟(12) - Pydantic-based HTTP forms
  
- [easyconfig](https://github.com/spacemanspiff2007/easyconfig) 🌟(7) - Easy application configuration with yaml files and pydantic models. Allows automatic creation of default configuration files with value descriptions as comments. Additionally has environment variable expansion and support for docker secrets. Can also has support for reloading values on the fly e.g. in combination with a file watcher. Works with normal pydantic models and pydantic settings.
  
- [Settus](https://github.com/okube-ai/settus) 🌟(5) - Settings management using Pydantic Settings and extended to secrets from Azure Keyvault, Databricks secrets, AWS Secrets Manager and GCP Secrets Manager
  

## Web
  
- [FastAPI](https://github.com/tiangolo/fastapi) 🌟(84387) - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
  
- [Django Ninja](https://github.com/vitalik/django-ninja) 🌟(8089) - Django + Pydantic = Fast, Async-ready, OpenAPI, type hints based framework for building APIs.
  
- [Litestar (before Starlite)](https://github.com/litestar-org/litestar) 🌟(6567) - Flexible ASGI API framework built on top of Starlette and pydantic.
  
- [FastStream](https://github.com/airtai/faststream) 🌟(3888) - FastStream simplifies the process of writing producers and consumers for message queues, handling all the parsing, networking and documentation generation automatically.
  
- [BlackSheep](https://github.com/Neoteroi/BlackSheep) 🌟(2150) - BlackSheep is an asynchronous web framework to build event based web applications with Python. It is inspired by Flask, ASP.NET Core, and the work by Yury Selivanov.
  
- [Propan](https://github.com/Lancetnik/Propan) 🌟(508) - Propan is a powerful and easy-to-use Python framework for building event-driven applications that interact with any MQ Broker.
  
- [Flask Pydantic](https://github.com/bauerji/flask_pydantic) 🌟(388) - Flask extension for integration of the awesome pydantic package with Flask.
  
- [Piccolo Admin](https://github.com/piccolo-orm/piccolo_admin) 🌟(349) - An admin interface powered by Pydantic. Automatically generate forms using Pydantic models.
  
- [Esmerald](https://github.com/dymmond/esmerald) 🌟(342) - Full suite python web framework with results and design in mind based on Python type hints and pydantic.
  
- [SpecTree](https://github.com/0b01001001/spectree) 🌟(333) - API spec validator and OpenAPI document generator for Python web frameworks (Flask, Falcon, Starlette).
  
- [RichAPI](https://github.com//ManiMozaffar/richapi) 🌟(151) - Find HTTPExceptions and turn them into documented responses!
  
- [Quart-Schema](https://github.com/pgjones/quart-schema) 🌟(93) - Quart-Schema is a Quart extension that provides schema validation and auto-generated API documentation.
  
- [turms](https://github.com/jhnnsrs/turms) 🌟(66) - GraphQL code generator that generates pydantic models from GraphQL documents
  
- [graphql-query](https://github.com/denisart/graphql-query) 🌟(65) - The package to build GraphQL queries from pydantic classes
  
- [PydanticRPC](https://github.com/i2y/pydantic-rpc) 🌟(23) - PydanticRPC enables you to quickly expose your Pydantic models via gRPC/Connect RPC services without having to manually write any protobuf files.
  
- [pydantic-enhanced-serializer](https://github.com/adamsussman/pydantic-enhanced-serializer) 🌟(6) - Better pydantic object output for apis including selectable fields and smart object expansions.
  


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
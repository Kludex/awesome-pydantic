# Awesome Pydantic [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)

> A curated list of awesome things related to [Pydantic](https://pydantic-docs.helpmanual.io/).

These packages have not been vetted or approved by the pydantic team.


## Command-Line Interface
  
- [Tyro](https://github.com/brentyi/tyro) 🌟(646) - Tyro is a tool for generating command-line interfaces and configuration objects in Python. Generates CLI interfaces, populates helptext automatically from defaults, annotations and docstrings, understand nesting of `dataclasses`, `pydantic`, and `attrs` structures, and it supports subcommands and fine-grained configuration via runtime annotations.
  
- [Pydantic Argparse](https://github.com/SupImDos/pydantic-argparse) 🌟(124) - Pydantic Argparse provides declarative typed argument parsing using Pydantic models. (Compatibility with Pydantic V2 still pending)
  
- [Clipstick](https://github.com/sander76/clipstick) 🌟(37) - Clipstick creates your cli using Pydantic models. Define a Pydantic model as you would normally do, pass it to `clipstick` and you get a cli including subcommands, nice docstrings and validations based on `typing` and `pydantic` validators.
  

## Data Engineering
  
- [sparkdantic](https://github.com/mitchelllisle/sparkdantic) 🌟(92) - A library that converts Pydantic models to PySpark schemas (StructType), facilitating schema validation in PySpark pipelines.
  
- [Laktory](https://github.com/opencubes-ai/laktory) 🌟(50) - A DataOps framework for building Databricks lakehouse.
  

## Machine Learning
  
- [Transformers](https://github.com/huggingface/transformers) 🌟(145219) - State-of-the-art Natural Language Processing for PyTorch and TensorFlow 2.0.
  
- [ray](https://github.com/ray-project/ray) 🌟(37385) - Ray provides a simple, universal API for building distributed applications.
  
- [spaCy](https://github.com/explosion/spaCy) 🌟(31711) - spaCy is a free open-source library for Natural Language Processing in Python. It features NER, POS tagging, dependency parsing, word vectors and more.
  
- [jina](https://github.com/jina-ai/jina) 🌟(21598) - Jina is geared towards building search systems for any kind of data, including text, images, audio, video and many more. With the modular design & multi-layer abstraction, you can leverage the efficient patterns to build the system by parts, or chaining them into a Flow for an end-to-end experience.
  
- [Instructor](https://github.com/jxnl/instructor) 🌟(10695) - Controlling OpenAI Function Calling via Pydantic Models
  
- [ZenML](https://github.com/zenml-io/zenml) 🌟(4620) - MLOps framework to create reproducible ML pipelines for production machine learning.
  
- [Opyrator](https://github.com/ml-tooling/opyrator) 🌟(3124) - Turns your machine learning code into microservices with web API, interactive GUI, and more.
  
- [DocArray](https://github.com/docarray/docarray) 🌟(3068) - Represent, send, store and search multimodal data based on Pydantic. Compatible with Multiple Vector Databases
  
- [FastMRI](https://github.com/facebookresearch/fastMRI) 🌟(1435) - fastMRI is a collaborative research project from Facebook AI Research (FAIR) and NYU Langone Health to investigate the use of AI to make MRI scans faster.
  
- [Mirascope](https://github.com/Mirascope/mirascope) 🌟(1164) - Pythonic prompt engineering for developers built on Pydantic
  
- [ContextGem](https://github.com/shcherbak-ai/contextgem) 🌟(1105) - A free, open-source LLM framework that makes it radically easier to extract structured data and insights from documents with minimal code.
  
- [BoFire](https://github.com/experimental-design/bofire) 🌟(289) - Bayesian Optimization Framework Intended for Real Experiments.
  

## Object Mapping
  
- [SQLModel](https://github.com/tiangolo/sqlmodel) 🌟(16099) - SQLModel is a library for interacting with SQL databases from Python code, with Python objects.
  
- [Beanie](https://github.com/roman-right/beanie) 🌟(2334) - Beanie - is an Asynchronous Python object-document mapper (ODM) for MongoDB, based on Motor and Pydantic.
  
- [Ormar](https://github.com/collerek/ormar) 🌟(1745) - Ormar is an async ORM that was written with FastAPI in mind and uses pydantic validation. It bridges FastAPI with pydantic, as ormar models can be used directly in FastAPI requests and responses so you are left with only one set of models to maintain. Alembic migrations included.
  
- [Piccolo](https://github.com/piccolo-orm/piccolo) 🌟(1609) - An async query builder and ORM, which can auto generate Pydantic models from database tables.
  
- [Redis-OM-Python](https://github.com/redis/redis-om-python) 🌟(1223) - Redis OM Python makes it easy to model Redis data in your Python applications.
  
- [ODMantic](https://github.com/art049/odmantic) 🌟(1119) - Asynchronous ODM(Object Document Mapper) for MongoDB based on standard python type hints. It's built on top of pydantic for model definition and validation.
  
- [Djantic](https://github.com/jordaneremieff/djantic) 🌟(465) - Pydantic model support for Django.
  
- [FastDepends](https://github.com/Lancetnik/FastDepends) 🌟(382) - FastDepends - FastAPI Dependency Injection system extracted from FastAPI and cleared of all HTTP logic.
  
- [Edgy](https://github.com/tarsil/edgy) 🌟(281) - Edgy is a modern, full suite complete ORM fully built on the top of Pydantic v2. All you need in a ORM in one place. From migrations, to automatic validations.
  
- [django-pydantic-field](https://github.com/surenkov/django-pydantic-field) 🌟(154) - Django JSONField with Pydantic models as a Schema. DRF supported.
  
- [Mongox](https://github.com/aminalaee/mongox) 🌟(121) - Familiar async MongoDB ODM based on Pydantic and Motor.
  
- [pydantic-aioredis](https://github.com/andrewthetechie/pydantic-aioredis) 🌟(60) - A simple Declarative ORM for Redis using Pydantic Models and aioredis
  
- [pydantic-numpy](https://github.com/caniko/pydantic-numpy) 🌟(45) - NumPy typing for Pydantic; `NumpyModel` Pydantic model for numpy arrays for saving and loading numpy files
  
- [pydantic-sqs](https://github.com/andrewthetechie/pydantic-sqs) 🌟(4) - Send and receive pydantic models via AWS SQS
  

## Utilities
  
- [Strawberry GraphQL](https://github.com/strawberry-graphql/strawberry) 🌟(4288) - Python GraphQL library based on dataclasses.
  
- [HttpRunner](https://github.com/httprunner/httprunner) 🌟(4144) - HttpRunner is a simple & elegant, yet powerful HTTP(S) testing framework.
  
- [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator) 🌟(3236) - Pydantic model generator for easy conversion of JSON, OpenAPI, JSON Schema, GraphQL Schema, and YAML data sources.
  
- [Robusta](https://github.com/robusta-dev/robusta) 🌟(2780) - Open source Kubernetes troubleshooting and automation platform.
  
- [Pydantic-Factories](https://github.com/Goldziher/pydantic-factories) 🌟(1220) - Pydantic based factories to generate testing data.
  
- [Pydantic PyCharm Plugin](https://github.com/koxudaxi/pydantic-pycharm-plugin) 🌟(498) - A JetBrains PyCharm plugin for pydantic.
  
- [erdantic](https://github.com/drivendataorg/erdantic) 🌟(375) - Entity relationship diagrams for Python data model classes like Pydantic.
  
- [Pydantic-resolve](https://github.com/allmonday/pydantic-resolve) 🌟(245) - A small yet powerful tool to extend your pydantic schema, and resolve all descendants automatically.
  
- [pydantic-xml](https://github.com/dapper91/pydantic-xml) 🌟(203) - Pydantic xml extension
  
- [AioClock](https://github.com//ManiMozaffar/aioclock) 🌟(182) - Scheduler framework asyncio-based designed for execution of periodic task with dependency injection
  
- [jsf](https://github.com/ghandic/jsf) 🌟(181) - Creates fake JSON files from a JSON schema.
  
- [autodoc_pydantic](https://github.com/mansenfranzen/autodoc_pydantic) 🌟(168) - Seamlessly integrate pydantic models in your Sphinx documentation.
  
- [Goodconf](https://github.com/lincolnloop/goodconf) 🌟(141) - A thin wrapper over Pydantic's settings management. Allows you to define configuration variables and load them from environment or JSON/YAML file. Also generates initial configuration files and documentation for your defined configuration.
  
- [pydantic-i18n](https://github.com/boardpack/pydantic-i18n) 🌟(92) - An extension to support an i18n for the pydantic error messages.
  
- [Settings Doc](https://github.com/radeklat/settings-doc) 🌟(46) - A command line tool for generating Markdown documentation and .env files from pydantic_settings.BaseSettings.
  
- [Flake8 Pydantic](https://github.com/Viicos/flake8-pydantic) 🌟(17) - A Flake8 plugin to check Pydantic related code.
  
- [fodantic](https://github.com/jpsca/fodantic) 🌟(13) - Pydantic-based HTTP forms
  
- [easyconfig](https://github.com/spacemanspiff2007/easyconfig) 🌟(7) - Easy application configuration with yaml files and pydantic models. Allows automatic creation of default configuration files with value descriptions as comments. Additionally has environment variable expansion and support for docker secrets. Can also has support for reloading values on the fly e.g. in combination with a file watcher. Works with normal pydantic models and pydantic settings.
  
- [Settus](https://github.com/okube-ai/settus) 🌟(5) - Settings management using Pydantic Settings and extended to secrets from Azure Keyvault, Databricks secrets, AWS Secrets Manager and GCP Secrets Manager
  

## Web
  
- [FastAPI](https://github.com/tiangolo/fastapi) 🌟(85933) - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
  
- [Django Ninja](https://github.com/vitalik/django-ninja) 🌟(8208) - Django + Pydantic = Fast, Async-ready, OpenAPI, type hints based framework for building APIs.
  
- [Litestar (before Starlite)](https://github.com/litestar-org/litestar) 🌟(6741) - Flexible ASGI API framework built on top of Starlette and pydantic.
  
- [FastStream](https://github.com/airtai/faststream) 🌟(4005) - FastStream simplifies the process of writing producers and consumers for message queues, handling all the parsing, networking and documentation generation automatically.
  
- [BlackSheep](https://github.com/Neoteroi/BlackSheep) 🌟(2172) - BlackSheep is an asynchronous web framework to build event based web applications with Python. It is inspired by Flask, ASP.NET Core, and the work by Yury Selivanov.
  
- [Propan](https://github.com/Lancetnik/Propan) 🌟(506) - Propan is a powerful and easy-to-use Python framework for building event-driven applications that interact with any MQ Broker.
  
- [Flask Pydantic](https://github.com/bauerji/flask_pydantic) 🌟(392) - Flask extension for integration of the awesome pydantic package with Flask.
  
- [Piccolo Admin](https://github.com/piccolo-orm/piccolo_admin) 🌟(358) - An admin interface powered by Pydantic. Automatically generate forms using Pydantic models.
  
- [Esmerald](https://github.com/dymmond/esmerald) 🌟(345) - Full suite python web framework with results and design in mind based on Python type hints and pydantic.
  
- [SpecTree](https://github.com/0b01001001/spectree) 🌟(336) - API spec validator and OpenAPI document generator for Python web frameworks (Flask, Falcon, Starlette).
  
- [RichAPI](https://github.com//ManiMozaffar/richapi) 🌟(153) - Find HTTPExceptions and turn them into documented responses!
  
- [Quart-Schema](https://github.com/pgjones/quart-schema) 🌟(93) - Quart-Schema is a Quart extension that provides schema validation and auto-generated API documentation.
  
- [turms](https://github.com/jhnnsrs/turms) 🌟(66) - GraphQL code generator that generates pydantic models from GraphQL documents
  
- [graphql-query](https://github.com/denisart/graphql-query) 🌟(66) - The package to build GraphQL queries from pydantic classes
  
- [PydanticRPC](https://github.com/i2y/pydantic-rpc) 🌟(25) - PydanticRPC enables you to quickly expose your Pydantic models via gRPC/Connect RPC services without having to manually write any protobuf files.
  
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
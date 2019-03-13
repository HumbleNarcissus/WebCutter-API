# WebCutter-API
[![Build Status](https://travis-ci.org/HumbleNarcissus/WebCutter-API.svg?branch=master)](https://travis-ci.org/HumbleNarcissus/WebCutter-API) [![codecov](https://codecov.io/gh/HumbleNarcissus/WebCutter-API/branch/master/graph/badge.svg)](https://codecov.io/gh/HumbleNarcissus/WebCutter-API)

Python RESTful API - Bitly like app

Webcutter is an application created for fun using: Python, Flask, Flask RESTful and SQLAlchemy with PostgreSQL.

The goal of this application is to create RESTful Api using Python and connect it with my Javascript's frontend created with React.

Application is live on DigitalOcen and can be tested at http://165.227.122.123/ or locally with docker.
To run locally run:
1. "docker-compose -f docker-compose.yml up -d --build" to set up and build project.
2. "docker-compose -f docker-compose.yml exec cutter python manage.py recreate-db" to create database.
3. "docker-compose -f docker-compose.yml exec cutter python manage.py test" to test everything is working.

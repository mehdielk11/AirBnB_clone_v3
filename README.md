# AirBnB Clone - RESTful API

The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A RESTful API is added in this segment to aid data access in AirBnB(HBnB) website.

## Environment

This project is interpreted/tested on Ubuntu 20.04 LTS using python3 (version 3.4.3)

# Getting Started

You can launch the API with your storage type of choice and the correct environment variables.

- _Database Storage_
  `HBNB_MYSQL_USER=<mysqluser> HBNB_MYSQL_PWD=<mysqlpassword> HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=<mysqldb> HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app`
- _File Storage_
  `HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app`

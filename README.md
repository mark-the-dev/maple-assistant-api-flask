# flask_rest_api_template
Template to use in creating RESTful APIs using Flask

This API is built using the `flask_restx` library, utilizing SQLAlchemy as an ORM for a remote MySQL database

# Local Setup

It is required to have python installed inorder to utilize pip. Assuming python is installed, enter following in the terminal to install the python dependencies

```
$ make install
```

It is required to have a MySQL database for this API to work. Assuming one is prepared, follow these instructions in the terminal to prepare environment variables

1. Create a `.env` file
2. Using a file editor of choice include:
```
DB_HOST=[host here]
DB_USER=[user here]
DB_PASSWORD=[passsword here]
DB_DATABASE=[database here]
```

# Manual

## Startup Developer Environment
```
$ make dev 
```

## Startup Test Environment
```
$ make test
```

## Execute Unit Tests
```
$ make unittest
```


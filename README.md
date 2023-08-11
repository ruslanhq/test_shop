# TestShop

This repository contains the source code for the TestShop app, a simple application with user and products with tags, category.

## Table of Contents

- [Installation](#installation)
- [Endpoints](#endpoints)

## Installation

To install and run this project, follow these steps:

1. Clone the repository: 
```sh
git clone https://github.com/ruslanhq/test_shop.git
```
2. Rename *.env.dist* to *.env*:
```sh
mv .env.dist .env
```
3. Run command for up docker containers and start application:
```sh
make up
```

## Endpoints

The Orders App provides the following endpoints:

1. **POST api/registration/**: Register user.
2. **POST api/login/**: Login user (get jwt tokens).
3. **GET /api/products/**: Get List of products.
4. **GET /api/products/export/**: Get XLSX file with products data.
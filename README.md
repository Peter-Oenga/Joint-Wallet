# Joint Wallet Savings Group

## Overview
Joint Wallet is a web application designed to facilitate collaborative savings among group members. It provides features such as user management, loan management, and payment tracking. This project leverages Django for backend development and PostgreSQL for database management. The goal is to create an efficient and user-friendly platform for managing group savings and related financial activities.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Database Setup](#database-setup)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Run Migrations](#run-migrations)
  - [Create a Superuser](#create-a-superuser)
  - [Run the Development Server](#run-the-development-server)
- [Database Migrations](#database-migrations)
  - [Drop Tables with Dependencies](#drop-tables-with-dependencies)
  - [Fake Migrations](#fake-migrations)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
- **User Management**: Custom user model extending Django's `AbstractUser` with additional fields such as phone number and address.
- **Loan Management**: Ability to create, update, and manage loans within the savings group.
- **Payment Tracking**: Track payments made towards loans and maintain payment histories.
- **Admin Interface**: Enhanced admin interface for comprehensive management of users, loans, and payments. Utilizes Django's admin capabilities to provide an easy-to-use backend management system.
- **Security**: Built-in authentication and authorization mechanisms provided by Django to ensure secure access to the application.
- **Scalability**: Designed to handle an increasing number of users and transactions efficiently.

## Installation

### Prerequisites
Before you begin, ensure you have met the following requirements:
- **Python 3.7+**: The programming language used for backend development.
- **Django 3.2+**: The web framework used to build the application.
- **PostgreSQL**: The relational database management system used for data storage.

### Clone the Repository
Clone the repository from GitHub to your local machine using the following command:
```bash
git clone https://github.com/Peter-Oenga/joint-wallet.git
cd joint-wallet

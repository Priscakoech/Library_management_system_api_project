# Library Management System API Project

This is a Django-based API for managing a library system. The project allows users to manage books, authors, and library records.

## Setup Instructions

Follow these steps to set up the project on your local machine.

### 1. Clone the repository

First, clone the repository to my local machine:

```bash
git clone https://github.com/Priscakoech/Library_management_system_api_project.git

# API Authentication Setup

This project uses Django Rest Framework for building an API, with basic authentication implemented using both session-based and token-based methods.

## Authentication Methods

### 1. Session-Based Authentication
- This method uses Django's built-in session authentication. To test it:
  1. Log in through the Django login page or set up a session in Postman.
  2. Send a request to `/api/users/` with the session cookie.

### 2. Token-Based Authentication
- Token authentication is implemented using `djangorestframework.authtoken`.
- To obtain a token, send a `POST` request to `/api-token-auth/` with your `username` and `password`.
- Include the token in the `Authorization` header of your requests:

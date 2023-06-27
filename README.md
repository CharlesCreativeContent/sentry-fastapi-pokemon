# Sentry-FastAPI-Demo
This repository contains a template for a FastAPI backend with Sentry Monitoring, ready to be deployed on Vercel.

## Overview
The Sentry-FastAPI-Demo is a backend application built with FastAPI and integrated with Sentry for error tracking and reporting. The application is designed to be deployed on Vercel, providing a seamless and scalable solution for backend services.

## Repository Structure
The repository contains the following key files:

main.py: This is the main application file where the FastAPI application is defined.

requirements.txt: This file lists the Python dependencies required by the application.

vercel.json: This file contains the configuration settings for deploying the application on Vercel.

## Getting Started
To get started with this template, follow these steps:

Clone the repository: git clone https://github.com/CharlesCreativeContent/sentry-fastapi-demo.git

Navigate into the project directory: cd sentry-fastapi-demo

Install the required dependencies: pip install -r requirements.txt

Run the application locally: uvicorn main:app --reload

Open your browser and navigate to http://localhost:8000 to view the application.

## Deploying on Vercel

To deploy the application on Vercel, you will need to:

Create a new project on Vercel and link it to your cloned repository.

Configure the project settings according to the vercel.json file.

Deploy the application.

## Sentry Monitoring
This application is integrated with Sentry for error tracking and reporting. To use Sentry, you will need to sign up for a Sentry account and configure the Sentry DSN in your application.

## Contributing
Contributions to the Sentry-FastAPI-Demo are welcome. Please feel free to fork the repository and submit pull requests.

## License
The Sentry-FastAPI-Demo is open-source software licensed under the MIT license.

## Support
If you encounter any issues while using the Sentry-FastAPI-Demo, please open an issue on the GitHub repository.

## Acknowledgements
Thanks to the FastAPI and Sentry communities for their great work, which made this template possible.

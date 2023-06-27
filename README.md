# Sentry-FastAPI-Demo
The Sentry-FastAPI-Demo is a backend application built with FastAPI and integrated with Sentry for error tracking and reporting. The application is designed to be deployed on Vercel, providing a seamless and scalable solution for backend services.

## Repository Structure
The repository contains the following key files:

+ __main.py__: This is the main application file where the FastAPI application is defined.

+ __requirements.txt__: This file lists the Python dependencies required by the application.

+ __vercel.json__: This file contains the configuration settings for deploying the application on Vercel.

+ __pokedex.py__: This file contains the pokemon data to be served.

## Getting Started
To get started with this template, follow these steps:

1. Clone the repository: ```git clone https://github.com/CharlesCreativeContent/sentry-fastapi-demo.git```

2. Navigate into the project directory: ```cd sentry-fastapi-demo```

3. Run the application locally: ```uvicorn main:app --reload```

4. Open your browser and navigate to http://localhost:8000 to view the application.

## Deploying on Vercel

To deploy the application on Vercel, you will need to:

+ Create a new project on Vercel and link it to your cloned repository.

+ To use Sentry, you will need to sign in to your Sentry account from [Vercel Integration Dashboard](https://vercel.com/integrations/sentry).

+ Deploy the application.

## License
The Sentry-FastAPI-Demo is open-source software licensed under the MIT license.

## Acknowledgements
Thanks to the FastAPI and Sentry communities for their great work, which made this template possible.

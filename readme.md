# Multi-Service Web Application

This project is a comprehensive web application leveraging Docker to integrate Django, React, Flutter, and a Language Model (LLM) service. It utilizes Docker Swarm for orchestration and deployment.

## Architecture

- **Backend**: Django application for server-side logic and user management
- **Frontend**: React-based user interface
- **Mobile/Web App**: Flutter application served via Nginx
- **AI Service**: Custom LLM based on GPT-2, fine-tuned with the Alpaca dataset

## Prerequisites

- Docker Desktop
- Git

## Installation

1. Clone the repository:
   ```console
   git clone https://github.com/poornikabonam/Django-test.git
   ```

3. Navigate to the project directory:
   ```console
   cd Django-test
   ```

## Deployment

1. Initialize Docker Swarm:
   ```console
   docker swarm init
   ```

3. Deploy the stack:
   ```console
   docker stack deploy -c docker-stack.yml my_stack
   ```

## Service Access

After successful deployment, access the services at:

- Django Backend: http://localhost:8000
- React Frontend: http://localhost:3000
- Flutter Web App: http://localhost:9000
- LLM Service: http://localhost:5000

## Monitoring

To view running services:
docker ps

## Shutdown

To leave the swarm and stop all services:
docker swarm leave --force

## Troubleshooting

- If services fail to start, check Docker logs for detailed error messages.
- For Django-specific issues, ensure the container is configured correctly in the docker-stack.yml file.

## Testing

To run tests within Docker:

1. Ensure your Dockerfile includes necessary test commands.
2. Execute tests as part of the build process or via custom Docker commands.


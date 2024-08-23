This project is a multi-service web application setup using Docker, integrating Django, React, Flutter, and an LLM service. The Django application handles backend logic and user management, while React serves as the frontend UI. Flutter is used to build a web application that is deployed via Nginx. The LLM service, based on a GPT-2 model fine-tuned on the Alpaca dataset, is used for language modeling tasks.Used docker desktop to run the containers using docker swarm.
Running the Services

    Django: Handles backend logic and user management. Access it at http://localhost:8000. Make sure to run docker-compose up or docker stack deploy for it to start correctly.

    React: Serves as the frontend for user interactions. Visit http://localhost:3000 to access the React application.

    Flutter: The web app built with Flutter is served by Nginx. Access it at http://localhost:9000.

    LLM Service: This service uses a fine-tuned GPT-2 model on the Alpaca dataset for various language processing tasks. It's available at http://localhost:5000.

Notes

    Ensure all services are up and running by using Docker commands: docker stack deploy -c docker-stack.yml my_stack.
    For the Django container, if issues arise (like failing to start), check Docker logs for details.
    For running tests within Docker, ensure that your Dockerfile includes necessary test commands and execute them as part of the build process.
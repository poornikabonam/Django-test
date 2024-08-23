# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

COPY . .
RUN python -m pip install langflow -U
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN echo "from django.contrib.auth import get_user_model; \
    User = get_user_model(); \
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell



CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "myproject.asgi:application"]

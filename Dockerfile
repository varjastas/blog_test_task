FROM node:14 as build-react

WORKDIR /code/frontend

# Copy React's package.json and package-lock.json
COPY ./frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the React app
COPY ./frontend/ ./

RUN npm run build

FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy Django project
COPY . /code/

# Installing netcat required for running entrypoint.sh
RUN apt-get update && apt-get install -y netcat


# Copying entrypoint.sh and making it executable
COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

# Generating content
RUN python generate_fixtures.py

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10

# Set environment variables
ENV APP_USER=appuser \
    APP_HOME=/app

# Set up a user to run the app as
RUN adduser --disabled-password $APP_USER

# Copy the application files to the container
COPY . $APP_HOME

# Install the dependencies
RUN pip install --no-cache-dir -r ${APP_HOME}/requirements.txt

# Use a Python base image
FROM python:3

# Set the working directory in the container
WORKDIR /usr/app

COPY tests_runner/build/requirements.txt /usr/app/

# Install project dependencies
RUN pip install -r /usr/app/requirements.txt

# Copy the project files to the working directory
COPY game /usr/app/game
COPY tests /usr/app/tests

# Run the tests using pytest
CMD ["python", "-m", "pytest"]
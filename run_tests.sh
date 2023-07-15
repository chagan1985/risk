#!/bin/bash

# Build test-runner docker container
sudo docker build -t test-runner -f ./tests_runner/build/Dockerfile .

# Execute test run
sudo docker run --rm test-runner

#!/bin/bash

# Use this to run locally during development

sudo docker run -it --network=host -e ADMIN_PASSWORD=asdf --rm pupp

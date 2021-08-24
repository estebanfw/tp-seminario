#!/bin/bash
set -x
docker-compose -f docker-compose.yml up &
docker run ubuntu/testing5

#!/bin/bash
docker build -t python-image . && docker run --network=development_network -it -p 5001:5000 python-image
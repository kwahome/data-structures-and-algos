#!/usr/bin/env bash

target=${1:-.}

find . -name "*.pyc" -exec rm -f {} \;

echo "running tests in python 2..."
python2 -m unittest discover -s ${target}

echo "running tests in python 3..."
python3 -m unittest discover -s ${target}

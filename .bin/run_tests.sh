#!/usr/bin/env bash
find . -name "*.pyc" -exec rm -f {} \;

echo "running tests in python 2..."
python2 -m unittest discover -s .

echo "running tests in python 3..."
python3 -m unittest discover -s .

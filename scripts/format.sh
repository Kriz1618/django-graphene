#!/bin/bash
printf "\nRunning flake8...\n"
flake8 ./

printf "\nRunning isort...\n"
isort ./

printf "\nRunning black to format lines length...\n"
black -l 120 app/ --exclude ".*\/migrations\/.*"

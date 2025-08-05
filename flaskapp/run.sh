#!/bin/bash

# Runs the aplication
if [ $? -eq 0 ]
then
  # Executa o programa
  # echo Upgrade 
  # pip install -r requirements.txt --no-cache-dir --upgrade
  
  echo Running App: $1
  #gunicorn -w 10 -b :5000 app:app
  python $1
fi
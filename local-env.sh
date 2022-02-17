#!/bin/bash

export FLASK_APP=project
export PORT=5000
export FLASK_DEBUG=1
export SQLALCHEMY_TRACK_MODIFICATIONS=False

#alias p-run="source venv/bin/activate && python3 app.py"
alias p-run="source venv/bin/activate && flask run project"

alias p-build-image="docker image build -t maria ."
alias p-run-image='docker run -p '"$PORT"':'"$PORT"' -d --name maria_app maria'
alias p-stop-image="docker kill peek_app && docker rm maria_app"
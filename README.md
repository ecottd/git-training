### git-training
A temporary repo for training people on some git basics when working in a team

## Running the Flask app
First, build the docker image by running:
  docker build -t gittraining/flask .
from this directory. 

Then run the image using docker with a localhost port binding by running:
  docker run -p 5000:5000 gittraining/flask

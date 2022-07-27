# Git training repo
A temporary repo for training people on some git basics when working in a team

<<<<<<< HEAD
## How to use
1. Clone this repo
2. From the root of this project folder, run 'docker build -t git-training/flask:latest .'
3. From the root of this project folder, run 'docker run -p 5000:5000 git-training/flask'
4. Open your browser and browse to the flask website at http://127.0.0.1:5000

=======
## Running the Flask app
First, build the docker image by running:
  docker build -t gittraining/flask .
from this directory. 

Then run the image using docker with a localhost port binding by running:
  docker run -p 5000:5000 gittraining/flask
>>>>>>> 4d65ec4a4dcc4ef39e98cfe75e204ed5ce3dbff7

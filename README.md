## Development

1. Create a virtual environment.
2. Install the dependencies from requirements.txt.
3. Start the development server: `python app.py`.


## Production

1. Install docker.
2. Build the docker image: `docker build -t flask_app .`.
2. Run the docker container: `docker run -d --restart=always -p 80:80 -t flask_app`.
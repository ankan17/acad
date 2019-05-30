## Development

1. Create a virtual environment.
2. Install the dependencies from requirements.txt.
3. run 'python manage.py db init'
4. run 'python manage.py db migrate'
5. run 'python manage.py db upgrade'
6. Start the development server: `python app.py`.

__Create a User__: Run `python manage.py createadminuser` 
and follow the instructions.


## Production

1. Install docker.
2. Build the docker image: `docker build -t flask_app .`.
3. Run the docker container: `docker run --name flask_acad_container -d --restart=always -p 80:80 -t flask_app`.

__Create a User__: Run `docker exec -it flask_acad_container python manage.py createadminuser` 
and follow the instructions.

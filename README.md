# book-api

api for books

### setup

1. create virtualenv `python -m venv .venv`
2. activate environment:

- linux: `source .venv/bin/activate`

- windows: `.venv\Scripts\activate`

3. install dependencies `pip install -r requirements.txt`
4. run `fastapi dev main.py`


# Run from docker
1. Download and install docker
2. Startup docker on your system
3. run once `docker build -t books_api .` to build docker image
4. run `docker run -p 8000:8000 books_api` 
5. access your api on port `0.0.0.0:8000/docs`
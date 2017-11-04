FROM python:3.6

WORKDIR /usr/src/app

# Setup requirements
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pip install pipenv
RUN pipenv install --ignore-pipfile --system

# Copy api src
COPY . .

# Adding inmem db for this example
ENV DATABASE_URL "sqlite:///docker.db"
RUN python load_db.py

EXPOSE 5000

# Run api
CMD ["gunicorn", "app:app", "--bind=0.0.0.0:5000", "--worker-class=meinheld.gmeinheld.MeinheldWorker"]
FROM python:3.6.4-alpine

WORKDIR /usr/src/app

# Setup requirements
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pip install pipenv
RUN apk --update add --virtual build-base \
 && pipenv install --ignore-pipfile --system \
 && apk del build-base

# Copy api src
COPY . .

EXPOSE 5000

# Run api
CMD ["gunicorn", "app:app", "--bind=0.0.0.0:5000", "--worker-class=meinheld.gmeinheld.MeinheldWorker"]
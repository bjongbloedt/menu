FROM python:3.6

WORKDIR /usr/src/app

# Setup requirements
COPY requirements requirements
RUN pip install --no-cache-dir -r requirements/prod.txt

# Copy api src
COPY . .

EXPOSE 5000

# Run api
CMD ["gunicorn", "app:app", "--bind=0.0.0.0:5000", "--worker-class=meinheld.gmeinheld.MeinheldWorker"]
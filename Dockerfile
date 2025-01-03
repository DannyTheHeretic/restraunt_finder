FROM python:3.13

ENV PYTHONUNBUFFERED=1

RUN mkdir /requirements
WORKDIR /requirements
COPY requirements.txt /requirements/
RUN pip install -r requirements.txt

RUN mkdir /code
WORKDIR /code

# Expose the port Gunicorn will listen on
EXPOSE 8000

# Run Gunicorn when the container starts
CMD ["gunicorn", "restaurant_core.wsgi:application", "-b", "0.0.0.0:8000"]
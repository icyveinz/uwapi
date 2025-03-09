FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /django_web

COPY . /django_web

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/django_web

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8001", "django_web.wsgi:application"]
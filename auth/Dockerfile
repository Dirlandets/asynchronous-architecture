FROM python:3.9-slim as base

ARG HOMEDIR=/app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
    pipenv install --deploy --system --ignore-pipfile --dev

WORKDIR ${HOMEDIR}

COPY . ${HOMEDIR}

EXPOSE 8000

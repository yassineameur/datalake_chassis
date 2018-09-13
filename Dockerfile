FROM python:3.6
LABEL maintainer="yassine"

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

# Airflow
ARG AIRFLOW_VERSION=1.10.0
ENV AIRFLOW_HOME=/opt/app

RUN apt-get update && \
    apt-get install libgeos-dev -y && \
    pip install --upgrade pip

WORKDIR ${AIRFLOW_HOME}

COPY requirements.txt .

# Needed by airflow to avoid a dependency installation
ENV SLUGIFY_USES_TEXT_UNIDECODE yes

RUN pip install -r requirements.txt

COPY airflow.cfg .
COPY dags/ dags/
COPY plugins/ plugins/
COPY tests/ tests/
COPY tools/ tools/

ENV PYTHONPATH=.

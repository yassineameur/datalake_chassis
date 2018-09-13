# datalake_chassis

This project is a chassis for any airflow project with a celery executor (most production-grade airflow's executor). It is mainly destined for those who are interested in airflow and want to test it quickly without spending much time on configuration.

## Requirements:
In order to use this chassis, you need to install:
   - docker
   - docker-compose
   - python 3.6 or +

## Docker
This chassis contains two docker-compose files that will help you to launch your dags and see them executing tasks.
- `docker/infra.yml`: This file contains the definition of the two following containers:
   - `Postgres` container that contains the airflow' metadata database.
   - `Rabbimq` container that contains rabbitmq running with a vhost named `airflow` and a user named also `airflow`. We will be using rabbitmq as a broker for airflow's worker.

- `docker/airflow.yml`: This file contains the three following containers:
   - `webserver`: airflow's webserver mapped on port 8080
   - `scheduler`: airflow's scheduler
   -  `worker`: airflow's worker

## Before developing:

- Before starting developing your dags, you need to run your infra docker-compose file:
`docker-compose -f docker/infra.yml up -d`

## When developing
- To develop your dags, you can:
  - Add plugins: hooks and operators in the folder plugins (see airflow's documentation for more details)
  - Add dags in the folder `dags`
  - Add your new dependencies to the file `requirements.txt`

## After developing
- After developing your dags, to see them working, you have two options:

1) Launch dags locally:
   - Create a virtual environment
   - Install dependencies: `docker-compose -f docker/infra.yml up -d`
   - Add the two following env variables to your `~/.bash_profile`:
       - export `AIRFLOW_HOME`=`absolute_path_to_your_project`
       - export `AIRFLOW_HOME`=`absolute_path_to_your_project` (This is needed so that airflow can load your plugins)
   - source your `~/.bash_profile`
   - Initiate airflow's metadata database: `airflow initdb`
   - open three terminals and launch those three commands:
       - `airflow webserver`
       - `airflow scheduler`
       - `docker/airflow.yml`

   And finally open `localhost:8080` on your browser: Tadaa !! You must see your dags running !!

2) Launch dags on docker containers:
   - Build a docker image of your project: `docker build --no-cache -t airflow .`
   - Run airflow containers: `docker-compose -f docker/airflow.yml up -d`
   - Open `localhost:8080` to see your dags running.

If you want to deploy your project to google kubernetes, you can use those docker-compose files with some modifications:
- After building your airflow's docker image, push it to your docker hub repository.
- In the file `docker/airflow.yml`, replace the local airflow's image name by the one you have just pushed.


## Why I have done this project:
While trying to use airflow with a celery executor, I have spent a lot of time on configuration problems. I have read a lot of articles, debugged many problems and seen many other projects suggesting some complex solutions to small problems. I was badly annoyed by this and wanted to make it simpler for those who want to discover this wonderful tool.
As a matter of fact, airflow is really an amazing technology and I found it really bad that many people (especially non-technical profiles) let it down because they were stuck on configuration problem.





# Metabase + MySQL workbench

This repository has Metabase running with MySQL as the application database and also connects to a MySQL database for testing

## Components

- Nginx as a reverse proxy (sends traces to Tempo) + it's prometheus exporter
- Metabase (exposing prometheus metrics + exposing JMX telemetry + Java OTEL that sends traces to Tempo)
- Tempo (for capturing traces)
- Prometheus
- Grafana
- API (which captures Metabase log lines and adds a few things to send to Loki)
- Loki
- ProxySQL (just for testing), can be disabled
- MySQL as the App DB (can switch between MySQL and MariaDB)
- MySQL (data 2). To create tables and play with some data via Metabase. Can be disabled
- MySQL with SSL. Can be disabled, this was there just to do some testing with MySQL and SSL
- Setup container: does the setup of Metabase
- MySQL sample database: this gets connected on the setup of Metabase
- Maildev: just an email server
- Commented out singlestore: just to test this engine
- MySQL Prometheus exporter: currently getting metrics out of the App DB, but you can add any other exporter to test other DBs in the stack

## How to run

Install docker + do a `docker compose run --build`

### Need to change the Metabase version?

Just change the version on the metabase container, wipe the mysql-data folder and just do again `docker compose run --build`


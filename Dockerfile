FROM python:3.8-alpine

ARG DEPLOY_ENV
ENV DEPLOY_ENV ${DEPLOY_ENV}
RUN pip install -r requirements.txt
RUN python app.py

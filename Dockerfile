# syntax=docker/dockerfile:1
# FROM node:18-alpine
FROM python:3.8
COPY src/ ./src/
RUN pip install flask_login
RUN pip install psycopg2
RUN pip install pycryptodome
CMD ["python", "src/backend/appserver.py"]
FROM python:3.11.1
COPY src/ ./src/
RUN pip install -r src/backend/requirements.txt
CMD ["python", "src/backend/appserver.py"]
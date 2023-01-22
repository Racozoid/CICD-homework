FROM python:3.9-slim-buster
ADD . /python-homework
WORKDIR /python-homework
RUN pip install -r requirements.txt
CMD ["python", "./main.py"]
FROM python:3.7
ADD ./requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt

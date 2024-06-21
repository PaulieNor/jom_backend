FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend
COPY requirements.txt /backend/
EXPOSE 8000
RUN pip install .
COPY . /backend/


ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
FROM python:3.10

# set work directory
WORKDIR /usr/src/literature

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./req.txt /usr/src/req.txt
RUN pip install -r /usr/src/req.txt

COPY . /usr/src/literature

EXPOSE 8000
CMD ["python","manage.py","runserver"]
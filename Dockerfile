# used image
FROM python:stretch
# Workspace options.
COPY . /app
WORKDIR /app
# Installation required library.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# server and start parameter
ENTRYPOINT ["gunicorn", "-b", ":8080", "main:APP"]


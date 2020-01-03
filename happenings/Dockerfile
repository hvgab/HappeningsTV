FROM python:3.8.0-alpine

WORKDIR /usr/src/app

# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# "Host" dependencies for app
# TODO: Delete build deps after installing and building stuff.
# Pillow
RUN apk add --no-cache build-base python-dev py-pip jpeg-dev zlib-dev musl-dev
# https://github.com/python-pillow/Pillow/issues/1763
ENV LIBRARY_PATH=/lib:/usr/lib

# MySQL
RUN apk add --no-cache mariadb-dev

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copy Project
COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
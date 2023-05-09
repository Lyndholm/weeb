FROM python:3.11.3-alpine

WORKDIR /usr/src/weeb

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/weeb/entrypoint.sh
RUN chmod +x /usr/src/weeb/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/weeb/entrypoint.sh"]

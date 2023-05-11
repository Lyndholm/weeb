FROM nginx:1.23-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY robots.txt /usr/share/nginx/html/robots.txt

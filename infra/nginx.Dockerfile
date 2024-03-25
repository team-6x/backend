FROM nginx:1.25
COPY infra/nginx.conf /etc/nginx/conf.d/default.conf

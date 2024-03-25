FROM nginx:1.25
COPY infra/nginx.conf /etc/nginx/templates/default.conf.template

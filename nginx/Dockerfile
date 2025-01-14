FROM nginx:latest

# remove the default configuration
RUN rm /etc/nginx/conf.d/default.conf

# copy the configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# expose the port
# EXPOSE 80

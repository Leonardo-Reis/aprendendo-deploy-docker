FROM python
WORKDIR /application
COPY . .
RUN apt update
RUN apt install apache2 -y
RUN apt install apache2-dev -y
RUN pip install mod_wsgi
RUN pip install flask
ENTRYPOINT mod_wsgi-express start-server wsgi.py
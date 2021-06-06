FROM tiangolo/meinheld-gunicorn-flask:python3.7-2019-10-15

COPY ./app /app

# ### Set environment variables for deployment ###
ENV APP_MODULE main:app
ENV WORKERS_PER_CORE 2
ENV BIND 0.0.0.0:80
ENV LOG_LEVEL debug

# ### Install dependencies ###
RUN pip install -r requirements.txt

# ### Set FLASK_APP env variable ###
ENV FLASK_APP main.py

ENV LISTEN_PORT 80

EXPOSE 80
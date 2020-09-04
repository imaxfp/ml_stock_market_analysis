FROM python:3.7
MAINTAINER "imaxfp@gmail.com"
RUN mkdir stock
COPY . /stock
WORKDIR /stock
RUN pip install -r requirements.txt
RUN ls -la
WORKDIR /stock/src
RUN ls -la
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["app.py"]

#CMD gunicorn --worker-class gevent --workers 1 --bind 0.0.0.0:5001 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
#CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
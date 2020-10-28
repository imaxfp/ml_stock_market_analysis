##################### dependent base image with requerements #####################
FROM python:3.8 AS ml_similarity_base
COPY ./requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
#RUN pip install pip3
RUN pip3 install streamlit \
    && pip3 install -r requirements.txt

##################### dependent ml app #####################
FROM ml_similarity_base AS ml_similarity_app
ENV PYTHONPATH "${PYTHONPATH}" \
    + ":/usr/local/bin/python3.8" \
    + ":/app"

RUN mkdir app
COPY . /app
WORKDIR /app/src

EXPOSE 8501
RUN ls -la
#CMD ["streamlit run --server.port 5000 app_streamlit.py"]
CMD ["streamlit", "run", "app_streamlit.py"]


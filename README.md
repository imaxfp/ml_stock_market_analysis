# Stock market analysis based on ML/AI #
# Similarity analysis "finance, real estate, etc..."


#### Setup
pip install networkx
pip install -U pip
python3 -m pip install streamlit

#### Run 
streamlit run app_streamlit.py

#### Debug 
/Library/Frameworks/Python.framework/Versions/3.8/Resources/Python.app/Contents/MacOS/Python /Library/Frameworks/Python.framework/Versions/3.8/bin/streamlit run app_streamlit.py

##### How to build docker 

1. build base docker image with all dependencies
docker build --target ml_similarity_base -t ml-similarity-base:latest .
2. Build container with app
docker build --target ml_similarity_app -t ml_similarity_app:latest .


##### With docker-compose
docker-compose up
docker-compose stop
docker-compose up -d --build

##### Run the Docker container using the command shown below.
docker run -p 8501:8501 ml_similarity_app
http://localhost:8501/


##### Docker run and attach into container 
docker run --entrypoint "/bin/sh" -it ml-similarity-base

##### Docker attach
https://phase2.github.io/devtools/common-tasks/ssh-into-a-container/
docker exec -it <container name> /bin/bash

#### Remove 
1. images: 
docker rmi
2. containers:
docker rm $(docker ps -aq)
docker system prune



#### Setup python

ls -l /usr/local/bin/python*


#### MARKS 
https://kanoki.org/2020/07/04/create-interactive-dashboard-in-python-using-streamlit/


#### STEPS
1. Similarities detection
2. Features importance detection
https://towardsdatascience.com/feature-selection-techniques-in-machine-learning-with-python-f24e7da3f36e#:~:text=using%20SelectKBest%20class-,2.,feature%20towards%20your%20output%20variable.
HEATMAP - (or heatmap) is a data visualization technique that shows magnitude of a phenomenon as color in two dimensions.

#### Feature engineering 
https://www.kaggle.com/willkoehrsen/start-here-a-gentle-introduction
https://towardsdatascience.com/formatting-tips-for-correlation-heatmaps-in-seaborn-4478ef15d87f
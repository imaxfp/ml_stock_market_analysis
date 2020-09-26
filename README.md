# Stock market analysis based on ML/AI #
# Similarity analisys "finance, real estate, etc..."


#### Setup
pip install networkx
pip install -U pip
python3 -m pip install streamlit

#### Run 
streamlit run app_streamlit.py

#### Debug 
/Library/Frameworks/Python.framework/Versions/3.8/Resources/Python.app/Contents/MacOS/Python /Library/Frameworks/Python.framework/Versions/3.8/bin/streamlit run app_streamlit.py

#### How to run 
```bash
docker build -t ml-stock-market-analysis:latest .
```
Run the Docker container using the command shown below.

```bash
docker run -p 5000:5000 ml-stock-market-analysis
``` 

Remove all containers
```bash
docker rm $(docker ps -aq)
```

#### Setup python
```
ls -l /usr/local/bin/python*
```

#### MARKS 
https://kanoki.org/2020/07/04/create-interactive-dashboard-in-python-using-streamlit/


#### STEPS
1. Similarities detection
2. Features importance detection
https://towardsdatascience.com/feature-selection-techniques-in-machine-learning-with-python-f24e7da3f36e#:~:text=using%20SelectKBest%20class-,2.,feature%20towards%20your%20output%20variable.
HEATMAP - (or heatmap) is a data visualization technique that shows magnitude of a phenomenon as color in two dimensions.


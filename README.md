# Stock market analysis based on ML/AI #


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
docker build -t new-or-used-ml-build .
docker run -d -p 84:80 --name new-or-used-api new-or-used-ml-build
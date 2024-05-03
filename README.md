# SynthCT
Synthetic CT Generation from MRI Scan
Experiment 8
FROM nginx:alpine
COPY index.html /usr/share/nginx/html
EXPOSE 80


//comments to run
docker build -t name .

docker run -p 8080:80 name 

-----------------------------------------------------------------------------
Experiment 9

Docker login 

docker build -t your_directory_name:tag_name .

docker images

docker tag image_id docker_hub_username/repository_name:tag_name

docker push docker_hub_username/repository_name:tag_name

docker pull docker_hub_username/repository_name:tag_name


----------------------------------------------------------------------------
Experiment 10

version: '3'
services:
    web1:
      image: nginx:latest
      ports:
        - '8085:80'
    web2:
      image: sample
      ports:
         - '8086:80'

docker compose up
---------------------------------------------------------------------------
Experiment 11 Swarm


docker swarm init

docker service create --name webapp --replicas 3 -p 8080:80 nginx

docker service scale webapp=5

docker service update --image nginx:1.19.8 webapp

Docker services ls –filter name=webapp

Docker swarm leave –force
---------------------------------------------------------------------------
Experiment 11 Minikube 

install kubernets

curl.exe -LO "https://dl.k8s.io/release/v1.30.0/bin/windows/amd64/kubectl.exe"

install minikube 

winget install minikube

minikube start

kubectl cluster-info

kubectl create deployment nginx-deployment --image=nginx


kubectl get pods

kubectl expose deployment nginx-deployment --port=80 --type=NodePor

Kubectl get pods –all-namespaces


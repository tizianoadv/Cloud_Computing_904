kubectl describe ksvc monitor
kubectl get ksvc monitor
kubectl apply -f function.yml
kubectl create secret docker-registry regcred --docker-server=docker.io --docker-username=tiziadv --docker-password=--docker-email=tiziano.naance@gmail.com
kubectl get secrets --all-namespacesB1777
kubectl get secrets
minikube profile list
minikube tunnel --profile knative
kn quickstart minikube
kubectl get pods --namespace knative-serving
kubectl get pods --namespace default
kubectl get knative
kubectl get service

kubectl apply -f dns-reader-binding.yaml
kubectl auth can-i get services/kube-dns:dns --namespace kube-system --as system:authenticated

kubectl exec -it monitor-deployment-5f968c5c7c-fx9p2 -- bash
kubectl get pods
kubectl port-forward monitor-deployment-5f968c5c7c-fx9p2 8888:8080


docker build -t monitor -f Dockerfile.function .
docker tag monitor:latest tizianoadv/monitor:latest
docker push tizianoadv/monitor:latest
kubectl get pods
kubectl delete pods

kubectl get node --output 'jsonpath={.items[0].status.addresses[0].address}'
kubectl get svc monitor-deployment --namespace default --output 'jsonpath={.spec.ports[?(@.port==8080)].nodePort}'
http://192.168.49.2:30116/data
kubectl get ksvc monitor-deployment --output=custom-columns=NAME:.metadata.name,DOMAIN:.status.domain

curl -X POST -H "Content-Type: application/json" -d "{\"timestamp\": \"2022-03-15T15:30:00\", \"temperature\":\"25.5\", \"humidity\": \"60\"}" http://localhost:8888/data

curl -X POST -H "Content-Type: application/json" -d '{"temperature": 25.67, "humidity": 60.34, "luminosity": 32.45, "timestamp": "2023-03-16 12:34:56"}' http://localhost:8888/data

minikube tunnel
minikube tunnel --cleanup

CDR - Knative serving installation
kubectl apply --filename https://github.com/knative/serving/releases/download/v0.26.0/serving-crds.yaml

kubectl expose deployment monitor-deployment --port=8080 --type=NodePort

kn service update database-service --image=redis:latest
kn service update monitoring-service --image=docker.io/tizianoadv/monitor:latest
kn service delete monitoring-service
kn service create monitoring-service --image=docker.io/tizianoadv/monitor:latest



minikube ip

dashboard not working 
https://github.com/microsoft/WSL/issues/4199#issuecomment-668270398



brew tap knative-sandbox/kn-plugins
brew install func


# Install knative CLI & Knative cluster using minikube
https://knative.dev/docs/install/quickstart-install/


docker build -t monitor -f Dockerfile.function .
docker tag monitor:latest tizianoadv/monitor:latest
docker push tizianoadv/monitor:latest
kn service delete database-service
kn service delete monitoring-service
kubectl apply -f database-service.yaml
kubectl apply -f monitoring-service.yaml
kn service list

kubectl logs -l serving.knative.dev/service=monitoring-service -f
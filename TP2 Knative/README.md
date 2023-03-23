# Monitoring application - IoT 

The application aims to create a serverless function to store and retrieve data in real-time. It uses the Knative framework and the Kubernetes Minikube cluster simulator to facilitate the deployment and management of the application. Data storage is provided by a Redis database. Redis was chosen for its ease of use and ability to store real-time data. The application is developed in Python and uses Flask to create a RESTful API that will allow the user to retrieve data stored in the Redis database in the form of JSON files. The entire system is deployed in a local environment using Minikube.

## Prerequisites

Follow the steps mentioned in the official [Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/) to install Kubernetes CLI

Follow the steps mentioned in the official [Knative documentation](https://knative.dev/docs/install/quickstart-install/) to install Knative CLI & Knative cluster using minikube.

# Memo

## Install Knative func 
```Bash
brew tap knative-sandbox/kn-plugins
brew install func
```
## Minikube Useful Commands
Use the following Minikube commands:

- `minikube profile list` - List all available profiles
- `minikube ip` - Get IP address of the Minikube cluster
- `minikube tunnel` - Create a tunnel to services inside a cluster
- `minikube tunnel --cleanup` - Remove stale tunnel processes
- `minikube tunnel --profile knative` - Create a tunnel to services inside a Knative cluster

## Kubectl Useful Commands
- `kubectl get pods`: This command retrieves information about the pods running in the current Kubernetes cluster.
- `kubectl delete pods`: This command deletes one or more pods from the current Kubernetes cluster.
- `kubectl create secret docker-registry regcred --docker-server=docker.io --docker-username=<user> --docker-password=<pwd> --docker-email=<email>`: This command creates a secret for a Docker registry that can be used to authenticate with the registry when pulling images.
- `kubectl get secrets`: This command retrieves information about the secrets in the current Kubernetes cluster.
- `kubectl auth can-i get services/kube-dns:dns --namespace kube-system --as system:authenticated`: This command checks if the current user has permission to retrieve information about the kube-dns service in the kube-system namespace.
- `kubectl get node --output 'jsonpath={.items[0].status.addresses[0].address}'`: This command retrieves the IP address of the first node in the current Kubernetes cluster.
- `kubectl get svc <deployment> --namespace <namespace> --output 'jsonpath={.spec.ports[?(@.port==8080)].nodePort}'`: This command retrieves the node port associated with the specified deployment and namespace.
- `kubectl get ksvc <deployment> --output=custom-columns=NAME:.metadata.name,DOMAIN:.status.domain`: This command retrieves the name and domain of the specified Knative service.
- `kubectl exec -it <pod> -- bash`: This command executes a shell command inside the specified pod.
- `kubectl expose deployment <deployment> --port=<port> --type=NodePort`: This command exposes the specified deployment as a service with the specified port and type.
- `kubectl port-forward <pod> 8888:8080`: This command forwards traffic from the local machine to the specified pod.
- `kubectl apply -f <manifest>`: This command creates or updates Kubernetes resources in the specified manifest file.
- `kubectl logs -l serving.knative.dev/service=<service> -f`: This command retrieves the logs for the specified Knative service.
- `kubectl logs <deployment> -c <container>`: This command retrieves the logs for the specified container within the specified deployment.
- `kubectl get pods --namespace <namespace>`: This command retrieves information about the pods in the specified namespace.
- `kubectl describe ksvc <pod>`: This command retrieves detailed information about the specified Knative service.
- `kubectl get ksvc <pod>`: This command retrieves information about the specified Knative service.

## Useful Knative commands

- `kn service update <service> --image=<image>`: This command updates the image associated with the specified Knative service.

- `kn service delete <service>`: This command deletes the specified Knative service.

- `kn service create <service> --image=<image>`: This command creates a new Knative service with the specified image.

- `kn service list`: This command lists all Knative services running in the current Kubernetes cluster.

## Possible issue - Dashboard not working
Follow the steps [Dashboard not working](https://github.com/microsoft/WSL/issues/4199#issuecomment-668270398) to fix the dashboard issue.

## Knative Useful commands
- `kn service update <service> --image=<image>`: Update a Knative service with a new image
- `kn service delete <service>`: Delete a Knative service
- `kn service create <service> --image=<image>`: Create a new Knative service with a specified image
- `kn service list`: List all Knative services

## Docker Useful Commands
- `docker build -t <repo:tag> -f <dockerfile> .`:  Build the image with the given tag and Dockerfile
- `docker tag <repo:tag> <username/repo:tag>`:  Push a custom Docker image to a registry
- `docker push <username/repo:tag>`:  Push the tagged image to the registry



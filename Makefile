build:
	docker build -t hariharan26/iris-ml:latest .
	docker push hariharan26/iris-ml:latest

run:

	docker run -d --name ml-k8s-demo -p 9000:5000 hariharan26/iris-ml:latest

deploy:
	minikube start
	kubectl apply -f k8s/deployment.yaml
	kubectl apply -f k8s/service.yaml

clean:
	docker rmi hariharan26/iris-ml:latest
	docker rm -f ml-k8s-demo || true
	kubectl delete -f k8s/deployment.yaml
	kubectl delete -f k8s/service.yaml
	minikube stop

url:
	minikube service iris-service --url

format:
	ruff check . --fix
	ruff format .
	ruff format --check .

pytest:
	pytest

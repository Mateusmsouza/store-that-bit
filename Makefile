settup-cluster:
	k3d cluster create --config IaaC/kubernetes/cluster.yml
	export KUBECONFIG=$(k3d kubeconfig get store-that-bit)
	docker build . -f IaaC/docker/Dockerfile.dev -t store-that-bit --no-cache
	k3d image import store-that-bit -c store-that-bit
	kubectl apply -f IaaC/kubernetes/deployments/store-that-bit.yml

destroy-cluster:
	k3d cluster delete --config IaaC/kubernetes/cluster.yml

build-image:
	docker build . -f IaaC/docker/Dockerfile.prod -t store-that-bit --no-cache

dev-environment:
	docker build . -f IaaC/docker/Dockerfile.dev -t store-that-bit-dev --no-cache
	docker run -d -p 8000:8000 store-that-bit

dev-watch:
	docker logs store-that-bit

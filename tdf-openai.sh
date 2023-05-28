DOCKER_IMAGE_NAME=tbnsok/my-fastapi-image
DOCKER_IMAGE_TAG=latest

docker build -t $DOCKER_IMAGE_NAME/$DOCKER_IMAGE_TAG .

# Push the Docker image to the Docker Hub registry
docker push $DOCKER_IMAGE_NAME/$DOCKER_IMAGE_TAG

echo "DONE"
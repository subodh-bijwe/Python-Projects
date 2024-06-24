### Docker Commands

1. **docker run \<image\> [command]**
   - Creates and starts a new container from the specified image.
   - Example: `docker run ubuntu`

2. **docker ps**
   - Lists all running containers.
   - Example: `docker ps`

3. **docker ps -a**
   - Lists all containers (running and stopped).
   - Example: `docker ps -a`

4. **docker pull \<image\>**
   - Pulls an image from a registry (default is Docker Hub).
   - Example: `docker pull nginx`

5. **docker build -t \<image-name\> <path>**
   - Builds a Docker image from a Dockerfile.
   - Example: `docker build -t myapp .`

6. **docker images**
   - Lists all images on the local machine.
   - Example: `docker images`

7. **docker stop \<container\>**
   - Stops a running container.
   - Example: `docker stop mycontainer`

8. **docker start \<container\>**
   - Starts a stopped container.
   - Example: `docker start mycontainer`

9. **docker restart \<container\>**
   - Restarts a running or stopped container.
   - Example: `docker restart mycontainer`

10. **docker rm \<container\>**
    - Removes a stopped container.
    - Example: `docker rm mycontainer`

11. **docker rmi \<image\>**
    - Removes an image.
    - Example: `docker rmi myimage`

12. **docker exec -it \<container\> <command>**
    - Executes a command inside a running container.
    - Example: `docker exec -it mycontainer bash`

13. **docker inspect \<resource\>**
    - Displays detailed information about a Docker resource (container, image, network, etc.).
    - Example: `docker inspect mycontainer`

14. **docker logs \<container\>**
    - Fetches the logs of a container.
    - Example: `docker logs mycontainer`

15. **docker network ls**
    - Lists all networks.
    - Example: `docker network ls`

16. **docker network create \<network\>**
    - Creates a new network.
    - Example: `docker network create mynetwork`

17. **docker network connect \<network\> \<container\>**
    - Connects a container to a network.
    - Example: `docker network connect mynetwork mycontainer`

18. **docker network disconnect \<network\> \<container\>**
    - Disconnects a container from a network.
    - Example: `docker network disconnect mynetwork mycontainer`

19. **docker-compose up**
    - Starts services defined in a `docker-compose.yml`.
    - Example: `docker-compose up`

20. **docker-compose down**
    - Stops and removes containers, networks, volumes, and images created by `docker-compose up`.
    - Example: `docker-compose down`

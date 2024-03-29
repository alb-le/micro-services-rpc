# RPC service using a microservices architecture
## How to
To run this project, you should have installed the latest docker. Then, just run the following in the project root:
```
docker compose up
```
After docker finishes up, open the client in a new tab:
```
docker exec -it micro-services-rpc-client-1 python3 client_handler.py
```

Usuly the client container name is ```micro-services-rpc-client-1 ``` but it can change. To look up the container name, just run ```docker container ls```.

## Video
You can see a [video of the RPC in action](https://youtu.be/HKxhMgp4-vA).

## Intro
This project originates from the 2023 Computer Network curse from UnB (Universidade de Brasília). It's divided in four
different projects: an RPC Client, a Proxy Server and two servers to compute the requests.

About Docker, containers are a technology similar to virtualization (VMWare, VirtualBox, QEMU, Hyper-V), but only
the User part is virtualized, allowing the same system to behave like a range of systems,
using your own package manager, dependency versions, environment settings and everything else.
This technology has increasingly grown in popularity, as it allows reproducibility of environments and
prevent applications from interfering with each other, something common in non-isolated environments, exposing only the
ports referring to services offered to the external network.
## Motivation
Each student must create a docker-compose.yml file that defines multiple complementary services
or interdependent with each other, as they would do in a commercial application. The file, containing at least 4
services, must be submitted together with a report explaining the reason for choosing the services, how they were
configured to interconnect your services, and how it can be used in a real situation (e.g. business).
The link to a video presentation with the student using the services must also be provided
hosted in the containers.

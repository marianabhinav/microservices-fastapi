# Description
This project contains 2 Microservices:
> Service A

> Service B

Both services are implemented using the [Multitier architecture](https://en.wikipedia.org/wiki/Multitier_architecture) aligning with the design principle of [Sepration of Concerns(SoC)](https://en.wikipedia.org/wiki/Separation_of_concerns). Other design patterns like [Singleton](https://en.wikipedia.org/wiki/Singleton_pattern) have been used for database access.

For authentication between the services, we have used the Bearer token scheme. A JWT token is created using `RS256` **asymmetric encryption**. These public & private keys are currently maintained in the code, ideally, they should be moved to a vault where we should maintain them in rotation.  
This implementation has been used to keep simplicity in perspective. In an ideal scenario, we can also create a dedicated `auth service` which will issue and verify the tokens.  

A config file `ConfigFile.properties` is maintained which contains environment variables. Both the services have a copy of these files which should be synchronized. For now, we can pick this properties file from the outer folder which dockerizing the solutions or when starting the services.  

## Workflow
When Service A gets a **POST** request on `/addDocument` endpoint its saves the request body in the database. And makes an authenticated **POST** request on Service B `/addSkills` endpoint with skills mentioned as part of `/addDocument` request body.  
This call is a loosely coupled call and the response of Service A does not depend on the response from Service B.

# Database
DAO layer accesses the database. For now, a simple implementation has been done by maintaining DB in a CSV file.

# Logging/Monitoring
Both the services have logging implemented on several checkpoints. All the logs for the service are dumped into a log file with a timestamp. These log files can further be used for monitoring purposes as well with tools like [Splunk](https://www.splunk.com/) or [Sumologic](https://www.sumologic.com/).  Although I do believe that more verbose logging could have been achieved.

# Hosting
Both the services have a docker file associated with them which can then further be used to dockerize the solutions.

## Steps to Dockerize
Go to the respective folder of the service. Eg:  
```bash
cd service_a
```
Then build the docker image by command:  
```bash
docker build -t service_a:v1 ./
```
**Note:** v1 stands for version number for the image and can be varied as per the build.  

Once the build process is complete, this docker image can be run in a container using the command:  
```bash
docker run -p 8001:8001 service:v1
```
**Note:** 8001 stands for the port number that needs to be forwarded from the docker. In this case, the default port number for service_a was 8001 which needs to be forwarded to the same port number. This should be changed as per the server port number.  

# Scalability
These docker images can be used with a container-orchestration system like [Kubernetes](https://kubernetes.io/) for achieving **CI/CD** and auto-scaling.  
Hence, with this current solution, we have achieved scaling on the **x-axis** as well as **y-axis** of the [Scale Cube](https://microservices.io/articles/scalecube.html) which makes this solution highly-scalable.

# Documentation
Both the services have Swagger documentation available. Please refer to individual readme files.  

# Deployement
Since, both the services are containerized solutions we can easily create a CI/CD pipeline using [Jenkins](https://www.jenkins.io/) or [GitLab](https://docs.gitlab.com/ee/ci/) and create a dockerized image which then can further be deployed.
# Run mysql
docker-compose -f mysql/mysql.yml up -d

# Run cluster
cd vagrant-kubernetes && vagrant up

# Run app
cd python-app && docker build -t python-image . && docker run --network=development_network -d -p 5001:5000 python-image

I created a Jenkinsfile as a example of ci/ci pipeline. First test the code, if it is passing. 
Secondly, check Dockerfile, build and push the registry. Then check helm charts, push the helm registry.
Finally, if user approve the deployment to production, or it can be removed, run helm install in cluster. 
It is similar to continuous delivery.


# Folder aws-node-example
Also i have a Circle CI pipeline on AWS which have create infrastructure, deploy application. 

# Folder helm-mysql
Also i created a helm chart with specific configuration for mysql.

# Folder jenkins-agent-base
Also i created a base image for jenkins agents.

# Folder mysql
Also i created a docker-compose file to run mysql.

# Folder python-app
I created a ci/ci pipeline for an application you gave.

# Folder vagrant-kubernetes
Also i created a k8s cluster with vagrant


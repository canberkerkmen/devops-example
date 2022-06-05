FROM jenkins/agent:jdk8@sha256:d006ddecbd0d77ffcafb1025b61683a0f74d4ad4345d36dcf08be16fb7e0e891

USER root
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates curl

#Add Google Cloud public signing key
RUN curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg

#Set up the repository
RUN echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list

#Install Kubectl
RUN apt-get update && apt-get install -y kubectl

#Install Helm
RUN curl -O https://get.helm.sh/helm-v3.9.0-linux-amd64.tar.gz && tar -xvzf helm-v3.9.0-linux-amd64.tar.gz && cp linux-amd64/helm /usr/bin

USER jenkins

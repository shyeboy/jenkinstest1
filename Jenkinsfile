pipeline {
  agent any

  environment {
    DOCKER_REGISTRY = "docker.io"
    DOCKER_IMAGE = "kimsunghyun26/final_project"
    ACR_NAME = "kimsunghyun26/final_project:V3"
    AKS_NAME = "aks-1"
    RESOURCE_GROUP = "test_rg"
    AZURE_CREDENTIAL_ID = "08a5b32e-6669-4195-8b61-da1961a0caaf"
    K8S_NAMESPACE = "default"
    K8S_DEPLOYMENT_NAME = "was"
    K8S_CONTAINER_NAME = "kimsunghyun26/final_project:V3"
  }
  stages {
    stage('Build Docker image') {
      steps {
        script {
          sh "docker build -t ${DOCKER_IMAGE} ."
        }
      }
    }
    stage('Tag Docker image') {
      steps {
        script {
          sh "docker tag ${DOCKER_IMAGE} ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:V3"
        }
      }
    }
    stage('Push Docker image to Docker Hub') {
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'kimsunghyun26', passwordVariable: 'ksh31010!@')]) {
            sh "docker login -u kimsunghyun26 -p ksh31010!@"
            sh "docker push ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:V3"
          }
        }
      }
    }
/
}
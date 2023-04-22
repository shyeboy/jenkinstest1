pipeline {
  agent any
  environment {
    DOCKER_REGISTRY = "docker.io"
    DOCKER_IMAGE = "kimsunghyun26/final_project"
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
          sh "docker tag ${DOCKER_IMAGE} ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:V2"
        }
      }
    }
    stage('Push Docker image to Docker Hub') {
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'kimsunghyun26', passwordVariable: 'ksh31010!@')]) {
            sh "docker login -u kimsunghyun26 -p ksh31010!@"
            sh "docker push ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:V2"
          }
        }
      }
    }
  }
}






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
          sh "docker tag ${DOCKER_IMAGE} ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${BUILD_NUMBER}"
        }
      }
    }
    stage('Push Docker image to Docker Hub') {
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
            sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
            sh "docker push ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${BUILD_NUMBER}"
          }
        }
      }
    }
  }
}






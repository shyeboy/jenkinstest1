 pipeline {
  agent any

  environment {
  DOCKER_USERNAME = credentials('dockerhub').username
  DOCKER_PASSWORD = credentials('dockerhub').password
  }

  stages {
    stage('Build Docker image') {
      steps {
        script {
          def imageName = "kimsunghyun26/final_project"
          sh "docker build -t kimsunghyun26/final_project ."
          sh "docker tag kimsunghyun26/final_project hyeran0920/project:v12"
        }
      }
    }

    stage('Push Docker image to Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'kimsunghyun26', passwordVariable: 'ksh31010!@')]) {
          script {
            def imageName = "kimsunghyun26/final_project"
            sh "docker login -u kimsunghyun26 -p ksh31010!@"
            sh "docker push hyeran0920/project:v12"
          }
        }
      }
    }
  }
}




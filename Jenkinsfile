pipeline {
  agent any

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
        withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
          script {
            def imageName = "kimsunghyun26/final_project"
            sh "docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD"
            sh "docker push hyeran0920/project:v12"
          }
        }
      }
    }
  }
}





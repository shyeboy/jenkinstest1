pipeline {
  agent any

  stages {
    stage('Build Docker image') {
      steps {
        script {
          def imageName = "kimsunghyun26/final_project"
          sh "docker build -t ${hyeran0920/project:v11} ."
          sh "docker tag ${hyeran0920/project:v11} ${hyeran0920/project:v11}:latest"
        }
      }
    }

    stage('Push Docker image to Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'kimsunghyun26', passwordVariable: 'ksh31010!@')]) {
          script {
            def imageName = "kimsunghyun26/final_project"
            sh "docker login -u ${kimsunghyun26} -p ${ksh31010!@}"
            sh "docker push ${hyeran0920/project:v11}:latest"
          }
        }
      }
    }
  }
}

pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "docker.io"
        DOCKER_HUB_USERNAME = credentials("kimsunghyun26")
        DOCKER_HUB_PASSWORD = credentials("ksh31010!@")
        DOCKER_IMAGE_NAME = "hyeran0920/project"
        DOCKER_IMAGE_TAG = "v12"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} -f ./Dockerfile ."
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry("${DOCKER_REGISTRY}", "Dockerhub") {
                        def dockerImage = docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}")
                        dockerImage.push()
                    }
                }
            }
        }
    }
    
    post {
        always {
            sh "docker rmi -f ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}"
        }
    }
}

def credentials(credentialsId) {
    return "${env[credentialsId]}"
}

def dockerHubLogin() {
    return dockerRegistry.credentials("${DOCKER_HUB_USERNAME}", "${DOCKER_HUB_PASSWORD}")
}




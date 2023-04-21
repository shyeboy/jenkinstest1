pipeline {
    agent any
    
    environment {
        DOCKER_REGISTRY = "https://index.docker.io/shyeboy/hyeran0920/project:v11" // Dockerhub 등 레지스트리의 URL
        DOCKER_IMAGE_NAME = "hyeran0920/project:v11" // 빌드할 Docker 이미지의 이름
        DOCKERFILE = "./Dockerfile" // Dockerfile의 경로
        DOCKER_USERNAME = "kimsunghyun26"
        DOCKER_PASSWORD = "ksh31010!@"
    }
    
    stages {
        stage("Build Docker image") {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Dockerhub', passwordVariable: 'ksh31010!@', usernameVariable: 'kimsunghyun26')]) {
  
                    echo $DOCKERHUB_PASSWORD | docker login --username $DOCKERHUB_USERNAME --password-stdin
                    docker build -t shyeboy/hyeran0920/project:v11 -f ./Dockerfile .
                }
        
        stage("Push Docker image") {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Dockerhub', passwordVariable: 'ksh31010!@', usernameVariable: 'kimsunghyun26')]) {
                    // Dockerhub credentials 등록 및 사용
                    sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                }
                
                sh "docker push ${DOCKER_REGISTRY}/${DOCKER_IMAGE_NAME}" // Docker 이미지 push
            }
        }
    }
}




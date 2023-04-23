pipeline {
  agent any

  environment {
    DOCKER_REGISTRY = "docker.io"
    DOCKER_IMAGE = "kimsunghyun26/final_project"
    ACR_NAME = "kimsunghyun26/final_project:V2"
    AKS_NAME = "aks-1"
    RESOURCE_GROUP = "test_rg"
    AZURE_CREDENTIAL_ID = "08a5b32e-6669-4195-8b61-da1961a0caaf"
    K8S_NAMESPACE = "default"
    K8S_DEPLOYMENT_NAME = "was"
    K8S_CONTAINER_NAME = "kimsunghyun26/final_project:V2"
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
    stage('Deploy to Azure AKS') {
      steps {
        script {
          withCredentials([[
              $class: 'AzureCredentialsBinding',
              credentialsId: env.AZURE_CREDENTIAL_ID,
              useAzureCli: true
          ]]) {
            def azCredentials = azureCredentials(env.AZURE_CREDENTIAL_ID)

            sh "az login --service-principal -u ${azCredentials.getClientId()} -p ${azCredentials.getClientSecret()} --tenant ${azCredentials.getTenantId()}"
            sh "az aks get-credentials --name ${env.AKS_NAME} --resource-group ${env.RESOURCE_GROUP}"

            sh "kubectl set image deployment/${env.K8S_DEPLOYMENT_NAME} ${env.K8S_CONTAINER_NAME}=${env.ACR_NAME}.azurecr.io/${env.DOCKER_IMAGE} -n ${env.K8S_NAMESPACE}"
          }
        }
      }
    }
  }
}
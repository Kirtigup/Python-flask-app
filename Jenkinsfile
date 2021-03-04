
pipeline {
  environment {
  IBM_CLOUD_REGION = 'us-south'
  REGISTRY_HOSTNAME = 'de.icr.io'
  IKS_CLUSTER = 'c0sagkcd061p803m83rg'
  DEPLOYMENT_NAME = 'iks-test-1'
  PORT = '3001'
  registry = "kirtigupta123456/my-app"
  registryCredential = 'DockerIdentity'
  dockerImage = ''
  }
  agent any 
  stages {
    stage('Authenticate with IBM Cloud CLI') {
      steps {
        sh '''
            ibmcloud login --apikey iOWdNWHrRiIeQFd-xMWW_pYrcxGcRul5a4ZInHFi0Kze -r "${IBM_CLOUD_REGION}" -g Default
            ibmcloud ks cluster config --cluster ${IKS_CLUSTER}
            '''
      }
    }
    stage('Build with Docker') {
      steps {
        script {
        dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Push the image to ICR') {
      steps {
        script {
          docker.withRegistry( '', registryCredential ) {
          dockerImage.push()
          }
        }
      }
    }
    stage('Deploy to IKS') {
      steps {
        sh '''
            ibmcloud ks cluster config --cluster ${IKS_CLUSTER}
            kubectl config current-context
            kubectl apply -f deployment.yaml
            kubectl apply -f service.yaml
            kubectl get services -o wide
            '''
      }
    }
  }
}


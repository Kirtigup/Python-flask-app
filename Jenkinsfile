
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
   
    stage('Deploy to IKS') {
      steps {
        sh '''
            ibmcloud ks cluster config --cluster ${IKS_CLUSTER}
            kubectl config current-context
            kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-0.32.0/deploy/static/provider/baremetal/deploy.yaml
            kubectl apply -f deployment.yaml
            kubectl apply -f service.yaml
            kubectl apply -f ingress.yaml
            kubectl get services -o wide
            '''
      }
    }}}
  


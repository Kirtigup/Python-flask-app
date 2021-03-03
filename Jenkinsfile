node
{
  stage('Get Source')
  {
    git 'https://github.com/Kirtigup/Python-flask-app.git'
}
  stage('Docker-build')
  {
    sh 'docker build -t kirtigupta123456/my-app '
  }
  stage('Docker-push')
  {
  docker.withRegistry('https://registry.hub.docker.com', 'DockerIdentity')
    {
   def customImage=docker.build("kirtigupta123456/my-app")
    customImage.push()
  }
}
  stage('Kubernetes pod')
  {
        sh 'kubectl apply -f service.yaml'
        sh 'kubectl apply -f deployment.yaml'
        sh 'kubectl apply -f pod.yaml'
  }}

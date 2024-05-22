pipeline {
  agent {
    kubernetes {
      podTemplate(containers:[
        containerTemplate {
          name 'python'
          image 'python:3.10.5-alpine3.16'
          ttyEnabled true
          command 'cat'
        }
        containerTemplate {
          name 'helm'
          image 'lachlanevenson/k8s-helm:latest'
          ttyEnabled true
          command 'cat'
        }
      ])
    }
  }
  stages {
    container('python') {
      stage('Checkout') {
        steps {
          git url: 'https://github.com/maperez1225/devops-web-app-example.git' branch: 'dev'
          sh 'cd api/'
        }
      }
      stage('Install packages') {
        sh 'apk add --no-cache entr postgresql-dev musl-dev gcc'
      }
      stage('Test API') {
        steps {
          sh 'pip install -r requirements.txt'
          sh 'gunicorn app:app -b 0.0.0.0:80 --log-file - --access-logfile - --workers 4 --keep-alive 0'
          sh 'python test.py'
        }
      }
    }
    stage('Deploy to Kubernetes') {
      steps {
        container('helm') {
          sh "helm upgrade --install postgres ./charts/postgresql"
          sh "helm upgrade --install api ./charts/api"
          sh "helm upgrade --install web ./charts/web"
        }  
      }
    }
  }
}
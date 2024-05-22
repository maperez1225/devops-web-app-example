pipeline {
  agent {
    kubernetes {
      yaml '''
apiVersion: v1
kind: Pod
metadata:
  labels:
    label: agent
spec:
  containers:
  - name: python
    image: python:3.10.5-alpine3.16
    env:
    - name: "PGDATABASE"
      value: "postgres"
    - name: "PGUSER"
      value: "postgres"
    - name: "PGPASSWORD"
      value: "postgres"
    command:
    - cat
    tty: true
    volumeMounts:
    - mountPath: '/var/run/docker.sock'
      name: docker-socket
  - name: helm
    image: lachlanevenson/k8s-helm:latest
    command:
    - cat
    tty: true
  - name: node
    image: node:10-alpine
    env:
    - name: "PORT"
      value: "80"
    command:
      - cat
    tty: true
    volumeMounts:
    - mountPath: '/var/run/docker.sock'
      name: docker-socket
  volumes:
  - name: docker-socket
    hostPath:
      path: '/var/run/docker.sock'
  securityContext:
    runAsUser: 0
      '''
    }
  }
  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/maperez1225/devops-web-app-example.git', branch: 'dev'
      }
    }
    stage('Test API') {
      steps {
        container('python') {
          sh 'apk add --no-cache entr postgresql-dev musl-dev gcc'
          sh 'pip install -r ./api/requirements.txt'
          sh 'gunicorn app:app -b 0.0.0.0:80 --chdir ./api --daemon --log-file - --access-logfile - --workers 4 --keep-alive 0'
          sh 'python ./api/test.py'
        }
      }
    }
    stage('Test Web') {
      steps {
        container('node') {
          sh 'npm install --prefix ./web'
          //sh 'npm run lint --prefix ./web'
          sh 'npm run test --prefix ./web'
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
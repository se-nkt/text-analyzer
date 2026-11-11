pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "senkt/text-analyzer"
    }
    stages {
        stage('Lint') {
            steps {
                sh 'flake8 analyzer.py test_analyzer.py --max-line-length=100'
            }
        }
        stage('Unit Tests') {
            steps {
                sh 'pytest -v'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker rm -f text-analyzer-prod 2>/dev/null || true'
                sh 'docker run -d --name text-analyzer-prod -p 5001:5000 $DOCKER_IMAGE:latest'
            }
        }
    }
}

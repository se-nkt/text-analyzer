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
        stage('Database Migration (Flyway)') {
            steps {
                sh 'docker run --rm --network host -v /root/text-analyzer/sql:/flyway/sql flyway/flyway:10 -url=jdbc:postgresql://localhost:5432/analyzer_db -user=admin -password=secretpass migrate'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker rm -f text-analyzer-prod 2>/dev/null || true'
                sh 'docker run -d --name text-analyzer-prod -e HOST=0.0.0.0 -p 5001:5000 $DOCKER_IMAGE:latest'
            }
        }
    }
}

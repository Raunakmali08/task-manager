pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t task-manager .'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'docker run --rm task-manager pytest tests/test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying container...'
                sh 'docker stop task-manager-app || true'
                sh 'docker rm task-manager-app || true'
                sh 'docker run -d -p 5000:5000 --name task-manager-app task-manager'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully! App is live on port 5000.'
        }
        failure {
            echo 'Pipeline failed. Check the logs above.'
        }
    }
}

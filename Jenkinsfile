pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Amarbiradar107/EndtoEndAutomation.git'
            }
        }

        stage('Run Tests with Docker Compose') {
            steps {
                sh '''
                echo ===== Cleaning old containers =====

                docker rm -f jenkins-docker my-jenkins-2 selenium-pytest >nul 2>&1

                echo ===== Stopping previous compose stack =====
                docker-compose down

                echo ===== Starting test execution =====
                docker-compose up

                '''
            }
        }
    }

    post {
        always {
            sh '''
            echo ===== Cleaning Docker Resources =====
            docker compose down
            '''
        }
    }
}
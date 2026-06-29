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

                    docker rm -f jenkins-docker my-jenkins-2 selenium-pytest 2>nul || echo "No existing containers to remove"
                    

                    docker compose down --remove-orphans --volumes 2>nul || echo "Compose down completed"
                    

                    docker compose up --abort-on-container-exit --exit-code-from pytest --remove-orphans --force-recreate
                    

                    docker compose down --remove-orphans --volumes
                '''
            }
        }      
    }
}
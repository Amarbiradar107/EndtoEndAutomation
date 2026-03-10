pipeline {
    agent {
        label "windows_agent" //crate a node or slave on windows
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Amarbiradar107/EndtoEndAutomation.git'
            }
        }

        stage('Run Tests with Docker Compose') {
            steps {
                bat '''
                    docker-compose down
                    docker-compose up --abort-on-container-exit --exit-code-from pytest
                    docker-compose down
                '''
            }
        }       
    }
}
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
                    REM Force remove any existing containers with conflicting names
                    docker rm -f jenkins-docker my-jenkins-2 selenium-pytest 2>nul || echo "No existing containers to remove"
                    
                    REM Bring down compose stack with cleanup
                    docker-compose down --remove-orphans --volumes 2>nul || echo "Compose down completed"
                    
                    REM Start fresh with force recreate
                    docker-compose up --abort-on-container-exit --exit-code-from pytest --remove-orphans --force-recreate
                    
                    REM Clean up after tests
                    docker-compose down --remove-orphans --volumes
                '''
            }
        }      
    }
}
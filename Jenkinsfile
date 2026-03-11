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

        stage('Build image') {
            steps {
                bat '''
                       docker build -t selenium-pytest .
                       cd 
                    '''
            }
        }
         stage('Run Pytest in Docker') {
            steps {
                bat '''
                    docker run --rm -v %cd%:/app -w /app selenium-pytest pytest --html=reports/report.html --self-contained-html -vs
                '''
            }
        }       
    }
}
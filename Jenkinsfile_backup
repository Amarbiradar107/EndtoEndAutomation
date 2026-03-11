pipeline {
    agent none  // Explicitly set agents per stage
    
    stages {
        stage('Checkout') {
            agent { label 'master' }  // Run on Windows agent node
            steps {
                checkout scm
            }
        }
        
        stage('Build image') {
            agent { label 'master' }
            steps {
                // Docker build happens on Windows (via PowerShell/Docker Desktop)
                sh 'docker build -t selenium-pytest .'
            }
        }
        
        stage('Run Pytest in Docker') {
            agent {
                docker {
                    image 'selenium-pytest'
                    args '-u root'
                }
            }
            steps {
                sh '''
                    pytest --html=reports/report.html --self-contained-html -vs
                '''
            }
        }
    }
}
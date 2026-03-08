pipeline {
    agent {
        label 'master'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build image') {
            steps {
                bat '''

                       docker build -t selenium-pytest .
                       docker-compose up
                '''
            }
        }

        stage('Run Pytest in Docker') {
            agent {
                docker {
                    image 'selenium-pytest'      // use the image we just built
                    args '-u root'
                    reuseNode true
                }
            }
            steps {
                bat '''
                    pip install --upgrade pip    # requirements already in image
                    google-chrome --version || echo "chrome not installed"
                    pytest --html=TestAutomation/reports/report.html --self-contained-html -vs
                    pwd
                    ls -l TestAutomation/reports/
                '''
            }
        }
        stage('Post Test Execution') {


            steps {
                    sh '''
                        docker system prune -a

                    '''
            }

//            agent{
//                docker{
//                    image 'amazon/aws-cli:latest'
//                    reuseNode true
//                    args "--entrypoint=''"
//                }
//            }
//
//            environment{
//                // Set the S3 bucket name as an environment variable
//                AWS_S3_BUCKET= 'jenkins-test-26022026'
//            }
//
//            steps {
//                // Use Jenkins credentials to set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
//                withCredentials([usernamePassword(credentialsId: 'awsID', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')]) {
//                        sh '''
//                                aws --version
//                                aws s3 ls
//                                pwd
//                                // Sync the local reports directory to the specified S3 bucket
//                                aws s3 sync /var/jenkins_home/workspace/git_docker/Optima_Automation/reports/ s3://$AWS_S3_BUCKET/reports/
//                        '''
//                    }
//
//            }
        }
    }
}
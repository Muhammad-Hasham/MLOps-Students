pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // Clone the repository
                    git 'https://github.com/Muhammad-Hasham/MLOps-Students.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }

        stage('Execute test.py') {
            steps {
                script {
                    
                    sh 'python test.py'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy based on branch name
                    def branchName = sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()
                    if (branchName == 'master') {
                        echo 'Deploying to production'
                        // Add production deployment steps, e.g., deploy to production server
                        sh 'bash deploy-production.sh' // Example: Execute a deployment script
                    } else {
                        echo 'Deploying to UAT'
                        // Add UAT deployment steps, e.g., deploy to UAT server
                        sh 'bash deploy-uat.sh' // Example: Execute a UAT deployment script
                    }
                }
            }
        }
    }
}

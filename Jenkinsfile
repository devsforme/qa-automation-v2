pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/devsforme/qa-automation-v2.git'
            }
        }

        stage('Install dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                // Добавляем -s, чтобы print() выводился в консоль
                bat 'pytest -s --junitxml=reports/junit-report.xml'
            }
        }
    }

    post {
        always {
            junit 'reports/junit-report.xml'
        }
        failure {
            mail to: 'you@example.com',
                 subject: "Tests Failed in ${env.JOB_NAME} Build #${env.BUILD_NUMBER}",
                 body: "Please check the Jenkins console output: ${env.BUILD_URL}"
        }
    }
}

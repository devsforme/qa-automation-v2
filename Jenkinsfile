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
        bat '"C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\\python.exe" -m pip install -r requirements.txt'
    }
}

stage('Run tests') {
    steps {
        bat 'pytest -s test_sample.py --junitxml=reports/junit-report.xml'
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

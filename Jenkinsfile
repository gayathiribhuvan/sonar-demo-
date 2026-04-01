pipeline {
    agent any

    tools {
        sonarQubeScanner 'SonarScanner'
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/gayathiri_bhuvan/sonar-demo-.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('My Sonar Server') {
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=my-project \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://localhost:9000
                    '''
                }
            }
        }
    }
}

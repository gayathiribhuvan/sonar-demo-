pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/gayathiribhuvan/sonar-demo-.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('My Sonar Server') {
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=my-project \
                    -Dsonar.sources=. \
                    '''
                }
            }
        }
    }
}

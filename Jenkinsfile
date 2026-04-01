pipeline {
    agent any

    stages {

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

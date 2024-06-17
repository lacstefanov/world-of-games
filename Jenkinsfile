pipeline {
    agent any

    environment {
        DOCKER_IMAGE_ID = '5dea1f4edf69'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Jenkins image') {
            steps {
                script {
                    sh 'docker build -t jenkins-image . -f jenkins/Dockerfile'
                }
            }
        }
    }
}
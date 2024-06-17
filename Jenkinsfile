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

        stage('Build') {
            steps {
                script {
                    docker.build("world_of_games_app")
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    docker.image("world_of_games_app").run('-p 8777:5001 --name world_of_games_container')
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    bat 'docker.image("my_flask_app").inside { bat python /app/e2e.py } '
                }
            }
        }
    }
}
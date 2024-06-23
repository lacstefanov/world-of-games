pipeline {
    agent any

    environment {
        DOCKER_IMAGE_ID = '5dea1f4edf69'
        DOCKER_IMAGE = 'world_of_games_app'.toLowerCase()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
    }
}
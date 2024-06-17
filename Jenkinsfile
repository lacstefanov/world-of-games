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
                    docker.withRun("-v $(which docker):/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock") {
                    docker.image("${DOCKER_IMAGE_ID}").pull()
                    docker.image("${DOCKER_IMAGE_ID}").run()
                    #def image = docker.build("world_of_games_app")
                }
            }
        }
    }
}
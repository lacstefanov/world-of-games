pipeline {
    agent any

    environment {
     DOCKER_TOOL = tool name: 'Docker'
     PATH = "${DOCKER_TOOL}/bin:${env.PATH}"
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
                    sh 'docker --version'
                    def image = docker.build("world_of_games_app")
                }
            }
        }
    }
}
pipeline {
    agent any

     tools {
        tool name: 'docker', type: 'DockerTool'
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
    }
}
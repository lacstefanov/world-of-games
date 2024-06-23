pipeline {
    agent any

    tools {
        // Specify the name of the Docker installation configured in Jenkins
        dockerTool 'docker'
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
pipeline {
    agent any

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
                    docker.image("world_of_games_app").run('-p 8777:5001 -v /app/Scores.txt:/app/Scores.txt --name world_of_games_container')
                }
            }
        }

    }
}
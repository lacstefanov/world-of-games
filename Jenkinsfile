pipeline {
    agent any


    stages {

       stage('Cleanup') {
            steps {
                script {
                    // Stop and remove any existing container named world_of_games_container
                    sh 'docker rm -f world_of_games_container || true'
                    // Remove any existing image named world_of_games_app
                    sh 'docker rmi -f world_of_games_app || true'
                }
            }
        }

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
                    // Run the dockerized application exposing port 8777 and mount the dummy Scores.txt file
                    sh 'docker run -d --name world_of_games_container -p 8777:5001 -v "$(pwd)/Scores.txt:/app/Scores.txt" world_of_games_app'
                }
            }
        }
    }
}
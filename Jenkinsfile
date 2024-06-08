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

        

    }
}
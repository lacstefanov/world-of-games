pipeline {
    agent any

    environment {
        DOCKER_PATH = '/usr/bin/docker'
        PATH = "/usr/bin:${env.PATH}"
    }

    stages {

            stage('Debug') {
            steps {
                script {
                    // Print the Docker tool path
                    echo "Docker binary path: ${DOCKER_PATH}"

                    // Print the current PATH
                    echo "Current PATH: ${env.PATH}"

                    // Check Docker version
                    sh "${DOCKER_PATH} --version"
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
                    sh 'docker --version'
                    def image = docker.build("world_of_games_app")
                }
            }
        }
    }
}
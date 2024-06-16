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
                    def dockerPath = sh(script: 'which docker', returnStdout: true).trim()
                    echo "Docker binary path: ${dockerPath}"

                    // Print the current PATH
                    echo "Current PATH: ${env.PATH}"

                    // Check Docker version using the found Docker path
                    sh "${dockerPath} --version"
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
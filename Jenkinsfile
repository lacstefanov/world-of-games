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
                    echo "Starting Debug Stage"
                    echo "PATH: ${env.PATH}"

                    def dockerPath = sh(script: 'which docker', returnStdout: true).trim()
                    echo "Docker binary path: ${dockerPath}"

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
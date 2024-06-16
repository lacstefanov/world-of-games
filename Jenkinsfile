pipeline {
    agent any

    environment {
        PATH = "/usr/bin:$PATH" // Ensure Docker path is included in PATH
    }

    stages {

            stage('Debug') {
            steps {
                script {
                    def dockerPath = '/usr/bin/docker'
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
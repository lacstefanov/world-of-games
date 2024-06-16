pipeline {
    agent any

    environment {
        PATH = "/usr/bin:$PATH" // Ensure Docker path is included in PATH
    }

    stages {

            stage('Debug') {
            steps {
                script {
                    echo "Starting Debug Stage"
                    echo "PATH: ${env.PATH}"

                    // Use the Docker installation configured in Jenkins
                    def dockerHome = tool name: 'Docker', type: 'org.jenkinsci.plugins.docker.commons.tools.DockerTool'
                    def dockerClient = dockerHome.getClient()
                    dockerClient.version()

                    // Test docker version
                    sh "docker --version"
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
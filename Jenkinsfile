pipeline {
    agent any

    tools {
        // Define the Docker tool with the configured name from Jenkins Global Tool Configuration
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
                def dockerHome = tool name: 'docker', type: 'org.jenkinsci.plugins.docker.commons.tools.DockerTool'

                    dockerHome.withDockerRegistry([credentialsId: 'docker-registry-creds', url: 'https://index.docker.io/v1/']) {
                    docker.build("world_of_games_app")
                    }
                }
            }
        }
    }
}
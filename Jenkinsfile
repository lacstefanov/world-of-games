pipeline {
    agent any

    tools {
        'org.jenkinsci.plugins.docker.commons.tools.DockerTool' 'docker'
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
                    docker.withTool('docker') {
                        docker.withRegistry('repo', 'credentials') {
                            docker.build("world_of_games_app")
                        }
                    }
                }
            }
        }
    }
}
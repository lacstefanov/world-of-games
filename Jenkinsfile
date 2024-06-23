pipeline {
    agent any

    environment {
        registry = 'https://index.docker.io/v1/'
        registryCredential = 'e98a7f29-90e1-493d-ae0d-82823d8a1470'
    }

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
                        docker.withRegistry(registry, registryCredential) {
                            docker.build("world_of_games_app")
                        }
                    }
                }
            }
        }
    }
}
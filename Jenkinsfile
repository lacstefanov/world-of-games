pipeline {
    agent any

    environment {
        DOCKER_IMAGE_ID = '5dea1f4edf69'
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
                    // Run Docker container with explicit Docker path
                    docker.withRun("-v ${sh(script: 'which docker', returnStdout: true).trim()}:${dockerToolPath('docker')} -v /var/run/docker.sock:/var/run/docker.sock") {
                        // Your Docker commands here
                        docker.image("${DOCKER_IMAGE_ID}").pull()
                        docker.image("${DOCKER_IMAGE_ID}").run()
                    }
                }
            }
        }
}
}
pipeline {
    agent any

    environment {
        DOCKER_NETWORK = 'world_of_games_network'
        DOCKERHUB_CREDENTIALS = 'a6b347e4-0c43-4f7f-9a75-ac0e352d2fdb'
        DOCKERHUB_REPO = 'lstefanov010/world_of_games_app'
    }

    stages {
        stage('Cleanup') {
            steps {
                script {
                    // Stop and remove any existing container named world_of_games_container
                    sh 'docker rm -f world_of_games_container || true'
                    // Remove any existing image named world_of_games_app
                    sh 'docker rmi -f world_of_games_app || true'
                    // Remove the custom Docker network
                    sh 'docker network rm $DOCKER_NETWORK || true'
                }
            }
        }

        stage('Create Network') {
            steps {
                script {
                    // Create a custom Docker network
                    sh 'docker network create $DOCKER_NETWORK'
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
                    docker.build("world_of_games_app")
                    }
                }
            }

        stage('Run') {
            steps {
                script {
                    // Run the dockerized application exposing port 8777 and mount the dummy Scores.txt file
                    def dockerRunCommand = "-d --name world_of_games_container -p 8777:5001 --network $DOCKER_NETWORK -v $(pwd)/Scores.txt:/app/Scores.txt world_of_games_app"
                    sh "docker run ${dockerRunCommand}"
                    sh 'docker logs world_of_games_container' // Check logs for any errors
                    sh 'docker exec world_of_games_container curl http://localhost:5001' // Check internal access
                }
            }
        }

        stage('Test') {
            steps {
                script {
                        // Execute Selenium tests within the Docker container environment
                        withEnv(['APP_URL=http://world_of_games_container:5001']) {
                            docker.image('world_of_games_app').inside("--network $DOCKER_NETWORK") {
                                sh "python /app/tests/e2e.py"
                            }
                        }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Stop and remove the running container
                    sh 'docker stop world_of_games_container'
                    sh 'docker rm world_of_games_container'

                    // Log in to Docker Hub
                    withCredentials([usernamePassword(credentialsId: env.DOCKERHUB_CREDENTIALS, usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        sh '''
                            echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin
                            docker tag world_of_games_app ${DOCKERHUB_REPO}:latest
                            docker push ${DOCKERHUB_REPO}:latest
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up the Docker environment
                sh 'docker system prune -f'
            }
        }
    }
}
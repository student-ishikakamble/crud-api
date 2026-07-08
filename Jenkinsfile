pipeline {

    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t crud-api .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running health test'
                sh '''
                docker run -d --name crud-test -p 8000:8000 crud-api
                sleep 5
                curl -f http://localhost:8000/health
                docker stop crud-test
                docker rm crud-test
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application'
                sh '''
                docker stop crud-api-container || true
                docker rm crud-api-container || true

                docker run -d \
                --name crud-api-container \
                -p 8000:8000 \
                crud-api
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }

        failure {
            echo 'Deployment failed - rollback required'
        }
    }
}

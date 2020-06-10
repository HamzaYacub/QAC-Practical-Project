pipeline {
    agent any
    stages {
        stage("Change permissions for scripts") {
            steps {
                sh 'chmod +x ./scripts/*'
            }
        }
        stage("Export environment variables") {
            steps {
                sh './scripts/variables.sh'
            }
        }
        stage("Install ansible") {
            steps {
                sh './scripts/ansible.sh'
            }
        }
        stage("Deploy docker") {
            steps {
                sh './scripts/docker.sh'
            }
        }
    }
}
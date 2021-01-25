pipeline {
    agent none
    triggers {
        githubPush()
    }
    stages {
        stage('Build') {
            agent any
            steps {
                sh 'python3.7 setup.py sdist --formats=zip,gztar bdist_wheel'
            }
        }
    }
}

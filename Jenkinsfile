pipeline {
    agent none
    stages {
        stage('Build') {
            agent any
            steps {
                sh 'python3.7 setup.py sdist --formats=zip,gztar bdist_wheel'
                stash(name: 'compiled-results', includes: 'vboxcli/*.py*')
            }
        }
    }
}

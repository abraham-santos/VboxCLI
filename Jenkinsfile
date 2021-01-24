pipeline {
    agent none
    stages {
        stage('Build') {
            agent any
            steps {
                sh 'python3.7 -O -m PyInstaller -F src/vboxcli.py'
                stash(name: 'compiled-results', includes: 'src/*.py*')
            }
        }
    }
}

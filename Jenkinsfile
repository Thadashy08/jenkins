pipeline {
    agent any

    stages {
        stage('Preparar entorno') {
            steps {
                sh 'apt update && apt install -y python3 python3-venv'
                sh 'python3 -m venv venv'
            }
        }
        stage('Ejecutar pruebas') {
            steps {
                sh './venv/bin/python -m unittest test_app.py'
            }
        }
    }
}


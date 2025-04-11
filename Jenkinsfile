pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {
        stage('Preparar entorno') {
            steps {
                sh 'python -m venv venv'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh './venv/bin/python -m unittest test_app.py'
            }
        }
    }
}

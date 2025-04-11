pipeline {
    agent any

    stages {
        stage('Instalar dependencias') {
            steps {
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

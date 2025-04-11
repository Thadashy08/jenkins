pipeline {
    agent any

    stages {
        stage('Preparar entorno') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh '. venv/bin/activate && python -m unittest test_app.py'
            }
        }
    }
}

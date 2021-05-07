pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'main', url: 'https://github.com/pauliee99/movie-database.git'

                
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    python3 -m venv myvenv
                    source myvenv/bin/activate
                    pip install -r requirements.txt
                    cd movies
                    cp movies/.env.example movies/.env
                    python manage.py makemigrations
                    python manage.py migrate
                    ./manage.py test'''
            }
        }

        stage('Deploy') {
            steps {
                sshagent (credentials: ['']) {

                    sh '''
                    '''
                }
            }
        }
    }
}

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
                    source ./myvenv/bin/activate
                    pip install -r requirements.txt
                    cd database
                    cp database/.env.example database/.env
                    python manage.py makemigrations
                    python manage.py migrate
                    ./manage.py test
		    '''
            }
        }

        stage('Deploy') {
            steps {
                sshagent (credentials: ['ssh-deploy']) {

                    sh '''
			pwd
			echo $WORKSPACE
			cd ~/workspace/movie-ansible
                        chmod 777 define_user_dir.sh
                        ./define_user_dir.sh > group_vars/deploymentservers.yml
                        chmod 777 define.sh
                        ./define.sh > hosts.yml
                        ansible-playbook -l deploymentservers playbooks/mysql-database.yml
                        ansible-playbook -l deploymentservers playbooks/movie-database-install.yml
                    '''
                }
            }
        }
    }
}

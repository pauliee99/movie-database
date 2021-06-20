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
                    python manage.py makemigrations posts
                    python manage.py migrate
                    ./manage.py test
		    '''
            }
        }

        stage('Deploy') {
            environment {
                DB_ROOT_PASSWD=credentials('db-root-passwd')
                DB_NAME=credentials('db-name')
                DB_USER=credentials('db-user')
                DB_PASSWD=credentials('db-passwd')
                DB_SECRET_KEY=credentials('db-key')
                DB_HOST=credentials('db-host')
                DB_PORT=credentials('db-port')
            }
            steps {
                sshagent (credentials: ['ssh-classic']) {

                    sh '''
			pwd
			echo $WORKSPACE
			cd ~/workspace/movie-ansible
                        chmod 777 define_user_dir.sh
                        ./define_user_dir.sh > group_vars/deploymentservers.yml
                        chmod 777 define.sh
                        ./define.sh > hosts.yml
                        ansible-playbook -l deploymentservers playbooks/mysql-database.yml \
                        -e DB_ROOT_PASSWD=$DB_ROOT_PASSWD \
                        -e DB_NAME=$DB_NAME \
                        -e DB_USER=$DB_USER \
                        -e DB_PASSWD=$DB_PASSWD
                        ansible-playbook -l deploymentservers playbooks/movie-database-install.yml \
                        -e DB_NAME=$DB_NAME \
                        -e DB_USER=$DB_USER \
                        -e DB_PASSWD=$DB_PASSWD \
                        -e DB_SECRET_KEY=$DB_SECRET_KEY \
                        -e DB_HOST=$DB_HOST \
                        -e DB_PORT=$DB_PORT
                    '''
                }
            }
        }
    }
}

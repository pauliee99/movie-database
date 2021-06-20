pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'main', url: 'https://github.com/pauliee99/movie-database.git'

                
            }
        }

        stage('Push mysql image for test and docker push'){
            steps {
                sh '''
                    docker pull mysql
                    docker run --name=mysql_test_server -d mysql \
                    --env MYSQL_ROOT_PASSWORD='example' \
                    --env MYSQL_DATABASE='test' \
                    --env MYSQL_USER='test_user' \
                    --env MYSQL_PASSWORD='testpasswd'
                    '''
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    python3 -m venv myvenv
                    source ./myvenv/bin/activate
                    pip install -r requirements.txt
                    cd database
                    cp database/.env.example.docker database/.env
                    python manage.py makemigrations
                    python manage.py migrate
                    ./manage.py test
		    '''
            }
        }

        stage('Docker create image and push image') {
            environment {
                IMAGE='belpanos/movie-db'
                DOCKER_USERNAME=credentials('docker-user')
                DOCKER_PASSWORD=credentials('docker-passwd')
            }
            steps {
                sh '''
                    echo $BUILD_ID
                    COMMIT_ID=$(git rev-parse --short HEAD)
                    echo $COMMIT_ID
                    TAG=$COMMIT_ID-$BUILD_ID
                    docker build -t $IMAGE -t $IMAGE:$TAG -f nonroot.Dockerfile .
                    docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
                    docker push $IMAGE --all-tags
                '''
            }
        }

        stage('Docker Deploy') {
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
              sshagent (credentials: ['ssh-docker']) {
                sh '''
                    pwd
		    echo $WORKSPACE
		    cd ~/workspace/movie-ansible
                    chmod 777 define_docker.sh
                    ./define_docker.sh > hosts.yml
                    ansible-playbook -l deploymentservers playbooks/docker/docker_movies_db.yml \
                    -e DB_ROOT_PASSWD=$DB_ROOT_PASSWD \
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

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

        stage('DOCKER') {
            steps {
              sshagent (credentials: ['ssh-deploy']) {
                sh '''
                    pwd
		    echo $WORKSPACE
		    cd ~/workspace/movie-ansible
                    chmod 777 define_docker.sh
                    ./define_docker.sh > hosts.yml
                    ansible-playbook -l deploymentservers playbooks/docker/docker_deployment.yml
                '''
              }
            }
        }

    }
}

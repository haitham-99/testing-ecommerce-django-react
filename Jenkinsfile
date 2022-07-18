@Library("shared-library") _

pipeline {
    agent any

    environment {
      JIRA_URL = "https://testecom.atlassian.net/"
      JIRA_CREDENTIALS = credentials("jira-jenkins")
    }

    stages {
        stage('Pulling from GitHub') {
          steps {
           git branch: 'main',
           credentialsId: 'e2adb9fa-442b-4e72-a6a8-43ae07acb268',
           url: 'https://github.com/haitham-99/testing-ecommerce-django-react.git'
          }
        }
        stage('Build python') {
            steps {
                bat '''python -m venv venv
                       call ./venv/Scripts/activate
                       pip install -r requirements.txt
                       pip install pytest-html
                      '''
            }
        }

        stage('Running pytest tests') {
            steps {
                bat '''call ./venv/Scripts/activate
                       pytest '''
            }
        }
        // stage('Deploying to Docker') {
        //     steps {
        //         bat '''
        //         docker image build -t ecommerce-project .
        //         docker run  --name=flask-project -p 8000:8000 -d ecommerce-project
        //         '''
        //     }
        // }


    }


    post {
      failure {
                  bat '''curl -D- -u haithamodehodeh@gmail.com:RRwPUHY7qXkiv4RrwvhZ94CC -X POST --data "@C:\\Users\\haith\\Desktop\\add.txt" -H "Content-Type:application/json" https://testecom.atlassian.net/rest/api/2/issue/'''

    }

}
}
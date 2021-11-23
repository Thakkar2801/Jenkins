pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/BThangaraju/Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "python Prog1.py"
                sh "./Prog1.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "python Test.py"
                sh "./Test.py"
            }
        }
    } 
}

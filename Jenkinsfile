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
                sh "chmod u+x python Prog1.py"
                sh "./Prog1.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x python Test.py"
                sh "./Test.py"
            }
        }
    } 
}

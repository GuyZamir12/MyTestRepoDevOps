pipeline {
    agent any

    stages {
        stage('Initialize') {
            steps {
                // Ensure tool is available (running as root in your Docker setup)
                sh 'apt-get update && apt-get install -y jq'
            }
        }

        stage('JSON Syntax Check') {
            steps {
                script {
                    // Finds all .json files and validates them
                    sh '''
                        echo "Starting JSON validation for all files..."
                        find . -name "*.json" | while read file; do
                            echo "Checking: $file"
                            jq . "$file" > /dev/null || (echo "❌ Invalid JSON in $file" && exit 1)
                        done
                        echo "✅ All JSON files are valid."
                    '''
                }
            }
        }
    }
}
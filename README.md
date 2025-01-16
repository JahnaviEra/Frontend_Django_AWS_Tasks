# Frontend_Django_AWS_Tasks
This repository contains a collection of tasks and projects focused on frontend development, Django-based web application development, and AWS Lambda functions. Each task is organized into its own branch for better modularity and version control. The repository is structured to showcase the implementation process, from initial setup to deployment.


Here’s the exact content you can add to your README.md for the Frontend Development task:

# Frontend Development
Task 1: Create a Responsive Webpage
**Steps to Run the Frontend Task**
Clone the Repository: Clone the repository to your local machine.

------https://github.com/JahnaviEra/Frontend_Django_AWS_Tasks.git---------

Navigate to the Frontend Folder: Go to the folder where the frontend files are located. 

cd Frontend_Django_AWS_Tasks/Task1
open index.html


# Django Chat Application

Task 2: Develop a Chat Application with the Following Features
        User Authentication
        Users can sign up and log in
        User List
        Chat Functionality

**Steps to Run the Django Chat Application**

Navigate to the Django Project Folder: Change the directory to the Django project folder.

cd Frontend_Django_AWS_Tasks/Task2
Set Up a Virtual Environment:
python -m venv venv
.\venv\Scripts\activate

Install Required Libraries: Install the required libraries using pip.

pip install -r requirements.txt
python manage.py startapp chat
Apply Migrations: Run the following command to apply database migrations. This will set up the database tables required for the project.
created app:

python manage.py makemigrations chat
python manage.py migrate 
## to Create users for chatting
python manage.py createsuperuser ## add users now

Run the Development Server: Start the Django development server.

python manage.py runserver
This will start the server, and you can access the chat application at:

**http://127.0.0.1:8000**

# AWS Lambda Functions
Task 3.1: Lambda Function to Add Two Numbers and Return the Result
Write an AWS Lambda function that takes two numbers as input, adds them, and returns the result.

Task 3.2: Lambda Function to Store a Document or PDF File in an S3 Bucket
Write an AWS Lambda function that stores a document or PDF file (provided as a base64-encoded string) in an S3 bucket.

**Steps to Run the AWS Lambda Functions**
Prerequisites:
An AWS account.
AWS CLI installed and configured with your AWS credentials. If you don't have it, you can install and configure it using this guide.
IAM Role with the necessary permissions for AWS Lambda and S3. The role should have policies such as AWSLambdaBasicExecutionRole and AmazonS3FullAccess attached to it.
Task 3.1: AWS Lambda Function to Add Two Numbers
Create the Lambda Function:

Log in to the AWS Management Console.
Go to the Lambda service.
Click on Create function and select Author from scratch.
Set the function name, e.g., AddNumbersFunction.
Choose an existing role or create a new one with basic Lambda permissions.
cd Frontend_Django_AWS_Tasks/Task3
use the lambda_function.py code 
Deploy the Function:

Click on Deploy to save the function.
Test the Function:
Create a test event with the following JSON payload to test the function:

{
  "num1": 5,
  "num2": 3
}

# Task 3.2: AWS Lambda Function to Store a Document or PDF in an S3 Bucket
Create the Lambda Function:

Go to the AWS Lambda service in the AWS Management Console.
Click on Create function and select Author from scratch.
Set the function name, e.g., StoreFileInS3.
Choose an existing role or create a new one with the necessary S3 permissions.
use the lambda_func_s3_bucket.py code

Deploy the Function:

Click on Deploy to save the function.

### Test the Function:###

Create a test event with the following JSON payload to test the function:

{
  "file_content": "base64_encoded_file_content_here",
  "file_name": "document.pdf",
  "bucket_name": "your-s3-bucket-name"
}

By following these steps in your README, you should be able to execute all the tasks without any issues, provided the prerequisites (like AWS CLI and IAM roles) are met.



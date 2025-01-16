import json
import boto3
import base64

# Initialize the S3 client using boto3. This will allow the function to interact with the S3 service.
s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
    Lambda function handler to store a document (PDF or other file types) in an S3 bucket.
    """
    
    # Step 1: Extract the base64-encoded file content, file name, and S3 bucket name from the event.
    file_content_base64 = event['file_content']  # Base64-encoded file content passed in the event.
    file_name = event['file_name']  # File name to be stored in S3.
    bucket_name = event['bucket_name']  # The S3 bucket where the file will be uploaded.

    # Step 2: Decode the base64-encoded file content to get the actual binary data of the file.
    file_content = base64.b64decode(file_content_base64)

    try:
        # Step 3: Upload the file to the specified S3 bucket using the `put_object` method.
        s3.put_object(
            Bucket=bucket_name,  # The name of the S3 bucket to store the file in.
            Key=file_name,       # The name to use for the file in the S3 bucket.
            Body=file_content,   # The actual binary content of the file.
            ContentType='application/pdf'  # Specify the content type (adjust if uploading other file types).
        )

        # Step 4: Return a success response if the file upload is successful.
        return {
            'statusCode': 200,  # HTTP status code 200 indicates success.
            'body': json.dumps({'message': 'File uploaded successfully'})  # JSON response message.
        }

    except Exception as e:
        # Step 5: Handle any exceptions that occur during the file upload and return an error response.
        return {
            'statusCode': 500,  # HTTP status code 500 indicates a server-side error.
            'body': json.dumps({'message': str(e)})  # Include the error message in the response.
        }


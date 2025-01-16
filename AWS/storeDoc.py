import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        file_name = body.get('fileName')
        file_content = body.get('fileContent')
        bucket_name = body.get('bucketName')

        if not file_name or not file_content or not bucket_name:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Missing required parameters: fileName, fileContent, or bucketName."
                })
            }

        decoded_file_content = base64.b64decode(file_content)

        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=decoded_file_content,
            ContentType='application/pdf'  
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"File uploaded successfully to {bucket_name}/{file_name}"
            })
        }
    except Exception as e:
        print(f"Error uploading file to S3: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": "Failed to upload file to S3.",
                "details": str(e)
            })
        }

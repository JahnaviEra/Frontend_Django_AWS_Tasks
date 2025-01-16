import json

def lambda_handler(event, context):
    # Extract numbers from the event (you can modify the structure as per your needs)
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)

    # Add the numbers
    result = num1 + num2

    # Return the result in a JSON response
    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }

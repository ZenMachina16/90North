import json

def lambda_handler(event, context):
    try:
        # Parse the input from the event body
        body = json.loads(event.get('body', '{}'))
        number1 = body.get('number1')
        number2 = body.get('number2')

        # Validate inputs
        if not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid input. Both number1 and number2 must be numeric."})
            }

        # Calculate the sum
        result = number1 + number2

        # Return the result
        return {
            "statusCode": 200,
            "body": json.dumps({"result": result})
        }
    except json.JSONDecodeError:
        # Handle JSON parsing errors
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON in request body."})
        }
    except Exception as e:
        # Handle other unexpected errors
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"An internal error occurred: {str(e)}"})
        }

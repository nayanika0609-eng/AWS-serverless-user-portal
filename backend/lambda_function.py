import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("UserData")

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

        email = body.get("email")
        name = body.get("name")

        if not email or not name:
            return {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"message": "Email and Name are required."})
            }

        table.put_item(Item={
            "email": email,
            "name": name
        })

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "*"
            },
            "body": json.dumps({"message": "User added successfully!"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"message": f"Error: {str(e)}"})
        }

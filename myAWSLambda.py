import json

def lambda_handler(event, context): 
    message = f" Hello {event['queryStringParameters']['name']} from {event['queryStringParameters']['country']} !"
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
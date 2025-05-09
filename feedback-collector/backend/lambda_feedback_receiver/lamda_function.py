import json
import boto3
import datetime

sns = boto3.client('sns')
SNS_TOPIC_ARN = 'arn:aws:sns:eu-west-1:788174142154:yannick-feedback-topic'  

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))  # Zeigt das gesamte Event

    body = json.loads(event['body'])
    print("Parsed body:", body)  # Zeigt Name + Feedback

    message = {
        "name": body.get('name'),
        "feedback": body.get('feedback'),
        "timestamp": datetime.datetime.utcnow().isoformat()
    }

    print("Message to SNS:", message)

    response = sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=json.dumps(message)
    )

    print("SNS response:", response)

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"message": "Feedback received!"})
    }

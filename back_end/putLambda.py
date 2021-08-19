import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitors')

def lambda_handler(event, context):
    
    response = table.update_item(
        Key={
            'id':'visitors'
        },
        UpdateExpression="set visitorCount = visitorCount +:val",
        ExpressionAttributeValues={
            ':val': Decimal(1)
        },
        ReturnValues="UPDATED_NEW"
    )
    return response
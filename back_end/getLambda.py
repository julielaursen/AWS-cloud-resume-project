import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal


#convert decimal to float
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitors')

def lambda_handler(event, context):

    response = table.get_item(
        Key={
            'id': 'visitors' 
        }
    )
    print(response)
    return {
        'statusCode': 200,
         'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'https://www.example.com',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(response, cls=DecimalEncoder)
    }
    
    
   
    
    
    
    
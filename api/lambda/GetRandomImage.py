import json
import random
import boto3

BUCKET = 'sheldonbot-images-21985152'
CDN_PREFIX = 'https://cdn.sheldonbot.com/'

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print(event)
    tag = event['tag']

    # List all objects in the bucket with the requested prefix except for the bucket itself
    resp = s3.list_objects_v2(Bucket=BUCKET, Prefix=tag+'/', StartAfter=tag+'/')

    # Select a random object from the listing
    obj = random.choice(resp['Contents']) if 'Contents' in resp else None

    # Return a response
    if obj is None:
        return {
            'statusCode': 400,
            "headers": {"Access-Control-Allow-Origin":"*"},
            "body": json.dumps( { "Status": "Failure", "Reason": "Invalid tag", "Image": CDN_PREFIX + "not_found.png" } )
        }
    else:
        return {
            'statusCode': 200,
            "headers": {"Access-Control-Allow-Origin":"*"},
            "body": json.dumps( { "Status": "Success", "Image": CDN_PREFIX + obj['Key'] } )
        }

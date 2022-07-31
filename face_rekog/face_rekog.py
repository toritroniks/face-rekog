import boto3
import json
import base64
import os
import logging

print('Loading function')

rekognition = boto3.client('rekognition')

def search_face(b64Image):
    response = rekognition.search_faces_by_image(CollectionId='face-rekog', Image={"Bytes": b64Image})
    return response

def lambda_handler(event, context):

    try:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)


        if event['body']:
            out = search_face(base64.b64decode(event['body']))

    except Exception as e:
        # Lambdaログにエクセプションの情報を入れる
        logger.exception(e)
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json', 
                'Access-Control-Allow-Origin': '*' 
            },
            'body': json.dumps({'error_message': str(e)}),
        }
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json', 
            'Access-Control-Allow-Origin': '*' 
        },
        'body': json.dumps(out)
    }
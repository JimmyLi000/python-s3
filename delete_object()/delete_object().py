'''
delete object
'''

import boto3

s3_client = boto3.client('s3')

response = s3_client.delete_object(
    Bucket='demo12366747',            #bucket_name
    Key='test.txt',                   #delete object_name
)

print(response)                       #show result  
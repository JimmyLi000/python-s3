'''
Upload the file to the specified Bucket
'''

import boto3

s3_client = boto3.client('s3')

response = s3_client.upload_file('C:/Users/user/Desktop/test.txt', 'demo12366747', 'test.txt')       #upload_file('file_path', 'bucketname', 'filename')
response1 = s3_client.upload_file('C:/Users/user/Desktop/test2.txt', 'demo12366747', 'test2.txt') 

print(response)                          #show result
print(response1)   
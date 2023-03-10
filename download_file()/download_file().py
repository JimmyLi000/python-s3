'''
download the file to the computer
'''

import boto3

s3_client = boto3.client('s3')

response = s3_client.download_file('demo12366747', 'test.txt', 'C:/Users/user/Desktop/test.txt')       #download_file('bucketname', 'filename', 'file_path')

print(response)                          #show result 
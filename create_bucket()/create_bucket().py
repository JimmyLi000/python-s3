'''
create bucket
'''

import boto3

s3_client = boto3.client('s3')

response = s3_client.create_bucket(          #使用函數叫 create_bucket() 
    ACL='private',                           #ACL設定私有
    Bucket='demo12366744',                   #bucket的名稱
    CreateBucketConfiguration={              #區域
       'LocationConstraint': 'us-east-2'
   },
  
   
)

print(response)                              #顯示執行結果        

 [create_bucket()](#create_bucket())
 [deploy success](#deploy success)
# create_bucket()
官方文件：
- S3
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html

- create_bucket()
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html


```python
'''
create bucket
'''

import boto3

s3_client = boto3.client('s3')

response = s3_client.create_bucket(          #使用函數叫 create_bucket() 
    ACL='private',                           #ACL設定私有
    Bucket='demo12366747',                   #bucket的名稱
    CreateBucketConfiguration={              #區域
       'LocationConstraint': 'us-east-2'
   },
  
   
)

print(response)                              #顯示執行結果
```

<div><br></div>

如果不加區域的話，<font color="#f00">預設會在us-east-1</font>，
以下是加入區域的方式
```js 
CreateBucketConfiguration={
        'LocationConstraint': 'af-south-1'|'ap-east-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-southeast-3'|'ca-central-1'|'cn-north-1'|'cn-northwest-1'|'EU'|'eu-central-1'|'eu-north-1'|'eu-south-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'me-south-1'|'sa-east-1'|'us-east-2'|'us-gov-east-1'|'us-gov-west-1'|'us-west-1'|'us-west-2'
    },
```

<div><br></div>

#小提醒 
但加了us-east-1會顯示錯誤，其它區域皆為正常
https://repost.aws/questions/QUKgr9fG6fSimVSUqK9fvkwQ/illegal-location-constraint-exception-error-when-using-s-3-create-bucket-code
```js 
    raise error_class(parsed_response, operation_name)

ClientError: An error occurred (InvalidLocationConstraint) when calling the CreateBucket operation: The specified location-constraint is not valid
```

<div><br></div>

---

# create success

回到AWS S3頁面，看到創建成功Bucket

![[create.png]]
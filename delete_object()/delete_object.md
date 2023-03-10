# aws configure
First set aws configure，Please refer to the article：

https://github.com/JimmyLi000/python-s3/blob/main/00_aws%20cli%20for%20aws%20configure/aws%20configure.md

<div><br></div>

---
<div><br></div>

# delete_object()
official document：
- S3：
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html

- delete_object()：
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_object.html

```python
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
```


<div><br></div>

---
<div><br></div>

# delete success

Go back to the AWS S3 ，Check bucket ，will delete test.txt .

![[object.png]]

<div><br></div>

Delete object through python

![[delete object.png]]
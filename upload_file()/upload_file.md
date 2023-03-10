
[create_bucket()](#create_bucket())
[deploy success](#deploy success)

# aws configure()
First set aws configure，Please refer to the article：

https://github.com/JimmyLi000/python-s3/blob/main/00_aws%20cli%20for%20aws%20configure/aws%20configure.md

<div><br></div>

---
<div><br></div>

# upload_file()
official document：
- S3：
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html

- upload_file()：
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/upload_file.html

```python
'''
Upload the file to the specified Bucket
'''

import boto3

s3_client = boto3.client('s3')

response = s3_client.upload_file('C:/Users/user/Desktop/test.txt', 'demo12366747', 'test.txt')       #upload_file('file_path', 'bucketname', 'filename')
response1 = s3_client.upload_file('C:/Users/user/Desktop/test2.txt', 'demo12366747', 'test2.txt') 

print(response)                          #show result
print(response1)                     
```


<div><br></div>

---
<div><br></div>

# upload success

Go back to the AWS S3 ，Check that the upload is successful to the <font color=#FF0000>specified Bucket</font> .

![[upload success.png]](https://github.com/JimmyLi000/python-s3/blob/main/upload_file()/upload.png)

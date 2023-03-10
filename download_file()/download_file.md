# aws configure
First set aws configure，Please refer to the article：

https://github.com/JimmyLi000/python-s3/blob/main/00_aws%20cli%20for%20aws%20configure/aws%20configure.md

<div><br></div>

---
<div><br></div>

# download_file()
official document：
- S3：
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html

- download_file()：
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/download_file.html

```python
'''
download the file to the computer
'''

import boto3

s3_client = boto3.client('s3')

response = s3_client.download_file('demo12366747', 'test.txt', 'C:/Users/user/Desktop/test.txt')       #download_file('bucketname', 'filename', 'file_path')

print(response)                          #show result                   
```


<div><br></div>

---
<div><br></div>

# download success

Go back to the AWS S3 ，Check that the download is successful .

![[download.png]]
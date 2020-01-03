import boto3
import json
BUCKET = 'fueb-analitics'
FILE_TO_READ = 'dataoftry.json'
client = boto3.client('s3',
                       region_name='ap-south-1',
                       aws_access_key_id='AKIA6RBMXR2AFQYQ3REQ',
                       aws_secret_access_key='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'
                     )
result = client.get_object(Bucket=BUCKET, Key=FILE_TO_READ)
text = result["Body"].read()
print(text)
just = json.loads(text)
print(just)
print(just['fruit'])

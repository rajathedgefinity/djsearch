import boto3

s3 = boto3.resource(
    's3',
    region_name='ap-south-1',
    aws_access_key_id='AKIA6RBMXR2AFQYQ3REQ',
    aws_secret_access_key='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'
)
content="String content to write to a new S3 file"
s3.Object('fueb-analitics', 'newfile.txt').put(Body=content)

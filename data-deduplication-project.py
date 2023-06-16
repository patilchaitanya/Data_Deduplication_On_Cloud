import boto3
import hashlib
import os

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)

# Connect to S3
s3 = session.resource('s3')
bucket_name = 'dedup-data-test'

# Specify folder containing files to upload
folder_name = '/home/test_folder'

# Loop through all files in the specified folder
for file_name in os.listdir(folder_name):
    # Generate a hash of the file's contents
    with open(os.path.join(folder_name, file_name), 'rb') as f:
        file_contents = f.read()
    hash = hashlib.md5(file_contents).hexdigest()
    prefix = hash + '/'
    existing_objs = list(s3.Bucket(bucket_name).objects.filter(Prefix=prefix))
    if len(existing_objs) > 0:
        print(f'Skipping {file_name} - hash folder already exists in S3')
    else:
        # Handle the exception here
        print(f'{file_name} does not exist in S3')

    # Upload the file to S3 with the hash as the object key
        s3.Object(bucket_name, hash + '/' + file_name).put(Body=file_contents)
        print(f'Uploaded {file_name} to S3 with key {hash}')

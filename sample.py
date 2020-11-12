import csv
import io
import boto3

'''
def get_s3file(bucket_name, key):
        """
        S3からcsvを読み取る
        """
        s3 = boto3.resource('s3')
        s3obj = s3.Object(bucket_name, key).get()

        return io.TextIOWrapper(io.BytesIO(s3obj['Body'].read()))

if __name__ == '__main__':
    result=get_s3file('realmadridsite', 'que.txt')
    print(result)
'''
BUCKET_NAME = 'realmadridsite'
s3 = boto3.client('s3')
file_name = 'que.txt'
res = s3.get_object(Bucket=BUCKET_NAME, Key=file_name)
body = res['Body'].read() # b'テキストの中身'
bodystr = body.decode('utf-8')
print(bodystr)

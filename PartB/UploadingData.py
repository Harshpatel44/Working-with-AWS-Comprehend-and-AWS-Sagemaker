import boto3
import glob

class s3Api:
    """ Get name of the buckets """
    def listBuckets(self):
        s3 = boto3.client('s3')
        return s3.list_buckets()

    """ Upload a file """
    def fileUpload(self, bucket_name, source_file_name, file_name):
        s3Resource = boto3.resource('s3')
        s3Resource.Object(bucket_name, source_file_name).upload_file(Filename=file_name)
        print('file uploaded')

    def getFile(self,bucket_name, file_name):
        s3 = boto3.client('s3')
        try:
            return s3.get_object(Bucket=bucket_name, Key=file_name)
        except Exception as e:
            print (e)
            return False

s3 = s3Api()
for i in glob.glob("Dataset\Dataset\Train\*.txt"):
    s3.fileUpload("source-data-b00845449",i.split('\\')[-1], i)
print('Training files Upload Successful')

# for i in glob.glob("Dataset\Dataset\Test\*.txt"):
#     s3.fileUpload("source-data-b00845449",i.split('\\')[-1], i)
# print('Testing files Upload Successful')






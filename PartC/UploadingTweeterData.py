import boto3

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

s3 = s3Api()
s3.fileUpload("twitter-data-b00845449","file_mongo_tweets.txt", "file_mongo_tweets.txt")
print('Upload Successful')
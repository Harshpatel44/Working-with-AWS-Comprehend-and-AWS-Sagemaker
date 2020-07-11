import boto3

def triggerComprehend(event,context):
    s3 = boto3.client('s3')
    if(event):
        event_object = event["Records"][0]
        file_name = str(event_object["s3"]["object"]["key"])
        file_object = s3.get_object(Bucket = 'sample-data-b00845449',Key = file_name)
        content = file_object["Body"].read().decode('utf-8')

        client2 = boto3.client('comprehend')
        sentiment = client2.detect_sentiment(Text=content, LanguageCode='en')['Sentiment']
        print(sentiment)
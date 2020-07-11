import boto3

def triggerComprehend(event,context):
    s3 = boto3.client('s3')
    if (event):
        event_object = event["Records"][0]
        file_name = str(event_object["s3"]["object"]["key"])
        file_object = s3.get_object(Bucket='twitter-data-b00845449', Key=file_name)
        content = file_object["Body"].read().decode('utf-8')

        """As all the tweets paragraphs are seperated by 2 lines, 
        I split the paragraphs by '/n/n' and find each tweet sentiments"""
        content = content.replace(b"\n \n", b'\n\n')
        content = content.split(b'\n\n')
        print(content.decode('utf-8'))
        client2 = boto3.client('comprehend')
        for i in content:
            sentiment = client2.detect_sentiment(Text=i.decode('utf-8'), LanguageCode='en')['Sentiment']
            print([i, sentiment])
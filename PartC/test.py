import nltk
file = open("file_mongo_tweets.txt","rb")
content = file.read()
content = content.replace(b"\n \n",b'\n\n')
content = content.split(b'\n\n')
for i in content:
    print(i.decode('utf-8'))


# print(nltk.sent_tokenize(content))
# print(content.split())
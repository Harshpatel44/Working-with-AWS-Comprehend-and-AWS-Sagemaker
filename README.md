# Serverless-A4

<h2> Working with AWS Comprehend </h2>
<p>1. Uploaded a file on a new bucket. </p>
<p>2. Lambda function created with default role, and a new policy added to access Comprehend and logs.</p>
<p>3. Lambda function time and memory size increased to 30 seconds and 256 mb respectively. </p>
<p>4. S3 PUT trigger added to Lambda function so whenever file will be uploaded to S3, this lambda function will be invoked. </p>
<p>5. Comprehend is called to detect sentiment for the file present in the S3 bucket. </p>
<p>6. As Comprehend doesnt take more than 5000 bytes at a time and our text file is quite big, we will now use nltk to sentence tokenize the whole text and pass each sentence one by one.
<p>7. The above way worked fine, but as sentiments of paragraphs are better than a sentence, so I decided to do that. Seeing the file we can notice that all the tweets in the file are 2 line seperated so I split them using '/n/n' and found sentiment of each item of the list </p>
<h2> References </h2>
<i>https://aws.amazon.com/blogs/compute/using-aws-lambda-and-amazon-comprehend-for-sentiment-analysis/</i>

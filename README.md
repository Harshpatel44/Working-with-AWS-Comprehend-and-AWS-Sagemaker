# Serverless-A4

<h2> Working with AWS Comprehend </h2>
<p>1. Uploaded a file on a new bucket. </p>
<p>2. Lambda function created with default role, and a new policy added to access Comprehend and logs.</p>
<p>3. S3 PUT trigger added to Lambda function so whenever file will be uploaded to S3, this lambda function will be invoked. </p>
<p>3. Comprehend is called to detect sentiment for the file present in the S3 bucket. </p>
import boto3
import csv
from nltk.metrics import *
from nltk import data
from nltk import word_tokenize
import uploadS3Api
data.path.append("/opt/nltk_data")

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    if (event):
        event_object = event["Records"][0]
        file_name = str(event_object["s3"]["object"]["key"])
        file_object = s3.get_object(Bucket='source-data-b00845449', Key=file_name)
        content = file_object["Body"].read().decode('utf-8')
        word_tokenized_list = word_tokenize(content)

        # Creating a list for CSV file
        row_list = []
        for i in range(len(word_tokenized_list) - 1):
            distance = edit_distance(word_tokenized_list[i], word_tokenized_list[i + 1])
            row_list.append([word_tokenized_list[i], word_tokenized_list[i + 1], distance])

        if (int(file_name.split(".")[0]) >= 300):
            print("testVector")
            file_name = "testVector.csv"
        else:
            print("trainVector")
            file_name = "trainVector.csv"

        # Check if the existing file is present
        s3 = uploadS3Api.s3Api()
        existing_file = s3.getFile("train-data-b00845449", file_name)

        # Creating new csv file
        if (existing_file == False):
            # Creating a csv file and importing data using row_list[]
            temp_csv_file = csv.writer(open("/tmp/" + file_name, "w+"))
            temp_csv_file.writerow(["Current_Word", "Next_Word", "Levenshtein_distance"])

        # Copying the existing file contents in the csv file
        else:
            file = open("/tmp/" + file_name, "w+")
            file.write(existing_file["Body"].read().decode('utf-8'))
            temp_csv_file = csv.writer(open("/tmp/" + file_name, "w+"))

        # Adding new values to CSV
        for row in row_list:
            temp_csv_file.writerow([row[0], row[1], row[2]])

        # Sending csv file to S3
        s3.fileUpload("train-data-b00845449", file_name, "/tmp/" + file_name)

# lambda_handler(1,1)
## Introduction
The STEDI Team has been hard at work developing a hardware STEDI Step Trainer that:

* trains the user to do a STEDI balance exercise;
* has sensors on the device that collect data to train a machine-learning algorithm to detect steps;
* has a companion mobile app that collects customer data and interacts with the device sensors.

STEDI has heard from millions of early adopters who are willing to purchase the STEDI Step Trainers and use them. Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. The Step Trainer is just a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions.

The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used.

Some of the early adopters have agreed to share their data for research purposes. Only these customers’ Step Trainer and acceleromete

## Project Description
In this project, we will extract the data produced by the STEDI Step Trainer sensors and the mobile app, and curate them into a data lakehouse solution on AWS so that Data Scientists can train the learning model.

## Project Data
STEDI has three JSON data sources to use from the Step Trainer. Check out the JSON data in the following folders in the Github repo linked above:
* customer
* step_trainer
* accelerometer

Here are the steps to download the data:

1. Go to [nd027-Data-Engineering-Data-Lakes-AWS-Exercises](https://github.com/udacity/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/tree/main) repository and click on Download Zip.
2. Extract the zip file.
3. Navigate to the `project/starter` folder in the extracted output to find the JSON data files within three sub-folders. You should have 999 rows in the customer_landing table, 744413 rows in the accelerometer_landing table, and 239760 rows in the step_trainer_landing table.

### Data Folders 
1. **Customer Records (from fulfillment and the STEDI website)**:
    [Data Download URL](https://github.com/udacity/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/tree/main/project/starter/customer)

AWS S3 Bucket URI - 
    
    
    s3://cd0030bucket/customers/
    

contains the following fields:

* *serialnumber, sharewithpublicasofdate, birthday, registrationdate, sharewithresearchasofdate, customername, email, lastupdatedate, phone, sharewithfriendsasofdate*

2. **Step Trainer Records (data from the motion sensor)**:
[Data Download URL](https://github.com/udacity/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/tree/main/project/starter/step_trainer)

AWS S3 Bucket URI - 
  
  s3://cd0030bucket/step_trainer/

contains the following fields:

* *sensorReadingTime, serialNumber, distanceFromObject*

3. **Accelerometer Records (from the mobile app)**:

Data Download URL

AWS S3 Bucket URI - 

  s3://cd0030bucket/accelerometer/

contains the following fields:

* *timeStamp, user, x, y, z*
  
## Project Environment
In order to complete this project, you'll need to use these tools:

* Python and Spark
* AWS Glue
* AWS Athena
* AWS S3

## Project files
`customer_landing_to_trusted.py`: This script filters for customers who have agreed to share data with researchers and transfers customer data from the 'landing' and store those data to 'trusted' zones.<br>
`accelerometer_landing_to_trusted_zone.py`: This script use a join on customer_trusted and accelerometer_landing, filters the Accelerometer readings from customers who have agreed to share data with researchers and transfers accelerometer data from the 'landing' to 'trusted' zones.<br>
`customer_landing.sql`: This script is to create a Glue tables for the customer landing zones.<br>
`accelerometer_landing.sql`: This script is to create a Glue tables for the accelerometer landing zones.<br>
`Customer_trusted_to_curated.py`: This script using a join on customer_trusted and accelerometer_landing, filters the customers with Accelerometer readings and have agreed to share data with researchers and transfers customer data from the 'trusted' to 'curated' zones.<br>
`trainer_trusted_to_curated.py`: This script is used to create an aggregated table that has each of the Step Trainer Readings, and the associated accelerometer reading data for the same timestamp, but only for customers who have agreed to share their data.<br>


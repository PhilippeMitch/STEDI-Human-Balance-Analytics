import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1694190505495 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="accelerometer_landing",
    transformation_ctx="AmazonS3_node1694190505495",
)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi", table_name="customer_trusted", transformation_ctx="S3bucket_node1"
)

# Script generated for node Join
Join_node1694188510599 = Join.apply(
    frame1=S3bucket_node1,
    frame2=AmazonS3_node1694190505495,
    keys1=["email"],
    keys2=["user"],
    transformation_ctx="Join_node1694188510599",
)

# Script generated for node Change Schema
ChangeSchema_node1694188608893 = ApplyMapping.apply(
    frame=Join_node1694188510599,
    mappings=[
        ("customername", "string", "customername", "string"),
        ("email", "string", "email", "string"),
        ("phone", "string", "phone", "string"),
        ("birthday", "string", "birthday", "string"),
        ("serialnumber", "string", "serialnumber", "string"),
        ("registrationdate", "long", "registrationdate", "long"),
        ("lastupdatedate", "long", "lastupdatedate", "long"),
        ("sharewithresearchasofdate", "long", "sharewithresearchasofdate", "long"),
        ("sharewithpublicasofdate", "long", "sharewithpublicasofdate", "long"),
    ],
    transformation_ctx="ChangeSchema_node1694188608893",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node1694188608893,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-project-s3/customer/curated/",
        "partitionKeys": [],
    },
    transformation_ctx="S3bucket_node3",
)

job.commit()

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

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi", table_name="customer_trusted", transformation_ctx="S3bucket_node1"
)

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1694188008243 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="accelerometer_landing",
    transformation_ctx="AccelerometerLanding_node1694188008243",
)

# Script generated for node Join
Join_node1694188510599 = Join.apply(
    frame1=S3bucket_node1,
    frame2=AccelerometerLanding_node1694188008243,
    keys1=["email"],
    keys2=["user"],
    transformation_ctx="Join_node1694188510599",
)

# Script generated for node Change Schema
ChangeSchema_node1694188608893 = ApplyMapping.apply(
    frame=Join_node1694188510599,
    mappings=[
        ("user", "string", "user", "string"),
        ("timestamp", "long", "timestamp", "long"),
        ("x", "float", "x", "float"),
        ("y", "float", "y", "float"),
        ("z", "float", "z", "float"),
    ],
    transformation_ctx="ChangeSchema_node1694188608893",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node1694188608893,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-project-s3/accelerometer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="S3bucket_node3",
)

job.commit()

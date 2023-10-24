
import boto3

from botocore.exceptions import ClientError
import random

class ObjectWrapper:
    
    def hello_s3():
        """
        Use the AWS SDK for Python (Boto3) to create an Amazon Simple Storage Service
        (Amazon S3) resource and list the buckets in your account.
        This example uses the default settings specified in your shared credentials
        and config files.
        """
        s3_resource = boto3.resource("s3")
        print("Hello, Amazon S3! Let's list your buckets:")
        for bucket in s3_resource.buckets.all():
            print(f"\t{bucket.name}")



# snippet-start:[python.example_code.s3.Scenario_ObjectManagement]
def usage_demo():
    print("-" * 88)
    print("Welcome to the Amazon S3 object demo!")
    print("-" * 88)


    s3_resource = boto3.client("s3")
    with open('./static/image/s3-test2.jpg', 'rb') as data:
        
        s3_resource.upload_fileobj(data, 'my-image-jc', 'test2.jpg', ExtraArgs={ "ContentType": "image/jpeg"})
    
    print(f"Put 10 random lines from this script as objects.")
    print("Thanks for watching!")
    print("-" * 88)


# snippet-end:[python.example_code.s3.Scenario_ObjectManagement]


if __name__ == "__main__":
    usage_demo()
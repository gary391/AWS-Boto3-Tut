import boto3

# Using session method

# Create an object of the service you would like to work with.
# Provide credential: Access Keys & Secret Access keys, which can be configured used using AWS configure,
# This is information is store in ~/.aws/credentials file
session = boto3.Session(
    region_name='us-east-1',
    profile_name='sbc-iad-alpha')
s3_res_obj = session.resource('s3')
for each_bu in s3_res_obj.buckets.all():
    print (each_bu.name)
print("="*80)
ec2_res_obj = session.resource('ec2')
for each_in in ec2_res_obj.instances.all():
    print(each_in.id )

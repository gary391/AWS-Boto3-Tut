import boto3
import pprint

# Create a session & client object
session = boto3.Session(region_name="us-east-1", profile_name="sbc-iad-alpha")
ec2_cli = session.client(service_name= 'ec2')
#ec2_re = session.resource(service_name= 'ec2')

# How to get all the regions using boto3

all_regions = ec2_cli.describe_regions()
# pprint.pprint(all_regions['Regions'])

list_of_regions = []
for region in all_regions['Regions']:
    # print(region['RegionName'])
    list_of_regions.append(region['RegionName'])
# print(list_of_regions)

# In order to find instances in all regions within the account, you will have to create a session for each
# regions

for each_region in list_of_regions:
    session = boto3.Session(profile_name="sbc-iad-alpha",region_name=each_region)
    ec2_re = session.resource(service_name='ec2')
    print(f'List of EC2 instances from the region:', each_region)
    for each_in in ec2_re.instances.all():  # ec2_re.instances.all() This represents a list of objects
        # print(each_in) # This is the object
        print(each_in.id, each_in.state['Name'])
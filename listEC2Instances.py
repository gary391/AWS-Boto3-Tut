import boto3
import pprint
# Step1 create a session

session = boto3.Session(region_name="us-east-1", profile_name="sbc-iad-alpha")

ec2_cli = session.client(service_name= 'ec2')

# ec2_re represents the ec2 console page
# Using resource object:

ec2_re = session.resource(service_name= 'ec2')

# Here we are selecting the instances on the ec2 console page, last option is all i.e. you would like to
# display all object
print("Instance information with resource\n")
for each_in in ec2_re.instances.all(): # ec2_re.instances.all() This represents a list of objects
    # print(each_in) # This is the object
    print(each_in.id, each_in.state['Name'])
# NOTE: In the resource, we only get the dictionary at the last step.
# dot operations
print("\n")
print("="*80)
print("\n")
###### USING CLIENT OBJECT

# The first operation will give you a dictionary using the client operation


print("Instance information with client\n")
for each in (ec2_cli.describe_instances()['Reservations']):
    for each_in in (each['Instances']):
        # pprint.pprint (each_in)
        print(each_in['InstanceId'], each_in['State']['Name'])

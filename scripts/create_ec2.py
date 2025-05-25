
import boto3

def launch_instance(subnet_id, ami_id, instance_type="t2.micro", key_name=None):
    ec2 = boto3.client('ec2')
    params = {
        'ImageId': ami_id,
        'InstanceType': instance_type,
        'MinCount': 1,
        'MaxCount': 1,
        'SubnetId': subnet_id
    }
    if key_name:
        params['KeyName'] = key_name
    instance = ec2.run_instances(**params)
    print("Launched EC2 Instance:", instance['Instances'][0]['InstanceId'])

# Example: launch_instance("subnet-abc123", "ami-0abcdef1234567890", "t2.micro")

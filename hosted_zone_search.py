import boto3
import os
import time
import sys
import argparse
from botocore.exceptions import ClientError

#Catch profile name from arg that user will provide&create a parser
parser = argparse.ArgumentParser()
parser.add_argument('--profile','--p', type=str, help='oktaws profile name to be used')
args = parser.parse_args()
prof=args.profile

#Define AWS client
session=boto3.Session(profile_name=prof,region_name="us-east-1")
client = session.client('route53', region_name="us-east-1")

#Ask user to type a hosted zone
hosted_zone = str(input("enter a hosted zone name: "))
#filter hosted zones based on the input
response_hosted_zone = client.list_hosted_zones_by_name(DNSName=hosted_zone, MaxItems='1')
#print the result
output = response_hosted_zone["HostedZones"][0]["Name"]
if hosted_zone in output:
    print(output)
else:
    print("hosted zone not found")

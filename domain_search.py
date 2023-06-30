#Import modules
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
client = session.client('route53domains', region_name="us-east-1")

#Ask user to type a domain name
domain_name = str(input("enter a domain name: "))
#filter domains based on the input
response_domain = client.list_domains(FilterConditions=[{'Name': 'DomainName', 'Operator': 'BEGINS_WITH', 'Values': [domain_name]}])
#print the result
if response_domain["Domains"] == []:
    print("domain not found")
else:
    print(response_domain["Domains"])

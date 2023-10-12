#check the os and only run on macos
import platform
if platform.system() != 'Darwin':
    print('This script only works on MacOS currently')
    exit()

#check if brew install swagger-codegen has been run before 
import subprocess
try:
    subprocess.check_output(['brew', 'list', 'swagger-codegen'])
except subprocess.CalledProcessError as e:
    print('Please run "brew install swagger-codegen" before running this script')
    exit()



# we need to get this openapi spec from the server:  https://api.smccd.edu/v1/directory/docs/specs.yaml 

import requests as r

# get the openapi spec from the server
openapi_spec = r.get('https://api.smccd.edu/v1/directory/docs/specs.yaml').text

# write the openapi spec to a file
with open('specs.yaml', 'w') as f:
    f.write(openapi_spec)


# generate the client
import os

#use java swagger-codegen 
os.system('swagger-codegen generate -DpackageName=smccd_directory -i specs.yaml -l python -o ../smccd_directory_client ')


# remove the openapi spec file
os.remove('specs.yaml')


#sleep for 15 sec to be nice
import time
time.sleep(15)

#same for  https://api.smccd.edu/v1/schedule/docs/specs.yaml 

# get the openapi spec from the server
openapi_spec = r.get('https://api.smccd.edu/v1/schedule/docs/specs.yaml').text

# write the openapi spec to a file
with open('specs.yaml', 'w') as f:
    f.write(openapi_spec)

#use java swagger-codegen
os.system('swagger-codegen generate -DpackageName=smccd_websmart -i specs.yaml -l python -o ../smccd_schedule_client')

# remove the openapi spec file
os.remove('specs.yaml')


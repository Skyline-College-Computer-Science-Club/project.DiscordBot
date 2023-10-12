# smccd_directory.EmailApi

All URIs are relative to *https://api.smccd.edu/v1/directory*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_directory_by_email**](EmailApi.md#get_directory_by_email) | **GET** /email/{email} | Get directory information by email in url path

# **get_directory_by_email**
> ApiResponse get_directory_by_email(email)

Get directory information by email in url path

Returns relevent person from the directory

### Example
```python
from __future__ import print_function
import time
import smccd_directory
from smccd_directory.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: directory_auth
configuration = smccd_directory.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = smccd_directory.EmailApi(smccd_directory.ApiClient(configuration))
email = 'email_example' # str | Full email address (must be @smccd.edu)

try:
    # Get directory information by email in url path
    api_response = api_instance.get_directory_by_email(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->get_directory_by_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Full email address (must be @smccd.edu) | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[directory_auth](../README.md#directory_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+xml, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


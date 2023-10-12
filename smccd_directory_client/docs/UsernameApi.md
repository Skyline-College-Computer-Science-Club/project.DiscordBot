# smccd_directory.UsernameApi

All URIs are relative to *https://api.smccd.edu/v1/directory*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_directory_by_username**](UsernameApi.md#get_directory_by_username) | **GET** /users/{username} | Get directory information by username in url path
[**get_photo_by_user_email**](UsernameApi.md#get_photo_by_user_email) | **GET** /users/{email}/photo | Get directory information by username in url path

# **get_directory_by_username**
> ApiResponse get_directory_by_username(username)

Get directory information by username in url path

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
api_instance = smccd_directory.UsernameApi(smccd_directory.ApiClient(configuration))
username = 'username_example' # str | SAM Account Name

try:
    # Get directory information by username in url path
    api_response = api_instance.get_directory_by_username(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsernameApi->get_directory_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| SAM Account Name | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[directory_auth](../README.md#directory_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+xml, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_photo_by_user_email**
> get_photo_by_user_email(email)

Get directory information by username in url path

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
api_instance = smccd_directory.UsernameApi(smccd_directory.ApiClient(configuration))
email = 'email_example' # str | Full email address (must be @smccd.edu)

try:
    # Get directory information by username in url path
    api_instance.get_photo_by_user_email(email)
except ApiException as e:
    print("Exception when calling UsernameApi->get_photo_by_user_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Full email address (must be @smccd.edu) | 

### Return type

void (empty response body)

### Authorization

[directory_auth](../README.md#directory_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+xml, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


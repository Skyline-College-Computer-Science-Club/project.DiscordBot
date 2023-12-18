# smccd_directory.LocationApi

All URIs are relative to *https://api.smccd.edu/v1/directory*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_directory_by_location**](LocationApi.md#get_directory_by_location) | **GET** /location/{location} | List directory by location in url path
[**get_directory_by_location_query**](LocationApi.md#get_directory_by_location_query) | **GET** /location | List directory by optional location query parameter

# **get_directory_by_location**
> ApiResponse get_directory_by_location(location)

List directory by location in url path

Returns a collection of directory entries

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
api_instance = smccd_directory.LocationApi(smccd_directory.ApiClient(configuration))
location = 'location_example' # str | Location of directory to return (skyline, csm, canada, district)

try:
    # List directory by location in url path
    api_response = api_instance.get_directory_by_location(location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->get_directory_by_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location of directory to return (skyline, csm, canada, district) | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[directory_auth](../README.md#directory_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+xml, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_by_location_query**
> ApiResponse get_directory_by_location_query(location=location)

List directory by optional location query parameter

Returns a collection of directory entries

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
api_instance = smccd_directory.LocationApi(smccd_directory.ApiClient(configuration))
location = 'location_example' # str | (Optional) Location of directory to return (skyline, csm, canada, district). Without any query parameter, the whole directory listing will return. (optional)

try:
    # List directory by optional location query parameter
    api_response = api_instance.get_directory_by_location_query(location=location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->get_directory_by_location_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| (Optional) Location of directory to return (skyline, csm, canada, district). Without any query parameter, the whole directory listing will return. | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[directory_auth](../README.md#directory_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+xml, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


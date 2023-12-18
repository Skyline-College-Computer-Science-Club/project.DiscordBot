# smccd_websmart.CoursesApi

All URIs are relative to *https://api.smccd.edu/v1/schedule*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_courses_by_crn**](CoursesApi.md#get_courses_by_crn) | **GET** /courses/{crn} | Get course with CRN
[**get_courses_by_query**](CoursesApi.md#get_courses_by_query) | **GET** /courses | List courses with optional query parameters
[**get_courses_by_term_crn**](CoursesApi.md#get_courses_by_term_crn) | **GET** /courses/{term_code}/{crn} | Get course with term code and crn

# **get_courses_by_crn**
> ApiResponse get_courses_by_crn(crn)

Get course with CRN

Returns a single course within available terms

### Example
```python
from __future__ import print_function
import time
import smccd_websmart
from smccd_websmart.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: directory_auth
configuration = smccd_websmart.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = smccd_websmart.CoursesApi(smccd_websmart.ApiClient(configuration))
crn = 1.2 # float | CRN number of the course

try:
    # Get course with CRN
    api_response = api_instance.get_courses_by_crn(crn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->get_courses_by_crn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crn** | **float**| CRN number of the course | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[directory_auth](../README.md#directory_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+xml, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_courses_by_query**
> ApiResponse get_courses_by_query(limit=limit, page=page, s=s, crn=crn, college_code=college_code, college_desc=college_desc, term_code=term_code, term_desc=term_desc, department_desc=department_desc, course_types=course_types, instructor=instructor, instructor_first_name=instructor_first_name, instructor_last_name=instructor_last_name, day=day, evening=evening, day_or_evening_code=day_or_evening_code, days=days, units=units, min_units=min_units, max_units=max_units, meet_begin_time=meet_begin_time, meet_end_time=meet_end_time)

List courses with optional query parameters

Returns a paged collection of 20 courses by default

### Example
```python
from __future__ import print_function
import time
import smccd_websmart
from smccd_websmart.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: directory_auth
configuration = smccd_websmart.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = smccd_websmart.CoursesApi(smccd_websmart.ApiClient(configuration))
limit = 1.2 # float | Limiting number of courses to return.    * Default is set to `20`. Setting `-1` will returns all courses and sections information from currently available terms. (optional)
page = 1.2 # float | Page number.   * To get the courses list starts from `101th` course to `120th` course, set      `page=6`. Calaculated as `6 x 20` (`20` is the default limit value).   * To get the 55<sup>th</sup> course will need to combine with `limit` filter.     `page=55&limit=1`  (optional)
s = 's_example' # str | Get coursess by search keywords in CRN, Department, Subject code, Course number, Instructor first name, and Instructor last name.  (optional)
crn = [3.4] # list[float] | Get courses by CRN.   URL query string can be in a single number (or) in comma seperated string (or) multiple of `crn[]` values. * `crn=50001` (or) `crn=50001, 50003` (or) `crn[]=50001&crn[]=50003`.  (optional)
college_code = [3.4] # list[float] | Get courses by college code.   URL query string can be in a single number (or) in comma seperated string (or) multiple of `college_code[]` values.   * `college_code = 2` (or) `college_code = 2, 3` (or) `college_code[]=2&college_code[]=3`.   * *Only one `college_code` or `college_desc` should be in the query. `college_code` will be prioritized over `college_desc`.*  (optional)
college_desc = ['college_desc_example'] # list[str] | Get courses by college description.   URL query string can be in a single string (or) in comma seperated string (or) multiple of `college_desc[]` values.    * `college_desc = skyline college` (or) `college_desc = skyline college, canada college` (or) `college_desc[]=skyline college&college_desc[]=canada college`.   * *Only one `college_code` or `college_desc` should be in the query. `college_code` will be prioritized over `college_desc`.*  (optional)
term_code = [3.4] # list[float] | Get course by term code.   URL query string can be in a single number (or) in comma seperated string (or) multiple of `term_code[]` values.   * `term_code = 201705` (or) `term_code = 201705, 201708` (or) `term_code[]=201705&term_code[]=201708`.  (optional)
term_desc = ['term_desc_example'] # list[str] | Get course by term description.   URL query string can be in a single string (or) in comma seperated string (or) multiple of `term_desc[]` values.   * `term_desc = Summer 2017` (or) `term_code = Summer 2017, Fall 2017` (or) `term_desc[]=Summer 2017&term_desc[]=Fall 2017`.  (optional)
department_desc = 'department_desc_example' # str | Get course by department description. Query string must be in a single string value.  (optional)
course_types = ['course_types_example'] # list[str] | Get courses by course types. Available course types are - honor, hybrid, webbased, xlo, spanish, offsite_ind, supplemental_instruction, learning_community, fast_track_transfer.  (optional)
instructor = 'instructor_example' # str | Get courses by Instructor first or last name.  (optional)
instructor_first_name = 'instructor_first_name_example' # str | Get courses by Instructor First name.  (optional)
instructor_last_name = 'instructor_last_name_example' # str | Get courses by Instructor Last name.  (optional)
day = 'day_example' # str | Get courses by Day class time.  (optional)
evening = 'evening_example' # str | Get courses by Evening class time.  (optional)
day_or_evening_code = 'day_or_evening_code_example' # str | Get courses by Day or Evening class time.  (optional)
days = ['days_example'] # list[str] | Get courses by Days of a week.  (optional)
units = 1.2 # float | Get courses by units.  (optional)
min_units = 1.2 # float | Get courses by minimum units.  (optional)
max_units = 1.2 # float | Get courses by maximum units.  (optional)
meet_begin_time = 'meet_begin_time_example' # str | Get courses by meeting begin time. The time values are in 4 digits 24 hours format. 8am will be 0800 and 4.30pm will be 1630.  (optional)
meet_end_time = 1.2 # float | Get courses by meeting end time. The time values are in 4 digits 24 hours format. 8am will be 0800 and 4.30pm will be 1630.  (optional)

try:
    # List courses with optional query parameters
    api_response = api_instance.get_courses_by_query(limit=limit, page=page, s=s, crn=crn, college_code=college_code, college_desc=college_desc, term_code=term_code, term_desc=term_desc, department_desc=department_desc, course_types=course_types, instructor=instructor, instructor_first_name=instructor_first_name, instructor_last_name=instructor_last_name, day=day, evening=evening, day_or_evening_code=day_or_evening_code, days=days, units=units, min_units=min_units, max_units=max_units, meet_begin_time=meet_begin_time, meet_end_time=meet_end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->get_courses_by_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Limiting number of courses to return.    * Default is set to &#x60;20&#x60;. Setting &#x60;-1&#x60; will returns all courses and sections information from currently available terms. | [optional] 
 **page** | **float**| Page number.   * To get the courses list starts from &#x60;101th&#x60; course to &#x60;120th&#x60; course, set      &#x60;page&#x3D;6&#x60;. Calaculated as &#x60;6 x 20&#x60; (&#x60;20&#x60; is the default limit value).   * To get the 55&lt;sup&gt;th&lt;/sup&gt; course will need to combine with &#x60;limit&#x60; filter.     &#x60;page&#x3D;55&amp;limit&#x3D;1&#x60;  | [optional] 
 **s** | **str**| Get coursess by search keywords in CRN, Department, Subject code, Course number, Instructor first name, and Instructor last name.  | [optional] 
 **crn** | [**list[float]**](float.md)| Get courses by CRN.   URL query string can be in a single number (or) in comma seperated string (or) multiple of &#x60;crn[]&#x60; values. * &#x60;crn&#x3D;50001&#x60; (or) &#x60;crn&#x3D;50001, 50003&#x60; (or) &#x60;crn[]&#x3D;50001&amp;crn[]&#x3D;50003&#x60;.  | [optional] 
 **college_code** | [**list[float]**](float.md)| Get courses by college code.   URL query string can be in a single number (or) in comma seperated string (or) multiple of &#x60;college_code[]&#x60; values.   * &#x60;college_code &#x3D; 2&#x60; (or) &#x60;college_code &#x3D; 2, 3&#x60; (or) &#x60;college_code[]&#x3D;2&amp;college_code[]&#x3D;3&#x60;.   * *Only one &#x60;college_code&#x60; or &#x60;college_desc&#x60; should be in the query. &#x60;college_code&#x60; will be prioritized over &#x60;college_desc&#x60;.*  | [optional] 
 **college_desc** | [**list[str]**](str.md)| Get courses by college description.   URL query string can be in a single string (or) in comma seperated string (or) multiple of &#x60;college_desc[]&#x60; values.    * &#x60;college_desc &#x3D; skyline college&#x60; (or) &#x60;college_desc &#x3D; skyline college, canada college&#x60; (or) &#x60;college_desc[]&#x3D;skyline college&amp;college_desc[]&#x3D;canada college&#x60;.   * *Only one &#x60;college_code&#x60; or &#x60;college_desc&#x60; should be in the query. &#x60;college_code&#x60; will be prioritized over &#x60;college_desc&#x60;.*  | [optional] 
 **term_code** | [**list[float]**](float.md)| Get course by term code.   URL query string can be in a single number (or) in comma seperated string (or) multiple of &#x60;term_code[]&#x60; values.   * &#x60;term_code &#x3D; 201705&#x60; (or) &#x60;term_code &#x3D; 201705, 201708&#x60; (or) &#x60;term_code[]&#x3D;201705&amp;term_code[]&#x3D;201708&#x60;.  | [optional] 
 **term_desc** | [**list[str]**](str.md)| Get course by term description.   URL query string can be in a single string (or) in comma seperated string (or) multiple of &#x60;term_desc[]&#x60; values.   * &#x60;term_desc &#x3D; Summer 2017&#x60; (or) &#x60;term_code &#x3D; Summer 2017, Fall 2017&#x60; (or) &#x60;term_desc[]&#x3D;Summer 2017&amp;term_desc[]&#x3D;Fall 2017&#x60;.  | [optional] 
 **department_desc** | **str**| Get course by department description. Query string must be in a single string value.  | [optional] 
 **course_types** | [**list[str]**](str.md)| Get courses by course types. Available course types are - honor, hybrid, webbased, xlo, spanish, offsite_ind, supplemental_instruction, learning_community, fast_track_transfer.  | [optional] 
 **instructor** | **str**| Get courses by Instructor first or last name.  | [optional] 
 **instructor_first_name** | **str**| Get courses by Instructor First name.  | [optional] 
 **instructor_last_name** | **str**| Get courses by Instructor Last name.  | [optional] 
 **day** | **str**| Get courses by Day class time.  | [optional] 
 **evening** | **str**| Get courses by Evening class time.  | [optional] 
 **day_or_evening_code** | **str**| Get courses by Day or Evening class time.  | [optional] 
 **days** | [**list[str]**](str.md)| Get courses by Days of a week.  | [optional] 
 **units** | **float**| Get courses by units.  | [optional] 
 **min_units** | **float**| Get courses by minimum units.  | [optional] 
 **max_units** | **float**| Get courses by maximum units.  | [optional] 
 **meet_begin_time** | **str**| Get courses by meeting begin time. The time values are in 4 digits 24 hours format. 8am will be 0800 and 4.30pm will be 1630.  | [optional] 
 **meet_end_time** | **float**| Get courses by meeting end time. The time values are in 4 digits 24 hours format. 8am will be 0800 and 4.30pm will be 1630.  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[directory_auth](../README.md#directory_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+xml, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_courses_by_term_crn**
> ApiResponse get_courses_by_term_crn(term_code, crn)

Get course with term code and crn

Returns a single course within available terms

### Example
```python
from __future__ import print_function
import time
import smccd_websmart
from smccd_websmart.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: directory_auth
configuration = smccd_websmart.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = smccd_websmart.CoursesApi(smccd_websmart.ApiClient(configuration))
term_code = 1.2 # float | Term code of the year (eg. 201705 = Summer 2017)
crn = 1.2 # float | CRN number of the course (eg. 50001)

try:
    # Get course with term code and crn
    api_response = api_instance.get_courses_by_term_crn(term_code, crn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->get_courses_by_term_crn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_code** | **float**| Term code of the year (eg. 201705 &#x3D; Summer 2017) | 
 **crn** | **float**| CRN number of the course (eg. 50001) | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[directory_auth](../README.md#directory_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+xml, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


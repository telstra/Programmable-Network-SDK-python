# TelstraTPN.AuthenticationApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_generatetoken_post**](AuthenticationApi.md#auth_generatetoken_post) | **POST** /1.0.0/auth/generatetoken | Create an authentication token
[**auth_validatetoken_get**](AuthenticationApi.md#auth_validatetoken_get) | **GET** /1.0.0/auth/validatetoken | Validate authentication token


# **auth_generatetoken_post**
> AuthGeneratetokenResponse auth_generatetoken_post(grant_type, username, password)

Create an authentication token

Create an authentication token

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.AuthenticationApi()
grant_type = 'grant_type_example' # str | 
username = 'username_example' # str | 
password = 'password_example' # str | 

try:
    # Create an authentication token
    api_response = api_instance.auth_generatetoken_post(grant_type, username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_generatetoken_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  | 
 **username** | **str**|  | 
 **password** | **str**|  | 

### Return type

[**AuthGeneratetokenResponse**](AuthGeneratetokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_validatetoken_get**
> AuthValidatetokenResponse auth_validatetoken_get()

Validate authentication token

Validate the authentication token and get information about the user (roles, permissions, etc.)

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.AuthenticationApi()

try:
    # Validate authentication token
    api_response = api_instance.auth_validatetoken_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_validatetoken_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthValidatetokenResponse**](AuthValidatetokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


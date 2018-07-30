# TelstraTPN.AuthenticationApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_token**](AuthenticationApi.md#generate_token) | **POST** /1.0.0/auth/generatetoken | Create an authentication token
[**validate_token**](AuthenticationApi.md#validate_token) | **GET** /1.0.0/auth/validatetoken | Validate authentication token


# **generate_token**
> InlineResponse20015 generate_token(grant_type, username, password)

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
grant_type = 'password' # str |  (default to 'password')
username = 'username_example' # str | 
password = 'password_example' # str | 

try:
    # Create an authentication token
    api_response = api_instance.generate_token(grant_type, username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->generate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  | [default to &#39;password&#39;]
 **username** | **str**|  | 
 **password** | **str**|  | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_token**
> InlineResponse20016 validate_token()

Validate authentication token

Validate the authentication token and get information about the user (roles, permissions, etc.)

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oAuth2
configuration = TelstraTPN.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.AuthenticationApi(TelstraTPN.ApiClient(configuration))

try:
    # Validate authentication token
    api_response = api_instance.validate_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->validate_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


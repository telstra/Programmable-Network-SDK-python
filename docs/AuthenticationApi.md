# TelstraTPN.AuthenticationApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_generatetoken_post**](AuthenticationApi.md#auth_generatetoken_post) | **POST** /1.0.0/auth/generatetoken | authgeneratetokenpost
[**auth_validatetoken_get**](AuthenticationApi.md#auth_validatetoken_get) | **GET** /1.0.0/auth/validatetoken | authvalidatetokenget


# **auth_generatetoken_post**
> AuthgeneratetokenpostResponse auth_generatetoken_post(grant_type, username, password)

authgeneratetokenpost

Create an authentication token

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = TelstraTPN.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.AuthenticationApi(TelstraTPN.ApiClient(configuration))
grant_type = 'grant_type_example' # str | 
username = 'username_example' # str | 
password = 'password_example' # str | 

try:
    # authgeneratetokenpost
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

[**AuthgeneratetokenpostResponse**](AuthgeneratetokenpostResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_validatetoken_get**
> AuthvalidatetokengetResponse auth_validatetoken_get()

authvalidatetokenget

Validate the authentication token and get information about the user (roles, permissions, etc.)

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = TelstraTPN.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.AuthenticationApi(TelstraTPN.ApiClient(configuration))

try:
    # authvalidatetokenget
    api_response = api_instance.auth_validatetoken_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_validatetoken_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthvalidatetokengetResponse**](AuthvalidatetokengetResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


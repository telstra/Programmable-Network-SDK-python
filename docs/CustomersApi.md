# TelstraTPN.CustomersApi

All URIs are relative to *https://penapi.pacnetconnect.com/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_customeruuid_get**](CustomersApi.md#account_customeruuid_get) | **GET** /account/{customeruuid}/ | Get account information details
[**account_customeruuid_user_get**](CustomersApi.md#account_customeruuid_user_get) | **GET** /account/{customeruuid}/user/ | List users


# **account_customeruuid_get**
> InlineResponse20017 account_customeruuid_get(customeruuid)

Get account information details

Get the account information for the specified customer

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
api_instance = TelstraTPN.CustomersApi(TelstraTPN.ApiClient(configuration))
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try:
    # Get account information details
    api_response = api_instance.account_customeruuid_get(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->account_customeruuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jsonapplication/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_customeruuid_user_get**
> list[User] account_customeruuid_user_get(customeruuid)

List users

List all users associated with the specified customer

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
api_instance = TelstraTPN.CustomersApi(TelstraTPN.ApiClient(configuration))
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try:
    # List users
    api_response = api_instance.account_customeruuid_user_get(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->account_customeruuid_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**list[User]**](User.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# TelstraTPN.CustomersApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_information_details**](CustomersApi.md#get_account_information_details) | **GET** /1.0.0/account/{customeruuid} | Get account information details
[**list_users**](CustomersApi.md#list_users) | **GET** /1.0.0/account/{customeruuid}/user | List users


# **get_account_information_details**
> Model100AccountResponse get_account_information_details(customeruuid)

Get account information details

Get the account information for the specified customer

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.CustomersApi()
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try: 
    # Get account information details
    api_response = api_instance.get_account_information_details(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_account_information_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**Model100AccountResponse**](Model100AccountResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> list[User] list_users(customeruuid)

List users

List all users associated with the specified customer

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.CustomersApi()
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try: 
    # List users
    api_response = api_instance.list_users(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**list[User]**](User.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


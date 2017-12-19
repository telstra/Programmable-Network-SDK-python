# TelstraTPN.CustomersApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**100_account_by_customeruuid_get**](CustomersApi.md#100_account_by_customeruuid_get) | **GET** /1.0.0/account/{customeruuid} | Get account information details
[**100_account_user_by_customeruuid_get**](CustomersApi.md#100_account_user_by_customeruuid_get) | **GET** /1.0.0/account/{customeruuid}/user | List users


# **100_account_by_customeruuid_get**
> Model100AccountResponse 100_account_by_customeruuid_get(customeruuid)

Get account information details

Get the account information for the specified customer

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.CustomersApi()
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try: 
    # Get account information details
    api_response = api_instance.100_account_by_customeruuid_get(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->100_account_by_customeruuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**Model100AccountResponse**](Model100AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **100_account_user_by_customeruuid_get**
> list[User] 100_account_user_by_customeruuid_get(customeruuid)

List users

List all users associated with the specified customer

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.CustomersApi()
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try: 
    # List users
    api_response = api_instance.100_account_user_by_customeruuid_get(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->100_account_user_by_customeruuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


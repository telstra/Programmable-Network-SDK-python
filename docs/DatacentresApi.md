# TelstraTPN.DatacentresApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_of_all_the_data_centers**](DatacentresApi.md#get_list_of_all_the_data_centers) | **GET** /1.0.0/inventory/datacenters | Get list of all the data centers


# **get_list_of_all_the_data_centers**
> list[Model100InventoryDatacentersResponse] get_list_of_all_the_data_centers()

Get list of all the data centers

Get list of all the data centers

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
api_instance = TelstraTPN.DatacentresApi()

try: 
    # Get list of all the data centers
    api_response = api_instance.get_list_of_all_the_data_centers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatacentresApi->get_list_of_all_the_data_centers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Model100InventoryDatacentersResponse]**](Model100InventoryDatacentersResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


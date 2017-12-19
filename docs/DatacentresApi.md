# TelstraTPN.DatacentresApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**100_inventory_datacenters_get**](DatacentresApi.md#100_inventory_datacenters_get) | **GET** /1.0.0/inventory/datacenters | Get list of all the data centers


# **100_inventory_datacenters_get**
> list[Model100InventoryDatacentersResponse] 100_inventory_datacenters_get()

Get list of all the data centers

Get list of all the data centers

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.DatacentresApi()

try: 
    # Get list of all the data centers
    api_response = api_instance.100_inventory_datacenters_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatacentresApi->100_inventory_datacenters_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Model100InventoryDatacentersResponse]**](Model100InventoryDatacentersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


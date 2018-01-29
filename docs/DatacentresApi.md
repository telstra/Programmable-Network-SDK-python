# TelstraTPN.DatacentresApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_datacenters_get**](DatacentresApi.md#inventory_datacenters_get) | **GET** /1.0.0/inventory/datacenters | inventorydatacentersget


# **inventory_datacenters_get**
> InventorydatacentersgetResponse inventory_datacenters_get()

inventorydatacentersget

Get list of all the data centers

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
api_instance = TelstraTPN.DatacentresApi(TelstraTPN.ApiClient(configuration))

try:
    # inventorydatacentersget
    api_response = api_instance.inventory_datacenters_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatacentresApi->inventory_datacenters_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InventorydatacentersgetResponse**](InventorydatacentersgetResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


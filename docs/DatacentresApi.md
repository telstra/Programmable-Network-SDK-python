# TelstraTPN.DatacentresApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventorydatacentersget**](DatacentresApi.md#inventorydatacentersget) | **GET** /1.0.0/inventory/datacenters | Get list of all the data centers


# **inventorydatacentersget**
> Datacenterget inventorydatacentersget()

Get list of all the data centers

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
api_instance = TelstraTPN.DatacentresApi(TelstraTPN.ApiClient(configuration))

try:
    # Get list of all the data centers
    api_response = api_instance.inventorydatacentersget()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatacentresApi->inventorydatacentersget: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Datacenterget**](Datacenterget.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


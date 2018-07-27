# TelstraTPN.DatacentresApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_datacentres**](DatacentresApi.md#inventory_datacentres) | **GET** /1.0.0/inventory/datacenters | Get list of all the data centers


# **inventory_datacentres**
> InlineResponse200 inventory_datacentres()

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
    api_response = api_instance.inventory_datacentres()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatacentresApi->inventory_datacentres: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


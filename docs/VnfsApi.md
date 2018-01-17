# TelstraTPN.VnfsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marketplace_image_get**](VnfsApi.md#marketplace_image_get) | **GET** /1.0.0/marketplace/image | List images in the Marketplace


# **marketplace_image_get**
> MarketplaceImageResponse marketplace_image_get()

List images in the Marketplace

List images in the Marketplace

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))

try:
    # List images in the Marketplace
    api_response = api_instance.marketplace_image_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketplaceImageResponse**](MarketplaceImageResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


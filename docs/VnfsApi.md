# TelstraTPN.VnfsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_images_in_the_marketplace**](VnfsApi.md#list_images_in_the_marketplace) | **GET** /1.0.0/marketplace/image | List images in the Marketplace


# **list_images_in_the_marketplace**
> Model100MarketplaceImageResponse list_images_in_the_marketplace()

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
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.VnfsApi()

try: 
    # List images in the Marketplace
    api_response = api_instance.list_images_in_the_marketplace()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->list_images_in_the_marketplace: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Model100MarketplaceImageResponse**](Model100MarketplaceImageResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


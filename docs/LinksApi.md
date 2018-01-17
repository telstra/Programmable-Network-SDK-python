# TelstraTPN.LinksApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_link_post**](LinksApi.md#inventory_link_post) | **POST** /1.0.0/inventory/link | Create Link and initial Contract
[**inventory_links_by_linkid_get**](LinksApi.md#inventory_links_by_linkid_get) | **GET** /1.0.0/inventory/links/{linkid} | Get details of specified link
[**inventory_links_customer_by_customeruuid_get**](LinksApi.md#inventory_links_customer_by_customeruuid_get) | **GET** /1.0.0/inventory/links/customer/{customeruuid} | Get active Links
[**inventory_links_history_by_linkid_get**](LinksApi.md#inventory_links_history_by_linkid_get) | **GET** /1.0.0/inventory/links/history/{linkid} | Get Link history


# **inventory_link_post**
> InventoryLinkResponse inventory_link_post(body=body)

Create Link and initial Contract

Create Link and initial Contract

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
api_instance = TelstraTPN.LinksApi(TelstraTPN.ApiClient(configuration))
body = TelstraTPN.InventoryLinkRequest() # InventoryLinkRequest |  (optional)

try:
    # Create Link and initial Contract
    api_response = api_instance.inventory_link_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->inventory_link_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryLinkRequest**](InventoryLinkRequest.md)|  | [optional] 

### Return type

[**InventoryLinkResponse**](InventoryLinkResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_by_linkid_get**
> InventoryLinksResponse inventory_links_by_linkid_get(linkid)

Get details of specified link

Get details of specified link

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
api_instance = TelstraTPN.LinksApi(TelstraTPN.ApiClient(configuration))
linkid = 'linkid_example' # str | Unique identifier representing a specific link

try:
    # Get details of specified link
    api_response = api_instance.inventory_links_by_linkid_get(linkid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->inventory_links_by_linkid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 

### Return type

[**InventoryLinksResponse**](InventoryLinksResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_customer_by_customeruuid_get**
> list[Link] inventory_links_customer_by_customeruuid_get(customeruuid)

Get active Links

Get active Links

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
api_instance = TelstraTPN.LinksApi(TelstraTPN.ApiClient(configuration))
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try:
    # Get active Links
    api_response = api_instance.inventory_links_customer_by_customeruuid_get(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->inventory_links_customer_by_customeruuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**list[Link]**](Link.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_history_by_linkid_get**
> InventoryLinksHistoryResponse inventory_links_history_by_linkid_get(linkid)

Get Link history

Get Link history

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
api_instance = TelstraTPN.LinksApi(TelstraTPN.ApiClient(configuration))
linkid = 'linkid_example' # str | Unique identifier representing a specific link

try:
    # Get Link history
    api_response = api_instance.inventory_links_history_by_linkid_get(linkid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->inventory_links_history_by_linkid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 

### Return type

[**InventoryLinksHistoryResponse**](InventoryLinksHistoryResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


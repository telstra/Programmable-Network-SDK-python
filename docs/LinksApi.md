# TelstraTPN.LinksApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**100_inventory_link_post**](LinksApi.md#100_inventory_link_post) | **POST** /1.0.0/inventory/link | Create Link and initial Contract
[**100_inventory_links_by_linkid_get**](LinksApi.md#100_inventory_links_by_linkid_get) | **GET** /1.0.0/inventory/links/{linkid} | Get details of specified link
[**100_inventory_links_customer_by_customeruuid_get**](LinksApi.md#100_inventory_links_customer_by_customeruuid_get) | **GET** /1.0.0/inventory/links/customer/{customeruuid} | Get active Links
[**100_inventory_links_history_by_linkid_get**](LinksApi.md#100_inventory_links_history_by_linkid_get) | **GET** /1.0.0/inventory/links/history/{linkid} | Get Link history


# **100_inventory_link_post**
> Model100InventoryLinkResponse 100_inventory_link_post(body=body)

Create Link and initial Contract

Create Link and initial Contract

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.LinksApi()
body = TelstraTPN.Model100InventoryLinkRequest() # Model100InventoryLinkRequest |  (optional)

try: 
    # Create Link and initial Contract
    api_response = api_instance.100_inventory_link_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->100_inventory_link_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model100InventoryLinkRequest**](Model100InventoryLinkRequest.md)|  | [optional] 

### Return type

[**Model100InventoryLinkResponse**](Model100InventoryLinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **100_inventory_links_by_linkid_get**
> Model100InventoryLinksResponse 100_inventory_links_by_linkid_get(linkid)

Get details of specified link

Get details of specified link

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.LinksApi()
linkid = 'linkid_example' # str | Unique identifier representing a specific link

try: 
    # Get details of specified link
    api_response = api_instance.100_inventory_links_by_linkid_get(linkid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->100_inventory_links_by_linkid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 

### Return type

[**Model100InventoryLinksResponse**](Model100InventoryLinksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **100_inventory_links_customer_by_customeruuid_get**
> list[Link] 100_inventory_links_customer_by_customeruuid_get(customeruuid)

Get active Links

Get active Links

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.LinksApi()
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try: 
    # Get active Links
    api_response = api_instance.100_inventory_links_customer_by_customeruuid_get(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->100_inventory_links_customer_by_customeruuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**list[Link]**](Link.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **100_inventory_links_history_by_linkid_get**
> Model100InventoryLinksHistoryResponse 100_inventory_links_history_by_linkid_get(linkid)

Get Link history

Get Link history

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.LinksApi()
linkid = 'linkid_example' # str | Unique identifier representing a specific link

try: 
    # Get Link history
    api_response = api_instance.100_inventory_links_history_by_linkid_get(linkid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->100_inventory_links_history_by_linkid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 

### Return type

[**Model100InventoryLinksHistoryResponse**](Model100InventoryLinksHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


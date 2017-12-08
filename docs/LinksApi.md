# TelstraTPN.LinksApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_link_and_initial_contract**](LinksApi.md#create_link_and_initial_contract) | **POST** /1.0.0/inventory/link | Create Link and initial Contract
[**get_active_links**](LinksApi.md#get_active_links) | **GET** /1.0.0/inventory/links/customer/{customeruuid} | Get active Links
[**get_details_of_specified_link**](LinksApi.md#get_details_of_specified_link) | **GET** /1.0.0/inventory/links/{linkid} | Get details of specified link
[**get_link_history**](LinksApi.md#get_link_history) | **GET** /1.0.0/inventory/links/history/{linkid} | Get Link history


# **create_link_and_initial_contract**
> Model100InventoryLinkResponse create_link_and_initial_contract(body=body)

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
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.LinksApi()
body = TelstraTPN.Model100InventoryLinkRequest() # Model100InventoryLinkRequest |  (optional)

try: 
    # Create Link and initial Contract
    api_response = api_instance.create_link_and_initial_contract(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->create_link_and_initial_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model100InventoryLinkRequest**](Model100InventoryLinkRequest.md)|  | [optional] 

### Return type

[**Model100InventoryLinkResponse**](Model100InventoryLinkResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_links**
> list[Link] get_active_links(customeruuid)

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
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.LinksApi()
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try: 
    # Get active Links
    api_response = api_instance.get_active_links(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->get_active_links: %s\n" % e)
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

# **get_details_of_specified_link**
> Model100InventoryLinksResponse get_details_of_specified_link(linkid)

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
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.LinksApi()
linkid = 'linkid_example' # str | Unique identifier representing a specific link

try: 
    # Get details of specified link
    api_response = api_instance.get_details_of_specified_link(linkid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->get_details_of_specified_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 

### Return type

[**Model100InventoryLinksResponse**](Model100InventoryLinksResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link_history**
> Model100InventoryLinksHistoryResponse get_link_history(linkid)

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
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.LinksApi()
linkid = 'linkid_example' # str | Unique identifier representing a specific link

try: 
    # Get Link history
    api_response = api_instance.get_link_history(linkid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->get_link_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 

### Return type

[**Model100InventoryLinksHistoryResponse**](Model100InventoryLinksHistoryResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


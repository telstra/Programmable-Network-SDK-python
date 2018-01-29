# TelstraTPN.ContractsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_links_contract_by_linkid_and_contractid_get**](ContractsApi.md#inventory_links_contract_by_linkid_and_contractid_get) | **GET** /1.0.0/inventory/links/{linkid}/contract/{contractid} | inventorylinksget
[**inventory_links_contract_by_linkid_and_contractid_put**](ContractsApi.md#inventory_links_contract_by_linkid_and_contractid_put) | **PUT** /1.0.0/inventory/links/{linkid}/contract/{contractid} | inventorylinksput
[**inventory_links_contract_by_linkid_post**](ContractsApi.md#inventory_links_contract_by_linkid_post) | **POST** /1.0.0/inventory/links/{linkid}/contract | inventorylinkslinkidcontractpost


# **inventory_links_contract_by_linkid_and_contractid_get**
> InventorylinksgetResponse inventory_links_contract_by_linkid_and_contractid_get(linkid, contractid)

inventorylinksget

Get active Contract by ContractID

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
api_instance = TelstraTPN.ContractsApi(TelstraTPN.ApiClient(configuration))
linkid = 'linkid_example' # str | Unique identifier representing a specific link
contractid = 'contractid_example' # str | Unique identifier representing a specific contract

try:
    # inventorylinksget
    api_response = api_instance.inventory_links_contract_by_linkid_and_contractid_get(linkid, contractid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->inventory_links_contract_by_linkid_and_contractid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 
 **contractid** | **str**| Unique identifier representing a specific contract | 

### Return type

[**InventorylinksgetResponse**](InventorylinksgetResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_contract_by_linkid_and_contractid_put**
> InventorylinksputResponse inventory_links_contract_by_linkid_and_contractid_put(linkid, contractid, body=body)

inventorylinksput

Update active Contract by ContractID

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
api_instance = TelstraTPN.ContractsApi(TelstraTPN.ApiClient(configuration))
linkid = 'linkid_example' # str | Unique identifier representing a specific link
contractid = 'contractid_example' # str | Unique identifier representing a specific contract
body = TelstraTPN.Body45() # Body45 |  (optional)

try:
    # inventorylinksput
    api_response = api_instance.inventory_links_contract_by_linkid_and_contractid_put(linkid, contractid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->inventory_links_contract_by_linkid_and_contractid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 
 **contractid** | **str**| Unique identifier representing a specific contract | 
 **body** | [**Body45**](Body45.md)|  | [optional] 

### Return type

[**InventorylinksputResponse**](InventorylinksputResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_contract_by_linkid_post**
> InventorylinkslinkidcontractpostResponse inventory_links_contract_by_linkid_post(linkid, body=body)

inventorylinkslinkidcontractpost

Create new Contract on specified link

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
api_instance = TelstraTPN.ContractsApi(TelstraTPN.ApiClient(configuration))
linkid = 'linkid_example' # str | Unique identifier representing a specific link
body = TelstraTPN.Body42() # Body42 |  (optional)

try:
    # inventorylinkslinkidcontractpost
    api_response = api_instance.inventory_links_contract_by_linkid_post(linkid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->inventory_links_contract_by_linkid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 
 **body** | [**Body42**](Body42.md)|  | [optional] 

### Return type

[**InventorylinkslinkidcontractpostResponse**](InventorylinkslinkidcontractpostResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


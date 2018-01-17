# TelstraTPN.ContractsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_links_contract_by_linkid_and_contractid_get**](ContractsApi.md#inventory_links_contract_by_linkid_and_contractid_get) | **GET** /1.0.0/inventory/links/{linkid}/contract/{contractid} | Get active Contract by ContractID
[**inventory_links_contract_by_linkid_and_contractid_put**](ContractsApi.md#inventory_links_contract_by_linkid_and_contractid_put) | **PUT** /1.0.0/inventory/links/{linkid}/contract/{contractid} | Update active Contract by ContractID
[**inventory_links_contract_by_linkid_post**](ContractsApi.md#inventory_links_contract_by_linkid_post) | **POST** /1.0.0/inventory/links/{linkid}/contract | Create new Contract on specified link


# **inventory_links_contract_by_linkid_and_contractid_get**
> InventoryLinksContractResponse inventory_links_contract_by_linkid_and_contractid_get(linkid, contractid)

Get active Contract by ContractID

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
    # Get active Contract by ContractID
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

[**InventoryLinksContractResponse**](InventoryLinksContractResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_contract_by_linkid_and_contractid_put**
> InventoryLinksContractResponse33 inventory_links_contract_by_linkid_and_contractid_put(linkid, contractid, body=body)

Update active Contract by ContractID

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
body = TelstraTPN.InventoryLinksContractRequest() # InventoryLinksContractRequest |  (optional)

try:
    # Update active Contract by ContractID
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
 **body** | [**InventoryLinksContractRequest**](InventoryLinksContractRequest.md)|  | [optional] 

### Return type

[**InventoryLinksContractResponse33**](InventoryLinksContractResponse33.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_contract_by_linkid_post**
> list[InventoryLinksContractResponse38] inventory_links_contract_by_linkid_post(linkid, body=body)

Create new Contract on specified link

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
body = TelstraTPN.InventoryLinksContractRequest37() # InventoryLinksContractRequest37 |  (optional)

try:
    # Create new Contract on specified link
    api_response = api_instance.inventory_links_contract_by_linkid_post(linkid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->inventory_links_contract_by_linkid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 
 **body** | [**InventoryLinksContractRequest37**](InventoryLinksContractRequest37.md)|  | [optional] 

### Return type

[**list[InventoryLinksContractResponse38]**](InventoryLinksContractResponse38.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


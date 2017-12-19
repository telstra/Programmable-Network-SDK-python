# TelstraTPN.ContractsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**100_inventory_links_contract_by_linkid_and_contractid_get**](ContractsApi.md#100_inventory_links_contract_by_linkid_and_contractid_get) | **GET** /1.0.0/inventory/links/{linkid}/contract/{contractid} | Get active Contract by ContractID
[**100_inventory_links_contract_by_linkid_and_contractid_put**](ContractsApi.md#100_inventory_links_contract_by_linkid_and_contractid_put) | **PUT** /1.0.0/inventory/links/{linkid}/contract/{contractid} | Update active Contract by ContractID
[**100_inventory_links_contract_by_linkid_post**](ContractsApi.md#100_inventory_links_contract_by_linkid_post) | **POST** /1.0.0/inventory/links/{linkid}/contract | Create new Contract on specified link


# **100_inventory_links_contract_by_linkid_and_contractid_get**
> Model100InventoryLinksContractResponse 100_inventory_links_contract_by_linkid_and_contractid_get(linkid, contractid)

Get active Contract by ContractID

Get active Contract by ContractID

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.ContractsApi()
linkid = 'linkid_example' # str | Unique identifier representing a specific link
contractid = 'contractid_example' # str | Unique identifier representing a specific contract

try: 
    # Get active Contract by ContractID
    api_response = api_instance.100_inventory_links_contract_by_linkid_and_contractid_get(linkid, contractid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->100_inventory_links_contract_by_linkid_and_contractid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 
 **contractid** | **str**| Unique identifier representing a specific contract | 

### Return type

[**Model100InventoryLinksContractResponse**](Model100InventoryLinksContractResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **100_inventory_links_contract_by_linkid_and_contractid_put**
> Model100InventoryLinksContractResponse33 100_inventory_links_contract_by_linkid_and_contractid_put(linkid, contractid, body=body)

Update active Contract by ContractID

Update active Contract by ContractID

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.ContractsApi()
linkid = 'linkid_example' # str | Unique identifier representing a specific link
contractid = 'contractid_example' # str | Unique identifier representing a specific contract
body = TelstraTPN.Model100InventoryLinksContractRequest() # Model100InventoryLinksContractRequest |  (optional)

try: 
    # Update active Contract by ContractID
    api_response = api_instance.100_inventory_links_contract_by_linkid_and_contractid_put(linkid, contractid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->100_inventory_links_contract_by_linkid_and_contractid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 
 **contractid** | **str**| Unique identifier representing a specific contract | 
 **body** | [**Model100InventoryLinksContractRequest**](Model100InventoryLinksContractRequest.md)|  | [optional] 

### Return type

[**Model100InventoryLinksContractResponse33**](Model100InventoryLinksContractResponse33.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **100_inventory_links_contract_by_linkid_post**
> Model100InventoryLinksContractResponse38 100_inventory_links_contract_by_linkid_post(linkid, body=body)

Create new Contract on specified link

Create new Contract on specified link

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.ContractsApi()
linkid = 'linkid_example' # str | Unique identifier representing a specific link
body = TelstraTPN.Model100InventoryLinksContractRequest37() # Model100InventoryLinksContractRequest37 |  (optional)

try: 
    # Create new Contract on specified link
    api_response = api_instance.100_inventory_links_contract_by_linkid_post(linkid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->100_inventory_links_contract_by_linkid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 
 **body** | [**Model100InventoryLinksContractRequest37**](Model100InventoryLinksContractRequest37.md)|  | [optional] 

### Return type

[**Model100InventoryLinksContractResponse38**](Model100InventoryLinksContractResponse38.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# TelstraTPN.ContractsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_contract_on_specified_link**](ContractsApi.md#create_new_contract_on_specified_link) | **POST** /1.0.0/inventory/links/{linkid}/contract | Create new Contract on specified link
[**get_active_contract_by_contract_id**](ContractsApi.md#get_active_contract_by_contract_id) | **GET** /1.0.0/inventory/links/{linkid}/contract/{contractid} | Get active Contract by ContractID
[**update_active_contract_by_contract_id**](ContractsApi.md#update_active_contract_by_contract_id) | **PUT** /1.0.0/inventory/links/{linkid}/contract/{contractid} | Update active Contract by ContractID


# **create_new_contract_on_specified_link**
> Model100InventoryLinksContractResponse36 create_new_contract_on_specified_link(linkid, body=body)

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
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.ContractsApi()
linkid = 'linkid_example' # str | Unique identifier representing a specific link
body = TelstraTPN.Model100InventoryLinksContractRequest35() # Model100InventoryLinksContractRequest35 |  (optional)

try: 
    # Create new Contract on specified link
    api_response = api_instance.create_new_contract_on_specified_link(linkid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->create_new_contract_on_specified_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 
 **body** | [**Model100InventoryLinksContractRequest35**](Model100InventoryLinksContractRequest35.md)|  | [optional] 

### Return type

[**Model100InventoryLinksContractResponse36**](Model100InventoryLinksContractResponse36.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_contract_by_contract_id**
> Model100InventoryLinksContractResponse get_active_contract_by_contract_id(linkid, contractid)

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
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.ContractsApi()
linkid = 'linkid_example' # str | Unique identifier representing a specific link
contractid = 'contractid_example' # str | Unique identifier representing a specific contract

try: 
    # Get active Contract by ContractID
    api_response = api_instance.get_active_contract_by_contract_id(linkid, contractid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_active_contract_by_contract_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 
 **contractid** | **str**| Unique identifier representing a specific contract | 

### Return type

[**Model100InventoryLinksContractResponse**](Model100InventoryLinksContractResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_active_contract_by_contract_id**
> Model100InventoryLinksContractResponse31 update_active_contract_by_contract_id(linkid, contractid, body=body)

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
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.ContractsApi()
linkid = 'linkid_example' # str | Unique identifier representing a specific link
contractid = 'contractid_example' # str | Unique identifier representing a specific contract
body = TelstraTPN.Model100InventoryLinksContractRequest() # Model100InventoryLinksContractRequest |  (optional)

try: 
    # Update active Contract by ContractID
    api_response = api_instance.update_active_contract_by_contract_id(linkid, contractid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->update_active_contract_by_contract_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 
 **contractid** | **str**| Unique identifier representing a specific contract | 
 **body** | [**Model100InventoryLinksContractRequest**](Model100InventoryLinksContractRequest.md)|  | [optional] 

### Return type

[**Model100InventoryLinksContractResponse31**](Model100InventoryLinksContractResponse31.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# TelstraTPN.ContractsApi

All URIs are relative to *https://penapi.pacnetconnect.com/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_links_linkid_contract_contractid_get**](ContractsApi.md#inventory_links_linkid_contract_contractid_get) | **GET** /inventory/links/{linkid}/contract/{contractid}/ | Get active Contract by ContractID
[**inventory_links_linkid_contract_contractid_put**](ContractsApi.md#inventory_links_linkid_contract_contractid_put) | **PUT** /inventory/links/{linkid}/contract/{contractid}/ | Update active Contract by ContractID
[**inventory_links_linkid_contract_post**](ContractsApi.md#inventory_links_linkid_contract_post) | **POST** /inventory/links/{linkid}/contract/ | Create new Contract on specified link


# **inventory_links_linkid_contract_contractid_get**
> InlineResponse2006 inventory_links_linkid_contract_contractid_get(linkid, contractid)

Get active Contract by ContractID

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
api_instance = TelstraTPN.ContractsApi(TelstraTPN.ApiClient(configuration))
linkid = 'linkid_example' # str | Unique identifier representing a specific link
contractid = 'contractid_example' # str | Unique identifier representing a specific contract

try:
    # Get active Contract by ContractID
    api_response = api_instance.inventory_links_linkid_contract_contractid_get(linkid, contractid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->inventory_links_linkid_contract_contractid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 
 **contractid** | **str**| Unique identifier representing a specific contract | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_linkid_contract_contractid_put**
> SuccessFragment inventory_links_linkid_contract_contractid_put(linkid, contractid, body=body)

Update active Contract by ContractID

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
api_instance = TelstraTPN.ContractsApi(TelstraTPN.ApiClient(configuration))
linkid = 'linkid_example' # str | Unique identifier representing a specific link
contractid = 'contractid_example' # str | Unique identifier representing a specific contract
body = TelstraTPN.Body() # Body |  (optional)

try:
    # Update active Contract by ContractID
    api_response = api_instance.inventory_links_linkid_contract_contractid_put(linkid, contractid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->inventory_links_linkid_contract_contractid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 
 **contractid** | **str**| Unique identifier representing a specific contract | 
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**SuccessFragment**](SuccessFragment.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_linkid_contract_post**
> SuccessFragment inventory_links_linkid_contract_post(linkid, createcontractrequest=createcontractrequest)

Create new Contract on specified link

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
api_instance = TelstraTPN.ContractsApi(TelstraTPN.ApiClient(configuration))
linkid = 'linkid_example' # str | Unique identifier representing a specific link
createcontractrequest = TelstraTPN.Createcontractrequest() # Createcontractrequest |  (optional)

try:
    # Create new Contract on specified link
    api_response = api_instance.inventory_links_linkid_contract_post(linkid, createcontractrequest=createcontractrequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->inventory_links_linkid_contract_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 
 **createcontractrequest** | [**Createcontractrequest**](Createcontractrequest.md)|  | [optional] 

### Return type

[**SuccessFragment**](SuccessFragment.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


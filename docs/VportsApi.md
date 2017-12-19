# TelstraTPN.VportsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**100_inventory_regularvport_post**](VportsApi.md#100_inventory_regularvport_post) | **POST** /1.0.0/inventory/regularvport | Create VPort for physical endpoint
[**100_inventory_vnf_vport_post**](VportsApi.md#100_inventory_vnf_vport_post) | **POST** /1.0.0/inventory/vnf/vport | Create VNF VPort
[**100_inventory_vport_by_vportuuid_get**](VportsApi.md#100_inventory_vport_by_vportuuid_get) | **GET** /1.0.0/inventory/vport/{vportuuid} | Get information about the specified VPort


# **100_inventory_regularvport_post**
> Model100InventoryRegularvportResponse 100_inventory_regularvport_post(body=body)

Create VPort for physical endpoint

Create VPort representing a VLAN on a Physical Ethernet Port

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.VportsApi()
body = TelstraTPN.Model100InventoryRegularvportRequest() # Model100InventoryRegularvportRequest |  (optional)

try: 
    # Create VPort for physical endpoint
    api_response = api_instance.100_inventory_regularvport_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VportsApi->100_inventory_regularvport_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model100InventoryRegularvportRequest**](Model100InventoryRegularvportRequest.md)|  | [optional] 

### Return type

[**Model100InventoryRegularvportResponse**](Model100InventoryRegularvportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **100_inventory_vnf_vport_post**
> Model100InventoryVnfVportResponse 100_inventory_vnf_vport_post(body=body)

Create VNF VPort

Create VNF VPort

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.VportsApi()
body = TelstraTPN.Model100InventoryVnfVportRequest() # Model100InventoryVnfVportRequest |  (optional)

try: 
    # Create VNF VPort
    api_response = api_instance.100_inventory_vnf_vport_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VportsApi->100_inventory_vnf_vport_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model100InventoryVnfVportRequest**](Model100InventoryVnfVportRequest.md)|  | [optional] 

### Return type

[**Model100InventoryVnfVportResponse**](Model100InventoryVnfVportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **100_inventory_vport_by_vportuuid_get**
> EndpointPort 100_inventory_vport_by_vportuuid_get(vportuuid)

Get information about the specified VPort

Get information about the specified VPort

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.VportsApi()
vportuuid = 'vportuuid_example' # str | Unique identifier representing a specific virtual port

try: 
    # Get information about the specified VPort
    api_response = api_instance.100_inventory_vport_by_vportuuid_get(vportuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VportsApi->100_inventory_vport_by_vportuuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vportuuid** | **str**| Unique identifier representing a specific virtual port | 

### Return type

[**EndpointPort**](EndpointPort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


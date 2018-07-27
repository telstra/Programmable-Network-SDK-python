# TelstraTPN.EndpointsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoint_endpointuuid_get**](EndpointsApi.md#endpoint_endpointuuid_get) | **GET** /eis/1.0.0/endpoint/endpointuuid/{endpointuuid} | Get Endpoint name and status
[**endpoint_endpointuuid_put**](EndpointsApi.md#endpoint_endpointuuid_put) | **PUT** /eis/1.0.0/endpoint/endpointuuid/{endpointuuid} | Update Endpoint name
[**endpoints_assign_topology_tag**](EndpointsApi.md#endpoints_assign_topology_tag) | **POST** /eis/1.0.0/endpoints/{endpointuuid}/assign_topology_tag | Assign an Endpoint to a Topology
[**endpoints_topology_tag_uuid**](EndpointsApi.md#endpoints_topology_tag_uuid) | **GET** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid} | List Endpoints for Topology
[**endpoints_topology_tag_uuid_endpoint**](EndpointsApi.md#endpoints_topology_tag_uuid_endpoint) | **DELETE** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid}/endpoint/{endpointuuid} | Remove Endpoint from a Topology
[**inventory_endpoint**](EndpointsApi.md#inventory_endpoint) | **GET** /1.0.0/inventory/endpoint/{endpointuuid} | Get information about the specified endpoint
[**inventory_endpoints_customeruuid**](EndpointsApi.md#inventory_endpoints_customeruuid) | **GET** /1.0.0/inventory/endpoints/customeruuid/{customeruuid} | Get list of endpoints for a customer
[**inventory_links_stats_endpoint**](EndpointsApi.md#inventory_links_stats_endpoint) | **GET** /1.0.0/inventory/links-stats/endpoint/{endpointuuid}/{startdate}/{enddate} | Get statistics for endpoint
[**inventory_links_stats_endpointstate**](EndpointsApi.md#inventory_links_stats_endpointstate) | **GET** /1.0.0/inventory/links-stats/endpointstate/{endpointuuid}/{startdate}/{enddate} | Get state statistics for endpoint
[**inventory_regularendpoint**](EndpointsApi.md#inventory_regularendpoint) | **POST** /1.0.0/inventory/regularendpoint | Create Physical (Port) Endpoint
[**inventory_regularvport**](EndpointsApi.md#inventory_regularvport) | **POST** /1.0.0/inventory/regularvport | Create VPort for physical endpoint
[**inventory_vnfendpoint**](EndpointsApi.md#inventory_vnfendpoint) | **POST** /1.0.0/inventory/vnfendpoint | Instantiate Virtual Network Function
[**vnfendpoint_vnfuuid**](EndpointsApi.md#vnfendpoint_vnfuuid) | **GET** /eis/1.0.0/vnfendpoint/vnfuuid/{vnfuuid} | Get details of a specific VNF


# **endpoint_endpointuuid_get**
> InlineResponse2004 endpoint_endpointuuid_get(endpointuuid)

Get Endpoint name and status

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint

try:
    # Get Endpoint name and status
    api_response = api_instance.endpoint_endpointuuid_get(endpointuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_endpointuuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_endpointuuid_put**
> SuccessFragment endpoint_endpointuuid_put(endpointuuid, endpointupdaterequest=endpointupdaterequest)

Update Endpoint name

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint
endpointupdaterequest = TelstraTPN.Endpointupdaterequest() # Endpointupdaterequest |  (optional)

try:
    # Update Endpoint name
    api_response = api_instance.endpoint_endpointuuid_put(endpointuuid, endpointupdaterequest=endpointupdaterequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_endpointuuid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 
 **endpointupdaterequest** | [**Endpointupdaterequest**](Endpointupdaterequest.md)|  | [optional] 

### Return type

[**SuccessFragment**](SuccessFragment.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_assign_topology_tag**
> SuccessFragment endpoints_assign_topology_tag(endpointuuid, assigntopotagrequest=assigntopotagrequest)

Assign an Endpoint to a Topology

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint
assigntopotagrequest = TelstraTPN.Assigntopotagrequest() # Assigntopotagrequest |  (optional)

try:
    # Assign an Endpoint to a Topology
    api_response = api_instance.endpoints_assign_topology_tag(endpointuuid, assigntopotagrequest=assigntopotagrequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoints_assign_topology_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 
 **assigntopotagrequest** | [**Assigntopotagrequest**](Assigntopotagrequest.md)|  | [optional] 

### Return type

[**SuccessFragment**](SuccessFragment.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_topology_tag_uuid**
> InlineResponse20014 endpoints_topology_tag_uuid(topotaguuid)

List Endpoints for Topology

List all Endpoints associated with the topology tag.

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try:
    # List Endpoints for Topology
    api_response = api_instance.endpoints_topology_tag_uuid(topotaguuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoints_topology_tag_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_topology_tag_uuid_endpoint**
> endpoints_topology_tag_uuid_endpoint(topotaguuid, endpointuuid)

Remove Endpoint from a Topology

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint

try:
    # Remove Endpoint from a Topology
    api_instance.endpoints_topology_tag_uuid_endpoint(topotaguuid, endpointuuid)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoints_topology_tag_uuid_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_endpoint**
> InlineResponse2002 inventory_endpoint(endpointuuid)

Get information about the specified endpoint

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint

try:
    # Get information about the specified endpoint
    api_response = api_instance.inventory_endpoint(endpointuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventory_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_endpoints_customeruuid**
> InlineResponse2001 inventory_endpoints_customeruuid(customeruuid)

Get list of endpoints for a customer

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try:
    # Get list of endpoints for a customer
    api_response = api_instance.inventory_endpoints_customeruuid(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventory_endpoints_customeruuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_stats_endpoint**
> list[InlineResponse20018] inventory_links_stats_endpoint(endpointuuid, startdate, enddate)

Get statistics for endpoint

Get statistics related to the specified endpoint

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint
startdate = 'startdate_example' # str | Start date for statistics query
enddate = 'enddate_example' # str | End date for statistics query

try:
    # Get statistics for endpoint
    api_response = api_instance.inventory_links_stats_endpoint(endpointuuid, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventory_links_stats_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 
 **startdate** | **str**| Start date for statistics query | 
 **enddate** | **str**| End date for statistics query | 

### Return type

[**list[InlineResponse20018]**](InlineResponse20018.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_stats_endpointstate**
> list[InlineResponse20020] inventory_links_stats_endpointstate(endpointuuid, startdate, enddate)

Get state statistics for endpoint

Get statistics related to the state of the specified endpoint

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint
startdate = 'startdate_example' # str | Start date for statistics query
enddate = 'enddate_example' # str | End date for statistics query

try:
    # Get state statistics for endpoint
    api_response = api_instance.inventory_links_stats_endpointstate(endpointuuid, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventory_links_stats_endpointstate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 
 **startdate** | **str**| Start date for statistics query | 
 **enddate** | **str**| End date for statistics query | 

### Return type

[**list[InlineResponse20020]**](InlineResponse20020.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_regularendpoint**
> SuccessFragment inventory_regularendpoint(regendpointrequest=regendpointrequest)

Create Physical (Port) Endpoint

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
regendpointrequest = TelstraTPN.Regendpointrequest() # Regendpointrequest |  (optional)

try:
    # Create Physical (Port) Endpoint
    api_response = api_instance.inventory_regularendpoint(regendpointrequest=regendpointrequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventory_regularendpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regendpointrequest** | [**Regendpointrequest**](Regendpointrequest.md)|  | [optional] 

### Return type

[**SuccessFragment**](SuccessFragment.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_regularvport**
> SuccessFragment inventory_regularvport(regvportrequest=regvportrequest)

Create VPort for physical endpoint

Create VPort representing a VLAN on a Physical Ethernet Port

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
regvportrequest = TelstraTPN.Regvportrequest() # Regvportrequest |  (optional)

try:
    # Create VPort for physical endpoint
    api_response = api_instance.inventory_regularvport(regvportrequest=regvportrequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventory_regularvport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regvportrequest** | [**Regvportrequest**](Regvportrequest.md)|  | [optional] 

### Return type

[**SuccessFragment**](SuccessFragment.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_vnfendpoint**
> SuccessFragment inventory_vnfendpoint(vnfendpointrequest=vnfendpointrequest)

Instantiate Virtual Network Function

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
vnfendpointrequest = TelstraTPN.Vnfendpointrequest() # Vnfendpointrequest |  (optional)

try:
    # Instantiate Virtual Network Function
    api_response = api_instance.inventory_vnfendpoint(vnfendpointrequest=vnfendpointrequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventory_vnfendpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfendpointrequest** | [**Vnfendpointrequest**](Vnfendpointrequest.md)|  | [optional] 

### Return type

[**SuccessFragment**](SuccessFragment.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnfendpoint_vnfuuid**
> InlineResponse2003 vnfendpoint_vnfuuid(vnfuuid)

Get details of a specific VNF

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function

try:
    # Get details of a specific VNF
    api_response = api_instance.vnfendpoint_vnfuuid(vnfuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->vnfendpoint_vnfuuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# TelstraTPN.StatisticsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_links_stats_endpoint**](StatisticsApi.md#inventory_links_stats_endpoint) | **GET** /1.0.0/inventory/links-stats/endpoint/{endpointuuid}/{startdate}/{enddate} | Get statistics for endpoint
[**inventory_links_stats_endpointstate**](StatisticsApi.md#inventory_links_stats_endpointstate) | **GET** /1.0.0/inventory/links-stats/endpointstate/{endpointuuid}/{startdate}/{enddate} | Get state statistics for endpoint
[**inventory_links_stats_flow**](StatisticsApi.md#inventory_links_stats_flow) | **GET** /1.0.0/inventory/links-stats/flow/{linkid}/{startdate}/{enddate} | Get statistics for flow


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
api_instance = TelstraTPN.StatisticsApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint
startdate = 'startdate_example' # str | Start date for statistics query
enddate = 'enddate_example' # str | End date for statistics query

try:
    # Get statistics for endpoint
    api_response = api_instance.inventory_links_stats_endpoint(endpointuuid, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->inventory_links_stats_endpoint: %s\n" % e)
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
api_instance = TelstraTPN.StatisticsApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint
startdate = 'startdate_example' # str | Start date for statistics query
enddate = 'enddate_example' # str | End date for statistics query

try:
    # Get state statistics for endpoint
    api_response = api_instance.inventory_links_stats_endpointstate(endpointuuid, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->inventory_links_stats_endpointstate: %s\n" % e)
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

# **inventory_links_stats_flow**
> list[InlineResponse20019] inventory_links_stats_flow(linkid, startdate, enddate)

Get statistics for flow

Get statistics related to the specified flow

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
api_instance = TelstraTPN.StatisticsApi(TelstraTPN.ApiClient(configuration))
linkid = 'linkid_example' # str | Unique identifier representing a specific link
startdate = 'startdate_example' # str | Start date for statistics query
enddate = 'enddate_example' # str | End date for statistics query

try:
    # Get statistics for flow
    api_response = api_instance.inventory_links_stats_flow(linkid, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->inventory_links_stats_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 
 **startdate** | **str**| Start date for statistics query | 
 **enddate** | **str**| End date for statistics query | 

### Return type

[**list[InlineResponse20019]**](InlineResponse20019.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


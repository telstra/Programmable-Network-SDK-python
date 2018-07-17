# TelstraTPN.LinksApi

All URIs are relative to *https://penapi.pacnetconnect.com/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_link_post**](LinksApi.md#inventory_link_post) | **POST** /inventory/link/ | Create Link and initial Contract
[**inventory_links_customer_customeruuid_get**](LinksApi.md#inventory_links_customer_customeruuid_get) | **GET** /inventory/links/customer/{customeruuid}/ | Get active Links
[**inventory_links_history_linkid_get**](LinksApi.md#inventory_links_history_linkid_get) | **GET** /inventory/links/history/{linkid}/ | Get Link history
[**inventory_links_linkid_get**](LinksApi.md#inventory_links_linkid_get) | **GET** /inventory/links/{linkid}/ | Get details of specified link
[**inventory_links_stats_flow_linkid_startdate_enddate_get**](LinksApi.md#inventory_links_stats_flow_linkid_startdate_enddate_get) | **GET** /inventory/links-stats/flow/{linkid}/{startdate}/{enddate}/ | Get statistics for flow


# **inventory_link_post**
> SuccessFragment inventory_link_post(createlinkrequest=createlinkrequest)

Create Link and initial Contract

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
api_instance = TelstraTPN.LinksApi(TelstraTPN.ApiClient(configuration))
createlinkrequest = TelstraTPN.Createlinkrequest() # Createlinkrequest |  (optional)

try:
    # Create Link and initial Contract
    api_response = api_instance.inventory_link_post(createlinkrequest=createlinkrequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->inventory_link_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createlinkrequest** | [**Createlinkrequest**](Createlinkrequest.md)|  | [optional] 

### Return type

[**SuccessFragment**](SuccessFragment.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_customer_customeruuid_get**
> list[Link] inventory_links_customer_customeruuid_get(customeruuid)

Get active Links

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
api_instance = TelstraTPN.LinksApi(TelstraTPN.ApiClient(configuration))
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try:
    # Get active Links
    api_response = api_instance.inventory_links_customer_customeruuid_get(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->inventory_links_customer_customeruuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**list[Link]**](Link.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_history_linkid_get**
> InlineResponse2005 inventory_links_history_linkid_get(linkid)

Get Link history

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
api_instance = TelstraTPN.LinksApi(TelstraTPN.ApiClient(configuration))
linkid = 'linkid_example' # str | Unique identifier representing a specific link

try:
    # Get Link history
    api_response = api_instance.inventory_links_history_linkid_get(linkid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->inventory_links_history_linkid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_linkid_get**
> InlineResponse2007 inventory_links_linkid_get(linkid)

Get details of specified link

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
api_instance = TelstraTPN.LinksApi(TelstraTPN.ApiClient(configuration))
linkid = 'linkid_example' # str | Unique identifier representing a specific link

try:
    # Get details of specified link
    api_response = api_instance.inventory_links_linkid_get(linkid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->inventory_links_linkid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_links_stats_flow_linkid_startdate_enddate_get**
> list[InlineResponse20019] inventory_links_stats_flow_linkid_startdate_enddate_get(linkid, startdate, enddate)

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
api_instance = TelstraTPN.LinksApi(TelstraTPN.ApiClient(configuration))
linkid = 'linkid_example' # str | Unique identifier representing a specific link
startdate = 'startdate_example' # str | Start date for statistics query
enddate = 'enddate_example' # str | End date for statistics query

try:
    # Get statistics for flow
    api_response = api_instance.inventory_links_stats_flow_linkid_startdate_enddate_get(linkid, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->inventory_links_stats_flow_linkid_startdate_enddate_get: %s\n" % e)
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


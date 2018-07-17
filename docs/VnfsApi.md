# TelstraTPN.VnfsApi

All URIs are relative to *https://penapi.pacnetconnect.com/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup_backupuuid_delete**](VnfsApi.md#backup_backupuuid_delete) | **DELETE** /backup/{backupuuid}/ | Delete specified backup
[**backup_backupuuid_get**](VnfsApi.md#backup_backupuuid_get) | **GET** /backup/{backupuuid}/ | Get information about the specified backup
[**backup_backupuuid_restore_post**](VnfsApi.md#backup_backupuuid_restore_post) | **POST** /backup/{backupuuid}/restore/ | Restore VNF from backup
[**backup_post**](VnfsApi.md#backup_post) | **POST** /backup/ | Create backup of specified VNF
[**backup_vnf_vnfuuid_delete_post**](VnfsApi.md#backup_vnf_vnfuuid_delete_post) | **POST** /backup/vnf/{vnfuuid}/delete/ | Delete multiple backups
[**backup_vnf_vnfuuid_get**](VnfsApi.md#backup_vnf_vnfuuid_get) | **GET** /backup/vnf/{vnfuuid}/ | List backups
[**inventory_vnf_vport_post**](VnfsApi.md#inventory_vnf_vport_post) | **POST** /inventory/vnf/vport/ | Create VNF VPort
[**inventory_vnfendpoint_post**](VnfsApi.md#inventory_vnfendpoint_post) | **POST** /inventory/vnfendpoint/ | Instantiate Virtual Network Function
[**marketplace_image_get**](VnfsApi.md#marketplace_image_get) | **GET** /marketplace/image/ | List images in the Marketplace
[**marketplace_image_imageid_add_to_my_images_post**](VnfsApi.md#marketplace_image_imageid_add_to_my_images_post) | **POST** /marketplace/image/{imageid}/add_to_my_images/ | Add specified image to \&quot;My Images\&quot;
[**marketplace_image_imageid_get**](VnfsApi.md#marketplace_image_imageid_get) | **GET** /marketplace/image/{imageid}/ | Get information about the specified image
[**marketplace_image_imageid_remove_from_my_images_post**](VnfsApi.md#marketplace_image_imageid_remove_from_my_images_post) | **POST** /marketplace/image/{imageid}/remove_from_my_images/ | Remove specified image from \&quot;My Images\&quot;
[**marketplace_image_my_images_get**](VnfsApi.md#marketplace_image_my_images_get) | **GET** /marketplace/image/my_images/ | List images in \&quot;My Images\&quot;
[**vnf_vnfuuid_get**](VnfsApi.md#vnf_vnfuuid_get) | **GET** /vnf/{vnfuuid}/ | Get status information about the specified VNF
[**vnf_vnfuuid_reboot_post**](VnfsApi.md#vnf_vnfuuid_reboot_post) | **POST** /vnf/{vnfuuid}/reboot/ | Reboot the specified VNF
[**vnf_vnfuuid_resume_post**](VnfsApi.md#vnf_vnfuuid_resume_post) | **POST** /vnf/{vnfuuid}/resume/ | Resume the specified VNF
[**vnf_vnfuuid_suspend_post**](VnfsApi.md#vnf_vnfuuid_suspend_post) | **POST** /vnf/{vnfuuid}/suspend/ | Suspend the specified VNF
[**vnfendpoint_vnfuuid_vnfuuid_get**](VnfsApi.md#vnfendpoint_vnfuuid_vnfuuid_get) | **GET** /vnfendpoint/vnfuuid/{vnfuuid}/ | Get details of a specific VNF


# **backup_backupuuid_delete**
> Backup backup_backupuuid_delete(backupuuid)

Delete specified backup

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
backupuuid = 'backupuuid_example' # str | Unique identifier representing a specific VNF backup

try:
    # Delete specified backup
    api_response = api_instance.backup_backupuuid_delete(backupuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->backup_backupuuid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backupuuid** | **str**| Unique identifier representing a specific VNF backup | 

### Return type

[**Backup**](Backup.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_backupuuid_get**
> Backup backup_backupuuid_get(backupuuid)

Get information about the specified backup

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
backupuuid = 'backupuuid_example' # str | Unique identifier representing a specific VNF backup

try:
    # Get information about the specified backup
    api_response = api_instance.backup_backupuuid_get(backupuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->backup_backupuuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backupuuid** | **str**| Unique identifier representing a specific VNF backup | 

### Return type

[**Backup**](Backup.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_backupuuid_restore_post**
> Backup backup_backupuuid_restore_post(backupuuid)

Restore VNF from backup

Restore VNF from specified backup

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
backupuuid = 'backupuuid_example' # str | Unique identifier representing a specific VNF backup

try:
    # Restore VNF from backup
    api_response = api_instance.backup_backupuuid_restore_post(backupuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->backup_backupuuid_restore_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backupuuid** | **str**| Unique identifier representing a specific VNF backup | 

### Return type

[**Backup**](Backup.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jsonapplication/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_post**
> Backup backup_post(backuprequest=backuprequest)

Create backup of specified VNF

'Note: if a second backup creation is attempted while one is already active, an error will be returned indicating that the VNF is invalid. If replace_backup_uuid is provided, this backup is deleted once the new backup is successfully completed'

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
backuprequest = TelstraTPN.Backuprequest() # Backuprequest |  (optional)

try:
    # Create backup of specified VNF
    api_response = api_instance.backup_post(backuprequest=backuprequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->backup_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backuprequest** | [**Backuprequest**](Backuprequest.md)|  | [optional] 

### Return type

[**Backup**](Backup.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_vnf_vnfuuid_delete_post**
> InlineResponse202 backup_vnf_vnfuuid_delete_post(vnfuuid)

Delete multiple backups

Delete list of backups associated with specified VNF

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function

try:
    # Delete multiple backups
    api_response = api_instance.backup_vnf_vnfuuid_delete_post(vnfuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->backup_vnf_vnfuuid_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_vnf_vnfuuid_get**
> list[Backup] backup_vnf_vnfuuid_get(vnfuuid)

List backups

List available backups for the specified VNF

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function

try:
    # List backups
    api_response = api_instance.backup_vnf_vnfuuid_get(vnfuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->backup_vnf_vnfuuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 

### Return type

[**list[Backup]**](Backup.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_vnf_vport_post**
> InlineResponse2008 inventory_vnf_vport_post(vportrequest=vportrequest)

Create VNF VPort

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vportrequest = TelstraTPN.Vportrequest() # Vportrequest |  (optional)

try:
    # Create VNF VPort
    api_response = api_instance.inventory_vnf_vport_post(vportrequest=vportrequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->inventory_vnf_vport_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vportrequest** | [**Vportrequest**](Vportrequest.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_vnfendpoint_post**
> SuccessFragment inventory_vnfendpoint_post(vnfendpointrequest=vnfendpointrequest)

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfendpointrequest = TelstraTPN.Vnfendpointrequest() # Vnfendpointrequest |  (optional)

try:
    # Instantiate Virtual Network Function
    api_response = api_instance.inventory_vnfendpoint_post(vnfendpointrequest=vnfendpointrequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->inventory_vnfendpoint_post: %s\n" % e)
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

# **marketplace_image_get**
> InlineResponse2009 marketplace_image_get()

List images in the Marketplace

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))

try:
    # List images in the Marketplace
    api_response = api_instance.marketplace_image_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_image_imageid_add_to_my_images_post**
> InlineResponse20010 marketplace_image_imageid_add_to_my_images_post(imageid, unknown_base_type=unknown_base_type)

Add specified image to \"My Images\"

Note that trailing / is required, body must be {}

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
imageid = 56 # int | Identifier representing a specific VNF image
unknown_base_type = TelstraTPN.UNKNOWN_BASE_TYPE() # object |  (optional)

try:
    # Add specified image to \"My Images\"
    api_response = api_instance.marketplace_image_imageid_add_to_my_images_post(imageid, unknown_base_type=unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_imageid_add_to_my_images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageid** | **int**| Identifier representing a specific VNF image | 
 **unknown_base_type** | [**object**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/jsonapplication/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_image_imageid_get**
> Image marketplace_image_imageid_get(imageid)

Get information about the specified image

Note that trailing / is required

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
imageid = 56 # int | Identifier representing a specific VNF image

try:
    # Get information about the specified image
    api_response = api_instance.marketplace_image_imageid_get(imageid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_imageid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageid** | **int**| Identifier representing a specific VNF image | 

### Return type

[**Image**](Image.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_image_imageid_remove_from_my_images_post**
> InlineResponse20010 marketplace_image_imageid_remove_from_my_images_post(imageid, unknown_base_type=unknown_base_type)

Remove specified image from \"My Images\"

Note that trailing / is required, body must be {}

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
imageid = 56 # int | Identifier representing a specific VNF image
unknown_base_type = TelstraTPN.UNKNOWN_BASE_TYPE() # object |  (optional)

try:
    # Remove specified image from \"My Images\"
    api_response = api_instance.marketplace_image_imageid_remove_from_my_images_post(imageid, unknown_base_type=unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_imageid_remove_from_my_images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageid** | **int**| Identifier representing a specific VNF image | 
 **unknown_base_type** | [**object**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/jsonapplication/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_image_my_images_get**
> InlineResponse2009 marketplace_image_my_images_get()

List images in \"My Images\"

Note that trailing / is required

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))

try:
    # List images in \"My Images\"
    api_response = api_instance.marketplace_image_my_images_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_my_images_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnf_vnfuuid_get**
> InlineResponse20011 vnf_vnfuuid_get(vnfuuid)

Get status information about the specified VNF

'Possible return values:   ACTIVE,   BUILD,   SHUTOFF,   VERIFY_RESIZE,   PAUSED,   SUSPENDED,   RESCUE,   ERROR,   DELETED,   SOFT_DELETED,   SHELVED,   SHELVED_OFFLOADED'

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function

try:
    # Get status information about the specified VNF
    api_response = api_instance.vnf_vnfuuid_get(vnfuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->vnf_vnfuuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnf_vnfuuid_reboot_post**
> vnf_vnfuuid_reboot_post(vnfuuid, rebootrequest=rebootrequest)

Reboot the specified VNF

reboot_type is 'warm' or 'cold'

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function
rebootrequest = TelstraTPN.Rebootrequest() # Rebootrequest |  (optional)

try:
    # Reboot the specified VNF
    api_instance.vnf_vnfuuid_reboot_post(vnfuuid, rebootrequest=rebootrequest)
except ApiException as e:
    print("Exception when calling VnfsApi->vnf_vnfuuid_reboot_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 
 **rebootrequest** | [**Rebootrequest**](Rebootrequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnf_vnfuuid_resume_post**
> vnf_vnfuuid_resume_post(vnfuuid)

Resume the specified VNF

Note that body must be {}

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function

try:
    # Resume the specified VNF
    api_instance.vnf_vnfuuid_resume_post(vnfuuid)
except ApiException as e:
    print("Exception when calling VnfsApi->vnf_vnfuuid_resume_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnf_vnfuuid_suspend_post**
> vnf_vnfuuid_suspend_post(vnfuuid)

Suspend the specified VNF

Note that body must be {}

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function

try:
    # Suspend the specified VNF
    api_instance.vnf_vnfuuid_suspend_post(vnfuuid)
except ApiException as e:
    print("Exception when calling VnfsApi->vnf_vnfuuid_suspend_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnfendpoint_vnfuuid_vnfuuid_get**
> InlineResponse2003 vnfendpoint_vnfuuid_vnfuuid_get(vnfuuid)

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function

try:
    # Get details of a specific VNF
    api_response = api_instance.vnfendpoint_vnfuuid_vnfuuid_get(vnfuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->vnfendpoint_vnfuuid_vnfuuid_get: %s\n" % e)
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


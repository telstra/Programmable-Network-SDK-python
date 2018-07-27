# TelstraTPN.VnfsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bms_backup**](VnfsApi.md#bms_backup) | **POST** /bms/1.0.0/backup | Create backup of specified VNF
[**bms_backup_delete**](VnfsApi.md#bms_backup_delete) | **DELETE** /bms/1.0.0/backup/{backupuuid} | Delete specified backup
[**bms_backup_get**](VnfsApi.md#bms_backup_get) | **GET** /bms/1.0.0/backup/{backupuuid} | Get information about the specified backup
[**bms_backup_restore**](VnfsApi.md#bms_backup_restore) | **POST** /bms/1.0.0/backup/{backupuuid}/restore | Restore VNF from backup
[**bms_backup_vnf**](VnfsApi.md#bms_backup_vnf) | **GET** /bms/1.0.0/backup/vnf/{vnfuuid} | List backups
[**bms_backup_vnf_delete**](VnfsApi.md#bms_backup_vnf_delete) | **POST** /bms/1.0.0/backup/vnf/{vnfuuid}/delete | Delete multiple backups
[**inventory_vnf_vport**](VnfsApi.md#inventory_vnf_vport) | **POST** /1.0.0/inventory/vnf/vport | Create VNF VPort
[**inventory_vnfendpoint**](VnfsApi.md#inventory_vnfendpoint) | **POST** /1.0.0/inventory/vnfendpoint | Instantiate Virtual Network Function
[**marketplace_image**](VnfsApi.md#marketplace_image) | **GET** /1.0.0/marketplace/image | List images in the Marketplace
[**marketplace_image_add**](VnfsApi.md#marketplace_image_add) | **POST** /1.0.0/marketplace/image/{imageid}/add_to_my_images/ | Add specified image to \&quot;My Images\&quot;
[**marketplace_image_imageid**](VnfsApi.md#marketplace_image_imageid) | **GET** /1.0.0/marketplace/image/{imageid}/ | Get information about the specified image
[**marketplace_image_my_images**](VnfsApi.md#marketplace_image_my_images) | **GET** /1.0.0/marketplace/image/my_images/ | List images in \&quot;My Images\&quot;
[**marketplace_image_remove**](VnfsApi.md#marketplace_image_remove) | **POST** /1.0.0/marketplace/image/{imageid}/remove_from_my_images/ | Remove specified image from \&quot;My Images\&quot;
[**vnf**](VnfsApi.md#vnf) | **GET** /vnfds/1.0.0/vnf/{vnfuuid}/ | Get status information about the specified VNF
[**vnf_reboot**](VnfsApi.md#vnf_reboot) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/reboot | Reboot the specified VNF
[**vnf_resume**](VnfsApi.md#vnf_resume) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/resume | Resume the specified VNF
[**vnf_suspend**](VnfsApi.md#vnf_suspend) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/suspend | Suspend the specified VNF
[**vnfendpoint_vnfuuid**](VnfsApi.md#vnfendpoint_vnfuuid) | **GET** /eis/1.0.0/vnfendpoint/vnfuuid/{vnfuuid} | Get details of a specific VNF


# **bms_backup**
> Backup bms_backup(backuprequest=backuprequest)

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
    api_response = api_instance.bms_backup(backuprequest=backuprequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->bms_backup: %s\n" % e)
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

# **bms_backup_delete**
> Backup bms_backup_delete(backupuuid)

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
    api_response = api_instance.bms_backup_delete(backupuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->bms_backup_delete: %s\n" % e)
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

# **bms_backup_get**
> Backup bms_backup_get(backupuuid)

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
    api_response = api_instance.bms_backup_get(backupuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->bms_backup_get: %s\n" % e)
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

# **bms_backup_restore**
> Backup bms_backup_restore(backupuuid)

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
    api_response = api_instance.bms_backup_restore(backupuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->bms_backup_restore: %s\n" % e)
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
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bms_backup_vnf**
> list[Backup] bms_backup_vnf(vnfuuid)

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
    api_response = api_instance.bms_backup_vnf(vnfuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->bms_backup_vnf: %s\n" % e)
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

# **bms_backup_vnf_delete**
> InlineResponse202 bms_backup_vnf_delete(vnfuuid)

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
    api_response = api_instance.bms_backup_vnf_delete(vnfuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->bms_backup_vnf_delete: %s\n" % e)
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

# **inventory_vnf_vport**
> InlineResponse2008 inventory_vnf_vport(vportrequest=vportrequest)

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
    api_response = api_instance.inventory_vnf_vport(vportrequest=vportrequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->inventory_vnf_vport: %s\n" % e)
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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfendpointrequest = TelstraTPN.Vnfendpointrequest() # Vnfendpointrequest |  (optional)

try:
    # Instantiate Virtual Network Function
    api_response = api_instance.inventory_vnfendpoint(vnfendpointrequest=vnfendpointrequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->inventory_vnfendpoint: %s\n" % e)
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

# **marketplace_image**
> InlineResponse2009 marketplace_image()

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
    api_response = api_instance.marketplace_image()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image: %s\n" % e)
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

# **marketplace_image_add**
> InlineResponse20010 marketplace_image_add(imageid, unknown_base_type=unknown_base_type)

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
unknown_base_type = TelstraTPN.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Add specified image to \"My Images\"
    api_response = api_instance.marketplace_image_add(imageid, unknown_base_type=unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageid** | **int**| Identifier representing a specific VNF image | 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_image_imageid**
> Image marketplace_image_imageid(imageid)

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
    api_response = api_instance.marketplace_image_imageid(imageid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_imageid: %s\n" % e)
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

# **marketplace_image_my_images**
> InlineResponse2009 marketplace_image_my_images()

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
    api_response = api_instance.marketplace_image_my_images()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_my_images: %s\n" % e)
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

# **marketplace_image_remove**
> InlineResponse20010 marketplace_image_remove(imageid, unknown_base_type=unknown_base_type)

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
unknown_base_type = TelstraTPN.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Remove specified image from \"My Images\"
    api_response = api_instance.marketplace_image_remove(imageid, unknown_base_type=unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageid** | **int**| Identifier representing a specific VNF image | 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnf**
> InlineResponse20011 vnf(vnfuuid)

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
    api_response = api_instance.vnf(vnfuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->vnf: %s\n" % e)
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

# **vnf_reboot**
> vnf_reboot(vnfuuid, rebootrequest=rebootrequest)

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
    api_instance.vnf_reboot(vnfuuid, rebootrequest=rebootrequest)
except ApiException as e:
    print("Exception when calling VnfsApi->vnf_reboot: %s\n" % e)
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

# **vnf_resume**
> vnf_resume(vnfuuid)

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
    api_instance.vnf_resume(vnfuuid)
except ApiException as e:
    print("Exception when calling VnfsApi->vnf_resume: %s\n" % e)
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

# **vnf_suspend**
> vnf_suspend(vnfuuid)

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
    api_instance.vnf_suspend(vnfuuid)
except ApiException as e:
    print("Exception when calling VnfsApi->vnf_suspend: %s\n" % e)
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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function

try:
    # Get details of a specific VNF
    api_response = api_instance.vnfendpoint_vnfuuid(vnfuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->vnfendpoint_vnfuuid: %s\n" % e)
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


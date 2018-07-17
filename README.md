# TelstraTPN
Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.


- API version: 2.4.2
- Package version: 1.0.4
For more information, please visit [https://dev.telstra.com/content/programmable-network-api](https://dev.telstra.com/content/programmable-network-api)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install


```sh
pip install git+https://github.com/Telstra/Programmable-Network-SDK-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Telstra/Programmable-Network-SDK-python.git`)

```python
import TelstraTPN 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

```python
import TelstraTPN
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.AuthenticationApi(TelstraTPN.ApiClient(configuration))
grant_type = 'password' # str |  (default to 'password')
username = 'username_example' # str | 
password = 'password_example' # str | 

try:
    # Create an authentication token
    api_response = api_instance.auth_generatetoken_post(grant_type, username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_generatetoken_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://penapi.pacnetconnect.com/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**auth_generatetoken_post**](docs/AuthenticationApi.md#auth_generatetoken_post) | **POST** /auth/generatetoken/ | Create an authentication token
*AuthenticationApi* | [**auth_validatetoken_get**](docs/AuthenticationApi.md#auth_validatetoken_get) | **GET** /auth/validatetoken/ | Validate authentication token
*ContractsApi* | [**inventory_links_linkid_contract_contractid_get**](docs/ContractsApi.md#inventory_links_linkid_contract_contractid_get) | **GET** /inventory/links/{linkid}/contract/{contractid}/ | Get active Contract by ContractID
*ContractsApi* | [**inventory_links_linkid_contract_contractid_put**](docs/ContractsApi.md#inventory_links_linkid_contract_contractid_put) | **PUT** /inventory/links/{linkid}/contract/{contractid}/ | Update active Contract by ContractID
*ContractsApi* | [**inventory_links_linkid_contract_post**](docs/ContractsApi.md#inventory_links_linkid_contract_post) | **POST** /inventory/links/{linkid}/contract/ | Create new Contract on specified link
*CustomersApi* | [**account_customeruuid_get**](docs/CustomersApi.md#account_customeruuid_get) | **GET** /account/{customeruuid}/ | Get account information details
*CustomersApi* | [**account_customeruuid_user_get**](docs/CustomersApi.md#account_customeruuid_user_get) | **GET** /account/{customeruuid}/user/ | List users
*DatacentresApi* | [**inventory_datacenters_get**](docs/DatacentresApi.md#inventory_datacenters_get) | **GET** /inventory/datacenters/ | Get list of all the data centers
*EndpointsApi* | [**endpoint_endpointuuid_endpointuuid_get**](docs/EndpointsApi.md#endpoint_endpointuuid_endpointuuid_get) | **GET** /endpoint/endpointuuid/{endpointuuid}/ | Get Endpoint name and status
*EndpointsApi* | [**endpoint_endpointuuid_endpointuuid_put**](docs/EndpointsApi.md#endpoint_endpointuuid_endpointuuid_put) | **PUT** /endpoint/endpointuuid/{endpointuuid}/ | Update Endpoint name
*EndpointsApi* | [**endpoints_endpointuuid_assign_topology_tag_post**](docs/EndpointsApi.md#endpoints_endpointuuid_assign_topology_tag_post) | **POST** /endpoints/{endpointuuid}/assign_topology_tag/ | Assign an Endpoint to a Topology
*EndpointsApi* | [**endpoints_topology_tag_uuid_topotaguuid_endpoint_endpointuuid_delete**](docs/EndpointsApi.md#endpoints_topology_tag_uuid_topotaguuid_endpoint_endpointuuid_delete) | **DELETE** /endpoints/topology_tag_uuid/{topotaguuid}/endpoint/{endpointuuid}/ | Remove Endpoint from a Topology
*EndpointsApi* | [**endpoints_topology_tag_uuid_topotaguuid_get**](docs/EndpointsApi.md#endpoints_topology_tag_uuid_topotaguuid_get) | **GET** /endpoints/topology_tag_uuid/{topotaguuid}/ | List Endpoints for Topology
*EndpointsApi* | [**inventory_endpoint_endpointuuid_get**](docs/EndpointsApi.md#inventory_endpoint_endpointuuid_get) | **GET** /inventory/endpoint/{endpointuuid}/ | Get information about the specified endpoint
*EndpointsApi* | [**inventory_endpoints_customeruuid_customeruuid_get**](docs/EndpointsApi.md#inventory_endpoints_customeruuid_customeruuid_get) | **GET** /inventory/endpoints/customeruuid/{customeruuid}/ | Get list of endpoints for a customer
*EndpointsApi* | [**inventory_links_stats_endpoint_endpointuuid_startdate_enddate_get**](docs/EndpointsApi.md#inventory_links_stats_endpoint_endpointuuid_startdate_enddate_get) | **GET** /inventory/links-stats/endpoint/{endpointuuid}/{startdate}/{enddate}/ | Get statistics for endpoint
*EndpointsApi* | [**inventory_links_stats_endpointstate_endpointuuid_startdate_enddate_get**](docs/EndpointsApi.md#inventory_links_stats_endpointstate_endpointuuid_startdate_enddate_get) | **GET** /inventory/links-stats/endpointstate/{endpointuuid}/{startdate}/{enddate}/ | Get state statistics for endpoint
*EndpointsApi* | [**inventory_regularendpoint_post**](docs/EndpointsApi.md#inventory_regularendpoint_post) | **POST** /inventory/regularendpoint/ | Create Physical (Port) Endpoint
*EndpointsApi* | [**inventory_regularvport_post**](docs/EndpointsApi.md#inventory_regularvport_post) | **POST** /inventory/regularvport/ | Create VPort for physical endpoint
*EndpointsApi* | [**inventory_vnfendpoint_post**](docs/EndpointsApi.md#inventory_vnfendpoint_post) | **POST** /inventory/vnfendpoint/ | Instantiate Virtual Network Function
*EndpointsApi* | [**vnfendpoint_vnfuuid_vnfuuid_get**](docs/EndpointsApi.md#vnfendpoint_vnfuuid_vnfuuid_get) | **GET** /vnfendpoint/vnfuuid/{vnfuuid}/ | Get details of a specific VNF
*ExchangeApi* | [**account_profile_exchange_get**](docs/ExchangeApi.md#account_profile_exchange_get) | **GET** /account/profile/exchange/ | Get the current account&#39;s Exchange profile
*ExchangeApi* | [**exchange_exprovuuid_get**](docs/ExchangeApi.md#exchange_exprovuuid_get) | **GET** /exchange/{exprovuuid}/ | Exchange provider details
*ExchangeApi* | [**exchange_get**](docs/ExchangeApi.md#exchange_get) | **GET** /exchange/ | List all Exchange providers, with POPs
*ExchangeApi* | [**visitcard_get**](docs/ExchangeApi.md#visitcard_get) | **GET** /visitcard/ | Get list of Visit Cards
*ExchangeApi* | [**visitcard_visitcarduuid_get**](docs/ExchangeApi.md#visitcard_visitcarduuid_get) | **GET** /visitcard/{visitcarduuid}/ | View details of the specified Visit Card
*ExchangeApi* | [**visitcard_visitcarduuid_put**](docs/ExchangeApi.md#visitcard_visitcarduuid_put) | **PUT** /visitcard/{visitcarduuid}/ | Update details of the specified Visit Card
*LinksApi* | [**inventory_link_post**](docs/LinksApi.md#inventory_link_post) | **POST** /inventory/link/ | Create Link and initial Contract
*LinksApi* | [**inventory_links_customer_customeruuid_get**](docs/LinksApi.md#inventory_links_customer_customeruuid_get) | **GET** /inventory/links/customer/{customeruuid}/ | Get active Links
*LinksApi* | [**inventory_links_history_linkid_get**](docs/LinksApi.md#inventory_links_history_linkid_get) | **GET** /inventory/links/history/{linkid}/ | Get Link history
*LinksApi* | [**inventory_links_linkid_get**](docs/LinksApi.md#inventory_links_linkid_get) | **GET** /inventory/links/{linkid}/ | Get details of specified link
*LinksApi* | [**inventory_links_stats_flow_linkid_startdate_enddate_get**](docs/LinksApi.md#inventory_links_stats_flow_linkid_startdate_enddate_get) | **GET** /inventory/links-stats/flow/{linkid}/{startdate}/{enddate}/ | Get statistics for flow
*StatisticsApi* | [**inventory_links_stats_endpoint_endpointuuid_startdate_enddate_get**](docs/StatisticsApi.md#inventory_links_stats_endpoint_endpointuuid_startdate_enddate_get) | **GET** /inventory/links-stats/endpoint/{endpointuuid}/{startdate}/{enddate}/ | Get statistics for endpoint
*StatisticsApi* | [**inventory_links_stats_endpointstate_endpointuuid_startdate_enddate_get**](docs/StatisticsApi.md#inventory_links_stats_endpointstate_endpointuuid_startdate_enddate_get) | **GET** /inventory/links-stats/endpointstate/{endpointuuid}/{startdate}/{enddate}/ | Get state statistics for endpoint
*StatisticsApi* | [**inventory_links_stats_flow_linkid_startdate_enddate_get**](docs/StatisticsApi.md#inventory_links_stats_flow_linkid_startdate_enddate_get) | **GET** /inventory/links-stats/flow/{linkid}/{startdate}/{enddate}/ | Get statistics for flow
*TopologiesApi* | [**endpoints_endpointuuid_assign_topology_tag_post**](docs/TopologiesApi.md#endpoints_endpointuuid_assign_topology_tag_post) | **POST** /endpoints/{endpointuuid}/assign_topology_tag/ | Assign an Endpoint to a Topology
*TopologiesApi* | [**endpoints_topology_tag_uuid_topotaguuid_endpoint_endpointuuid_delete**](docs/TopologiesApi.md#endpoints_topology_tag_uuid_topotaguuid_endpoint_endpointuuid_delete) | **DELETE** /endpoints/topology_tag_uuid/{topotaguuid}/endpoint/{endpointuuid}/ | Remove Endpoint from a Topology
*TopologiesApi* | [**endpoints_topology_tag_uuid_topotaguuid_get**](docs/TopologiesApi.md#endpoints_topology_tag_uuid_topotaguuid_get) | **GET** /endpoints/topology_tag_uuid/{topotaguuid}/ | List Endpoints for Topology
*TopologiesApi* | [**topology_tag_get**](docs/TopologiesApi.md#topology_tag_get) | **GET** /topology_tag/ | List all topology tags
*TopologiesApi* | [**topology_tag_post**](docs/TopologiesApi.md#topology_tag_post) | **POST** /topology_tag/ | Create a named topology tag
*TopologiesApi* | [**topology_tag_topotaguuid_delete**](docs/TopologiesApi.md#topology_tag_topotaguuid_delete) | **DELETE** /topology_tag/{topotaguuid}/ | Delete a topology tag
*TopologiesApi* | [**topology_tag_topotaguuid_get**](docs/TopologiesApi.md#topology_tag_topotaguuid_get) | **GET** /topology_tag/{topotaguuid}/ | Get information about the specified topology tag
*TopologiesApi* | [**topology_tag_topotaguuid_objects_get**](docs/TopologiesApi.md#topology_tag_topotaguuid_objects_get) | **GET** /topology_tag/{topotaguuid}/objects/ | List objects for Topology
*TopologiesApi* | [**topology_tag_topotaguuid_put**](docs/TopologiesApi.md#topology_tag_topotaguuid_put) | **PUT** /topology_tag/{topotaguuid}/ | Update a topology tag&#39;s name and/or description
*UsersApi* | [**account_customeruuid_user_get**](docs/UsersApi.md#account_customeruuid_user_get) | **GET** /account/{customeruuid}/user/ | List users
*VnfsApi* | [**backup_backupuuid_delete**](docs/VnfsApi.md#backup_backupuuid_delete) | **DELETE** /backup/{backupuuid}/ | Delete specified backup
*VnfsApi* | [**backup_backupuuid_get**](docs/VnfsApi.md#backup_backupuuid_get) | **GET** /backup/{backupuuid}/ | Get information about the specified backup
*VnfsApi* | [**backup_backupuuid_restore_post**](docs/VnfsApi.md#backup_backupuuid_restore_post) | **POST** /backup/{backupuuid}/restore/ | Restore VNF from backup
*VnfsApi* | [**backup_post**](docs/VnfsApi.md#backup_post) | **POST** /backup/ | Create backup of specified VNF
*VnfsApi* | [**backup_vnf_vnfuuid_delete_post**](docs/VnfsApi.md#backup_vnf_vnfuuid_delete_post) | **POST** /backup/vnf/{vnfuuid}/delete/ | Delete multiple backups
*VnfsApi* | [**backup_vnf_vnfuuid_get**](docs/VnfsApi.md#backup_vnf_vnfuuid_get) | **GET** /backup/vnf/{vnfuuid}/ | List backups
*VnfsApi* | [**inventory_vnf_vport_post**](docs/VnfsApi.md#inventory_vnf_vport_post) | **POST** /inventory/vnf/vport/ | Create VNF VPort
*VnfsApi* | [**inventory_vnfendpoint_post**](docs/VnfsApi.md#inventory_vnfendpoint_post) | **POST** /inventory/vnfendpoint/ | Instantiate Virtual Network Function
*VnfsApi* | [**marketplace_image_get**](docs/VnfsApi.md#marketplace_image_get) | **GET** /marketplace/image/ | List images in the Marketplace
*VnfsApi* | [**marketplace_image_imageid_add_to_my_images_post**](docs/VnfsApi.md#marketplace_image_imageid_add_to_my_images_post) | **POST** /marketplace/image/{imageid}/add_to_my_images/ | Add specified image to \&quot;My Images\&quot;
*VnfsApi* | [**marketplace_image_imageid_get**](docs/VnfsApi.md#marketplace_image_imageid_get) | **GET** /marketplace/image/{imageid}/ | Get information about the specified image
*VnfsApi* | [**marketplace_image_imageid_remove_from_my_images_post**](docs/VnfsApi.md#marketplace_image_imageid_remove_from_my_images_post) | **POST** /marketplace/image/{imageid}/remove_from_my_images/ | Remove specified image from \&quot;My Images\&quot;
*VnfsApi* | [**marketplace_image_my_images_get**](docs/VnfsApi.md#marketplace_image_my_images_get) | **GET** /marketplace/image/my_images/ | List images in \&quot;My Images\&quot;
*VnfsApi* | [**vnf_vnfuuid_get**](docs/VnfsApi.md#vnf_vnfuuid_get) | **GET** /vnf/{vnfuuid}/ | Get status information about the specified VNF
*VnfsApi* | [**vnf_vnfuuid_reboot_post**](docs/VnfsApi.md#vnf_vnfuuid_reboot_post) | **POST** /vnf/{vnfuuid}/reboot/ | Reboot the specified VNF
*VnfsApi* | [**vnf_vnfuuid_resume_post**](docs/VnfsApi.md#vnf_vnfuuid_resume_post) | **POST** /vnf/{vnfuuid}/resume/ | Resume the specified VNF
*VnfsApi* | [**vnf_vnfuuid_suspend_post**](docs/VnfsApi.md#vnf_vnfuuid_suspend_post) | **POST** /vnf/{vnfuuid}/suspend/ | Suspend the specified VNF
*VnfsApi* | [**vnfendpoint_vnfuuid_vnfuuid_get**](docs/VnfsApi.md#vnfendpoint_vnfuuid_vnfuuid_get) | **GET** /vnfendpoint/vnfuuid/{vnfuuid}/ | Get details of a specific VNF
*VportsApi* | [**inventory_regularvport_post**](docs/VportsApi.md#inventory_regularvport_post) | **POST** /inventory/regularvport/ | Create VPort for physical endpoint
*VportsApi* | [**inventory_vnf_vport_post**](docs/VportsApi.md#inventory_vnf_vport_post) | **POST** /inventory/vnf/vport/ | Create VNF VPort
*VportsApi* | [**inventory_vport_vportuuid_get**](docs/VportsApi.md#inventory_vport_vportuuid_get) | **GET** /inventory/vport/{vportuuid}/ | Get information about the specified VPort


## Documentation For Models

 - [Assigntopotagrequest](docs/Assigntopotagrequest.md)
 - [Backup](docs/Backup.md)
 - [Backuprequest](docs/Backuprequest.md)
 - [Billing](docs/Billing.md)
 - [Body](docs/Body.md)
 - [Connections](docs/Connections.md)
 - [Contract](docs/Contract.md)
 - [ContractresponseFragment](docs/ContractresponseFragment.md)
 - [ContractresponsefragmentParams](docs/ContractresponsefragmentParams.md)
 - [Createcontractrequest](docs/Createcontractrequest.md)
 - [Createlinkrequest](docs/Createlinkrequest.md)
 - [EndpointPort](docs/EndpointPort.md)
 - [Endpointupdaterequest](docs/Endpointupdaterequest.md)
 - [Error](docs/Error.md)
 - [ExchangeProvider](docs/ExchangeProvider.md)
 - [Flavor](docs/Flavor.md)
 - [Image](docs/Image.md)
 - [ImageClassifications](docs/ImageClassifications.md)
 - [ImageGlanceImage](docs/ImageGlanceImage.md)
 - [ImageProduct](docs/ImageProduct.md)
 - [ImageZeroDayConfigSpec](docs/ImageZeroDayConfigSpec.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20013Endpoints](docs/InlineResponse20013Endpoints.md)
 - [InlineResponse20013Links](docs/InlineResponse20013Links.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20014Endpoints](docs/InlineResponse20014Endpoints.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse20019](docs/InlineResponse20019.md)
 - [InlineResponse2001Endpointlist](docs/InlineResponse2001Endpointlist.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse20020](docs/InlineResponse20020.md)
 - [InlineResponse2002Datacenter](docs/InlineResponse2002Datacenter.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2006Params](docs/InlineResponse2006Params.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse200Datacenters](docs/InlineResponse200Datacenters.md)
 - [InlineResponse202](docs/InlineResponse202.md)
 - [InlineResponse202Errormsg](docs/InlineResponse202Errormsg.md)
 - [InlineResponse401](docs/InlineResponse401.md)
 - [InventorylinksstatsflowlinkidstartdateenddateTags](docs/InventorylinksstatsflowlinkidstartdateenddateTags.md)
 - [Link](docs/Link.md)
 - [Meta](docs/Meta.md)
 - [Pop](docs/Pop.md)
 - [Rebootrequest](docs/Rebootrequest.md)
 - [Regendpointrequest](docs/Regendpointrequest.md)
 - [Regvportrequest](docs/Regvportrequest.md)
 - [RegvportrequestVportvalue](docs/RegvportrequestVportvalue.md)
 - [Role](docs/Role.md)
 - [SuccessFragment](docs/SuccessFragment.md)
 - [Topology](docs/Topology.md)
 - [Topotagcreaterequest](docs/Topotagcreaterequest.md)
 - [Topotagupdateresponse](docs/Topotagupdateresponse.md)
 - [User](docs/User.md)
 - [Visitcard](docs/Visitcard.md)
 - [Vlan](docs/Vlan.md)
 - [VnfTag](docs/VnfTag.md)
 - [Vnfendpointrequest](docs/Vnfendpointrequest.md)
 - [Vport](docs/Vport.md)
 - [Vportrequest](docs/Vportrequest.md)


## Documentation For Authorisation


## oAuth2

- **Type**: OAuth
- **Flow**: password
- **Authorisation URL**: 
- **Scopes**: N/A


## Author

pnapi-support@team.telstra.com


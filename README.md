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
    api_response = api_instance.generate_token(grant_type, username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->generate_token: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://penapi.pacnetconnect.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**generate_token**](docs/AuthenticationApi.md#generate_token) | **POST** /1.0.0/auth/generatetoken | Create an authentication token
*AuthenticationApi* | [**validate_token**](docs/AuthenticationApi.md#validate_token) | **GET** /1.0.0/auth/validatetoken | Validate authentication token
*ContractsApi* | [**inventory_links_contract**](docs/ContractsApi.md#inventory_links_contract) | **POST** /1.0.0/inventory/links/{linkid}/contract | Create new Contract on specified link
*ContractsApi* | [**inventory_links_contract_get**](docs/ContractsApi.md#inventory_links_contract_get) | **GET** /1.0.0/inventory/links/{linkid}/contract/{contractid} | Get active Contract by ContractID
*ContractsApi* | [**inventory_links_contract_put**](docs/ContractsApi.md#inventory_links_contract_put) | **PUT** /1.0.0/inventory/links/{linkid}/contract/{contractid} | Update active Contract by ContractID
*CustomersApi* | [**account**](docs/CustomersApi.md#account) | **GET** /1.0.0/account/{customeruuid} | Get account information details
*CustomersApi* | [**account_user**](docs/CustomersApi.md#account_user) | **GET** /1.0.0/account/{customeruuid}/user | List users
*DatacentresApi* | [**inventory_datacentres**](docs/DatacentresApi.md#inventory_datacentres) | **GET** /1.0.0/inventory/datacenters | Get list of all the data centers
*EndpointsApi* | [**endpoint_endpointuuid_get**](docs/EndpointsApi.md#endpoint_endpointuuid_get) | **GET** /eis/1.0.0/endpoint/endpointuuid/{endpointuuid} | Get Endpoint name and status
*EndpointsApi* | [**endpoint_endpointuuid_put**](docs/EndpointsApi.md#endpoint_endpointuuid_put) | **PUT** /eis/1.0.0/endpoint/endpointuuid/{endpointuuid} | Update Endpoint name
*EndpointsApi* | [**endpoints_assign_topology_tag**](docs/EndpointsApi.md#endpoints_assign_topology_tag) | **POST** /eis/1.0.0/endpoints/{endpointuuid}/assign_topology_tag | Assign an Endpoint to a Topology
*EndpointsApi* | [**endpoints_topology_tag_uuid**](docs/EndpointsApi.md#endpoints_topology_tag_uuid) | **GET** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid} | List Endpoints for Topology
*EndpointsApi* | [**endpoints_topology_tag_uuid_endpoint**](docs/EndpointsApi.md#endpoints_topology_tag_uuid_endpoint) | **DELETE** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid}/endpoint/{endpointuuid} | Remove Endpoint from a Topology
*EndpointsApi* | [**inventory_endpoint**](docs/EndpointsApi.md#inventory_endpoint) | **GET** /1.0.0/inventory/endpoint/{endpointuuid} | Get information about the specified endpoint
*EndpointsApi* | [**inventory_endpoints_customeruuid**](docs/EndpointsApi.md#inventory_endpoints_customeruuid) | **GET** /1.0.0/inventory/endpoints/customeruuid/{customeruuid} | Get list of endpoints for a customer
*EndpointsApi* | [**inventory_links_stats_endpoint**](docs/EndpointsApi.md#inventory_links_stats_endpoint) | **GET** /1.0.0/inventory/links-stats/endpoint/{endpointuuid}/{startdate}/{enddate} | Get statistics for endpoint
*EndpointsApi* | [**inventory_links_stats_endpointstate**](docs/EndpointsApi.md#inventory_links_stats_endpointstate) | **GET** /1.0.0/inventory/links-stats/endpointstate/{endpointuuid}/{startdate}/{enddate} | Get state statistics for endpoint
*EndpointsApi* | [**inventory_regularendpoint**](docs/EndpointsApi.md#inventory_regularendpoint) | **POST** /1.0.0/inventory/regularendpoint | Create Physical (Port) Endpoint
*EndpointsApi* | [**inventory_regularvport**](docs/EndpointsApi.md#inventory_regularvport) | **POST** /1.0.0/inventory/regularvport | Create VPort for physical endpoint
*EndpointsApi* | [**inventory_vnfendpoint**](docs/EndpointsApi.md#inventory_vnfendpoint) | **POST** /1.0.0/inventory/vnfendpoint | Instantiate Virtual Network Function
*EndpointsApi* | [**vnfendpoint_vnfuuid**](docs/EndpointsApi.md#vnfendpoint_vnfuuid) | **GET** /eis/1.0.0/vnfendpoint/vnfuuid/{vnfuuid} | Get details of a specific VNF
*ExchangeApi* | [**account_profile_exchange**](docs/ExchangeApi.md#account_profile_exchange) | **GET** /1.0.0/account/profile/exchange | Get the current account&#39;s Exchange profile
*ExchangeApi* | [**exchange**](docs/ExchangeApi.md#exchange) | **GET** /1.0.0/exchange | List all Exchange providers, with POPs
*ExchangeApi* | [**exchange_exprovuuid**](docs/ExchangeApi.md#exchange_exprovuuid) | **GET** /1.0.0/exchange/{exprovuuid} | Exchange provider details
*ExchangeApi* | [**visitcard**](docs/ExchangeApi.md#visitcard) | **GET** /1.0.0/visitcard | Get list of Visit Cards
*ExchangeApi* | [**visitcard_uuid_get**](docs/ExchangeApi.md#visitcard_uuid_get) | **GET** /1.0.0/visitcard/{visitcarduuid} | View details of the specified Visit Card
*ExchangeApi* | [**visitcard_uuid_put**](docs/ExchangeApi.md#visitcard_uuid_put) | **PUT** /1.0.0/visitcard/{visitcarduuid} | Update details of the specified Visit Card
*LinksApi* | [**inventory_link**](docs/LinksApi.md#inventory_link) | **POST** /1.0.0/inventory/link | Create Link and initial Contract
*LinksApi* | [**inventory_links**](docs/LinksApi.md#inventory_links) | **GET** /1.0.0/inventory/links/{linkid} | Get details of specified link
*LinksApi* | [**inventory_links_customer**](docs/LinksApi.md#inventory_links_customer) | **GET** /1.0.0/inventory/links/customer/{customeruuid} | Get active Links
*LinksApi* | [**inventory_links_history**](docs/LinksApi.md#inventory_links_history) | **GET** /1.0.0/inventory/links/history/{linkid} | Get Link history
*LinksApi* | [**inventory_links_stats_flow**](docs/LinksApi.md#inventory_links_stats_flow) | **GET** /1.0.0/inventory/links-stats/flow/{linkid}/{startdate}/{enddate} | Get statistics for flow
*StatisticsApi* | [**inventory_links_stats_endpoint**](docs/StatisticsApi.md#inventory_links_stats_endpoint) | **GET** /1.0.0/inventory/links-stats/endpoint/{endpointuuid}/{startdate}/{enddate} | Get statistics for endpoint
*StatisticsApi* | [**inventory_links_stats_endpointstate**](docs/StatisticsApi.md#inventory_links_stats_endpointstate) | **GET** /1.0.0/inventory/links-stats/endpointstate/{endpointuuid}/{startdate}/{enddate} | Get state statistics for endpoint
*StatisticsApi* | [**inventory_links_stats_flow**](docs/StatisticsApi.md#inventory_links_stats_flow) | **GET** /1.0.0/inventory/links-stats/flow/{linkid}/{startdate}/{enddate} | Get statistics for flow
*TopologiesApi* | [**endpoints_assign_topology_tag**](docs/TopologiesApi.md#endpoints_assign_topology_tag) | **POST** /eis/1.0.0/endpoints/{endpointuuid}/assign_topology_tag | Assign an Endpoint to a Topology
*TopologiesApi* | [**endpoints_topology_tag_uuid**](docs/TopologiesApi.md#endpoints_topology_tag_uuid) | **GET** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid} | List Endpoints for Topology
*TopologiesApi* | [**endpoints_topology_tag_uuid_endpoint**](docs/TopologiesApi.md#endpoints_topology_tag_uuid_endpoint) | **DELETE** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid}/endpoint/{endpointuuid} | Remove Endpoint from a Topology
*TopologiesApi* | [**topology_tag_get**](docs/TopologiesApi.md#topology_tag_get) | **GET** /ttms/1.0.0/topology_tag | List all topology tags
*TopologiesApi* | [**topology_tag_objects**](docs/TopologiesApi.md#topology_tag_objects) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/objects/ | List objects for Topology
*TopologiesApi* | [**topology_tag_post**](docs/TopologiesApi.md#topology_tag_post) | **POST** /ttms/1.0.0/topology_tag | Create a named topology tag
*TopologiesApi* | [**topology_tag_uuid_delete**](docs/TopologiesApi.md#topology_tag_uuid_delete) | **DELETE** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Delete a topology tag
*TopologiesApi* | [**topology_tag_uuid_get**](docs/TopologiesApi.md#topology_tag_uuid_get) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Get information about the specified topology tag
*TopologiesApi* | [**topology_tag_uuid_put**](docs/TopologiesApi.md#topology_tag_uuid_put) | **PUT** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Update a topology tag&#39;s name and/or description
*UsersApi* | [**account_user**](docs/UsersApi.md#account_user) | **GET** /1.0.0/account/{customeruuid}/user | List users
*VnfsApi* | [**bms_backup**](docs/VnfsApi.md#bms_backup) | **POST** /bms/1.0.0/backup | Create backup of specified VNF
*VnfsApi* | [**bms_backup_delete**](docs/VnfsApi.md#bms_backup_delete) | **DELETE** /bms/1.0.0/backup/{backupuuid} | Delete specified backup
*VnfsApi* | [**bms_backup_get**](docs/VnfsApi.md#bms_backup_get) | **GET** /bms/1.0.0/backup/{backupuuid} | Get information about the specified backup
*VnfsApi* | [**bms_backup_restore**](docs/VnfsApi.md#bms_backup_restore) | **POST** /bms/1.0.0/backup/{backupuuid}/restore | Restore VNF from backup
*VnfsApi* | [**bms_backup_vnf**](docs/VnfsApi.md#bms_backup_vnf) | **GET** /bms/1.0.0/backup/vnf/{vnfuuid} | List backups
*VnfsApi* | [**bms_backup_vnf_delete**](docs/VnfsApi.md#bms_backup_vnf_delete) | **POST** /bms/1.0.0/backup/vnf/{vnfuuid}/delete | Delete multiple backups
*VnfsApi* | [**inventory_vnf_vport**](docs/VnfsApi.md#inventory_vnf_vport) | **POST** /1.0.0/inventory/vnf/vport | Create VNF VPort
*VnfsApi* | [**inventory_vnfendpoint**](docs/VnfsApi.md#inventory_vnfendpoint) | **POST** /1.0.0/inventory/vnfendpoint | Instantiate Virtual Network Function
*VnfsApi* | [**marketplace_image**](docs/VnfsApi.md#marketplace_image) | **GET** /1.0.0/marketplace/image | List images in the Marketplace
*VnfsApi* | [**marketplace_image_0**](docs/VnfsApi.md#marketplace_image_0) | **GET** /1.0.0/marketplace/image/{imageid}/ | Get information about the specified image
*VnfsApi* | [**marketplace_image_add**](docs/VnfsApi.md#marketplace_image_add) | **POST** /1.0.0/marketplace/image/{imageid}/add_to_my_images/ | Add specified image to \&quot;My Images\&quot;
*VnfsApi* | [**marketplace_image_my_images**](docs/VnfsApi.md#marketplace_image_my_images) | **GET** /1.0.0/marketplace/image/my_images/ | List images in \&quot;My Images\&quot;
*VnfsApi* | [**marketplace_image_remove**](docs/VnfsApi.md#marketplace_image_remove) | **POST** /1.0.0/marketplace/image/{imageid}/remove_from_my_images/ | Remove specified image from \&quot;My Images\&quot;
*VnfsApi* | [**vnf**](docs/VnfsApi.md#vnf) | **GET** /vnfds/1.0.0/vnf/{vnfuuid}/ | Get status information about the specified VNF
*VnfsApi* | [**vnf_reboot**](docs/VnfsApi.md#vnf_reboot) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/reboot | Reboot the specified VNF
*VnfsApi* | [**vnf_resume**](docs/VnfsApi.md#vnf_resume) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/resume | Resume the specified VNF
*VnfsApi* | [**vnf_suspend**](docs/VnfsApi.md#vnf_suspend) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/suspend | Suspend the specified VNF
*VnfsApi* | [**vnfendpoint_vnfuuid**](docs/VnfsApi.md#vnfendpoint_vnfuuid) | **GET** /eis/1.0.0/vnfendpoint/vnfuuid/{vnfuuid} | Get details of a specific VNF
*VportsApi* | [**inventory_regularvport**](docs/VportsApi.md#inventory_regularvport) | **POST** /1.0.0/inventory/regularvport | Create VPort for physical endpoint
*VportsApi* | [**inventory_vnf_vport**](docs/VportsApi.md#inventory_vnf_vport) | **POST** /1.0.0/inventory/vnf/vport | Create VNF VPort
*VportsApi* | [**inventory_vport**](docs/VportsApi.md#inventory_vport) | **GET** /1.0.0/inventory/vport/{vportuuid} | Get information about the specified VPort


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
 - [Link](docs/Link.md)
 - [Meta](docs/Meta.md)
 - [Model100inventorylinksstatsflowlinkidstartdateenddateTags](docs/Model100inventorylinksstatsflowlinkidstartdateenddateTags.md)
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



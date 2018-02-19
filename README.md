[![Build Status](https://travis-ci.org/telstra/Programmable-Network-SDK-python.svg?branch=master)](https://travis-ci.org/telstra/Programmable-Network-SDK-python)

# TelstraTPN
Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.


- API version: 2.3.3
- Package version: 1.0.1
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
api_instance = TelstraTPN.AuthenticationApi()
grant_type = 'password' # str |  (default to password)
username = 'username_example' # str | 
password = 'password_example' # str | 

try:
    # Create an authentication token
    api_response = api_instance.authgeneratetokenpost(grant_type, username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authgeneratetokenpost: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://penapi.pacnetconnect.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**authgeneratetokenpost**](docs/AuthenticationApi.md#authgeneratetokenpost) | **POST** /1.0.0/auth/generatetoken | Create an authentication token
*AuthenticationApi* | [**authvalidatetokenget**](docs/AuthenticationApi.md#authvalidatetokenget) | **GET** /1.0.0/auth/validatetoken | Validate authentication token
*ContractsApi* | [**inventorylinksget**](docs/ContractsApi.md#inventorylinksget) | **GET** /1.0.0/inventory/links/{linkid}/contract/{contractid} | Get active Contract by ContractID
*ContractsApi* | [**inventorylinkslinkidcontractpost**](docs/ContractsApi.md#inventorylinkslinkidcontractpost) | **POST** /1.0.0/inventory/links/{linkid}/contract | Create new Contract on specified link
*ContractsApi* | [**inventorylinksput**](docs/ContractsApi.md#inventorylinksput) | **PUT** /1.0.0/inventory/links/{linkid}/contract/{contractid} | Update active Contract by ContractID
*CustomersApi* | [**accountcustomeruuidget**](docs/CustomersApi.md#accountcustomeruuidget) | **GET** /1.0.0/account/{customeruuid} | Get account information details
*CustomersApi* | [**accountcustomeruuiduserget**](docs/CustomersApi.md#accountcustomeruuiduserget) | **GET** /1.0.0/account/{customeruuid}/user | List users
*DatacentresApi* | [**inventorydatacentersget**](docs/DatacentresApi.md#inventorydatacentersget) | **GET** /1.0.0/inventory/datacenters | Get list of all the data centers
*EndpointsApi* | [**eisendpointendpointuuidendpointuuidput**](docs/EndpointsApi.md#eisendpointendpointuuidendpointuuidput) | **PUT** /eis/1.0.0/endpoint/endpointuuid/{endpointuuid} | Update Endpoint name
*EndpointsApi* | [**eisendpointsendpointuuidassigntopologytagpost**](docs/EndpointsApi.md#eisendpointsendpointuuidassigntopologytagpost) | **POST** /eis/1.0.0/endpoints/{endpointuuid}/assign_topology_tag | Assign an Endpoint to a Topology
*EndpointsApi* | [**eisendpointstopologytaguuiddelete**](docs/EndpointsApi.md#eisendpointstopologytaguuiddelete) | **DELETE** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid}/endpoint/{endpointuuid} | Remove Endpoint from a Topology
*EndpointsApi* | [**eisendpointstopologytaguuidtopotaguuidget**](docs/EndpointsApi.md#eisendpointstopologytaguuidtopotaguuidget) | **GET** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid} | List Endpoints for Topology
*EndpointsApi* | [**inventoryendpointendpointuuidget**](docs/EndpointsApi.md#inventoryendpointendpointuuidget) | **GET** /1.0.0/inventory/endpoint/{endpointuuid} | Get information about the specified endpoint
*EndpointsApi* | [**inventoryendpointscustomeruuidcustomeruuidget**](docs/EndpointsApi.md#inventoryendpointscustomeruuidcustomeruuidget) | **GET** /1.0.0/inventory/endpoints/customeruuid/{customeruuid} | Get list of endpoints for a customer
*EndpointsApi* | [**inventoryregularendpointpost**](docs/EndpointsApi.md#inventoryregularendpointpost) | **POST** /1.0.0/inventory/regularendpoint | Create Physical (Port) Endpoint
*EndpointsApi* | [**inventoryregularvportpost**](docs/EndpointsApi.md#inventoryregularvportpost) | **POST** /1.0.0/inventory/regularvport | Create VPort for physical endpoint
*EndpointsApi* | [**inventoryvnfendpointpost**](docs/EndpointsApi.md#inventoryvnfendpointpost) | **POST** /1.0.0/inventory/vnfendpoint | Instantiate Virtual Network Function
*LinksApi* | [**inventorylinkpost**](docs/LinksApi.md#inventorylinkpost) | **POST** /1.0.0/inventory/link | Create Link and initial Contract
*LinksApi* | [**inventorylinkscustomercustomeruuidget**](docs/LinksApi.md#inventorylinkscustomercustomeruuidget) | **GET** /1.0.0/inventory/links/customer/{customeruuid} | Get active Links
*LinksApi* | [**inventorylinkshistorylinkidget**](docs/LinksApi.md#inventorylinkshistorylinkidget) | **GET** /1.0.0/inventory/links/history/{linkid} | Get Link history
*LinksApi* | [**inventorylinkslinkidget**](docs/LinksApi.md#inventorylinkslinkidget) | **GET** /1.0.0/inventory/links/{linkid} | Get details of specified link
*TopologiesApi* | [**eisendpointsendpointuuidassigntopologytagpost**](docs/TopologiesApi.md#eisendpointsendpointuuidassigntopologytagpost) | **POST** /eis/1.0.0/endpoints/{endpointuuid}/assign_topology_tag | Assign an Endpoint to a Topology
*TopologiesApi* | [**eisendpointstopologytaguuiddelete**](docs/TopologiesApi.md#eisendpointstopologytaguuiddelete) | **DELETE** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid}/endpoint/{endpointuuid} | Remove Endpoint from a Topology
*TopologiesApi* | [**eisendpointstopologytaguuidtopotaguuidget**](docs/TopologiesApi.md#eisendpointstopologytaguuidtopotaguuidget) | **GET** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid} | List Endpoints for Topology
*TopologiesApi* | [**ttmstopologytagget**](docs/TopologiesApi.md#ttmstopologytagget) | **GET** /ttms/1.0.0/topology_tag | List all topology tags
*TopologiesApi* | [**ttmstopologytagpost**](docs/TopologiesApi.md#ttmstopologytagpost) | **POST** /ttms/1.0.0/topology_tag | Create a named topology tag
*TopologiesApi* | [**ttmstopologytagtopotaguuiddelete**](docs/TopologiesApi.md#ttmstopologytagtopotaguuiddelete) | **DELETE** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Delete a topology tag
*TopologiesApi* | [**ttmstopologytagtopotaguuidget**](docs/TopologiesApi.md#ttmstopologytagtopotaguuidget) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Get information about the specified topology tag
*TopologiesApi* | [**ttmstopologytagtopotaguuidobjectsget**](docs/TopologiesApi.md#ttmstopologytagtopotaguuidobjectsget) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/objects/ | List objects for Topology
*TopologiesApi* | [**ttmstopologytagtopotaguuidput**](docs/TopologiesApi.md#ttmstopologytagtopotaguuidput) | **PUT** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Update a topology tag&#39;s name and/or description
*UsersApi* | [**accountcustomeruuiduserget**](docs/UsersApi.md#accountcustomeruuiduserget) | **GET** /1.0.0/account/{customeruuid}/user | List users
*VnfsApi* | [**inventoryvnfendpointpost**](docs/VnfsApi.md#inventoryvnfendpointpost) | **POST** /1.0.0/inventory/vnfendpoint | Instantiate Virtual Network Function
*VnfsApi* | [**inventoryvnfvportpost**](docs/VnfsApi.md#inventoryvnfvportpost) | **POST** /1.0.0/inventory/vnf/vport | Create VNF VPort
*VnfsApi* | [**marketplaceimageget**](docs/VnfsApi.md#marketplaceimageget) | **GET** /1.0.0/marketplace/image | List images in the Marketplace
*VnfsApi* | [**marketplaceimageimageidaddtomyimagespost**](docs/VnfsApi.md#marketplaceimageimageidaddtomyimagespost) | **POST** /1.0.0/marketplace/image/{imageid}/add_to_my_images/ | Add specified image to \&quot;My Images\&quot;
*VnfsApi* | [**marketplaceimageimageidget**](docs/VnfsApi.md#marketplaceimageimageidget) | **GET** /1.0.0/marketplace/image/{imageid}/ | Get information about the specified image
*VnfsApi* | [**marketplaceimageimageidremovefrommyimagespost**](docs/VnfsApi.md#marketplaceimageimageidremovefrommyimagespost) | **POST** /1.0.0/marketplace/image/{imageid}/remove_from_my_images/ | Remove specified image from \&quot;My Images\&quot;
*VnfsApi* | [**marketplaceimagemyimagesget**](docs/VnfsApi.md#marketplaceimagemyimagesget) | **GET** /1.0.0/marketplace/image/my_images/ | List images in \&quot;My Images\&quot;
*VnfsApi* | [**vnfdsvnfvnfuuidget**](docs/VnfsApi.md#vnfdsvnfvnfuuidget) | **GET** /vnfds/1.0.0/vnf/{vnfuuid}/ | Get status information about the specified VNF
*VnfsApi* | [**vnfdsvnfvnfuuidrebootpost**](docs/VnfsApi.md#vnfdsvnfvnfuuidrebootpost) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/reboot | Reboot the specified VNF
*VnfsApi* | [**vnfdsvnfvnfuuidresumepost**](docs/VnfsApi.md#vnfdsvnfvnfuuidresumepost) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/resume | Resume the specified VNF
*VnfsApi* | [**vnfdsvnfvnfuuidsuspendpost**](docs/VnfsApi.md#vnfdsvnfvnfuuidsuspendpost) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/suspend | Suspend the specified VNF
*VportsApi* | [**inventoryregularvportpost**](docs/VportsApi.md#inventoryregularvportpost) | **POST** /1.0.0/inventory/regularvport | Create VPort for physical endpoint
*VportsApi* | [**inventoryvnfvportpost**](docs/VportsApi.md#inventoryvnfvportpost) | **POST** /1.0.0/inventory/vnf/vport | Create VNF VPort
*VportsApi* | [**inventoryvportvportuuidget**](docs/VportsApi.md#inventoryvportvportuuidget) | **GET** /1.0.0/inventory/vport/{vportuuid} | Get information about the specified VPort


## Documentation For Models

 - [BandwidthKbs](docs/BandwidthKbs.md)
 - [BandwidthMbs](docs/BandwidthMbs.md)
 - [Billing](docs/Billing.md)
 - [Body](docs/Body.md)
 - [Body1](docs/Body1.md)
 - [Body10](docs/Body10.md)
 - [Body11](docs/Body11.md)
 - [Body12](docs/Body12.md)
 - [Body13](docs/Body13.md)
 - [Body14](docs/Body14.md)
 - [Body2](docs/Body2.md)
 - [Body3](docs/Body3.md)
 - [Body4](docs/Body4.md)
 - [Body5](docs/Body5.md)
 - [Body6](docs/Body6.md)
 - [Body7](docs/Body7.md)
 - [Body8](docs/Body8.md)
 - [Body9](docs/Body9.md)
 - [Connections](docs/Connections.md)
 - [Contract](docs/Contract.md)
 - [ContractEndTime](docs/ContractEndTime.md)
 - [ContractStartTime](docs/ContractStartTime.md)
 - [ContractStatus](docs/ContractStatus.md)
 - [Contractgetres](docs/Contractgetres.md)
 - [ContractgetresParams](docs/ContractgetresParams.md)
 - [Contractid](docs/Contractid.md)
 - [CurrencyCode](docs/CurrencyCode.md)
 - [CurrencyID](docs/CurrencyID.md)
 - [DatacenterResponse](docs/DatacenterResponse.md)
 - [DatacenterResponseDatacenter](docs/DatacenterResponseDatacenter.md)
 - [Datacenterget](docs/Datacenterget.md)
 - [DatacentergetDatacenters](docs/DatacentergetDatacenters.md)
 - [Deletedtimestamp](docs/Deletedtimestamp.md)
 - [DurationHrs](docs/DurationHrs.md)
 - [DurationMins](docs/DurationMins.md)
 - [Endpoint](docs/Endpoint.md)
 - [EndpointPort](docs/EndpointPort.md)
 - [Endpointone](docs/Endpointone.md)
 - [EndpointoneEpoint](docs/EndpointoneEpoint.md)
 - [EndpointuuidResponse](docs/EndpointuuidResponse.md)
 - [EndpointuuidResponseParams](docs/EndpointuuidResponseParams.md)
 - [Error](docs/Error.md)
 - [Flavor](docs/Flavor.md)
 - [Image](docs/Image.md)
 - [ImageClassifications](docs/ImageClassifications.md)
 - [ImageGlanceImage](docs/ImageGlanceImage.md)
 - [ImageProduct](docs/ImageProduct.md)
 - [ImageZeroDayConfigSpec](docs/ImageZeroDayConfigSpec.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse401](docs/InlineResponse401.md)
 - [Latency](docs/Latency.md)
 - [Link](docs/Link.md)
 - [Linkid](docs/Linkid.md)
 - [Links](docs/Links.md)
 - [Meta](docs/Meta.md)
 - [Price](docs/Price.md)
 - [RenewalOption](docs/RenewalOption.md)
 - [Role](docs/Role.md)
 - [SuccessContractid](docs/SuccessContractid.md)
 - [SuccessFragment](docs/SuccessFragment.md)
 - [SuccessFragment2](docs/SuccessFragment2.md)
 - [SuccessLinks](docs/SuccessLinks.md)
 - [SuccesscontractidParams](docs/SuccesscontractidParams.md)
 - [SuccesslinksParams](docs/SuccesslinksParams.md)
 - [Topology](docs/Topology.md)
 - [User](docs/User.md)
 - [Version](docs/Version.md)
 - [Vlan](docs/Vlan.md)
 - [VnfTag](docs/VnfTag.md)
 - [Vport](docs/Vport.md)
 - [VportVportvalue](docs/VportVportvalue.md)
 - [Vportvalue](docs/Vportvalue.md)


## Documentation For Authorisation


## oAuth2

- **Type**: OAuth
- **Flow**: password
- **Authorisation URL**: 
- **Scopes**: 
 - **oAuth2**: oAuth2


## Author

pnapi-support@team.telstra.com


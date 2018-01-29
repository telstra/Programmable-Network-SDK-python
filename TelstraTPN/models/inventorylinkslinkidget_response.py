# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.  # noqa: E501

    OpenAPI spec version: 2.3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from TelstraTPN.models.contract import Contract  # noqa: F401,E501


class InventorylinkslinkidgetResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'billing_id': 'str',
        'connections': 'list[str]',
        'contracts': 'list[Contract]',
        'description': 'str',
        'latency': 'int',
        'link_status': 'int',
        'linkid': 'str',
        'tag': 'str',
        'topology_tag_uuid': 'str',
        'type': 'str'
    }

    attribute_map = {
        'billing_id': 'billing-id',
        'connections': 'connections',
        'contracts': 'contracts',
        'description': 'description',
        'latency': 'latency',
        'link_status': 'linkStatus',
        'linkid': 'linkid',
        'tag': 'tag',
        'topology_tag_uuid': 'topology_tag_uuid',
        'type': 'type'
    }

    def __init__(self, billing_id=None, connections=None, contracts=None, description=None, latency=None, link_status=None, linkid=None, tag=None, topology_tag_uuid=None, type=None):  # noqa: E501
        """InventorylinkslinkidgetResponse - a model defined in Swagger"""  # noqa: E501

        self._billing_id = None
        self._connections = None
        self._contracts = None
        self._description = None
        self._latency = None
        self._link_status = None
        self._linkid = None
        self._tag = None
        self._topology_tag_uuid = None
        self._type = None
        self.discriminator = None

        if billing_id is not None:
            self.billing_id = billing_id
        if connections is not None:
            self.connections = connections
        if contracts is not None:
            self.contracts = contracts
        if description is not None:
            self.description = description
        if latency is not None:
            self.latency = latency
        if link_status is not None:
            self.link_status = link_status
        if linkid is not None:
            self.linkid = linkid
        if tag is not None:
            self.tag = tag
        if topology_tag_uuid is not None:
            self.topology_tag_uuid = topology_tag_uuid
        if type is not None:
            self.type = type

    @property
    def billing_id(self):
        """Gets the billing_id of this InventorylinkslinkidgetResponse.  # noqa: E501

          # noqa: E501

        :return: The billing_id of this InventorylinkslinkidgetResponse.  # noqa: E501
        :rtype: str
        """
        return self._billing_id

    @billing_id.setter
    def billing_id(self, billing_id):
        """Sets the billing_id of this InventorylinkslinkidgetResponse.

          # noqa: E501

        :param billing_id: The billing_id of this InventorylinkslinkidgetResponse.  # noqa: E501
        :type: str
        """

        self._billing_id = billing_id

    @property
    def connections(self):
        """Gets the connections of this InventorylinkslinkidgetResponse.  # noqa: E501

          # noqa: E501

        :return: The connections of this InventorylinkslinkidgetResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this InventorylinkslinkidgetResponse.

          # noqa: E501

        :param connections: The connections of this InventorylinkslinkidgetResponse.  # noqa: E501
        :type: list[str]
        """

        self._connections = connections

    @property
    def contracts(self):
        """Gets the contracts of this InventorylinkslinkidgetResponse.  # noqa: E501

          # noqa: E501

        :return: The contracts of this InventorylinkslinkidgetResponse.  # noqa: E501
        :rtype: list[Contract]
        """
        return self._contracts

    @contracts.setter
    def contracts(self, contracts):
        """Sets the contracts of this InventorylinkslinkidgetResponse.

          # noqa: E501

        :param contracts: The contracts of this InventorylinkslinkidgetResponse.  # noqa: E501
        :type: list[Contract]
        """

        self._contracts = contracts

    @property
    def description(self):
        """Gets the description of this InventorylinkslinkidgetResponse.  # noqa: E501

          # noqa: E501

        :return: The description of this InventorylinkslinkidgetResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InventorylinkslinkidgetResponse.

          # noqa: E501

        :param description: The description of this InventorylinkslinkidgetResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def latency(self):
        """Gets the latency of this InventorylinkslinkidgetResponse.  # noqa: E501

        Latency: 0=Low, 1=Standard, 2=Best Effort  # noqa: E501

        :return: The latency of this InventorylinkslinkidgetResponse.  # noqa: E501
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this InventorylinkslinkidgetResponse.

        Latency: 0=Low, 1=Standard, 2=Best Effort  # noqa: E501

        :param latency: The latency of this InventorylinkslinkidgetResponse.  # noqa: E501
        :type: int
        """

        self._latency = latency

    @property
    def link_status(self):
        """Gets the link_status of this InventorylinkslinkidgetResponse.  # noqa: E501

          # noqa: E501

        :return: The link_status of this InventorylinkslinkidgetResponse.  # noqa: E501
        :rtype: int
        """
        return self._link_status

    @link_status.setter
    def link_status(self, link_status):
        """Sets the link_status of this InventorylinkslinkidgetResponse.

          # noqa: E501

        :param link_status: The link_status of this InventorylinkslinkidgetResponse.  # noqa: E501
        :type: int
        """

        self._link_status = link_status

    @property
    def linkid(self):
        """Gets the linkid of this InventorylinkslinkidgetResponse.  # noqa: E501

        Identifier of a link  # noqa: E501

        :return: The linkid of this InventorylinkslinkidgetResponse.  # noqa: E501
        :rtype: str
        """
        return self._linkid

    @linkid.setter
    def linkid(self, linkid):
        """Sets the linkid of this InventorylinkslinkidgetResponse.

        Identifier of a link  # noqa: E501

        :param linkid: The linkid of this InventorylinkslinkidgetResponse.  # noqa: E501
        :type: str
        """

        self._linkid = linkid

    @property
    def tag(self):
        """Gets the tag of this InventorylinkslinkidgetResponse.  # noqa: E501

          # noqa: E501

        :return: The tag of this InventorylinkslinkidgetResponse.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this InventorylinkslinkidgetResponse.

          # noqa: E501

        :param tag: The tag of this InventorylinkslinkidgetResponse.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def topology_tag_uuid(self):
        """Gets the topology_tag_uuid of this InventorylinkslinkidgetResponse.  # noqa: E501

          # noqa: E501

        :return: The topology_tag_uuid of this InventorylinkslinkidgetResponse.  # noqa: E501
        :rtype: str
        """
        return self._topology_tag_uuid

    @topology_tag_uuid.setter
    def topology_tag_uuid(self, topology_tag_uuid):
        """Sets the topology_tag_uuid of this InventorylinkslinkidgetResponse.

          # noqa: E501

        :param topology_tag_uuid: The topology_tag_uuid of this InventorylinkslinkidgetResponse.  # noqa: E501
        :type: str
        """

        self._topology_tag_uuid = topology_tag_uuid

    @property
    def type(self):
        """Gets the type of this InventorylinkslinkidgetResponse.  # noqa: E501

          # noqa: E501

        :return: The type of this InventorylinkslinkidgetResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InventorylinkslinkidgetResponse.

          # noqa: E501

        :param type: The type of this InventorylinkslinkidgetResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InventorylinkslinkidgetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
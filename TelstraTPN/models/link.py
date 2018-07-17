# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.  # noqa: E501

    OpenAPI spec version: 2.4.2
    Contact: pnapi-support@team.telstra.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Link(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'description': 'str',
        'latency': 'int',
        'linkid': 'str',
        'contracts': 'list[Contract]',
        'tag': 'str',
        'connections': 'Connections',
        'type': 'str',
        'link_status': 'int',
        'billing_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'latency': 'latency',
        'linkid': 'linkid',
        'contracts': 'contracts',
        'tag': 'tag',
        'connections': 'connections',
        'type': 'type',
        'link_status': 'linkStatus',
        'billing_id': 'billing-id'
    }

    def __init__(self, description=None, latency=None, linkid=None, contracts=None, tag=None, connections=None, type=None, link_status=None, billing_id=None):  # noqa: E501
        """Link - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._latency = None
        self._linkid = None
        self._contracts = None
        self._tag = None
        self._connections = None
        self._type = None
        self._link_status = None
        self._billing_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if latency is not None:
            self.latency = latency
        if linkid is not None:
            self.linkid = linkid
        if contracts is not None:
            self.contracts = contracts
        if tag is not None:
            self.tag = tag
        if connections is not None:
            self.connections = connections
        if type is not None:
            self.type = type
        if link_status is not None:
            self.link_status = link_status
        if billing_id is not None:
            self.billing_id = billing_id

    @property
    def description(self):
        """Gets the description of this Link.  # noqa: E501


        :return: The description of this Link.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Link.


        :param description: The description of this Link.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def latency(self):
        """Gets the latency of this Link.  # noqa: E501


        :return: The latency of this Link.  # noqa: E501
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this Link.


        :param latency: The latency of this Link.  # noqa: E501
        :type: int
        """

        self._latency = latency

    @property
    def linkid(self):
        """Gets the linkid of this Link.  # noqa: E501


        :return: The linkid of this Link.  # noqa: E501
        :rtype: str
        """
        return self._linkid

    @linkid.setter
    def linkid(self, linkid):
        """Sets the linkid of this Link.


        :param linkid: The linkid of this Link.  # noqa: E501
        :type: str
        """

        self._linkid = linkid

    @property
    def contracts(self):
        """Gets the contracts of this Link.  # noqa: E501


        :return: The contracts of this Link.  # noqa: E501
        :rtype: list[Contract]
        """
        return self._contracts

    @contracts.setter
    def contracts(self, contracts):
        """Sets the contracts of this Link.


        :param contracts: The contracts of this Link.  # noqa: E501
        :type: list[Contract]
        """

        self._contracts = contracts

    @property
    def tag(self):
        """Gets the tag of this Link.  # noqa: E501


        :return: The tag of this Link.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Link.


        :param tag: The tag of this Link.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def connections(self):
        """Gets the connections of this Link.  # noqa: E501


        :return: The connections of this Link.  # noqa: E501
        :rtype: Connections
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this Link.


        :param connections: The connections of this Link.  # noqa: E501
        :type: Connections
        """

        self._connections = connections

    @property
    def type(self):
        """Gets the type of this Link.  # noqa: E501


        :return: The type of this Link.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Link.


        :param type: The type of this Link.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def link_status(self):
        """Gets the link_status of this Link.  # noqa: E501


        :return: The link_status of this Link.  # noqa: E501
        :rtype: int
        """
        return self._link_status

    @link_status.setter
    def link_status(self, link_status):
        """Sets the link_status of this Link.


        :param link_status: The link_status of this Link.  # noqa: E501
        :type: int
        """

        self._link_status = link_status

    @property
    def billing_id(self):
        """Gets the billing_id of this Link.  # noqa: E501


        :return: The billing_id of this Link.  # noqa: E501
        :rtype: str
        """
        return self._billing_id

    @billing_id.setter
    def billing_id(self, billing_id):
        """Sets the billing_id of this Link.


        :param billing_id: The billing_id of this Link.  # noqa: E501
        :type: str
        """

        self._billing_id = billing_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Link):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

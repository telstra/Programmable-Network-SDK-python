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


class Body(object):
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
        'bandwidth': 'int',
        'billing_id': 'str',
        'connections': 'list[str]',
        'description': 'str',
        'duration': 'int',
        'latency': 'int',
        'link_type': 'int',
        'renewal_option': 'int',
        'tag': 'str',
        'topology_tag_uuid': 'str'
    }

    attribute_map = {
        'bandwidth': 'bandwidth',
        'billing_id': 'billing-id',
        'connections': 'connections',
        'description': 'description',
        'duration': 'duration',
        'latency': 'latency',
        'link_type': 'link-type',
        'renewal_option': 'renewal-option',
        'tag': 'tag',
        'topology_tag_uuid': 'topology_tag_uuid'
    }

    def __init__(self, bandwidth=None, billing_id=None, connections=None, description=None, duration=None, latency=None, link_type=None, renewal_option=None, tag=None, topology_tag_uuid=None):  # noqa: E501
        """Body - a model defined in Swagger"""  # noqa: E501

        self._bandwidth = None
        self._billing_id = None
        self._connections = None
        self._description = None
        self._duration = None
        self._latency = None
        self._link_type = None
        self._renewal_option = None
        self._tag = None
        self._topology_tag_uuid = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if billing_id is not None:
            self.billing_id = billing_id
        if connections is not None:
            self.connections = connections
        if description is not None:
            self.description = description
        if duration is not None:
            self.duration = duration
        if latency is not None:
            self.latency = latency
        if link_type is not None:
            self.link_type = link_type
        if renewal_option is not None:
            self.renewal_option = renewal_option
        if tag is not None:
            self.tag = tag
        if topology_tag_uuid is not None:
            self.topology_tag_uuid = topology_tag_uuid

    @property
    def bandwidth(self):
        """Gets the bandwidth of this Body.  # noqa: E501

        Bandwidth in kB/s  # noqa: E501

        :return: The bandwidth of this Body.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this Body.

        Bandwidth in kB/s  # noqa: E501

        :param bandwidth: The bandwidth of this Body.  # noqa: E501
        :type: int
        """
        if bandwidth is not None and bandwidth > 10000000:  # noqa: E501
            raise ValueError("Invalid value for `bandwidth`, must be a value less than or equal to `10000000`")  # noqa: E501
        if bandwidth is not None and bandwidth < 1000:  # noqa: E501
            raise ValueError("Invalid value for `bandwidth`, must be a value greater than or equal to `1000`")  # noqa: E501

        self._bandwidth = bandwidth

    @property
    def billing_id(self):
        """Gets the billing_id of this Body.  # noqa: E501

          # noqa: E501

        :return: The billing_id of this Body.  # noqa: E501
        :rtype: str
        """
        return self._billing_id

    @billing_id.setter
    def billing_id(self, billing_id):
        """Sets the billing_id of this Body.

          # noqa: E501

        :param billing_id: The billing_id of this Body.  # noqa: E501
        :type: str
        """

        self._billing_id = billing_id

    @property
    def connections(self):
        """Gets the connections of this Body.  # noqa: E501

          # noqa: E501

        :return: The connections of this Body.  # noqa: E501
        :rtype: list[str]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this Body.

          # noqa: E501

        :param connections: The connections of this Body.  # noqa: E501
        :type: list[str]
        """

        self._connections = connections

    @property
    def description(self):
        """Gets the description of this Body.  # noqa: E501

          # noqa: E501

        :return: The description of this Body.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Body.

          # noqa: E501

        :param description: The description of this Body.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def duration(self):
        """Gets the duration of this Body.  # noqa: E501

        Duration of contract in minutes  # noqa: E501

        :return: The duration of this Body.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Body.

        Duration of contract in minutes  # noqa: E501

        :param duration: The duration of this Body.  # noqa: E501
        :type: int
        """
        if duration is not None and duration < 3600:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `3600`")  # noqa: E501

        self._duration = duration

    @property
    def latency(self):
        """Gets the latency of this Body.  # noqa: E501

        Latency: 0=Low, 1=Standard, 2=Best Effort  # noqa: E501

        :return: The latency of this Body.  # noqa: E501
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this Body.

        Latency: 0=Low, 1=Standard, 2=Best Effort  # noqa: E501

        :param latency: The latency of this Body.  # noqa: E501
        :type: int
        """

        self._latency = latency

    @property
    def link_type(self):
        """Gets the link_type of this Body.  # noqa: E501

        1=VLAN, 2=VNF  # noqa: E501

        :return: The link_type of this Body.  # noqa: E501
        :rtype: int
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """Sets the link_type of this Body.

        1=VLAN, 2=VNF  # noqa: E501

        :param link_type: The link_type of this Body.  # noqa: E501
        :type: int
        """

        self._link_type = link_type

    @property
    def renewal_option(self):
        """Gets the renewal_option of this Body.  # noqa: E501

        \"Renewal Option: 0=Auto Disconnect, 1=Auto Renew, 2=Pay per hour\"  # noqa: E501

        :return: The renewal_option of this Body.  # noqa: E501
        :rtype: int
        """
        return self._renewal_option

    @renewal_option.setter
    def renewal_option(self, renewal_option):
        """Sets the renewal_option of this Body.

        \"Renewal Option: 0=Auto Disconnect, 1=Auto Renew, 2=Pay per hour\"  # noqa: E501

        :param renewal_option: The renewal_option of this Body.  # noqa: E501
        :type: int
        """

        self._renewal_option = renewal_option

    @property
    def tag(self):
        """Gets the tag of this Body.  # noqa: E501

          # noqa: E501

        :return: The tag of this Body.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Body.

          # noqa: E501

        :param tag: The tag of this Body.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def topology_tag_uuid(self):
        """Gets the topology_tag_uuid of this Body.  # noqa: E501

          # noqa: E501

        :return: The topology_tag_uuid of this Body.  # noqa: E501
        :rtype: str
        """
        return self._topology_tag_uuid

    @topology_tag_uuid.setter
    def topology_tag_uuid(self, topology_tag_uuid):
        """Sets the topology_tag_uuid of this Body.

          # noqa: E501

        :param topology_tag_uuid: The topology_tag_uuid of this Body.  # noqa: E501
        :type: str
        """

        self._topology_tag_uuid = topology_tag_uuid

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
        if not isinstance(other, Body):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.  # noqa: E501

    OpenAPI spec version: 2.4.1
    Contact: pnapi-support@team.telstra.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Body7(object):
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
        'config': 'str',
        'customeruuid': 'str',
        'datacenteruuid': 'str',
        'flavoruuid': 'int',
        'imageuuid': 'int',
        'topology_tag_uuid': 'str'
    }

    attribute_map = {
        'config': 'config',
        'customeruuid': 'customeruuid',
        'datacenteruuid': 'datacenteruuid',
        'flavoruuid': 'flavoruuid',
        'imageuuid': 'imageuuid',
        'topology_tag_uuid': 'topology_tag_uuid'
    }

    def __init__(self, config=None, customeruuid=None, datacenteruuid=None, flavoruuid=None, imageuuid=None, topology_tag_uuid=None):  # noqa: E501
        """Body7 - a model defined in Swagger"""  # noqa: E501

        self._config = None
        self._customeruuid = None
        self._datacenteruuid = None
        self._flavoruuid = None
        self._imageuuid = None
        self._topology_tag_uuid = None
        self.discriminator = None

        self.config = config
        self.customeruuid = customeruuid
        self.datacenteruuid = datacenteruuid
        self.flavoruuid = flavoruuid
        self.imageuuid = imageuuid
        if topology_tag_uuid is not None:
            self.topology_tag_uuid = topology_tag_uuid

    @property
    def config(self):
        """Gets the config of this Body7.  # noqa: E501

        Boot configuration for VNF, base64 encoded  # noqa: E501

        :return: The config of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Body7.

        Boot configuration for VNF, base64 encoded  # noqa: E501

        :param config: The config of this Body7.  # noqa: E501
        :type: str
        """
        if config is None:
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config

    @property
    def customeruuid(self):
        """Gets the customeruuid of this Body7.  # noqa: E501


        :return: The customeruuid of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._customeruuid

    @customeruuid.setter
    def customeruuid(self, customeruuid):
        """Sets the customeruuid of this Body7.


        :param customeruuid: The customeruuid of this Body7.  # noqa: E501
        :type: str
        """
        if customeruuid is None:
            raise ValueError("Invalid value for `customeruuid`, must not be `None`")  # noqa: E501

        self._customeruuid = customeruuid

    @property
    def datacenteruuid(self):
        """Gets the datacenteruuid of this Body7.  # noqa: E501


        :return: The datacenteruuid of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._datacenteruuid

    @datacenteruuid.setter
    def datacenteruuid(self, datacenteruuid):
        """Sets the datacenteruuid of this Body7.


        :param datacenteruuid: The datacenteruuid of this Body7.  # noqa: E501
        :type: str
        """
        if datacenteruuid is None:
            raise ValueError("Invalid value for `datacenteruuid`, must not be `None`")  # noqa: E501

        self._datacenteruuid = datacenteruuid

    @property
    def flavoruuid(self):
        """Gets the flavoruuid of this Body7.  # noqa: E501


        :return: The flavoruuid of this Body7.  # noqa: E501
        :rtype: int
        """
        return self._flavoruuid

    @flavoruuid.setter
    def flavoruuid(self, flavoruuid):
        """Sets the flavoruuid of this Body7.


        :param flavoruuid: The flavoruuid of this Body7.  # noqa: E501
        :type: int
        """
        if flavoruuid is None:
            raise ValueError("Invalid value for `flavoruuid`, must not be `None`")  # noqa: E501

        self._flavoruuid = flavoruuid

    @property
    def imageuuid(self):
        """Gets the imageuuid of this Body7.  # noqa: E501


        :return: The imageuuid of this Body7.  # noqa: E501
        :rtype: int
        """
        return self._imageuuid

    @imageuuid.setter
    def imageuuid(self, imageuuid):
        """Sets the imageuuid of this Body7.


        :param imageuuid: The imageuuid of this Body7.  # noqa: E501
        :type: int
        """
        if imageuuid is None:
            raise ValueError("Invalid value for `imageuuid`, must not be `None`")  # noqa: E501

        self._imageuuid = imageuuid

    @property
    def topology_tag_uuid(self):
        """Gets the topology_tag_uuid of this Body7.  # noqa: E501


        :return: The topology_tag_uuid of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._topology_tag_uuid

    @topology_tag_uuid.setter
    def topology_tag_uuid(self, topology_tag_uuid):
        """Sets the topology_tag_uuid of this Body7.


        :param topology_tag_uuid: The topology_tag_uuid of this Body7.  # noqa: E501
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
        if not isinstance(other, Body7):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

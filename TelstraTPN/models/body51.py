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


class Body51(object):
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
        'customeruuid': 'str',
        'datacenteruuid': 'str',
        'interfacetype': 'str'
    }

    attribute_map = {
        'customeruuid': 'customeruuid',
        'datacenteruuid': 'datacenteruuid',
        'interfacetype': 'interfacetype'
    }

    def __init__(self, customeruuid=None, datacenteruuid=None, interfacetype=None):  # noqa: E501
        """Body51 - a model defined in Swagger"""  # noqa: E501

        self._customeruuid = None
        self._datacenteruuid = None
        self._interfacetype = None
        self.discriminator = None

        if customeruuid is not None:
            self.customeruuid = customeruuid
        if datacenteruuid is not None:
            self.datacenteruuid = datacenteruuid
        if interfacetype is not None:
            self.interfacetype = interfacetype

    @property
    def customeruuid(self):
        """Gets the customeruuid of this Body51.  # noqa: E501

          # noqa: E501

        :return: The customeruuid of this Body51.  # noqa: E501
        :rtype: str
        """
        return self._customeruuid

    @customeruuid.setter
    def customeruuid(self, customeruuid):
        """Sets the customeruuid of this Body51.

          # noqa: E501

        :param customeruuid: The customeruuid of this Body51.  # noqa: E501
        :type: str
        """

        self._customeruuid = customeruuid

    @property
    def datacenteruuid(self):
        """Gets the datacenteruuid of this Body51.  # noqa: E501

          # noqa: E501

        :return: The datacenteruuid of this Body51.  # noqa: E501
        :rtype: str
        """
        return self._datacenteruuid

    @datacenteruuid.setter
    def datacenteruuid(self, datacenteruuid):
        """Sets the datacenteruuid of this Body51.

          # noqa: E501

        :param datacenteruuid: The datacenteruuid of this Body51.  # noqa: E501
        :type: str
        """

        self._datacenteruuid = datacenteruuid

    @property
    def interfacetype(self):
        """Gets the interfacetype of this Body51.  # noqa: E501

          # noqa: E501

        :return: The interfacetype of this Body51.  # noqa: E501
        :rtype: str
        """
        return self._interfacetype

    @interfacetype.setter
    def interfacetype(self, interfacetype):
        """Sets the interfacetype of this Body51.

          # noqa: E501

        :param interfacetype: The interfacetype of this Body51.  # noqa: E501
        :type: str
        """

        self._interfacetype = interfacetype

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
        if not isinstance(other, Body51):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class Rebootrequest(object):
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
        'reboot_type': 'str'
    }

    attribute_map = {
        'reboot_type': 'reboot_type'
    }

    def __init__(self, reboot_type=None):  # noqa: E501
        """Rebootrequest - a model defined in OpenAPI"""  # noqa: E501

        self._reboot_type = None
        self.discriminator = None

        if reboot_type is not None:
            self.reboot_type = reboot_type

    @property
    def reboot_type(self):
        """Gets the reboot_type of this Rebootrequest.  # noqa: E501


        :return: The reboot_type of this Rebootrequest.  # noqa: E501
        :rtype: str
        """
        return self._reboot_type

    @reboot_type.setter
    def reboot_type(self, reboot_type):
        """Sets the reboot_type of this Rebootrequest.


        :param reboot_type: The reboot_type of this Rebootrequest.  # noqa: E501
        :type: str
        """

        self._reboot_type = reboot_type

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
        if not isinstance(other, Rebootrequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

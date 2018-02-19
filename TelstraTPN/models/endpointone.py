# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.  # noqa: E501

    OpenAPI spec version: 2.3.3
    Contact: pnapi-support@team.telstra.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from TelstraTPN.models.endpointone_epoint import EndpointoneEpoint  # noqa: F401,E501


class Endpointone(object):
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
        'epoint': 'list[EndpointoneEpoint]'
    }

    attribute_map = {
        'epoint': 'epoint'
    }

    def __init__(self, epoint=None):  # noqa: E501
        """Endpointone - a model defined in Swagger"""  # noqa: E501

        self._epoint = None
        self.discriminator = None

        if epoint is not None:
            self.epoint = epoint

    @property
    def epoint(self):
        """Gets the epoint of this Endpointone.  # noqa: E501


        :return: The epoint of this Endpointone.  # noqa: E501
        :rtype: list[EndpointoneEpoint]
        """
        return self._epoint

    @epoint.setter
    def epoint(self, epoint):
        """Sets the epoint of this Endpointone.


        :param epoint: The epoint of this Endpointone.  # noqa: E501
        :type: list[EndpointoneEpoint]
        """

        self._epoint = epoint

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
        if not isinstance(other, Endpointone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
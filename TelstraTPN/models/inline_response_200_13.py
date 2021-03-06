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


class InlineResponse20013(object):
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
        'vnfuuid': 'str',
        'vnportuuid': 'str'
    }

    attribute_map = {
        'vnfuuid': 'vnfuuid',
        'vnportuuid': 'vnportuuid'
    }

    def __init__(self, vnfuuid=None, vnportuuid=None):  # noqa: E501
        """InlineResponse20013 - a model defined in Swagger"""  # noqa: E501

        self._vnfuuid = None
        self._vnportuuid = None
        self.discriminator = None

        if vnfuuid is not None:
            self.vnfuuid = vnfuuid
        if vnportuuid is not None:
            self.vnportuuid = vnportuuid

    @property
    def vnfuuid(self):
        """Gets the vnfuuid of this InlineResponse20013.  # noqa: E501

        vnfuuid which was passed in the request  # noqa: E501

        :return: The vnfuuid of this InlineResponse20013.  # noqa: E501
        :rtype: str
        """
        return self._vnfuuid

    @vnfuuid.setter
    def vnfuuid(self, vnfuuid):
        """Sets the vnfuuid of this InlineResponse20013.

        vnfuuid which was passed in the request  # noqa: E501

        :param vnfuuid: The vnfuuid of this InlineResponse20013.  # noqa: E501
        :type: str
        """

        self._vnfuuid = vnfuuid

    @property
    def vnportuuid(self):
        """Gets the vnportuuid of this InlineResponse20013.  # noqa: E501

        uuid of the newly-created vport  # noqa: E501

        :return: The vnportuuid of this InlineResponse20013.  # noqa: E501
        :rtype: str
        """
        return self._vnportuuid

    @vnportuuid.setter
    def vnportuuid(self, vnportuuid):
        """Sets the vnportuuid of this InlineResponse20013.

        uuid of the newly-created vport  # noqa: E501

        :param vnportuuid: The vnportuuid of this InlineResponse20013.  # noqa: E501
        :type: str
        """

        self._vnportuuid = vnportuuid

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
        if not isinstance(other, InlineResponse20013):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class InlineResponse2009(object):
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
        'meta': 'Meta',
        'objects': 'list[Image]'
    }

    attribute_map = {
        'meta': 'meta',
        'objects': 'objects'
    }

    def __init__(self, meta=None, objects=None):  # noqa: E501
        """InlineResponse2009 - a model defined in OpenAPI"""  # noqa: E501

        self._meta = None
        self._objects = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        if objects is not None:
            self.objects = objects

    @property
    def meta(self):
        """Gets the meta of this InlineResponse2009.  # noqa: E501


        :return: The meta of this InlineResponse2009.  # noqa: E501
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this InlineResponse2009.


        :param meta: The meta of this InlineResponse2009.  # noqa: E501
        :type: Meta
        """

        self._meta = meta

    @property
    def objects(self):
        """Gets the objects of this InlineResponse2009.  # noqa: E501


        :return: The objects of this InlineResponse2009.  # noqa: E501
        :rtype: list[Image]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this InlineResponse2009.


        :param objects: The objects of this InlineResponse2009.  # noqa: E501
        :type: list[Image]
        """

        self._objects = objects

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
        if not isinstance(other, InlineResponse2009):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

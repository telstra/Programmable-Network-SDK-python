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


class Meta(object):
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
        'limit': 'int',
        'next': 'int',
        'offset': 'int',
        'previous': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'next': 'next',
        'offset': 'offset',
        'previous': 'previous',
        'total_count': 'total_count'
    }

    def __init__(self, limit=None, next=None, offset=None, previous=None, total_count=None):  # noqa: E501
        """Meta - a model defined in OpenAPI"""  # noqa: E501

        self._limit = None
        self._next = None
        self._offset = None
        self._previous = None
        self._total_count = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if next is not None:
            self.next = next
        if offset is not None:
            self.offset = offset
        if previous is not None:
            self.previous = previous
        if total_count is not None:
            self.total_count = total_count

    @property
    def limit(self):
        """Gets the limit of this Meta.  # noqa: E501


        :return: The limit of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this Meta.


        :param limit: The limit of this Meta.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """Gets the next of this Meta.  # noqa: E501


        :return: The next of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Meta.


        :param next: The next of this Meta.  # noqa: E501
        :type: int
        """

        self._next = next

    @property
    def offset(self):
        """Gets the offset of this Meta.  # noqa: E501


        :return: The offset of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this Meta.


        :param offset: The offset of this Meta.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def previous(self):
        """Gets the previous of this Meta.  # noqa: E501


        :return: The previous of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this Meta.


        :param previous: The previous of this Meta.  # noqa: E501
        :type: int
        """

        self._previous = previous

    @property
    def total_count(self):
        """Gets the total_count of this Meta.  # noqa: E501


        :return: The total_count of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this Meta.


        :param total_count: The total_count of this Meta.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if not isinstance(other, Meta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

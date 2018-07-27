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


class Pop(object):
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
        'datacentername': 'str',
        'datacenteruuid': 'str',
        'datacentercode': 'str'
    }

    attribute_map = {
        'datacentername': 'datacentername',
        'datacenteruuid': 'datacenteruuid',
        'datacentercode': 'datacentercode'
    }

    def __init__(self, datacentername=None, datacenteruuid=None, datacentercode=None):  # noqa: E501
        """Pop - a model defined in OpenAPI"""  # noqa: E501

        self._datacentername = None
        self._datacenteruuid = None
        self._datacentercode = None
        self.discriminator = None

        if datacentername is not None:
            self.datacentername = datacentername
        if datacenteruuid is not None:
            self.datacenteruuid = datacenteruuid
        if datacentercode is not None:
            self.datacentercode = datacentercode

    @property
    def datacentername(self):
        """Gets the datacentername of this Pop.  # noqa: E501

        Name of the data centre  # noqa: E501

        :return: The datacentername of this Pop.  # noqa: E501
        :rtype: str
        """
        return self._datacentername

    @datacentername.setter
    def datacentername(self, datacentername):
        """Sets the datacentername of this Pop.

        Name of the data centre  # noqa: E501

        :param datacentername: The datacentername of this Pop.  # noqa: E501
        :type: str
        """

        self._datacentername = datacentername

    @property
    def datacenteruuid(self):
        """Gets the datacenteruuid of this Pop.  # noqa: E501

        UUID of the data centre  # noqa: E501

        :return: The datacenteruuid of this Pop.  # noqa: E501
        :rtype: str
        """
        return self._datacenteruuid

    @datacenteruuid.setter
    def datacenteruuid(self, datacenteruuid):
        """Sets the datacenteruuid of this Pop.

        UUID of the data centre  # noqa: E501

        :param datacenteruuid: The datacenteruuid of this Pop.  # noqa: E501
        :type: str
        """

        self._datacenteruuid = datacenteruuid

    @property
    def datacentercode(self):
        """Gets the datacentercode of this Pop.  # noqa: E501

        Four-letter code unique to the data centre  # noqa: E501

        :return: The datacentercode of this Pop.  # noqa: E501
        :rtype: str
        """
        return self._datacentercode

    @datacentercode.setter
    def datacentercode(self, datacentercode):
        """Sets the datacentercode of this Pop.

        Four-letter code unique to the data centre  # noqa: E501

        :param datacentercode: The datacentercode of this Pop.  # noqa: E501
        :type: str
        """

        self._datacentercode = datacentercode

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
        if not isinstance(other, Pop):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
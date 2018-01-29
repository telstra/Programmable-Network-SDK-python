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


class InventoryregularvportpostResponse(object):
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
        'success_auxiliary': 'str',
        'success_code': 'int',
        'success_message': 'str',
        'vportuuid': 'str'
    }

    attribute_map = {
        'success_auxiliary': 'success-auxiliary',
        'success_code': 'success-code',
        'success_message': 'success-message',
        'vportuuid': 'vportuuid'
    }

    def __init__(self, success_auxiliary=None, success_code=None, success_message=None, vportuuid=None):  # noqa: E501
        """InventoryregularvportpostResponse - a model defined in Swagger"""  # noqa: E501

        self._success_auxiliary = None
        self._success_code = None
        self._success_message = None
        self._vportuuid = None
        self.discriminator = None

        if success_auxiliary is not None:
            self.success_auxiliary = success_auxiliary
        if success_code is not None:
            self.success_code = success_code
        if success_message is not None:
            self.success_message = success_message
        if vportuuid is not None:
            self.vportuuid = vportuuid

    @property
    def success_auxiliary(self):
        """Gets the success_auxiliary of this InventoryregularvportpostResponse.  # noqa: E501

          # noqa: E501

        :return: The success_auxiliary of this InventoryregularvportpostResponse.  # noqa: E501
        :rtype: str
        """
        return self._success_auxiliary

    @success_auxiliary.setter
    def success_auxiliary(self, success_auxiliary):
        """Sets the success_auxiliary of this InventoryregularvportpostResponse.

          # noqa: E501

        :param success_auxiliary: The success_auxiliary of this InventoryregularvportpostResponse.  # noqa: E501
        :type: str
        """

        self._success_auxiliary = success_auxiliary

    @property
    def success_code(self):
        """Gets the success_code of this InventoryregularvportpostResponse.  # noqa: E501

          # noqa: E501

        :return: The success_code of this InventoryregularvportpostResponse.  # noqa: E501
        :rtype: int
        """
        return self._success_code

    @success_code.setter
    def success_code(self, success_code):
        """Sets the success_code of this InventoryregularvportpostResponse.

          # noqa: E501

        :param success_code: The success_code of this InventoryregularvportpostResponse.  # noqa: E501
        :type: int
        """

        self._success_code = success_code

    @property
    def success_message(self):
        """Gets the success_message of this InventoryregularvportpostResponse.  # noqa: E501

          # noqa: E501

        :return: The success_message of this InventoryregularvportpostResponse.  # noqa: E501
        :rtype: str
        """
        return self._success_message

    @success_message.setter
    def success_message(self, success_message):
        """Sets the success_message of this InventoryregularvportpostResponse.

          # noqa: E501

        :param success_message: The success_message of this InventoryregularvportpostResponse.  # noqa: E501
        :type: str
        """

        self._success_message = success_message

    @property
    def vportuuid(self):
        """Gets the vportuuid of this InventoryregularvportpostResponse.  # noqa: E501

          # noqa: E501

        :return: The vportuuid of this InventoryregularvportpostResponse.  # noqa: E501
        :rtype: str
        """
        return self._vportuuid

    @vportuuid.setter
    def vportuuid(self, vportuuid):
        """Sets the vportuuid of this InventoryregularvportpostResponse.

          # noqa: E501

        :param vportuuid: The vportuuid of this InventoryregularvportpostResponse.  # noqa: E501
        :type: str
        """

        self._vportuuid = vportuuid

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
        if not isinstance(other, InventoryregularvportpostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
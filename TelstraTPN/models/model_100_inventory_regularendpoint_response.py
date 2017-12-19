# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.

    OpenAPI spec version: 2.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Model100InventoryRegularendpointResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'endpointuuid': 'str'
    }

    attribute_map = {
        'success_auxiliary': 'success-auxiliary',
        'success_code': 'success-code',
        'success_message': 'success-message',
        'endpointuuid': 'endpointuuid'
    }

    def __init__(self, success_auxiliary=None, success_code=None, success_message=None, endpointuuid=None):
        """
        Model100InventoryRegularendpointResponse - a model defined in Swagger
        """

        self._success_auxiliary = None
        self._success_code = None
        self._success_message = None
        self._endpointuuid = None

        if success_auxiliary is not None:
          self.success_auxiliary = success_auxiliary
        if success_code is not None:
          self.success_code = success_code
        if success_message is not None:
          self.success_message = success_message
        if endpointuuid is not None:
          self.endpointuuid = endpointuuid

    @property
    def success_auxiliary(self):
        """
        Gets the success_auxiliary of this Model100InventoryRegularendpointResponse.
        

        :return: The success_auxiliary of this Model100InventoryRegularendpointResponse.
        :rtype: str
        """
        return self._success_auxiliary

    @success_auxiliary.setter
    def success_auxiliary(self, success_auxiliary):
        """
        Sets the success_auxiliary of this Model100InventoryRegularendpointResponse.
        

        :param success_auxiliary: The success_auxiliary of this Model100InventoryRegularendpointResponse.
        :type: str
        """

        self._success_auxiliary = success_auxiliary

    @property
    def success_code(self):
        """
        Gets the success_code of this Model100InventoryRegularendpointResponse.
        

        :return: The success_code of this Model100InventoryRegularendpointResponse.
        :rtype: int
        """
        return self._success_code

    @success_code.setter
    def success_code(self, success_code):
        """
        Sets the success_code of this Model100InventoryRegularendpointResponse.
        

        :param success_code: The success_code of this Model100InventoryRegularendpointResponse.
        :type: int
        """

        self._success_code = success_code

    @property
    def success_message(self):
        """
        Gets the success_message of this Model100InventoryRegularendpointResponse.
        

        :return: The success_message of this Model100InventoryRegularendpointResponse.
        :rtype: str
        """
        return self._success_message

    @success_message.setter
    def success_message(self, success_message):
        """
        Sets the success_message of this Model100InventoryRegularendpointResponse.
        

        :param success_message: The success_message of this Model100InventoryRegularendpointResponse.
        :type: str
        """

        self._success_message = success_message

    @property
    def endpointuuid(self):
        """
        Gets the endpointuuid of this Model100InventoryRegularendpointResponse.
        

        :return: The endpointuuid of this Model100InventoryRegularendpointResponse.
        :rtype: str
        """
        return self._endpointuuid

    @endpointuuid.setter
    def endpointuuid(self, endpointuuid):
        """
        Sets the endpointuuid of this Model100InventoryRegularendpointResponse.
        

        :param endpointuuid: The endpointuuid of this Model100InventoryRegularendpointResponse.
        :type: str
        """

        self._endpointuuid = endpointuuid

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Model100InventoryRegularendpointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

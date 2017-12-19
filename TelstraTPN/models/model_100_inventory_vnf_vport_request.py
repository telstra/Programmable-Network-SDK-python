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


class Model100InventoryVnfVportRequest(object):
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
        'customeruuid': 'str',
        'vnfuuid': 'str',
        'management_port': 'bool'
    }

    attribute_map = {
        'customeruuid': 'customeruuid',
        'vnfuuid': 'vnfuuid',
        'management_port': 'management_port'
    }

    def __init__(self, customeruuid=None, vnfuuid=None, management_port=None):
        """
        Model100InventoryVnfVportRequest - a model defined in Swagger
        """

        self._customeruuid = None
        self._vnfuuid = None
        self._management_port = None

        if customeruuid is not None:
          self.customeruuid = customeruuid
        if vnfuuid is not None:
          self.vnfuuid = vnfuuid
        if management_port is not None:
          self.management_port = management_port

    @property
    def customeruuid(self):
        """
        Gets the customeruuid of this Model100InventoryVnfVportRequest.
        

        :return: The customeruuid of this Model100InventoryVnfVportRequest.
        :rtype: str
        """
        return self._customeruuid

    @customeruuid.setter
    def customeruuid(self, customeruuid):
        """
        Sets the customeruuid of this Model100InventoryVnfVportRequest.
        

        :param customeruuid: The customeruuid of this Model100InventoryVnfVportRequest.
        :type: str
        """

        self._customeruuid = customeruuid

    @property
    def vnfuuid(self):
        """
        Gets the vnfuuid of this Model100InventoryVnfVportRequest.
        

        :return: The vnfuuid of this Model100InventoryVnfVportRequest.
        :rtype: str
        """
        return self._vnfuuid

    @vnfuuid.setter
    def vnfuuid(self, vnfuuid):
        """
        Sets the vnfuuid of this Model100InventoryVnfVportRequest.
        

        :param vnfuuid: The vnfuuid of this Model100InventoryVnfVportRequest.
        :type: str
        """

        self._vnfuuid = vnfuuid

    @property
    def management_port(self):
        """
        Gets the management_port of this Model100InventoryVnfVportRequest.
        

        :return: The management_port of this Model100InventoryVnfVportRequest.
        :rtype: bool
        """
        return self._management_port

    @management_port.setter
    def management_port(self, management_port):
        """
        Sets the management_port of this Model100InventoryVnfVportRequest.
        

        :param management_port: The management_port of this Model100InventoryVnfVportRequest.
        :type: bool
        """

        self._management_port = management_port

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
        if not isinstance(other, Model100InventoryVnfVportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

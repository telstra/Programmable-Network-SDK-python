# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.  # noqa: E501

    OpenAPI spec version: 2.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InventoryDatacentersResponse(object):
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
        'cityname': 'str',
        'countryname': 'str',
        'datacentername': 'str',
        'datacentercode': 'str',
        'datacenteruuid': 'str',
        'interfacetypes': 'list[str]',
        'operatorname': 'str'
    }

    attribute_map = {
        'cityname': 'cityname',
        'countryname': 'countryname',
        'datacentername': 'datacentername',
        'datacentercode': 'datacentercode',
        'datacenteruuid': 'datacenteruuid',
        'interfacetypes': 'interfacetypes',
        'operatorname': 'operatorname'
    }

    def __init__(self, cityname=None, countryname=None, datacentername=None, datacentercode=None, datacenteruuid=None, interfacetypes=None, operatorname=None):  # noqa: E501
        """InventoryDatacentersResponse - a model defined in Swagger"""  # noqa: E501

        self._cityname = None
        self._countryname = None
        self._datacentername = None
        self._datacentercode = None
        self._datacenteruuid = None
        self._interfacetypes = None
        self._operatorname = None
        self.discriminator = None

        if cityname is not None:
            self.cityname = cityname
        if countryname is not None:
            self.countryname = countryname
        if datacentername is not None:
            self.datacentername = datacentername
        if datacentercode is not None:
            self.datacentercode = datacentercode
        if datacenteruuid is not None:
            self.datacenteruuid = datacenteruuid
        if interfacetypes is not None:
            self.interfacetypes = interfacetypes
        if operatorname is not None:
            self.operatorname = operatorname

    @property
    def cityname(self):
        """Gets the cityname of this InventoryDatacentersResponse.  # noqa: E501

          # noqa: E501

        :return: The cityname of this InventoryDatacentersResponse.  # noqa: E501
        :rtype: str
        """
        return self._cityname

    @cityname.setter
    def cityname(self, cityname):
        """Sets the cityname of this InventoryDatacentersResponse.

          # noqa: E501

        :param cityname: The cityname of this InventoryDatacentersResponse.  # noqa: E501
        :type: str
        """

        self._cityname = cityname

    @property
    def countryname(self):
        """Gets the countryname of this InventoryDatacentersResponse.  # noqa: E501

          # noqa: E501

        :return: The countryname of this InventoryDatacentersResponse.  # noqa: E501
        :rtype: str
        """
        return self._countryname

    @countryname.setter
    def countryname(self, countryname):
        """Sets the countryname of this InventoryDatacentersResponse.

          # noqa: E501

        :param countryname: The countryname of this InventoryDatacentersResponse.  # noqa: E501
        :type: str
        """

        self._countryname = countryname

    @property
    def datacentername(self):
        """Gets the datacentername of this InventoryDatacentersResponse.  # noqa: E501

          # noqa: E501

        :return: The datacentername of this InventoryDatacentersResponse.  # noqa: E501
        :rtype: str
        """
        return self._datacentername

    @datacentername.setter
    def datacentername(self, datacentername):
        """Sets the datacentername of this InventoryDatacentersResponse.

          # noqa: E501

        :param datacentername: The datacentername of this InventoryDatacentersResponse.  # noqa: E501
        :type: str
        """

        self._datacentername = datacentername

    @property
    def datacentercode(self):
        """Gets the datacentercode of this InventoryDatacentersResponse.  # noqa: E501

          # noqa: E501

        :return: The datacentercode of this InventoryDatacentersResponse.  # noqa: E501
        :rtype: str
        """
        return self._datacentercode

    @datacentercode.setter
    def datacentercode(self, datacentercode):
        """Sets the datacentercode of this InventoryDatacentersResponse.

          # noqa: E501

        :param datacentercode: The datacentercode of this InventoryDatacentersResponse.  # noqa: E501
        :type: str
        """

        self._datacentercode = datacentercode

    @property
    def datacenteruuid(self):
        """Gets the datacenteruuid of this InventoryDatacentersResponse.  # noqa: E501

          # noqa: E501

        :return: The datacenteruuid of this InventoryDatacentersResponse.  # noqa: E501
        :rtype: str
        """
        return self._datacenteruuid

    @datacenteruuid.setter
    def datacenteruuid(self, datacenteruuid):
        """Sets the datacenteruuid of this InventoryDatacentersResponse.

          # noqa: E501

        :param datacenteruuid: The datacenteruuid of this InventoryDatacentersResponse.  # noqa: E501
        :type: str
        """

        self._datacenteruuid = datacenteruuid

    @property
    def interfacetypes(self):
        """Gets the interfacetypes of this InventoryDatacentersResponse.  # noqa: E501

          # noqa: E501

        :return: The interfacetypes of this InventoryDatacentersResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._interfacetypes

    @interfacetypes.setter
    def interfacetypes(self, interfacetypes):
        """Sets the interfacetypes of this InventoryDatacentersResponse.

          # noqa: E501

        :param interfacetypes: The interfacetypes of this InventoryDatacentersResponse.  # noqa: E501
        :type: list[str]
        """

        self._interfacetypes = interfacetypes

    @property
    def operatorname(self):
        """Gets the operatorname of this InventoryDatacentersResponse.  # noqa: E501

          # noqa: E501

        :return: The operatorname of this InventoryDatacentersResponse.  # noqa: E501
        :rtype: str
        """
        return self._operatorname

    @operatorname.setter
    def operatorname(self, operatorname):
        """Sets the operatorname of this InventoryDatacentersResponse.

          # noqa: E501

        :param operatorname: The operatorname of this InventoryDatacentersResponse.  # noqa: E501
        :type: str
        """

        self._operatorname = operatorname

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
        if not isinstance(other, InventoryDatacentersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
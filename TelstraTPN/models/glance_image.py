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


class GlanceImage(object):
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
        'create_at': 'str',
        'id': 'int',
        'name': 'str',
        'owner': 'str',
        'status': 'str'
    }

    attribute_map = {
        'create_at': 'create_at',
        'id': 'id',
        'name': 'name',
        'owner': 'owner',
        'status': 'status'
    }

    def __init__(self, create_at=None, id=None, name=None, owner=None, status=None):  # noqa: E501
        """GlanceImage - a model defined in Swagger"""  # noqa: E501

        self._create_at = None
        self._id = None
        self._name = None
        self._owner = None
        self._status = None
        self.discriminator = None

        if create_at is not None:
            self.create_at = create_at
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if status is not None:
            self.status = status

    @property
    def create_at(self):
        """Gets the create_at of this GlanceImage.  # noqa: E501

          # noqa: E501

        :return: The create_at of this GlanceImage.  # noqa: E501
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this GlanceImage.

          # noqa: E501

        :param create_at: The create_at of this GlanceImage.  # noqa: E501
        :type: str
        """

        self._create_at = create_at

    @property
    def id(self):
        """Gets the id of this GlanceImage.  # noqa: E501

          # noqa: E501

        :return: The id of this GlanceImage.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GlanceImage.

          # noqa: E501

        :param id: The id of this GlanceImage.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GlanceImage.  # noqa: E501

          # noqa: E501

        :return: The name of this GlanceImage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlanceImage.

          # noqa: E501

        :param name: The name of this GlanceImage.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this GlanceImage.  # noqa: E501

          # noqa: E501

        :return: The owner of this GlanceImage.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this GlanceImage.

          # noqa: E501

        :param owner: The owner of this GlanceImage.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def status(self):
        """Gets the status of this GlanceImage.  # noqa: E501

          # noqa: E501

        :return: The status of this GlanceImage.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GlanceImage.

          # noqa: E501

        :param status: The status of this GlanceImage.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, GlanceImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

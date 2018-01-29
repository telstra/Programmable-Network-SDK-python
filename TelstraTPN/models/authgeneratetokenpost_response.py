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


class AuthgeneratetokenpostResponse(object):
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
        'access_token': 'str',
        'expires_in': 'int',
        'refresh_token': 'str',
        'token_type': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'expires_in': 'expires_in',
        'refresh_token': 'refresh_token',
        'token_type': 'token_type'
    }

    def __init__(self, access_token=None, expires_in=None, refresh_token=None, token_type=None):  # noqa: E501
        """AuthgeneratetokenpostResponse - a model defined in Swagger"""  # noqa: E501

        self._access_token = None
        self._expires_in = None
        self._refresh_token = None
        self._token_type = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if expires_in is not None:
            self.expires_in = expires_in
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if token_type is not None:
            self.token_type = token_type

    @property
    def access_token(self):
        """Gets the access_token of this AuthgeneratetokenpostResponse.  # noqa: E501

          # noqa: E501

        :return: The access_token of this AuthgeneratetokenpostResponse.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this AuthgeneratetokenpostResponse.

          # noqa: E501

        :param access_token: The access_token of this AuthgeneratetokenpostResponse.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def expires_in(self):
        """Gets the expires_in of this AuthgeneratetokenpostResponse.  # noqa: E501

          # noqa: E501

        :return: The expires_in of this AuthgeneratetokenpostResponse.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this AuthgeneratetokenpostResponse.

          # noqa: E501

        :param expires_in: The expires_in of this AuthgeneratetokenpostResponse.  # noqa: E501
        :type: int
        """

        self._expires_in = expires_in

    @property
    def refresh_token(self):
        """Gets the refresh_token of this AuthgeneratetokenpostResponse.  # noqa: E501

          # noqa: E501

        :return: The refresh_token of this AuthgeneratetokenpostResponse.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this AuthgeneratetokenpostResponse.

          # noqa: E501

        :param refresh_token: The refresh_token of this AuthgeneratetokenpostResponse.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def token_type(self):
        """Gets the token_type of this AuthgeneratetokenpostResponse.  # noqa: E501

          # noqa: E501

        :return: The token_type of this AuthgeneratetokenpostResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this AuthgeneratetokenpostResponse.

          # noqa: E501

        :param token_type: The token_type of this AuthgeneratetokenpostResponse.  # noqa: E501
        :type: str
        """

        self._token_type = token_type

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
        if not isinstance(other, AuthgeneratetokenpostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

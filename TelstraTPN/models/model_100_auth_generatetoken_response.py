# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.

    OpenAPI spec version: 2.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Model100AuthGeneratetokenResponse(object):
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
        'token_type': 'str',
        'expires_in': 'int',
        'refresh_token': 'str',
        'access_token': 'str'
    }

    attribute_map = {
        'token_type': 'token_type',
        'expires_in': 'expires_in',
        'refresh_token': 'refresh_token',
        'access_token': 'access_token'
    }

    def __init__(self, token_type=None, expires_in=None, refresh_token=None, access_token=None):
        """
        Model100AuthGeneratetokenResponse - a model defined in Swagger
        """

        self._token_type = None
        self._expires_in = None
        self._refresh_token = None
        self._access_token = None

        if token_type is not None:
          self.token_type = token_type
        if expires_in is not None:
          self.expires_in = expires_in
        if refresh_token is not None:
          self.refresh_token = refresh_token
        if access_token is not None:
          self.access_token = access_token

    @property
    def token_type(self):
        """
        Gets the token_type of this Model100AuthGeneratetokenResponse.
        

        :return: The token_type of this Model100AuthGeneratetokenResponse.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """
        Sets the token_type of this Model100AuthGeneratetokenResponse.
        

        :param token_type: The token_type of this Model100AuthGeneratetokenResponse.
        :type: str
        """

        self._token_type = token_type

    @property
    def expires_in(self):
        """
        Gets the expires_in of this Model100AuthGeneratetokenResponse.
        

        :return: The expires_in of this Model100AuthGeneratetokenResponse.
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """
        Sets the expires_in of this Model100AuthGeneratetokenResponse.
        

        :param expires_in: The expires_in of this Model100AuthGeneratetokenResponse.
        :type: int
        """

        self._expires_in = expires_in

    @property
    def refresh_token(self):
        """
        Gets the refresh_token of this Model100AuthGeneratetokenResponse.
        

        :return: The refresh_token of this Model100AuthGeneratetokenResponse.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """
        Sets the refresh_token of this Model100AuthGeneratetokenResponse.
        

        :param refresh_token: The refresh_token of this Model100AuthGeneratetokenResponse.
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def access_token(self):
        """
        Gets the access_token of this Model100AuthGeneratetokenResponse.
        

        :return: The access_token of this Model100AuthGeneratetokenResponse.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this Model100AuthGeneratetokenResponse.
        

        :param access_token: The access_token of this Model100AuthGeneratetokenResponse.
        :type: str
        """

        self._access_token = access_token

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
        if not isinstance(other, Model100AuthGeneratetokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

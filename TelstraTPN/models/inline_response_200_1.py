# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.  # noqa: E501

    OpenAPI spec version: 2.4.1
    Contact: pnapi-support@team.telstra.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse2001(object):
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
        'address': 'str',
        'city': 'str',
        'companyname': 'str',
        'companyuuid': 'str',
        'country': 'str',
        'customeraccountid': 'str',
        'customertype': 'str',
        'fax': 'str',
        'phone': 'str',
        'postalcode': 'str',
        'state': 'str',
        'status': 'str',
        'website': 'str'
    }

    attribute_map = {
        'address': 'address',
        'city': 'city',
        'companyname': 'companyname',
        'companyuuid': 'companyuuid',
        'country': 'country',
        'customeraccountid': 'customeraccountid',
        'customertype': 'customertype',
        'fax': 'fax',
        'phone': 'phone',
        'postalcode': 'postalcode',
        'state': 'state',
        'status': 'status',
        'website': 'website'
    }

    def __init__(self, address=None, city=None, companyname=None, companyuuid=None, country=None, customeraccountid=None, customertype=None, fax=None, phone=None, postalcode=None, state=None, status=None, website=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._city = None
        self._companyname = None
        self._companyuuid = None
        self._country = None
        self._customeraccountid = None
        self._customertype = None
        self._fax = None
        self._phone = None
        self._postalcode = None
        self._state = None
        self._status = None
        self._website = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if companyname is not None:
            self.companyname = companyname
        if companyuuid is not None:
            self.companyuuid = companyuuid
        if country is not None:
            self.country = country
        if customeraccountid is not None:
            self.customeraccountid = customeraccountid
        if customertype is not None:
            self.customertype = customertype
        if fax is not None:
            self.fax = fax
        if phone is not None:
            self.phone = phone
        if postalcode is not None:
            self.postalcode = postalcode
        if state is not None:
            self.state = state
        if status is not None:
            self.status = status
        if website is not None:
            self.website = website

    @property
    def address(self):
        """Gets the address of this InlineResponse2001.  # noqa: E501


        :return: The address of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this InlineResponse2001.


        :param address: The address of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def city(self):
        """Gets the city of this InlineResponse2001.  # noqa: E501


        :return: The city of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this InlineResponse2001.


        :param city: The city of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def companyname(self):
        """Gets the companyname of this InlineResponse2001.  # noqa: E501


        :return: The companyname of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._companyname

    @companyname.setter
    def companyname(self, companyname):
        """Sets the companyname of this InlineResponse2001.


        :param companyname: The companyname of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._companyname = companyname

    @property
    def companyuuid(self):
        """Gets the companyuuid of this InlineResponse2001.  # noqa: E501


        :return: The companyuuid of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._companyuuid

    @companyuuid.setter
    def companyuuid(self, companyuuid):
        """Sets the companyuuid of this InlineResponse2001.


        :param companyuuid: The companyuuid of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._companyuuid = companyuuid

    @property
    def country(self):
        """Gets the country of this InlineResponse2001.  # noqa: E501


        :return: The country of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this InlineResponse2001.


        :param country: The country of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def customeraccountid(self):
        """Gets the customeraccountid of this InlineResponse2001.  # noqa: E501


        :return: The customeraccountid of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._customeraccountid

    @customeraccountid.setter
    def customeraccountid(self, customeraccountid):
        """Sets the customeraccountid of this InlineResponse2001.


        :param customeraccountid: The customeraccountid of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._customeraccountid = customeraccountid

    @property
    def customertype(self):
        """Gets the customertype of this InlineResponse2001.  # noqa: E501


        :return: The customertype of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._customertype

    @customertype.setter
    def customertype(self, customertype):
        """Sets the customertype of this InlineResponse2001.


        :param customertype: The customertype of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._customertype = customertype

    @property
    def fax(self):
        """Gets the fax of this InlineResponse2001.  # noqa: E501


        :return: The fax of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this InlineResponse2001.


        :param fax: The fax of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def phone(self):
        """Gets the phone of this InlineResponse2001.  # noqa: E501


        :return: The phone of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this InlineResponse2001.


        :param phone: The phone of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def postalcode(self):
        """Gets the postalcode of this InlineResponse2001.  # noqa: E501


        :return: The postalcode of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._postalcode

    @postalcode.setter
    def postalcode(self, postalcode):
        """Sets the postalcode of this InlineResponse2001.


        :param postalcode: The postalcode of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._postalcode = postalcode

    @property
    def state(self):
        """Gets the state of this InlineResponse2001.  # noqa: E501


        :return: The state of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineResponse2001.


        :param state: The state of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def status(self):
        """Gets the status of this InlineResponse2001.  # noqa: E501


        :return: The status of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2001.


        :param status: The status of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def website(self):
        """Gets the website of this InlineResponse2001.  # noqa: E501


        :return: The website of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this InlineResponse2001.


        :param website: The website of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._website = website

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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

from TelstraTPN.models.bandwidth_kbs import BandwidthKbs  # noqa: F401,E501
from TelstraTPN.models.contractid import Contractid  # noqa: F401,E501
from TelstraTPN.models.currency_id import CurrencyID  # noqa: F401,E501
from TelstraTPN.models.duration_mins import DurationMins  # noqa: F401,E501
from TelstraTPN.models.linkid import Linkid  # noqa: F401,E501
from TelstraTPN.models.price import Price  # noqa: F401,E501
from TelstraTPN.models.renewal_option import RenewalOption  # noqa: F401,E501


class ContractresschemaParams(object):
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
        'bandwidth': 'BandwidthKbs',
        'contractid': 'Contractid',
        'currency_id': 'CurrencyID',
        'duration': 'DurationMins',
        'linkid': 'Linkid',
        'price': 'Price',
        'renewal_option': 'RenewalOption'
    }

    attribute_map = {
        'bandwidth': 'bandwidth',
        'contractid': 'contractid',
        'currency_id': 'currencyId',
        'duration': 'duration',
        'linkid': 'linkid',
        'price': 'price',
        'renewal_option': 'renewal-option'
    }

    def __init__(self, bandwidth=None, contractid=None, currency_id=None, duration=None, linkid=None, price=None, renewal_option=None):  # noqa: E501
        """ContractresschemaParams - a model defined in Swagger"""  # noqa: E501

        self._bandwidth = None
        self._contractid = None
        self._currency_id = None
        self._duration = None
        self._linkid = None
        self._price = None
        self._renewal_option = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if contractid is not None:
            self.contractid = contractid
        if currency_id is not None:
            self.currency_id = currency_id
        if duration is not None:
            self.duration = duration
        if linkid is not None:
            self.linkid = linkid
        if price is not None:
            self.price = price
        if renewal_option is not None:
            self.renewal_option = renewal_option

    @property
    def bandwidth(self):
        """Gets the bandwidth of this ContractresschemaParams.  # noqa: E501


        :return: The bandwidth of this ContractresschemaParams.  # noqa: E501
        :rtype: BandwidthKbs
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this ContractresschemaParams.


        :param bandwidth: The bandwidth of this ContractresschemaParams.  # noqa: E501
        :type: BandwidthKbs
        """

        self._bandwidth = bandwidth

    @property
    def contractid(self):
        """Gets the contractid of this ContractresschemaParams.  # noqa: E501


        :return: The contractid of this ContractresschemaParams.  # noqa: E501
        :rtype: Contractid
        """
        return self._contractid

    @contractid.setter
    def contractid(self, contractid):
        """Sets the contractid of this ContractresschemaParams.


        :param contractid: The contractid of this ContractresschemaParams.  # noqa: E501
        :type: Contractid
        """

        self._contractid = contractid

    @property
    def currency_id(self):
        """Gets the currency_id of this ContractresschemaParams.  # noqa: E501


        :return: The currency_id of this ContractresschemaParams.  # noqa: E501
        :rtype: CurrencyID
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this ContractresschemaParams.


        :param currency_id: The currency_id of this ContractresschemaParams.  # noqa: E501
        :type: CurrencyID
        """

        self._currency_id = currency_id

    @property
    def duration(self):
        """Gets the duration of this ContractresschemaParams.  # noqa: E501


        :return: The duration of this ContractresschemaParams.  # noqa: E501
        :rtype: DurationMins
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ContractresschemaParams.


        :param duration: The duration of this ContractresschemaParams.  # noqa: E501
        :type: DurationMins
        """

        self._duration = duration

    @property
    def linkid(self):
        """Gets the linkid of this ContractresschemaParams.  # noqa: E501


        :return: The linkid of this ContractresschemaParams.  # noqa: E501
        :rtype: Linkid
        """
        return self._linkid

    @linkid.setter
    def linkid(self, linkid):
        """Sets the linkid of this ContractresschemaParams.


        :param linkid: The linkid of this ContractresschemaParams.  # noqa: E501
        :type: Linkid
        """

        self._linkid = linkid

    @property
    def price(self):
        """Gets the price of this ContractresschemaParams.  # noqa: E501


        :return: The price of this ContractresschemaParams.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ContractresschemaParams.


        :param price: The price of this ContractresschemaParams.  # noqa: E501
        :type: Price
        """

        self._price = price

    @property
    def renewal_option(self):
        """Gets the renewal_option of this ContractresschemaParams.  # noqa: E501


        :return: The renewal_option of this ContractresschemaParams.  # noqa: E501
        :rtype: RenewalOption
        """
        return self._renewal_option

    @renewal_option.setter
    def renewal_option(self, renewal_option):
        """Sets the renewal_option of this ContractresschemaParams.


        :param renewal_option: The renewal_option of this ContractresschemaParams.  # noqa: E501
        :type: RenewalOption
        """

        self._renewal_option = renewal_option

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
        if not isinstance(other, ContractresschemaParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

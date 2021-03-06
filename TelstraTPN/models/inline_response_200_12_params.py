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
from TelstraTPN.models.connections import Connections  # noqa: F401,E501
from TelstraTPN.models.contract_end_time import ContractEndTime  # noqa: F401,E501
from TelstraTPN.models.contract_start_time import ContractStartTime  # noqa: F401,E501
from TelstraTPN.models.contract_status import ContractStatus  # noqa: F401,E501
from TelstraTPN.models.contractid import Contractid  # noqa: F401,E501
from TelstraTPN.models.deletedtimestamp import Deletedtimestamp  # noqa: F401,E501
from TelstraTPN.models.duration_mins import DurationMins  # noqa: F401,E501
from TelstraTPN.models.latency import Latency  # noqa: F401,E501
from TelstraTPN.models.linkid import Linkid  # noqa: F401,E501
from TelstraTPN.models.price import Price  # noqa: F401,E501
from TelstraTPN.models.renewal_option import RenewalOption  # noqa: F401,E501
from TelstraTPN.models.version import Version  # noqa: F401,E501


class InlineResponse20012Params(object):
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
        'billing_id': 'str',
        'connection': 'Connections',
        'contract_end_time': 'ContractEndTime',
        'contract_start_time': 'ContractStartTime',
        'contract_status': 'ContractStatus',
        'contractid': 'Contractid',
        'deletedtimestamp': 'Deletedtimestamp',
        'description': 'str',
        'duration': 'DurationMins',
        'latency': 'Latency',
        'linkid': 'Linkid',
        'price': 'Price',
        'renewal_option': 'RenewalOption',
        'tag': 'str',
        'type': 'str',
        'version': 'Version'
    }

    attribute_map = {
        'bandwidth': 'bandwidth',
        'billing_id': 'billing-id',
        'connection': 'connection',
        'contract_end_time': 'contract-end-time',
        'contract_start_time': 'contract-start-time',
        'contract_status': 'contractStatus',
        'contractid': 'contractid',
        'deletedtimestamp': 'deletedtimestamp',
        'description': 'description',
        'duration': 'duration',
        'latency': 'latency',
        'linkid': 'linkid',
        'price': 'price',
        'renewal_option': 'renewal-option',
        'tag': 'tag',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, bandwidth=None, billing_id=None, connection=None, contract_end_time=None, contract_start_time=None, contract_status=None, contractid=None, deletedtimestamp=None, description=None, duration=None, latency=None, linkid=None, price=None, renewal_option=None, tag=None, type=None, version=None):  # noqa: E501
        """InlineResponse20012Params - a model defined in Swagger"""  # noqa: E501

        self._bandwidth = None
        self._billing_id = None
        self._connection = None
        self._contract_end_time = None
        self._contract_start_time = None
        self._contract_status = None
        self._contractid = None
        self._deletedtimestamp = None
        self._description = None
        self._duration = None
        self._latency = None
        self._linkid = None
        self._price = None
        self._renewal_option = None
        self._tag = None
        self._type = None
        self._version = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if billing_id is not None:
            self.billing_id = billing_id
        if connection is not None:
            self.connection = connection
        if contract_end_time is not None:
            self.contract_end_time = contract_end_time
        if contract_start_time is not None:
            self.contract_start_time = contract_start_time
        if contract_status is not None:
            self.contract_status = contract_status
        if contractid is not None:
            self.contractid = contractid
        if deletedtimestamp is not None:
            self.deletedtimestamp = deletedtimestamp
        if description is not None:
            self.description = description
        if duration is not None:
            self.duration = duration
        if latency is not None:
            self.latency = latency
        if linkid is not None:
            self.linkid = linkid
        if price is not None:
            self.price = price
        if renewal_option is not None:
            self.renewal_option = renewal_option
        if tag is not None:
            self.tag = tag
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def bandwidth(self):
        """Gets the bandwidth of this InlineResponse20012Params.  # noqa: E501


        :return: The bandwidth of this InlineResponse20012Params.  # noqa: E501
        :rtype: BandwidthKbs
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this InlineResponse20012Params.


        :param bandwidth: The bandwidth of this InlineResponse20012Params.  # noqa: E501
        :type: BandwidthKbs
        """

        self._bandwidth = bandwidth

    @property
    def billing_id(self):
        """Gets the billing_id of this InlineResponse20012Params.  # noqa: E501


        :return: The billing_id of this InlineResponse20012Params.  # noqa: E501
        :rtype: str
        """
        return self._billing_id

    @billing_id.setter
    def billing_id(self, billing_id):
        """Sets the billing_id of this InlineResponse20012Params.


        :param billing_id: The billing_id of this InlineResponse20012Params.  # noqa: E501
        :type: str
        """

        self._billing_id = billing_id

    @property
    def connection(self):
        """Gets the connection of this InlineResponse20012Params.  # noqa: E501


        :return: The connection of this InlineResponse20012Params.  # noqa: E501
        :rtype: Connections
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this InlineResponse20012Params.


        :param connection: The connection of this InlineResponse20012Params.  # noqa: E501
        :type: Connections
        """

        self._connection = connection

    @property
    def contract_end_time(self):
        """Gets the contract_end_time of this InlineResponse20012Params.  # noqa: E501


        :return: The contract_end_time of this InlineResponse20012Params.  # noqa: E501
        :rtype: ContractEndTime
        """
        return self._contract_end_time

    @contract_end_time.setter
    def contract_end_time(self, contract_end_time):
        """Sets the contract_end_time of this InlineResponse20012Params.


        :param contract_end_time: The contract_end_time of this InlineResponse20012Params.  # noqa: E501
        :type: ContractEndTime
        """

        self._contract_end_time = contract_end_time

    @property
    def contract_start_time(self):
        """Gets the contract_start_time of this InlineResponse20012Params.  # noqa: E501


        :return: The contract_start_time of this InlineResponse20012Params.  # noqa: E501
        :rtype: ContractStartTime
        """
        return self._contract_start_time

    @contract_start_time.setter
    def contract_start_time(self, contract_start_time):
        """Sets the contract_start_time of this InlineResponse20012Params.


        :param contract_start_time: The contract_start_time of this InlineResponse20012Params.  # noqa: E501
        :type: ContractStartTime
        """

        self._contract_start_time = contract_start_time

    @property
    def contract_status(self):
        """Gets the contract_status of this InlineResponse20012Params.  # noqa: E501


        :return: The contract_status of this InlineResponse20012Params.  # noqa: E501
        :rtype: ContractStatus
        """
        return self._contract_status

    @contract_status.setter
    def contract_status(self, contract_status):
        """Sets the contract_status of this InlineResponse20012Params.


        :param contract_status: The contract_status of this InlineResponse20012Params.  # noqa: E501
        :type: ContractStatus
        """

        self._contract_status = contract_status

    @property
    def contractid(self):
        """Gets the contractid of this InlineResponse20012Params.  # noqa: E501


        :return: The contractid of this InlineResponse20012Params.  # noqa: E501
        :rtype: Contractid
        """
        return self._contractid

    @contractid.setter
    def contractid(self, contractid):
        """Sets the contractid of this InlineResponse20012Params.


        :param contractid: The contractid of this InlineResponse20012Params.  # noqa: E501
        :type: Contractid
        """

        self._contractid = contractid

    @property
    def deletedtimestamp(self):
        """Gets the deletedtimestamp of this InlineResponse20012Params.  # noqa: E501


        :return: The deletedtimestamp of this InlineResponse20012Params.  # noqa: E501
        :rtype: Deletedtimestamp
        """
        return self._deletedtimestamp

    @deletedtimestamp.setter
    def deletedtimestamp(self, deletedtimestamp):
        """Sets the deletedtimestamp of this InlineResponse20012Params.


        :param deletedtimestamp: The deletedtimestamp of this InlineResponse20012Params.  # noqa: E501
        :type: Deletedtimestamp
        """

        self._deletedtimestamp = deletedtimestamp

    @property
    def description(self):
        """Gets the description of this InlineResponse20012Params.  # noqa: E501


        :return: The description of this InlineResponse20012Params.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse20012Params.


        :param description: The description of this InlineResponse20012Params.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def duration(self):
        """Gets the duration of this InlineResponse20012Params.  # noqa: E501


        :return: The duration of this InlineResponse20012Params.  # noqa: E501
        :rtype: DurationMins
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse20012Params.


        :param duration: The duration of this InlineResponse20012Params.  # noqa: E501
        :type: DurationMins
        """

        self._duration = duration

    @property
    def latency(self):
        """Gets the latency of this InlineResponse20012Params.  # noqa: E501


        :return: The latency of this InlineResponse20012Params.  # noqa: E501
        :rtype: Latency
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this InlineResponse20012Params.


        :param latency: The latency of this InlineResponse20012Params.  # noqa: E501
        :type: Latency
        """

        self._latency = latency

    @property
    def linkid(self):
        """Gets the linkid of this InlineResponse20012Params.  # noqa: E501


        :return: The linkid of this InlineResponse20012Params.  # noqa: E501
        :rtype: Linkid
        """
        return self._linkid

    @linkid.setter
    def linkid(self, linkid):
        """Sets the linkid of this InlineResponse20012Params.


        :param linkid: The linkid of this InlineResponse20012Params.  # noqa: E501
        :type: Linkid
        """

        self._linkid = linkid

    @property
    def price(self):
        """Gets the price of this InlineResponse20012Params.  # noqa: E501


        :return: The price of this InlineResponse20012Params.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InlineResponse20012Params.


        :param price: The price of this InlineResponse20012Params.  # noqa: E501
        :type: Price
        """

        self._price = price

    @property
    def renewal_option(self):
        """Gets the renewal_option of this InlineResponse20012Params.  # noqa: E501


        :return: The renewal_option of this InlineResponse20012Params.  # noqa: E501
        :rtype: RenewalOption
        """
        return self._renewal_option

    @renewal_option.setter
    def renewal_option(self, renewal_option):
        """Sets the renewal_option of this InlineResponse20012Params.


        :param renewal_option: The renewal_option of this InlineResponse20012Params.  # noqa: E501
        :type: RenewalOption
        """

        self._renewal_option = renewal_option

    @property
    def tag(self):
        """Gets the tag of this InlineResponse20012Params.  # noqa: E501


        :return: The tag of this InlineResponse20012Params.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this InlineResponse20012Params.


        :param tag: The tag of this InlineResponse20012Params.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def type(self):
        """Gets the type of this InlineResponse20012Params.  # noqa: E501


        :return: The type of this InlineResponse20012Params.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20012Params.


        :param type: The type of this InlineResponse20012Params.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this InlineResponse20012Params.  # noqa: E501


        :return: The version of this InlineResponse20012Params.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InlineResponse20012Params.


        :param version: The version of this InlineResponse20012Params.  # noqa: E501
        :type: Version
        """

        self._version = version

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
        if not isinstance(other, InlineResponse20012Params):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

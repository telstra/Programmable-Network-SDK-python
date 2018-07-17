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

from TelstraTPN.models.model100inventorylinksstatsflowlinkidstartdateenddate_tags import Model100inventorylinksstatsflowlinkidstartdateenddateTags  # noqa: F401,E501


class InlineResponse2009(object):
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
        'tags': 'Model100inventorylinksstatsflowlinkidstartdateenddateTags',
        'aggregate_tags': 'list[str]',
        'dps': 'dict(str, float)',
        'metric': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'aggregate_tags': 'aggregateTags',
        'dps': 'dps',
        'metric': 'metric'
    }

    def __init__(self, tags=None, aggregate_tags=None, dps=None, metric=None):  # noqa: E501
        """InlineResponse2009 - a model defined in Swagger"""  # noqa: E501

        self._tags = None
        self._aggregate_tags = None
        self._dps = None
        self._metric = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if aggregate_tags is not None:
            self.aggregate_tags = aggregate_tags
        if dps is not None:
            self.dps = dps
        if metric is not None:
            self.metric = metric

    @property
    def tags(self):
        """Gets the tags of this InlineResponse2009.  # noqa: E501


        :return: The tags of this InlineResponse2009.  # noqa: E501
        :rtype: Model100inventorylinksstatsflowlinkidstartdateenddateTags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InlineResponse2009.


        :param tags: The tags of this InlineResponse2009.  # noqa: E501
        :type: Model100inventorylinksstatsflowlinkidstartdateenddateTags
        """

        self._tags = tags

    @property
    def aggregate_tags(self):
        """Gets the aggregate_tags of this InlineResponse2009.  # noqa: E501


        :return: The aggregate_tags of this InlineResponse2009.  # noqa: E501
        :rtype: list[str]
        """
        return self._aggregate_tags

    @aggregate_tags.setter
    def aggregate_tags(self, aggregate_tags):
        """Sets the aggregate_tags of this InlineResponse2009.


        :param aggregate_tags: The aggregate_tags of this InlineResponse2009.  # noqa: E501
        :type: list[str]
        """

        self._aggregate_tags = aggregate_tags

    @property
    def dps(self):
        """Gets the dps of this InlineResponse2009.  # noqa: E501


        :return: The dps of this InlineResponse2009.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._dps

    @dps.setter
    def dps(self, dps):
        """Sets the dps of this InlineResponse2009.


        :param dps: The dps of this InlineResponse2009.  # noqa: E501
        :type: dict(str, float)
        """

        self._dps = dps

    @property
    def metric(self):
        """Gets the metric of this InlineResponse2009.  # noqa: E501


        :return: The metric of this InlineResponse2009.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this InlineResponse2009.


        :param metric: The metric of this InlineResponse2009.  # noqa: E501
        :type: str
        """

        self._metric = metric

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
        if not isinstance(other, InlineResponse2009):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

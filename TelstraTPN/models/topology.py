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


class Topology(object):
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
        'uuid': 'str',
        'name': 'str',
        'description': 'str',
        'status': 'str',
        'customer_uuid': 'str',
        'nsd_uuid': 'str',
        'guid_topology_id': 'str',
        'created_by': 'str',
        'creation_date': 'int',
        'deletion_date': 'int'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'customer_uuid': 'customer_uuid',
        'nsd_uuid': 'nsd_uuid',
        'guid_topology_id': 'guid_topology_id',
        'created_by': 'created_by',
        'creation_date': 'creation_date',
        'deletion_date': 'deletion_date'
    }

    def __init__(self, uuid=None, name=None, description=None, status=None, customer_uuid=None, nsd_uuid=None, guid_topology_id=None, created_by=None, creation_date=None, deletion_date=None):
        """
        Topology - a model defined in Swagger
        """

        self._uuid = None
        self._name = None
        self._description = None
        self._status = None
        self._customer_uuid = None
        self._nsd_uuid = None
        self._guid_topology_id = None
        self._created_by = None
        self._creation_date = None
        self._deletion_date = None

        if uuid is not None:
          self.uuid = uuid
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if status is not None:
          self.status = status
        if customer_uuid is not None:
          self.customer_uuid = customer_uuid
        if nsd_uuid is not None:
          self.nsd_uuid = nsd_uuid
        if guid_topology_id is not None:
          self.guid_topology_id = guid_topology_id
        if created_by is not None:
          self.created_by = created_by
        if creation_date is not None:
          self.creation_date = creation_date
        if deletion_date is not None:
          self.deletion_date = deletion_date

    @property
    def uuid(self):
        """
        Gets the uuid of this Topology.
        

        :return: The uuid of this Topology.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this Topology.
        

        :param uuid: The uuid of this Topology.
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """
        Gets the name of this Topology.
        

        :return: The name of this Topology.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Topology.
        

        :param name: The name of this Topology.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Topology.
        

        :return: The description of this Topology.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Topology.
        

        :param description: The description of this Topology.
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """
        Gets the status of this Topology.
        

        :return: The status of this Topology.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Topology.
        

        :param status: The status of this Topology.
        :type: str
        """

        self._status = status

    @property
    def customer_uuid(self):
        """
        Gets the customer_uuid of this Topology.
        

        :return: The customer_uuid of this Topology.
        :rtype: str
        """
        return self._customer_uuid

    @customer_uuid.setter
    def customer_uuid(self, customer_uuid):
        """
        Sets the customer_uuid of this Topology.
        

        :param customer_uuid: The customer_uuid of this Topology.
        :type: str
        """

        self._customer_uuid = customer_uuid

    @property
    def nsd_uuid(self):
        """
        Gets the nsd_uuid of this Topology.
        no longer used

        :return: The nsd_uuid of this Topology.
        :rtype: str
        """
        return self._nsd_uuid

    @nsd_uuid.setter
    def nsd_uuid(self, nsd_uuid):
        """
        Sets the nsd_uuid of this Topology.
        no longer used

        :param nsd_uuid: The nsd_uuid of this Topology.
        :type: str
        """

        self._nsd_uuid = nsd_uuid

    @property
    def guid_topology_id(self):
        """
        Gets the guid_topology_id of this Topology.
        

        :return: The guid_topology_id of this Topology.
        :rtype: str
        """
        return self._guid_topology_id

    @guid_topology_id.setter
    def guid_topology_id(self, guid_topology_id):
        """
        Sets the guid_topology_id of this Topology.
        

        :param guid_topology_id: The guid_topology_id of this Topology.
        :type: str
        """

        self._guid_topology_id = guid_topology_id

    @property
    def created_by(self):
        """
        Gets the created_by of this Topology.
        

        :return: The created_by of this Topology.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Topology.
        

        :param created_by: The created_by of this Topology.
        :type: str
        """

        self._created_by = created_by

    @property
    def creation_date(self):
        """
        Gets the creation_date of this Topology.
        

        :return: The creation_date of this Topology.
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this Topology.
        

        :param creation_date: The creation_date of this Topology.
        :type: int
        """

        self._creation_date = creation_date

    @property
    def deletion_date(self):
        """
        Gets the deletion_date of this Topology.
        

        :return: The deletion_date of this Topology.
        :rtype: int
        """
        return self._deletion_date

    @deletion_date.setter
    def deletion_date(self, deletion_date):
        """
        Sets the deletion_date of this Topology.
        

        :param deletion_date: The deletion_date of this Topology.
        :type: int
        """

        self._deletion_date = deletion_date

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
        if not isinstance(other, Topology):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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

from TelstraTPN.models.classification import Classification  # noqa: F401,E501
from TelstraTPN.models.flavor import Flavor  # noqa: F401,E501
from TelstraTPN.models.glance_image import GlanceImage  # noqa: F401,E501
from TelstraTPN.models.product import Product  # noqa: F401,E501
from TelstraTPN.models.vnf_tag import VnfTag  # noqa: F401,E501


class Image(object):
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
        'tags': 'list[VnfTag]',
        'brief_description': 'str',
        'buyers': 'str',
        'classifications': 'list[Classification]',
        'comments': 'str',
        'create_at': 'int',
        'creator': 'str',
        'description': 'str',
        'eos': 'str',
        'flavors': 'list[Flavor]',
        'flavors_price': 'str',
        'glance_comments': 'str',
        'glance_image': 'GlanceImage',
        'glance_name': 'str',
        'glance_properties': 'str',
        'id': 'int',
        'image_format': 'str',
        'license_required': 'bool',
        'logo': 'str',
        'max_ports': 'int',
        'md5': 'str',
        'min_ports': 'int',
        'name': 'str',
        'os_version': 'str',
        'owner': 'str',
        'product': 'Product',
        'publish_date': 'str',
        'restrict_vnc_console': 'bool',
        'status': 'str',
        'support_hot_plug': 'bool',
        'upload_at': 'int',
        'vendor_name': 'str',
        'zero_day_config_spec': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'brief_description': 'brief_description',
        'buyers': 'buyers',
        'classifications': 'classifications',
        'comments': 'comments',
        'create_at': 'create_at',
        'creator': 'creator',
        'description': 'description',
        'eos': 'eos',
        'flavors': 'flavors',
        'flavors_price': 'flavors_price',
        'glance_comments': 'glance_comments',
        'glance_image': 'glance_image',
        'glance_name': 'glance_name',
        'glance_properties': 'glance_properties',
        'id': 'id',
        'image_format': 'image_format',
        'license_required': 'license_required',
        'logo': 'logo',
        'max_ports': 'max_ports',
        'md5': 'md5',
        'min_ports': 'min_ports',
        'name': 'name',
        'os_version': 'os_version',
        'owner': 'owner',
        'product': 'product',
        'publish_date': 'publish_date',
        'restrict_vnc_console': 'restrict_vnc_console',
        'status': 'status',
        'support_hot_plug': 'support_hot_plug',
        'upload_at': 'upload_at',
        'vendor_name': 'vendor_name',
        'zero_day_config_spec': 'zero_day_config_spec'
    }

    def __init__(self, tags=None, brief_description=None, buyers=None, classifications=None, comments=None, create_at=None, creator=None, description=None, eos=None, flavors=None, flavors_price=None, glance_comments=None, glance_image=None, glance_name=None, glance_properties=None, id=None, image_format=None, license_required=None, logo=None, max_ports=None, md5=None, min_ports=None, name=None, os_version=None, owner=None, product=None, publish_date=None, restrict_vnc_console=None, status=None, support_hot_plug=None, upload_at=None, vendor_name=None, zero_day_config_spec=None):  # noqa: E501
        """Image - a model defined in Swagger"""  # noqa: E501

        self._tags = None
        self._brief_description = None
        self._buyers = None
        self._classifications = None
        self._comments = None
        self._create_at = None
        self._creator = None
        self._description = None
        self._eos = None
        self._flavors = None
        self._flavors_price = None
        self._glance_comments = None
        self._glance_image = None
        self._glance_name = None
        self._glance_properties = None
        self._id = None
        self._image_format = None
        self._license_required = None
        self._logo = None
        self._max_ports = None
        self._md5 = None
        self._min_ports = None
        self._name = None
        self._os_version = None
        self._owner = None
        self._product = None
        self._publish_date = None
        self._restrict_vnc_console = None
        self._status = None
        self._support_hot_plug = None
        self._upload_at = None
        self._vendor_name = None
        self._zero_day_config_spec = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if brief_description is not None:
            self.brief_description = brief_description
        if buyers is not None:
            self.buyers = buyers
        if classifications is not None:
            self.classifications = classifications
        if comments is not None:
            self.comments = comments
        if create_at is not None:
            self.create_at = create_at
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if eos is not None:
            self.eos = eos
        if flavors is not None:
            self.flavors = flavors
        if flavors_price is not None:
            self.flavors_price = flavors_price
        if glance_comments is not None:
            self.glance_comments = glance_comments
        if glance_image is not None:
            self.glance_image = glance_image
        if glance_name is not None:
            self.glance_name = glance_name
        if glance_properties is not None:
            self.glance_properties = glance_properties
        if id is not None:
            self.id = id
        if image_format is not None:
            self.image_format = image_format
        if license_required is not None:
            self.license_required = license_required
        if logo is not None:
            self.logo = logo
        if max_ports is not None:
            self.max_ports = max_ports
        if md5 is not None:
            self.md5 = md5
        if min_ports is not None:
            self.min_ports = min_ports
        if name is not None:
            self.name = name
        if os_version is not None:
            self.os_version = os_version
        if owner is not None:
            self.owner = owner
        if product is not None:
            self.product = product
        if publish_date is not None:
            self.publish_date = publish_date
        if restrict_vnc_console is not None:
            self.restrict_vnc_console = restrict_vnc_console
        if status is not None:
            self.status = status
        if support_hot_plug is not None:
            self.support_hot_plug = support_hot_plug
        if upload_at is not None:
            self.upload_at = upload_at
        if vendor_name is not None:
            self.vendor_name = vendor_name
        if zero_day_config_spec is not None:
            self.zero_day_config_spec = zero_day_config_spec

    @property
    def tags(self):
        """Gets the tags of this Image.  # noqa: E501

          # noqa: E501

        :return: The tags of this Image.  # noqa: E501
        :rtype: list[VnfTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Image.

          # noqa: E501

        :param tags: The tags of this Image.  # noqa: E501
        :type: list[VnfTag]
        """

        self._tags = tags

    @property
    def brief_description(self):
        """Gets the brief_description of this Image.  # noqa: E501

          # noqa: E501

        :return: The brief_description of this Image.  # noqa: E501
        :rtype: str
        """
        return self._brief_description

    @brief_description.setter
    def brief_description(self, brief_description):
        """Sets the brief_description of this Image.

          # noqa: E501

        :param brief_description: The brief_description of this Image.  # noqa: E501
        :type: str
        """

        self._brief_description = brief_description

    @property
    def buyers(self):
        """Gets the buyers of this Image.  # noqa: E501

          # noqa: E501

        :return: The buyers of this Image.  # noqa: E501
        :rtype: str
        """
        return self._buyers

    @buyers.setter
    def buyers(self, buyers):
        """Sets the buyers of this Image.

          # noqa: E501

        :param buyers: The buyers of this Image.  # noqa: E501
        :type: str
        """

        self._buyers = buyers

    @property
    def classifications(self):
        """Gets the classifications of this Image.  # noqa: E501

          # noqa: E501

        :return: The classifications of this Image.  # noqa: E501
        :rtype: list[Classification]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """Sets the classifications of this Image.

          # noqa: E501

        :param classifications: The classifications of this Image.  # noqa: E501
        :type: list[Classification]
        """

        self._classifications = classifications

    @property
    def comments(self):
        """Gets the comments of this Image.  # noqa: E501

          # noqa: E501

        :return: The comments of this Image.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Image.

          # noqa: E501

        :param comments: The comments of this Image.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def create_at(self):
        """Gets the create_at of this Image.  # noqa: E501

          # noqa: E501

        :return: The create_at of this Image.  # noqa: E501
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this Image.

          # noqa: E501

        :param create_at: The create_at of this Image.  # noqa: E501
        :type: int
        """

        self._create_at = create_at

    @property
    def creator(self):
        """Gets the creator of this Image.  # noqa: E501

          # noqa: E501

        :return: The creator of this Image.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Image.

          # noqa: E501

        :param creator: The creator of this Image.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def description(self):
        """Gets the description of this Image.  # noqa: E501

          # noqa: E501

        :return: The description of this Image.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Image.

          # noqa: E501

        :param description: The description of this Image.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def eos(self):
        """Gets the eos of this Image.  # noqa: E501

          # noqa: E501

        :return: The eos of this Image.  # noqa: E501
        :rtype: str
        """
        return self._eos

    @eos.setter
    def eos(self, eos):
        """Sets the eos of this Image.

          # noqa: E501

        :param eos: The eos of this Image.  # noqa: E501
        :type: str
        """

        self._eos = eos

    @property
    def flavors(self):
        """Gets the flavors of this Image.  # noqa: E501

          # noqa: E501

        :return: The flavors of this Image.  # noqa: E501
        :rtype: list[Flavor]
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        """Sets the flavors of this Image.

          # noqa: E501

        :param flavors: The flavors of this Image.  # noqa: E501
        :type: list[Flavor]
        """

        self._flavors = flavors

    @property
    def flavors_price(self):
        """Gets the flavors_price of this Image.  # noqa: E501

          # noqa: E501

        :return: The flavors_price of this Image.  # noqa: E501
        :rtype: str
        """
        return self._flavors_price

    @flavors_price.setter
    def flavors_price(self, flavors_price):
        """Sets the flavors_price of this Image.

          # noqa: E501

        :param flavors_price: The flavors_price of this Image.  # noqa: E501
        :type: str
        """

        self._flavors_price = flavors_price

    @property
    def glance_comments(self):
        """Gets the glance_comments of this Image.  # noqa: E501

          # noqa: E501

        :return: The glance_comments of this Image.  # noqa: E501
        :rtype: str
        """
        return self._glance_comments

    @glance_comments.setter
    def glance_comments(self, glance_comments):
        """Sets the glance_comments of this Image.

          # noqa: E501

        :param glance_comments: The glance_comments of this Image.  # noqa: E501
        :type: str
        """

        self._glance_comments = glance_comments

    @property
    def glance_image(self):
        """Gets the glance_image of this Image.  # noqa: E501


        :return: The glance_image of this Image.  # noqa: E501
        :rtype: GlanceImage
        """
        return self._glance_image

    @glance_image.setter
    def glance_image(self, glance_image):
        """Sets the glance_image of this Image.


        :param glance_image: The glance_image of this Image.  # noqa: E501
        :type: GlanceImage
        """

        self._glance_image = glance_image

    @property
    def glance_name(self):
        """Gets the glance_name of this Image.  # noqa: E501

          # noqa: E501

        :return: The glance_name of this Image.  # noqa: E501
        :rtype: str
        """
        return self._glance_name

    @glance_name.setter
    def glance_name(self, glance_name):
        """Sets the glance_name of this Image.

          # noqa: E501

        :param glance_name: The glance_name of this Image.  # noqa: E501
        :type: str
        """

        self._glance_name = glance_name

    @property
    def glance_properties(self):
        """Gets the glance_properties of this Image.  # noqa: E501

          # noqa: E501

        :return: The glance_properties of this Image.  # noqa: E501
        :rtype: str
        """
        return self._glance_properties

    @glance_properties.setter
    def glance_properties(self, glance_properties):
        """Sets the glance_properties of this Image.

          # noqa: E501

        :param glance_properties: The glance_properties of this Image.  # noqa: E501
        :type: str
        """

        self._glance_properties = glance_properties

    @property
    def id(self):
        """Gets the id of this Image.  # noqa: E501

          # noqa: E501

        :return: The id of this Image.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Image.

          # noqa: E501

        :param id: The id of this Image.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def image_format(self):
        """Gets the image_format of this Image.  # noqa: E501

          # noqa: E501

        :return: The image_format of this Image.  # noqa: E501
        :rtype: str
        """
        return self._image_format

    @image_format.setter
    def image_format(self, image_format):
        """Sets the image_format of this Image.

          # noqa: E501

        :param image_format: The image_format of this Image.  # noqa: E501
        :type: str
        """

        self._image_format = image_format

    @property
    def license_required(self):
        """Gets the license_required of this Image.  # noqa: E501

          # noqa: E501

        :return: The license_required of this Image.  # noqa: E501
        :rtype: bool
        """
        return self._license_required

    @license_required.setter
    def license_required(self, license_required):
        """Sets the license_required of this Image.

          # noqa: E501

        :param license_required: The license_required of this Image.  # noqa: E501
        :type: bool
        """

        self._license_required = license_required

    @property
    def logo(self):
        """Gets the logo of this Image.  # noqa: E501

          # noqa: E501

        :return: The logo of this Image.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Image.

          # noqa: E501

        :param logo: The logo of this Image.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def max_ports(self):
        """Gets the max_ports of this Image.  # noqa: E501

          # noqa: E501

        :return: The max_ports of this Image.  # noqa: E501
        :rtype: int
        """
        return self._max_ports

    @max_ports.setter
    def max_ports(self, max_ports):
        """Sets the max_ports of this Image.

          # noqa: E501

        :param max_ports: The max_ports of this Image.  # noqa: E501
        :type: int
        """

        self._max_ports = max_ports

    @property
    def md5(self):
        """Gets the md5 of this Image.  # noqa: E501

          # noqa: E501

        :return: The md5 of this Image.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this Image.

          # noqa: E501

        :param md5: The md5 of this Image.  # noqa: E501
        :type: str
        """

        self._md5 = md5

    @property
    def min_ports(self):
        """Gets the min_ports of this Image.  # noqa: E501

          # noqa: E501

        :return: The min_ports of this Image.  # noqa: E501
        :rtype: int
        """
        return self._min_ports

    @min_ports.setter
    def min_ports(self, min_ports):
        """Sets the min_ports of this Image.

          # noqa: E501

        :param min_ports: The min_ports of this Image.  # noqa: E501
        :type: int
        """

        self._min_ports = min_ports

    @property
    def name(self):
        """Gets the name of this Image.  # noqa: E501

          # noqa: E501

        :return: The name of this Image.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Image.

          # noqa: E501

        :param name: The name of this Image.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def os_version(self):
        """Gets the os_version of this Image.  # noqa: E501

          # noqa: E501

        :return: The os_version of this Image.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this Image.

          # noqa: E501

        :param os_version: The os_version of this Image.  # noqa: E501
        :type: str
        """

        self._os_version = os_version

    @property
    def owner(self):
        """Gets the owner of this Image.  # noqa: E501

          # noqa: E501

        :return: The owner of this Image.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Image.

          # noqa: E501

        :param owner: The owner of this Image.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def product(self):
        """Gets the product of this Image.  # noqa: E501


        :return: The product of this Image.  # noqa: E501
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this Image.


        :param product: The product of this Image.  # noqa: E501
        :type: Product
        """

        self._product = product

    @property
    def publish_date(self):
        """Gets the publish_date of this Image.  # noqa: E501

          # noqa: E501

        :return: The publish_date of this Image.  # noqa: E501
        :rtype: str
        """
        return self._publish_date

    @publish_date.setter
    def publish_date(self, publish_date):
        """Sets the publish_date of this Image.

          # noqa: E501

        :param publish_date: The publish_date of this Image.  # noqa: E501
        :type: str
        """

        self._publish_date = publish_date

    @property
    def restrict_vnc_console(self):
        """Gets the restrict_vnc_console of this Image.  # noqa: E501

          # noqa: E501

        :return: The restrict_vnc_console of this Image.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_vnc_console

    @restrict_vnc_console.setter
    def restrict_vnc_console(self, restrict_vnc_console):
        """Sets the restrict_vnc_console of this Image.

          # noqa: E501

        :param restrict_vnc_console: The restrict_vnc_console of this Image.  # noqa: E501
        :type: bool
        """

        self._restrict_vnc_console = restrict_vnc_console

    @property
    def status(self):
        """Gets the status of this Image.  # noqa: E501

          # noqa: E501

        :return: The status of this Image.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Image.

          # noqa: E501

        :param status: The status of this Image.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def support_hot_plug(self):
        """Gets the support_hot_plug of this Image.  # noqa: E501

          # noqa: E501

        :return: The support_hot_plug of this Image.  # noqa: E501
        :rtype: bool
        """
        return self._support_hot_plug

    @support_hot_plug.setter
    def support_hot_plug(self, support_hot_plug):
        """Sets the support_hot_plug of this Image.

          # noqa: E501

        :param support_hot_plug: The support_hot_plug of this Image.  # noqa: E501
        :type: bool
        """

        self._support_hot_plug = support_hot_plug

    @property
    def upload_at(self):
        """Gets the upload_at of this Image.  # noqa: E501

          # noqa: E501

        :return: The upload_at of this Image.  # noqa: E501
        :rtype: int
        """
        return self._upload_at

    @upload_at.setter
    def upload_at(self, upload_at):
        """Sets the upload_at of this Image.

          # noqa: E501

        :param upload_at: The upload_at of this Image.  # noqa: E501
        :type: int
        """

        self._upload_at = upload_at

    @property
    def vendor_name(self):
        """Gets the vendor_name of this Image.  # noqa: E501

          # noqa: E501

        :return: The vendor_name of this Image.  # noqa: E501
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """Sets the vendor_name of this Image.

          # noqa: E501

        :param vendor_name: The vendor_name of this Image.  # noqa: E501
        :type: str
        """

        self._vendor_name = vendor_name

    @property
    def zero_day_config_spec(self):
        """Gets the zero_day_config_spec of this Image.  # noqa: E501

          # noqa: E501

        :return: The zero_day_config_spec of this Image.  # noqa: E501
        :rtype: str
        """
        return self._zero_day_config_spec

    @zero_day_config_spec.setter
    def zero_day_config_spec(self, zero_day_config_spec):
        """Sets the zero_day_config_spec of this Image.

          # noqa: E501

        :param zero_day_config_spec: The zero_day_config_spec of this Image.  # noqa: E501
        :type: str
        """

        self._zero_day_config_spec = zero_day_config_spec

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
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

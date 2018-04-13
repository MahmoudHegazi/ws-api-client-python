# coding: utf-8

"""
    Wheel Fitment API

    The Wheel Fitment API allows for programmatic access to the database of www.wheel-size.com and its services. Use this API to retrieve information about vehicle fitment database for rims and tires, including OE and option fitments, and plus/minus sizing fitment information. A variety of country and language specific options are available. The coverage of fitment data for vehicles manufactured since 2000 is nearly 100%.  The information about fitment data is updated on a daily basis.  # noqa: E501

    OpenAPI spec version: v1
    Contact: info@wheel-size.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MakeModel(object):
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
        'slug': 'str',
        'name': 'str',
        'name_en': 'str'
    }

    attribute_map = {
        'slug': 'slug',
        'name': 'name',
        'name_en': 'name_en'
    }

    def __init__(self, slug=None, name=None, name_en=None):  # noqa: E501
        """MakeModel - a model defined in Swagger"""  # noqa: E501

        self._slug = None
        self._name = None
        self._name_en = None
        self.discriminator = None

        self.slug = slug
        self.name = name
        self.name_en = name_en

    @property
    def slug(self):
        """Gets the slug of this MakeModel.  # noqa: E501

        Manufacturer slug name (e.g. `mitsubishi`)  # noqa: E501

        :return: The slug of this MakeModel.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this MakeModel.

        Manufacturer slug name (e.g. `mitsubishi`)  # noqa: E501

        :param slug: The slug of this MakeModel.  # noqa: E501
        :type: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501
        if slug is not None and not re.search('^[-a-zA-Z0-9_]+$', slug):  # noqa: E501
            raise ValueError("Invalid value for `slug`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")  # noqa: E501

        self._slug = slug

    @property
    def name(self):
        """Gets the name of this MakeModel.  # noqa: E501

        Manufacturer name (e.g. `Mitsubishi`)  # noqa: E501

        :return: The name of this MakeModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MakeModel.

        Manufacturer name (e.g. `Mitsubishi`)  # noqa: E501

        :param name: The name of this MakeModel.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def name_en(self):
        """Gets the name_en of this MakeModel.  # noqa: E501

         Original english name. Use it along with _**`lang`**_ query parameter    # noqa: E501

        :return: The name_en of this MakeModel.  # noqa: E501
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this MakeModel.

         Original english name. Use it along with _**`lang`**_ query parameter    # noqa: E501

        :param name_en: The name_en of this MakeModel.  # noqa: E501
        :type: str
        """
        if name_en is None:
            raise ValueError("Invalid value for `name_en`, must not be `None`")  # noqa: E501

        self._name_en = name_en

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
        if not isinstance(other, MakeModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

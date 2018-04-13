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


class Pressure(object):
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
        'bar': 'float',
        'psi': 'float',
        'k_pa': 'float'
    }

    attribute_map = {
        'bar': 'bar',
        'psi': 'psi',
        'k_pa': 'kPa'
    }

    def __init__(self, bar=None, psi=None, k_pa=None):  # noqa: E501
        """Pressure - a model defined in Swagger"""  # noqa: E501

        self._bar = None
        self._psi = None
        self._k_pa = None
        self.discriminator = None

        self.bar = bar
        self.psi = psi
        self.k_pa = k_pa

    @property
    def bar(self):
        """Gets the bar of this Pressure.  # noqa: E501

        Pressure, bar (e.g. `2.4`)  # noqa: E501

        :return: The bar of this Pressure.  # noqa: E501
        :rtype: float
        """
        return self._bar

    @bar.setter
    def bar(self, bar):
        """Sets the bar of this Pressure.

        Pressure, bar (e.g. `2.4`)  # noqa: E501

        :param bar: The bar of this Pressure.  # noqa: E501
        :type: float
        """
        if bar is None:
            raise ValueError("Invalid value for `bar`, must not be `None`")  # noqa: E501

        self._bar = bar

    @property
    def psi(self):
        """Gets the psi of this Pressure.  # noqa: E501

        Pressure, psi (e.g. `35`)  # noqa: E501

        :return: The psi of this Pressure.  # noqa: E501
        :rtype: float
        """
        return self._psi

    @psi.setter
    def psi(self, psi):
        """Sets the psi of this Pressure.

        Pressure, psi (e.g. `35`)  # noqa: E501

        :param psi: The psi of this Pressure.  # noqa: E501
        :type: float
        """
        if psi is None:
            raise ValueError("Invalid value for `psi`, must not be `None`")  # noqa: E501

        self._psi = psi

    @property
    def k_pa(self):
        """Gets the k_pa of this Pressure.  # noqa: E501

        Pressure, kPa (e.g. `240`)  # noqa: E501

        :return: The k_pa of this Pressure.  # noqa: E501
        :rtype: float
        """
        return self._k_pa

    @k_pa.setter
    def k_pa(self, k_pa):
        """Sets the k_pa of this Pressure.

        Pressure, kPa (e.g. `240`)  # noqa: E501

        :param k_pa: The k_pa of this Pressure.  # noqa: E501
        :type: float
        """
        if k_pa is None:
            raise ValueError("Invalid value for `k_pa`, must not be `None`")  # noqa: E501

        self._k_pa = k_pa

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
        if not isinstance(other, Pressure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

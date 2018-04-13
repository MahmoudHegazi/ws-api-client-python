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

from swagger_client.models.market import Market  # noqa: F401,E501


class TrimWithMarketAndYears(object):
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
        'trim': 'str',
        'market': 'Market',
        'years': 'list[int]'
    }

    attribute_map = {
        'trim': 'trim',
        'market': 'market',
        'years': 'years'
    }

    def __init__(self, trim=None, market=None, years=None):  # noqa: E501
        """TrimWithMarketAndYears - a model defined in Swagger"""  # noqa: E501

        self._trim = None
        self._market = None
        self._years = None
        self.discriminator = None

        self.trim = trim
        self.market = market
        self.years = years

    @property
    def trim(self):
        """Gets the trim of this TrimWithMarketAndYears.  # noqa: E501

        Trim name (e.g. `2.0`, can be __*`null`*__)  # noqa: E501

        :return: The trim of this TrimWithMarketAndYears.  # noqa: E501
        :rtype: str
        """
        return self._trim

    @trim.setter
    def trim(self, trim):
        """Sets the trim of this TrimWithMarketAndYears.

        Trim name (e.g. `2.0`, can be __*`null`*__)  # noqa: E501

        :param trim: The trim of this TrimWithMarketAndYears.  # noqa: E501
        :type: str
        """
        if trim is None:
            raise ValueError("Invalid value for `trim`, must not be `None`")  # noqa: E501

        self._trim = trim

    @property
    def market(self):
        """Gets the market of this TrimWithMarketAndYears.  # noqa: E501


        :return: The market of this TrimWithMarketAndYears.  # noqa: E501
        :rtype: Market
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this TrimWithMarketAndYears.


        :param market: The market of this TrimWithMarketAndYears.  # noqa: E501
        :type: Market
        """
        if market is None:
            raise ValueError("Invalid value for `market`, must not be `None`")  # noqa: E501

        self._market = market

    @property
    def years(self):
        """Gets the years of this TrimWithMarketAndYears.  # noqa: E501

        Production years for these trim and market  # noqa: E501

        :return: The years of this TrimWithMarketAndYears.  # noqa: E501
        :rtype: list[int]
        """
        return self._years

    @years.setter
    def years(self, years):
        """Sets the years of this TrimWithMarketAndYears.

        Production years for these trim and market  # noqa: E501

        :param years: The years of this TrimWithMarketAndYears.  # noqa: E501
        :type: list[int]
        """
        if years is None:
            raise ValueError("Invalid value for `years`, must not be `None`")  # noqa: E501

        self._years = years

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
        if not isinstance(other, TrimWithMarketAndYears):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

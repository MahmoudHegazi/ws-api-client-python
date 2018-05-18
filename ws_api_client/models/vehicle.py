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

from ws_api_client.models.generation import Generation  # noqa: F401,E501
from ws_api_client.models.market import Market  # noqa: F401,E501
from ws_api_client.models.power import Power  # noqa: F401,E501
from ws_api_client.models.wheel_pair import WheelPair  # noqa: F401,E501


class Vehicle(object):
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
        'market': 'Market',
        'generation': 'Generation',
        'lock_type': 'str',
        'bolt_pattern': 'str',
        'power': 'Power',
        'wheels': 'list[WheelPair]'
    }

    attribute_map = {
        'market': 'market',
        'generation': 'generation',
        'lock_type': 'lock_type',
        'bolt_pattern': 'bolt_pattern',
        'power': 'power',
        'wheels': 'wheels'
    }

    def __init__(self, market=None, generation=None, lock_type=None, bolt_pattern=None, power=None, wheels=None):  # noqa: E501
        """Vehicle - a model defined in Swagger"""  # noqa: E501

        self._market = None
        self._generation = None
        self._lock_type = None
        self._bolt_pattern = None
        self._power = None
        self._wheels = None
        self.discriminator = None

        self.market = market
        self.generation = generation
        if lock_type is not None:
            self.lock_type = lock_type
        self.bolt_pattern = bolt_pattern
        if power is not None:
            self.power = power
        if wheels is not None:
            self.wheels = wheels

    @property
    def market(self):
        """Gets the market of this Vehicle.  # noqa: E501


        :return: The market of this Vehicle.  # noqa: E501
        :rtype: Market
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this Vehicle.


        :param market: The market of this Vehicle.  # noqa: E501
        :type: Market
        """
        if market is None:
            raise ValueError("Invalid value for `market`, must not be `None`")  # noqa: E501

        self._market = market

    @property
    def generation(self):
        """Gets the generation of this Vehicle.  # noqa: E501


        :return: The generation of this Vehicle.  # noqa: E501
        :rtype: Generation
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this Vehicle.


        :param generation: The generation of this Vehicle.  # noqa: E501
        :type: Generation
        """
        if generation is None:
            raise ValueError("Invalid value for `generation`, must not be `None`")  # noqa: E501

        self._generation = generation

    @property
    def lock_type(self):
        """Gets the lock_type of this Vehicle.  # noqa: E501


        :return: The lock_type of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._lock_type

    @lock_type.setter
    def lock_type(self, lock_type):
        """Sets the lock_type of this Vehicle.


        :param lock_type: The lock_type of this Vehicle.  # noqa: E501
        :type: str
        """
        allowed_values = ["nut", "bolt"]  # noqa: E501
        if lock_type not in allowed_values:
            raise ValueError(
                "Invalid value for `lock_type` ({0}), must be one of {1}"  # noqa: E501
                .format(lock_type, allowed_values)
            )

        self._lock_type = lock_type

    @property
    def bolt_pattern(self):
        """Gets the bolt_pattern of this Vehicle.  # noqa: E501

        Bolt pattern (e.g. `5x105`, can be __*`N/A`*__)  # noqa: E501

        :return: The bolt_pattern of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._bolt_pattern

    @bolt_pattern.setter
    def bolt_pattern(self, bolt_pattern):
        """Sets the bolt_pattern of this Vehicle.

        Bolt pattern (e.g. `5x105`, can be __*`N/A`*__)  # noqa: E501

        :param bolt_pattern: The bolt_pattern of this Vehicle.  # noqa: E501
        :type: str
        """
        if bolt_pattern is None:
            raise ValueError("Invalid value for `bolt_pattern`, must not be `None`")  # noqa: E501

        self._bolt_pattern = bolt_pattern

    @property
    def power(self):
        """Gets the power of this Vehicle.  # noqa: E501


        :return: The power of this Vehicle.  # noqa: E501
        :rtype: Power
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this Vehicle.


        :param power: The power of this Vehicle.  # noqa: E501
        :type: Power
        """

        self._power = power

    @property
    def wheels(self):
        """Gets the wheels of this Vehicle.  # noqa: E501


        :return: The wheels of this Vehicle.  # noqa: E501
        :rtype: list[WheelPair]
        """
        return self._wheels

    @wheels.setter
    def wheels(self, wheels):
        """Sets the wheels of this Vehicle.


        :param wheels: The wheels of this Vehicle.  # noqa: E501
        :type: list[WheelPair]
        """

        self._wheels = wheels

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
        if not isinstance(other, Vehicle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

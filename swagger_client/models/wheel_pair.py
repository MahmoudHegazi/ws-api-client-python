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

from swagger_client.models.wheel import Wheel  # noqa: F401,E501


class WheelPair(object):
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
        'showing_fp_only': 'bool',
        'is_stock': 'bool',
        'front': 'Wheel',
        'rear': 'Wheel'
    }

    attribute_map = {
        'showing_fp_only': 'showing_fp_only',
        'is_stock': 'is_stock',
        'front': 'front',
        'rear': 'rear'
    }

    def __init__(self, showing_fp_only=None, is_stock=None, front=None, rear=None):  # noqa: E501
        """WheelPair - a model defined in Swagger"""  # noqa: E501

        self._showing_fp_only = None
        self._is_stock = None
        self._front = None
        self._rear = None
        self.discriminator = None

        self.showing_fp_only = showing_fp_only
        self.is_stock = is_stock
        self.front = front
        self.rear = rear

    @property
    def showing_fp_only(self):
        """Gets the showing_fp_only of this WheelPair.  # noqa: E501

        Show front pair only  # noqa: E501

        :return: The showing_fp_only of this WheelPair.  # noqa: E501
        :rtype: bool
        """
        return self._showing_fp_only

    @showing_fp_only.setter
    def showing_fp_only(self, showing_fp_only):
        """Sets the showing_fp_only of this WheelPair.

        Show front pair only  # noqa: E501

        :param showing_fp_only: The showing_fp_only of this WheelPair.  # noqa: E501
        :type: bool
        """
        if showing_fp_only is None:
            raise ValueError("Invalid value for `showing_fp_only`, must not be `None`")  # noqa: E501

        self._showing_fp_only = showing_fp_only

    @property
    def is_stock(self):
        """Gets the is_stock of this WheelPair.  # noqa: E501

        Original Equipment (OE)  # noqa: E501

        :return: The is_stock of this WheelPair.  # noqa: E501
        :rtype: bool
        """
        return self._is_stock

    @is_stock.setter
    def is_stock(self, is_stock):
        """Sets the is_stock of this WheelPair.

        Original Equipment (OE)  # noqa: E501

        :param is_stock: The is_stock of this WheelPair.  # noqa: E501
        :type: bool
        """
        if is_stock is None:
            raise ValueError("Invalid value for `is_stock`, must not be `None`")  # noqa: E501

        self._is_stock = is_stock

    @property
    def front(self):
        """Gets the front of this WheelPair.  # noqa: E501


        :return: The front of this WheelPair.  # noqa: E501
        :rtype: Wheel
        """
        return self._front

    @front.setter
    def front(self, front):
        """Sets the front of this WheelPair.


        :param front: The front of this WheelPair.  # noqa: E501
        :type: Wheel
        """
        if front is None:
            raise ValueError("Invalid value for `front`, must not be `None`")  # noqa: E501

        self._front = front

    @property
    def rear(self):
        """Gets the rear of this WheelPair.  # noqa: E501


        :return: The rear of this WheelPair.  # noqa: E501
        :rtype: Wheel
        """
        return self._rear

    @rear.setter
    def rear(self, rear):
        """Sets the rear of this WheelPair.


        :param rear: The rear of this WheelPair.  # noqa: E501
        :type: Wheel
        """
        if rear is None:
            raise ValueError("Invalid value for `rear`, must not be `None`")  # noqa: E501

        self._rear = rear

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
        if not isinstance(other, WheelPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

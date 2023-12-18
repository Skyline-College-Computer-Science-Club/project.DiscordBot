# coding: utf-8

"""
    SMCCD Schedule API

    This is SMCCD Schedule API documentation. The API requires basic authentication username and password pair to access the data.  # noqa: E501

    OpenAPI spec version: v1
    Contact: webmaster@smccd.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SectionLocation(object):
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
        'building': 'str',
        'room': 'str',
        'location': 'str',
        'college_code': 'int',
        'college_description': 'str',
        'offsite_indicator': 'str',
        'offsite_address': 'str'
    }

    attribute_map = {
        'building': 'building',
        'room': 'room',
        'location': 'location',
        'college_code': 'college_code',
        'college_description': 'college_description',
        'offsite_indicator': 'offsite_indicator',
        'offsite_address': 'offsite_address'
    }

    def __init__(self, building=None, room=None, location=None, college_code=None, college_description=None, offsite_indicator=None, offsite_address=None):  # noqa: E501
        """SectionLocation - a model defined in Swagger"""  # noqa: E501
        self._building = None
        self._room = None
        self._location = None
        self._college_code = None
        self._college_description = None
        self._offsite_indicator = None
        self._offsite_address = None
        self.discriminator = None
        if building is not None:
            self.building = building
        if room is not None:
            self.room = room
        if location is not None:
            self.location = location
        if college_code is not None:
            self.college_code = college_code
        if college_description is not None:
            self.college_description = college_description
        if offsite_indicator is not None:
            self.offsite_indicator = offsite_indicator
        if offsite_address is not None:
            self.offsite_address = offsite_address

    @property
    def building(self):
        """Gets the building of this SectionLocation.  # noqa: E501


        :return: The building of this SectionLocation.  # noqa: E501
        :rtype: str
        """
        return self._building

    @building.setter
    def building(self, building):
        """Sets the building of this SectionLocation.


        :param building: The building of this SectionLocation.  # noqa: E501
        :type: str
        """

        self._building = building

    @property
    def room(self):
        """Gets the room of this SectionLocation.  # noqa: E501


        :return: The room of this SectionLocation.  # noqa: E501
        :rtype: str
        """
        return self._room

    @room.setter
    def room(self, room):
        """Sets the room of this SectionLocation.


        :param room: The room of this SectionLocation.  # noqa: E501
        :type: str
        """

        self._room = room

    @property
    def location(self):
        """Gets the location of this SectionLocation.  # noqa: E501


        :return: The location of this SectionLocation.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SectionLocation.


        :param location: The location of this SectionLocation.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def college_code(self):
        """Gets the college_code of this SectionLocation.  # noqa: E501


        :return: The college_code of this SectionLocation.  # noqa: E501
        :rtype: int
        """
        return self._college_code

    @college_code.setter
    def college_code(self, college_code):
        """Sets the college_code of this SectionLocation.


        :param college_code: The college_code of this SectionLocation.  # noqa: E501
        :type: int
        """

        self._college_code = college_code

    @property
    def college_description(self):
        """Gets the college_description of this SectionLocation.  # noqa: E501


        :return: The college_description of this SectionLocation.  # noqa: E501
        :rtype: str
        """
        return self._college_description

    @college_description.setter
    def college_description(self, college_description):
        """Sets the college_description of this SectionLocation.


        :param college_description: The college_description of this SectionLocation.  # noqa: E501
        :type: str
        """

        self._college_description = college_description

    @property
    def offsite_indicator(self):
        """Gets the offsite_indicator of this SectionLocation.  # noqa: E501


        :return: The offsite_indicator of this SectionLocation.  # noqa: E501
        :rtype: str
        """
        return self._offsite_indicator

    @offsite_indicator.setter
    def offsite_indicator(self, offsite_indicator):
        """Sets the offsite_indicator of this SectionLocation.


        :param offsite_indicator: The offsite_indicator of this SectionLocation.  # noqa: E501
        :type: str
        """

        self._offsite_indicator = offsite_indicator

    @property
    def offsite_address(self):
        """Gets the offsite_address of this SectionLocation.  # noqa: E501


        :return: The offsite_address of this SectionLocation.  # noqa: E501
        :rtype: str
        """
        return self._offsite_address

    @offsite_address.setter
    def offsite_address(self, offsite_address):
        """Sets the offsite_address of this SectionLocation.


        :param offsite_address: The offsite_address of this SectionLocation.  # noqa: E501
        :type: str
        """

        self._offsite_address = offsite_address

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
        if issubclass(SectionLocation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SectionLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
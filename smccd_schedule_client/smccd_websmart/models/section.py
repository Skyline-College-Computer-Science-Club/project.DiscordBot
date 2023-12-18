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

class Section(object):
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
        'section_sequence': 'str',
        'schedule_description': 'str',
        'default_sort_order': 'int',
        'location': 'SectionLocation',
        'days': 'SectionDays',
        'dates': 'SectionDates',
        'time': 'SectionTime',
        'instructor': 'SectionInstructor'
    }

    attribute_map = {
        'section_sequence': 'section_sequence',
        'schedule_description': 'schedule_description',
        'default_sort_order': 'default_sort_order',
        'location': 'location',
        'days': 'days',
        'dates': 'dates',
        'time': 'time',
        'instructor': 'instructor'
    }

    def __init__(self, section_sequence=None, schedule_description=None, default_sort_order=None, location=None, days=None, dates=None, time=None, instructor=None):  # noqa: E501
        """Section - a model defined in Swagger"""  # noqa: E501
        self._section_sequence = None
        self._schedule_description = None
        self._default_sort_order = None
        self._location = None
        self._days = None
        self._dates = None
        self._time = None
        self._instructor = None
        self.discriminator = None
        if section_sequence is not None:
            self.section_sequence = section_sequence
        if schedule_description is not None:
            self.schedule_description = schedule_description
        if default_sort_order is not None:
            self.default_sort_order = default_sort_order
        if location is not None:
            self.location = location
        if days is not None:
            self.days = days
        if dates is not None:
            self.dates = dates
        if time is not None:
            self.time = time
        if instructor is not None:
            self.instructor = instructor

    @property
    def section_sequence(self):
        """Gets the section_sequence of this Section.  # noqa: E501

        Section sequence.  # noqa: E501

        :return: The section_sequence of this Section.  # noqa: E501
        :rtype: str
        """
        return self._section_sequence

    @section_sequence.setter
    def section_sequence(self, section_sequence):
        """Sets the section_sequence of this Section.

        Section sequence.  # noqa: E501

        :param section_sequence: The section_sequence of this Section.  # noqa: E501
        :type: str
        """

        self._section_sequence = section_sequence

    @property
    def schedule_description(self):
        """Gets the schedule_description of this Section.  # noqa: E501

        Description of the schedule section.  # noqa: E501

        :return: The schedule_description of this Section.  # noqa: E501
        :rtype: str
        """
        return self._schedule_description

    @schedule_description.setter
    def schedule_description(self, schedule_description):
        """Sets the schedule_description of this Section.

        Description of the schedule section.  # noqa: E501

        :param schedule_description: The schedule_description of this Section.  # noqa: E501
        :type: str
        """

        self._schedule_description = schedule_description

    @property
    def default_sort_order(self):
        """Gets the default_sort_order of this Section.  # noqa: E501

        Default prefer sort order of the course.  # noqa: E501

        :return: The default_sort_order of this Section.  # noqa: E501
        :rtype: int
        """
        return self._default_sort_order

    @default_sort_order.setter
    def default_sort_order(self, default_sort_order):
        """Sets the default_sort_order of this Section.

        Default prefer sort order of the course.  # noqa: E501

        :param default_sort_order: The default_sort_order of this Section.  # noqa: E501
        :type: int
        """

        self._default_sort_order = default_sort_order

    @property
    def location(self):
        """Gets the location of this Section.  # noqa: E501


        :return: The location of this Section.  # noqa: E501
        :rtype: SectionLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Section.


        :param location: The location of this Section.  # noqa: E501
        :type: SectionLocation
        """

        self._location = location

    @property
    def days(self):
        """Gets the days of this Section.  # noqa: E501


        :return: The days of this Section.  # noqa: E501
        :rtype: SectionDays
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this Section.


        :param days: The days of this Section.  # noqa: E501
        :type: SectionDays
        """

        self._days = days

    @property
    def dates(self):
        """Gets the dates of this Section.  # noqa: E501


        :return: The dates of this Section.  # noqa: E501
        :rtype: SectionDates
        """
        return self._dates

    @dates.setter
    def dates(self, dates):
        """Sets the dates of this Section.


        :param dates: The dates of this Section.  # noqa: E501
        :type: SectionDates
        """

        self._dates = dates

    @property
    def time(self):
        """Gets the time of this Section.  # noqa: E501


        :return: The time of this Section.  # noqa: E501
        :rtype: SectionTime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Section.


        :param time: The time of this Section.  # noqa: E501
        :type: SectionTime
        """

        self._time = time

    @property
    def instructor(self):
        """Gets the instructor of this Section.  # noqa: E501


        :return: The instructor of this Section.  # noqa: E501
        :rtype: SectionInstructor
        """
        return self._instructor

    @instructor.setter
    def instructor(self, instructor):
        """Sets the instructor of this Section.


        :param instructor: The instructor of this Section.  # noqa: E501
        :type: SectionInstructor
        """

        self._instructor = instructor

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
        if issubclass(Section, dict):
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
        if not isinstance(other, Section):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
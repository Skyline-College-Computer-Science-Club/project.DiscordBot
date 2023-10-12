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

class CourseNotices(object):
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
        'coreq': 'str',
        'cohort': 'str',
        'section_text': 'str',
        'dept_text': 'str'
    }

    attribute_map = {
        'coreq': 'coreq',
        'cohort': 'cohort',
        'section_text': 'section_text',
        'dept_text': 'dept_text'
    }

    def __init__(self, coreq=None, cohort=None, section_text=None, dept_text=None):  # noqa: E501
        """CourseNotices - a model defined in Swagger"""  # noqa: E501
        self._coreq = None
        self._cohort = None
        self._section_text = None
        self._dept_text = None
        self.discriminator = None
        if coreq is not None:
            self.coreq = coreq
        if cohort is not None:
            self.cohort = cohort
        if section_text is not None:
            self.section_text = section_text
        if dept_text is not None:
            self.dept_text = dept_text

    @property
    def coreq(self):
        """Gets the coreq of this CourseNotices.  # noqa: E501

        Corequisite course information text if the course has corequisites.  # noqa: E501

        :return: The coreq of this CourseNotices.  # noqa: E501
        :rtype: str
        """
        return self._coreq

    @coreq.setter
    def coreq(self, coreq):
        """Sets the coreq of this CourseNotices.

        Corequisite course information text if the course has corequisites.  # noqa: E501

        :param coreq: The coreq of this CourseNotices.  # noqa: E501
        :type: str
        """

        self._coreq = coreq

    @property
    def cohort(self):
        """Gets the cohort of this CourseNotices.  # noqa: E501

        Corequisite course information text if the course has special cohort requirements  # noqa: E501

        :return: The cohort of this CourseNotices.  # noqa: E501
        :rtype: str
        """
        return self._cohort

    @cohort.setter
    def cohort(self, cohort):
        """Sets the cohort of this CourseNotices.

        Corequisite course information text if the course has special cohort requirements  # noqa: E501

        :param cohort: The cohort of this CourseNotices.  # noqa: E501
        :type: str
        """

        self._cohort = cohort

    @property
    def section_text(self):
        """Gets the section_text of this CourseNotices.  # noqa: E501

        Section information text for the course.  # noqa: E501

        :return: The section_text of this CourseNotices.  # noqa: E501
        :rtype: str
        """
        return self._section_text

    @section_text.setter
    def section_text(self, section_text):
        """Sets the section_text of this CourseNotices.

        Section information text for the course.  # noqa: E501

        :param section_text: The section_text of this CourseNotices.  # noqa: E501
        :type: str
        """

        self._section_text = section_text

    @property
    def dept_text(self):
        """Gets the dept_text of this CourseNotices.  # noqa: E501

        Department information text for the course.  # noqa: E501

        :return: The dept_text of this CourseNotices.  # noqa: E501
        :rtype: str
        """
        return self._dept_text

    @dept_text.setter
    def dept_text(self, dept_text):
        """Sets the dept_text of this CourseNotices.

        Department information text for the course.  # noqa: E501

        :param dept_text: The dept_text of this CourseNotices.  # noqa: E501
        :type: str
        """

        self._dept_text = dept_text

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
        if issubclass(CourseNotices, dict):
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
        if not isinstance(other, CourseNotices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from plugin.models.base_model import Model
from plugin.models.vm_clarity_data import VMClarityData
from plugin import util

from plugin.models.vm_clarity_data import VMClarityData  # noqa: E501

class Result(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, annotations=None, vmclarity=None):  # noqa: E501
        """Result - a model defined in OpenAPI

        :param annotations: The annotations of this Result.  # noqa: E501
        :type annotations: Dict[str, str]
        :param vmclarity: The vmclarity of this Result.  # noqa: E501
        :type vmclarity: VMClarityData
        """
        self.openapi_types = {
            'annotations': Dict[str, str],
            'vmclarity': VMClarityData
        }

        self.attribute_map = {
            'annotations': 'annotations',
            'vmclarity': 'vmclarity'
        }

        self._annotations = annotations
        self._vmclarity = vmclarity

    @classmethod
    def from_dict(cls, dikt) -> 'Result':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Result of this Result.  # noqa: E501
        :rtype: Result
        """
        return util.deserialize_model(dikt, cls)

    @property
    def annotations(self) -> Dict[str, str]:
        """Gets the annotations of this Result.

        Generic map of string keys and string values to attach arbitrary non-identifying metadata to objects.  # noqa: E501

        :return: The annotations of this Result.
        :rtype: Dict[str, str]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations: Dict[str, str]):
        """Sets the annotations of this Result.

        Generic map of string keys and string values to attach arbitrary non-identifying metadata to objects.  # noqa: E501

        :param annotations: The annotations of this Result.
        :type annotations: Dict[str, str]
        """

        self._annotations = annotations

    @property
    def vmclarity(self) -> VMClarityData:
        """Gets the vmclarity of this Result.


        :return: The vmclarity of this Result.
        :rtype: VMClarityData
        """
        return self._vmclarity

    @vmclarity.setter
    def vmclarity(self, vmclarity: VMClarityData):
        """Sets the vmclarity of this Result.


        :param vmclarity: The vmclarity of this Result.
        :type vmclarity: VMClarityData
        """
        if vmclarity is None:
            raise ValueError("Invalid value for `vmclarity`, must not be `None`")  # noqa: E501

        self._vmclarity = vmclarity
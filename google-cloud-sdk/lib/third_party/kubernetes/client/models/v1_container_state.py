# coding: utf-8
"""
    Kubernetes

    No description provided (generated by Swagger Codegen
    https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.4

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class V1ContainerState(object):
  """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
  """
    Attributes:
      swagger_types (dict): The key is attribute name and the value is attribute
        type.
      attribute_map (dict): The key is attribute name and the value is json key
        in definition.
  """
  swagger_types = {
      'running': 'V1ContainerStateRunning',
      'terminated': 'V1ContainerStateTerminated',
      'waiting': 'V1ContainerStateWaiting'
  }

  attribute_map = {
      'running': 'running',
      'terminated': 'terminated',
      'waiting': 'waiting'
  }

  def __init__(self, running=None, terminated=None, waiting=None):
    """
        V1ContainerState - a model defined in Swagger
        """

    self._running = None
    self._terminated = None
    self._waiting = None
    self.discriminator = None

    if running is not None:
      self.running = running
    if terminated is not None:
      self.terminated = terminated
    if waiting is not None:
      self.waiting = waiting

  @property
  def running(self):
    """
        Gets the running of this V1ContainerState.
        Details about a running container

        :return: The running of this V1ContainerState.
        :rtype: V1ContainerStateRunning
        """
    return self._running

  @running.setter
  def running(self, running):
    """
        Sets the running of this V1ContainerState.
        Details about a running container

        :param running: The running of this V1ContainerState.
        :type: V1ContainerStateRunning
        """

    self._running = running

  @property
  def terminated(self):
    """
        Gets the terminated of this V1ContainerState.
        Details about a terminated container

        :return: The terminated of this V1ContainerState.
        :rtype: V1ContainerStateTerminated
        """
    return self._terminated

  @terminated.setter
  def terminated(self, terminated):
    """
        Sets the terminated of this V1ContainerState.
        Details about a terminated container

        :param terminated: The terminated of this V1ContainerState.
        :type: V1ContainerStateTerminated
        """

    self._terminated = terminated

  @property
  def waiting(self):
    """
        Gets the waiting of this V1ContainerState.
        Details about a waiting container

        :return: The waiting of this V1ContainerState.
        :rtype: V1ContainerStateWaiting
        """
    return self._waiting

  @waiting.setter
  def waiting(self, waiting):
    """
        Sets the waiting of this V1ContainerState.
        Details about a waiting container

        :param waiting: The waiting of this V1ContainerState.
        :type: V1ContainerStateWaiting
        """

    self._waiting = waiting

  def to_dict(self):
    """
        Returns the model properties as a dict
        """
    result = {}

    for attr, _ in iteritems(self.swagger_types):
      value = getattr(self, attr)
      if isinstance(value, list):
        result[attr] = list(
            map(lambda x: x.to_dict() if hasattr(x, 'to_dict') else x, value))
      elif hasattr(value, 'to_dict'):
        result[attr] = value.to_dict()
      elif isinstance(value, dict):
        result[attr] = dict(
            map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], 'to_dict') else item, value.items()))
      else:
        result[attr] = value

    return result

  def to_str(self):
    """
        Returns the string representation of the model
        """
    return pformat(self.to_dict())

  def __repr__(self):
    """
        For `print` and `pprint`
        """
    return self.to_str()

  def __eq__(self, other):
    """
        Returns true if both objects are equal
        """
    if not isinstance(other, V1ContainerState):
      return False

    return self.__dict__ == other.__dict__

  def __ne__(self, other):
    """
        Returns true if both objects are not equal
        """
    return not self == other

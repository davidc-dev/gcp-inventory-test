"""Generated client library for parametermanager version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.parametermanager.v1 import parametermanager_v1_messages as messages


class ParametermanagerV1(base_api.BaseApiClient):
  """Generated client library for service parametermanager version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://parametermanager.googleapis.com/'
  MTLS_BASE_URL = 'https://parametermanager.mtls.googleapis.com/'

  _PACKAGE = 'parametermanager'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'ParametermanagerV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new parametermanager handle."""
    url = url or self.BASE_URL
    super(ParametermanagerV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_parameters_versions = self.ProjectsLocationsParametersVersionsService(self)
    self.projects_locations_parameters = self.ProjectsLocationsParametersService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsParametersVersionsService(base_api.BaseApiService):
    """Service class for the projects_locations_parameters_versions resource."""

    _NAME = 'projects_locations_parameters_versions'

    def __init__(self, client):
      super(ParametermanagerV1.ProjectsLocationsParametersVersionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new ParameterVersion in a given project, location, and parameter.

      Args:
        request: (ParametermanagerProjectsLocationsParametersVersionsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ParameterVersion) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/parameters/{parametersId}/versions',
        http_method='POST',
        method_id='parametermanager.projects.locations.parameters.versions.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['parameterVersionId', 'requestId'],
        relative_path='v1/{+parent}/versions',
        request_field='parameterVersion',
        request_type_name='ParametermanagerProjectsLocationsParametersVersionsCreateRequest',
        response_type_name='ParameterVersion',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single ParameterVersion.

      Args:
        request: (ParametermanagerProjectsLocationsParametersVersionsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/parameters/{parametersId}/versions/{versionsId}',
        http_method='DELETE',
        method_id='parametermanager.projects.locations.parameters.versions.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ParametermanagerProjectsLocationsParametersVersionsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single ParameterVersion.

      Args:
        request: (ParametermanagerProjectsLocationsParametersVersionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ParameterVersion) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/parameters/{parametersId}/versions/{versionsId}',
        http_method='GET',
        method_id='parametermanager.projects.locations.parameters.versions.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['view'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ParametermanagerProjectsLocationsParametersVersionsGetRequest',
        response_type_name='ParameterVersion',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists ParameterVersions in a given project, location, and parameter.

      Args:
        request: (ParametermanagerProjectsLocationsParametersVersionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListParameterVersionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/parameters/{parametersId}/versions',
        http_method='GET',
        method_id='parametermanager.projects.locations.parameters.versions.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/versions',
        request_field='',
        request_type_name='ParametermanagerProjectsLocationsParametersVersionsListRequest',
        response_type_name='ListParameterVersionsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a single ParameterVersion.

      Args:
        request: (ParametermanagerProjectsLocationsParametersVersionsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ParameterVersion) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/parameters/{parametersId}/versions/{versionsId}',
        http_method='PATCH',
        method_id='parametermanager.projects.locations.parameters.versions.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1/{+name}',
        request_field='parameterVersion',
        request_type_name='ParametermanagerProjectsLocationsParametersVersionsPatchRequest',
        response_type_name='ParameterVersion',
        supports_download=False,
    )

    def Render(self, request, global_params=None):
      r"""Gets rendered version of a ParameterVersion.

      Args:
        request: (ParametermanagerProjectsLocationsParametersVersionsRenderRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RenderParameterVersionResponse) The response message.
      """
      config = self.GetMethodConfig('Render')
      return self._RunMethod(
          config, request, global_params=global_params)

    Render.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/parameters/{parametersId}/versions/{versionsId}:render',
        http_method='GET',
        method_id='parametermanager.projects.locations.parameters.versions.render',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:render',
        request_field='',
        request_type_name='ParametermanagerProjectsLocationsParametersVersionsRenderRequest',
        response_type_name='RenderParameterVersionResponse',
        supports_download=False,
    )

  class ProjectsLocationsParametersService(base_api.BaseApiService):
    """Service class for the projects_locations_parameters resource."""

    _NAME = 'projects_locations_parameters'

    def __init__(self, client):
      super(ParametermanagerV1.ProjectsLocationsParametersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Parameter in a given project and location.

      Args:
        request: (ParametermanagerProjectsLocationsParametersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Parameter) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/parameters',
        http_method='POST',
        method_id='parametermanager.projects.locations.parameters.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['parameterId', 'requestId'],
        relative_path='v1/{+parent}/parameters',
        request_field='parameter',
        request_type_name='ParametermanagerProjectsLocationsParametersCreateRequest',
        response_type_name='Parameter',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Parameter.

      Args:
        request: (ParametermanagerProjectsLocationsParametersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/parameters/{parametersId}',
        http_method='DELETE',
        method_id='parametermanager.projects.locations.parameters.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ParametermanagerProjectsLocationsParametersDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Parameter.

      Args:
        request: (ParametermanagerProjectsLocationsParametersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Parameter) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/parameters/{parametersId}',
        http_method='GET',
        method_id='parametermanager.projects.locations.parameters.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ParametermanagerProjectsLocationsParametersGetRequest',
        response_type_name='Parameter',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Parameters in a given project and location.

      Args:
        request: (ParametermanagerProjectsLocationsParametersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListParametersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/parameters',
        http_method='GET',
        method_id='parametermanager.projects.locations.parameters.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/parameters',
        request_field='',
        request_type_name='ParametermanagerProjectsLocationsParametersListRequest',
        response_type_name='ListParametersResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a single Parameter.

      Args:
        request: (ParametermanagerProjectsLocationsParametersPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Parameter) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/parameters/{parametersId}',
        http_method='PATCH',
        method_id='parametermanager.projects.locations.parameters.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1/{+name}',
        request_field='parameter',
        request_type_name='ParametermanagerProjectsLocationsParametersPatchRequest',
        response_type_name='Parameter',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(ParametermanagerV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (ParametermanagerProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='parametermanager.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ParametermanagerProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (ParametermanagerProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='parametermanager.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['extraLocationTypes', 'filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/locations',
        request_field='',
        request_type_name='ParametermanagerProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(ParametermanagerV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

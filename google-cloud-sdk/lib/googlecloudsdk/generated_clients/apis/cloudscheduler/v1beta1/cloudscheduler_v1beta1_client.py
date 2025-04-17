"""Generated client library for cloudscheduler version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.cloudscheduler.v1beta1 import cloudscheduler_v1beta1_messages as messages


class CloudschedulerV1beta1(base_api.BaseApiClient):
  """Generated client library for service cloudscheduler version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://cloudscheduler.googleapis.com/'
  MTLS_BASE_URL = 'https://cloudscheduler.mtls.googleapis.com/'

  _PACKAGE = 'cloudscheduler'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1beta1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'CloudschedulerV1beta1'
  _URL_VERSION = 'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudscheduler handle."""
    url = url or self.BASE_URL
    super(CloudschedulerV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_jobs = self.ProjectsLocationsJobsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsJobsService(base_api.BaseApiService):
    """Service class for the projects_locations_jobs resource."""

    _NAME = 'projects_locations_jobs'

    def __init__(self, client):
      super(CloudschedulerV1beta1.ProjectsLocationsJobsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a job.

      Args:
        request: (CloudschedulerProjectsLocationsJobsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobs',
        http_method='POST',
        method_id='cloudscheduler.projects.locations.jobs.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1beta1/{+parent}/jobs',
        request_field='job',
        request_type_name='CloudschedulerProjectsLocationsJobsCreateRequest',
        response_type_name='Job',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a job.

      Args:
        request: (CloudschedulerProjectsLocationsJobsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}',
        http_method='DELETE',
        method_id='cloudscheduler.projects.locations.jobs.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['legacyAppEngineCron'],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='CloudschedulerProjectsLocationsJobsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a job.

      Args:
        request: (CloudschedulerProjectsLocationsJobsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}',
        http_method='GET',
        method_id='cloudscheduler.projects.locations.jobs.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='CloudschedulerProjectsLocationsJobsGetRequest',
        response_type_name='Job',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists jobs.

      Args:
        request: (CloudschedulerProjectsLocationsJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListJobsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobs',
        http_method='GET',
        method_id='cloudscheduler.projects.locations.jobs.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'legacyAppEngineCron', 'pageSize', 'pageToken'],
        relative_path='v1beta1/{+parent}/jobs',
        request_field='',
        request_type_name='CloudschedulerProjectsLocationsJobsListRequest',
        response_type_name='ListJobsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a job. If successful, the updated Job is returned. If the job does not exist, `NOT_FOUND` is returned. If UpdateJob does not successfully return, it is possible for the job to be in an Job.State.UPDATE_FAILED state. A job in this state may not be executed. If this happens, retry the UpdateJob request until a successful response is received.

      Args:
        request: (CloudschedulerProjectsLocationsJobsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}',
        http_method='PATCH',
        method_id='cloudscheduler.projects.locations.jobs.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1beta1/{+name}',
        request_field='job',
        request_type_name='CloudschedulerProjectsLocationsJobsPatchRequest',
        response_type_name='Job',
        supports_download=False,
    )

    def Pause(self, request, global_params=None):
      r"""Pauses a job. If a job is paused then the system will stop executing the job until it is re-enabled via ResumeJob. The state of the job is stored in state; if paused it will be set to Job.State.PAUSED. A job must be in Job.State.ENABLED to be paused.

      Args:
        request: (CloudschedulerProjectsLocationsJobsPauseRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Pause')
      return self._RunMethod(
          config, request, global_params=global_params)

    Pause.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}:pause',
        http_method='POST',
        method_id='cloudscheduler.projects.locations.jobs.pause',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:pause',
        request_field='pauseJobRequest',
        request_type_name='CloudschedulerProjectsLocationsJobsPauseRequest',
        response_type_name='Job',
        supports_download=False,
    )

    def Resume(self, request, global_params=None):
      r"""Resume a job. This method reenables a job after it has been Job.State.PAUSED. The state of a job is stored in Job.state; after calling this method it will be set to Job.State.ENABLED. A job must be in Job.State.PAUSED to be resumed.

      Args:
        request: (CloudschedulerProjectsLocationsJobsResumeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Resume')
      return self._RunMethod(
          config, request, global_params=global_params)

    Resume.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}:resume',
        http_method='POST',
        method_id='cloudscheduler.projects.locations.jobs.resume',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:resume',
        request_field='resumeJobRequest',
        request_type_name='CloudschedulerProjectsLocationsJobsResumeRequest',
        response_type_name='Job',
        supports_download=False,
    )

    def Run(self, request, global_params=None):
      r"""Forces a job to run now. When this method is called, Cloud Scheduler will dispatch the job, even if the job is already running.

      Args:
        request: (CloudschedulerProjectsLocationsJobsRunRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Run')
      return self._RunMethod(
          config, request, global_params=global_params)

    Run.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}:run',
        http_method='POST',
        method_id='cloudscheduler.projects.locations.jobs.run',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:run',
        request_field='runJobRequest',
        request_type_name='CloudschedulerProjectsLocationsJobsRunRequest',
        response_type_name='Job',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(CloudschedulerV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (CloudschedulerProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='cloudscheduler.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='CloudschedulerProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (CloudschedulerProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='cloudscheduler.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['extraLocationTypes', 'filter', 'pageSize', 'pageToken'],
        relative_path='v1beta1/{+name}/locations',
        request_field='',
        request_type_name='CloudschedulerProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(CloudschedulerV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

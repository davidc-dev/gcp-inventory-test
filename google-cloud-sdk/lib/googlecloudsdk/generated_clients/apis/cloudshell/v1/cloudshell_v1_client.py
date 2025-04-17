"""Generated client library for cloudshell version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.cloudshell.v1 import cloudshell_v1_messages as messages


class CloudshellV1(base_api.BaseApiClient):
  """Generated client library for service cloudshell version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://cloudshell.googleapis.com/'
  MTLS_BASE_URL = 'https://cloudshell.mtls.googleapis.com/'

  _PACKAGE = 'cloudshell'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'CloudshellV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudshell handle."""
    url = url or self.BASE_URL
    super(CloudshellV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.operations = self.OperationsService(self)
    self.users_environments = self.UsersEnvironmentsService(self)
    self.users = self.UsersService(self)

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = 'operations'

    def __init__(self, client):
      super(CloudshellV1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.

      Args:
        request: (CloudshellOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='cloudshell.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='CloudshellOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (CloudshellOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/operations/{operationsId}',
        http_method='DELETE',
        method_id='cloudshell.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='CloudshellOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (CloudshellOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/operations/{operationsId}',
        http_method='GET',
        method_id='cloudshell.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='CloudshellOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (CloudshellOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/operations',
        http_method='GET',
        method_id='cloudshell.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='CloudshellOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class UsersEnvironmentsService(base_api.BaseApiService):
    """Service class for the users_environments resource."""

    _NAME = 'users_environments'

    def __init__(self, client):
      super(CloudshellV1.UsersEnvironmentsService, self).__init__(client)
      self._upload_configs = {
          }

    def AddPublicKey(self, request, global_params=None):
      r"""Adds a public SSH key to an environment, allowing clients with the corresponding private key to connect to that environment via SSH. If a key with the same content already exists, this will error with ALREADY_EXISTS.

      Args:
        request: (CloudshellUsersEnvironmentsAddPublicKeyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('AddPublicKey')
      return self._RunMethod(
          config, request, global_params=global_params)

    AddPublicKey.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/users/{usersId}/environments/{environmentsId}:addPublicKey',
        http_method='POST',
        method_id='cloudshell.users.environments.addPublicKey',
        ordered_params=['environment'],
        path_params=['environment'],
        query_params=[],
        relative_path='v1/{+environment}:addPublicKey',
        request_field='addPublicKeyRequest',
        request_type_name='CloudshellUsersEnvironmentsAddPublicKeyRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Authorize(self, request, global_params=None):
      r"""Sends OAuth credentials to a running environment on behalf of a user. When this completes, the environment will be authorized to run various Google Cloud command line tools without requiring the user to manually authenticate.

      Args:
        request: (CloudshellUsersEnvironmentsAuthorizeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Authorize')
      return self._RunMethod(
          config, request, global_params=global_params)

    Authorize.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/users/{usersId}/environments/{environmentsId}:authorize',
        http_method='POST',
        method_id='cloudshell.users.environments.authorize',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:authorize',
        request_field='authorizeEnvironmentRequest',
        request_type_name='CloudshellUsersEnvironmentsAuthorizeRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets an environment. Returns NOT_FOUND if the environment does not exist.

      Args:
        request: (CloudshellUsersEnvironmentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Environment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/users/{usersId}/environments/{environmentsId}',
        http_method='GET',
        method_id='cloudshell.users.environments.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='CloudshellUsersEnvironmentsGetRequest',
        response_type_name='Environment',
        supports_download=False,
    )

    def RemovePublicKey(self, request, global_params=None):
      r"""Removes a public SSH key from an environment. Clients will no longer be able to connect to the environment using the corresponding private key. If a key with the same content is not present, this will error with NOT_FOUND.

      Args:
        request: (CloudshellUsersEnvironmentsRemovePublicKeyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('RemovePublicKey')
      return self._RunMethod(
          config, request, global_params=global_params)

    RemovePublicKey.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/users/{usersId}/environments/{environmentsId}:removePublicKey',
        http_method='POST',
        method_id='cloudshell.users.environments.removePublicKey',
        ordered_params=['environment'],
        path_params=['environment'],
        query_params=[],
        relative_path='v1/{+environment}:removePublicKey',
        request_field='removePublicKeyRequest',
        request_type_name='CloudshellUsersEnvironmentsRemovePublicKeyRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Start(self, request, global_params=None):
      r"""Starts an existing environment, allowing clients to connect to it. The returned operation will contain an instance of StartEnvironmentMetadata in its metadata field. Users can wait for the environment to start by polling this operation via GetOperation. Once the environment has finished starting and is ready to accept connections, the operation will contain a StartEnvironmentResponse in its response field.

      Args:
        request: (CloudshellUsersEnvironmentsStartRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Start')
      return self._RunMethod(
          config, request, global_params=global_params)

    Start.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/users/{usersId}/environments/{environmentsId}:start',
        http_method='POST',
        method_id='cloudshell.users.environments.start',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:start',
        request_field='startEnvironmentRequest',
        request_type_name='CloudshellUsersEnvironmentsStartRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class UsersService(base_api.BaseApiService):
    """Service class for the users resource."""

    _NAME = 'users'

    def __init__(self, client):
      super(CloudshellV1.UsersService, self).__init__(client)
      self._upload_configs = {
          }

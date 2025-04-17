"""Generated message classes for oslogin version v1alpha.

You can use OS Login to manage access to your VM instances using IAM roles.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'oslogin'


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }
  """



class GoogleCloudOsloginControlplaneRegionalV1alphaSignSshPublicKeyRequest(_messages.Message):
  r"""A request message for signing an SSH public key.

  Fields:
    appEngineInstance: The App Engine instance to sign the SSH public key for.
      Expected format:
      services/{service}/versions/{version}/instances/{instance}
    computeInstance: The Compute instance to sign the SSH public key for.
      Expected format:
      projects/{project}/zones/{zone}/instances/{numeric_instance_id}
    serviceAccount: Optional. The service account for the instance. If the
      instance in question does not have a service account, this field should
      be left empty. If the wrong service account is provided, this operation
      will return a signed certificate that will not be accepted by the VM.
    sshPublicKey: Required. The SSH public key to sign.
  """

  appEngineInstance = _messages.StringField(1)
  computeInstance = _messages.StringField(2)
  serviceAccount = _messages.StringField(3)
  sshPublicKey = _messages.StringField(4)


class GoogleCloudOsloginControlplaneRegionalV1alphaSignSshPublicKeyResponse(_messages.Message):
  r"""The response message for signing an SSH public key.

  Fields:
    signedSshPublicKey: The signed SSH public key to use in the SSH handshake.
  """

  signedSshPublicKey = _messages.StringField(1)


class ImportSshPublicKeyResponse(_messages.Message):
  r"""A response message for importing an SSH public key.

  Fields:
    details: Detailed information about import results.
    loginProfile: The login profile information for the user.
  """

  details = _messages.StringField(1)
  loginProfile = _messages.MessageField('LoginProfile', 2)


class LoginProfile(_messages.Message):
  r"""The user profile information used for logging in to a virtual machine on
  Google Compute Engine.

  Messages:
    SshPublicKeysValue: A map from SSH public key fingerprint to the
      associated key object.

  Fields:
    name: Required. A unique user ID.
    posixAccounts: The list of POSIX accounts associated with the user.
    securityKeys: The registered security key credentials for a user.
    sshPublicKeys: A map from SSH public key fingerprint to the associated key
      object.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class SshPublicKeysValue(_messages.Message):
    r"""A map from SSH public key fingerprint to the associated key object.

    Messages:
      AdditionalProperty: An additional property for a SshPublicKeysValue
        object.

    Fields:
      additionalProperties: Additional properties of type SshPublicKeysValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a SshPublicKeysValue object.

      Fields:
        key: Name of the additional property.
        value: A SshPublicKey attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('SshPublicKey', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  name = _messages.StringField(1)
  posixAccounts = _messages.MessageField('PosixAccount', 2, repeated=True)
  securityKeys = _messages.MessageField('SecurityKey', 3, repeated=True)
  sshPublicKeys = _messages.MessageField('SshPublicKeysValue', 4)


class OsloginProjectsLocationsSignSshPublicKeyRequest(_messages.Message):
  r"""A OsloginProjectsLocationsSignSshPublicKeyRequest object.

  Fields:
    googleCloudOsloginControlplaneRegionalV1alphaSignSshPublicKeyRequest: A
      GoogleCloudOsloginControlplaneRegionalV1alphaSignSshPublicKeyRequest
      resource to be passed as the request body.
    parent: Required. The parent for the signing request. Format:
      projects/{project}/locations/{location}
  """

  googleCloudOsloginControlplaneRegionalV1alphaSignSshPublicKeyRequest = _messages.MessageField('GoogleCloudOsloginControlplaneRegionalV1alphaSignSshPublicKeyRequest', 1)
  parent = _messages.StringField(2, required=True)


class OsloginUsersGetLoginProfileRequest(_messages.Message):
  r"""A OsloginUsersGetLoginProfileRequest object.

  Enums:
    OperatingSystemTypeValueValuesEnum: The type of operating system
      associated with the account.
    ViewValueValuesEnum: The view configures whether to retrieve security keys
      information.

  Fields:
    name: Required. The unique ID for the user in format `users/{user}`.
    operatingSystemType: The type of operating system associated with the
      account.
    projectId: The project ID of the Google Cloud Platform project.
    systemId: A system ID for filtering the results of the request.
    view: The view configures whether to retrieve security keys information.
  """

  class OperatingSystemTypeValueValuesEnum(_messages.Enum):
    r"""The type of operating system associated with the account.

    Values:
      OPERATING_SYSTEM_TYPE_UNSPECIFIED: The operating system type associated
        with the user account information is unspecified.
      LINUX: Linux user account information.
      WINDOWS: Windows user account information.
    """
    OPERATING_SYSTEM_TYPE_UNSPECIFIED = 0
    LINUX = 1
    WINDOWS = 2

  class ViewValueValuesEnum(_messages.Enum):
    r"""The view configures whether to retrieve security keys information.

    Values:
      LOGIN_PROFILE_VIEW_UNSPECIFIED: The default login profile view. The API
        defaults to the BASIC view.
      BASIC: Includes POSIX and SSH key information.
      SECURITY_KEY: Include security key information for the user.
    """
    LOGIN_PROFILE_VIEW_UNSPECIFIED = 0
    BASIC = 1
    SECURITY_KEY = 2

  name = _messages.StringField(1, required=True)
  operatingSystemType = _messages.EnumField('OperatingSystemTypeValueValuesEnum', 2)
  projectId = _messages.StringField(3)
  systemId = _messages.StringField(4)
  view = _messages.EnumField('ViewValueValuesEnum', 5)


class OsloginUsersImportSshPublicKeyRequest(_messages.Message):
  r"""A OsloginUsersImportSshPublicKeyRequest object.

  Enums:
    ViewValueValuesEnum: The view configures whether to retrieve security keys
      information.

  Fields:
    parent: The unique ID for the user in format `users/{user}`.
    projectId: The project ID of the Google Cloud Platform project.
    regions: Optional. The regions to wait for a POSIX account to be written
      to before returning a response. If unspecified, defaults to all regions.
      Regions are listed at https://cloud.google.com/about/locations#region.
    sshPublicKey: A SshPublicKey resource to be passed as the request body.
    view: The view configures whether to retrieve security keys information.
  """

  class ViewValueValuesEnum(_messages.Enum):
    r"""The view configures whether to retrieve security keys information.

    Values:
      LOGIN_PROFILE_VIEW_UNSPECIFIED: The default login profile view. The API
        defaults to the BASIC view.
      BASIC: Includes POSIX and SSH key information.
      SECURITY_KEY: Include security key information for the user.
    """
    LOGIN_PROFILE_VIEW_UNSPECIFIED = 0
    BASIC = 1
    SECURITY_KEY = 2

  parent = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2)
  regions = _messages.StringField(3, repeated=True)
  sshPublicKey = _messages.MessageField('SshPublicKey', 4)
  view = _messages.EnumField('ViewValueValuesEnum', 5)


class OsloginUsersProjectsDeleteRequest(_messages.Message):
  r"""A OsloginUsersProjectsDeleteRequest object.

  Enums:
    OperatingSystemTypeValueValuesEnum: The type of operating system
      associated with the account.

  Fields:
    name: Required. A reference to the POSIX account to update. POSIX accounts
      are identified by the project ID they are associated with. A reference
      to the POSIX account is in format `users/{user}/projects/{project}`.
    operatingSystemType: The type of operating system associated with the
      account.
  """

  class OperatingSystemTypeValueValuesEnum(_messages.Enum):
    r"""The type of operating system associated with the account.

    Values:
      OPERATING_SYSTEM_TYPE_UNSPECIFIED: The operating system type associated
        with the user account information is unspecified.
      LINUX: Linux user account information.
      WINDOWS: Windows user account information.
    """
    OPERATING_SYSTEM_TYPE_UNSPECIFIED = 0
    LINUX = 1
    WINDOWS = 2

  name = _messages.StringField(1, required=True)
  operatingSystemType = _messages.EnumField('OperatingSystemTypeValueValuesEnum', 2)


class OsloginUsersProjectsLocationsSignSshPublicKeyRequest(_messages.Message):
  r"""A OsloginUsersProjectsLocationsSignSshPublicKeyRequest object.

  Fields:
    parent: The parent project and region for the signing request.
    signSshPublicKeyRequest: A SignSshPublicKeyRequest resource to be passed
      as the request body.
  """

  parent = _messages.StringField(1, required=True)
  signSshPublicKeyRequest = _messages.MessageField('SignSshPublicKeyRequest', 2)


class OsloginUsersProjectsProvisionPosixAccountRequest(_messages.Message):
  r"""A OsloginUsersProjectsProvisionPosixAccountRequest object.

  Fields:
    name: Required. The unique ID for the user in format
      `users/{user}/projects/{project}`.
    provisionPosixAccountRequest: A ProvisionPosixAccountRequest resource to
      be passed as the request body.
  """

  name = _messages.StringField(1, required=True)
  provisionPosixAccountRequest = _messages.MessageField('ProvisionPosixAccountRequest', 2)


class OsloginUsersProjectsZonesSignSshPublicKeyRequest(_messages.Message):
  r"""A OsloginUsersProjectsZonesSignSshPublicKeyRequest object.

  Fields:
    parent: The parent project and region for the signing request.
    signSshPublicKeyRequest: A SignSshPublicKeyRequest resource to be passed
      as the request body.
  """

  parent = _messages.StringField(1, required=True)
  signSshPublicKeyRequest = _messages.MessageField('SignSshPublicKeyRequest', 2)


class OsloginUsersSshPublicKeysCreateRequest(_messages.Message):
  r"""A OsloginUsersSshPublicKeysCreateRequest object.

  Fields:
    parent: Required. The unique ID for the user in format `users/{user}`.
    sshPublicKey: A SshPublicKey resource to be passed as the request body.
  """

  parent = _messages.StringField(1, required=True)
  sshPublicKey = _messages.MessageField('SshPublicKey', 2)


class OsloginUsersSshPublicKeysDeleteRequest(_messages.Message):
  r"""A OsloginUsersSshPublicKeysDeleteRequest object.

  Fields:
    name: Required. The fingerprint of the public key to update. Public keys
      are identified by their SHA-256 fingerprint. The fingerprint of the
      public key is in format `users/{user}/sshPublicKeys/{fingerprint}`.
  """

  name = _messages.StringField(1, required=True)


class OsloginUsersSshPublicKeysGetRequest(_messages.Message):
  r"""A OsloginUsersSshPublicKeysGetRequest object.

  Fields:
    name: Required. The fingerprint of the public key to retrieve. Public keys
      are identified by their SHA-256 fingerprint. The fingerprint of the
      public key is in format `users/{user}/sshPublicKeys/{fingerprint}`.
  """

  name = _messages.StringField(1, required=True)


class OsloginUsersSshPublicKeysPatchRequest(_messages.Message):
  r"""A OsloginUsersSshPublicKeysPatchRequest object.

  Fields:
    name: Required. The fingerprint of the public key to update. Public keys
      are identified by their SHA-256 fingerprint. The fingerprint of the
      public key is in format `users/{user}/sshPublicKeys/{fingerprint}`.
    sshPublicKey: A SshPublicKey resource to be passed as the request body.
    updateMask: Mask to control which fields get updated. Updates all if not
      present.
  """

  name = _messages.StringField(1, required=True)
  sshPublicKey = _messages.MessageField('SshPublicKey', 2)
  updateMask = _messages.StringField(3)


class PosixAccount(_messages.Message):
  r"""The POSIX account information associated with a Google account.

  Enums:
    OperatingSystemTypeValueValuesEnum: The operating system type where this
      account applies.

  Fields:
    accountId: Output only. A POSIX account identifier.
    gecos: The GECOS (user information) entry for this account.
    gid: The default group ID.
    homeDirectory: The path to the home directory for this account.
    name: Output only. The canonical resource name.
    operatingSystemType: The operating system type where this account applies.
    primary: Only one POSIX account can be marked as primary.
    shell: The path to the logic shell for this account.
    systemId: System identifier for which account the username or uid applies
      to. By default, the empty value is used.
    uid: The user ID.
    username: The username of the POSIX account.
  """

  class OperatingSystemTypeValueValuesEnum(_messages.Enum):
    r"""The operating system type where this account applies.

    Values:
      OPERATING_SYSTEM_TYPE_UNSPECIFIED: The operating system type associated
        with the user account information is unspecified.
      LINUX: Linux user account information.
      WINDOWS: Windows user account information.
    """
    OPERATING_SYSTEM_TYPE_UNSPECIFIED = 0
    LINUX = 1
    WINDOWS = 2

  accountId = _messages.StringField(1)
  gecos = _messages.StringField(2)
  gid = _messages.IntegerField(3)
  homeDirectory = _messages.StringField(4)
  name = _messages.StringField(5)
  operatingSystemType = _messages.EnumField('OperatingSystemTypeValueValuesEnum', 6)
  primary = _messages.BooleanField(7)
  shell = _messages.StringField(8)
  systemId = _messages.StringField(9)
  uid = _messages.IntegerField(10)
  username = _messages.StringField(11)


class ProvisionPosixAccountRequest(_messages.Message):
  r"""A request message for creating a POSIX account entry.

  Fields:
    regions: Optional. The regions to wait for a POSIX account to be written
      to before returning a response. If unspecified, defaults to all regions.
      Regions are listed at https://cloud.google.com/about/locations#region.
  """

  regions = _messages.StringField(1, repeated=True)


class SecurityKey(_messages.Message):
  r"""The credential information for a Google registered security key.

  Fields:
    deviceNickname: The security key nickname explicitly set by the user.
    privateKey: Hardware-backed private key text in SSH format.
    publicKey: Public key text in SSH format, defined by
      [RFC4253]("https://www.ietf.org/rfc/rfc4253.txt") section 6.6.
    universalTwoFactor: The U2F protocol type.
    webAuthn: The Web Authentication protocol type.
  """

  deviceNickname = _messages.StringField(1)
  privateKey = _messages.StringField(2)
  publicKey = _messages.StringField(3)
  universalTwoFactor = _messages.MessageField('UniversalTwoFactor', 4)
  webAuthn = _messages.MessageField('WebAuthn', 5)


class SignSshPublicKeyRequest(_messages.Message):
  r"""A SignSshPublicKeyRequest object.

  Fields:
    sshPublicKey: The SSH public key to sign.
  """

  sshPublicKey = _messages.StringField(1)


class SignSshPublicKeyResponse(_messages.Message):
  r"""A SignSshPublicKeyResponse object.

  Fields:
    signedSshPublicKey: The signed SSH public key to use in the SSH handshake.
  """

  signedSshPublicKey = _messages.StringField(1)


class SshPublicKey(_messages.Message):
  r"""The SSH public key information associated with a Google account.

  Fields:
    expirationTimeUsec: An expiration time in microseconds since epoch.
    fingerprint: Output only. The SHA-256 fingerprint of the SSH public key.
    key: Required. Public key text in SSH format, defined by
      [RFC4253](https://www.ietf.org/rfc/rfc4253.txt) section 6.6.
    name: Output only. The canonical resource name.
  """

  expirationTimeUsec = _messages.IntegerField(1)
  fingerprint = _messages.StringField(2)
  key = _messages.StringField(3)
  name = _messages.StringField(4)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class UniversalTwoFactor(_messages.Message):
  r"""Security key information specific to the U2F protocol.

  Fields:
    appId: Application ID for the U2F protocol.
  """

  appId = _messages.StringField(1)


class WebAuthn(_messages.Message):
  r"""Security key information specific to the Web Authentication protocol.

  Fields:
    rpId: Relying party ID for Web Authentication.
  """

  rpId = _messages.StringField(1)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')

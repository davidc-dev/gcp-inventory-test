"""Generated message classes for seclm version v1.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'seclm'


class CancelOperationRequest(_messages.Message):
  r"""The request message for Operations.CancelOperation."""


class Candidate(_messages.Message):
  r"""A response candidate generated from the model.

  Enums:
    FinishReasonValueValuesEnum: Optional. Output only. The reason why the
      model stopped generating tokens. If empty, the model has not stopped
      generating the tokens.

  Fields:
    citationMetadata: Output only. Citation information for model-generated
      candidate. This field may be populated with recitation information for
      any text included in the `content`. These are passages that are
      "recited" from copyrighted material in the foundational LLM's training
      data.
    content: Output only. Generated content returned from the model.
    finishReason: Optional. Output only. The reason why the model stopped
      generating tokens. If empty, the model has not stopped generating the
      tokens.
    groundingMetadata: Output only. Grounding metadata for model-generated
      candidate. Grounding sources returned by extensions are checked against
      the model generated candidate, return the grounding sources that are
      used to generate the candidate.
    index: Output only. Index of the candidate in the list of candidates.
    safetyRatings: List of ratings for the safety of a response candidate.
      There is at most one rating per category.
    tokenCount: Output only. Token count for this candidate.
  """

  class FinishReasonValueValuesEnum(_messages.Enum):
    r"""Optional. Output only. The reason why the model stopped generating
    tokens. If empty, the model has not stopped generating the tokens.

    Values:
      FINISH_REASON_UNSPECIFIED: Default value. This value is unused.
      STOP: Natural stop point of the model or provided stop sequence.
      MAX_TOKENS: The maximum number of tokens as specified in the request was
        reached.
      SAFETY: The candidate content was flagged for safety reasons.
      RECITATION: The candidate content was flagged for recitation reasons.
      OTHER: Unknown reason.
      BLOCKLIST: Token generation stopped because the content contains
        forbidden terms.
      PROHIBITED_CONTENT: Token generation stopped for potentially containing
        prohibited content.
      SPII: Token generation stopped because the content potentially contains
        Sensitive Personally Identifiable Information (SPII).
      MALFORMED_FUNCTION_CALL: The function call generated by the model is
        invalid.
    """
    FINISH_REASON_UNSPECIFIED = 0
    STOP = 1
    MAX_TOKENS = 2
    SAFETY = 3
    RECITATION = 4
    OTHER = 5
    BLOCKLIST = 6
    PROHIBITED_CONTENT = 7
    SPII = 8
    MALFORMED_FUNCTION_CALL = 9

  citationMetadata = _messages.MessageField('CitationMetadata', 1)
  content = _messages.MessageField('Content', 2)
  finishReason = _messages.EnumField('FinishReasonValueValuesEnum', 3)
  groundingMetadata = _messages.MessageField('GroundingMetadata', 4)
  index = _messages.IntegerField(5, variant=_messages.Variant.INT32)
  safetyRatings = _messages.MessageField('SafetyRating', 6, repeated=True)
  tokenCount = _messages.IntegerField(7, variant=_messages.Variant.INT32)


class Citation(_messages.Message):
  r"""Metadata of one citation.

  Fields:
    endIndex: Index in the prediction output where the citation ends
      (exclusive). Must be > start_index and < len(output).
    license: License associated with this recitation. If present, it refers to
      the license of the source of this citation. Possible licenses include
      code licenses, e.g., mit license.
    publicationDate: Publication date associated with this citation. If
      present, it refers to the date at which the source of this citation was
      published. Possible formats are YYYY, YYYY-MM, YYYY-MM-DD.
    startIndex: Index in the prediction output where the citation starts
      (inclusive). Must be >= 0 and < end_index.
    title: Title associated with this citation. If present, it refers to the
      title of the source of this citation. Possible titles include news
      titles, book titles, etc.
    url: URL associated with this citation. If present, this URL links to the
      webpage of the source of this citation. Possible URLs include news
      websites, GitHub repos, etc.
  """

  endIndex = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  license = _messages.StringField(2)
  publicationDate = _messages.StringField(3)
  startIndex = _messages.IntegerField(4, variant=_messages.Variant.INT32)
  title = _messages.StringField(5)
  url = _messages.StringField(6)


class CitationMetadata(_messages.Message):
  r"""The schema of citations found in textual prediction outputs. Citations
  originate from various sources and indicate that these contents should be
  cited properly.

  Fields:
    citations: Metadata of all citations found in this prediction output.
  """

  citations = _messages.MessageField('Citation', 1, repeated=True)


class Content(_messages.Message):
  r"""The base structured datatype containing multi-part content of a message.
  A `Content` includes a `role` field designating the producer of the
  `Content` and a `parts` field containing multi-part data that contains the
  content of the message turn.

  Fields:
    parts: Required. Ordered `Parts` that constitute a single message. Parts
      may have different IANA MIME types.
    role: Optional. The producer of the content. Must be either 'user' or
      'model'. Useful to set for multi-turn conversations, otherwise can be
      left blank or unset.
  """

  parts = _messages.MessageField('Part', 1, repeated=True)
  role = _messages.StringField(2)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }
  """



class GroundingChunk(_messages.Message):
  r"""Grounding chunk.

  Fields:
    retrievedContext: Grounding chunk from context retrieved by the retrieval
      tools.
    web: Grounding chunk from the web.
  """

  retrievedContext = _messages.MessageField('RetrievedContext', 1)
  web = _messages.MessageField('Web', 2)


class GroundingMetadata(_messages.Message):
  r"""Grounding metadata for model-generated candidate. Grounding sources
  returned by extensions are checked against the model generated candidate,
  return the grounding sources that are used to generate the candidate.

  Fields:
    groundingChunks: List of supporting references retrieved from specified
      grounding source.
    groundingSupports: Optional. List of grounding support.
    searchEntryPoint: Optional. Google search entry for the following-up web
      searches.
    webSearchQueries: Optional. Web search queries for the following-up web
      search.
  """

  groundingChunks = _messages.MessageField('GroundingChunk', 1, repeated=True)
  groundingSupports = _messages.MessageField('GroundingSupport', 2, repeated=True)
  searchEntryPoint = _messages.MessageField('SearchEntryPoint', 3)
  webSearchQueries = _messages.StringField(4, repeated=True)


class GroundingSupport(_messages.Message):
  r"""Grounding support.

  Fields:
    confidenceScores: Confidence score of the support references. Ranges from
      0 to 1. 1 is the most confident. This list must have the same size as
      the grounding_chunk_indices.
    groundingChunkIndices: A list of indices (into 'grounding_chunk')
      specifying the citations associated with the claim. For instance [1,3,4]
      means that grounding_chunk[1], grounding_chunk[3], grounding_chunk[4]
      are the retrieved content attributed to the claim.
    segment: Segment of the content this support belongs to.
  """

  confidenceScores = _messages.FloatField(1, repeated=True, variant=_messages.Variant.FLOAT)
  groundingChunkIndices = _messages.IntegerField(2, repeated=True, variant=_messages.Variant.INT32)
  segment = _messages.MessageField('Segment', 3)


class ListLocationsResponse(_messages.Message):
  r"""The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListOperationsResponse(_messages.Message):
  r"""The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class ListWorkbenchesResponse(_messages.Message):
  r"""Message for response to listing Workbenches.

  Fields:
    nextPageToken: A token identifying a page of results the server should
      return.
    unreachable: Locations that could not be reached.
    workbenches: The list of Workbench
  """

  nextPageToken = _messages.StringField(1)
  unreachable = _messages.StringField(2, repeated=True)
  workbenches = _messages.MessageField('Workbench', 3, repeated=True)


class Location(_messages.Message):
  r"""A resource that represents a Google Cloud location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    displayName: The friendly name for this location, typically a nearby city
      name. For example, "Tokyo".
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  displayName = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  locationId = _messages.StringField(3)
  metadata = _messages.MessageField('MetadataValue', 4)
  name = _messages.StringField(5)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal, successful response of the operation. If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal, successful response of the operation. If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation. It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata. Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal, successful response of the operation. If the original
    method returns no data on success, such as `Delete`, the response is
    `google.protobuf.Empty`. If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource. For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name. For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OperationMetadata(_messages.Message):
  r"""Represents the metadata of the long-running operation.

  Fields:
    apiVersion: Output only. API version used to start the operation.
    createTime: Output only. The time the operation was created.
    endTime: Output only. The time the operation finished running.
    requestedCancellation: Output only. Identifies whether the user has
      requested cancellation of the operation. Operations that have been
      cancelled successfully have Operation.error value with a
      google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.
    statusMessage: Output only. Human-readable status of the operation, if
      any.
    target: Output only. Server-defined resource path for the target of the
      operation.
    verb: Output only. Name of the verb executed by the operation.
  """

  apiVersion = _messages.StringField(1)
  createTime = _messages.StringField(2)
  endTime = _messages.StringField(3)
  requestedCancellation = _messages.BooleanField(4)
  statusMessage = _messages.StringField(5)
  target = _messages.StringField(6)
  verb = _messages.StringField(7)


class Part(_messages.Message):
  r"""A datatype containing media that is part of a multi-part `Content`
  message. A `Part` consists of data which has an associated datatype. A
  `Part` can only contain one of the accepted types in `Part.data`.

  Fields:
    text: Optional. Text part (can be code).
  """

  text = _messages.StringField(1)


class RetrievedContext(_messages.Message):
  r"""Chunk from context retrieved by the retrieval tools.

  Fields:
    title: Title of the attribution.
    uri: URI reference of the attribution.
  """

  title = _messages.StringField(1)
  uri = _messages.StringField(2)


class SafetyRating(_messages.Message):
  r"""Safety rating for a piece of content. The safety rating contains the
  category of harm and the harm probability level in that category for a piece
  of content. Content is classified for safety across a number of harm
  categories and the probability of the harm classification is included here.

  Enums:
    CategoryValueValuesEnum: Required. The category for this rating.
    ProbabilityValueValuesEnum: Required. The probability of harm for this
      content.

  Fields:
    blocked: Was this content blocked because of this rating?
    category: Required. The category for this rating.
    probability: Required. The probability of harm for this content.
  """

  class CategoryValueValuesEnum(_messages.Enum):
    r"""Required. The category for this rating.

    Values:
      HARM_CATEGORY_UNSPECIFIED: The harm category is unspecified.
      HARM_CATEGORY_HATE_SPEECH: The harm category is hate speech.
      HARM_CATEGORY_DANGEROUS_CONTENT: The harm category is dangerous content.
      HARM_CATEGORY_HARASSMENT: The harm category is harassment.
      HARM_CATEGORY_SEXUALLY_EXPLICIT: The harm category is sexually explicit
        content.
    """
    HARM_CATEGORY_UNSPECIFIED = 0
    HARM_CATEGORY_HATE_SPEECH = 1
    HARM_CATEGORY_DANGEROUS_CONTENT = 2
    HARM_CATEGORY_HARASSMENT = 3
    HARM_CATEGORY_SEXUALLY_EXPLICIT = 4

  class ProbabilityValueValuesEnum(_messages.Enum):
    r"""Required. The probability of harm for this content.

    Values:
      HARM_PROBABILITY_UNSPECIFIED: Probability is unspecified.
      NEGLIGIBLE: Content has a negligible chance of being unsafe.
      LOW: Content has a low chance of being unsafe.
      MEDIUM: Content has a medium chance of being unsafe.
      HIGH: Content has a high chance of being unsafe.
    """
    HARM_PROBABILITY_UNSPECIFIED = 0
    NEGLIGIBLE = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4

  blocked = _messages.BooleanField(1)
  category = _messages.EnumField('CategoryValueValuesEnum', 2)
  probability = _messages.EnumField('ProbabilityValueValuesEnum', 3)


class SafetySetting(_messages.Message):
  r"""Safety setting, affecting the safety-blocking behavior. Passing a safety
  setting for a category changes the allowed proability that content is
  blocked.

  Enums:
    CategoryValueValuesEnum: Required. The category for this setting.
    ThresholdValueValuesEnum: Required. Controls the probability threshold at
      which harm is blocked.

  Fields:
    category: Required. The category for this setting.
    threshold: Required. Controls the probability threshold at which harm is
      blocked.
  """

  class CategoryValueValuesEnum(_messages.Enum):
    r"""Required. The category for this setting.

    Values:
      HARM_CATEGORY_UNSPECIFIED: The harm category is unspecified.
      HARM_CATEGORY_HATE_SPEECH: The harm category is hate speech.
      HARM_CATEGORY_DANGEROUS_CONTENT: The harm category is dangerous content.
      HARM_CATEGORY_HARASSMENT: The harm category is harassment.
      HARM_CATEGORY_SEXUALLY_EXPLICIT: The harm category is sexually explicit
        content.
    """
    HARM_CATEGORY_UNSPECIFIED = 0
    HARM_CATEGORY_HATE_SPEECH = 1
    HARM_CATEGORY_DANGEROUS_CONTENT = 2
    HARM_CATEGORY_HARASSMENT = 3
    HARM_CATEGORY_SEXUALLY_EXPLICIT = 4

  class ThresholdValueValuesEnum(_messages.Enum):
    r"""Required. Controls the probability threshold at which harm is blocked.

    Values:
      HARM_BLOCK_THRESHOLD_UNSPECIFIED: Threshold is unspecified.
      BLOCK_LOW_AND_ABOVE: Content with NEGLIGIBLE will be allowed.
      BLOCK_MEDIUM_AND_ABOVE: Content with NEGLIGIBLE and LOW will be allowed.
      BLOCK_ONLY_HIGH: Content with NEGLIGIBLE, LOW, and MEDIUM will be
        allowed.
      BLOCK_NONE: All content will be allowed.
      OFF: Turn off the safety filter.
    """
    HARM_BLOCK_THRESHOLD_UNSPECIFIED = 0
    BLOCK_LOW_AND_ABOVE = 1
    BLOCK_MEDIUM_AND_ABOVE = 2
    BLOCK_ONLY_HIGH = 3
    BLOCK_NONE = 4
    OFF = 5

  category = _messages.EnumField('CategoryValueValuesEnum', 1)
  threshold = _messages.EnumField('ThresholdValueValuesEnum', 2)


class SearchEntryPoint(_messages.Message):
  r"""Google search entry point.

  Fields:
    renderedContent: Optional. Web content snippet that can be embedded in a
      web page or an app webview.
    sdkBlob: Optional. Base64 encoded JSON representing array of tuple.
  """

  renderedContent = _messages.StringField(1)
  sdkBlob = _messages.BytesField(2)


class SeclmProjectsLocationsGetRequest(_messages.Message):
  r"""A SeclmProjectsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class SeclmProjectsLocationsListRequest(_messages.Message):
  r"""A SeclmProjectsLocationsListRequest object.

  Fields:
    extraLocationTypes: Optional. A list of extra location types that should
      be used as conditions for controlling the visibility of the locations.
    filter: A filter to narrow down results to a preferred subset. The
      filtering language accepts strings like `"displayName=tokyo"`, and is
      documented in more detail in [AIP-160](https://google.aip.dev/160).
    name: The resource that owns the locations collection, if applicable.
    pageSize: The maximum number of results to return. If not set, the service
      selects a default.
    pageToken: A page token received from the `next_page_token` field in the
      response. Send that page token to receive the subsequent page.
  """

  extraLocationTypes = _messages.StringField(1, repeated=True)
  filter = _messages.StringField(2)
  name = _messages.StringField(3, required=True)
  pageSize = _messages.IntegerField(4, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(5)


class SeclmProjectsLocationsOperationsCancelRequest(_messages.Message):
  r"""A SeclmProjectsLocationsOperationsCancelRequest object.

  Fields:
    cancelOperationRequest: A CancelOperationRequest resource to be passed as
      the request body.
    name: The name of the operation resource to be cancelled.
  """

  cancelOperationRequest = _messages.MessageField('CancelOperationRequest', 1)
  name = _messages.StringField(2, required=True)


class SeclmProjectsLocationsOperationsDeleteRequest(_messages.Message):
  r"""A SeclmProjectsLocationsOperationsDeleteRequest object.

  Fields:
    name: The name of the operation resource to be deleted.
  """

  name = _messages.StringField(1, required=True)


class SeclmProjectsLocationsOperationsGetRequest(_messages.Message):
  r"""A SeclmProjectsLocationsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class SeclmProjectsLocationsOperationsListRequest(_messages.Message):
  r"""A SeclmProjectsLocationsOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class SeclmProjectsLocationsWorkbenchesCreateRequest(_messages.Message):
  r"""A SeclmProjectsLocationsWorkbenchesCreateRequest object.

  Fields:
    parent: Required. Value for parent.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
    workbench: A Workbench resource to be passed as the request body.
    workbenchId: Required. Id of the requesting object. If auto-generating Id
      server-side, remove this field and workbench_id from the
      method_signature of Create RPC.
  """

  parent = _messages.StringField(1, required=True)
  requestId = _messages.StringField(2)
  workbench = _messages.MessageField('Workbench', 3)
  workbenchId = _messages.StringField(4)


class SeclmProjectsLocationsWorkbenchesDeleteRequest(_messages.Message):
  r"""A SeclmProjectsLocationsWorkbenchesDeleteRequest object.

  Fields:
    name: Required. Name of the resource.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes after the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
  """

  name = _messages.StringField(1, required=True)
  requestId = _messages.StringField(2)


class SeclmProjectsLocationsWorkbenchesGetRequest(_messages.Message):
  r"""A SeclmProjectsLocationsWorkbenchesGetRequest object.

  Fields:
    name: Required. Name of the resource.
  """

  name = _messages.StringField(1, required=True)


class SeclmProjectsLocationsWorkbenchesListRequest(_messages.Message):
  r"""A SeclmProjectsLocationsWorkbenchesListRequest object.

  Fields:
    filter: Optional. String for filtering results.
    orderBy: Optional. Hint for how to order the results.
    pageSize: Optional. Requested page size. Server may return fewer items
      than requested. If unspecified, server will pick an appropriate default.
    pageToken: Optional. A token identifying a page of results the server
      should return.
    parent: Required. Parent value for ListWorkbenchesRequest.
  """

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)


class SeclmProjectsLocationsWorkbenchesPatchRequest(_messages.Message):
  r"""A SeclmProjectsLocationsWorkbenchesPatchRequest object.

  Fields:
    name: Identifier. Name of resource.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
    updateMask: Optional. Field mask is used to specify the fields to be
      overwritten in the Workbench resource by the update. The fields
      specified in the update_mask are relative to the resource, not the full
      request. A field will be overwritten if it is in the mask. If the user
      does not provide a mask then all fields will be overwritten.
    workbench: A Workbench resource to be passed as the request body.
  """

  name = _messages.StringField(1, required=True)
  requestId = _messages.StringField(2)
  updateMask = _messages.StringField(3)
  workbench = _messages.MessageField('Workbench', 4)


class SeclmProjectsLocationsWorkbenchesQueryRequest(_messages.Message):
  r"""A SeclmProjectsLocationsWorkbenchesQueryRequest object.

  Fields:
    name: Required. Name of the resource.
    workbenchQueryRequest: A WorkbenchQueryRequest resource to be passed as
      the request body.
  """

  name = _messages.StringField(1, required=True)
  workbenchQueryRequest = _messages.MessageField('WorkbenchQueryRequest', 2)


class Segment(_messages.Message):
  r"""Segment of the content.

  Fields:
    endIndex: Output only. End index in the given Part, measured in bytes.
      Offset from the start of the Part, exclusive, starting at zero.
    partIndex: Output only. The index of a Part object within its parent
      Content object.
    startIndex: Output only. Start index in the given Part, measured in bytes.
      Offset from the start of the Part, inclusive, starting at zero.
    text: Output only. The text corresponding to the segment from the
      response.
  """

  endIndex = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  partIndex = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  startIndex = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  text = _messages.StringField(4)


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


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details. You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details. There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class Web(_messages.Message):
  r"""Chunk from the web.

  Fields:
    title: Title of the chunk.
    uri: URI reference of the chunk.
  """

  title = _messages.StringField(1)
  uri = _messages.StringField(2)


class Workbench(_messages.Message):
  r"""Message describing Workbench object.

  Messages:
    LabelsValue: Optional. Labels as key value pairs.

  Fields:
    createTime: Output only. Create time stamp.
    labels: Optional. Labels as key value pairs.
    name: Identifier. Name of resource.
    updateTime: Output only. Update time stamp.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Optional. Labels as key value pairs.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  createTime = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  name = _messages.StringField(3)
  updateTime = _messages.StringField(4)


class WorkbenchQueryRequest(_messages.Message):
  r"""Message for querying a Workbench.

  Fields:
    contents: Optional. The content of the current conversation with the
      model. For single-turn queries, this is a single instance. For multi-
      turn queries, this is a repeated field that contains conversation
      history + latest request.
    safetySettings: Optional. Per request settings for blocking unsafe
      content. Enforced on GenerateContentResponse.candidates.
  """

  contents = _messages.MessageField('Content', 1, repeated=True)
  safetySettings = _messages.MessageField('SafetySetting', 2, repeated=True)


class WorkbenchQueryResponse(_messages.Message):
  r"""Response to querying a Workbench.

  Fields:
    candidates: Output only. Candidate responses from the model.
  """

  candidates = _messages.MessageField('Candidate', 1, repeated=True)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')

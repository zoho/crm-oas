# POST /{moduleApiName}/{recordId}/actions/get_related_records_count
**Operation:** `getRelatedRecordsCount` — Get related records count
> To retrieve the count of related records for a specified parent record in your Zoho CRM organization. Supports optional filtering by approval status, conversion status, category type, and field-level equality criteria. A single request can include up to 20 related list count specifications. You can use this API to get the count of records in the following types of related lists:

- **System-defined related lists**, such as:
  - Survey
  - Desk
  - Projects
  - Visits
  - Expense
  - Invoice
  - Subscription
- **Custom related lists** created via Lookup fields.
- **Custom related lists** created via Multi-select Lookup fields.
- **Custom related lists** created via Multi-module Lookup fields.
- **Related lists** created when history tracking is enabled for a picklist field.

**Parameters:**
- `moduleApiName` (path, string, required) [maxLen=100, minLen=1, pattern=^[A-Za-z0-9_]+$]: Specify the API name of the CRM module that contains the parent record. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module API name and its unique ID.
- `recordId` (path, string, required) [maxLen=50, minLen=1, pattern=^[0-9a-fA-F-]+$]: Specify the unique ID of the parent record for which you want to count related records. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the record ID.

**Schemas:**
`ErrorDetailsAmbiguity`:
  > Error details containing information about ambiguous fields that caused processing conflict
  - `ambiguity_due_to` (array of object) [minItems=2, maxItems=2] **REQ** — List of conflicting fields that caused the ambiguity (id and api_name)
    - `api_name` (string) **REQ** [maxLen=100] — The API name of the ambiguous field
    - `json_path` (string) **REQ** [maxLen=500] — JSON path indicating the location of the ambiguous field in the request
`ErrorDetailsExpectedFields`:
  > Error details containing list of expected fields that are missing
  - `expected_fields` (array of object) [minItems=1, maxItems=20] **REQ** — List of field names that were expected but not provided
    - `api_name` (string) **REQ** [maxLen=100] — API name of the expected field
    - `json_path` (string) **REQ** [maxLen=500] — JSON path indicating where the field was expected in the request
`ErrorDetailsFieldInfo`:
  > Error details with field information, used for field-level validation errors
  - `api_name` (string) **REQ** [maxLen=100] — The API name of the field that caused the error
  - `json_path` (string) **REQ** [maxLen=500] — JSON path indicating the location of the field in the request
`ErrorDetailsNotSupportedFilters`:
  > Error details for unsupported filters, containing the expected data type and field information
  - `expected_data_type` (string) **REQ** [enum=['json_type']] — The expected data type for the field
  - `api_name` (string) **REQ** [maxLen=100] — The API name of the field that is not supported
  - `json_path` (string) **REQ** [maxLen=500] — JSON path indicating the location of the unsupported field in the request
`ErrorDetailsResourcePathIndex`:
  > Error details containing resource path index information
  - `resource_path_index` (integer/int32) **REQ** [min=0] — The index of the resource path segment that is invalid
`RelatedListReference`:
  > Represents a related list identified by its API name and unique ID. Used in both the request to specify the target related list and in the response to echo the queried related list.
  - `api_name` (string) **REQ** [maxLen=100, minLen=1, pattern=^[A-Za-z0-9_]+$] — Represents the API name of the related list.
  - `id` (string/int64) **REQ** [maxLen=20, minLen=1, pattern=^[0-9]+$] — Represents the unique ID of the related list.  Use the  [Get Related Records API](related_records.yaml#$.paths./{parentRecordModule}/{parentRecord}/{relatedList}.get) to get the ID of the related list in the key ID.
`RelatedRecordCountResult`:
  > Represents the count result for a specific related list, including the total number of matching records and the related list identifier.
  - `count` (integer/int32) **REQ** [min=0] — Represents the total number of related records matching the specified criteria.
  - `related_list` (object `RelatedListReference`) **REQ** — Represents a related list identified by its API name and unique ID. Used in both the request to specify the target related list and in the response to echo the queried related list.

**Request Body** (required) — application/json `GetRelatedRecordsCountRequest`
> The request body must contain a **get_related_records_count** array. You can include a maximum of 20 objects per request. Use the [Get Related Records API](related_records.yaml#$.paths./{parentRecordModule}/{parentRecord}/{relatedList}.get) to get the ID of the related list in the key ID.
  > Represents the request payload for counting related records. Contains an array of related list count specifications, each identifying a related list and optional filtering criteria.
  - `get_related_records_count` (array of object `RelatedRecordCountItem`) [minItems=1, maxItems=20] **REQ** — Represents the array of related list count request objects. Each object specifies a related list to query and optional filtering criteria to apply before counting.
    schema: `RelatedRecordCountItem`
    - `related_list` (object `RelatedListReference`) **REQ** — Represents a related list identified by its API name and unique ID. Used in both the request to specify the target related list and in the response to echo the queried related list.
    - `params` (object `CountParameters`) — Represents optional filtering and selection parameters applied to related records before counting. Includes support for approval status, conversion status, category type, and field-level equality filters.
      schema: `CountParameters`
      - `approved` (boolean) — Indicates whether to restrict the count to approved records only.
Possible values:
**true** - Count only approved records.
**false** - Count only records that are not approved.
      - `filters` (object `FilterCriteria`) **REQ** — Represents the field-based filter criteria applied to related records before counting. Contains the field to evaluate, the comparison operator, and the value to compare against.
        schema: `FilterCriteria`
        - `comparator` (string) **REQ** [enum=['equal']] — Represents the comparison operator used to filter related records before counting.
Possible values:
**equal** - Matches records where the specified field value equals the given value.
        - `field` (object `FilterField`) **REQ** — Represents the field to use when filtering related records before counting.
          schema: `FilterField`
          - `api_name` (string) **REQ** [maxLen=100, minLen=1, pattern=^[A-Za-z0-9_]+$] — Represents the API name of the field to filter on when counting related records.
        - `value` (string) **REQ** [maxLen=255, minLen=1] — Represents the value to compare the specified field against when filtering related records before counting.
      - `converted` (boolean) — Indicates whether to restrict the count to converted records only. Applicable to the Leads module.
Possible values:
**true** - Count only converted records.
**false** - Count only records that have not been converted.
      - `category` (string) [enum=['link', 'files']] — Represents the category type used to filter related records before counting.
Possible values:
**link** - Count only link-type related records.
**files** - Count only file-attachment related records.
      - `approval_state` (string) [enum=['approved']] — Represents the approval workflow state used to filter related records before counting.
Possible values:
**approved** - Count only records in the approved workflow state.

**Responses:**

- **200**: Returns an array of count results for the requested related lists, each containing the count of matching records and the related list identifier. — Schema: `GetRelatedRecordsCountResponse` [application/json]
    > Represents the response returned when the count operation succeeds. Contains an array of count results, one entry for each related list requested.
    schema: `GetRelatedRecordsCountResponse`
    - `get_related_records_count` (array of object `RelatedRecordCountResult`) [maxItems=20] **REQ** — Represents the array of count results, one entry for each related list requested.

- **207**: Multi-Status. Returned when the request contains multiple related list count items where some succeed and others fail (partial success). Each item in the get_related_records_count array independently reports either a successful count or an error. [application/json]
    oneOf:
      - `PartialSuccessResponse` — Multi-Status (HTTP 207) response returned when a request containing multiple related list count items has mixed results - some items succeed with a count while others fail with a per-item error. Each entry in get_related_records_count corresponds positionally to a requested item and independently reports either success (count + related_list) or an error (status, code, message, details).
        - `get_related_records_count` (array of object `PartialSuccessResponseItem`) [minItems=1, maxItems=20] **REQ** — Array of per-item results, one entry per requested related list. Each entry is either a RelatedRecordCountResult (success) or a PartialSuccessItemError (failure).
          oneOf:
            - `RelatedRecordCountResult` — Represents the count result for a specific related list, including the total number of matching records and the related list identifier.
            - `PartialSuccessItemError` — Per-item error entry inside the get_related_records_count array of a partial-success (HTTP 207) response. Indicates that this particular related list count request failed while other items in the same array may have succeeded.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
Possible values:
**error** - The request was unsuccessful.
              - `code` (string) **REQ** [enum=[4 values]] — Error code identifying the failure reason for this item
              - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the validation failure.
              - `details` (object) **REQ** — Additional context about the per-item error (field info, expected fields, ambiguity info, or unsupported-filter info depending on the error code)
                oneOf:
                  - `ErrorDetailsFieldInfo` — Error details with field information, used for field-level validation errors
                  - `ErrorDetailsExpectedFields` — Error details containing list of expected fields that are missing
                  - `ErrorDetailsAmbiguity` — Error details containing information about ambiguous fields that caused processing conflict
                  - `ErrorDetailsNotSupportedFilters` — Error details for unsupported filters, containing the expected data type and field information
                  - `ErrorDetailsEmpty` (object) — Empty error details object for errors that don't require additional context
      - `PartialSuccessMandatoryNotFoundResponse` — Multi-Status (HTTP 207) response returned when a request contains multiple related list count items where some succeed and others fail because a required field (such as related_list) is missing. Each entry in get_related_records_count corresponds positionally to a requested item and independently reports either success (count + related_list) or a MANDATORY_NOT_FOUND error (status, code, message, details).
        - `get_related_records_count` (array of object `PartialSuccessMandatoryNotFoundResponseItem`) [minItems=1, maxItems=20] **REQ** — Array of per-item results, one entry per requested related list. Each entry is either a RelatedRecordCountResult (success) or a PartialSuccessMandatoryNotFoundItemError (failure).
          oneOf:
            - `RelatedRecordCountResult` — Represents the count result for a specific related list, including the total number of matching records and the related list identifier.
            - `PartialSuccessMandatoryNotFoundItemError` — Per-item MANDATORY_NOT_FOUND error entry inside the get_related_records_count array of a partial-success (HTTP 207) response. Indicates that a required field (such as related_list) was missing from this particular request item.
              - `status` (string) **REQ** [enum=['error']] — The status of this item, always 'error' for failed items
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code for missing mandatory field
              - `message` (string) **REQ** [enum=['required field not found']] — Human-readable error message describing the missing mandatory field
              - `details` (object `ErrorDetailsFieldInfo`) **REQ** — Error details with field information, used for field-level validation errors

- **400**: The request contains invalid, missing, or unsupported data.
**Resolution:** The error code and details in the response body identify the specific validation failure. The request must be corrected before retrying. [application/json]
    oneOf:
      - `InvalidDataError` — Error response for invalid data in request (record ID, related list ID, or field values). Response is wrapped in get_related_records_count array.
        - `get_related_records_count` (array of object) [minItems=1, maxItems=1] **REQ** — Array containing the error details for invalid data
          - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code for invalid data
          - `message` (string) **REQ** [enum=['Given related_list is invalid']] — Human-readable error message describing the invalid data error
          - `details` (object `ErrorDetailsFieldInfo`) **REQ** — Error details with field information, used for field-level validation errors
      - `InvalidDataRecordIdError` — Flat error response for invalid record ID in URL path. Unlike other INVALID_DATA errors, this is not wrapped in the get_related_records_count array because the error relates to the URL path parameter rather than a request body field.
        - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code for invalid data
        - `message` (string) **REQ** [maxLen=500] — Human-readable error message describing the invalid record ID validation failure.
        - `details` (object `ErrorDetailsResourcePathIndex`) **REQ** — Error details containing resource path index information
      - `MandatoryNotFoundError` — Error response for missing mandatory fields in request. Response is wrapped in get_related_records_count array.
        - `get_related_records_count` (array of object) [minItems=1, maxItems=1] **REQ** — Array containing the error details for missing mandatory field
          - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code for missing mandatory field
          - `message` (string) **REQ** [enum=['required field not found']] — Human-readable error message describing the missing mandatory field
          - `details` (object `ErrorDetailsFieldInfo`) **REQ** — Error details with field information, used for field-level validation errors
      - `InvalidModuleError` — Error response for invalid module API name in request URL
        - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code for invalid module
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Human-readable error message describing the invalid module error
        - `details` (object `ErrorDetailsResourcePathIndex`) **REQ** — Error details containing resource path index information
      - `ExpectedFieldMissingError` — Error response for missing expected fields (id or api_name). Response is wrapped in get_related_records_count array.
        - `get_related_records_count` (array of object) [minItems=1, maxItems=1] **REQ** — Array containing the error details for missing expected fields
          - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
          - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Error code for missing expected field
          - `message` (string) **REQ** [enum=['Specify atleast one field']] — Human-readable error message describing the missing expected fields
          - `details` (object `ErrorDetailsExpectedFields`) **REQ** — Error details containing list of expected fields that are missing
      - `AmbiguityDuringProcessingError` — Error response for ambiguous data (ID and API name mismatch). Response is wrapped in get_related_records_count array.
        - `get_related_records_count` (array of object) [minItems=1, maxItems=1] **REQ** — Array containing the error details for ambiguous data
          - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
          - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Error code for ambiguous processing
          - `message` (string) **REQ** [enum=['Ambiguity while processing the request']] — Human-readable error message describing the ambiguity error
          - `details` (object `ErrorDetailsAmbiguity`) **REQ** — Error details containing information about ambiguous fields that caused processing conflict
      - `NotSupportedFiltersError` — Error response when filters are not supported for the specified module's related list. Response is wrapped in get_related_records_count array.
        - `get_related_records_count` (array of object) [minItems=1, maxItems=1] **REQ** — Array containing the error details for unsupported filters
          - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
          - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Error code for unsupported operation
          - `message` (string) **REQ** [enum=['Filters are not supported for this modules']] — Human-readable error message describing the unsupported filters
          - `details` (object `ErrorDetailsNotSupportedFilters`) **REQ** — Error details for unsupported filters, containing the expected data type and field information
      - `NotSupportedRelatedListError` — Error response when the given related list ID is not supported in API. Response is wrapped in get_related_records_count array.
        - `get_related_records_count` (array of object) [minItems=1, maxItems=1] **REQ** — Array containing the error details for unsupported related list
          - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
          - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Error code for unsupported related list
          - `message` (string) **REQ** [enum=['The given related list id is not supported in api']] — Human-readable error message describing the unsupported related list
          - `details` (object) **REQ** — Empty error details object for errors that don't require additional context
      - `AuthorizationFailedError` — Error response for insufficient permissions to perform the operation
        - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
        - `code` (string) **REQ** [enum=['AUTHORIZATION_FAILED']] — Error code for authorization failure
        - `message` (string) **REQ** [enum=['You do not have sufficient permission to read the module records']] — Human-readable error message describing the authorization failure
        - `details` (object) **REQ** — Empty error details object for errors that don't require additional context
      - `InvalidRequestMethodError` — Error response for incorrect HTTP request method
        - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Error code for invalid request method
        - `message` (string) **REQ** [enum=['The http request method type is not a valid one']] — Human-readable error message describing the invalid request method error
        - `details` (object) **REQ** — Empty error details object for errors that don't require additional context
      - `InvalidRequestError` — Error response for invalid request
        - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
        - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Error code for invalid request
        - `message` (string) **REQ** [enum=[1 values]] — Human-readable error message describing the invalid request error
        - `details` (object) **REQ** — Empty error details object for errors that don't require additional context

- **401**: Unauthorized. Authentication failed due to invalid, expired, or missing access token, or the token lacks required OAuth scopes. [application/json]
    oneOf:
      - `AuthenticationFailureError` — Error response for authentication failure
        - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
        - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Error code for authentication failure
        - `message` (string) **REQ** [enum=['Authentication failed']] — Human-readable error message describing the authentication failure
        - `details` (object) **REQ** — Empty error details object for errors that don't require additional context
      - `InvalidTokenError` — Error response for invalid or expired access token
        - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
        - `code` (string) **REQ** [enum=['INVALID_TOKEN']] — Error code for invalid token
        - `message` (string) **REQ** [enum=['Invalid API token']] — Human-readable error message describing the invalid token error
        - `details` (object) **REQ** — Empty error details object for errors that don't require additional context
      - `OAuthScopeMismatchError` — Error response for OAuth scope mismatch
        - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Error code for OAuth scope mismatch
        - `message` (string) **REQ** [enum=['The access token does not have the required scope']] — Human-readable error message describing the scope mismatch error
        - `details` (object) **REQ** — Empty error details object for errors that don't require additional context

- **403**: Forbidden. You do not have permission to perform this operation, either due to insufficient user privileges or organizational restrictions. [application/json]
    oneOf:
      - `NoPermissionError` — Error response for no permission to read records from the module
        - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code for no permission
        - `message` (string) **REQ** [enum=['You do not have permission to read records from the module']] — Human-readable error message describing the permission error
        - `details` (object) **REQ** — Empty error details object for errors that don't require additional context
      - `NotAllowedError` — Error response for not allowed to read related records from the module
        - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code for not allowed operation
        - `message` (string) **REQ** [enum=['You do not have permission to read related records from the module']] — Human-readable error message describing the not allowed error
        - `details` (object) **REQ** — Empty error details object for errors that don't require additional context

- **404**: Not Found. The requested URL pattern is incorrect or the resource does not exist. — Schema: `InvalidUrlPatternError` [application/json]
    > Error response for invalid URL pattern
    schema: `InvalidUrlPatternError`
    - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Error code for invalid URL pattern
    - `message` (string) **REQ** [enum=['The request URL is incorrect. Please check the URL']] — Human-readable error message describing the invalid URL pattern error
    - `details` (object) **REQ** — Empty error details object for errors that don't require additional context

- **500**: Internal Server Error. Unexpected and unhandled exception in the server. Contact support if the error persists. — Schema: `InternalError` [application/json]
    > Error response for internal server error
    schema: `InternalError`
    - `status` (string) **REQ** [enum=['error']] — The status of the response, always 'error' for error responses
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Error code for internal server error
    - `message` (string) **REQ** [enum=['Internal Server Error']] — Human-readable error message describing the internal error
    - `details` (object) **REQ** — Empty error details object for errors that don't require additional context

**Scopes:** ZohoCRM.modules.READ

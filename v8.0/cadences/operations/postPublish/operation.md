# POST /settings/automation/cadences/{id}/actions/publish
**Operation:** `postPublish` — Publish a Cadence
> Publishes a draft cadence by merging its follow-up tree, transitions, and triggers into the live cadence, and then clears the draft. If the cadence is being published for the first time, it is promoted from a draft to an inactive published cadence. Call the Activate Cadence API separately to begin enrolling records. Before publishing, ensure the cadence contains at least one follow-up and complies with the action count and active cadence limits. When the enrollment type is `custom_view`, the `process_existing_records` parameter determines whether records that already match the custom view are enrolled at the time of publication.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: Specify the unique identifier of the Cadence to publish.

**Schemas:**
`AllErrorResponse`:
  > Represents the error response returned when the API request fails due to validation errors or unsupported operations.
  - `code` (string) **REQ** [enum=[18 values]] — Represents a machine-readable error code; branch on this value, not on message.
  - `message` (string/error message) **REQ** — Represents the error message describing the validation failure.
  - `status` (string) **REQ** [const=error] — Represents the status of the API response.
  - `details` (object) **REQ** — Represents additional details providing context about the error.
    oneOf:
      - `ExpectedFieldMissingDetails` — Represents error details when expected fields are missing from the request.
      - `ExpectedDependentFieldMissingDetails` — Represents error details when expected dependent fields are missing from the request.
      - `InvalidDataWithId` — Represents error details when a field contains an invalid identifier.
      - `InvalidDataWithSupportedValues` — Represents error details when a field contains an invalid value, listing the supported values.
      - `InvalidDataWithDataType` — Represents error details when a field contains invalid data, specifying the expected data type.
      - `InvalidDataWithDataTypeAndSupportedValues` — Represents error details when a field contains invalid data, specifying the expected data type and supported values.
      - `MandatoryInvalidDataCommonApiNameJsonPath` — Represents error details when a mandatory field contains invalid data.
      - `DependentMismatchDetails` — Represents error details when a dependent field value does not match the expected values based on the parent field.
      - `DependencyFieldMissingDetails` — Represents error details when a required dependency field is missing from the request.
      - `ResourcePathIndex` — Represents error details containing the resource path index where the validation error occurred.
      - `IdDetails` — Represents error details containing the unique identifier of the resource associated with the error.
      - `ParamNameDetails` — Represents error details containing the parameter name associated with the error.
      - `ParamNameWithEnumDetails` — Represents error details containing the parameter name associated with the error.
      - `ApiNameLimit` — Represents error details when a field exceeds its maximum allowed count.
      - `DetailsPermission` — Represents error details when the request fails due to missing permissions.
      - `EmptyDetails` (object) — Represents an empty error details object with no additional information.
      - `ApiNameLimitJsonPath` — Represents error details when a field at a specific JSON path exceeds its maximum allowed count.
      - `AmbiguityDetails` — Represents error details for ambiguity, listing the fields that caused the ambiguity.
      - `ApiNameExistsInJsonPath` — Represents error details when an API name already exists at the specified JSON path.
      - `MaximumLengthApiNameJsonPath` — Represents error details when a field value exceeds the maximum allowed length.
`AmbiguityDetails`:
  > Represents error details for ambiguity, listing the fields that caused the ambiguity.
  - `ambiguity_due_to` (array of object) [maxItems=100] **REQ** — Represents the list of fields that caused the ambiguity during processing.
    - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the ambiguity.
    - `json_path` (string) [maxLen=255] — Represents the JSON path of the field that caused the ambiguity.
`ApiNameExistsInJsonPath`:
  > Represents error details when an API name already exists at the specified JSON path.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that already exists in the specified JSON path.
  - `exists_in` (object) **REQ** — Represents the location where the API name already exists, identified by its API name and JSON path.
    - `api_name` (string) [maxLen=255] — Represents the API name at the existing location.
    - `json_path` (string) [maxLen=500] — Represents the JSON path of the existing field location.
  - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the duplicate field in the request payload.
`ApiNameLimit`:
  > Represents error details when a field exceeds its maximum allowed count.
  - `api_name` (string) [maxLen=255] — Represents the API name of the field that exceeded the limit.
  - `limit` (integer/int32) **REQ** — Represents the maximum allowed count for the field.
`ApiNameLimitJsonPath`:
  > Represents error details when a field at a specific JSON path exceeds its maximum allowed count.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that exceeded the limit.
  - `limit` (integer/int32) **REQ** — Represents the maximum allowed count for the field.
  - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field that exceeded the limit.
`DependencyFieldMissingDetails`:
  > Represents error details when a required dependency field is missing from the request.
  - `dependee` (object) **REQ** — Represents the dependee field that is required but missing from the request.
    - `api_name` (string) [maxLen=255] — Represents the API name of the dependee field.
    - `json_path` (string) [maxLen=500] — Represents the JSON path of the dependee field.
    - `param_name` (string) [maxLen=255] — Represents the parameter name of the dependee field.
  - `api_name` (string) [maxLen=255] — Represents the API name of the field with the missing dependency.
  - `json_path` (string) [maxLen=500] — Represents the JSON path of the field with the missing dependency.
  - `param_name` (string) [maxLen=255] — Represents the parameter name associated with the field.
`DependentMismatchDetails`:
  - `dependee` (object) **REQ** — Represents the dependee field associated with the mismatch.
  - `api_name` (string) [maxLen=255] — Represents the API name of the field with the dependency mismatch.
  - `json_path` (string) [maxLen=500] — Represents the JSON path of the field with the dependency mismatch.
  - `expected_data_type` (string) [maxLen=255] — Represents the data type the server expected for the dependent field based on the parent field's value.
  - `supported_values` (array) [maxItems=25] — Represents the list of supported values for the dependee field.
  - `param_name` (string) [maxLen=255] — Represents the parameter name associated with the field.
  oneOf:
      - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of allowed values for the dependent field given the parent field's current value.
        items: [maxLen=500]
      - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type expected for the dependent field given the parent field's current value.
`DetailsPermission`:
  > Represents error details when the request fails due to missing permissions.
  - `permissions` (array of string) [maxItems=25] **REQ** — Represents the list of required permissions that are missing.
    items: [maxLen=255]
`ExpectedDependentFieldMissingDetails`:
  > Represents error details when expected dependent fields are missing from the request.
  - `dependee` (object) **REQ** — Represents the expected dependent field that is missing from the request.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the expected dependent field.
    - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the expected dependent field.
  - `expected_fields` (array of object) [maxItems=25] **REQ** — Represents the list of expected fields that are missing from the request.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing expected field.
    - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the missing expected field.
`ExpectedFieldMissingDetails`:
  > Represents error details when expected fields are missing from the request.
  - `expected_fields` (array of object) [maxItems=25] **REQ** — Represents the list of expected fields that are missing from the request.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing expected field.
    - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the missing expected field.
`IdDetails`:
  > Represents error details containing the unique identifier of the resource associated with the error.
  - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the resource.
`InvalidDataWithDataType`:
  > Represents error details when a field contains invalid data, specifying the expected data type.
  - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type for the field.
  - `api_name` (string) [maxLen=255] — Represents the API name of the field with invalid data.
  - `json_path` (string) [maxLen=500] — Represents the JSON path of the field with invalid data.
  - `param_name` (string) [maxLen=255] — Represents the parameter name of the field with invalid data.
`InvalidDataWithDataTypeAndSupportedValues`:
  > Represents error details when a field contains invalid data, specifying the expected data type and supported values.
  - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type for the field.
  - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of supported values for the field.
    items: [maxLen=500]
  - `api_name` (string) [maxLen=255] — Represents the API name of the field with invalid data.
  - `json_path` (string) [maxLen=500] — Represents the JSON path of the field with invalid data.
  - `param_name` (string) [maxLen=255] — Represents the parameter name of the field with invalid data.
`InvalidDataWithId`:
  > Represents error details when a field contains an invalid identifier.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field with invalid data.
  - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field with invalid data.
  - `id` (string) **REQ** [maxLen=255] — Represents the identifier of the invalid value provided.
`InvalidDataWithSupportedValues`:
  > Represents error details when a field contains an invalid value, listing the supported values.
  - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of supported values for the field.
    items: [maxLen=500]
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field with invalid data.
  - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field with invalid data.
  - `param_name` (string) [maxLen=255] — Represents the parameter name of the field with invalid data.
`MandatoryInvalidDataCommonApiNameJsonPath`:
  > Represents error details when a mandatory field contains invalid data.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the mandatory field with invalid data.
  - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the mandatory field with invalid data.
  - `param_name` (string) [maxLen=255] — Represents the parameter name of the mandatory field with invalid data.
`MaximumLengthApiNameJsonPath`:
  > Represents error details when a field value exceeds the maximum allowed length.
  - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the field.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that exceeded the maximum length.
  - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field that exceeded the maximum length.
`ParamNameDetails`:
  > Represents error details containing the parameter name associated with the error.
  - `param_name` (string) **REQ** [maxLen=255] — Represents the parameter name associated with the error detail.
`ParamNameWithEnumDetails`:
  > Represents error details containing the parameter name associated with the error.
  - `param_name` (string) **REQ** [maxLen=255, enum=['ids']] — Represents the parameter name associated with the error detail.
Possible values:
ids - The ids query parameter.
`ResourcePathIndex`:
  > Represents error details containing the resource path index where the validation error occurred.
  - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path where the validation error occurred.

**Request Body** — application/json `PutpublishRequest`
> The request body must contain a Cadences array with the publishing configuration for each Cadence.
  > Represents the request body schema for publishing one or more Cadences.
  - `cadences` (array of object) [maxItems=1] **REQ** — Represents the list of Cadences to publish.
    - `process_existing_records` (boolean) — Represents whether existing records should be enrolled in the Cadence upon publication.

**Responses:**

- **200**: Returns a success response confirming the Cadence was published. — Schema: `SuccessResponse200` [application/json]
    > Represents the success response returned after a Cadence operation is completed successfully.
    schema: `SuccessResponse200`
    - `cadences` (array of object `CadencesItemNested`) [maxItems=100] — Represents the list of Cadences with their result status from the operation.
      schema: `CadencesItemNested`
      - `code` (string) [maxLen=255] — Represents the result code for the individual Cadence record operation.
      - `details` (object `DetailsNested`) — Represents the nested details of a Cadence operation result, including follow-up actions and resource identifiers.
        schema: `DetailsNested`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the resource associated with the operation.
        - `follow_ups` (array of object) [maxItems=100, nullable] — Represents the list of follow-up actions involved in the operation.
          - `id` (string) [maxLen=255] — Represents the unique identifier of the follow-up item.
          - `action` (object) — Represents the action associated with the follow-up item.
            - `id` (string) [maxLen=255] — Represents the unique identifier of the follow-up action.
            - `type` (string) [maxLen=255] — Represents the type of the follow-up action.
        - `draft_cadence` (object) — Represents the draft version of the Cadence associated with the operation.
          - `id` (string) [maxLen=255] — Represents the unique identifier of the draft Cadence.
      - `message` (string) [maxLen=255] — Represents the result message for the individual Cadence record operation.
      - `status` (string) [maxLen=255] — Represents the result status for the individual Cadence record operation.

- **400**: Returned when the request contains invalid data, or when the
Cadence cannot be published due to its current state, edition restrictions,
limit violations, or unsupported configuration.\n**Resolution:** The Cadence
ID must be valid, at least one follow-up action must be configured, and
all publishing requirements must be met. [application/json]
    > Represents the error response for the Cadence publish operation, containing either a standard error or a per-Cadence error response.
    oneOf:
      - `AllErrorResponse` — Represents the error response returned when the API request fails due to validation errors or unsupported operations.
      - `ErrorResponseWithCadenceAsHead` — Represents an error response where the Cadence object serves as the top-level container for field-level errors.
        - `cadences` (array of object `AllErrorResponse`) [maxItems=300] — Represents the list of Cadences, each containing field-level error details for the corresponding request entry.

- **403**: The user does not have permission to publish Cadences.
**Resolution:** The CRM administrator must grant the required Cadence management permission to the user's profile, and a new access token must be generated with the required scope. — Schema: `AllErrorResponse` [application/json]
    > Represents the error response returned when the API request fails due to validation errors or unsupported operations.

**Scopes:** ZohoCRM.settings.cadences.CREATE

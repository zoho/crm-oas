# POST /settings/automation/cadences/{id}/actions/clone
**Operation:** `postCloneCadences` — Clone a Cadence
> Creates a new cadence with the same follow-up tree as the source cadence (identified by path id) but with the name / description / custom_view supplied in the body. Every follow-up action is copied into a new action record - the clone has no shared rows with the source. The new cadence starts in draft status and must be published before it can enroll records.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: Specify the unique identifier of the Cadence to clone.

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

**Request Body** — application/json `CadencesCloneRequestBody`
> The request body must contain a Cadences array with the configuration details for the cloned Cadence.
  > Represents the request body schema for cloning an existing Cadence.
  - `cadences` (array of object) [maxItems=1] **REQ** — Represents the list of Cadences to clone.
    - `module` (object `ModuleInformation`) **REQ** — Represents the API name and identifier of a CRM module.
      schema: `ModuleInformation`
      - `api_name` (string) [maxLen=255] — Represents the API name of the CRM module.
      - `id` (string/int64) [maxLen=255] — Represents the unique identifier of the CRM module.
    - `name` (string) **REQ** [maxLen=100] — Represents the name of the cloned Cadence.
    - `description` (string) [maxLen=500] — Represents the description of the cloned Cadence.
    - `type` (string) **REQ** [enum=['custom_view', 'manual_enrollment']] — Represents the enrollment type of the Cadence.
Possible values:
custom_view - Automatically enrolls records matching a Custom View.
manual_enrollment - Allows manual enrollment of records into the Cadence.
    - `custom_view` (object) — Represents the Custom View associated with the Cadence enrollment.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the Custom View.
    - `execution_details` (object) — Represents the execution frequency details for the Cadence.
      - `execute_every` (object `ExecuteEvery`) — Represents the recurring execution interval for a Cadence, specifying the frequency period and numeric value.
        schema: `ExecuteEvery`
        - `period` (string) **REQ** [enum=['immediately', 'hours', 'days', 'weeks']] — Represents the frequency interval for recurring Cadence execution.
Possible values:
immediately - Execute immediately after each enrollment trigger.
hours - Execute at the specified number of hours interval.
days - Execute at the specified number of days interval.
weeks - Execute at the specified number of weeks interval.
        - `unit` (integer/int32) [min=1, max=99] — Represents the numeric value of the execution interval, expressed in the specified period unit.

**Responses:**

- **201**: Returns the details of the newly cloned Cadence, including its unique identifier. — Schema: `SuccessResponse200` [application/json]
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

- **400**: The request contains invalid or missing data.
**Resolution:** All required fields must be included in the request body, field values must conform to the expected format, and the Cadence count limits must not be exceeded. [application/json]
    > Represents the error response for the Cadence clone operation.
    oneOf:
      - `ErrorResponseWithCadenceAsHead` — Represents an error response where the Cadence object serves as the top-level container for field-level errors.
        - `cadences` (array of object `AllErrorResponse`) [maxItems=300] — Represents the list of Cadences, each containing field-level error details for the corresponding request entry.
      - `AllErrorResponse` — Represents the error response returned when the API request fails due to validation errors or unsupported operations.

- **403**: The user does not have permission to clone Cadences.
**Resolution:** The CRM administrator must grant the required Cadence management permission to the user's profile, and a new access token must be generated with the required scope. — Schema: `AllErrorResponse` [application/json]
    > Represents the error response returned when the API request fails due to validation errors or unsupported operations.

**Scopes:** ZohoCRM.settings.cadences.CREATE

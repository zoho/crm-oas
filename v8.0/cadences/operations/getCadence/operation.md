# GET /settings/automation/cadences/{id}
**Operation:** `getCadence` — Get a Cadence
> To retrieve the configuration and details of a specific Cadence from your Zoho CRM organization. The response includes the follow-up action tree with server-resolved parent follow-up IDs, unenroll properties, Custom View configuration, and the current Cadence status.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: Specify the unique identifier of the Cadence.

**Responses:**

- **200**: Returns the details of the specified Cadence. — Schema: `GetByIdCadenceSuccessResp` [application/json]
    > Represents the response containing the details of a specific Cadence retrieved by its identifier.
    schema: `GetByIdCadenceSuccessResp`
    - `cadences` (array of object) [maxItems=1] — Represents the list of Cadences with their full details.
      - `summary` (object `FollowUpSummary`) — Represents a summary of follow-up action counts in a Cadence, broken down by action type.
        schema: `FollowUpSummary`
        - `whatsapp_follow_up_count` (integer/int32) — Represents the number of WhatsApp message follow-up actions in the Cadence.
        - `task_follow_up_count` (integer/int32) — Represents the number of task follow-up actions in the Cadence.
        - `call_follow_up_count` (integer/int32) — Represents the number of scheduled call follow-up actions in the Cadence.
        - `email_follow_up_count` (integer/int32) — Represents the number of email notification follow-up actions in the Cadence.
      - `created_time` (string/date-time) — Represents the creation date and time of the Cadence, in ISO 8601 format.
      - `module` (object `ModuleInformation`) **REQ** — Represents the API name and identifier of a CRM module.
        schema: `ModuleInformation`
        - `api_name` (string) [maxLen=255] — Represents the API name of the CRM module.
        - `id` (string/int64) [maxLen=255] — Represents the unique identifier of the CRM module.
      - `description` (string) [maxLen=500] — Represents the description text of a Cadence.
      - `execution_details` (object) — Represents the execution frequency and unenrollment configuration for the Cadence.
        - `unenroll_properties` (array of object) [maxItems=50, nullable] — Represents the list of conditions under which records are automatically unenrolled from the Cadence.
          - `details` (object) [nullable] — Represents additional details for the unenrollment condition.
          - `id` (string) [maxLen=255] — Represents the unique identifier of the unenrollment condition.
          - `type` (string) [maxLen=255] — Represents the type of unenrollment condition.
        - `execute_every` (object `ExecuteEvery`) — Represents the recurring execution interval for a Cadence, specifying the frequency period and numeric value.
          schema: `ExecuteEvery`
          - `period` (string) **REQ** [enum=['immediately', 'hours', 'days', 'weeks']] — Represents the frequency interval for recurring Cadence execution.
Possible values:
immediately - Execute immediately after each enrollment trigger.
hours - Execute at the specified number of hours interval.
days - Execute at the specified number of days interval.
weeks - Execute at the specified number of weeks interval.
          - `unit` (integer/int32) [min=1, max=99] — Represents the numeric value of the execution interval, expressed in the specified period unit.
      - `type` (string) **REQ** [maxLen=255, enum=['custom_view', 'manual_enrollment']] — Represents the enrollment type of a Cadence, indicating how records are enrolled.
      - `created_by` (object `CreatorInfo`) — Represents the identifier and name of the user who created the record.
        schema: `CreatorInfo`
        - `name` (string) [maxLen=255] — Represents the full name of the user who created the record.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the user who created the record.
      - `modified_time` (string) [maxLen=255, nullable] — Represents the date and time when the Cadence was last modified.
      - `modified_by` (object `ModifierInfo`) — Represents the identifier and name of the user who last modified the record.
        schema: `ModifierInfo`
        - `name` (string) [maxLen=255] — Represents the full name of the user who last modified the record.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the user who last modified the record.
      - `name` (string) **REQ** [maxLen=100] — Represents the name of a Cadence.
      - `follow_ups` (array of object) [maxItems=200] — Represents the list of follow-up steps configured in the Cadence.
        title: Follow-Up Details
        - `parent_follow_up` (object) **REQ** — Represents the parent follow-up step that this step branches from.
          - `id` (string) [maxLen=255] — Represents the unique identifier of the parent follow-up step.
          - `type` (string) [maxLen=255] — Represents the branch type of the parent follow-up connection.
        - `execute_after` (object) — Represents the wait period before this follow-up step executes.
          - `unit` (integer/int32) — Represents the time unit for the wait period.
          - `period` (string) [maxLen=255] — Represents the numeric duration of the wait period.
          - `id` (string) [maxLen=255] — Represents the unique identifier for the execute-after configuration.
        - `action` (object) **REQ** — Represents the action configured for the follow-up step.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the follow-up step.
        - `triggers` (array of string) [maxItems=25, nullable] — Represents the list of trigger conditions for the follow-up step.
          items: [maxLen=255]
      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of a Cadence.
      - `draft_cadence` (object) — Represents the draft version of the Cadence, if one exists.
        - `id` (string) [maxLen=255] — Represents the unique identifier of a Cadence.
        - `name` (string) [maxLen=100] — Represents the name of a Cadence.
      - `parent_cadence` (object) — Represents the original Cadence from which this Cadence was cloned.
        - `id` (string) [maxLen=255] — Represents the unique identifier of a Cadence.
        - `name` (string) [maxLen=100] — Represents the name of a Cadence.
      - `custom_view` (object `CustomViewInfo`) — Represents the identifier and name of a Custom View.
        schema: `CustomViewInfo`
        - `name` (string) [maxLen=255] — Represents the name of the Custom View.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the Custom View.
      - `status` (string) **REQ** [maxLen=255] — Cadence lifecycle status. draft = not yet published; active = published and enrolling records; inactive = published but currently deactivated.

- **204**: Indicates no Cadence was found for the specified ID. The response body is empty.

- **403**: The user does not have permission to retrieve Cadences, or the API is not supported for the selected domain.
**Resolution:** The CRM administrator must grant the required Cadence read permission to the user's profile, and a new access token must be generated with the required scope. — Schema: `AllErrorResponse` [application/json]
    > Represents the error response returned when the API request fails due to validation errors or unsupported operations.
    schema: `AllErrorResponse`
    - `code` (string) **REQ** [enum=[18 values]] — Represents a machine-readable error code; branch on this value, not on message.
    - `message` (string/error message) **REQ** — Represents the error message describing the validation failure.
    - `status` (string) **REQ** [const=error] — Represents the status of the API response.
    - `details` (object) **REQ** — Represents additional details providing context about the error.
      oneOf:
        - `ExpectedFieldMissingDetails` — Represents error details when expected fields are missing from the request.
          - `expected_fields` (array of object) [maxItems=25] **REQ** — Represents the list of expected fields that are missing from the request.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing expected field.
            - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the missing expected field.
        - `ExpectedDependentFieldMissingDetails` — Represents error details when expected dependent fields are missing from the request.
          - `dependee` (object) **REQ** — Represents the expected dependent field that is missing from the request.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the expected dependent field.
            - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the expected dependent field.
          - `expected_fields` (array of object) [maxItems=25] **REQ** — Represents the list of expected fields that are missing from the request.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing expected field.
            - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the missing expected field.
        - `InvalidDataWithId` — Represents error details when a field contains an invalid identifier.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field with invalid data.
          - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field with invalid data.
          - `id` (string) **REQ** [maxLen=255] — Represents the identifier of the invalid value provided.
        - `InvalidDataWithSupportedValues` — Represents error details when a field contains an invalid value, listing the supported values.
          - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of supported values for the field.
            items: [maxLen=500]
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field with invalid data.
          - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field with invalid data.
          - `param_name` (string) [maxLen=255] — Represents the parameter name of the field with invalid data.
        - `InvalidDataWithDataType` — Represents error details when a field contains invalid data, specifying the expected data type.
          - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type for the field.
          - `api_name` (string) [maxLen=255] — Represents the API name of the field with invalid data.
          - `json_path` (string) [maxLen=500] — Represents the JSON path of the field with invalid data.
          - `param_name` (string) [maxLen=255] — Represents the parameter name of the field with invalid data.
        - `InvalidDataWithDataTypeAndSupportedValues` — Represents error details when a field contains invalid data, specifying the expected data type and supported values.
          - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type for the field.
          - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of supported values for the field.
            items: [maxLen=500]
          - `api_name` (string) [maxLen=255] — Represents the API name of the field with invalid data.
          - `json_path` (string) [maxLen=500] — Represents the JSON path of the field with invalid data.
          - `param_name` (string) [maxLen=255] — Represents the parameter name of the field with invalid data.
        - `MandatoryInvalidDataCommonApiNameJsonPath` — Represents error details when a mandatory field contains invalid data.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the mandatory field with invalid data.
          - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the mandatory field with invalid data.
          - `param_name` (string) [maxLen=255] — Represents the parameter name of the mandatory field with invalid data.
        - `DependentMismatchDetails` — Represents error details when a dependent field value does not match the expected values based on the parent field.
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
        - `DependencyFieldMissingDetails` — Represents error details when a required dependency field is missing from the request.
          - `dependee` (object) **REQ** — Represents the dependee field that is required but missing from the request.
            - `api_name` (string) [maxLen=255] — Represents the API name of the dependee field.
            - `json_path` (string) [maxLen=500] — Represents the JSON path of the dependee field.
            - `param_name` (string) [maxLen=255] — Represents the parameter name of the dependee field.
          - `api_name` (string) [maxLen=255] — Represents the API name of the field with the missing dependency.
          - `json_path` (string) [maxLen=500] — Represents the JSON path of the field with the missing dependency.
          - `param_name` (string) [maxLen=255] — Represents the parameter name associated with the field.
        - `ResourcePathIndex` — Represents error details containing the resource path index where the validation error occurred.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path where the validation error occurred.
        - `IdDetails` — Represents error details containing the unique identifier of the resource associated with the error.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the resource.
        - `ParamNameDetails` — Represents error details containing the parameter name associated with the error.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the parameter name associated with the error detail.
        - `ParamNameWithEnumDetails` — Represents error details containing the parameter name associated with the error.
          - `param_name` (string) **REQ** [maxLen=255, enum=['ids']] — Represents the parameter name associated with the error detail.
Possible values:
ids - The ids query parameter.
        - `ApiNameLimit` — Represents error details when a field exceeds its maximum allowed count.
          - `api_name` (string) [maxLen=255] — Represents the API name of the field that exceeded the limit.
          - `limit` (integer/int32) **REQ** — Represents the maximum allowed count for the field.
        - `DetailsPermission` — Represents error details when the request fails due to missing permissions.
          - `permissions` (array of string) [maxItems=25] **REQ** — Represents the list of required permissions that are missing.
            items: [maxLen=255]
        - `EmptyDetails` (object) — Represents an empty error details object with no additional information.
        - `ApiNameLimitJsonPath` — Represents error details when a field at a specific JSON path exceeds its maximum allowed count.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that exceeded the limit.
          - `limit` (integer/int32) **REQ** — Represents the maximum allowed count for the field.
          - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field that exceeded the limit.
        - `AmbiguityDetails` — Represents error details for ambiguity, listing the fields that caused the ambiguity.
          - `ambiguity_due_to` (array of object) [maxItems=100] **REQ** — Represents the list of fields that caused the ambiguity during processing.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the ambiguity.
            - `json_path` (string) [maxLen=255] — Represents the JSON path of the field that caused the ambiguity.
        - `ApiNameExistsInJsonPath` — Represents error details when an API name already exists at the specified JSON path.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that already exists in the specified JSON path.
          - `exists_in` (object) **REQ** — Represents the location where the API name already exists, identified by its API name and JSON path.
            - `api_name` (string) [maxLen=255] — Represents the API name at the existing location.
            - `json_path` (string) [maxLen=500] — Represents the JSON path of the existing field location.
          - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the duplicate field in the request payload.
        - `MaximumLengthApiNameJsonPath` — Represents error details when a field value exceeds the maximum allowed length.
          - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the field.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that exceeded the maximum length.
          - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field that exceeded the maximum length.

**Scopes:** ZohoCRM.settings.cadences.READ

# GET /settings/automation/cadences/{id}/actions/analytics
**Operation:** `getCadenceAnalytics` — Get Cadence analytics
> To retrieve per-follow-up execution statistics for the specified Cadence in your Zoho CRM organization. Each follow-up element returns an analytics payload whose structure depends on its action type: tasks (open, completed, and failed counts), schedule_call (created, scheduled, completed, missed, cancelled, overdue, and failed counts), email_notifications (sent, opened, clicked, replied, bounced, unsubscribed, and unsent counts), and whatsapp_message_notification (delivered and failed counts). Use the **filters** parameter to restrict results to a single action type, and the **follow_ups_executed_from** and **follow_ups_executed_till** parameters to restrict to a time range.

**Parameters:**
- `id` (path, string/int64, required): Specify the unique identifier of the Cadence for which you want to retrieve analytics.
- `filters` (query, object, optional): Specifies the filter criteria to narrow the analytics results by follow-up action type and value.
- `follow_ups_executed_from` (query, string/date-time, optional): Specifies the start date from which to retrieve follow-up execution analytics, in ISO 8601 format.
- `follow_ups_executed_till` (query, string/date-time, optional): Specifies the end date until which to retrieve follow-up execution analytics, in ISO 8601 format.

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

**Responses:**

- **200**: Returns the analytics data for the specified Cadence, including follow-up metrics grouped by action type. — Schema: `Cadence Analytics Response` [application/json]
    > Represents the analytics response for a Cadence, containing a list of Cadences and their follow-up analytics data.
    title: Cadence Analytics Response
    - `cadences` (array of object) [maxItems=100] — Represents the list of Cadences with their follow-up analytics data.
      - `module` (object `ModuleInformation`) — Represents the API name and identifier of a CRM module.
        schema: `ModuleInformation`
        - `api_name` (string) [maxLen=255] — Represents the API name of the CRM module.
        - `id` (string/int64) [maxLen=255] — Represents the unique identifier of the CRM module.
      - `name` (string) [maxLen=100] — Represents the name of a Cadence.
      - `follow_ups` (array of object) [maxItems=100] — Represents the list of follow-up steps in the Cadence, each containing action details and execution analytics.
        title: Follow-Up Details
        - `analytics` (object) — Represents the execution metrics for the follow-up action, including counts based on the action type.
          oneOf:
              - `open_tasks_count` (integer/int32) — Represents the number of tasks that are currently open.
              - `failed_tasks_count` (integer/int32) — Represents the number of tasks that failed to execute.
              - `subject` (string) [maxLen=255] — Represents the subject of the task action.
              - `completed_tasks_count` (integer/int32) — The number of tasks that were completed.
              - `tasks_count` (integer/int32) — Represents the total number of tasks generated by the follow-up action.
              - `created_calls_count` (integer/int32) — Represents the number of calls that were created.
              - `cancelled_calls_count` (integer/int32) — Represents the number of calls that were cancelled.
              - `failed_calls_count` (integer/int32) — Represents the number of calls that failed to execute.
              - `completed_calls_count` (integer/int32) — Represents the number of calls that were completed.
              - `scheduled_calls_count` (integer/int32) — Represents the number of calls that are currently scheduled.
              - `subject` (string) [maxLen=255] — Indicates the subject of the scheduled call action.
              - `calls_count` (integer/int32) — Represents the total number of calls generated by the follow-up action.
              - `overdue_calls_count` (integer/int32) — Represents the total number of calls that are overdue.
              - `missed_calls_count` (integer/int32) — Represents the total number of missed calls.
              - `email_count` (integer/int32) — Represents the total number of emails sent by the follow-up action.
              - `bounced_email_count` (integer/int32) — Represents the number of emails that bounced.
              - `clicked_email_count` (integer/int32) — Represents the number of emails where at least one link was clicked.
              - `replied_email_count` (integer/int32) — Represents the number of emails that received a reply.
              - `sent_email_count` (integer/int32) — Represents the number of emails that were successfully sent.
              - `unsent_email_count` (integer/int32) — Represents the number of emails that were not sent.
              - `opened_email_count` (integer/int32) — Represents the number of emails that were opened by recipients.
              - `unsubscribed_email_count` (integer/int32) — Represents the number of recipients who unsubscribed after receiving the email.
              - `whatsapp_count` (integer/int32) — Represents the total number of WhatsApp messages sent by the follow-up action.
              - `delivered_whatsapp_count` (integer/int32) — Represents the number of WhatsApp messages that were delivered.
              - `failed_whatsapp_count` (integer/int32) — Represents the number of WhatsApp messages that failed to deliver.
        - `parent_follow_up` (object) [nullable] — Represents the identifier of the parent follow-up step, if this is a conditional branch.
        - `action` (object) — Represents the action configured for the follow-up step.
          - `template` (object) — Represents the Email Template configured for the action.
            - `name` (string) [maxLen=255] — Represents the name of the Email Template.
            - `id` (string) [maxLen=255] — Represents the unique identifier of the Email Template.
          - `message_template` (object) — Represents the message template associated with the email or WhatsApp action.
            - `id` (string) [maxLen=255] — Represents the unique identifier of the message template.
            - `title` (string) [maxLen=255] — Represents the title of the message template.
          - `name` (string) **REQ** [maxLen=255] — Represents the name of the action.
          - `type` (string) [maxLen=255] — Represents the type of action configured for the follow-up step.
          - `id` (string) [maxLen=255] — Represents the unique identifier of the action.
        - `follow_up_number` (string) [maxLen=255] — Represents the sequential number of the follow-up step within the Cadence.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the follow-up step.
      - `id` (string) [maxLen=255] — Represents the unique identifier of a Cadence.
      - `created_by` (object `CreatorInfo`) — Represents the identifier and name of the user who created the record.
        schema: `CreatorInfo`
        - `name` (string) [maxLen=255] — Represents the full name of the user who created the record.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the user who created the record.

- **400**: The request contains invalid or missing filter parameters.
**Resolution:** All required filter fields must be present and their values must conform to the supported options. — Schema: `AllErrorResponse` [application/json]
    > Represents the error response returned when the API request fails due to validation errors or unsupported operations.

- **403**: The user does not have permission to view Cadence analytics.
**Resolution:** The CRM administrator must grant the required Cadence read permission to the user's profile, and a new access token must be generated with the required scope. — Schema: `AllErrorResponse` [application/json]
    > Represents the error response returned when the API request fails due to validation errors or unsupported operations.

**Scopes:** ZohoCRM.settings.cadences.READ

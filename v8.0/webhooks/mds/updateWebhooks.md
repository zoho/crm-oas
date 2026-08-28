# PUT /settings/automation/webhooks
**Operation:** `updateWebhooks` — Update webhooks
> To update the configuration of an existing webhook in your Zoho CRM organization.

The module field cannot be changed after creation. The request body must contain a webhooks array with exactly one webhook object.

To retrieve valid module API names, refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource.

**Schemas:**
`InvalidDataMaxLengthError`:
  > Represents the error returned when a field value exceeds the maximum allowed character length.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - A field value exceeds the maximum allowed length.
  - `details` (object) **REQ** — Represents the error details containing information about the field that exceeds the maximum allowed length.
    - `maximum_length` (integer/int32) — Represents the maximum number of characters allowed for the field.
    - `api_name` (string) [maxLen=255] — Represents the API name of the field that exceeds the maximum allowed length.
    - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that exceeds the maximum allowed length.
  - `message` (string) **REQ** [enum=['Invalid data', 'invalid data']] — Represents the error message describing the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
`InvalidDataTypeError`:
  > Represents the error returned when a field value has an incorrect data type.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - A field value has an incorrect data type.
  - `details` (object) **REQ** — Represents the error details containing information about the field with the incorrect data type.
    - `expected_data_type` (string) [maxLen=255] — Represents the expected data type for the field.
    - `api_name` (string) [maxLen=255] — Represents the API name of the field with the incorrect data type.
    - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field with the incorrect data type.
  - `message` (string) **REQ** [enum=['Invalid data type', 'data type not supported', 'invalid data']] — Represents the error message describing the failure.
Possible values:
**Invalid data type** - The field value does not match the expected data type.
**data type not supported** - The data type provided is not supported for this field.
**invalid data** - The field value is not valid.
  - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
`MandatoryFieldMissingError`:
  > Represents the error returned when a required field is absent from the request body.
  - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this failure.
Possible values:
**MANDATORY_NOT_FOUND** - A required field is missing from the request body.
  - `details` (object) **REQ** — Represents the error details identifying the mandatory field that is missing.
    - `api_name` (string) [maxLen=255] — Represents the API name of the mandatory field that is missing.
    - `json_path` (string) [maxLen=1000] — Represents the JSON path to the mandatory field that is missing.
  - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message describing the failure.
Possible values:
**Required field is missing** - A mandatory field was not included in the request.
  - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
`UserDefinedParameter`:
  > A single user-defined parameter appended as a URL query parameter. Note: The API uses plural 'user_defined_parameters' here but singular 'user_defined_parameter' in form_data_content  - both are single objects, not arrays.
  - `name` (string) [maxLen=255] — Represents the key name of the user-defined parameter.
  - `value` (string) [maxLen=255] — Represents the value of the user-defined parameter.
`WebhookCustomParameters`:
  > Represents a static key-value parameter for webhook requests. Used in headers, URL query parameters, or form data fields. The value is a fixed literal sent unchanged with every webhook execution.
  - `name` (string) [maxLen=255] — Represents the parameter key sent in the webhook request.
  - `value` (string) [maxLen=255] — Represents the static literal value sent with every webhook execution.
`WebhookModuleParameters`:
  > Represents a module merge-field parameter for webhook requests. Used in headers, URL query parameters, or form data fields. The value is resolved at runtime from the field of the triggering CRM record.
  - `name` (string) [maxLen=255] — Represents the parameter key sent in the webhook request. The name must be unique within the parameter collection.
  - `value` (string) [maxLen=255] — Represents the merge-field token resolved at runtime from the triggering CRM record. Use the API field names and not display names (for example, use ${!Leads.Last_Name}, not ${!Leads.Last Name}). Invalid API names return INVALID_DATA.

**Request Body** — application/json `UpdateWebhookRequest`
> The request body must contain a webhooks array with one object.
  > Represents the request body wrapper for updating a webhook. The webhooks array must contain exactly one webhook object.
  - `webhooks` (array of object `WebhookUpdateInput`) [minItems=1, maxItems=1] **REQ** — Represents the list containing exactly one webhook object with the full replacement configuration.
    schema: `WebhookUpdateInput`
    - `id` (string) [maxLen=20] — Represents the unique identifier of the webhook to update. The ID is required in the request body when using the bulk update endpoint.
    - `name` (string) **REQ** [maxLen=250] — Specify the display name of the webhook. The name must not contain the tilde (~) character. The name cannot be changed for kiosk feature actions.
    - `module` (object `AutomationModuleDetailsResponse`) **REQ** — The CRM module. Cannot be changed  - providing a different module returns NOT_ALLOWED.
      schema: `AutomationModuleDetailsResponse`
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM module (for example, Leads, Contacts, Deals).
      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the CRM module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
    - `url` (string) **REQ** [maxLen=2000] — Specify the destination URL that receives the webhook request when triggered. The URL must begin with http://, https://, www., or a merge-field token (${...}). URLs resolving to internal or private host addresses are rejected by SSRF protection.
    - `http_method` (string) **REQ** [enum=['POST', 'GET', 'PUT', 'DELETE']] — Specify the HTTP method used when the webhook fires.
Possible values:
**POST** - Sends a POST request.
**GET** - Sends a GET request.
**PUT** - Sends a PUT request.
**DELETE** - Sends a DELETE request.
    - `authentication` (object `WebhookAuthenticationDetails`) **REQ** — Authentication configuration.
      schema: `WebhookAuthenticationDetails`
      - `connection_name` (string) [maxLen=255, nullable] — Represents the name of the Zoho connection used for authentication. This field is required only when **type** is **connection**.
      - `type` (string) **REQ** [maxLen=255, enum=['general', 'connection']] — Specify the authentication method for the webhook endpoint.
Possible values:
**general** - No credentials required.
**connection** - Uses a pre-configured Zoho connection.
    - `description` (string) [maxLen=500, nullable] — Specify the optional description of the webhook purpose.
    - `related_module` (object `RelatedModuleReference`) — Related CRM module. Required when feature_type is kiosk.
      schema: `RelatedModuleReference`
      - `api_name` (string) [maxLen=255] — Represents the API name of the related CRM module.
      - `id` (string) [maxLen=255] — Represents the unique identifier of the related CRM module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
    - `feature_type` (string) **REQ** [maxLen=255, enum=[7 values]] — Specify the automation feature type for this webhook.
Possible values:
**workflow** - Workflow Rule.
**approval_process** - Approval Process.
**blueprint_transition** - Blueprint transition.
**blueprint_state** - Blueprint state.
**assignment_rules** - Assignment Rules.
**kiosk** - Kiosk feature.
**commandcenter_service** - CommandCenter service.
    - `headers` (object `WebhookHeaders`) — HTTP headers. Only allowed when http_method is POST, PUT, or DELETE. Restricted header name: HOST is not allowed. Parameter names must be unique (DUPLICATE_DATA).
      schema: `WebhookHeaders`
      - `custom_parameters` (array of object `WebhookCustomParameters`) [maxItems=10, nullable] — Represents the static key-value pairs sent as HTTP headers with every webhook execution.
      - `module_parameters` (array of object `WebhookModuleParameters`) [maxItems=25, nullable] — Represents the module merge-field parameters sent as HTTP headers. The key must be present but may be an empty array when only custom parameters are needed.
    - `url_parameters` (object `WebhookUrlParameters`) — URL query parameters. Only allowed when http_method is GET or DELETE.
      schema: `WebhookUrlParameters`
      - `custom_parameters` (array of object `WebhookCustomParameters`) [maxItems=10] — Represents the static key-value pairs appended as URL query parameters to every webhook request. Each entry must have a unique name.

- name (string, optional)

Specify a name to the custom header.


- value (string, optional)

Specify a value to the custom header.


"custom_parameters": [
    {
        "name": "OAuth",
        "value": "2.0"
    }
]. 


A maximum  of 10 entries is allowed.
      - `module_parameters` (array of object `WebhookModuleParameters`) [maxItems=25] — Represents the module merge-field parameters appended as URL query parameters. Values are resolved at runtime from the triggering CRM record using the merge-field format (for example, ${!Leads.Email}). Use the [Get Fields Metadata](fields.yaml#$.paths./settings/fields.get) resource to retrieve valid field API names.
      - `user_defined_parameters` (object `UserDefinedParameter`) — A single user-defined parameter appended as a URL query parameter. Note: The API uses plural 'user_defined_parameters' here but singular 'user_defined_parameter' in form_data_content  - both are single objects, not arrays.
    - `body` (object `WebhookRequestBody`) — Request body. Only allowed when http_method is POST or PUT. type and format are required. When type=form_data: provide form_data_content (object with module_parameters and custom_parameters arrays); format may be null. When type=raw: provide raw_data_content (string) and format (JSON, XML, Text, or HTML). When type=none: format may be null.
      schema: `WebhookRequestBody`
      - `format` (string) **REQ** [maxLen=25, enum=['JSON', 'XML', 'Text', 'HTML', None], nullable] — Specify the body content format.
Possible values:
**JSON** - JSON format.
**XML** - XML format.
**Text** - Plain text format.
**HTML** - HTML format.
**null** - Valid for form_data and none body types.
      - `raw_data_content` (string) [maxLen=500, nullable] — Represents the raw string content sent as the request body. This field is required when the body type is raw.
      - `type` (string) **REQ** [maxLen=255, enum=['form_data', 'raw', 'none']] — Specify the body type for the webhook request.
Possible values:
**form_data** - Sends data as key-value pairs in the request body.
**raw** - Sends plain text, JSON, HTML, or XML content directly.
**none** - No body content.
      - `form_data_content` (object `FormDataContent`) — Form data content when body type is form_data. Contains module parameters, custom parameters, and an optional user-defined parameter.
        schema: `FormDataContent`
        - `module_parameters` (array of object `WebhookModuleParameters`) [maxItems=25] — Represents the module merge-field parameters resolved at runtime and sent as form data in the webhook request.
        - `user_defined_parameter` (object `UserDefinedParameter`) — A single user-defined key-value parameter sent as a form data field. Note: The API uses singular 'user_defined_parameter' for form_data_content (this field) and plural 'user_defined_parameters' for url_parameters  - both are single objects, not arrays.
        - `custom_parameters` (array of object `WebhookCustomParameters`) [maxItems=10] — Represents the custom static key-value pairs sent as form data in the webhook request.
    - `date_time_format` (object `DateTimeFormatConfig`) — Optional. Only relevant when a date or datetime merge-field is used in any parameter (headers, url_parameters, or body). Use datetime_format + time_zone for datetime fields, date_format for date fields. Ignored if no date/datetime merge-fields are present.
      schema: `DateTimeFormatConfig`
      - `datetime_format` (string) [maxLen=255] — Represents the format pattern for datetime merge-field values in the webhook payload.
      - `date_format` (string) [maxLen=255] — Represents the format pattern for date-only merge-field values in the webhook payload.
      - `time_zone` (string) [maxLen=255] — Represents the timezone identifier applied to datetime merge-field values in the webhook payload.

**Responses:**

- **200**: Returns the success response for the webhook update operation, including the updated webhook ID in the **details** object. — Schema: `UpdateWebhookSuccessResponse` [application/json]
    > Represents the success response for a webhook update operation, including the operation result and the updated webhook ID.
    schema: `UpdateWebhookSuccessResponse`
    - `webhooks` (array of object `WebhookStatusResponse`) [maxItems=1] — Represents the list containing the operation result for the updated webhook.
      schema: `WebhookStatusResponse`
      - `code` (string) **REQ** [maxLen=255] — Represents the success or error code of the webhook operation.
      - `details` (object `WebhookDetailsResponse`) **REQ** — Result details. On success, contains the webhook id.
        schema: `WebhookDetailsResponse`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the webhook.
      - `message` (string) **REQ** [maxLen=255] — Represents the description of the operation result.
      - `status` (string) **REQ** [maxLen=255] — Represents the operation status.

- **400**: One or more request body fields are invalid. Returned for validation errors including invalid module ID, unsupported HTTP method, malformed URL, SSRF-protected URL, unsupported feature type, duplicate parameter names, module change attempt, and data type or length violations.

**Resolution:** All required fields must be present in the request body, and each field value must match the expected type, format, and allowed values for this operation. The module field cannot be changed after webhook creation. [application/json]
    > Contains the error response for an invalid webhook update request. The schema is a union of specific error variants covering field-level validation, data type, length, and supported value violations.
    oneOf:
        - `webhooks` (array of object) [maxItems=25] **REQ** — Represents the array containing the error object for the invalid webhook in the bulk update response.
          oneOf:
            - `InvalidModuleIdError` — Represents the error returned when the module ID in the request body does not correspond to an existing CRM module.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The module ID provided in the request is not valid.
              - `details` (object) **REQ** — Represents the error details identifying the field with the invalid module ID.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains the invalid module ID.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that contains the invalid module ID.
              - `message` (string) **REQ** [enum=[2 values]] — Represents the error message describing the failure.
Possible values:
**the module id given seems to be invalid** - The module ID does not match a valid CRM module.
**the tabId given seems to be invalid** - The tab ID provided does not match a valid module tab.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `AmbiguityProcessingErrorResponse` — Represents the error returned when both module id and api_name are provided but refer to different modules.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code for this failure.
Possible values:
**AMBIGUITY_DURING_PROCESSING** - Ambiguity was encountered while processing the request.
              - `details` (object) **REQ** — Represents the error details containing information about the field that caused the ambiguity.
                - `ambiguity_due_to` (array of object) [maxItems=25] — Represents the list of fields that caused the ambiguity in the request.
                  - `api_name` (string) [maxLen=255] — Represents the API name of the dependee or conflicting field.
                  - `json_path` (string) [maxLen=1000] — Represents the JSON path to the dependee or conflicting field.
              - `message` (string) **REQ** [enum=[2 values]] — Represents the error message describing the failure.
Possible values:
**Ambiguity while processing the request** - Multiple conflicting fields were detected.
**The given module api_name seems to be invalid** - The module API name provided is not recognized.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `InvalidNameErrorResponse` — Represents the error returned when the webhook name contains invalid or unsupported characters.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The webhook name contains invalid characters.
              - `details` (object) **REQ** — Represents the error details identifying the field with the invalid name.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field with the invalid name value.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field with the invalid name value.
              - `message` (string) **REQ** [enum=[2 values]] — Represents the error message describing the failure.
Possible values:
**Special characters not allowed** - The webhook name contains characters that are not permitted.
**webhook name should not contain the special character #%** - The webhook name includes the # or % characters, which are not allowed.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `NameLimitExceededErrorResponse` — Represents the error returned when the webhook name exceeds the maximum allowed character length.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The webhook name exceeds the maximum allowed length.
              - `details` (object) **REQ** — Represents the error details identifying the field for which the name length limit is exceeded.
                - `maximum_length` (integer/int32) — Represents the maximum allowed length for the field value.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field for which the name length limit is exceeded.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field for which the name length limit is exceeded.
              - `message` (string) **REQ** [enum=['The lenght of name has exceeded the limit']] — Represents the error message describing the failure.
Possible values:
**The lenght of name has exceeded the limit** - The webhook name exceeds the maximum allowed character limit.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `InvalidMethodTypeErrorResponse` — Represents the error returned when the http_method value is not a supported HTTP method for webhook operations.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The HTTP method type provided in the request is not valid.
              - `details` (object) **REQ** — Represents the error details identifying the field with the invalid method type value.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field with the invalid HTTP method type.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field with the invalid HTTP method type.
              - `message` (string) **REQ** [enum=['The method type given is invalid']] — Represents the error message describing the failure.
Possible values:
**The method type given is invalid** - The HTTP method value does not match the supported values.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `InvalidUrlErrorResponse` — Represents the error returned when the url field value is not a valid or well-formed URL.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The webhook URL is not valid or contains a blocked host.
              - `details` (object) **REQ** — Represents the error details identifying the field with the invalid URL.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field with the invalid URL.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field with the invalid URL.
              - `message` (string) **REQ** [enum=['please enter a valid URL']] — Represents the error message describing the failure.
Possible values:
**please enter a valid URL** - The webhook URL is not a valid HTTP or HTTPS URL, or it is blocked for security reasons.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `InvalidDateFormatErrorResponse` — Represents the error returned when the date_format value in date_time_format is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The date value provided in the request is in an invalid format.
              - `details` (object) **REQ** — Represents the error details identifying the field with the invalid date format.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field with the invalid date format.
                - `expected_data_type` (string) [maxLen=255] — Represents the expected data type for the date field.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the date field with the invalid format.
              - `message` (string) **REQ** [enum=['The Date given is invalid', 'Please provide a valid date format']] — Represents the error message describing the failure.
Possible values:
**The Date given is invalid** - The date value does not match the expected format.
**Please provide a valid date format** - The date format string is not recognized.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `InvalidTimezoneErrorResponse` — Represents the error returned when the time_zone value in date_time_format is not a supported timezone identifier.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The timezone identifier provided in the request is not valid.
              - `details` (object) **REQ** — Represents the error details identifying the field with the invalid timezone value.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field with the invalid timezone value.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field with the invalid timezone value.
              - `message` (string) **REQ** [enum=['The timezone given is invalid']] — Represents the error message describing the failure.
Possible values:
**The timezone given is invalid** - The timezone identifier does not match a valid timezone.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `InvalidDateTimeFormatErrorResponse` — Represents the error returned when the datetime_format value in date_time_format is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The datetime format provided in the request is not valid.
              - `details` (object) **REQ** — Represents the error details identifying the field with the invalid datetime format.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field with the invalid datetime format.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field with the invalid datetime format.
              - `message` (string) **REQ** [enum=[2 values]] — Represents the error message describing the failure.
Possible values:
**The date time format given is invalid** - The datetime value does not match the expected format.
**Please provide a valid date time format** - The datetime format string is not recognized.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `InvalidWebhookIdError` — Represents the error returned when the webhook ID in the request body does not match an existing webhook or is malformed.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The webhook ID provided in the request is not valid.
              - `details` (object) **REQ** — Represents the error details identifying the field with the invalid webhook ID.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field with the invalid webhook ID.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field with the invalid webhook ID.
              - `message` (string) **REQ** [enum=['The ID given is invalid']] — Represents the error message describing the failure.
Possible values:
**The ID given is invalid** - The webhook ID in the request does not match any existing webhook.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `UnsupportedMergeFieldErrorResponse` — Represents the error returned when a merge-field token in the webhook configuration references a field that is not supported for the module or context.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The request contains an unsupported merge field or a restricted parameter name.
              - `details` (object) **REQ** — Represents the error details containing information about the field that contains the unsupported merge field or restricted parameter name.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that triggered the error.
              - `message` (string) **REQ** [enum=['Unsupported fields are present', 'restricted parameter name found']] — Represents the error message describing the failure.
Possible values:
**Unsupported fields are present** - The request contains merge fields that are not supported for this operation.
**restricted parameter name found** - A parameter name in the request is reserved and cannot be used.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `DuplicateDataErrorResponse` — Represents the error returned when duplicate names are found in the module_parameters or custom_parameters collections.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code for this failure.
Possible values:
**DUPLICATE_DATA** - A duplicate parameter name was detected in the request.
              - `details` (object) **REQ** — Represents the error details containing information about the field that caused the duplicate data error.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that triggered the error.
                - `param_name` (string) [maxLen=255] — Represents the name of the parameter that contains the duplicate value.
              - `message` (string) **REQ** [enum=['duplicate parameter name found']] — Represents the error message describing the failure.
Possible values:
**duplicate parameter name found** - A parameter name appears more than once in the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `AuthorizationDependentMismatchError` — Represents the error returned when authentication.type is general but a connection_name is also provided, or when type is connection but connection_name is absent.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code for this failure.
Possible values:
**DEPENDENT_MISMATCH** - A required dependent field value does not match the expected configuration.
              - `details` (object) **REQ** — Represents the error details containing information about the field that triggered the validation failure.
                - `dependee` (object) — Represents the dependent field configuration that conflicts with the submitted value, including its API name and JSON path.
                  - `api_name` (string) [maxLen=255] — Represents the API name of the dependee or conflicting field.
                  - `json_path` (string) [maxLen=1000] — Represents the JSON path to the dependee or conflicting field.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that triggered the error.
              - `message` (string) **REQ** [enum=['provide appropriate authentication type']] — Represents the error message describing the failure.
Possible values:
**provide appropriate authentication type** - The authentication type configured does not match the expected dependent field configuration.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `ParameterNameValueMandatoryError` — Represents the error returned when a parameter entry in module_parameters or custom_parameters is missing its name or value. Both fields are required for each entry.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this failure.
Possible values:
**MANDATORY_NOT_FOUND** - Both name and value are required for each parameter entry in the request.
              - `details` (object) **REQ** — Represents the error details identifying the parameter entry with the missing name or value.
                - `api_name` (string) [maxLen=255] — Represents the API name of the parameter field that is missing the required name or value.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the parameter field that is missing the required name or value.
              - `message` (string) **REQ** [enum=['the given parameter is invalid, specify both name and value']] — Represents the error message describing the failure.
Possible values:
**the given parameter is invalid, specify both name and value** - Each parameter entry must include both a name and a value.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `HttpMethodMandatoryError` — Represents the error returned when the http_method field is absent from the webhook request body.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this failure.
Possible values:
**MANDATORY_NOT_FOUND** - The HTTP method field is missing from the request.
              - `details` (object) **REQ** — Represents the error details containing information about the mandatory HTTP method field that is missing.
                - `api_name` (string) [maxLen=255] — Represents the API name of the mandatory field that is missing.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the mandatory field that is missing.
              - `message` (string) **REQ** [enum=['The method type is not given ']] — Represents the error message describing the failure.
Possible values:
**The method type is not given** - The HTTP method field is missing from the request body.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `InvalidConnectionNameError` — Represents the error returned when the provided connection_name does not exist or is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The connection name provided in the authentication configuration is not valid.
              - `details` (object) **REQ** — Represents the error details containing information about the field with the invalid connection name.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that triggered the error.
              - `message` (string) **REQ** [enum=['Please provide valid connection name', 'invalid data']] — Represents the error message describing the failure.
Possible values:
**Please provide valid connection name** - The connection name in the authentication configuration does not match any existing Zoho Connections integration.
**invalid data** - The connection name value is not in a valid format.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `HttpMethodDependentMismatchError` — Represents the error returned when the request includes fields incompatible with the chosen http_method. For example, body with GET or DELETE, or url_parameters with POST or PUT.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code for this failure.
Possible values:
**DEPENDENT_MISMATCH** - The value provided for the HTTP method does not match the expected dependent field configuration.
              - `details` (object) **REQ** — Represents the error details containing information about the HTTP method field that caused the dependent mismatch.
                - `dependee` (object) — Represents the dependent field configuration that conflicts with the submitted HTTP method value.
                  - `api_name` (string) [maxLen=255] — Represents the API name of the dependee or conflicting field.
                  - `json_path` (string) [maxLen=1000] — Represents the JSON path to the dependee or conflicting field.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that triggered the error.
              - `message` (string) **REQ** [enum=['Invalid value provided for the given http method']] — Represents the error message describing the failure.
Possible values:
**Invalid value provided for the given http method** - The value submitted for the HTTP method field is not valid for the configured dependent field.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `ReadOnlyWebhookNotAllowedError` — Represents the error returned when a request attempts to edit a read-only webhook created by a Marketplace extension.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this failure.
Possible values:
**NOT_ALLOWED** - The read-only webhook cannot be edited.
              - `details` (object) **REQ** — Represents the error details containing the webhook ID that cannot be edited.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field on the read-only webhook that triggered the error.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field on the read-only webhook that triggered the error.
              - `message` (string) **REQ** [enum=['Insufficient privileges to edit Read only webhook']] — Represents the error message describing the failure.
Possible values:
**Insufficient privileges to edit Read only webhook** - The requesting user does not have permission to edit this read-only webhook.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `InvalidDataTypeError` — Represents the error returned when a field value has an incorrect data type.
            - `InvalidDataMaxLengthError` — Represents the error returned when a field value exceeds the maximum allowed character length.
            - `MandatoryFieldMissingError` — Represents the error returned when a required field is absent from the request body.
            - `ModuleChangeNotAllowedError` — Represents the error returned when a PUT request attempts to change the module of an existing webhook. The module field is immutable after creation.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this failure.
Possible values:
**NOT_ALLOWED** - The module field cannot be changed after the webhook is created.
              - `details` (object) **REQ** — Represents the error details identifying the field for which the module change is not allowed.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field for which the module change is not allowed.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field for which the module change is not allowed.
              - `message` (string) **REQ** [enum=['old value cannot be changed with new value for this field']] — Represents the error message describing the failure.
Possible values:
**old value cannot be changed with new value for this field** - The module field is immutable after webhook creation and cannot be updated.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `KioskNameChangeNotAllowedError` — Represents the error returned when a PUT request attempts to change the name of a webhook with feature_type kiosk. Kiosk action names are immutable.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this failure.
Possible values:
**NOT_ALLOWED** - The kiosk action name cannot be changed after creation.
              - `details` (object) **REQ** — Represents the error details identifying the field for which the kiosk name change is not allowed.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field for which the kiosk name change is not allowed.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field for which the kiosk name change is not allowed.
              - `message` (string) **REQ** [enum=['Action name not allow to change for kiosk feature actions']] — Represents the error message describing the failure.
Possible values:
**Action name not allow to change for kiosk feature actions** - The kiosk action name field cannot be modified after creation.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
      - `MarketplaceWebhookNotAllowedError` — Represents the error returned when a request attempts to modify or delete a webhook created by a Marketplace extension or CommandCenter.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this failure.
Possible values:
**NOT_ALLOWED** - The webhook was created by a Marketplace extension and cannot be modified or deleted.
        - `details` (object) **REQ** — Represents the error details containing additional context about the marketplace webhook restriction.
          - `resource_path_index` (integer/int32) — Represents the index of the invalid resource in the request URL path for the marketplace webhook.
        - `message` (string) **REQ** [enum=['Webhook  is associated with MarketPlace']] — Represents the error message describing the failure.
Possible values:
**Webhook  is associated with MarketPlace** - The webhook was created by a Marketplace extension and cannot be modified or deleted by the requesting user.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
        - `webhooks` (object `MandatoryFieldMissingError`) **REQ** — Represents the error returned when a required field is absent from the request body.
        - `webhooks` (object `InvalidDataTypeError`) **REQ** — Represents the error returned when a field value has an incorrect data type.
        - `webhooks` (object `InvalidDataMaxLengthError`) **REQ** — Represents the error returned when a field value exceeds the maximum allowed character length.
        - `webhooks` (object `InvalidDataSupportedValuesError`) **REQ** — Represents the error returned when a field value is not among the accepted values for that field. The details object includes a supported_values array listing the accepted values.
          schema: `InvalidDataSupportedValuesError`
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - A field value is not among the supported values.
          - `details` (object) **REQ** — Represents the error details containing information about the field with an unsupported value.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains the unsupported value.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that contains the unsupported value.
            - `regex` (string) [maxLen=1000] — Represents the regex pattern used for validation of the field value.
            - `supported_values` (array of string) [maxItems=25] — Represents the list of values that are supported for this field.
              items: [maxLen=255]
          - `message` (string) **REQ** [enum=['Invalid data', 'invalid data']] — Represents the error message describing the failure.

          - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.

- **403**: Permission denied to update webhooks in this organization.

**Resolution:** The CRM administrator must grant the Manage Workflow permission to the user profile. — Schema: `NoPermissionErrorResponse` [application/json]
    > Represents the error returned when the requesting user does not have the required CRM profile permission to perform the operation.
    schema: `NoPermissionErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — The requesting user does not have the required CRM profile permission.
    - `details` (object) **REQ** — Represents the error details containing the list of permissions required for this operation.
      - `permissions` (array of string) [maxItems=25] — Represents the list of CRM profile permissions required to perform this operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message describing the failure.

Possible values:
**permission denied** - The requesting user lacks the required CRM profile permission for this operation.
    - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.

**Scopes:** ZohoCRM.settings.automation_actions.UPDATE

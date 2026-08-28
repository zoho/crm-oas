# POST /settings/unsubscribe_links
**Operation:** `postUnsubscribeLinks` — Create Unsubscribe Link
> To create an unsubscribe link that can be used in email templates or email footers. You can configure the link to display a standard Zoho CRM unsubscribe page or redirect to a custom webpage.

**Schemas:**
`MandatoryFieldMissingError`:
  > Error returned when a required mandatory field is missing from the request.
  - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this response.
  - `details` (object) **REQ** — Contains additional validation information about the missing mandatory field error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing mandatory field
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the missing mandatory field
  - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message describing the missing mandatory field.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

**Request Body** — application/json `InitiateUnsubscribeLinksRequest`
> Request body containing the unsubscribe link configuration. The name, page_type, and submission_action_type fields are mandatory.
  > Request payload to create one or more unsubscribe links.
  - `unsubscribe_links` (array of object `UnsubscribeLinkCreateItem`) [maxItems=1] **REQ** — Array containing the unsubscribe link configuration to create (required)
    schema: `UnsubscribeLinkCreateItem`
    - `submission_message` (string) [maxLen=2000] — Represents the message displayed when the user clicks the unsubscribe button. Required when submission_action_type is display_message. unsubscribe button. Required when submission_action_type is display_message.
    - `submission_redirect_url` (string) [maxLen=255] — Represents the URL to redirect users to after unsubscribing. Required when submission_action_type is redirect. Required when submission_action_type is redirect.
    - `page_type` (string) **REQ** [maxLen=255] — Specifies where the unsubscribe page is hosted: standard (Zoho CRM page) or custom (your own webpage)
    - `custom_location_url` (string) [maxLen=255] — Represents the custom webpage URL for hosting the unsubscribe link. Required when page_type is custom. Required when page_type is custom. Required when page_type is custom.
    - `name` (string) **REQ** [maxLen=255] — Represents the unique name for the unsubscribe link
    - `id` (string) [maxLen=19] — Represents the unique identifier of the unsubscribe link
    - `standard_page_message` (string) [maxLen=2000] — The message displayed on the standard unsubscribe page. Can be rich text (HTML) or plain text.
    - `submission_action_type` (string) **REQ** [maxLen=255] — The action after unsubscribe: display_message (show a message) or redirect (redirect to a URL)
    additionalProperties: any

**Responses:**

- **201**: Created - Unsubscribe link created successfully — Schema: `CreateUnsubscribeLinksSuccessResponse` [application/json]
    > Success response for a POST request that returns the action status of each newly created unsubscribe link.
    schema: `CreateUnsubscribeLinksSuccessResponse`
    - `unsubscribe_links` (array of object `UnsubscribeLinkActionStatus`) [maxItems=1] — Array containing the status of the creation operation for each link
      schema: `UnsubscribeLinkActionStatus`
      - `code` (string) [maxLen=255] — The result code (SUCCESS or error code)
      - `details` (object `ActionEntityReference`) — Reference to the entity affected by an operation, containing its unique identifier.
        schema: `ActionEntityReference`
        - `id` (string) [maxLen=19] — The unique identifier of the affected unsubscribe link
      - `message` (string) [maxLen=255] — Represents the message describing the operation result.
      - `status` (string) [maxLen=255] — The status of the operation (success or error)

- **400**: Bad Request - Invalid data provided. Check field types, mandatory fields, dependencies, or refer to the Input JSON keys section in the help doc. [application/json]
    > Validation error response for the POST request, covering invalid data type, missing required fields, duplicate data, limit exceeded, and dependent field failures.
    oneOf:
        - `unsubscribe_links` (array of object) [maxItems=25] **REQ** — Represents the list of individual error objects for each unsubscribe link in the create request.
          anyOf:
            - `MandatoryFieldMissingError` — Error returned when a required mandatory field is missing from the request.
            - `DuplicateDataError` — Error returned when attempting to create an unsubscribe link with a name that already exists in your account.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional validation information about the duplicate data error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field with duplicate data
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the field with duplicate data
              - `message` (string) **REQ** [enum=['Unsubscribe Link name already exists']] — Represents the error message describing the duplicate data issue.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
            - `LinkLimitExceededError` — Error returned when the maximum allowed limit for creating unsubscribe links has been exceeded. You need to delete existing links before creating new ones.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional information about the unsubscribe link limit that has been exceeded.
                - `limit` (integer/int32) **REQ** — The maximum number of unsubscribe links allowed in your account
                - `limit_due_to` (array of object) [maxItems=25] **REQ** — The field(s) that caused the limit to be exceeded
                  - `api_name` (string) [maxLen=255] — Represents the API name of the field that is contributing to the limit.
                  - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field contributing to the limit.
              - `message` (string) **REQ** [enum=['Unsubscribe Link limit exceeded']] — Represents the error message describing the limit exceeded issue.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
            - `InvalidCustomLocationURLError` — Error returned when the custom location URL provided is invalid or does not match the expected website format.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional validation information about the invalid custom location URL error.
                - `expected_data_type` (string) **REQ** [maxLen=255] — The expected data type (e.g., website)
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the invalid field
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the invalid field
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the invalid URL issue.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
            - `DependentFieldMissingError` — Error returned when a required dependent field is missing. For example, custom_location_url is required when page_type is custom, or submission_redirect_url is required when submission_action_type is redirect.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional validation information about the dependent field error.
                - `dependee` (object) **REQ** — The field that depends on the missing field
                  - `api_name` (string) **REQ** [maxLen=255] — The API name of the dependee field
                  - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the dependee field
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the missing field
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the missing field
              - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message describing the missing dependency.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
            - `GeneralInvalidDataError` — General error returned when invalid data is provided for a field, including type mismatch or format issues.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional validation information about the invalid data error.
                - `expected_data_type` (string) **REQ** [maxLen=255] — The expected data type for this field
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the invalid field
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the invalid field
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the invalid data issue.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
            - `GenericInvalidDataError` — Error returned when invalid data is provided that exceeds maximum length limits or other validation constraints.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional validation information about the invalid data error.
                - `maximum_length` (integer/int32) **REQ** — The maximum allowed length for this field
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the invalid field
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the invalid field
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the invalid data issue.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
            - `InvalidDataValueErrorAlt` — Error returned when invalid data is provided that does not meet minimum length requirements.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional validation information about the invalid data value error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the invalid field
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field
                - `minimum_length` (integer/int32) **REQ** — Represents the minimum required length for this field
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the invalid value issue.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
            - `InvalidDataErrorType` — Error returned when invalid data is provided for a field. The response includes supported values when applicable.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional validation information about the invalid data error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the invalid field
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the invalid field
                - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of valid values for this field
                  items: [maxLen=255]
              - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid value issue.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
            - `UnsupportedPageTypeError` — Error returned when an unsupported value is provided for the page_type field. Supported values are 'standard' and 'custom'.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional validation information about the unsupported value error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field with the unsupported value
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the field with the unsupported value
                - `supported_values` (array of string) [maxItems=25] **REQ** — The list of supported values for this field
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['the given module is not supported in create or update']] — Represents the error message describing the unsupported value issue.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
            - `RequiredFieldDependencyError` — Error returned when a dependent field is missing. For example, custom_location_url is required when page_type is custom.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional validation information about the missing required dependent field.
                - `dependee` (object) **REQ** — The field that depends on the missing field
                  - `api_name` (string) **REQ** [maxLen=255] — The API name of the dependee field
                  - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the dependee field
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the missing dependent field
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the missing dependent field
              - `message` (string) **REQ** [enum=['Dependent field is missing']] — Represents the error message describing the missing dependent field.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `InvalidDataTypeError` — Error returned when the data type provided for a field does not match the expected type.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional validation information about the invalid data type error.
          - `maximum_length` (integer/int32) **REQ** — The maximum allowed length for this field
          - `api_name` (string) **REQ** [maxLen=255] — The API name of the invalid field
          - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the invalid field
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the invalid data type issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `RequestBodyNotFoundError` — Error returned when the request body is missing or not found in the request.
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional validation information about the missing request body error.
          - `api_name` (string) **REQ** [maxLen=255] — The API name of the missing field
          - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the missing field
        - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message describing the missing request body.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `InvalidDataBodyError` — Error response for an invalid request body data type, providing the expected data type for the body.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional validation information about the invalid request body error.
          - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type for the request body.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid request body issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `RequestBodyEmptyArray` — Error returned when the request body contains an empty array where data is expected.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional validation information about the empty array error.
          - `api_name` (string) **REQ** [maxLen=255] — API name of the field that is empty
          - `json_path` (string) **REQ** [maxLen=1000] — JSON path of the field that is empty
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the empty array issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

- **403**: Forbidden - The request requires the ZohoCRM.settings.unsubscribe.CREATE scope. The submission_action_type field is mandatory when submission_action_type is not provided. [application/json]
    > Wrapped error response containing an array of unsubscribe link errors returned when a required field is missing.
    - `unsubscribe_links` (array of object `MandatoryFieldMissingError`) [maxItems=25] **REQ** — Represents the list of error objects for unsubscribe links in this response.

**Scopes:** ZohoCRM.settings.unsubscribe.CREATE

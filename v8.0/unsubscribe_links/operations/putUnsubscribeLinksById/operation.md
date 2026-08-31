# PUT /settings/unsubscribe_links/{id}
**Operation:** `putUnsubscribeLinksById` — Update Unsubscribe Link by ID
> To update a specific unsubscribe link. You can modify the link's name, page type, custom URL, standard page message, submission action type, redirect URL, or submission message.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: The unique ID of the unsubscribe link to retrieve, update, or delete. This ID is returned in the response when creating or fetching unsubscribe links.

**Request Body** — application/json `UnsubscribeLinkModificationByIdRequest`
> Request body containing the unsubscribe link configuration to update. The id field is mandatory to identify which link to update.
  > Request payload to update an unsubscribe link identified by its ID.
  - `unsubscribe_links` (array of object `UnsubscribeLinkSingleUpdateItem`) [maxItems=1] **REQ** — Array containing the unsubscribe link configuration to update (required)
    schema: `UnsubscribeLinkSingleUpdateItem`
    - `submission_message` (string) [maxLen=2000] — Represents the message displayed when the user clicks the unsubscribe button. Required when submission_action_type is display_message. unsubscribe button. Required when submission_action_type is display_message.
    - `submission_redirect_url` (string) [maxLen=255] — Represents the URL to redirect users to after unsubscribing. Required when submission_action_type is redirect. Required when submission_action_type is redirect.
    - `page_type` (string) [maxLen=255] — Specifies where the unsubscribe page is hosted: standard (Zoho CRM page) or custom (your own webpage)
    - `custom_location_url` (string) [maxLen=255] — Represents the custom webpage URL for hosting the unsubscribe link. Required when page_type is custom. Required when page_type is custom. Required when page_type is custom.
    - `name` (string) [maxLen=255] — Represents the unique name for the unsubscribe link
    - `id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the unsubscribe link
    - `standard_page_message` (string) [maxLen=2000] — The message displayed on the standard unsubscribe page. Can be rich text (HTML) or plain text.
    - `submission_action_type` (string) [maxLen=255] — The action after unsubscribe: display_message (show a message) or redirect (redirect to a URL)
    additionalProperties: any

**Responses:**

- **200**: Success - Unsubscribe link updated successfully — Schema: `UpdateUnsubscribeLinksSuccessResponse` [application/json]
    > Success response for a PUT request that returns the action status of each updated unsubscribe link.
    schema: `UpdateUnsubscribeLinksSuccessResponse`
    - `unsubscribe_links` (array of object `UnsubscribeLinkActionStatus`) [maxItems=1] — Array containing the status of the update operation for each link
      schema: `UnsubscribeLinkActionStatus`
      - `code` (string) [maxLen=255] — The result code (SUCCESS or error code)
      - `details` (object `ActionEntityReference`) — Reference to the entity affected by an operation, containing its unique identifier.
        schema: `ActionEntityReference`
        - `id` (string) [maxLen=19] — The unique identifier of the affected unsubscribe link
      - `message` (string) [maxLen=255] — Represents the message describing the operation result.
      - `status` (string) [maxLen=255] — The status of the operation (success or error)

- **400**: Bad Request - Invalid data provided or the unsubscribe link ID is not part of your organization. Check field types, dependencies, or refer to the Input JSON keys section in the help doc. [application/json]
    > Validation error response for the PUT by ID request, covering invalid data type, empty array, missing required fields, and not-allowed or invalid ID errors.
    anyOf:
      - `InvalidDataTypeError` — Error returned when the data type provided for a field does not match the expected type.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional validation information about the invalid data type error.
          - `maximum_length` (integer/int32) **REQ** — The maximum allowed length for this field
          - `api_name` (string) **REQ** [maxLen=255] — The API name of the invalid field
          - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the invalid field
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the invalid data type issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `RequestBodyEmptyArray` — Error returned when the request body contains an empty array where data is expected.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional validation information about the empty array error.
          - `api_name` (string) **REQ** [maxLen=255] — API name of the field that is empty
          - `json_path` (string) **REQ** [maxLen=1000] — JSON path of the field that is empty
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the empty array issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `RequestBodyNotFoundError` — Error returned when the request body is missing or not found in the request.
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional validation information about the missing request body error.
          - `api_name` (string) **REQ** [maxLen=255] — The API name of the missing field
          - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the missing field
        - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message describing the missing request body.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `NotAllowedUnsubscribeLinkIdError` — Error returned when attempting to update or delete the default unsubscribe link, which is not allowed.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional validation information about the not-allowed operation on a default link.
          - `resource_path_index` (integer/int32) **REQ** — The index position in the URL path where the default link ID was found
        - `message` (string) **REQ** [enum=['The given Unsubscribe Link id is Default']] — Represents the error message describing the not-allowed operation on a default unsubscribe link.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `InvalidUnsubscribeLinkIdError` — Error returned when an invalid unsubscribe link ID is provided that does not belong to your organization.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional validation information about the invalid unsubscribe link ID error.
          - `resource_path_index` (integer/int32) **REQ** — The index position in the URL path where the invalid ID was found
        - `message` (string) **REQ** [enum=['The given Unsubscribe Link id is not part of Org']] — Represents the error message describing the invalid ID issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
        - `unsubscribe_links` (array of object) [maxItems=25] **REQ** — Represents the list of individual error objects for the unsubscribe link in the update-by-ID request.
          anyOf:
            - `UnsupportedPageTypeError` — Error returned when an unsupported value is provided for the page_type field. Supported values are 'standard' and 'custom'.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional validation information about the unsupported value error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field with the unsupported value
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the field with the unsupported value
                - `supported_values` (array of string) [maxItems=25] **REQ** — The list of supported values for this field
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['the given module is not supported in create or update']] — Represents the error message describing the unsupported value issue.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
            - `DuplicateDataError` — Error returned when attempting to create an unsubscribe link with a name that already exists in your account.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional validation information about the duplicate data error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field with duplicate data
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the field with duplicate data
              - `message` (string) **REQ** [enum=['Unsubscribe Link name already exists']] — Represents the error message describing the duplicate data issue.
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
            - `InvalidCustomLocationURLError` — Error returned when the custom location URL provided is invalid or does not match the expected website format.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional validation information about the invalid custom location URL error.
                - `expected_data_type` (string) **REQ** [maxLen=255] — The expected data type (e.g., website)
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the invalid field
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the invalid field
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the invalid URL issue.
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
            - `InvalidDataErrorType` — Error returned when invalid data is provided for a field. The response includes supported values when applicable.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional validation information about the invalid data error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the invalid field
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the invalid field
                - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of valid values for this field
                  items: [maxLen=255]
              - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid value issue.
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
            - `MandatoryFieldMissingError` — Error returned when a required mandatory field is missing from the request.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this response.
              - `details` (object) **REQ** — Contains additional validation information about the missing mandatory field error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing mandatory field
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the missing mandatory field
              - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message describing the missing mandatory field.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

**Scopes:** ZohoCRM.settings.unsubscribe.UPDATE

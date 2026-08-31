# PUT /settings/variable_groups
**Operation:** `updateVariableGroups` — Variable Groups
> To update the details of one or more variable groups in your Zoho CRM organization. The request accepts a maximum of 10 variable group items. When individual items succeed or fail independently, the API returns a 207 multi-status response with per-item results.

**Schemas:**
`VariableGroupFieldPathDetails`:
  > Represents the field path details returned in per-item operation results, providing context about which field the result pertains to.
  - `id` (string) [maxLen=255] — Represents the unique ID of the variable group field that the operation result refers to.
  - `api_name` (string) [maxLen=255] — Represents the API name of the variable group field that the operation result refers to.
`VariableGroupOperationStatus`:
  > Represents the per-item operation result for a variable group action, including the status code, message, and optional field path details.
  - `code` (string) [maxLen=255] — Represents the status code for the individual variable group operation result.
  - `details` (object `VariableGroupFieldPathDetails`) — Represents the field path details returned in per-item operation results, providing context about which field the result pertains to.
  - `message` (string) [maxLen=255] — Represents the message describing the result of the individual variable group operation.
  - `status` (string) [maxLen=255] — Represents the status of the individual variable group operation result.

**Request Body** — application/json `VariableGroupUpdateRequestAlt`
> Accepts a JSON request body containing an array of up to 10 variable group items to update.
  > Represents the request body for the bulk update variable groups operation.
  - `variable_groups` (array of object `VariableGroupUpdateItemAlt`) [minItems=1, maxItems=10] **REQ** — Represents an array of variable group update items for batch processing. The array accepts 1 to 10 items.
    schema: `VariableGroupUpdateItemAlt`
    - `name` (string) [maxLen=50, nullable] — Represents the updated display name for the variable group. This field is nullable.
    - `description` (string) [maxLen=3000, nullable] — Represents the updated description for the variable group. This field is nullable.
    - `id` (string) **REQ** [maxLen=18] — Represents the unique ID of the variable group to update.
    - `api_name` (string) [maxLen=100, nullable] — Represents the API name to update for the variable group. This field is nullable.

**Responses:**

- **200**: Returns the operation statuses for all updated variable groups when all items succeed. — Schema: `VariableGroupCollectionResponse` [application/json]
    > Represents the response body for a successful variable group update operation.
    schema: `VariableGroupCollectionResponse`
    - `variable_groups` (array of object `VariableGroupOperationStatus`) [maxItems=1] — Represents an array of per-item operation status objects returned after processing the update request.

- **207**: Returns a multi-status response when individual variable group items in the bulk update have different outcomes, with per-item success or error results. — Schema: `VariableGroupMultiStatusResponseAlt` [application/json]
    > Represents the multi-status response body returned when individual variable group items in a bulk update operation have different outcomes.
    schema: `VariableGroupMultiStatusResponseAlt`
    - `variable_groups` (array of object) [maxItems=2] — Represents an array of per-item results for the bulk update operation, where each item can be a success or an error response.
      oneOf:
        - `VariableGroupOperationStatus` — Represents the per-item operation result for a variable group action, including the status code, message, and optional field path details.
        - `ErrorResponseCore1117753881` — Represents an error response returned when duplicate data is detected for a variable group item in a multi-status response.
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code **DUPLICATE_DATA**.
          - `details` (object) **REQ** — Represents the validation details for the duplicate field.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains the duplicate value.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field that contains the duplicate value.
          - `message` (string) **REQ** [enum=['duplicate data']] — Represents the error message indicating that duplicate data was detected.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

- **400**: Returns an error response when the request contains invalid or missing data.
**Resolution:** Verify that all field values are valid and each ID refers to a user-defined variable group. [application/json]
    > Represents an error response returned when the bulk update variable groups request fails validation.
    oneOf:
      - `InvalidVariableGroupsTypeError` — Represents an error response returned when the `variable_groups` field in the request contains an invalid data type or format.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code **INVALID_DATA**.
        - `details` (object) **REQ** — Represents the validation details for the field with the invalid data type or value.
          - `maximum_length` (integer/int32) — Represents the maximum allowed length for the field that exceeded the limit.
          - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains invalid data.
          - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field that contains invalid data.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message indicating that the `variable_groups` field contains invalid data.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
        - `variable_groups` (array of object) [maxItems=25] **REQ** — Represents an array of error objects, one for each variable group item in the request that failed validation.
          oneOf:
            - `DuplicateVariableGroupError` — Represents an error response returned when duplicate data is detected for one or more variable groups in the request.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code **DUPLICATE_DATA**.
              - `details` (object) **REQ** — Represents the validation details for the duplicate field that caused the error.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains the duplicate value.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field that contains the duplicate value.
              - `message` (string) **REQ** [enum=['duplicate data']] — Represents the error message indicating that duplicate data was detected.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `SystemVariableGroupActionNotAllowedError` — Represents an error response returned when an update operation targets a system-defined variable group that does not support modification.
              - `code` (string) **REQ** [enum=['CANNOT_PERFORM_ACTION']] — Represents the error code **CANNOT_PERFORM_ACTION**.
              - `details` (object) **REQ** — Represents the validation details for the system-defined variable group that does not support the operation.
                - `api_name` (string) [maxLen=255] — Represents the API name of the system-defined variable group that does not support the operation.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field referencing the system-defined variable group.
              - `message` (string) **REQ** [enum=['the given operation is not supported for system defined variable group']] — Represents the error message indicating that the operation is not supported for system-defined variable groups.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `MandatoryFieldIdMissingError` — Represents an error response returned when the required `id` field is missing from the request body.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code **MANDATORY_NOT_FOUND**.
              - `details` (object) **REQ** — Represents the validation details for the missing required `id` field.
                - `api_name` (string) [maxLen=255] — Represents the API name of the missing required field.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the missing required field.
              - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message indicating that the required field was not found.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `ApiNamePatternMismatchError` — Represents an error response returned when the `api_name` value does not comply with the required naming pattern.
              - `code` (string) **REQ** [enum=['PATTERN_NOT_MATCHED']] — Represents the error code **PATTERN_NOT_MATCHED**.
              - `details` (object) **REQ** — Represents the validation details for the field that caused the pattern mismatch error.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the pattern mismatch.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field that caused the pattern mismatch.
              - `message` (string) **REQ** [enum=['Please check whether the input values are correct']] — Represents the error message indicating that the input value does not match the required naming pattern.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `InvalidVariableGroupIdError` — Represents an error response returned when the provided variable group ID in the request body is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code **INVALID_DATA**.
              - `details` (object) **REQ** — Represents the validation details for the field that contains the invalid variable group ID.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains the invalid variable group ID.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field that contains the invalid variable group ID.
              - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message indicating that the provided variable group ID is invalid.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `ProcessingAmbiguityError` — Represents an error response returned when ambiguity occurs while processing the request, typically when conflicting field references are detected in the same batch.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code **AMBIGUITY_DURING_PROCESSING**.
              - `details` (object) **REQ** — Represents the validation details containing the list of fields that caused the processing ambiguity.
                - `ambiguity_due_to` (array of object) [maxItems=25] — Represents an array of field references that caused the processing ambiguity.
                  - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the processing ambiguity.
                  - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field that caused the processing ambiguity.
              - `message` (string) **REQ** [enum=['Ambiguity while processing the request']] — Represents the error message indicating that ambiguity occurred during request processing.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `MandatoryFieldMissingError` — Represents an error response returned when a required field is missing from the request body.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code **MANDATORY_NOT_FOUND**.
              - `details` (object) **REQ** — Represents the validation details for the missing required field.
                - `api_name` (string) [maxLen=255] — Represents the API name of the missing required field.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the missing required field.
              - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message indicating that a required field is missing from the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `InvalidFieldDataTypeError` — Represents an error response returned when one or more fields contain values with an invalid data type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code **INVALID_DATA**.
              - `details` (object) **REQ** — Represents the validation details for the field with an invalid data type.
                - `expected_data_type` (string) [maxLen=255] — Represents the expected data type for the field that contains an invalid value.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field with the invalid data type.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field with the invalid data type.
              - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message indicating that one or more fields contain values with an invalid data type.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `InvalidDataError` — Represents an error response returned when the request contains invalid data for a field.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code **INVALID_DATA**.
              - `details` (object) **REQ** — Represents the validation details for the field that contains invalid data.
                - `maximum_length` (integer/int32) — Represents the maximum allowed length for the field that exceeded the limit.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains invalid data.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field that contains invalid data.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message indicating that the request contains invalid data.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

- **403**: Returns an error response when the client does not have the required permissions.
**Resolution:** Ensure the OAuth token includes the `ZohoCRM.settings.variable_groups.UPDATE` scope. — Schema: `PermissionDeniedError` [application/json]
    > Represents an error response returned when the client does not have the required permissions to access the variable group settings.
    schema: `PermissionDeniedError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code **NO_PERMISSION**.
    - `details` (object) **REQ** — Represents the validation details containing the list of permissions required to access this resource.
      - `permissions` (array of string) [maxItems=25] — Represents an array of permission names required to perform this operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message indicating that access to the resource is denied.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

**Scopes:** ZohoCRM.settings.variable_groups.UPDATE

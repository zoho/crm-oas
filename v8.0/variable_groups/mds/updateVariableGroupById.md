# PUT /settings/variable_groups/{id}
**Operation:** `updateVariableGroupById` — Update variable group by ID
> To update the details of a specific variable group by its ID in your Zoho CRM organization.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: Specifies the unique ID of the variable group to retrieve or update.

**Request Body** — application/json `VariableGroupDefinitionRequestAlt`
> Accepts a JSON request body containing the updated variable group fields for the specified variable group.
  > Represents the request body for updating a variable group by ID.
  - `variable_groups` (array of object `VariableGroupDefinitionInputAlt`) [minItems=1, maxItems=1] **REQ** — Represents an array containing a single variable group definition item for the update by ID operation.
    schema: `VariableGroupDefinitionInputAlt`
    - `name` (string) [maxLen=50, nullable] — Represents the display name of the variable group. This field is nullable.
    - `description` (string) [maxLen=3000, nullable] — Represents the description of the variable group. This field is nullable.
    - `api_name` (string) [maxLen=100, nullable] — Represents the API name for the variable group. The value must comply with the required naming pattern. This field is nullable.

**Responses:**

- **200**: Returns the operation status for the updated variable group. — Schema: `VariableGroupOperationResponse` [application/json]
    > Represents the response body for a successful update variable group by ID operation.
    schema: `VariableGroupOperationResponse`
    - `variable_groups` (array of object `VariableGroupOperationStatus`) [maxItems=1] — Represents an array containing the per-item operation status for the updated variable group.
      schema: `VariableGroupOperationStatus`
      - `code` (string) [maxLen=255] — Represents the status code for the individual variable group operation result.
      - `details` (object `VariableGroupFieldPathDetails`) — Represents the field path details returned in per-item operation results, providing context about which field the result pertains to.
        schema: `VariableGroupFieldPathDetails`
        - `id` (string) [maxLen=255] — Represents the unique ID of the variable group field that the operation result refers to.
        - `api_name` (string) [maxLen=255] — Represents the API name of the variable group field that the operation result refers to.
      - `message` (string) [maxLen=255] — Represents the message describing the result of the individual variable group operation.
      - `status` (string) [maxLen=255] — Represents the status of the individual variable group operation result.

- **400**: Returns an error response when the request contains invalid or missing data.
**Resolution:** Verify that all field values are valid and the ID refers to a user-defined variable group. [application/json]
    > Represents an error response returned when the update variable group by ID request fails validation.
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
            - `ApiNamePatternMismatchError` — Represents an error response returned when the `api_name` value does not comply with the required naming pattern.
              - `code` (string) **REQ** [enum=['PATTERN_NOT_MATCHED']] — Represents the error code **PATTERN_NOT_MATCHED**.
              - `details` (object) **REQ** — Represents the validation details for the field that caused the pattern mismatch error.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the pattern mismatch.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field that caused the pattern mismatch.
              - `message` (string) **REQ** [enum=['Please check whether the input values are correct']] — Represents the error message indicating that the input value does not match the required naming pattern.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `SystemVariableGroupActionNotAllowedError` — Represents an error response returned when an update operation targets a system-defined variable group that does not support modification.
              - `code` (string) **REQ** [enum=['CANNOT_PERFORM_ACTION']] — Represents the error code **CANNOT_PERFORM_ACTION**.
              - `details` (object) **REQ** — Represents the validation details for the system-defined variable group that does not support the operation.
                - `api_name` (string) [maxLen=255] — Represents the API name of the system-defined variable group that does not support the operation.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field referencing the system-defined variable group.
              - `message` (string) **REQ** [enum=['the given operation is not supported for system defined variable group']] — Represents the error message indicating that the operation is not supported for system-defined variable groups.
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
      - `InvalidIdentifierError` — Represents an error response returned when the provided ID in the request path is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code **INVALID_DATA**.
        - `details` (object) **REQ** — Represents the validation details indicating the path segment that contains the invalid identifier.
          - `resource_path_index` (integer/int32) — Represents the index of the resource path element that contains the invalid ID.
        - `message` (string) **REQ** [enum=['Invalid ID']] — Represents the error message indicating that the provided ID is invalid.
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

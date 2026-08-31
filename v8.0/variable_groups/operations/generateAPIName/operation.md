# POST /settings/variable_groups/actions/generate_api_name
**Operation:** `generateAPIName` — Generate API Name
> To generate an available API name for a new variable group in your Zoho CRM organization. Submit the proposed display name in the request, and the API returns a suggested `api_name` that complies with the naming requirements.

**Schemas:**
`InvalidVariableGroupsTypeError`:
  > Represents an error response returned when the `variable_groups` field in the request contains an invalid data type or format.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code **INVALID_DATA**.
  - `details` (object) **REQ** — Represents the validation details for the field with the invalid data type or value.
    - `maximum_length` (integer/int32) — Represents the maximum allowed length for the field that exceeded the limit.
    - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains invalid data.
    - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field that contains invalid data.
  - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message indicating that the `variable_groups` field contains invalid data.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

**Request Body** — application/json `ApiNameGenerationRequestAlt`
> Accepts a JSON request body containing the proposed variable group name for which an available API name is generated.
  > Represents the request body for the generate API name operation.
  - `variable_groups` (array of object `VariableGroupApiNameGenerationItemAlt`) [minItems=1, maxItems=1] **REQ** — Represents an array containing a single variable group item submitted for API name generation.
    schema: `VariableGroupApiNameGenerationItemAlt`
    - `name` (string) **REQ** [maxLen=50] — Represents the proposed name of the variable group for which an available API name is generated.

**Responses:**

- **200**: Returns the generated API name for each submitted variable group. — Schema: `ApiNameGenerationResponse` [application/json]
    > Represents the response body for a successful generate API name operation.
    schema: `ApiNameGenerationResponse`
    - `variable_groups` (array of object `VariableGroupOperationStatus`) [maxItems=1] — Represents an array of per-item results containing the generated API names for each submitted variable group.
      schema: `VariableGroupOperationStatus`
      - `code` (string) [maxLen=255] — Represents the status code for the individual variable group operation result.
      - `details` (object `VariableGroupFieldPathDetails`) — Represents the field path details returned in per-item operation results, providing context about which field the result pertains to.
        schema: `VariableGroupFieldPathDetails`
        - `id` (string) [maxLen=255] — Represents the unique ID of the variable group field that the operation result refers to.
        - `api_name` (string) [maxLen=255] — Represents the API name of the variable group field that the operation result refers to.
      - `message` (string) [maxLen=255] — Represents the message describing the result of the individual variable group operation.
      - `status` (string) [maxLen=255] — Represents the status of the individual variable group operation result.

- **400**: Returns an error response when the request contains missing or invalid data.
**Resolution:** Ensure all required fields are present and contain valid values. [application/json]
    > Represents an error response returned when the generate API name request fails validation.
    oneOf:
      - `InvalidVariableGroupsTypeError` — Represents an error response returned when the `variable_groups` field in the request contains an invalid data type or format.
        - `variable_groups` (array of object) [maxItems=25] **REQ** — Represents an array of error objects, one for each variable group item in the request that failed validation.
          oneOf:
            - `MandatoryFieldIdMissingError` — Represents an error response returned when the required `id` field is missing from the request body.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code **MANDATORY_NOT_FOUND**.
              - `details` (object) **REQ** — Represents the validation details for the missing required `id` field.
                - `api_name` (string) [maxLen=255] — Represents the API name of the missing required field.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the missing required field.
              - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message indicating that the required field was not found.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `InvalidVariableGroupsTypeError` — Represents an error response returned when the `variable_groups` field in the request contains an invalid data type or format.
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
**Resolution:** Ensure the OAuth token includes the `ZohoCRM.settings.variable_groups.CREATE` scope. — Schema: `PermissionDeniedError` [application/json]
    > Represents an error response returned when the client does not have the required permissions to access the variable group settings.
    schema: `PermissionDeniedError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code **NO_PERMISSION**.
    - `details` (object) **REQ** — Represents the validation details containing the list of permissions required to access this resource.
      - `permissions` (array of string) [maxItems=25] — Represents an array of permission names required to perform this operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message indicating that access to the resource is denied.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

**Scopes:** ZohoCRM.settings.variable_groups.CREATE

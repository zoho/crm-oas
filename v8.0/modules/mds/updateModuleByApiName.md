# PUT /settings/modules/{moduleIdentifier}
**Operation:** `updateModuleByApiName` — Update Module Labels and Profiles
> Updates the singular label, plural label, and profile assignments for the module identified by {moduleIdentifier}. Immutable fields such as access_type and api_name cannot be changed; attempting to include them returns a NOT_ALLOWED error

**Parameters:**
- `moduleIdentifier` (path, object, required): Specify the module identifier, either the numeric module ID or the module API name(case-sensitive).

**Request Body** (required) — application/json
> Payload for updating a module. Provide the module ID, updated singular and plural labels, and the list of profiles that should have access. access_type is not accepted in this request.
  > Request body schema for updating a module. Contains a single-element modules array with the module ID, updated labels, and profile assignments
  - `modules` (array of object) [minItems=1, maxItems=1] **REQ** — Single-element array containing the module object with the labels and profile assignments to update. Exactly one item is required.
    - `singular_label` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z0-9 ]+$] — Singular display label for the module. Accepts 1–50 alphanumeric characters and spaces; special characters are not permitted.
    - `plural_label` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z0-9 ]+$] — Plural display label for the module. Accepts 1–50 alphanumeric characters and spaces; special characters are not permitted.
    - `id` (string/int64) **REQ** — Unique numeric identifier of the module to update. Must match an existing module. Represented as a numeric string encoding a 64-bit positive integer (Java long/DB bigint).
    - `profiles` (array of object) [minItems=1, maxItems=203, uniqueItems] **REQ** — Non-empty list of unique profiles that should have access to this module. Accepts 1–203 unique profile objects; order is not significant. This cannot be empty.
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique numeric identifier of the profile. Represented as a numeric string encoding a 64-bit positive integer.

**Responses:**

- **200**: Module updated successfully. The response contains the updated module ID and a success confirmation [application/json]
    > Response body schema for a successful module update. Contains a single-element module array with the outcome code, updated module ID, confirmation message, and status
    - `modules` (array of object) [minItems=1, maxItems=1] **REQ** — Single-element array containing the success result for the updated module.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Always "SUCCESS". Indicates the module update completed without errors.
      - `details` (object) **REQ** — Contains the identifier of the successfully updated module.
        - `id` (string/int64) **REQ** — Unique numeric identifier of the successfully updated module. Represented as a numeric string encoding a 64-bit positive integer(Java long/DB bigint).
      - `message` (string) **REQ** [enum=['module updated successfully']] — Displays the success message and confirms that the update was applied.
      - `status` (string) **REQ** [enum=['success']] — Indicates that the operation completed successfully.

- **400**: Bad request. Returned when the module identifier is invalid, a field value fails validation, a required field is missing, a value is duplicated, a restricted field is included, a field does not meet minimum data requirements, or the API version does not support this endpoint [application/json]
    > Contains the error response for a failed module update request.
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Always "INVALID_MODULE". Returned when the specified module does not exist or the path parameter does not match any module.
        - `details` (object) **REQ** — Contains the index of the invalid resource in the URL path.
          - `resource_path_index` (integer/int32) **REQ** [min=0] — Represents the index of the invalid resource in the URL path (0-based). Typically 2 for the {api_name} parameter.
        - `message` (string) **REQ** [maxLen=1000] — Explains why the module reference supplied in the request is invalid.
        - `status` (string) **REQ** [enum=['error']] — Always "error". Indicates the request failed.
        - `modules` (array of object) [minItems=1, maxItems=1] **REQ** — One-element array containing the error detail object for the INVALID_DATA failure. Always contains exactly one entry.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Always "INVALID_DATA". Returned when a field value fails format, length, or type validation.
          - `details` (object) **REQ** — Error details identifying the invalid field and its location in the request body. May also include the maximum allowed length or expected data type depending on the violation.
            - `maximum_length` (integer/int32) [min=1] — Maximum permitted character length for the field. Present only when the validation failure is caused by a length constraint violation.
            - `expected_data_type` (string) [maxLen=50] — Expected data type for the field. Present only when the validation failure is caused by a type mismatch. Maximum 50 characters.
            - `api_name` (string) **REQ** [maxLen=50] — API name of the field that failed validation. Maximum 50 characters.
            - `json_path` (string) **REQ** [maxLen=100] — JSONPath expression identifying the location of the invalid field in the request body. Maximum 100 characters.
          - `message` (string) **REQ** [maxLen=1000] — Explains the validation failure for this field.
          - `status` (string) **REQ** [enum=['error']] — Always "error". Indicates the request failed.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Always "API_NOT_SUPPORTED". Returned when the requested endpoint is not supported by the current API version.
        - `details` (object) **REQ** — Object containing additional information about the API version incompatibility, including the minimum supported version for this endpoint.
          - `supported_version` (integer/int32) **REQ** [min=1] — Minimum API version number that supports this endpoint. The caller must use this version or higher.
        - `message` (string) **REQ** [maxLen=1000] — Explains why the current API version does not support this endpoint.
        - `status` (string) **REQ** [enum=['error']] — Always "error". Indicates the request failed.
        - `modules` (array of object) [minItems=1, maxItems=1] **REQ** — One-element array containing the error detail object for the MANDATORY_NOT_FOUND failure.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Always "MANDATORY_NOT_FOUND". Returned when a required field is missing or empty in the request.
          - `details` (object) **REQ** — Identifies the missing required field by its API name and its JSONPath location in the request body.
            - `api_name` (string) **REQ** [maxLen=50] — API name of the required field that is missing from the request. Maximum 50 characters.
            - `json_path` (string) **REQ** [maxLen=100] — JSONPath expression identifying the location in the request body where the required field is absent. Maximum 100 characters.
          - `message` (string) **REQ** [maxLen=1000] — Indicates which required field is absent from the request.
          - `status` (string) **REQ** [enum=['error']] — Always "error". Indicates the request failed.
        - `modules` (array of object) [minItems=1, maxItems=1] **REQ** — One-element array containing the error detail object for the DUPLICATE_DATA failure.
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Always "DUPLICATE_DATA". Returned when a field value is duplicated where uniqueness is required.
          - `details` (object) **REQ** — Identifies the field with the duplicate value by its API name and its JSONPath location in the request body.
            - `api_name` (string) **REQ** [maxLen=50] — API name of the field that contains a duplicate value. Maximum 50 characters.
            - `json_path` (string) **REQ** [maxLen=100] — JSONPath expression identifying the location of the duplicate field in the request body. Maximum 100 characters.
          - `message` (string) **REQ** [maxLen=1000] — Explains the duplicate value error for this field.
          - `status` (string) **REQ** [enum=['error']] — Always "error". Indicates that the module update failed due to duplicate data being submitted
        - `modules` (array of object) [minItems=1, maxItems=1] **REQ** — Array of error objects, each describing a module field that was rejected because the update is not permitted
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Always "NOT_ALLOWED". Indicates that the specified field cannot be updated because it is immutable or write-restricted
          - `details` (object) **REQ** — Identifies the restricted field by its API name and its JSONPath location in the request body
            - `api_name` (string) **REQ** [maxLen=50] — API name of the restricted field that cannot be updated. Maximum 50 characters
            - `json_path` (string) **REQ** [maxLen=100] — JSONPath expression identifying the location of the restricted field in the request body. Maximum 100 characters
          - `message` (string) **REQ** [maxLen=1000] — Explains why the field update was rejected.
          - `status` (string) **REQ** [enum=['error']] — Always "error". Indicates the request failed because a restricted field was included in the update
        - `modules` (array of object) [minItems=1, maxItems=1] **REQ** — Array of error objects, each describing a module field whose submitted value does not satisfy minimum data requirements
          - `code` (string) **REQ** [enum=['MINIMUM_DATA_NOT_FOUND']] — Always "MINIMUM_DATA_NOT_FOUND". Indicates that a field is present but its value does not meet the minimum data requirement
          - `details` (object) **REQ** — Identifies the field that failed minimum data validation by its API name and its JSONPath location in the request body
            - `api_name` (string) **REQ** [maxLen=50] — API name of the field that failed the minimum data requirement. Maximum 50 characters
            - `json_path` (string) **REQ** [maxLen=100] — JSONPath expression identifying the location of the field in the request body. Maximum 100 characters
          - `message` (string) **REQ** [maxLen=1000] — Explains the minimum data requirement that was not satisfied for this field.
          - `status` (string) **REQ** [enum=['error']] — Always "error". Indicates the request failed because a field does not meet the minimum data requirement

**Scopes:** ZohoCRM.settings.modules.UPDATE

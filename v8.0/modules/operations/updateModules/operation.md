# PUT /settings/modules
**Operation:** `updateModules` — Update CRM modules
> Updates existing modules in the CRM. Allows modification of module labels (`singular_label`, `plural_label`) and profile assignments. Supports batch updates of up to 100 modules per request. Returns 200 when all modules update successfully, or 207 Multi-Status when some succeed and others fail. Module `access_type` cannot be updated and must not be included in the request body. This operation is idempotent - submitting the same request multiple times produces the same result.

**Request Body** (required) — application/json
> Request body for updating modules. Supports batch updates -
multiple modules can be updated in a single request. Partial updates
are supported: only `id` is required; `singular_label`,
`plural_label`, and `profiles` are optional and can be updated
independently. Profile updates use delta semantics: profiles without
`_delete: null` are added (if not already present), profiles with
`_delete: null` are removed. Batch updates may result in partial
success (207 Multi-Status response) if some modules succeed and others
fail. access_type is not accepted in PUT request payload and cannot be
changed."
  > Batch update request containing an array of module objects to update. Each module requires `id`; other fields are optional.
  - `modules` (array of object) [minItems=1, maxItems=100, uniqueItems] **REQ** — Array of module objects to update, with one to 100 unique entries. Each entry must include `id`; `singular_label`, `plural_label`, and `profiles` are optional.
    - `singular_label` (string) [maxLen=50, minLen=1] — Singular display label for the module shown in the UI while referring to a single record (for example, `Contact` or `Deal`). Must contain only alphanumeric characters and underscores, with no consecutive underscores, and cannot be empty.
    - `plural_label` (string) [maxLen=50, minLen=1] — Plural display label for the module shown in the UI while referring to multiple records (for example, `Contacts` or `Deals`). Must contain only alphanumeric characters and underscores, with no consecutive underscores, and cannot be empty.
    - `id` (string/int64) **REQ** — Unique identifier of the module to update. Must be a valid existing module ID.
    - `profiles` (array of object) [minItems=1, maxItems=203, uniqueItems] — Optional list of user profiles to add or remove from this module using delta semantics. Profiles without `_delete` are added; profiles with `_delete: null` are removed. Omit this to leave profile assignments unchanged.Each profile ID represents a permission set determining which users can view, create, edit, or delete records in this module.
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique numeric identifier of the user profile.
      - `_delete` (null) — Deletion marker. Set to `null` to remove this profile from the module's access list. Omit to add or retain the profile.

**Responses:**

- **200**: All modules in the batch updated successfully. Each entry in the `modules` array confirms the update with a `SUCCESS` code and the module ID. [application/json]
    > Successful batch update response containing one result object per updated module, each confirming the update with a `SUCCESS` code.
    - `modules` (array of object) [minItems=1, maxItems=100] **REQ** — Array of success results for each updated module in the batch, preserving request order.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Returns `SUCCESS` when the module updates without error.
      - `details` (object) **REQ** — Details of the successfully updated module, containing its unique identifier.
        - `id` (string/int64) **REQ** [minLen=1] — Unique identifier of the module that was successfully updated.
      - `message` (string) **REQ** [maxLen=1000, minLen=1] — Confirmation text returned when the module update succeeds.
      - `status` (string) **REQ** [enum=['success']] — Status indicator for successful operation

- **207**: Multi-Status - partial success. Returned when batch update contains both successful and failed module updates. Response includes individual status for each module in the request. [application/json]
    > Multi-status batch update response containing one result object per module in the request. Results preserve request order and include both successful and failed updates.
    - `modules` (array of object) [minItems=1, maxItems=100] **REQ** — Array of per-module results for each entry in the request, preserving request order. Each element is either a success or an error variant.
      oneOf:
          - `code` (string) **REQ** [enum=['SUCCESS']] — Success code indicating that module was updated
          - `details` (object) **REQ** — Success details containing the updated module ID
            - `id` (string/int64) **REQ** [minLen=1] — Unique identifier of the successfully updated module.
          - `message` (string) **REQ** [maxLen=1000, minLen=1] — Confirmation text returned for the module entry that succeeded.
          - `status` (string) **REQ** [enum=['success']] — Fixed value `success`, indicating this module's update succeeded in the partial batch.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Fixed value `INVALID_DATA`, indicating this module's update failed because the submitted data was invalid.
          - `details` (object) **REQ** — Represents the error details for the invalid field.
            oneOf:
                - `api_name` (string) **REQ** [maxLen=50, minLen=1] — API name of the field that received a value of an incorrect data type.
                - `json_path` (string) **REQ** [maxLen=100, minLen=1] — JSONPath locating the field in the request body that contained the incorrect data type.
                - `expected_data_type` (string) [maxLen=50] — Expected data type for the field
                - `index` (integer/int32) [min=0] — Zero-based index of the invalid parameter.
                - `supported_values` (array of string) [minItems=1, maxItems=10] — List of valid values accepted for the parameter.
                  items: [maxLen=50, minLen=1]
                - `param_name` (string) **REQ** [maxLen=50, minLen=1] — Name of the invalid parameter
                - `maximum_length` (integer/int32) **REQ** [min=1] — Maximum number of characters permitted for the field.
                - `api_name` (string) **REQ** [maxLen=50, minLen=1] — API name of the field whose value exceeded the maximum allowed length.
                - `json_path` (string) **REQ** [maxLen=100, minLen=1] — JSONPath of the field in the request whose value exceeded the maximum allowed length.
          - `message` (string) **REQ** [maxLen=1000, minLen=1] — Explanation of the validation failure for the module entry that contained invalid data.
          - `status` (string) **REQ** [enum=['error']] — Fixed value `error`, indicating the module update failed because the submitted data was invalid.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Fixed value `MANDATORY_NOT_FOUND`, indicating the module update failed because a required field was absent from the request.
          - `details` (object) **REQ** — Details identifying the required field that was missing, including its API name and JSONPath location.
            - `api_name` (string) **REQ** [maxLen=50, minLen=1] — API name of the required field that was not provided in the request.
            - `json_path` (string) **REQ** [maxLen=100, minLen=1] — JSONPath location in the request where the required field was expected.
          - `message` (string) **REQ** [maxLen=1000, minLen=1] — Explanation of the missing required field that caused the module entry to fail.
          - `status` (string) **REQ** [enum=['error']] — Fixed value `error`, indicating the module update failed because a mandatory field was missing.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Fixed value `NOT_ALLOWED`, indicating the module update failed because the request attempted to modify a field that cannot be changed.
          - `details` (object) **REQ** — Details identifying the restricted field that was included in the request, by API name and JSONPath.
            - `api_name` (string) **REQ** [maxLen=50, minLen=1] — API name of the field whose update is not permitted.
            - `json_path` (string) **REQ** [maxLen=100, minLen=1] — JSONPath location of the restricted field in the request.
          - `message` (string) **REQ** [maxLen=1000, minLen=1] — Explanation of the disallowed field modification that caused the module entry to be rejected, identifying which field cannot be changed.
          - `status` (string) **REQ** [enum=['error']] — Fixed value `error`, indicating the module update failed because a disallowed field modification was attempted.
          - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Fixed value `INVALID_MODULE`, indicating the module reference is invalid, does not exist, or the operation is not supported for this module type.
          - `details` (object) **REQ** — Details identifying the field or reference that caused the invalid-module error, by API name and JSONPath.
            - `api_name` (string) **REQ** [maxLen=50, minLen=1] — API name of the field or reference associated with the invalid module.
            - `json_path` (string) **REQ** [maxLen=100, minLen=1] — JSONPath to the invalid module reference in the request.
          - `message` (string) **REQ** [maxLen=1000, minLen=1] — Explanation of why the module identifier was not recognized or could not be updated.
          - `status` (string) **REQ** [enum=['error']] — Fixed value `error`, indicating the module update failed because the module reference is invalid or the operation is unsupported for this module type.

- **400**: Bad request - validation failure. Returned when input data fails validation (invalid module ID, unsupported field values, field length exceeded, missing required fields, attempting unsupported operations on system modules, attempting to update immutable fields such as access_type, or attempting to update profiles for a team-based module). No modules are updated when this error occurs. [application/json]
    > Validation error response for batch update failures. Returned when all modules in the request fail validation. No modules are updated when this error occurs.
    - `modules` (array of object) [minItems=1, maxItems=100] **REQ** — Error result objects for each module in the request, preserving request order. Present when all modules fail validation.
      oneOf:
          - `code` (string) **REQ** [enum=['INVALID_MODULE', 'INVALID_DATA']] — `INVALID_MODULE` indicates the module ID does not exist or is invalid; `INVALID_DATA` indicates a field value in the module payload is invalid.
          - `details` (object) **REQ** — Represents the error details about the invalid module reference.
            oneOf:
                - `api_name` (string) **REQ** [maxLen=50, minLen=1] — API name of the field or module reference that failed validation.
                - `json_path` (string) **REQ** [maxLen=100, minLen=1] — JSONPath to the invalid field or module reference in the request.
                - `resource_path_index` (integer/int32) **REQ** [min=0] — Zero-based index of the invalid module in the request array.
          - `message` (string) **REQ** [maxLen=1000, minLen=1] — Explanation of the validation error that caused the entire batch request to fail.
          - `status` (string) **REQ** [enum=['error']] — Fixed value `error`, indicating this module update failed.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Fixed value `INVALID_DATA`, indicating the module update failed because the submitted data was invalid.
          - `details` (object) **REQ** — Represents the error details for the invalid field.
            oneOf:
                - `index` (integer/int32) [min=0] — Zero-based position of the invalid value within the parameter array.
                - `supported_values` (array of string) [minItems=1, maxItems=10] — List of valid values accepted for the parameter
                  items: [maxLen=50, minLen=1]
                - `param_name` (string) **REQ** [maxLen=50, minLen=1] — Name of the parameter whose submitted value is not among the supported values.
                - `maximum_length` (integer/int32) [min=1] — Maximum number of characters permitted for the field.
                - `api_name` (string) **REQ** [maxLen=50, minLen=1] — API name of the field whose submitted value exceeded the maximum allowed character length.
                - `json_path` (string) **REQ** [maxLen=100, minLen=1] — JSONPath to the field whose value exceeded the maximum allowed length.
                - `api_name` (string) **REQ** [maxLen=50, minLen=1] — API name of the field that contains an invalid value.
                - `json_path` (string) **REQ** [maxLen=100, minLen=1] — JSONPath to the field that contains an invalid value.
          - `message` (string) **REQ** [maxLen=1000, minLen=1] — Explanation of the error for the specific module entry that triggered the batch failure.
          - `status` (string) **REQ** [enum=['error']] — Fixed value `error`, indicating this module update failed because the submitted data was invalid.
          - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Fixed value `NOT_SUPPORTED`, indicating this module update failed because the operation is not supported for this module type or is restricted for system modules.
          - `details` (object) **REQ** — Additional context for the NOT_SUPPORTED error. Typically an empty object when no supplemental detail is available.
          - `message` (string) **REQ** [maxLen=1000, minLen=1] — Explanation of why the operation is not supported for this module type or is restricted for system modules.
          - `status` (string) **REQ** [enum=['error']] — Fixed value `error`, indicating this module update failed because the operation is not supported.
          - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Fixed value `EXPECTED_FIELD_MISSING`, indicating required fields were expected in the request but not found.
          - `details` (object) **REQ** — Details listing the fields that were expected but absent, each identified by API name and JSONPath.
            - `expected_fields` (array of object) [minItems=1, maxItems=10] **REQ** — Fields that were expected in the request but missing, each identified by its API name and JSONPath location.
              - `api_name` (string) **REQ** [maxLen=50, minLen=1] — API name of the field that was expected in the request but absent.
              - `json_path` (string) **REQ** [maxLen=100, minLen=1] — JSONPath location in the request where the expected field was absent.
          - `message` (string) **REQ** [maxLen=1000, minLen=1] — Explanation of the expected fields that were absent from the request, causing the module entry to be rejected.
          - `status` (string) **REQ** [enum=['error']] — Fixed value `error`, indicating the update failed because expected fields were missing from the request.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Fixed value `NOT_ALLOWED`, indicating the update failed because the request attempted to modify a field that cannot be changed.
          - `details` (object) **REQ** — Details identifying the restricted field that was included in the request, by API name and JSONPath.
            - `api_name` (string) **REQ** [maxLen=50, minLen=1] — API name of the field whose update is not permitted.
            - `json_path` (string) **REQ** [maxLen=100, minLen=1] — JSONPath location of the restricted field in the request.
          - `message` (string) **REQ** [maxLen=1000, minLen=1] — Explanation of the immutable field violation that caused the module entry to fail.
          - `status` (string) **REQ** [enum=['error']] — Fixed value `error`, indicating the update failed because a disallowed field modification was attempted.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Fixed value `MANDATORY_NOT_FOUND`, indicating the update failed because a required field was not provided in the request.
          - `details` (object) **REQ** — Details identifying the required field that was absent from the request, by API name and JSONPath.
            - `api_name` (string) **REQ** [maxLen=50, minLen=1] — API name of the required field that was not provided.
            - `json_path` (string) **REQ** [maxLen=100, minLen=1] — JSONPath location in the request body where the missing mandatory field was expected.
          - `message` (string) **REQ** [maxLen=1000, minLen=1] — Explanation of the mandatory field that was missing from the request, causing the module update to fail.
          - `status` (string) **REQ** [enum=['error']] — Fixed value `error`, indicating the update failed because a mandatory field was not provided.
          - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Fixed value `DEPENDENT_FIELD_MISSING`, indicating a field required by the presence of another field was absent from the request.
          - `details` (object) **REQ** — Details identifying both the missing dependent field relationship.
            - `api_name` (string) **REQ** [maxLen=50, minLen=1] — API name of the dependent field that was absent from the request.
            - `json_path` (string) **REQ** [maxLen=100, minLen=1] — JSONPath location in the request where the dependent field was expected.
            - `dependee` (object) **REQ** — The field that requires the dependent field to be present
              - `api_name` (string) **REQ** [maxLen=50, minLen=1] — API name of the field that requires the dependent field.
              - `json_path` (string) **REQ** [maxLen=100, minLen=1] — JSONPath location of the field that requires the dependent field.
          - `message` (string) **REQ** [maxLen=1000, minLen=1] — Explanation of the dependent field relationship that was violated, identifying which field was missing and which field required its presence.
          - `status` (string) **REQ** [enum=['error']] — Fixed value `error`, indicating the module update failed due to a missing dependent field.
          - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Fixed value `API_NOT_SUPPORTED`, indicating the request used an API version below the minimum required for this operation.
          - `details` (object) **REQ** — Object indicating the minimum supported API version for this operation.
            - `supported_version` (integer/int32) **REQ** [min=1] — Minimum API version number required to perform this operation.
          - `message` (string) **REQ** [maxLen=1000, minLen=1] — Explanation of the API version requirement that the request failed to meet, including the minimum supported version.
          - `status` (string) **REQ** [enum=['error']] — Fixed value `error`, indicating the module update failed because the API version is not supported.

**Scopes:** ZohoCRM.settings.modules.UPDATE

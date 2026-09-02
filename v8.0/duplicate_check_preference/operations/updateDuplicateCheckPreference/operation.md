# PUT /settings/duplicate_check_preference
**Operation:** `updateDuplicateCheckPreference` — Update Duplicate Check Preference
> Update Duplicate Check Preference API is used to update duplicate check settings for a specific module in the CRM system. It allows users to define how duplicate records are identified and managed based on field mappings between the current module and a mapped module, such as Contacts. This API helps maintain data integrity by preventing the creation of duplicate records during data entry or import processes.

**Parameters:**
- `module` (query, string, required) [enum=['Leads']]: Represents the module whose Duplicate Check Preference details you want to retrieve.  Supported module: Leads.

**Request Body** (required) — application/json
> The request body must contain the duplicate_check_preference object. To update mapped_module_records, you must include type_configurations with the field_mappings array and the mapped_module details.
  > Represents the request payload used to update duplicate check preference.
  - `duplicate_check_preference` (object) **REQ** — Duplicate Check Preference details
    - `type` (string) **REQ** [enum=['mapped_module_records', 'converted_records']] — Type of duplicate check preference
    - `type_configurations` (array of object) [maxItems=1] **REQ** — Type configurations for duplicate check preference
      - `field_mappings` (array of object) **REQ** — Field mappings between the current module and the mapped module
        - `current_field` (object) **REQ** — Unique field in the current module to match on
          - `id` (string/int64) **REQ** — Field id of the current module field. The mapping is stored against this id, so it is mandatory.
          - `api_name` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the current module field. Validated when supplied, but the mapping is stored against id.
          - `name` (string) [maxLen=50] — Accepted for symmetry with the response and ignored by the API.
        - `mapped_field` (object) **REQ** — Unique field in the mapped module to match against
          - `id` (string/int64) **REQ** — Represents the ID of the mapped field. The mapping is stored against this id, so it is mandatory.
          - `api_name` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Mapped field API name. Validated when supplied, but the mapping is stored against id.
          - `name` (string) [maxLen=50] — Accepted for symmetry with the response and ignored by the API.
          - `selected` (string) [maxLen=4, enum=['None']] — Send None to delete the existing mapping for this current_field. Any other value, or omitting the property, adds or updates the mapping.
      - `mapped_module` (object) **REQ** — Mapped module details
        - `id` (string/int64) **REQ** — Represents the ID of the mapped module. The module must resolve to Contacts.
        - `name` (string) [maxLen=50] — Accepted for symmetry with the response and ignored by the API.
        - `api_name` (string) [maxLen=50] — Mapped module API name. Validated when supplied, but the module is resolved from id.

**Responses:**

- **200**: Returns a success response confirming that the API updated the duplicate check preference. [application/json]
    > Represents the success response returned after the API updates the duplicate check preference.
    - `duplicate_check_preference` (object) **REQ** — Duplicate Check Preference update response
      - `code` (string) [enum=['SUCCESS']] — Response code for successful update
      - `status` (string) [enum=['success']] — Status of the update operation
      - `message` (string) [maxLen=1000] — Represents the message regarding the update operation.
      - `details` (object) — Additional details about the update operation

- **400**: The request could not be processed because the duplicate check preference input is invalid or incomplete.
**Resolution:** The module query parameter and request body fields must contain valid supported values for this API. [application/json]
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Error status indicator.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for request-level failures.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Human-readable error message.
        - `details` (object) **REQ** — Contextual error details including field location.
          - `param_name` (string) **REQ** [maxLen=10] — Represents the param_name that caused the error, for example, module.
        - `status` (string) **REQ** [enum=['error']] — Error status indicator.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_SUPPORTED']] — Represents the error code for request-level failures.
        - `message` (string) **REQ** [enum=['Your License does not support this feature.']] — Represents the error message.
        - `details` (object) **REQ** — Contextual error details including field location.
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the error code for request-level failures.
        - `message` (string) **REQ** [enum=[2 values]] — Represents the error message.
        - `details` (object) **REQ** — Contextual error details including field location.
          - `param_name` (string) **REQ** [maxLen=10] — Represents the param_name that caused the error, for example, module.
          - `api_name` (string) [maxLen=50] — API name of the field with invalid data.
          - `json_path` (string) [maxLen=100] — JSONPath to the location of the invalid field.
        - `status` (string) **REQ** [enum=['error']] — Status indicator for error.
        - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Error code indicating parameter ambiguity.
        - `details` (object) **REQ** — Details about the ambiguous parameters.
          - `ambiguity_due_to` (array of object) [maxItems=2] **REQ** — Array of conflicting parameters that caused the ambiguity.
            - `api_name` (string) **REQ** [maxLen=10] — Represents the API field name that caused the error, for example, tab_groups.
            - `json_path` (string) **REQ** [maxLen=100] — Represents the JSONPath expression locating the error, for example, $.tab_groups.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message explaining the ambiguity.
        - `status` (string) **REQ** [enum=['error']] — Error status indicator.
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code indicating a mandatory field is missing
        - `details` (object) **REQ** — Error details with field location information
          - `api_name` (string) **REQ** [maxLen=50] — Name of the required field that is missing
          - `json_path` (string) **REQ** [maxLen=100] — JSONPath expression locating where the field should be in the request
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the missing required field.
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Error code indicating a dependent field is missing
        - `details` (object) **REQ** — Error details with field location information
          - `api_name` (string) **REQ** [maxLen=50] — Name of the dependent field that is missing
          - `json_path` (string) **REQ** [maxLen=100] — JSONPath expression locating where the field should be in the request
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the missing dependent field.
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Error code for missing expected field
        - `details` (object) **REQ** — Details about missing expected fields
          - `expected_fields` (array of object) [minItems=1, maxItems=10] **REQ** — List of fields that were expected but missing
            - `api_name` (string) **REQ** [maxLen=50, minLen=1] — API name of the expected field
            - `json_path` (string) **REQ** [maxLen=100, minLen=1] — JSONPath location where field was expected
        - `message` (string) **REQ** [maxLen=1000, minLen=1] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Status indicator for error
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating invalid or malformed data
        - `details` (object) **REQ** — Error details with field information
          - `maximum_length` (integer/int32) — Maximum allowed length for the field
          - `expected_data_type` (string) [maxLen=50] — Expected data type for the field
          - `api_name` (string) [maxLen=50] — Name of the field with invalid data
          - `json_path` (string) [maxLen=100] — JSONPath expression locating the invalid field in the request
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the invalid data.
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code indicating operation is not allowed
        - `details` (object) **REQ** — Error details with field location information
          - `api_name` (string) **REQ** [maxLen=50] — Name of the field or operation that is not allowed
          - `json_path` (string) **REQ** [maxLen=100] — JSONPath expression locating the not-allowed field or operation
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message explaining what is not allowed.
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code for unsupported operation
        - `details` (object) **REQ** — Additional error details (typically empty)
          - `param_name` (string) [maxLen=10] — Represents the param_name that caused the error, for example, module.
        - `message` (string) **REQ** [maxLen=1000, minLen=1] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Status indicator for error
        - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Error code for unsupported operation
        - `details` (object) **REQ** — Additional error details (typically empty)
          - `dependee` (object) — Represents the param_name that caused the error, for example, module.
            - `api_name` (string) **REQ** [maxLen=50] — API name of the dependee field
            - `json_path` (string) **REQ** [maxLen=100] — JSON path of the dependee field
          - `api_name` (string) [maxLen=50] — API name of the dependee field
          - `json_path` (string) [maxLen=100] — JSON path of the dependee field
        - `message` (string) **REQ** [maxLen=1000, minLen=1] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Status indicator for error
        - `duplicate_check_preference` (object) **REQ** — Error details for the duplicate_check_preference field
          - `code` (string) **REQ** [enum=[7 values]] — Error code for the field-level error
          - `details` (object) **REQ** — Error context including field path
            - `api_name` (string) [maxLen=100] — API name of the field that caused the error
            - `json_path` (string) [maxLen=500] — JSON path to the field that caused the error
            - `expected_data_type` (string) [maxLen=500] — Expected data type for the field that caused the error
            - `dependee` (object) — Error context including field path
              - `api_name` (string) [maxLen=100] — API name of the dependee field that caused the error
              - `json_path` (string) [maxLen=500] — JSON path to the dependee field that caused the error
          - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
          - `status` (string) **REQ** [enum=['error']] — Error status indicator

- **403**: No permission or feature not enabled [application/json]
    oneOf:
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code indicating permission denied
        - `details` (object) **REQ** — Additional error details
          - `permissions` (array of string) [maxItems=25] — List of required permissions
            items: [maxLen=255]
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Status indicator for error
        - `duplicate_check_preference` (object) **REQ** — Error details for the duplicate_check_preference field
          - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Error code indicating feature is not enabled
          - `details` (object) **REQ** — Additional error details (typically empty)
          - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
          - `status` (string) **REQ** [enum=['error']] — Error status indicator

**Scopes:** ZohoCRM.settings.duplicate_check_preference.UPDATE

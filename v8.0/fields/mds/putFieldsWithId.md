# PATCH /settings/fields/{fieldId}
**Operation:** `putFieldsWithId` — Update a custom field
> To update a specific custom field in a module in your Zoho CRM account by its unique field ID.

**Parameters:**
- `module` (query, string, required) [maxLen=30] {style=form, explode=True}: Module name passed as parameter is case insensitive. For example, the module name 'Leads'.
- `fieldId` (path, string/int64, required): Specify the unique ID of the custom field to update.

**Schemas:**
`ErrorResponse`:
  oneOf:
      - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the specific type or category of the error returned in the response.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ**
        oneOf:
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the field that triggered the error, used to identify the specific field within the Zoho CRM module.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `api_name` (string) **REQ** [maxLen=30] — Represents the API name of the global picklist.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `expected_data_type` (string) **REQ** [maxLen=25] — Represents the name of the expected_data_type.
            - `api_name` (string) **REQ** [maxLen=30] — Represents the API name of the global picklist.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path identifying the exact location of the offending field within the request payload.
            - `range` (object) **REQ** — Represents the name of the expected_data_type.
              - `from` (integer/int32) — Represents the start of the expected data type range.
              - `to` (integer/int32) — Represents the end of the expected data type range.
            - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path.
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `supported_values` (array of object) [minItems=1, maxItems=25] **REQ** — Represents the list of supported values accepted for the JSON key identified by **api_name** and **json_path**.
              oneOf:
                  type: string [maxLen=255] — Represents the string values that can be present.
                  type: boolean — Represents a Boolean value that can be present in the supported values list.
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `allowed_values` (array of string) [minItems=1, maxItems=25] **REQ** — Represents the list of allowed values accepted for the JSON key identified by **api_name** and **json_path**.
              items: [maxLen=255]
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `maximum_length` (integer/int32) **REQ** — Represents the maximum lenght allowed.
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `minimum_length` (integer/int32) **REQ** — Represents the minimum length allowed.
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `supported_values` (array of string) [minItems=1, maxItems=25] **REQ** — Represents the list of supported values accepted for the JSON key identified by **api_name** and **json_path**.
              items: [maxLen=255]
            - `expected_data_type` (string) **REQ** [maxLen=25] — Represents the name of the expected_data_type.
      - `status` (string) **REQ** [enum=['error']] — Represents the response status.
      - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the invalid module details.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) **REQ** [enum=['DYNAMIC_EXPRESSION_LENGTH_EXCEEDED']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the length Exceeded details.
        - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
        - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
        - `dependee` (object) **REQ** — Represents the maximum length allowed.
          - `api_name` (string) [maxLen=25] — Represents the API name of the global picklist.
          - `json_path` (string) [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
      - `status` (string) **REQ** [enum=['error']] — Represents the response status.
      - `code` (string) **REQ** [enum=['SYNTAX_ERROR']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000, enum=['Formula expression has syntax error']] — Represents the error message describing the issue.
      - `details` (object) **REQ**
        oneOf:
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the field with syntax error.
            - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field with duplicate data.
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the field with syntax error.
            - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field with duplicate data.
            - `id` (string/int64) **REQ** — Represents the id of the field with duplicate data.
      - `status` (string) **REQ** [enum=['error']] — Represents the response status.
      - `code` (string) **REQ** [enum=['ALREADY_USED']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the details of the field that is already used.
        - `exists_in` (object) — Represents the field due to which dependent fields are expected.
          - `api_name` (string) [maxLen=30] — Represents the API name of the followed field.
          - `json_path` (string) [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
        - `api_name` (string) [maxLen=25] — Represents the API name of the global picklist.
        - `json_path` (string) [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000, enum=['Duration Configuration enhancement not enabled.']] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the details of the feature that is not enabled.
        - `api_name` (string) [maxLen=25] — Represents the API name of the global picklist.
        - `json_path` (string) [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
      - `status` (string) **REQ** [enum=['error']] — Represents the response status.
      - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the details of the feature that is not supported.
        - `api_name` (string) [maxLen=25] — Represents the API name of the global picklist.
        - `json_path` (string) [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
      - `status` (string) **REQ** [enum=['error']] — Represents the response status.
      - `code` (string) **REQ** [enum=['FEATURE_NOT_SUPPORTED']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the details of the feature that is not supported.
        - `api_name` (string) [maxLen=25] — Represents the API name of the global picklist.
        - `json_path` (string) [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
      - `status` (string) **REQ** [enum=['error']] — Represents the response status.
      - `code` (string) **REQ** [enum=['MISSING_BRACES']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000, enum=['Some of brace is missing in given expression']] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the details of the missing braces error.
        - `api_name` (string) **REQ** [maxLen=26, enum=['expression']] — Represents the API name of the field with missing braces.
        - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path of the field with missing braces.
      - `status` (string) **REQ** [enum=['error']] — Represents the response status.
      - `code` (string) **REQ** [enum=['INCORRECT_NUMBER_OF_PARAM']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000, enum=['The number of param is incorrect for one of the method']] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the details of the incorrect number of parameters error.
        - `api_name` (string) **REQ** [maxLen=26] — Represents the API name of the field with incorrect number of parameters.
        - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path of the field with incorrect number of parameters.
      - `status` (string) **REQ** [enum=['error']] — Represents the response status.
      - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ**
        oneOf:
            - `dependee` (object) **REQ** — Represents the dependice Details .
              - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
              - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field with the error.
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `dependee` (object) **REQ** — Represents the dependice Details .
              - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
              - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `range` (object) **REQ** — Represents the allowed numeric range.
              - `from` (integer/int32) **REQ** — Represents the minimum allowed value.
              - `to` (integer/int32) **REQ** — Represents the maximum allowed value.
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `supported_values` (array of object) [minItems=1, maxItems=25] **REQ** — Represents the list of supported values accepted for the JSON key identified by **api_name** and **json_path**.
              oneOf:
                  type: string [maxLen=255] — Represents the values can be present.
                  type: integer/int32 — Represents the values can be present.
            - `dependee` (object) **REQ** — Represents the dependice Details .
              - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
              - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `supported_values` (array of string) [minItems=1, maxItems=25] **REQ** — Represents the list of supported values that can be provided for the field.
              items: [maxLen=255]
            - `dependee` (object) **REQ** — Represents the dependice Details .
              - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
              - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
            - `maximum_length` (integer/int32) **REQ** — Represents the maximum length allowed.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED', 'FIELD_LIMIT_EXCEEDED']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ**
        oneOf:
            - `limit` (integer/int32) — Represents the maximum allowed limit.
            - `limit_due_to` (array of object) [minItems=1, maxItems=25] — Represents the fields due to which the limit is exceeded.
              - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the field.
              - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path of the field.
            - `limit` (integer/int32) — Represents the maximum allowed limit.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the missing dependent field details.
        - `dependee` (object) — Represents the field due to which dependent fields are expected.
          - `api_name` (string) [maxLen=30] — Represents the API name of the global picklist.
          - `json_path` (string) [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
        - `api_name` (string) [maxLen=25] — Represents the API name of the global picklist.
        - `json_path` (string) [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the details of the expected fields that are missing.
        - `expected_fields` (array of object) [minItems=1, maxItems=25] — Represents the list of expected fields that are missing.
          - `api_name` (string) [maxLen=25] — Represents the API name of the expected field.
          - `json_path` (string) [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path of the expected field.
        - `api_name` (string) [maxLen=25] — Represents the API name of the expected field.
        - `json_path` (string) [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path of the expected field.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the details about the fields causing ambiguity.
        - `ambiguity_due_to` (array of object) [minItems=1, maxItems=25] — Represents the list of fields causing ambiguity.
          - `api_name` (string) [maxLen=25] — Represents the API name of the ambiguous field.
          - `json_path` (string) [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path of the ambiguous field.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) **REQ** [enum=['EXPECTED_DEPENDENT_FIELD_MISSING']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the details of missing dependent fields.
        - `expected_fields` (array of object) [minItems=1, maxItems=25] — Represents the list of expected dependent fields that are missing.
          - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the expected dependent field.
          - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path of the expected dependent field.
        - `dependee` (object) — Represents the field due to which the dependent fields are expected.
          - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the dependee field.
          - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path of the dependee field.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000, enum=[6 values]] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the duplicate data details.
        - `api_name` (string) [maxLen=25] — Represents the API name of the field with duplicate data.
        - `json_path` (string) [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path of the field with duplicate data.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the details of the mandatory field that is missing.
        - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the mandatory field.
        - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path of the mandatory field.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) **REQ** [enum=['RESERVED_KEYWORD_NOT_ALLOWED']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the details of the field containing a reserved keyword.
        - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the field with reserved keyword.
        - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path of the field with reserved keyword.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ**
        oneOf:
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the field or operation.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path of the field or operation.
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the field or operation.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path of the field or operation.
            - `limit` (integer/int32) **REQ** — Represents the limit of the field or operation.
            - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the field or operation.
            - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path of the field or operation.
            - `limit` (integer/int32) **REQ** — Represents the limit of the field or operation.
            - `id` (string) **REQ** [maxLen=25] — Represents the ID of the field or operation.
            - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path.
      - `status` (string) **REQ** [enum=['error']] — Represents the response status.
      - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the details of the missing required parameter.
        - `param_name` (string) [maxLen=50] — Represents the name of the missing request parameter.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) **REQ** [enum=['PROPERTY_LOCKED']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the error Response for invalid data.
        - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
        - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the error Response for invalid data.
        - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the global picklist.
        - `json_path` (string) **REQ** [maxLen=500, pattern=^\$(\.[a-zA-Z_][a-zA-Z0-9_]*|\[[0-9]+\])+$] — Represents the JSON path to the field with the error.
        - `other_details` (object) **REQ** — Represents the response object containing an array of errors.
          - `savedCVFilters` (array of object) [maxItems=100] — Represents an array of field metadata objects.
            - `cvid` (string/int64) **REQ** — Represents the id of the CustomView.
            - `cvmodule` (string) **REQ** [maxLen=50] — Represents the module Name.
            - `cvname` (string) **REQ** [maxLen=100] — Represents the customView Name.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) [const=NO_PERMISSION] — Represents the error code for this error type.
      - `message` (string) [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) — Represents the details of the permissions required to perform the operation.
        - `permissions` (array of string) [minItems=1, maxItems=25] **REQ** — Represents the list of permissions required to perform the operation.
          items: [maxLen=100]
      - `status` (string) [const=error] — Represents the response status.
      - `code` (string) **REQ** [enum=[5 values]] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the additional error details.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the response status.
      - `code` (string) [enum=['INCORRECT_DATA_TYPE_PARAM']] — Represents the error code for this error type.
      - `message` (string) [maxLen=255] — Represents the error message describing the issue.
      - `details` (object) — Represents the details of the validation errors.
        - `api_name` (string) [maxLen=25] — Represents the API name of the field with incorrect data type.
        - `json_path` (string) [maxLen=500] — Represents the JSON path of the field with incorrect data type.
      - `status` (string) [const=error] — Represents the response status.
      - `code` (string) **REQ** [enum=['PARTICIPATING_FIELD_NOT_FOUND']] — Represents the error code for this error type.
      - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the issue.
      - `details` (object) **REQ** — Represents the details of the validation errors.
        - `api_name` (string) **REQ** [maxLen=25] — Represents the API name of the field with incorrect data type.
        - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field with incorrect data type.
        - `id` (string) **REQ** [maxLen=25] — Represents the ID of the field with incorrect data type.
      - `status` (string) **REQ** [const=error] — Represents the response status.

**Request Body** (required) — application/json `FieldUpdateRequestBodySchema`
  > Request body for updating custom fields. Maximum of 25 fields can be updated in a single call.
  - `fields` (array of object) [minItems=1, maxItems=25] — Specify the list of fields to update.
    - `field_label` (string) [maxLen=255] — Specify the unique display label of the field.
    - `id` (string/int64) — Id of the resource.
    - `length` (integer/int32) [min=1, max=50000] — Maximum number of characters allowed. Varies by data type.
    - `profiles` (array of object) [maxItems=10] — Specify the profiles to which the field is to be assigned.
      - `id` (string/int64) **REQ** — Id of the resource.
      - `permission_type` (string) **REQ** [enum=['read_write', 'read_only', 'hidden']] — Specify the permission level for this profile.
    - `unique` (object)
      oneOf:
          - `case_sensitive` (boolean) **REQ** — Indicates whether uniqueness is case sensitive.
          - `_disable` (object)
            oneOf:
                type: boolean — marking the field is not a unique key.
                type: null — Null if no information is available.
          type: boolean — Indicates whether the field value must be unique across records.
    - `lookup` (object) — Specify the lookup field configuration.
      - `query_details` (object) — Specify the filter criteria for lookup records.
        - `criteria` (object) — Specify the filter criteria for lookup fields.
          - `group_operator` (string) [enum=['AND', 'OR']] — Specify the logical operator for multiple conditions.
          - `group` (array of object) [maxItems=10] **REQ** — Specify the array of filter conditions.
            - `field` (object) **REQ** — Specify the field details.
              - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
              - `id` (string/int64) — Id of the resource.
            - `comparator` (string) **REQ** [enum=[20 values]] — Specify the comparison operator.
            - `value` (object) **REQ** — Specify the value to compare against.
              oneOf:
                  type: string [maxLen=125] — the value to be matched.
                  type: array of string [maxItems=10]
                    type: string [maxLen=125] — the value to be matched.
                    items: [maxLen=125]
    - `pick_list_values` (array of object) [maxItems=10] — Specify the picklist configuration.
      - `display_value` (string) [maxLen=25] — Specify the display Value to be shown.
      - `actual_value` (string) [maxLen=25] — Specify the actual value of the picklist option. Once set, this value cannot be changed.
      - `reference_value` (string) [maxLen=25] — Specify the reference value to be Userd Internal.
      - `colour_code` (string) [maxLen=25] — Specify the hex code for the picklist value color.
      - `id` (string/int64) — Id of the resource.
      - `_global_picklist_value` (object) — Specify the global picklist value.
        - `id` (string/int64) **REQ** — Id of the resource.
    - `global_picklist` (object)
      oneOf:
          - `id` (string/int64) **REQ** — ID of the global picklist to associate with this field.
          - `api_name` (string) [maxLen=25] — API name of the global picklist.
          type: null — Null if no information is available.
    - `sharing_properties` (object) — Specify the update sharing properties for user lookup fields.
      - `share_preference_enabled` (boolean) — Specify the share permission needed.
      - `share_permission` (string) [maxLen=25, enum=['full-access', 'read-write', 'read-only']] — Specify the share permission.
    - `history_tracking_enabled` (boolean) — Specify whether history tracking is enabled for the field.
    - `history_tracking` (object) — Specify the history tracking configuration.
      - `related_list_name` (string) [maxLen=50] — Specify the name of the related list for history tracking.
      - `duration_configuration` (string) [maxLen=25, enum=['days', 'time']] — Specify the duration for which history is tracked.
      - `followed_fields` (array of object) [maxItems=10] — Specify the list of fields to update.
        - `api_name` (string) [maxLen=25] — Specify the API name of the field to be tracked.
        - `id` (string/int64) — Specify the ID of the field to be tracked.
        - `_delete` (null) — Set to null to remove field from tracking.
    - `formula` (object) — Specify the details of the formula field, including the return type and the expression.
      - `expression` (string) **REQ** [maxLen=255] — Specify the formula expression.
      - `return_type` (string) **REQ** [enum=['double', 'currency', 'text', 'date', 'datetime', 'boolean']] — Specify the return type of the formula.
      - `sub_return_type` (string) [maxLen=50, enum=['small', 'medium', 'large']] — Specify the string subtype of the formula return value when the return type is text.
      - `dynamic` (boolean) — Specify whether the formula is Auto Refresh.
      - `stop_compute_conditionally` (boolean) — Specify whether to stop computation conditionally.
      - `stop_compute_expression` (string) [maxLen=255] — Specify the expression that determines when to stop computation.
    - `decimal_place` (number/int32) — The number of decimal places for the formula field. This is valid for double and currency return types. Possible values are from 0 to 9, both inclusive.
    - `currency` (object) — Currency Field Data.
      - `rounding_option` (string) **REQ** [maxLen=25, enum=['normal', 'round_off', 'round_up', 'round_down']] — Specify how to round currency values.
      - `precision` (string) **REQ** [maxLen=25] — Specify the number of decimal places displayed for the currency value in the user interface. This value should be less than decimal_place.
    - `rollup_summary` (object) — Specify the rollup summary field configuration.
      - `return_type` (string) **REQ** [enum=['currency', 'double', 'integer']] — Specify the return type of the rollup summary.
      - `expression` (object) **REQ** — Specify the calculation expression.
        - `function_parameters` (array of object) [maxItems=10] **REQ** — Specify the fields to aggregate.
          - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
        - `criteria` (object) — Specify the filter criteria for lookup fields.
          - `group_operator` (string) [enum=['AND', 'OR']] — Specify the logical operator for multiple conditions.
          - `group` (array of object) [maxItems=10] **REQ** — Specify the array of filter conditions.
            - `field` (object) **REQ** — Specify the field to be added in validation.
              - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
              - `id` (string/int64) — Id of the resource.
            - `comparator` (string) **REQ** [maxLen=25, enum=[20 values]] — Specify the comparison operator.
            - `value` (object) **REQ** — Specify the value to compare against.
              oneOf:
                  type: string [maxLen=125] — the value to be matched.
                  type: array of string [maxItems=10]
                    type: string [maxLen=125] — the value to be matched.
                    items: [maxLen=125]
        - `function` (string) **REQ** [enum=['SUM', 'COUNT', 'AVG', 'MIN', 'MAX']] — Specify the aggregation function.
      - `based_on_module` (object) **REQ** — Specify the source module for rollup.
        - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
      - `related_list` (object) **REQ** — Specify the related list for rollup.
        - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
    - `association_details` (object)
      oneOf:
          - `related_field` (object) **REQ** — Details of the related field.
            - `api_name` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
            - `id` (string/int64) — Id of the resource.
          - `lookup_field` (object) **REQ** — Details of the lookup field.
            - `api_name` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
            - `id` (string/int64) — Id of the resource.
        - `TypeNull` (null) — Represents the null if no information is available.

**Responses:**

- **200**: Returns the update status for the field, including its unique ID and confirmation of the successful update. [application/json]
    > Represents the response body for the single-field update operation, containing an array with one update result.
    - `fields` (array of object `FieldCreationResult`) [maxItems=1] — Represents the list of field update results for the single-field update operation, containing one entry.
      schema: `FieldCreationResult`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code.
      - `details` (object) **REQ** — Represents the details of the created field.
        - `id` (string) **REQ** [maxLen=25] — Represents the ID of the created field.
      - `message` (string) **REQ** [maxLen=225] — Represents the result message.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation.

- **400**: The request to update the custom field is invalid. Resolution: The request payload and module API name must be valid, and the field object must satisfy the schema for its declared **data_type**. [application/json]
    oneOf:
      - `ErrorResponse` — Represents the error response structure.
        - `fields` (array of object `ErrorResponse`) [maxItems=100] **REQ** — Represents the array of per-field error objects when validation fails for one or more properties of the field being updated.

- **500**: An unexpected error occurred on the Zoho CRM server while processing the request. Resolution: Contact Zoho CRM support if the issue persists. — Schema: `InternalServerError` [application/json]
    > Represents the internal server error response, including the error code, message, and additional details.
    schema: `InternalServerError`
    - `code` (string) **REQ** [maxLen=50, const=INTERNAL_ERROR] — Represents the error code indicating the type of server-side failure.
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the server failure.
    - `details` (object) **REQ** — Represents additional details about the internal server error.
    - `status` (string) **REQ** [maxLen=50, const=error] — Represents the status of the response.

**Scopes:** ZohoCRM.settings.fields.UPDATE

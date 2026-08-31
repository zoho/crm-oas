# POST /settings/fields
**Operation:** `createFields` — Create custom fields in a module
> To create custom fields in a module in your Zoho CRM organization, where supported modules include Leads, Contacts, Accounts, Campaigns, Cases, Invoices, Deals, Price Books, Products, Purchase Orders, Quotes, Sales Orders, Solutions, Vendors, Calls, Tasks, Events, Users, and Custom modules.

**Parameters:**
- `module` (query, string, required) [maxLen=30] {style=form, explode=True}: Specify the API name of the module for which you want to create custom fields. For example, the module name 'Leads'.

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
`FieldCreationResult`:
  > Represents the result of a single field creation.
  - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code.
  - `details` (object) **REQ** — Represents the details of the created field.
    - `id` (string) **REQ** [maxLen=25] — Represents the ID of the created field.
  - `message` (string) **REQ** [maxLen=225] — Represents the result message.
  - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation.

**Request Body** (required) — application/json `FieldRequestBodySchema`
  > Specify the request body for creating custom fields. Maximum of 25 fields can be created in a single call.
  - `fields` (array of object) [minItems=1, maxItems=25] — Specify the list of fields to create.

**Responses:**

- **201**: Returns a list of results confirming that all requested custom fields were created successfully. — Schema: `CreateFieldsResponse` [application/json]
    > Represents the response body returned when one or more custom fields are created.
    schema: `CreateFieldsResponse`
    - `fields` (array of object `FieldCreationResult`) [maxItems=5] **REQ** — Represents the list of creation results, one per field submitted in the request.

- **207**: Returns a mixed-status result in which at least one field creation succeeds and at least one field encounters an error, with each entry in the fields array carrying its own status. [application/json]
    > Represents a multi-status response in which each entry in the fields array independently reflects either a successful field creation or a field-level error.
    - `fields` (array of object) [minItems=2, maxItems=25] **REQ** — Represents the list of field creation results returned for the request. Each entry is either a success object or an error object, reflecting whether the corresponding field creation succeeded or failed.
      oneOf:
        - `FieldCreationResult` — Represents the result of a single field creation.
        - `ErrorResponse` — Represents the error response structure.

- **400**: Invalid data was submitted for one or more fields in the request.
**Resolution:** The caller should verify that all required keys such as field_label and data_type are present and that field type values are valid before resubmitting the request. [application/json]
    oneOf:
      - `ErrorResponse` — Represents the error response structure.
        - `fields` (array of object `ErrorResponse`) [maxItems=25] **REQ** — Represents the list of error details for each field that could not be created. Each entry describes the specific error encountered during field creation.


- **500**: An unexpected server-side error occurred while processing the request.
**Resolution:** The caller should wait briefly and retry the request; if the error persists, report the issue to Zoho CRM support. — Schema: `InternalServerError` [application/json]
    > Represents the internal server error response, including the error code, message, and additional details.
    schema: `InternalServerError`
    - `code` (string) **REQ** [maxLen=50, const=INTERNAL_ERROR] — Represents the error code indicating the type of server-side failure.
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the server failure.
    - `details` (object) **REQ** — Represents additional details about the internal server error.
    - `status` (string) **REQ** [maxLen=50, const=error] — Represents the status of the response.

**Scopes:** ZohoCRM.settings.fields.CREATE

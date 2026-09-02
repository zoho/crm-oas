# GET /settings/global_picklists
**Operation:** `getBulkGlobalPicklists` — Get All Global Picklists
> Fetches the list of global picklists available in the organization along with their details. pick_list_values, used_in_modules, and associated_fields_count can be included in the response based on the "include" query parameter. The response can be filtered in three ways: use the "fields" query parameter to filter by key, so that only the requested keys along with "id" are returned; use the "filters" query parameter to filter the global picklists themselves by the value of a key; and use the "inner_details_filters" query parameter to filter the inner details of the global picklists. A 204 is returned when no global picklists exist.

**Parameters:**
- `include` (query, array, optional) [maxItems=3] {style=form, explode=False}: Comma-separated list of related resources to include. Allowed values: "used_in_modules", "pick_list_values", "associated_fields_count". Use CSV encoding (style=form, explode=false) for multiple values, e.g. include=used_in_modules,pick_list_values.
- `include_inner_details` (query, string, optional) [enum=['used_in_modules.plural_label']]: Optional detailed expansion keys. Currently only allowed when `used_in_modules` is present in `include`. Allowed value: used_in_modules.plural_label.
- `fields` (query, array, optional) [minItems=1, maxItems=20] {style=form, explode=False}: Comma-separated list of the api_names of the global picklist keys to be returned in the response, which lets you filter the response by key. Only the requested keys along with `id` are returned. Keys need not be unique — a key repeated in the list is processed once and the duplicates are ignored. Use CSV encoding (style=form, explode=false) for multiple values, e.g. fields=display_label,api_name,customizable.
- `inner_details_filters` (query, object, optional): JSON array used to filter the inner details returned for each global picklist in the list response. Each entry gives the inner resource in "api_name" and the criteria to apply in "filters", both of which are mandatory. Only "pick_list_values" is supported in "api_name", and within it only the "type" key can be filtered on, using the "equal" and "not_equal" comparators with the value "used" or "unused". "filters" takes either a single criteria using "field", "comparator" and "value", or a set of criteria in "group" combined using "group_operator", and a group may be nested inside another group. Use the "filters" query parameter instead to filter the global picklists themselves.
- `filters` (query, object, optional): JSON object used to filter the global picklists by the value of a key. Give either a single criteria using "field", "comparator" and "value", or a set of criteria in "group" combined using "group_operator". "group" and "group_operator" are mandatory to each other, and within a criteria "comparator" and "value" are dependent on "field". Only the "api_name", "source" and "customizable" keys can be filtered on; any other key returns a 400 with the code NOT_SUPPORTED. The string keys "api_name" and "source" support the "equal" and "not_equal" comparators with a string value, and the boolean key "customizable" supports only the "equal" comparator with a boolean value. Criteria cannot be nested inside another "group".

**Responses:**

- **200**: Fetches the list of global picklists available in the organization along with their details. pick_list_values, used_in_modules, and associated_fields_count can be included in the response based on the "include" query parameter. When the "fields" query parameter is given, only the requested keys along with "id" are returned. When the "filters" query parameter is given, only the global picklists matching the criteria are returned. A 204 is returned when no global picklists exist. [application/json]
    > Response object containing an array of global picklists.
    - `global_picklists` (array of object) [maxItems=100] **REQ** — Array of global picklists with their properties.
      - `display_label` (string) [maxLen=50] — Display label of the global picklist.
      - `source` (string) [maxLen=50, enum=['crm', 'platform_plugin', 'marketplace_plugin']] — Source of the global picklist.
      - `api_name` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
      - `created_time` (string/date-time) [nullable] — Creation timestamp of the global picklist.
      - `modified_time` (string/date-time) [nullable] — Last modification timestamp of the global picklist.
      - `id` (string/int64) **REQ** — Id of the resource.
      - `actual_label` (string) [maxLen=50] — Actual label of the global picklist.
      - `description` (string) [maxLen=1000, nullable] — Description of the global picklist.
      - `associated_fields_count` (integer/int32) — Number of fields associated with this global picklist.
      - `modified_by` (object) — User who last modified the global picklist.
        oneOf:
            - `name` (string) [maxLen=255] — Name of the user.
            - `id` (string/int64) — Id of the resource.
            type: null — Null if no user information is available.
      - `used_in_modules` (array of object) [maxItems=100, nullable] — Array of modules using this global picklist.
        - `plural_label` (string) [maxLen=25] — Plural label of the module.
        - `api_name` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
        - `id` (string/int64) — Id of the resource.
      - `created_by` (object) — User who created the global picklist.
        oneOf:
            - `name` (string) [maxLen=255] — Name of the user.
            - `id` (string/int64) — Id of the resource.
            type: null — Null if no user information is available.
      - `presence` (boolean) — Indicates if the global picklist is present. false if global picklist is in delete scheduler.
      - `customizable` (boolean) — Indicates if the global picklist is customizable.
      - `pick_list_values_sorted_lexically` (boolean) — Indicates if picklist values are sorted lexically.
      - `pick_list_values` (array of object) [maxItems=5000] — Array of picklist values.
        - `type` (string) **REQ** [enum=['unused', 'used']] — Type of the picklist value (used or unused).
        - `id` (string/int64) **REQ** — Id of the resource.
        - `sequence_number` (integer/int32) **REQ** — Sequence number of the picklist value.
        - `display_value` (string) **REQ** [maxLen=120] — The picklist display value(translated value if translation enabled).
        - `reference_value` (string) **REQ** [maxLen=120] — Reference value of the picklist field.
        - `actual_value` (string) [maxLen=120] — Actual value of the picklist field.

- **204**: No global picklists available. (No content)

- **400**: Bad Request - The request cannot be processed due to invalid syntax, or the "filters" or "inner_details_filters" query parameter is malformed, holds an unsupported key, comparator or value, or a mandatory/dependent key inside it is missing. [application/json]
    oneOf:
      - `GlobalPicklistsInvalidFilterParamError` — 400 error returned when the filters or inner_details_filters query parameter contains invalid data while retrieving or filtering global picklists. The param_name detail identifies the query parameter that caused the error. Includes code INVALID_DATA, message 'invalid data', status 'error', and a details object with validation information.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `expected_data_type` (string) **REQ** [maxLen=255] — Expected data type for the parameter
          - `param_name` (string) **REQ** [maxLen=255] — Name of the parameter that caused the error
        - `message` (string) **REQ** [enum=['invalid data']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `GlobalPicklistsMandatoryApiNameMissingError` — 400 error returned when a required api_name field is missing in the request context for global picklists. Includes code MANDATORY_NOT_FOUND, message 'required field not found', status 'error', and details identifying the missing field.
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `api_name` (string) **REQ** [maxLen=255] — API name of the missing field
          - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the missing field
          - `param_name` (string) **REQ** [maxLen=255] — Name of the parameter that contains the missing field
        - `message` (string) **REQ** [enum=['required field not found']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `GlobalPicklistsInvalidApiNameError` — 400 error returned when the provided api_name is invalid for global picklists operations. Includes code INVALID_DATA, message 'invalid data', status 'error', and details describing the validation failure.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `api_name` (string) **REQ** [maxLen=255, enum=['api_name']] — API name of the invalid field
          - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the invalid field
          - `param_name` (string) **REQ** [maxLen=255] — Name of the parameter that contains the invalid field
        - `message` (string) **REQ** [enum=['invalid data']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `GlobalPicklistsInvalidFiltersError` — 400 error returned when the filters object contains invalid data while querying global picklists. Includes code INVALID_DATA, message 'invalid data', status 'error', and a details object outlining validation issues.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `expected_data_type` (string) **REQ** [maxLen=255] — Expected data type for the field
          - `api_name` (string) **REQ** [maxLen=255] — API name of the field with invalid data
          - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the field with invalid data
          - `param_name` (string) **REQ** [maxLen=255] — Name of the parameter that contains the invalid field
        - `message` (string) **REQ** [enum=['invalid data']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `GlobalPicklistsUnsupportedComparatorError` — 400 error returned when a provided comparator is not supported in a global picklists filter. Includes code INVALID_DATA, message 'The value given is not supported', status 'error', and details about the invalid comparator.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `api_name` (string) **REQ** [maxLen=255] — API name of the field with unsupported comparator
          - `json_path` (string) **REQ** [maxLen=1000] — Invalid JSON path
          - `supported_values` (array of string) [maxItems=25] **REQ** — List of supported comparator values
            items: [maxLen=255]
          - `param_name` (string) **REQ** [maxLen=255] — Name of the parameter that contains the unsupported comparator
        - `message` (string) **REQ** [enum=['The value given is not supported']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `GlobalPicklistsDependentTypeMismatchError` — 400 error returned when a filter value does not match the expected data type or dependency for global picklists. Includes code DEPENDENT_MISMATCH, message 'dependent mismatch', status 'error', and details describing the mismatch.
        - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `dependee` (object) **REQ** — Field that the dependent field depends on
            - `api_name` (string) **REQ** [maxLen=255] — API name of the dependee field
            - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the dependee field
          - `expected_data_type` (string) **REQ** [maxLen=255] — Expected data type for the dependent field
          - `api_name` (string) **REQ** [maxLen=255] — API name of the dependent field
          - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the dependent field
          - `param_name` (string) **REQ** [maxLen=255] — Name of the parameter that contains the dependent field
        - `message` (string) **REQ** [enum=['dependent mismatch']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `GlobalPicklistsMissingComparatorForFieldError` — 400 error returned when a filter specifies a field but omits the required comparator for global picklists. Includes code DEPENDENT_FIELD_MISSING, message 'Dependent Field missing', status 'error', and details indicating the missing comparator.
        - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `dependee` (object) **REQ** — Detail field: dependee
            - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
            - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
          - `api_name` (string) **REQ** [maxLen=255] — API name of the missing dependent field
          - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the missing dependent field
          - `param_name` (string) **REQ** [maxLen=255] — Name of the parameter that contains the missing field
        - `message` (string) **REQ** [enum=['Dependent Field missing']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `GlobalPicklistsNotSupportedFieldError` — 400 error returned when a field api_name value is not supported in the global picklists filters or inner_details_filters query parameter. The param_name detail identifies the query parameter that caused the error. Includes code NOT_SUPPORTED, message 'The value given is not supported', status 'error', and details identifying the unsupported field. The json_path varies based on the parameter and its filter nesting depth (e.g. $.filters.field.api_name, $.filters.group[n].field.api_name, $.inner_details_filters[0].filters.field.api_name, $.inner_details_filters[0].filters.group[n].field.api_name, $.inner_details_filters[0].filters.group[n].group[m].field.api_name, etc.).
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `api_name` (string) **REQ** [maxLen=255] — API name contains unsupported field
          - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the unsupported field. Varies based on filter nesting depth — can point to filters.field.api_name or any nested group level such as filters.group[n].field.api_name or filters.group[n].group[m].field.api_name.
          - `param_name` (string) **REQ** [maxLen=255] — Name of the parameter that contains the unsupported field
        - `message` (string) **REQ** [enum=['The value given is not supported']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `GlobalPicklistsInvalidGroupOperatorError` — 400 error returned when the group_operator value in the filters or inner_details_filters query parameter is invalid. The param_name detail identifies the query parameter that caused the error. Includes code INVALID_DATA, message 'invalid data', status 'error', and details with the supported values (and, or).
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `api_name` (string) **REQ** [maxLen=255, enum=['group_operator']] — Detail field: api_name. Always group_operator for this error.
          - `json_path` (string) **REQ** [maxLen=1000] — JSON path to the invalid field
          - `supported_values` (array of string) [maxItems=25] **REQ** — List of supported values for the group_operator field.
            items: [maxLen=255]
          - `param_name` (string) **REQ** [maxLen=255] — Name of the parameter that contains the invalid field
        - `message` (string) **REQ** [enum=['invalid data']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status

- **403**: Forbidden [application/json]
    > Error response object containing code, message, details, and status.
    - `code` (string) **REQ** [maxLen=50] — Error code indicating the type of error.
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `details` (object) **REQ** — Additional details about the error.
      - `permissions` (array of string) [maxItems=1] — List of permissions required to access the resource.
        items: [enum=['Crm_Implied_Customize_Zoho_CRM']]
    - `status` (string) **REQ** [maxLen=100, enum=['error']] — Status of the error response.

- **500**: Internal Server Error [application/json]
    > Internal server error response object containing code, message, details, and status.
    - `code` (string) **REQ** [maxLen=50] — Error code indicating the type of error.
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `details` (object) **REQ** — Additional details about the error.
    - `status` (string) **REQ** [enum=['error']] — Status of the error response.

**Scopes:** ZohoCRM.settings.global_picklist.READ

# PUT /settings/automation/assignment_rules/{id}/actions/reorder_entries
**Operation:** `putReorderEntries` — Reorder Assignment Rule entries
> To reorder rule entries for a single Assignment Rule in your Zoho CRM organization.

**Parameters:**
- `id` (path, string, required) [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$]: Specify the request path param ID value for the request. Use the [Assignment Rule API](assignment_rules.yaml#$.paths./settings/automation/assignment_rules.get) to retrieve the Assignment Rule ID.
- `module` (query, string, required) [maxLen=100]: Specify the param query module required schema value for the request. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID and API name.

**Schemas:**
`DetailsWithExpectedDataTypeInfo`:
  > Error details.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
  - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type returned for the Assignment Rule operation. 
`DetailsWithInvalidFieldInfo`:
  > Error details.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
`DetailsWithMaximumLengthInfo`:
  > Error details.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
  - `maximum_length` (integer/int32) **REQ** — Represents the maximum length returned for the Assignment Rule operation. 
`DetailsWithMinimumLengthInfo`:
  > Error details.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
  - `minimum_length` (integer/int32) **REQ** — Represents the minimum length returned for the Assignment Rule operation. 
`DetailsWithResourcePathIndexInfo`:
  > Error details.
  - `resource_path_index` (integer/int32) **REQ** [enum=[3]] — Index of the invalid request path parameter.
Possible values:
**3** - Represents 3. 
`DetailsWithSupportedValuesInfo`:
  > Error details.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
  - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the supported values returned for the Assignment Rule operation. 
    items: [maxLen=255]
`ErrorResponseInvalidData`:
  > Invalid data.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**INVALID_DATA** - Represents invalid data.
  - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
    oneOf:
      - `DetailsWithResourcePathIndexInfo` — Error details.
      - `DetailsWithExpectedDataTypeInfo` — Error details.
      - `DetailsWithMinimumLengthInfo` — Error details.
      - `DetailsWithMaximumLengthInfo` — Error details.
      - `DetailsWithSupportedValuesInfo` — Error details.
      - `DetailsWithInvalidFieldInfo` — Error details.
  - `message` (string) **REQ** [maxLen=255] — Represents the message that describes the result of the Assignment Rule operation.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.

**Request Body** — application/json `RequestBodySchemaForActionReorderEntries`
> The request body must contain an **assignment_rules** array with one object. Specify the rule entry IDs and their sequence numbers.
  > Request body for reordering entries of an Assignment Rule.
  - `assignment_rules` (array of object) [minItems=1, maxItems=1] **REQ** — Array of Assignment Rule objects to be created.
    - `rule_entries` (array of object `RuleEntryReorderRequestObject`) [minItems=1, maxItems=200] **REQ** — Specify the list of rule entries with updated sequence number for reordering.
      schema: `RuleEntryReorderRequestObject`
      - `id` (string) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — ID of the resource.
      - `sequence_number` (integer/int32) **REQ** — Entry order of the rule entry. This property can be updated only using reorder_entries API.

**Responses:**

- **200**: Returns the Assignment Rule response details for the completed operation. — Schema: `SuccessResponse` [application/json]
    > Successful API operation completed.
    schema: `SuccessResponse`
    - `assignment_rules` (array of object `SuccessObject`) [minItems=1, maxItems=1] — Represents the Assignment Rules returned for the Assignment Rule operation.
      schema: `SuccessObject`
      - `code` (string) [enum=['SUCCESS']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**SUCCESS** - Represents success.
      - `details` (object) — Represents additional details about the Assignment Rule operation result.
        - `id` (string) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — ID of the resource.
        - `rule_entries` (array of object) [minItems=1, maxItems=200] — Represents the rule entries returned for the Assignment Rule operation.
          - `id` (string) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — ID of the resource.
      - `message` (string) [maxLen=255] — Represents the message that describes the result of the Assignment Rule operation.
      - `status` (string) [enum=['success']] — Represents the status of the Assignment Rule operation.
Possible values:
**success** - Represents success.

- **400**: The request contains invalid, missing, or unsupported data.
**Resolution:** The request must include valid Assignment Rule data and valid parameter values for this operation. [application/json]
    > Error response for invalid data.
    oneOf:
      - `ErrorResponseRequiredParamMissing` — Required param missing.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**REQUIRED_PARAM_MISSING** - Represents required param missing.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
          - `param_name` (string) [maxLen=255] — Represents the param name returned for the Assignment Rule operation.
        - `message` (string) **REQ** [enum=['One of the expected param is missing']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**One of the expected param is missing** - Represents one of the expected param is missing.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
      - `ErrorResponseFeatureNotSupported` — Feature not supported.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_SUPPORTED']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**FEATURE_NOT_SUPPORTED** - Represents feature not supported.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
        - `message` (string) **REQ** [enum=['Assignment rules not supported for current edition']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**Assignment rules not supported for current edition** - Represents Assignment Rules not supported for current edition.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
      - `ErrorResponseInvalidModule` — Error response when module given is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**INVALID_MODULE** - Represents invalid module.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
          - `param_name` (string) **REQ** [enum=['module']] — Represents the param name returned for the Assignment Rule operation.
Possible values:
**module** - Represents module. 
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**the module name given seems to be invalid** - Represents the module name given seems to be invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
      - `ErrorResponseModuleNotSupported` — Error response for a module that is valid but unsupported in Assignment Rule processes.
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**NOT_SUPPORTED** - Represents not supported.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
          - `param_name` (string) **REQ** [enum=['module']] — Represents the param name returned for the Assignment Rule operation.
Possible values:
**module** - Represents module. 
        - `message` (string) **REQ** [enum=['Module not supported in assignment rules']] — Represents the error message returned when the specified module does not support Assignment Rules.
Possible values:
**Module not supported in assignment rules** - Indicates that Assignment Rules are not supported for the specified module.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
      - `ErrorResponseInvalidData` — Invalid data.
        - `assignment_rules` (array of object) [maxItems=1] **REQ** — Array of error objects. 
          oneOf:
            - `ErrorResponseInvalidData` — Invalid data.
            - `ErrorResponseMandatoryNotFound` — Mandatory not found.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**MANDATORY_NOT_FOUND** - Represents mandatory not found.
              - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
                - `api_name` (string) [maxLen=255] — Represents the API name returned for the Assignment Rule operation.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation.
              - `message` (string) **REQ** [maxLen=255] — Represents the message that describes the result of the Assignment Rule operation.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.

- **403**: Permission denied for the Assignment Rule operation.
**Resolution:** The CRM administrator must grant the required Assignment Rule permission for the specified module, and the OAuth token must include the required scope. — Schema: `Possible403ErrorResponsesInManagingAR` [application/json]
    > Error response for forbidden access.
    oneOf:
      - `ErrorResponseNoPermissionToAccessAPI` — If current user does not have permission to access API.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**NO_PERMISSION** - Represents no permission.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
          - `permissions` (array of string) [minItems=1, maxItems=1] **REQ** — Represents the list of required permissions. 
            items: [enum=['Crm_Implied_Api_Access']]
        - `message` (string) **REQ** [enum=['permission denied']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**permission denied** - Represents permission denied.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
      - `ErrorResponseNoPermissionToManageAR` — If current user does not have permission to manage Assignment Rules of given module.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**NO_PERMISSION** - Represents no permission.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
          - `permissions` (array of string) [minItems=1, maxItems=1] **REQ** — Represents the list of required permissions. 
            items: [maxLen=255]
        - `message` (string) **REQ** [enum=[1 values]] — Represents the error message for insufficient permission to manage Assignment Rules for the specified module.
Possible values:
**User does not have sufficient permission to manage assignment rules of given module** - Indicates that the user lacks the required Assignment Rule management permission for the module.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
      - `ErrorResponseNoPermissionToManageAROfPrivateModule` — If current user is neither the org admin nor the admin of the given private module.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**NO_PERMISSION** - Represents no permission.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
        - `message` (string) **REQ** [enum=['User is neither the org admin nor the admin of the given private module']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**User is neither the org admin nor the admin of the given private module** - Represents user is neither the org admin nor the admin of the given private module.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.

**Scopes:** ZohoCRM.settings.assignment_rules.UPDATE

# POST /settings/automation/functions
**Operation:** `postAutomationFunctions` — Create Automation Function
> To create a custom automation function in your Zoho CRM organization.

**Schemas:**
`AutomationFunctionModuleChangeInputV2`:
  > Module of the function (Required)
  - `api_name` (string) [maxLen=5] — Represents the API name of the module.
  - `id` (string/int64) [maxLen=18] — Represents the unique ID of the module.

**Request Body** — application/json `AutomationFunctionDefinitionsRequestV2`
> Request body
  > Represents a request payload containing an array of automation function definitions.
  - `functions` (array of object `AutomationFunctionDefinitionInputV2`) [maxItems=1] **REQ** — Represents the array of automation function definitions included in the request.
    schema: `AutomationFunctionDefinitionInputV2`
    - `feature_type` (string) [maxLen=22, enum=[13 values]] — The CRM automation feature type with which the function is associated. Possible values: **workflow** - A Workflow Rule automation feature. **approval_process** - An Approval Process automation feature. **blueprint** - A Blueprint automation feature. **blueprint_transition** - A Blueprint transition automation feature. **blueprint_state** - A Blueprint state automation feature. **review_process** - A review process automation feature. **orchestration** - An orchestration automation feature. **assignment_rules** - An Assignment Rule automation feature. **kiosk** - A kiosk automation feature. **pathfinder** - A pathfinder automation feature. **connected_workflows** - A connected workflows automation feature. **commandcenter_service** - A Command Center service automation feature. **cadences** - A Cadences automation feature.
    - `module` (object `AutomationFunctionModuleChangeInputV2`) **REQ** — Module of the function (Required)
    - `related_module` (object `AutomationFunctionModuleChangeInputV2`) — Related module information if applicable
    - `function` (object `AutomationFunctionLinkInputV2`) **REQ** — function details (Required)
      schema: `AutomationFunctionLinkInputV2`
      - `id` (string/int64) **REQ** [maxLen=18] — The unique identifier of the custom function to associate with the automation definition.
    - `name` (string) **REQ** [maxLen=250] — The name of the automation function.
    - `description` (string) [maxLen=5000] — The description of the automation function.
    - `language` (string) **REQ** [maxLen=11, enum=[9 values]] — Represents the programming language of the automation function. Possible values: **deluge** - Deluge scripting language. **python** - Python (legacy). **java** - Java (legacy). **node_js** - Node.js (legacy). **python_3_12** - Python 3.12. **java17** - Java 17. **nodejs_22** - Node.js 22. **nodejs** - Node.js. **golang** - Go programming language.
    - `arguments` (array of object `AutomationFunctionArgument`) [maxItems=50] — Represents the list of arguments configured for the automation function.
      schema: `AutomationFunctionArgument`
      - `name` (string) **REQ** [maxLen=100] — Represents the name of the automation function argument.
      - `type` (string) **REQ** [maxLen=255, enum=['static', 'merge_field']] — The type of the automation function argument. Possible values: 
* **static** - The argument uses a fixed, literal value.
* **merge_field** - The argument uses a dynamic value merged from a CRM field.

      - `value` (string) **REQ** [maxLen=1000] — Represents the value assigned to the automation function argument.

**Responses:**

- **201**: Returns a confirmation that the custom function was created successfully, including the ID of the newly created function. — Schema: `AutomationFunctionCreationResponse` [application/json]
    > Indicates the response returned after submitting automation function definitions, containing per-item results in a **functions** array.
    schema: `AutomationFunctionCreationResponse`
    - `functions` (array of object `AutomationFunctionActionResult`) [maxItems=1] **REQ** — The list of per-item results from the automation function creation operation.
      schema: `AutomationFunctionActionResult`
      - `code` (string) **REQ** [enum=['SUCCESS']] — The status code indicating the outcome of the automation function action. Possible values: **SUCCESS** - The automation function action was processed successfully.
      - `details` (object `AutomationFunctionOperationDetails`) **REQ** — Operation details for a processed automation function, including the resulting resource identifier.
        schema: `AutomationFunctionOperationDetails`
        - `id` (string/int64) **REQ** — The unique identifier of the automation function that was processed.
      - `message` (string) **REQ** [maxLen=255] — The message describing the result of the operation.
      - `status` (string) **REQ** [enum=['success']] — The overall status of the operation. Possible values: **success** - The operation completed successfully.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad Request - The request cannot be processed due to invalid syntax. [application/json]
    > Represents the error response body returned when a function creation request fails validation.
    - `functions` (array of object) [maxItems=25] **REQ** — Represents the list of error objects, each indicating a validation failure for the corresponding function in the request.
      oneOf:
        - `InvalidModuleNameErrorResponse` — Indicates the validation error returned when the specified module API name is not recognized.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of validation failure. Possible values: INVALID_DATA - Indicates that the data provided in the request is invalid.
          - `details` (object) **REQ** — Represents the error details associated with the invalid module name, including the API name and JSON path of the field that caused the error.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that caused the error.
          - `message` (string) **REQ** [enum=['the tabName given seems to be invalid']] — Represents the error message describing the issue with the request.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
        - `InvalidModuleIdErrorResponse` — The error response returned when the specified module identifier is invalid.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code identifying the type of validation error. Possible values: **INVALID_DATA** - Indicates that the submitted data contains an invalid module identifier.
          - `details` (object) **REQ** — An object containing additional validation details about the error, including the **api_name** and **json_path** of the invalid field.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation error.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that caused the error.
          - `message` (string) **REQ** [enum=['the tabId given seems to be invalid']] — Represents the error message describing the issue. Possible values: the tabId given seems to be invalid - Indicates that the module ID (tab ID) provided in the request is not recognized.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the API request. Possible values: error - Indicates that the request resulted in an error.
        - `ModuleAmbiguityErrorResponse` — Error returned when the provided module name and ID cause ambiguity during processing.
          - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — The error code identifying the type of error. Possible values: **AMBIGUITY_DURING_PROCESSING** - Returned when the provided module name and ID cause ambiguity during processing.
          - `details` (object) **REQ** — The error details associated with the ambiguity, including the **ambiguity_due_to** field that identifies the source of the conflict.
            - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Indicates the list of fields that caused the ambiguity during module resolution.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the dependent field involved in the module resolution error.
              - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the dependent field involved in the module resolution error.
          - `message` (string) **REQ** [enum=['The given moduleid seems to be invalid']] — The error message describing the module resolution issue. Possible values: **The given moduleid seems to be invalid** - Indicates that the provided module identifier could not be resolved.
          - `status` (string) **REQ** [enum=['error']] — The status of the response. Possible values: **error** - Indicates the request resulted in an error.
        - `InvalidLanguageErrorResponse` — Validation error returned when the specified programming language is not supported.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of error.
          - `details` (object) **REQ** — Additional error details for the invalid language data, including the API name of the field, its JSON path, and the list of supported values.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that caused the error.
            - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of supported values for the field that caused the error.
              items: [maxLen=255]
          - `message` (string) **REQ** [enum=['The language given is invalid']] — Represents the error message describing the invalid language condition. Possible values: **The language given is invalid** - Indicates that the language value supplied in the request is not recognized.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
        - `InvalidFunctionIdErrorResponse` — Validation error returned when the referenced function identifier is invalid.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of error. Possible values: INVALID_DATA - Indicates that the data provided in the request is invalid.
          - `details` (object) **REQ** — Represents the error details associated with the invalid function ID, containing the API name and JSON path of the field that caused the error.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that caused the error.
          - `message` (string) **REQ** [enum=['Invalid function Id']] — Represents the error message describing the issue. Possible values: **Invalid function Id** - Indicates that the function ID provided in the request is not valid.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
        - `ArgumentTypeValueMismatchErrorResponse` — Represents an error response returned when an argument's declared type does not match its supplied value.
          - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code identifying the type of argument type mismatch error. Possible values: **DEPENDENT_MISMATCH** - Indicates that the declared type of a dependent field does not match its supplied value.
          - `details` (object) **REQ** — Represents the error details for the argument type mismatch, including the dependent field's API name and JSON path.
            - `dependee` (object) **REQ** — Represents the dependent field for which the declared type does not match the supplied value, identified by its API name and JSON path.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the dependent field involved in the argument type mismatch error.
              - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the dependent field involved in the argument type mismatch error.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that caused the error.
          - `message` (string) **REQ** [enum=['Type and value is mismatched']] — Represents the error message describing the type-value mismatch that occurred.
          - `status` (string) **REQ** [enum=['error']] — Represents the status indicating the request resulted in an error.
        - `ArgumentMissingTypeErrorResponse` — Mandatory field error returned when required argument attributes (name and value) are not provided.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code identifying the type of error. Possible values: **MANDATORY_NOT_FOUND** - Indicates a required argument attribute is missing from the request.
          - `details` (object) **REQ** — Additional error details, including the API name and JSON path of the field that caused the validation failure.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that caused the error.
          - `message` (string) **REQ** [enum=['the given parameter is invalid, specify both name and value']] — Represents the error message describing the issue with the request. Possible values: the given parameter is invalid, specify both name and value - Indicates that the request parameter is missing either a name or a value.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: error - Indicates that the request resulted in an error.
        - `MandatoryFieldMissingErrorResponse` — Represents the error response returned when one or more required fields are missing from the request.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code identifying the type of error. Possible values: **MANDATORY_NOT_FOUND** - Indicates that one or more required fields are missing from the request.
          - `details` (object) **REQ** — Represents the error details containing validation information about the missing field, including its API name and JSON path.
            - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
          - `message` (string) **REQ** [enum=[5 values]] — The error message describing which required field is missing. Possible values: 
* **Required field is missing** - A required field is absent from the request. 
* **Please specify name** - The name field is required but was not provided. 
* **please specify tabId and module api name** - The tab ID and module API name are required but were not provided. 
* **please specify language** - The language field is required but was not provided. 
* **please specify function** - The function field is required but was not provided.

          - `status` (string) **REQ** [enum=['error']] — The status of the API response, indicating the request resulted in an error. Possible values: **error** - The request failed due to a missing required field.
        - `InvalidDataTypeErrorResponse` — Represents the error response returned when a request field contains an unsupported data type.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of validation error. Possible values: **INVALID_DATA** - Indicates that the request contains a field with an unsupported data type.
          - `details` (object) **REQ** — Represents the error details containing validation information, including the expected data type, the API name of the affected field, and its JSON path.
            - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type that the field is expected to receive.
            - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
          - `message` (string) **REQ** [enum=[3 values]] — Represents the error message describing the invalid data type issue. Possible values: 
* **Invalid data type** - The value provided does not match the expected data type for the field. 
* **data type not supported** - The data type used in the request is not supported. 
* **the tabId given seems to be invalid** - The tab ID provided in the request is not recognized.

          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: **error** - Indicates the request resulted in an error.
        - `InvalidDataErrorResponse` — Represents the error response returned when input data fails validation, containing the error code, status, message, and details of the failing field.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of invalid data error. Possible values: **INVALID_DATA** - The request contains data that failed validation.
          - `details` (object) **REQ** — Represents the validation details for the field that caused the error, including the field's API name, JSON path, and maximum allowed length.
            - `maximum_length` (integer/int32) — Represents the maximum allowed length for the value of the field that failed validation.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the validation error.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that caused the validation error.
          - `message` (string) **REQ** [enum=['Invalid data', 'the id given seems to be invalid']] — Represents the error message describing the invalid data condition. Possible values: 
* **Invalid data** - Indicates the submitted data is not valid. 
* **the id given seems to be invalid** - Indicates the provided ID does not match a valid record.

          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: **error** - Indicates the request resulted in an error.
        - `ScriptNotAllowedErrorResponse` — Represents the error response returned when the request body contains the **script** key, which is not permitted.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code identifying the type of error.
          - `details` (object) **REQ** — Additional details about the error, including the **api_name** and **json_path** of the field that caused the issue.
            - `api_name` (string) **REQ** [enum=['script']] — Represents the API name of the field that caused the error. Possible values: **script** - The script field that triggered the not-allowed error.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that caused the error.
          - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message describing the nature of the permission denial.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
        - `InvalidValueErrorResponse` — Represents the error response returned when a request value fails validation.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code identifying the type of validation error. Possible values: **INVALID_DATA** - Indicates that the provided value is invalid.
          - `details` (object) **REQ** — Indicates the additional details about the validation error, including the API name and JSON path of the field that caused the error.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that caused the validation error.
          - `message` (string) **REQ** [enum=['the given value seems to be invalid']] — Represents the error message describing the invalid value. Possible values: **the given value seems to be invalid** - The submitted value does not meet the expected format or constraints.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: **error** - Indicates the request resulted in an error.
        - `InvalidFeatureNameErrorResponse` — Represents the error response returned when the supplied feature name is invalid.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of error. Possible values: **INVALID_DATA** - Indicates the request contains an invalid feature name.
          - `details` (object) **REQ** — Represents the validation details for the error, including the API name and JSON path of the invalid field.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that caused the error.
          - `message` (string) **REQ** [enum=['the given feature name is invalid']] — Represents the error message describing the issue.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: **error** - Indicates the request resulted in an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.automation_actions.CREATE

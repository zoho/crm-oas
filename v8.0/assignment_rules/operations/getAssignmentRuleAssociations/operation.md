# GET /settings/automation/assignment_rules/{id}/actions/associations
**Operation:** `getAssignmentRuleAssociations` — Assignment Rule Associations
> To retrieve the CRM features associated with a single Assignment Rule in your Zoho CRM organization.

**Parameters:**
- `id` (path, string, required) [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$]: Specify the request path param ID value for the request. Use the [Assignment Rule API](assignment_rules.yaml#$.paths./settings/automation/assignment_rules.get) to retrieve the Assignment Rule ID.
- `module` (query, string, required) [maxLen=100]: Specify the param query module required schema value for the request. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID and API name.

**Responses:**

- **200**: Returns the Assignment Rule response details for the completed operation. — Schema: `SuccessResponseAssociations` [application/json]
    > Contains the response structure for Assignment Rule association details.
    schema: `SuccessResponseAssociations`
    - `associations` (array of object `AssociationSchema`) [minItems=1, maxItems=200] — Contains the CRM features associated with the Assignment Rule.
      schema: `AssociationSchema`
      - `resources` (array of object `ResourceResponseObject`) [maxItems=1] — Represents the list of features in which Assignment Rule is associated.
        schema: `ResourceResponseObject`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the resource. 
        - `id` (string) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — Id of the resource
        - `_details` (object) [nullable] — _Details Schema.
        - `api_name` (string) [maxLen=255] — Represents the API name of the resource.
        - `zuid` (string/int32) [maxLen=19] — Zuid of the user resource
        additionalProperties: any
      - `type` (string) [maxLen=255] — Represents the type returned for the Assignment Rule operation.

- **204**: Indicates that no Assignment Rule records are available for the request.

- **400**: The request contains invalid, missing, or unsupported data.
**Resolution:** The request must include valid Assignment Rule data and valid parameter values for this operation. [application/json]
    > 400 error cases for associations.
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
      - `ErrorResponseInvalidData` — Invalid data.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**INVALID_DATA** - Represents invalid data.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
          oneOf:
            - `DetailsWithResourcePathIndexInfo` — Error details.
              - `resource_path_index` (integer/int32) **REQ** [enum=[3]] — Index of the invalid request path parameter.
Possible values:
**3** - Represents 3. 
            - `DetailsWithExpectedDataTypeInfo` — Error details.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
              - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
              - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type returned for the Assignment Rule operation. 
            - `DetailsWithMinimumLengthInfo` — Error details.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
              - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
              - `minimum_length` (integer/int32) **REQ** — Represents the minimum length returned for the Assignment Rule operation. 
            - `DetailsWithMaximumLengthInfo` — Error details.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
              - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
              - `maximum_length` (integer/int32) **REQ** — Represents the maximum length returned for the Assignment Rule operation. 
            - `DetailsWithSupportedValuesInfo` — Error details.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
              - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
              - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the supported values returned for the Assignment Rule operation. 
                items: [maxLen=255]
            - `DetailsWithInvalidFieldInfo` — Error details.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name returned for the Assignment Rule operation. 
              - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path returned for the Assignment Rule operation. 
        - `message` (string) **REQ** [maxLen=255] — Represents the message that describes the result of the Assignment Rule operation.
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

- **403**: Permission denied for the Assignment Rule operation.
**Resolution:** The CRM administrator must grant the required Assignment Rule permission for the specified module, and the OAuth token must include the required scope. — Schema: `ErrorResponseNoPermissionToAccessAPI` [application/json]
    > If current user does not have permission to access API.
    schema: `ErrorResponseNoPermissionToAccessAPI`
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

**Scopes:** ZohoCRM.settings.assignment_rules.READ

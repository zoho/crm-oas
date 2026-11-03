# GET /settings/automation/functions
**Operation:** `getAllAutomationFunctions` — Get Automation Functions
> To retrieve all automation functions configured in your Zoho CRM organization.

**Parameters:**
- `module` (query, string, optional) [maxLen=200]: Specify the module API name to filter the automation functions returned in the response.
- `feature_type` (query, string, optional) [maxLen=22, enum=[13 values]]: Specify the automation feature type to filter the returned functions. Possible values: 
* **workflow**  
* **approval_process**  
* **blueprint** 
* **blueprint_transition**  
* **blueprint_state**  
* **review_process** 
* **orchestration**  
* **assignment_rules** 
* **kiosk** 
* **pathfinder** 
* **connected_workflows** 
* **commandcenter_service**
* **cadences** 

- `page` (query, integer/int32, optional) [min=1, default=1]: Specify the page number to retrieve in the paginated list of automation functions.
- `per_page` (query, integer/int32, optional) [min=1, max=200, default=200]: Specify the number of automation functions to return per page in the paginated response.

**Schemas:**
`AutomationFunctionModuleInfo`:
  > Module metadata associated with the automation function, including singular and plural labels, API name, internal name, and identifier.
  - `singular_label` (string) [maxLen=255] — Represents the singular display label of the module.
  - `plural_label` (string) [maxLen=255] — Represents the plural display label of the module.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module associated with the automation function.
  - `moduleName` (string) [maxLen=255] — Represents the internal name of the module.
  - `id` (string/int64) **REQ** — The unique identifier of the module associated with the automation function.

**Responses:**

- **200**: Returns the list of automation functions configured in the Zoho CRM organization. — Schema: `AutomationFunctionListResponse` [application/json]
    > Represents the response for an automation functions list request, including the list of functions and pagination information.
    schema: `AutomationFunctionListResponse`
    - `functions` (array of object `AutomationFunctionDetail`) [maxItems=200] **REQ** — Represents the list of automation functions returned in the response.
      schema: `AutomationFunctionDetail`
      - `created_time` (string) **REQ** [maxLen=255] — The timestamp when the automation function was created.
      - `lock_status` (object `AutomationFunctionLockStatus`) **REQ** — The lock status of an automation function, indicating whether editing is currently restricted.
        schema: `AutomationFunctionLockStatus`
        - `locked` (boolean) **REQ** — Indicates whether the automation function is currently locked from editing. Possible values: 
* **true** - The automation function is locked and cannot be edited. 
* **false** - The automation function is unlocked and available for editing.

      - `editable` (boolean) **REQ** — Indicates whether the automation function can be edited. Possible values: 
* **true** - The automation function can be edited. 
* **false** - The automation function cannot be edited.

      - `module` (object `AutomationFunctionModuleInfo`) **REQ** — Module metadata associated with the automation function, including singular and plural labels, API name, internal name, and identifier.
      - `related_module` (object) — The CRM module associated with the automation function, if applicable.
        oneOf:
            type: null — Indicates no related module is associated with this automation function.
          - `AutomationFunctionModuleInfo` — Module metadata associated with the automation function, including singular and plural labels, API name, internal name, and identifier.
      - `deletable` (boolean) **REQ** — Indicates whether the automation function can be deleted. Possible values: 
* **true** - The automation function can be deleted. 
* **false** - The automation function cannot be deleted."

      - `description` (string) [maxLen=5000, nullable] — A brief description of the automation function's purpose.
      - `language` (string) **REQ** [maxLen=255, enum=[9 values]] — The programming language used in the automation function script. Possible values: 
* **deluge** - Deluge scripting language. 
* **python** - Python language. 
* **java** - Java language. **node_js** - Node.js runtime.
* **python_3_12** - Python 3.12 runtime. 
* **java17** - Java 17 runtime. 
* **nodejs_22** - Node.js 22 runtime. 
* **nodejs** - Node.js runtime. 
* **GOlang** - Go programming language.

      - `source` (string) **REQ** [maxLen=255] — The source or origin from which the automation function was created.
      - `created_by` (object `CreatedByUserReference`) **REQ** — A minimal reference to the user who created the automation function, including the user ID and display name.
        schema: `CreatedByUserReference`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user who created the automation function.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the user who created the automation function.
      - `feature_type` (string) **REQ** [maxLen=22, enum=[13 values]] — The feature type classification of the automation function. Possible values: 
* **workflow**  
* **approval_process**
* **blueprint** 
* **blueprint_transition** 
* **blueprint_state** 
* **review_process**  
* **orchestration** 
* **assignment_rules** 
* **kiosk** 
* **pathfinder** 
* **connected_workflows** 
* **commandcenter_service** 
* **cadences** 

      - `modified_time` (string) **REQ** [maxLen=255] — The timestamp when the automation function was last modified.
      - `associated` (boolean) **REQ** — Indicates whether the automation function is currently associated with a workflow or action. Possible values: 
* **true** - The automation function is associated with a workflow or action. 
* **false** - The automation function is not associated with any workflow or action.

      - `function` (object `AutomationFunctionReference`) **REQ** — Reference to the underlying function by API name and identifier.
        schema: `AutomationFunctionReference`
        - `api_name` (string) [maxLen=255] — Represents the API name of the automation function.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the automation function.
      - `name` (string) **REQ** [maxLen=250] — Represents the display name of the automation function.
      - `modified_by` (object `ModifiedByUserReference`) **REQ** — Represents a reference to the user who last modified a record, including the user's display name and unique ID.
        schema: `ModifiedByUserReference`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user who last modified the record.
        - `id` (string/int64) **REQ** — Represents the unique ID of the user who last modified the record.
      - `arguments` (array of object `AutomationFunctionArgument`) [maxItems=50] — Represents the list of arguments configured for the automation function.
        schema: `AutomationFunctionArgument`
        - `name` (string) **REQ** [maxLen=100] — Represents the name of the automation function argument.
        - `type` (string) **REQ** [maxLen=255, enum=['static', 'merge_field']] — The type of the automation function argument. Possible values: 
* **static** - The argument uses a fixed, literal value.
* **merge_field** - The argument uses a dynamic value merged from a CRM field.

        - `value` (string) **REQ** [maxLen=1000] — Represents the value assigned to the automation function argument.
      - `id` (string/int64) **REQ** — Represents the unique identifier of the automation function.
    - `info` (object `ListPaginationInfo`) **REQ** — Represents the pagination metadata returned with list responses, including the number of records per page, total record count, current page number, and whether additional records are available.
      schema: `ListPaginationInfo`
      - `per_page` (integer/int32) **REQ** — Represents the number of records returned per page in the response.
      - `count` (integer/int32) **REQ** — Represents the total number of records in the current page.
      - `page` (integer/int32) **REQ** — Represents the current page number in the paginated response.
      - `more_records` (boolean) **REQ** — Indicates whether additional records are available beyond the current page. Possible values: **true** - Additional records exist beyond the current page. **false** - No additional records exist beyond the current page.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad Request - The request cannot be processed due to invalid syntax. [application/json]
    > Represents the error response body returned when the request contains invalid input for the automation functions retrieval operation.
    oneOf:
      - `NotAllowedModuleErrorResponse` — Represents the error response returned when the specified module is not supported for automation functions.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code identifying the type of error. Possible values: **NOT_ALLOWED** - The specified module is not supported for this operation.
        - `details` (object) **REQ** — Represents additional details about the error, including the name of the parameter that caused the issue.
          - `param_name` (string) **REQ** [enum=['module']] — Represents the name of the parameter that caused the error. Possible values: **module** - The module parameter is not allowed for this operation.
        - `message` (string) **REQ** [enum=['The given module is not supported']] — Represents the error message describing why the request was rejected. Possible values: **The given module is not supported** - Indicates that the specified module is not permitted for this operation.
        - `status` (string) **REQ** [enum=['error']] — Represents the outcome status of the request. Possible values: **error** - Indicates the request resulted in an error.
      - `InvalidFeatureTypeErrorResponse` — Error response returned when the specified feature type is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of error. Possible values: **INVALID_DATA** - Indicates that the supplied feature type data is invalid.
        - `details` (object) **REQ** — Represents additional details about the error. Contains the **param_name** property that identifies the parameter responsible for the error.
          - `param_name` (string) **REQ** [enum=['feature_type']] — Represents the name of the parameter that caused the error. Possible values: **feature_type** - Indicates that the **feature_type** parameter value is invalid.
        - `message` (string) **REQ** [enum=['the given feature name is invalid']] — Represents the error message describing the issue. Possible values: **the given feature name is invalid** - Indicates that the provided feature type value is not recognized.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request. Possible values: **error** - Indicates that the request resulted in an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.automation_actions.READ

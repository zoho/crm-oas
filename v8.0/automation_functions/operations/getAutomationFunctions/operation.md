# GET /settings/automation/functions/{functionId}
**Operation:** `getAutomationFunctions` — Get Automation Function
> To retrieve the details of a specific automation function in your Zoho CRM organization.

**Parameters:**
- `functionId` (path, string/int64, required) [maxLen=255]: Specify the unique ID of the function for which you want to perform the operation.

**Schemas:**
`AutomationFunctionModuleInfo`:
  > Module metadata associated with the automation function, including singular and plural labels, API name, internal name, and identifier.
  - `singular_label` (string) [maxLen=255] — Represents the singular display label of the module.
  - `plural_label` (string) [maxLen=255] — Represents the plural display label of the module.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module associated with the automation function.
  - `moduleName` (string) [maxLen=255] — Represents the internal name of the module.
  - `id` (string/int64) **REQ** — The unique identifier of the module associated with the automation function.

**Responses:**

- **200**: Returns the details of the requested automation function. — Schema: `AutomationFunctionQueryResponse` [application/json]
    > Represents the response containing automation function records returned for the requested query.
    schema: `AutomationFunctionQueryResponse`
    - `functions` (array of object `AutomationFunctionDetail`) [maxItems=1] **REQ** — The list of automation function detail records matching the query.
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
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: Indicates that the automation function was retrieved successfully and the response contains no body.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.automation_actions.READ

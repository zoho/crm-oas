# GET /settings/automation/tasks/{id}
**Operation:** `getTaskById` — Automation Task
> PURPOSE: Retrieves the full details of a specific automation task definition including field mappings, module association, lock status, and metadata. MANDATORY: id path parameter (string - automation task definition ID, not a Task record ID). Returns 204 if the task does not exist. Use this to inspect the current state before updating via PUT.

**Parameters:**
- `id` (path, string, required) [maxLen=20]: The unique ID of the automation task definition to retrieve (not a Task record ID).
- `include_inner_details` (query, string, optional) [enum=[7 values]]: Include additional nested labels/display metadata in task responses. Pass exactly one value per request (not comma-separated). Use "display_value" to include field_mapping display labels. Use "module.module_name" or "module.singular_label" to include module display names. Omit this parameter if you only need the raw task configuration.

**Schemas:**
`AutomationFieldAttributes`:
  > Target field to populate when the automation executes. api_name is required. If id is also provided, both must refer to the same field; otherwise the API returns AMBIGUITY_DURING_PROCESSING.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the target field in the destination module — for example, Subject, Due_Date, or Owner — used to identify the field receiving the mapped value within automation actions such as workflow tasks, create_record, and convert.
  - `id` (string) **REQ** [maxLen=255] — Represents the numeric identifier of the target CRM field. Used in conjunction with the field's API name, both of which must resolve to the same field for a mapping to be valid.
`ModuleDetails`:
  > Contains module metadata, including labels, API name, IDs, and optional module_name for related module contexts.
  - `singular_label` (string) [maxLen=255] — Singular display label of the module (e.g., Lead, Contact).
  - `moduleName` (string) [maxLen=255] — Module display name (camelCase). Present on parent module objects only.
  - `id` (string) [maxLen=255] — Unique Zoho CRM module ID.
  - `plural_label` (string) [maxLen=255] — Plural display label of the module (e.g., Leads, Contacts).
  - `api_name` (string) **REQ** [maxLen=255] — API name of the module used in API requests (e.g., Leads, Contacts, Deals).
  - `module_name` (string) [maxLen=255] — Module system name (snake_case). Present on related_module objects only.
`TaskInvalidDataSchema`:
  > Returned when the request contains invalid data  - such as an unrecognized field, wrong data type, value exceeding maximum length, unsupported parameter value, or invalid resource ID.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating invalid data.
  - `details` (object) **REQ** — Error details with contextual validation information.
    - `api_name` (string) [maxLen=255] — API name of the field that caused the error.
    - `json_path` (string) [maxLen=1000] — JSON path pointing to the invalid value in the request payload.
    - `expected_data_type` (string) [maxLen=255] — Expected data type for the field value.
    - `supported_values` (array of string) [maxItems=25] — List of accepted values for this field.
      items: [maxLen=255]
    - `maximum_length` (integer/int32) — Maximum allowed length or count for the field value.
    - `param_name` (string) [maxLen=255] — Name of the query parameter that caused the error.
    - `resource_path_index` (integer/int32) — Index of the resource in the request array that caused the error.
  - `message` (string) **REQ** [maxLen=255] — Error message describing the invalid data condition.
  - `status` (string) **REQ** [enum=['error']] — Error status.

**Responses:**

- **200**: Returns the full task configuration including field_mappings, module, lock_status, and metadata. — Schema: `GetTaskByIdSuccessResponse` [application/json]
    > Success response for retrieving a single automation task by ID. Contains the full task configuration including field_mappings, module, lock_status, and metadata.
    schema: `GetTaskByIdSuccessResponse`
    - `tasks` (array of object `TaskDetails`) [maxItems=1] **REQ** — Array containing exactly one task object matching the requested ID.
      schema: `TaskDetails`
      - `created_time` (string) **REQ** [maxLen=255] — Timestamp when the automation task was created.
      - `lock_status` (object `LockStatus`) — Represents the lock status of a resource, indicating whether it is currently locked or not.
        schema: `LockStatus`
        - `locked` (boolean) — Whether this automation task is locked from editing.
      - `editable` (boolean) — Indicates whether this task can be edited by the current user/context.
      - `module` (object `ModuleDetails`) **REQ** — Contains module metadata, including labels, API name, IDs, and optional module_name for related module contexts.
      - `related_module` (object) — Related module metadata when the task is tied to a secondary module; otherwise null. Specify the api_name and id of the related module.
        oneOf:
          - `ModuleDetails` — Contains module metadata, including labels, API name, IDs, and optional module_name for related module contexts.
          - `RelatedModuleNull` (null) — Null when no related module is associated with the task.
      - `deletable` (boolean) — Indicates whether this task can be deleted.
      - `source` (string) [maxLen=255] — Source system that created or owns this task (for example: crm).
      - `created_by` (object `CreatorDetails`) — Provides details about the creator of an entity, including their name and ID.
        schema: `CreatorDetails`
        - `name` (string) [maxLen=255] — Display name of the user who created this resource.
        - `id` (string) [maxLen=255] — Unique Zoho CRM user ID of the creator.
      - `notify` (boolean) — Whether owner notification is enabled for this task.
      - `feature_type` (string) **REQ** [maxLen=255, enum=[15 values]] — Specify the automation feature category that uses this task. Values: "workflow" (workflow rule), "approval_process" (Approval Process), "Blueprint" (Blueprint transition), "kiosks" (kiosk/process flow), "scoring_rule" (Scoring Rule), "case_escalation_rule" (case escalation rule).
      - `field_mappings` (array of object `AutomationFieldMappings`) [maxItems=20] **REQ** — Specify the field mappings configured for the task. When an automation task is created, the fields should be mapped to tasks modules. Use this JSON array to map the fields of Automation Tasks fields to create tasks automatically when an automation is triggered. 
        discriminator: `type`
          static → #/components/schemas/StaticFieldMapping
          merge_field → #/components/schemas/MergeFieldMapping
          execution_time → #/components/schemas/ExecutionTimeFieldMapping
          composite → #/components/schemas/CompositeFieldMapping
        oneOf:
          - `StaticFieldMapping` — Represents a static-type mapping that assigns a literal value directly to the target field at execution time. The value shape varies by field data type: a plain string for text, picklist, phone, email, URL, number, decimal, currency, and percentage fields (numeric values expressed as strings); an array of strings for multiselectpicklist fields; and an object containing ID and name for ownerlookup fields. Date, datetime, and ALARM fields do not support this type — use execution_time instead, as static on those fields produces a DEPENDENT_MISMATCH error. Fields marked unique in the module settings also require merge_field rather than static for create_record actions.
            - `display_value` (string) [maxLen=500] — The server-computed representation of the mapped value, included in GET responses. Omitted from create and update requests.
            - `field` (object `AutomationFieldAttributes`) **REQ** — Target field to populate when the automation executes. api_name is required. If id is also provided, both must refer to the same field; otherwise the API returns AMBIGUITY_DURING_PROCESSING.
            - `type` (string) **REQ** [const=static] — Identifies the mapping strategy for this field assignment. The value must be `static`, which instructs the automation engine to assign a fixed, literal value to the target field at execution time rather than resolving it dynamically.
            - `value` (object) **REQ** — The literal value assigned to the target field at automation execution time. The expected shape is determined by the target field data_type, discoverable via GET /settings/fields?module={module}. For most field types, supply a string (for example, "High", "Not Started", "1234"). For multi-select picklist fields (data_type: multiselectpicklist), supply an array of option strings. For fields that reference an entity such as an owner or layout (data_type: ownerlookup), supply an object with at minimum the entity ID.
              oneOf:
                - `StaticStringValue` (string) [maxLen=1000] — Represents a plain string value used as the static value for text, picklist, phone, email, URL, number, decimal, currency, and percentage fields. Numeric values are expressed as strings rather than numeric literals. Picklist values must exactly match one of the options defined for the field.
                - `StaticArrayValue` — Represents an array of string values used as the static value for multiselectpicklist fields, where each element corresponds to an available picklist option. Valid option labels are retrievable from the GET /settings/fields endpoint filtered by data_type=multiselectpicklist.
                  type: array of string [minItems=1, maxItems=50]
                    type: string [maxLen=255] — A single picklist option string to include in the multi-select field value. Each entry corresponds to one selectable option as defined for the target field in Zoho CRM.
                    items: [maxLen=255]
                - `StaticObjectValue` — Represents an object value used as the static value for ownerlookup and layout fields, containing an ID that identifies the target user or layout and an optional name that the server resolves from the ID when not supplied. Typically used to assign record ownership by providing the user ID.
                  - `id` (string) **REQ** [maxLen=255] — The system identifier of the referenced entity, such as a user or layout record. This value drives entity resolution by the automation engine and must be provided when the target field references an entity.
                  - `name` (string) [maxLen=255] — The display name of the referenced entity, such as a user full name or a layout label. When omitted from a request payload, the server resolves and populates this property from the supplied ID. The property is present in all GET responses.
                  additionalProperties: any
          - `MergeFieldMapping` — Represents a merge_field-type mapping whose value is resolved at execution time by substituting token references with live field data. Supports direct field tokens (${!Module.Field}), traversal tokens (${!Module.Lookup.Field}), and system tokens (${CURRENTTIME}, ${CURRENTUSER}). Applies to text-based fields such as Subject, Description, and custom text fields. Targeting owner or lookup fields with this type produces a DEPENDENT_MISMATCH error; those fields require a static mapping using an object with a numeric identifier and an optional name. Multiple tokens may be chained with surrounding text for multi-line fields, while single-value fields such as email or URL accept exactly one token.
            - `display_value` (string) [maxLen=500] — The server-computed representation of the mapped value, included in GET responses. Omitted from create and update requests.
            - `field` (object `AutomationFieldAttributes`) **REQ** — Target field to populate when the automation executes. api_name is required. If id is also provided, both must refer to the same field; otherwise the API returns AMBIGUITY_DURING_PROCESSING.
            - `type` (string) **REQ** [const=merge_field] — Identifies the mapping strategy for this field assignment. The value must be `merge_field`, which instructs the automation engine to resolve the field value dynamically from a merge field token at execution time rather than from a static literal.
            - `value` (string) **REQ** [maxLen=1000] — A string containing one or more ${!...} merge-field tokens resolved at runtime.
            - `allow_agent_user` (boolean) [default=False] — Controls whether agent users are eligible for record assignment. Possible values:
**true** — agent users are included in the assignment pool alongside standard users.
**false** — agent users are excluded from assignment.
Applies to mapping types role, group, profile, merge_field, and criteria. Does not apply to user or assignment_rule types.
          - `ExecutionTimeFieldMapping` — Represents an execution_time-type field mapping that computes a date, datetime, or ALARM value at runtime by applying a signed offset to a trigger field or the current time. The value carries an ExecutionTimeValue object specifying the period, unit, trigger_field, and optional time or notify_type properties. A plus sign places the result after the trigger; a minus sign places it before. ALARM fields always require minus. Workflow task actions support only days and business_days as period values.
            - `display_value` (string) [maxLen=500] — The server-computed representation of the mapped value, included in GET responses. Omitted from create and update requests.
            - `field` (object `AutomationFieldAttributes`) **REQ** — Target field to populate when the automation executes. api_name is required. If id is also provided, both must refer to the same field; otherwise the API returns AMBIGUITY_DURING_PROCESSING.
            - `type` (string) **REQ** [const=execution_time] — Identifies the mapping variant as an execution-time offset. The value is always "execution_time" for this schema and acts as the polymorphic discriminator across the AutomationFieldMappings union.
            - `value` (object `ExecutionTimeValue`) **REQ** — Execution-time object specifying how to compute the date/datetime offset from a reference field.
              schema: `ExecutionTimeValue`
              - `period` (string) **REQ** [enum=['days', 'business_days', 'hours', 'minutes']] — The calendar or time unit applied to the offset. Possible values:
**days** — counts all calendar days including weekends and holidays; supported by every action type.
**business_days** — excludes weekends and requires the organisation's business-day setting to be enabled; supported by all action types.
**hours** — available only for create_record, add_meeting, and schedule_call.
**minutes** — available only for create_record, add_meeting, and schedule_call.
workflow_tasks accept only **days** or **business_days**.
              - `unit` (string) **REQ** [maxLen=20, pattern=^[0-9]+$] — The number of period units to offset from the trigger date, supplied as a non-negative integer string (for example, "1", "30"). Passing "0" produces a same-day result, such as scheduling a Remind_At on the same day as the due date.
              - `sign` (string) [enum=['plus', 'minus'], default=plus] — The direction of the offset relative to the trigger date. Possible values:
**plus** — places the computed value after the trigger (for example, a due date two days after record creation).
**minus** — places the computed value before the trigger (for example, a reminder one day before the due date).
For datetime fields (data_type=datetime) a value is expected; omitting it returns a DEPENDENT_FIELD_MISSING error. For date-only fields (data_type=date) the value defaults to **plus** when absent. When targeting Remind_At (data_type=ALARM), **minus** is the only applicable direction.
              - `trigger_field` (string) **REQ** [maxLen=255] — The reference date or datetime field from which the offset is measured. Accepts a merge-field token that resolves to a Date or DateTime field on the parent module (for example, "${!Leads.Modified_Time}", "${!Tasks.Due_Date}"), or the reserved constant "${CURRENTTIME}" to use the automation execution timestamp. When computing a Remind_At (ALARM) value, "${!Tasks.Due_Date}" is the typical anchor.
              - `time` (string) [maxLen=20] — The time-of-day component of the computed value, expressed in 24-hour HH:mm format (for example, "13:00", "01:30"). Applies when the target field carries data type datetime or ALARM (as reported by GET /settings/fields). Supplying this property for a date-only field (data_type=date) produces a validation error.
              - `notify_type` (string) [enum=['popup', 'email', 'emailandpopup']] — The notification channel used to deliver the reminder. Applies exclusively when the target field carries data type ALARM (i.e., Remind_At); date and datetime fields do not use this property. Possible values:
**popup** — triggers an in-app notification.
**email** — sends a message to the task owner.
**emailandpopup** — delivers both simultaneously.
          - `CompositeFieldMapping` — Represents a composite-type field mapping used exclusively for the Participants field in the Events module via the add_meeting action. The value carries a structured object that encodes participant data and is not applicable to any other field or automation action type.
            - `display_value` (string) [maxLen=500] — The server-computed representation of the mapped value, included in GET responses. Omitted from create and update requests.
            - `field` (object `AutomationFieldAttributes`) **REQ** — Target field to populate when the automation executes. api_name is required. If id is also provided, both must refer to the same field; otherwise the API returns AMBIGUITY_DURING_PROCESSING.
            - `type` (string) **REQ** [const=composite] — Serves as the polymorphic discriminator that identifies this field mapping as a composite mapping; the value must be set to "composite" to select this schema variant.
            - `value` (object) **REQ** — Holds the structured composite object that encodes participant data for the Events module Participants field; the shape of this object varies according to the participant type configuration defined for the automation rule.
      - `modified_time` (string) **REQ** [maxLen=255] — Timestamp when the task definition was last modified.
      - `associated` (boolean) — Whether this task is associated with workflow/Blueprint/approval configuration.
      - `modified_by` (object `ModifierDetails`) — Provides details about the individual who modified an entity, including their name and ID.
        schema: `ModifierDetails`
        - `name` (string) [maxLen=255] — Display name of the user who last modified this resource.
        - `id` (string) [maxLen=255] — Unique Zoho CRM user ID of the modifier.
      - `name` (string) **REQ** [maxLen=255] — Specify the name of the automation task.
      - `id` (string) **REQ** [maxLen=255] — Unique ID of the automation task.

- **204**: Request processed successfully but no task record matched the provided ID in the current context.

- **400**: Invalid task ID, invalid feature_type query parameter, or invalid module query parameter. [application/json]
    > Error response returned when a request to retrieve a single automation task fails validation, covering invalid task ID, module, or feature_type values supplied alongside the path id.
    oneOf:
      - `TaskInvalidDataSchema` — Returned when the request contains invalid data  - such as an unrecognized field, wrong data type, value exceeding maximum length, unsupported parameter value, or invalid resource ID.
      - `TaskInvalidModuleSchema` — Returned when the specified module API name, ID, or query parameter value does not match any valid CRM module.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code indicating an invalid module.
        - `details` (object) **REQ** — Error details identifying the invalid module reference.
          - `api_name` (string) [maxLen=255] — API name of the field that caused the error.
          - `json_path` (string) [maxLen=1000] — JSON path pointing to the invalid module reference.
          - `param_name` (string) [maxLen=255] — Name of the query parameter with the invalid module value.
        - `message` (string) **REQ** [maxLen=255] — Error message describing the invalid module.
        - `status` (string) **REQ** [enum=['error']] — Error status.
      - `TaskNotAllowedSchema` — Returned when the requested operation is not allowed  - such as deleting a task associated with an Approval Process, Workflow Rule, or Blueprint, or modifying a read-only system-managed task.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code indicating operation not allowed.
        - `details` (object) **REQ** — Error details identifying the resource.
          - `resource_path_index` (integer/int32) — Index of the resource in the request array that caused the error.
        - `message` (string) **REQ** [maxLen=255] — Error message describing why the operation is not allowed.
        - `status` (string) **REQ** [enum=['error']] — Error status.

- **401**: Authentication or scope error while retrieving the automation task. — Schema: `PostTasksAuthenticationErrorResponse` [application/json]
    > Authentication or OAuth scope error response for POST automation tasks.
    oneOf:
      - `OAuthScopeMismatchErrorResponse` — Error response when access token does not include the required OAuth scope.
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Error code
        - `details` (object) **REQ** — Error details
        - `message` (string) **REQ** [maxLen=255] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `AuthenticationFailureErrorResponse` — Error response when authentication token is invalid or missing.
        - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Error code
        - `details` (object) **REQ** — Error details
        - `message` (string) **REQ** [maxLen=255] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status

- **403**: Insufficient permission or feature not available in this CRM edition. — Schema: `TaskNoPermissionSchema` [application/json]
    > Returned when the caller does not have the required permissions to perform this operation or access this feature.
    schema: `TaskNoPermissionSchema`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code indicating insufficient permissions.
    - `details` (object) **REQ** — Permission details required for this operation.
      - `permissions` (array of string) [maxItems=25] — Contains a list of required permissions for this operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Error message describing the permission issue.
    - `status` (string) **REQ** [enum=['error']] — Error status.

- **404**: Task resource not found for the requested path ID. — Schema: `TaskInvalidDataSchema` [application/json]
    > Returned when the request contains invalid data  - such as an unrecognized field, wrong data type, value exceeding maximum length, unsupported parameter value, or invalid resource ID.

- **500**: Internal server error. — Schema: `InternalServerErrorResponse` [application/json]
    > Error response when an unexpected server-side exception occurs.
    schema: `InternalServerErrorResponse`
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Error code
    - `details` (object) **REQ** — Error details
    - `message` (string) **REQ** [maxLen=255] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status

**Scopes:** ZohoCRM.settings.automation_actions.READ

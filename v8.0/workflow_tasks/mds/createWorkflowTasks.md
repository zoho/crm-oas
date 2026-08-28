# POST /settings/automation/tasks
**Operation:** `createWorkflowTasks` — Create an Automation Task 
> PURPOSE: Creates an automation task definition used by workflow rules, approval processes, blueprints, kiosks, scoring rules, and case escalation rules. PREREQUISITES: (1) Call GET /settings/automation/tasks to check existing task definitions and avoid duplicates. (2) Call GET /settings/layouts?module=Tasks to discover supported fields and identify mandatory fields where required: true in the field info. STRUCTURE: The request body contains a tasks array with exactly 1 task object. Each task requires: name (string), module ({api_name, id}), and field_mappings (array). Omitting mandatory fields returns REQUIRED_DATA_NOT_FOUND. Returns the created task ID.

**Schemas:**
`AutomationFieldAttributes`:
  > Target field to populate when the automation executes. api_name is required. If id is also provided, both must refer to the same field; otherwise the API returns AMBIGUITY_DURING_PROCESSING.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the target field in the destination module — for example, Subject, Due_Date, or Owner — used to identify the field receiving the mapped value within automation actions such as workflow tasks, create_record, and convert.
  - `id` (string) **REQ** [maxLen=255] — Represents the numeric identifier of the target CRM field. Used in conjunction with the field's API name, both of which must resolve to the same field for a mapping to be valid.
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
`TaskMandatoryNotFoundSchema`:
  > Returned when a required field or parameter is missing from the request payload.
  - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code indicating a mandatory field is missing.
  - `details` (object) **REQ** — Error details identifying the missing field.
    - `api_name` (string) [maxLen=255] — API name of the missing required field.
    - `json_path` (string) [maxLen=1000] — JSON path pointing to where the missing field is expected.
  - `message` (string) **REQ** [maxLen=255] — Error message describing which mandatory field is missing.
  - `status` (string) **REQ** [enum=['error']] — Error status.

**Request Body** — application/json `TaskCreateOrUpdateRequest`
> Task payload for create or update. tasks must contain exactly one task object. Required keys inside task are name, module, and field_mappings.
  > PURPOSE: Request body wrapper for creating or updating an automation task definition. MUST contain a tasks array with exactly 1 task object.
  - `tasks` (array of object `TaskCreateOrUpdateInput`) [minItems=1, maxItems=1] **REQ** — REQUIRED. Array containing exactly 1 automation task object. Multiple tasks per request are not supported.
    schema: `TaskCreateOrUpdateInput`
    - `name` (string) **REQ** [maxLen=255] — Display name for this task definition. Must be identical to the value provided in the Subject field_mapping entry. If they do not match, the API returns INVALID_DATA. For merge_field type Subject mappings, set name to the same token string (e.g., "${!Leads.Last_Name}").
    - `module` (object `TaskCreateOrUpdateModuleRef`) **REQ** — PURPOSE: The CRM module this task definition belongs to. Specifies which module's records will trigger task creation - not the Tasks module itself. PREREQUISITES: Call GET /settings/modules to discover available module api_names and IDs. api_name is required, id is optional.
      schema: `TaskCreateOrUpdateModuleRef`
      - `api_name` (string) **REQ** [maxLen=255] — REQUIRED. API name of the CRM module whose records trigger this task creation (e.g., Leads, Contacts, Deals). Use GET /settings/modules to discover available modules.
      - `id` (string) [maxLen=255] — Optional module ID. If provided alongside api_name, both must refer to the same module.
    - `notify` (boolean) [default=False] — Whether notification should be sent to the task owner when this automation task executes.
    - `feature_type` (string) [maxLen=255, enum=[15 values], default=workflow] — The automation feature this task definition belongs to. Defaults to "workflow" if omitted. A task can only be associated with the feature it was created for - a task with feature_type="workflow" can only be attached to workflow rules, not to blueprints or kiosks. Supported values are defined in the enum.
    - `field_mappings` (array of object `AutomationFieldMappings`) [minItems=1, maxItems=20] **REQ** — REQUIRED. Field mappings for task fields. Mandatory mappings: Subject (static or merge_field), Due_Date (execution_time), Status (static: Not Started, Deferred, In Progress, Completed, Waiting on someone else), Priority (static: Highest, High, Normal, Low, Lowest). Optional: Description, Owner, Remind_At (execution_time). Each entry requires field ({api_name, id}), type, and value. Types: static (literal values), merge_field (${!Module.Field} tokens), execution_time (for Date/DateTime/ALARM - requires period, unit, trigger_field, sign). Workflow tasks support period: days, business_days only. Max 20 entries.
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

**Responses:**

- **201**: Task definition created successfully. — Schema: `CreateTaskSuccessResponse` [application/json]
    > Successful response after creating an automation task definition.
    schema: `CreateTaskSuccessResponse`
    - `tasks` (array of object `TaskActionResult`) [maxItems=1] **REQ** — Array containing the created task result.
      schema: `TaskActionResult`
      - `code` (string) **REQ** [maxLen=255] — Operation result code (e.g., SUCCESS).
      - `details` (object `TaskActionResultDetails`) **REQ** — Details returned with a task action result, including the created or affected resource ID.
        schema: `TaskActionResultDetails`
        - `resource_path_index` (string) [maxLen=255] — Index of the resource in the request payload array.
        - `id` (string) **REQ** [maxLen=20] — Unique ID of the created or affected automation task.
      - `message` (string) **REQ** [maxLen=255] — Result message describing the outcome of the task action.
      - `status` (string) **REQ** [maxLen=255] — Operation result status (e.g., success).

- **400**: Validation error in request payload. Two response shapes exist: (1) Request-structure errors (e.g., invalid module type/length, missing field api_name) return tasks as a single error object. (2) Per-task validation errors (e.g., field_mapping errors, dependent mismatch, mandatory not found) return tasks as an array with one error object per task entry. Parse tasks as either object or array to handle both shapes. [application/json]
    > Error response returned when an automation task create fails validation, covering request-structure errors, per-task field-mapping errors, dependent-field mismatches, and missing mandatory fields.
    oneOf:
        - `tasks` (array of object) [maxItems=25] **REQ** — Array of error objects
          oneOf:
            - `TaskNotAllowedSchema` — Returned when the requested operation is not allowed  - such as deleting a task associated with an Approval Process, Workflow Rule, or Blueprint, or modifying a read-only system-managed task.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code indicating operation not allowed.
              - `details` (object) **REQ** — Error details identifying the resource.
                - `resource_path_index` (integer/int32) — Index of the resource in the request array that caused the error.
              - `message` (string) **REQ** [maxLen=255] — Error message describing why the operation is not allowed.
              - `status` (string) **REQ** [enum=['error']] — Error status.
            - `AutomationFieldMappingExpectedFieldMissingError` — Represents a validation error returned by the API when a field_mapping entry omits the field object entirely or provides a field object that contains neither api_name nor ID, leaving the target field unresolvable.
              - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Identifies the error code for the condition in which one or more expected field identifiers are absent from the request payload.
              - `details` (object) **REQ** — Contains the structured breakdown of expected field identifiers that were absent from the request payload, enabling precise identification of which fields were anticipated but not received.
                - `expected_fields` (array of object) [maxItems=25] — A collection of field identifier objects, each representing an anticipated field — referenced by its api_name, ID, or both — that was not present in the submitted request.
                  - `api_name` (string) [maxLen=255] — Specifies the name of the field identifier that was expected, such as api_name or ID, indicating which identifier type was looked up during field resolution.
                  - `json_path` (string) [maxLen=1000] — Provides the JSON path that pinpoints the exact location within the request payload where the missing identifier was expected to reside.
              - `message` (string) **REQ** [maxLen=255] — Provides a descriptive explanation of the expected-field-missing error, summarising why the operation could not be completed due to absent field identifiers.
              - `status` (string) **REQ** [enum=['error']] — Indicates the top-level outcome classification of the error response when expected field identifiers are absent from the request payload.
            - `AmbiguityDuringProcessingError` — Returned when the request contains ambiguous field or module references that cannot be resolved (e.g., invalid module ID, unrecognized field API name).
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `ambiguity_due_to` (array of object) [maxItems=25] — List of fields causing the ambiguity.
                  - `api_name` (string) [maxLen=255] — API name of the expected field.
                  - `json_path` (string) [maxLen=1000] — JSON path to the expected field location.
              - `message` (string) **REQ** [maxLen=255] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `AutomationFieldMappingDependentFieldMissingError` — Returned when a required sub-property is absent from an execution_time value object. This error occurs when type is set to execution_time but one or more of its dependent properties — such as period or unit — are not included in the submitted value payload.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Identifies the error code for the condition in which a field mapping is rejected because a required dependent field is absent from the automation action payload.
              - `details` (object) **REQ** — Contains structured diagnostic information that identifies the absent dependent field and the field whose value or presence governs the dependency relationship.
                - `dependee` (object) — Represents the field whose presence or selected value establishes a requirement for the missing or mismatched dependent field, providing context for resolving the dependency violation.
                  - `api_name` (string) [maxLen=255] — Indicates the API name of the field that drives the dependency requirement, such as a type selector or a nested field identifier, enabling callers to locate the governing field within the automation mapping.
                  - `json_path` (string) [maxLen=1000] — Indicates the path within the automation action request body that resolves to the dependee field, allowing callers to locate its exact position in the payload structure.
                - `api_name` (string) [maxLen=255] — Indicates the API name of the dependent field that was expected but not found in the automation action payload, such as a unit or period qualifier associated with another field's value.
                - `json_path` (string) [maxLen=1000] — Indicates the path within the automation action request body pointing to the location where the absent dependent field was expected to appear.
              - `message` (string) **REQ** [maxLen=255] — Provides a descriptive explanation of the dependent-field-missing error, describing which field was absent and the context in which it was required.
              - `status` (string) **REQ** [enum=['error']] — Indicates the top-level outcome classification of the error response when a dependent field is absent from the automation field mapping payload.
            - `TaskDependentMismatchSchema` — Returned when a field_mapping value conflicts with a dependent field constraint  - such as a mismatched dependee field or an invalid dependent value.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code indicating a dependent field mismatch.
              - `details` (object) **REQ** — Error details identifying the dependent field conflict.
                - `dependee` (object) — The field that the mismatched field depends on.
                  - `api_name` (string) [maxLen=255] — API name of the dependee field (e.g., type, field.id).
                  - `json_path` (string) [maxLen=1000] — JSON path to the dependee field in the request payload.
                - `api_name` (string) [maxLen=255] — API name of the field that caused the mismatch.
                - `json_path` (string) [maxLen=1000] — JSON path pointing to the mismatched value.
                - `maximum_length` (integer/int32) — Maximum allowed length for the dependent value.
              - `message` (string) **REQ** [maxLen=255] — Error message describing the dependent field mismatch.
              - `status` (string) **REQ** [enum=['error']] — Error status.
            - `TaskInvalidModuleSchema` — Returned when the specified module API name, ID, or query parameter value does not match any valid CRM module.
              - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code indicating an invalid module.
              - `details` (object) **REQ** — Error details identifying the invalid module reference.
                - `api_name` (string) [maxLen=255] — API name of the field that caused the error.
                - `json_path` (string) [maxLen=1000] — JSON path pointing to the invalid module reference.
                - `param_name` (string) [maxLen=255] — Name of the query parameter with the invalid module value.
              - `message` (string) **REQ** [maxLen=255] — Error message describing the invalid module.
              - `status` (string) **REQ** [enum=['error']] — Error status.
            - `TaskInvalidDataSchema` — Returned when the request contains invalid data  - such as an unrecognized field, wrong data type, value exceeding maximum length, unsupported parameter value, or invalid resource ID.
            - `TaskDuplicateDataSchema` — Returned when the request contains duplicate field mappings  - such as specifying the same field more than once in field_mappings.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Error code indicating duplicate data.
              - `details` (object) **REQ** — Error details identifying the duplicated field.
                - `api_name` (string) [maxLen=255] — API name of the duplicated field.
                - `json_path` (string) [maxLen=1000] — JSON path pointing to the duplicate entry in the request payload.
              - `message` (string) **REQ** [maxLen=255] — Error message describing the duplicate data condition.
              - `status` (string) **REQ** [enum=['error']] — Error status.
            - `TaskMandatoryNotFoundSchema` — Returned when a required field or parameter is missing from the request payload.
            - `AutomationFieldMappingRequiredDataNotFoundError` — Represents a validation error returned by the API when a field that the target module requires (such as Subject for Tasks) is absent from the field_mappings array. The details.value property identifies the missing field, and details.sub_json_path indicates the nested property path used to locate it.
              - `code` (string) **REQ** [enum=['REQUIRED_DATA_NOT_FOUND']] — Identifies the error code for the condition in which required data is absent from the field_mappings payload.
              - `details` (object) **REQ** — Supplies contextual information that pinpoints the specific field entry absent from the field_mappings collection, enabling precise identification of the missing data.
                - `sub_json_path` (string) [maxLen=255] — Indicates the nested property path, such as field.api_name, that further narrows the location of the missing field within the field_mappings structure.
                - `api_name` (string) [maxLen=255] — Denotes the property name context, such as api_name, associated with the field entry where required data was not found in field_mappings.
                - `json_path` (string) [maxLen=1000] — Specifies the JSON path pointing to the position within the field_mappings array where the expected entry was not found.
                - `value` (string) [maxLen=255] — Holds the api_name of the field that was expected but not found in field_mappings, such as Subject for Tasks, enabling callers to identify exactly which field requires attention.
              - `message` (string) **REQ** [maxLen=255] — Provides a descriptive explanation of the error returned when required data is not found within the field_mappings payload.
              - `status` (string) **REQ** [enum=['error']] — Indicates the top-level outcome classification of the error response when required data is absent from the field_mappings payload.
        - `tasks` (object) **REQ** — Represents the single error object returned when the create fails due to a request-structure issue such as a missing module api_name or an invalid module data type.
          oneOf:
            - `TaskMandatoryNotFoundSchema` — Returned when a required field or parameter is missing from the request payload.
            - `TaskInvalidDataSchema` — Returned when the request contains invalid data  - such as an unrecognized field, wrong data type, value exceeding maximum length, unsupported parameter value, or invalid resource ID.

- **401**: Authentication or scope error while creating automation tasks. — Schema: `PostTasksAuthenticationErrorResponse` [application/json]
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

- **403**: No permission to create automation tasks. — Schema: `TaskNoPermissionSchema` [application/json]
    > Returned when the caller does not have the required permissions to perform this operation or access this feature.
    schema: `TaskNoPermissionSchema`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code indicating insufficient permissions.
    - `details` (object) **REQ** — Permission details required for this operation.
      - `permissions` (array of string) [maxItems=25] — Contains a list of required permissions for this operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Error message describing the permission issue.
    - `status` (string) **REQ** [enum=['error']] — Error status.

- **404**: Invalid URL pattern. — Schema: `InvalidUrlPatternErrorResponse` [application/json]
    > Error response when the request URL does not match a valid API pattern.
    schema: `InvalidUrlPatternErrorResponse`
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Error code
    - `details` (object) **REQ** — Error details
    - `message` (string) **REQ** [maxLen=255] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status

- **500**: Internal server error. — Schema: `InternalServerErrorResponse` [application/json]
    > Error response when an unexpected server-side exception occurs.
    schema: `InternalServerErrorResponse`
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Error code
    - `details` (object) **REQ** — Error details
    - `message` (string) **REQ** [maxLen=255] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status

**Scopes:** ZohoCRM.settings.automation_actions.CREATE

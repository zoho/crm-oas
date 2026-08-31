# POST /settings/automation/cadences
**Operation:** `postCadences` — Create cadence
> Creates a new cadence (initially in draft status) with its follow-up tree and optional un-enrollment rules in a single call. custom_view cadences require a custom_view.id; manual_enrollment cadences must omit custom_view. Follow-ups reference each other via reference_id (a client-chosen string) so that parent/child links can be expressed in a single request before server ids are assigned. The cadence must be published and activated before it will enroll records.

**Schemas:**
`AllErrorResponse`:
  > Represents the error response returned when the API request fails due to validation errors or unsupported operations.
  - `code` (string) **REQ** [enum=[18 values]] — Represents a machine-readable error code; branch on this value, not on message.
  - `message` (string/error message) **REQ** — Represents the error message describing the validation failure.
  - `status` (string) **REQ** [const=error] — Represents the status of the API response.
  - `details` (object) **REQ** — Represents additional details providing context about the error.
    oneOf:
      - `ExpectedFieldMissingDetails` — Represents error details when expected fields are missing from the request.
      - `ExpectedDependentFieldMissingDetails` — Represents error details when expected dependent fields are missing from the request.
      - `InvalidDataWithId` — Represents error details when a field contains an invalid identifier.
      - `InvalidDataWithSupportedValues` — Represents error details when a field contains an invalid value, listing the supported values.
      - `InvalidDataWithDataType` — Represents error details when a field contains invalid data, specifying the expected data type.
      - `InvalidDataWithDataTypeAndSupportedValues` — Represents error details when a field contains invalid data, specifying the expected data type and supported values.
      - `MandatoryInvalidDataCommonApiNameJsonPath` — Represents error details when a mandatory field contains invalid data.
      - `DependentMismatchDetails` — Represents error details when a dependent field value does not match the expected values based on the parent field.
      - `DependencyFieldMissingDetails` — Represents error details when a required dependency field is missing from the request.
      - `ResourcePathIndex` — Represents error details containing the resource path index where the validation error occurred.
      - `IdDetails` — Represents error details containing the unique identifier of the resource associated with the error.
      - `ParamNameDetails` — Represents error details containing the parameter name associated with the error.
      - `ParamNameWithEnumDetails` — Represents error details containing the parameter name associated with the error.
      - `ApiNameLimit` — Represents error details when a field exceeds its maximum allowed count.
      - `DetailsPermission` — Represents error details when the request fails due to missing permissions.
      - `EmptyDetails` (object) — Represents an empty error details object with no additional information.
      - `ApiNameLimitJsonPath` — Represents error details when a field at a specific JSON path exceeds its maximum allowed count.
      - `AmbiguityDetails` — Represents error details for ambiguity, listing the fields that caused the ambiguity.
      - `ApiNameExistsInJsonPath` — Represents error details when an API name already exists at the specified JSON path.
      - `MaximumLengthApiNameJsonPath` — Represents error details when a field value exceeds the maximum allowed length.
`AmbiguityDetails`:
  > Represents error details for ambiguity, listing the fields that caused the ambiguity.
  - `ambiguity_due_to` (array of object) [maxItems=100] **REQ** — Represents the list of fields that caused the ambiguity during processing.
    - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the ambiguity.
    - `json_path` (string) [maxLen=255] — Represents the JSON path of the field that caused the ambiguity.
`ApiNameExistsInJsonPath`:
  > Represents error details when an API name already exists at the specified JSON path.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that already exists in the specified JSON path.
  - `exists_in` (object) **REQ** — Represents the location where the API name already exists, identified by its API name and JSON path.
    - `api_name` (string) [maxLen=255] — Represents the API name at the existing location.
    - `json_path` (string) [maxLen=500] — Represents the JSON path of the existing field location.
  - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the duplicate field in the request payload.
`ApiNameLimit`:
  > Represents error details when a field exceeds its maximum allowed count.
  - `api_name` (string) [maxLen=255] — Represents the API name of the field that exceeded the limit.
  - `limit` (integer/int32) **REQ** — Represents the maximum allowed count for the field.
`ApiNameLimitJsonPath`:
  > Represents error details when a field at a specific JSON path exceeds its maximum allowed count.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that exceeded the limit.
  - `limit` (integer/int32) **REQ** — Represents the maximum allowed count for the field.
  - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field that exceeded the limit.
`AutomationFieldAttributes`:
  > Target field to populate when the automation executes. api_name is required. If id is also provided, both must refer to the same field; otherwise the API returns AMBIGUITY_DURING_PROCESSING.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the target field in the destination module — for example, Subject, Due_Date, or Owner — used to identify the field receiving the mapped value within automation actions such as workflow tasks, create_record, and convert.
  - `id` (string) **REQ** [maxLen=255] — Represents the numeric identifier of the target CRM field. Used in conjunction with the field's API name, both of which must resolve to the same field for a mapping to be valid.
`DependencyFieldMissingDetails`:
  > Represents error details when a required dependency field is missing from the request.
  - `dependee` (object) **REQ** — Represents the dependee field that is required but missing from the request.
    - `api_name` (string) [maxLen=255] — Represents the API name of the dependee field.
    - `json_path` (string) [maxLen=500] — Represents the JSON path of the dependee field.
    - `param_name` (string) [maxLen=255] — Represents the parameter name of the dependee field.
  - `api_name` (string) [maxLen=255] — Represents the API name of the field with the missing dependency.
  - `json_path` (string) [maxLen=500] — Represents the JSON path of the field with the missing dependency.
  - `param_name` (string) [maxLen=255] — Represents the parameter name associated with the field.
`DependentMismatchDetails`:
  - `dependee` (object) **REQ** — Represents the dependee field associated with the mismatch.
  - `api_name` (string) [maxLen=255] — Represents the API name of the field with the dependency mismatch.
  - `json_path` (string) [maxLen=500] — Represents the JSON path of the field with the dependency mismatch.
  - `expected_data_type` (string) [maxLen=255] — Represents the data type the server expected for the dependent field based on the parent field's value.
  - `supported_values` (array) [maxItems=25] — Represents the list of supported values for the dependee field.
  - `param_name` (string) [maxLen=255] — Represents the parameter name associated with the field.
  oneOf:
      - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of allowed values for the dependent field given the parent field's current value.
        items: [maxLen=500]
      - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type expected for the dependent field given the parent field's current value.
`DetailsPermission`:
  > Represents error details when the request fails due to missing permissions.
  - `permissions` (array of string) [maxItems=25] **REQ** — Represents the list of required permissions that are missing.
    items: [maxLen=255]
`ExpectedDependentFieldMissingDetails`:
  > Represents error details when expected dependent fields are missing from the request.
  - `dependee` (object) **REQ** — Represents the expected dependent field that is missing from the request.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the expected dependent field.
    - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the expected dependent field.
  - `expected_fields` (array of object) [maxItems=25] **REQ** — Represents the list of expected fields that are missing from the request.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing expected field.
    - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the missing expected field.
`ExpectedFieldMissingDetails`:
  > Represents error details when expected fields are missing from the request.
  - `expected_fields` (array of object) [maxItems=25] **REQ** — Represents the list of expected fields that are missing from the request.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing expected field.
    - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the missing expected field.
`IdDetails`:
  > Represents error details containing the unique identifier of the resource associated with the error.
  - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the resource.
`InvalidDataWithDataType`:
  > Represents error details when a field contains invalid data, specifying the expected data type.
  - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type for the field.
  - `api_name` (string) [maxLen=255] — Represents the API name of the field with invalid data.
  - `json_path` (string) [maxLen=500] — Represents the JSON path of the field with invalid data.
  - `param_name` (string) [maxLen=255] — Represents the parameter name of the field with invalid data.
`InvalidDataWithDataTypeAndSupportedValues`:
  > Represents error details when a field contains invalid data, specifying the expected data type and supported values.
  - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type for the field.
  - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of supported values for the field.
    items: [maxLen=500]
  - `api_name` (string) [maxLen=255] — Represents the API name of the field with invalid data.
  - `json_path` (string) [maxLen=500] — Represents the JSON path of the field with invalid data.
  - `param_name` (string) [maxLen=255] — Represents the parameter name of the field with invalid data.
`InvalidDataWithId`:
  > Represents error details when a field contains an invalid identifier.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field with invalid data.
  - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field with invalid data.
  - `id` (string) **REQ** [maxLen=255] — Represents the identifier of the invalid value provided.
`InvalidDataWithSupportedValues`:
  > Represents error details when a field contains an invalid value, listing the supported values.
  - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of supported values for the field.
    items: [maxLen=500]
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field with invalid data.
  - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field with invalid data.
  - `param_name` (string) [maxLen=255] — Represents the parameter name of the field with invalid data.
`MandatoryInvalidDataCommonApiNameJsonPath`:
  > Represents error details when a mandatory field contains invalid data.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the mandatory field with invalid data.
  - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the mandatory field with invalid data.
  - `param_name` (string) [maxLen=255] — Represents the parameter name of the mandatory field with invalid data.
`MaximumLengthApiNameJsonPath`:
  > Represents error details when a field value exceeds the maximum allowed length.
  - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the field.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that exceeded the maximum length.
  - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the field that exceeded the maximum length.
`ParamNameDetails`:
  > Represents error details containing the parameter name associated with the error.
  - `param_name` (string) **REQ** [maxLen=255] — Represents the parameter name associated with the error detail.
`ParamNameWithEnumDetails`:
  > Represents error details containing the parameter name associated with the error.
  - `param_name` (string) **REQ** [maxLen=255, enum=['ids']] — Represents the parameter name associated with the error detail.
Possible values:
ids - The ids query parameter.
`ResourcePathIndex`:
  > Represents error details containing the resource path index where the validation error occurred.
  - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path where the validation error occurred.

**Request Body** — application/json `CadencesCreateRequestBody`
> The request body must contain a Cadences array with the configuration details for the new Cadence, including follow-up steps and action assignments.
  > Represents the request body schema for creating a new Cadence with follow-up steps and action configurations.
  - `cadences` (array of object) [maxItems=1] **REQ** — Represents the list of Cadences to create.
    - `module` (object `ModuleInformation`) **REQ** — Represents the API name and identifier of a CRM module.
      schema: `ModuleInformation`
      - `api_name` (string) [maxLen=255] — Represents the API name of the CRM module.
      - `id` (string/int64) [maxLen=255] — Represents the unique identifier of the CRM module.
    - `id` (string) [maxLen=255] — Represents the unique identifier of the Cadence.
    - `name` (string) **REQ** [maxLen=100] — Represents the name of the Cadence.
    - `description` (string) [maxLen=500] — Represents the description of the Cadence.
    - `type` (string) **REQ** [enum=['custom_view', 'manual_enrollment']] — Represents the enrollment type of the Cadence.
Possible values:
custom_view - Automatically enrolls records matching a Custom View.
manual_enrollment - Allows manual enrollment of records into the Cadence.
    - `custom_view` (object) — Represents the Custom View used for automatic record enrollment in the Cadence.
      - `id` (string/int64) **REQ** [maxLen=255] — Represents the unique identifier of the Custom View.
    - `execution_details` (object) — Represents the execution frequency and unenrollment configuration for the Cadence.
      - `execute_every` (object `ExecuteEvery`) — Represents the recurring execution interval for a Cadence, specifying the frequency period and numeric value.
        schema: `ExecuteEvery`
        - `period` (string) **REQ** [enum=['immediately', 'hours', 'days', 'weeks']] — Represents the frequency interval for recurring Cadence execution.
Possible values:
immediately - Execute immediately after each enrollment trigger.
hours - Execute at the specified number of hours interval.
days - Execute at the specified number of days interval.
weeks - Execute at the specified number of weeks interval.
        - `unit` (integer/int32) [min=1, max=99] — Represents the numeric value of the execution interval, expressed in the specified period unit.
      - `unenroll_properties` (array of object `UnenrollPropertiesNested`) [maxItems=200] — Represents the conditions under which records are automatically unenrolled from the Cadence.
        schema: `UnenrollPropertiesNested`
        - `details` (object) [nullable] — Represents the additional details for the unenrollment condition.
        - `type` (string) **REQ** [enum=['automatic_unenroll', 'end_date', 'criteria', 'followup_criteria']] — Represents the type of unenrollment condition for the Cadence.
Possible values:
automatic_unenroll - Unenroll records automatically based on the configured condition.
end_date - Unenroll records when the specified end date is reached.
criteria - Unenroll records that meet the specified criteria.
followup_criteria - Unenroll records based on follow-up criteria.
    - `follow_ups` (array of object) [maxItems=100] — Represents the list of follow-up steps configured for the Cadence.
      - `execute_after` (object `ExecuteAfterNested`) — Represents the execution delay configuration for a follow-up action, specifying the period unit and numeric value.
        schema: `ExecuteAfterNested`
        - `unit` (integer/int32) **REQ** [min=1, max=99] — Represents the numeric value of the execution delay, expressed in the specified period unit.
        - `period` (string) **REQ** [enum=['minutes', 'hours', 'business_hours', 'days', 'business_days', 'months']] — Represents the time unit for the follow-up execution delay.
Possible values:
minutes - Execution delay in minutes.
hours - Execution delay in hours.
business_hours - Execution delay in business hours.
days - Execution delay in days.
business_days - Execution delay in business days.
months - Execution delay in months.
      - `parent_follow_up` (object) — Represents the parent follow-up step that this step branches from.
        - `reference_id` (string) [maxLen=255] — Represents the reference identifier of the parent follow-up step.
      - `reference_id` (string) [maxLen=255] — Represents the unique reference identifier for the follow-up step within the Cadence.
      - `action` (object `ActionNested`) **REQ** — Cadence followup action (Required)
        oneOf:
          - `TaskTypeFollowupActionRequestObject` — Represents the follow-up step configuration for a task action in a Cadence.
            - `id` (string) [maxLen=255] — Represents the unique identifier of the task action.
            - `type` (string) **REQ** [enum=['tasks']] — Represents the action type for this follow-up step.
          - `EmailNotificationTypeFollowupActionRequestObject` — Represents the follow-up step configuration for an email notification action in a Cadence.
            - `id` (string) [maxLen=255] — Represents the unique identifier of the email notification action.
            - `type` (string) **REQ** [enum=['email_notifications']] — Represents the action type for this follow-up step.
          - `ScheduleCallTypeFollowupActionRequestObject` — Represents the follow-up step configuration for a scheduled call action in a Cadence.
            - `details` (object `AutomationScheduleCallDetails`) — Action configuration carrying module+layout+field_mappings for creating the Call record.
              schema: `AutomationScheduleCallDetails`
              - `module` (object `AutomationModuleRef`) **REQ** — Target module for the call. Must be the Calls module. Provide either api_name ("Calls") or the Calls module id.
                schema: `AutomationModuleRef`
                - `api_name` (string) [maxLen=255] — API name of the module (e.g., Leads, Contacts, Deals, Vendors).
                - `id` (string) [maxLen=20] — Unique module ID (19-digit format). Always use the full ID as returned by GET /settings/modules - truncated or shortened IDs return INVALID_DATA ('the tabId given seems to be invalid'). Optional in requests if api_name is provided; always present in responses.
              - `layout` (object `AutomationLayoutRef`) **REQ** — Layout to use when creating the Call record. Determines which fields are available and their validation rules. Fetch valid layouts from GET /settings/layouts?module=Calls. The layout.id is required.
                schema: `AutomationLayoutRef`
                - `id` (string) **REQ** [maxLen=20] — Unique layout ID. Required. Obtain from GET /settings/layouts?module={module_api_name}.
                - `name` (string) [maxLen=50, nullable] — Display name of the layout. Optional in requests; present in GET responses.
                - `display_label` (string) [maxLen=50] — Human-readable label of the layout. Present in GET responses.
              - `field_mappings` (array of object `AutomationFieldMappings`) [minItems=1, maxItems=25] **REQ** — Field mappings for the new Call. Each entry: {"field": {"api_name": "Subject"}, "type": "static", "value": "Follow-up"}. Must include all mandatory fields from GET /settings/layouts?module=Calls. Call_Type is system-mandatory (values: "Outbound", "Inbound", "Missed") - omitting returns REQUIRED_DATA_NOT_FOUND. Common fields: Subject, Call_Type, Call_Purpose, Call_Start_Time, Remind_At. Mapping types: static - literal values for text, picklist fields; NOT for DateTime/ALARM (DEPENDENT_MISMATCH). merge_field - runtime tokens like ${!Leads.Phone} for text-based fields; NOT for lookup/owner (DEPENDENT_MISMATCH). execution_time - REQUIRED for Call_Start_Time and Remind_At; sign required for datetime; periods: days, business_days, hours, minutes.
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
              - `apply_restriction` (boolean) [default=False, nullable] — Whether to enforce assignment-threshold rules (record count limits per user) on the record owner when creating the Call record. When true, the system checks whether the owner has reached their record limit before creating the record. Only effective when the org has assignment thresholds configured.
              - `id` (string) [maxLen=20] — Server-generated unique identifier for this schedule call action. Present only in GET responses; not required in POST requests.
            - `id` (string) [maxLen=255] — Represents the unique identifier of the scheduled call action in the Cadence.
            - `type` (string) **REQ** [enum=['schedule_call']] — Represents the action type for this follow-up step.
          - `WhatsappMessageNotificationTypeFollowupActionRequestObject` — Represents the follow-up step configuration for a WhatsApp message notification action in a Cadence.
            - `id` (string) [maxLen=255] — Represents the unique identifier of the WhatsApp message notification action.
            - `type` (string) **REQ** [enum=['whatsapp_message_notification']] — Represents the action type for this follow-up step.
      - `triggers` (array of string) [maxItems=500] — Represents the list of trigger conditions that determine when this follow-up step executes.
        items: [maxLen=255]

**Responses:**

- **201**: Returns the details of the newly created Cadence, including its unique identifier. — Schema: `SuccessResponse200` [application/json]
    > Represents the success response returned after a Cadence operation is completed successfully.
    schema: `SuccessResponse200`
    - `cadences` (array of object `CadencesItemNested`) [maxItems=100] — Represents the list of Cadences with their result status from the operation.
      schema: `CadencesItemNested`
      - `code` (string) [maxLen=255] — Represents the result code for the individual Cadence record operation.
      - `details` (object `DetailsNested`) — Represents the nested details of a Cadence operation result, including follow-up actions and resource identifiers.
        schema: `DetailsNested`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the resource associated with the operation.
        - `follow_ups` (array of object) [maxItems=100, nullable] — Represents the list of follow-up actions involved in the operation.
          - `id` (string) [maxLen=255] — Represents the unique identifier of the follow-up item.
          - `action` (object) — Represents the action associated with the follow-up item.
            - `id` (string) [maxLen=255] — Represents the unique identifier of the follow-up action.
            - `type` (string) [maxLen=255] — Represents the type of the follow-up action.
        - `draft_cadence` (object) — Represents the draft version of the Cadence associated with the operation.
          - `id` (string) [maxLen=255] — Represents the unique identifier of the draft Cadence.
      - `message` (string) [maxLen=255] — Represents the result message for the individual Cadence record operation.
      - `status` (string) [maxLen=255] — Represents the result status for the individual Cadence record operation.

- **400**: The request contains invalid or missing data.
**Resolution:** All required fields must be provided, field values must conform to the expected format, and the Cadence count limits must not be exceeded. [application/json]
    > Represents the error response for the Cadence creation operation.
    oneOf:
      - `ErrorResponseWithCadenceAsHead` — Represents an error response where the Cadence object serves as the top-level container for field-level errors.
        - `cadences` (array of object `AllErrorResponse`) [maxItems=300] — Represents the list of Cadences, each containing field-level error details for the corresponding request entry.
      - `AllErrorResponse` — Represents the error response returned when the API request fails due to validation errors or unsupported operations.

- **403**: The user does not have permission to create Cadences.
**Resolution:** The CRM administrator must grant the required Cadence management permission to the user's profile, and a new access token must be generated with the required scope. — Schema: `AllErrorResponse` [application/json]
    > Represents the error response returned when the API request fails due to validation errors or unsupported operations.

**Scopes:** ZohoCRM.settings.cadences.CREATE

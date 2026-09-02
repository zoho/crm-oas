# GET /workflow_configurations
**Operation:** `getWorkflowConfigurations` — Workflow Configuration
> Retrieves the available triggers, actions, and related trigger details for a specific module. Use this endpoint before creating or updating workflow rules to discover which triggers and actions are supported, their per-type limits, scheduling compatibility, and related module triggers. The response includes three sections: triggers (events that fire the rule), actions (operations executed when the rule fires), and related_triggers_details (child/related modules like Notes or Calls that can also trigger rules on the parent module).

**Parameters:**
- `module` (query, string, required) [maxLen=255]: Specify the API name of the CRM module for which you want to retrieve workflow configuration metadata. Must be a workflow-supported module (for example, Leads, Contacts, Deals, Accounts, Tasks, Cases, Products, Quotes, Sales_Orders, Purchase_Orders, Invoices, Campaigns, Vendors). Refer to the [Get Modules Metadata API](modules.yaml#$.paths./settings/modules.get) resource for valid values.

**Schemas:**
`WorkflowConfigurationsTrigger`:
  > A trigger type available for the module. Defines the event that initiates a workflow rule. Use the api_name value in the execute_when.type field when creating or updating a workflow rule via POST/PUT /settings/automation/workflow_rules.
  - `api_name` (string) [maxLen=255] — Represents the API identifier of the trigger type. Use this value in the execute_when.type field when creating a workflow rule (for example, create, edit, create_or_edit, delete, field_update, section_update, date_or_datetime, score_increase, score_decrease, score_update).
  - `deprecated` (boolean) — Indicates whether this trigger type is deprecated.
Possible values:
true - The trigger type is deprecated and should not be used for new workflow rules, though it may still appear on existing rules.
false - The trigger type is active and available for use.
  - `name` (string) [maxLen=255] — Represents the display name of the trigger type as shown in the CRM UI (for example, Create, Edit, FieldUpdate, DateBased).
  - `scheduled_actions_supported` (boolean) — Indicates whether this trigger type supports scheduled (time-delayed) actions.
Possible values:
true - Both instant_actions and scheduled_actions are available for workflow rules with this trigger.
false - Only instant_actions can be used in workflow rules with this trigger.
  - `actions` (array of string) [maxItems=20] — Represents the list of action type API names supported by this trigger. Only these action types can be used in workflow rules with this trigger type. Cross-reference with the top-level actions array in the response for full action metadata, including per-type limits and scheduling support.
    items: [maxLen=255]
  - `component_id` (string) [maxLen=255, nullable] — Represents the component identifier for marketplace or custom triggers. Returns null for standard built-in trigger types.
  - `generated_type` (string) [maxLen=255, nullable] — Represents the generated type identifier for marketplace or custom triggers. Returns null for standard built-in trigger types.

**Responses:**

- **200**: Returns the workflow configuration metadata for the specified module, including the available trigger types, action types with their per-type limits and scheduling support, and related module trigger details. — Schema: `GetworkflowconfigurationsResponse200` [application/json]
    > Response containing workflow configurations for a module including available triggers, actions, and related trigger details.
    schema: `GetworkflowconfigurationsResponse200`
    - `workflow_configurations` (object `WorkflowConfigurationsMetadata`) — Workflow configuration metadata for the requested module.
      schema: `WorkflowConfigurationsMetadata`
      - `related_triggers_details` (array of object `WorkflowConfigurationsRelatedTriggerDetail`) [maxItems=20] — List of related modules (e.g., Notes, Calls, Activities) whose record events can trigger workflow rules on the parent module. Each entry contains the related module's identity and available trigger types.
        schema: `WorkflowConfigurationsRelatedTriggerDetail`
        - `api_name` (string) [maxLen=255] — Represents the API name of the related module that can act as a trigger source (for example, Notes, Tasks, Events, Attachments). Use this value to identify the related module when creating workflow rules that should fire on related record events.
        - `module` (object `ModuleReference`) — Module identity including api_name, id, and labels.
          schema: `ModuleReference`
          - `singular_label` (string) [maxLen=255] — Represents the singular display name of the module as shown in the CRM UI (for example, Lead, Contact, Deal).
          - `plural_label` (string) [maxLen=255] — Represents the plural display name of the module as shown in the CRM UI (for example, Leads, Contacts, Deals).
          - `api_name` (string) [maxLen=255] — Represents the API name of the CRM module used in API requests (for example, Leads, Contacts, Deals, Accounts, Tasks, Cases, Products, Quotes, Sales_Orders, Invoices, Campaigns, Vendors).
          - `name` (string) [maxLen=255] — Represents the internal name of the CRM module.
          - `id` (string) [maxLen=20] — Represents the unique identifier of the CRM module.
        - `name` (string) [maxLen=255] — Represents the display name of the related module.
        - `triggers` (array of object `WorkflowConfigurationsTrigger`) [maxItems=20] — Represents the list of trigger types available from this related module. These triggers can be used in workflow rules on the parent module via the execute_when.details.trigger_module field.
      - `triggers` (array of object `WorkflowConfigurationsTrigger`) [maxItems=20] — Represents the list of trigger types available for the module. Each entry defines an event that can initiate a workflow rule, along with the action types supported for that trigger (for example, create, edit, delete, field_update, date_or_datetime).
      - `actions` (array of object `WorkflowConfigurationsAction`) [maxItems=20] — List of available action types for the module. Each action defines an operation that can be performed when the workflow rule fires, along with its per-type limit (applies independently to instant_actions and scheduled_actions), scheduling support, and whether it is an associate action (reusable entity referenced by ID) or non-associate action (defined inline).
        schema: `WorkflowConfigurationsAction`
        - `is_clickable` (boolean) — Indicates whether this action type can be edited directly from the workflow configuration UI page. Not relevant for API usage.
        - `associate_action` (boolean) — Indicates whether this action type is an associate action. Associate actions link or associate records between modules (for example, linking a Contact to a Deal or associating a Product with an Order). Associate actions differ from standard data-write actions such as field_updates or email_notifications.
Possible values: **true** - This action type is an associate action. **false** - This action type is a standard non-associate action.
        - `limit_per_action` (integer/int32) [nullable] — Represents the maximum number of items within a single action instance. For example, add_tags and remove_tags allow a maximum of 10 tags per action. Returns null if no per-action item limit applies.
        - `api_name` (string) [maxLen=255] — Represents the API identifier of the action type used when creating or modifying workflow rules (for example, field_updates, email_notifications, webhooks, assign_owner, add_tags, remove_tags, create_record, add_meeting, schedule_call, convert, functions, flow).
        - `supported_in_scheduled_action` (boolean) — Indicates whether this action type can be used as a scheduled (time-delayed) action in a workflow rule. **Possible values:** true - This action type is supported in scheduled_actions (for example, time-delayed email_notifications or field_updates). false - This action type is only supported in instant_actions.
        - `name` (string) [maxLen=255] — Represents the display name of the action type as shown in the CRM UI.
        - `limit` (integer/int32) [min=1] — Maximum number of instances of this action type allowed per workflow rule. Applies independently to instant_actions and scheduled_actions - for instance, if limit=5, you can add up to 5 instances in instant_actions and up to 5 in scheduled_actions. Returns LIMIT_EXCEEDED if exceeded.

- **400**: The module query parameter is missing from the request, or the specified module API name is not valid. Resolution: The module query parameter must be included in the request with a valid workflow-supported module API name. [application/json]
    > Represents the error response for a missing or invalid module query parameter.
    oneOf:
      - `RequiredParamMissingError` — Represents the error response when the required module query parameter is omitted from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code indicating a required parameter is missing.
        - `details` (object) **REQ** — Represents the object containing details about the missing parameter.
          - `param_name` (string) [enum=['module']] — Represents the name of the missing required parameter.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.
      - `InvalidModuleResponse` — Represents the error response when the module query parameter value does not correspond to a valid CRM module or a workflow-supported module.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code indicating the module API name is invalid.
        - `details` (object) **REQ** — Represents the object containing details about the invalid parameter.
          - `param_name` (string) [enum=['module']] — Represents the name of the parameter that contains the invalid value.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.

- **403**: The requesting user lacks the Manage Automation Actions privilege, or the workflow feature is unavailable in the current CRM edition. Resolution: The CRM administrator must grant the Crm_Implied_Manage_Workflow permission to the user's profile. — Schema: `NoPermissionError` [application/json]
    > Represents the error response when the user lacks the required Manage Automation Actions privilege or when the workflow feature is unavailable in the current CRM edition.
    schema: `NoPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION', 'FEATURE_NOT_SUPPORTED']] — Represents the error code indicating the type of permission or feature availability error.
Possible values:
NO_PERMISSION - The user's profile lacks the required privilege.
FEATURE_NOT_SUPPORTED - The workflow feature is unavailable in the current CRM edition.
 
    - `details` (object) **REQ** — Represents the object containing details about the missing permission.
      - `permissions` (array of string) [maxItems=5] — Represents the list of required permissions that the user's profile is missing.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Represents the permission error message describing the issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.

**Scopes:** ZohoCRM.settings.workflow_rules.READ

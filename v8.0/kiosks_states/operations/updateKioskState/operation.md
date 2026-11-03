# PUT /settings/kiosks/{kioskId}/states/{stateId}
**Operation:** `updateKioskState` — Kiosk State
> To update a particular state in a specific Kiosk in Zoho CRM using the Kiosk ID and state ID. Each state represents a screen, action, decision, or GetRecords.
A Kiosk must be in the draft status to update a state. This operation is not supported when the Kiosk is in the published or inactive status.
You can update only one state per request.
The state must already exist before it can be updated. To create a new state, use the [Create a Kiosk State API](kiosks_states.yaml#$.paths./settings/kiosks/{kioskId}/states.post). Once the Kiosk is fully configured, [publish](kiosks.yaml#$.paths./settings/kiosks/{kioskId}/actions/activate.put) it and [associate](kiosks_get_records.yaml#$.paths./settings/kiosks/{kioskId}/associations.put) it with the required CRM component.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=255]: Specify the unique identifier of the Kiosk.
- `stateId` (path, string, required) [maxLen=255]: Specify the unique identifier of the kiosk state.

**Schemas:**
`ActionAttachment`:
  > Represents a single attachment entry for a note created by the add note action. Each entry contains a merge field reference to a File Upload field.
  - `id` (string) [maxLen=200, nullable] — Represents a merge field reference to a File Upload field. Three formats are supported: (1) Record field — `${!<kiosk_group_api_name>.<resource_api_name>.<field_api_name>}`, where the resource is `CurrentRecord` or a GetRecord API name (for example, `GetRecords_1`). (2) CRM module field — `${!<module_api_name>.<field_api_name>}`, for example, `${!users.email}`. (3) Kiosk screen field — `${!<kiosk_group_api_name>.<screen_field_api_name>}`, which references a File Upload field on a kiosk screen.
`ActionEmailNotificationUpdate`:
  > Email notifications action will be used to trigger emails with pre-defined template and content to the configured records. This is an associate action and hence this JSON will consist of the email notification action's identifiers like ID and name. It is mandatory for the action to be created before associating in the Kiosk. A specific action can be associated with only one state in the Kiosk.
  - `name` (string) [maxLen=50, nullable] — Represents the name of the email notification action pre-created in Zoho CRM Workflow and associated with the kiosk action state.
  - `id` (string) [maxLen=20] — Represents the record ID of the email notification action pre-created in Zoho CRM Workflow and associated with the kiosk action state.
`ActionExecuteForRecordUpdate`:
  > For associate actions and few non associate actions, the action should be performed on a specific record in the CRM system. For example, if the user is creating the field update action to modify a company name, he must provide which record's company name should be changed. So, he should provide either a get record reference or a current record reference in "execute_for_record" key. ID and name of the resource will be enough. However, for actions which are unrelated for a specific record, this key can be ignored. 
  - `name` (string) [maxLen=50, nullable] — Represents the display name of the resource used for the action.
  - `id` (string) [maxLen=19, nullable] — Represents the ID of the resource used for the action. This ID identifies the specific get_record or current_record component to be retrieved when performing the action.
`ActionFieldUpdatesUpdate`:
  > In case the action type is "field_updates", this key is mandatory. It contains the information or identifier of the "Field update" action configured in the workflow. If we give ID of the configured action, it will be associated here. It is mandatory for this field update action id to be associated in only one place or state of the Kiosk. You cannot a single field update action in many action states.
  - `name` (string) [maxLen=50, nullable] — Represents the name of the field update action associated with the kiosk action state.
  - `id` (string) [maxLen=20] — Represents the record ID of the field update action associated with the kiosk action state.
`ActionFunctionsUpdate`:
  > Functions is an associated action which will execute a piece of code or other operations upon execution. These functions would have been created either previously or during the creation of the action which can be associated and run during action execution. It acts as a server-side function executed when kiosk is executed.
  - `name` (string) [maxLen=50, nullable] — Represents the name of the function action pre-created in Zoho CRM workflow and associated with the kiosk action state.
  - `id` (string/int64) — Represents the record ID of the function action pre-created in Zoho CRM workflow and associated with the kiosk action state.
`ActionGetRecordAssociationUpdate`:
  > This is the JSON which contains the association details of the get_record component for a get_records state.
  - `name` (string) [maxLen=50, nullable] — Represents the name of the get_record component associated with this kiosk state.
  - `id` (string) [maxLen=18, nullable] — Represents the ID of the get_record component associated with this kiosk state.
`ActionLayoutUpdate`:
  > Layout configuration used when creating the record.
  - `name` (string) [maxLen=50, nullable] — Represents the API name of the layout for the meeting event being created.
  - `id` (string) [maxLen=19, nullable] — Represents the layout ID for the meeting event being created.
`ActionModuleUpdate`:
  > Specifies the CRM module to which the note will be associated. For example, Leads module can have a note associated with it.
  - `api_name` (string) [maxLen=50, nullable] — Represents the API name of the CRM module to use when creating the meeting event.
  - `id` (string) [maxLen=19, nullable] — Represents the unique identifier of the CRM module to use when creating the meeting event.
`ActionNoteUpdate`:
  > Configuration used to create a note associated with a CRM record. For example, a specific Lead detail view page can have a note by running this particular action.
  - `attachments` (array of object `ActionAttachment`) [maxItems=10, nullable] — Represents the list of attachments for the note created by the add note action. Each object contains a merge field reference to a File Upload field.
  - `title` (string) [maxLen=50, nullable] — Represents the title of the note associated with the CRM record.
  - `content` (string) [maxLen=5000, nullable] — Represents the content of the note displayed on the record detail view.
  - `module` (object `ActionModuleUpdate`) — Specifies the CRM module to which the note will be associated. For example, Leads module can have a note associated with it.
`ActionOpenLinkUpdate`:
  > Open link is an action used to open a specific link which is configured during state creation when triggered. This json will consist of the link and encoding details.
  - `encode` (string) [maxLen=50, enum=['UTF-8', 'UTF-16', 'ISO-8859-1', 'ISO-8859-9', 'GB2312', 'Big5', 'Shift_JIS'], nullable] — Represents the character encoding used when opening the URL, for example, UTF-8.
  - `name` (string) [maxLen=250, nullable] — Represents the display name of the open link action state.
  - `link` (string) [maxLen=1000, nullable] — Represents the URL to be opened when the action is executed. The value must be a valid URL.
`ActionOpenRecordUpdate`:
  > It is an action to open a particular record fetched from the CRM modules. The user will configure either a get record or a current record with this action. The fetched record is opened automatically when the action is executed.
  - `name` (string) [maxLen=250, nullable] — Represents the display name of the open record action state.
  - `id` (string) [maxLen=19, nullable] — Represents the unique ID of the open record action.
`ActionQuickCreateRecordUpdate`:
  > It is an action used to quickly configure a create record action with minimal field input. However, there will be a pop up during the execution of the action where the user must provide the values for the fields configured. Then, the record will be created.
  - `field_mappings` (array of object `AutomationFieldMappings`) [maxItems=30, nullable] — Represents the field mappings that define the fields and their values used to populate the record during creation.
  - `layout` (object `ActionLayoutUpdate`) — Layout configuration used when creating the record.
  - `module` (object `ActionModuleUpdate`) — Specifies the CRM module in which the record will be created.
`ActionTasksUpdate`:
  > Tasks is another associate action which helps in assigning tasks to specific records. This JSON will consist of the resource identifiers for the Tasks action in the workflow.
  - `name` (string) [maxLen=250, nullable] — Represents the name of the task action pre-created in Zoho CRM Workflow and associated with the kiosk state.
  - `id` (string) [maxLen=255] — Represents the record ID of the task action pre-created in Zoho CRM Workflow and associated with the kiosk state. Each task action can be associated with only one kiosk state.
`ActionUpdateDetails`:
  > Represents the optional execute_for_record property, which identifies the CRM record or get_record component on which the action is performed.
`ActionWebhooksUpdate`:
  > Represents a webhook action that triggers an external HTTP callback when executed. The webhook configuration can be done during the creation of the state. However, these configuration details won't come in the webhook action payload. The payload will only refer the webhook created.
  - `name` (string) [maxLen=20, nullable] — Represents the name of the webhook action pre-created in Zoho CRM Workflow and associated with the kiosk action state.
  - `id` (string/int64) [maxLen=20] — Represents the record ID of the webhook action pre-created in Zoho CRM Workflow and associated with the kiosk action state.
`AutomationAddMeetingDetails`:
  > Configuration for the add_meeting action. Referenced from AutomationNonAssociateActions.json. MANDATORY: id (state id), and id (action's id inside "details")  is mandatory for update.
  - `module` (object `AutomationModuleRef`) **REQ** — Target module for the meeting. Must be the Events module. Provide either api_name ("Events") or the Events module id.
  - `layout` (object `AutomationLayoutRef`) **REQ** — Layout to use when creating the Event record. Determines which fields are available and their validation rules. Fetch valid layouts from GET /settings/layouts?module=Events. The layout.id is required.
  - `field_mappings` (array of object `AutomationFieldMappings`) [minItems=1, maxItems=25] **REQ** — Field mappings for the new Event. Each entry: {"field": {"api_name": "Event_Title"}, "type": "static", "value": "Meeting"}. Must include all mandatory fields from GET /settings/layouts?module=Events. Common fields: Event_Title, Start_DateTime, All_Day, Participants (composite type), Remind_At. End_DateTime is auto-computed from Start_DateTime + meeting_duration - do NOT provide it. Mapping types: static - literal values for text, picklist fields; NOT for DateTime/ALARM (DEPENDENT_MISMATCH). merge_field - runtime tokens like ${!Leads.Company} for text-based fields; NOT for lookup/owner (DEPENDENT_MISMATCH). execution_time - REQUIRED for Start_DateTime and Remind_At; sign required for datetime; periods: days, business_days, hours, minutes. When All_Day=true, period must be "days" and omit meeting_duration.
  - `meeting_duration` (object `AutomationMeetingDuration`) **REQ** — Duration of the meeting. Specifies a numeric value and time period (e.g., 1 hour, 30 minutes). Required when All_Day is not set to true in field_mappings. If All_Day is true, meeting_duration must not be provided  - the API returns INVALID_DATA with field1/field2 conflict details.
  - `host_unavailable` (object `AutomationHostUnavailable`) — Fallback behavior when the designated meeting host is unavailable. Either assign the record owner as host (assign_record_owner_as_host=true) or create a follow-up task (assign_task with a pre-configured task ID). Exactly one option must be specified; providing both returns INVALID_DATA with field1/field2 conflict, providing neither returns EXPECTED_FIELD_MISSING.
  - `apply_restriction` (boolean) [default=False, nullable] — Whether to enforce assignment-threshold rules (record count limits per user) on the record owner when creating the Event record. When true, the system checks whether the owner has reached their record limit before creating the record. Only effective when the org has assignment thresholds configured.
  - `id` (string) [maxLen=20] — Server-generated unique identifier for this add meeting action. Present only in GET responses; not required in POST requests.
`AutomationAddTagsDetails`:
  > Configuration for the add_tags action. Referenced from AutomationNonAssociateActions.json. MANDATORY: id (state id), and id (action's id inside "details") is mandatory for update.
  - `over_write` (boolean) [default=False] — Whether to overwrite all existing tags on the record with the specified tags (true) or append to existing tags (false). Default is false. When set to true, any RemoveTags action in the same workflow rule becomes invalid and returns INVALID_DATA ('Remove tag not supported with Overwrite Add Tag').
  - `tags` (array of object `AutomationTagRef`) [minItems=1, maxItems=10] **REQ** — List of tags to add to the record. All tags must pre-exist in the org  - fetch available tags from GET /settings/tags?module={module_api_name}. To create new tags: POST /settings/tags?module={module_api_name}. If the list is empty after parsing, the API returns FAILURE ('Empty Tag'). If the tag count exceeds the edition limit, the API returns FAILURE ('Invalid Tag Count').
  - `module` (object `AutomationModuleRef`) — Target module for the tag action. Must match the workflow rule's trigger module. Supported modules: Leads, Accounts, Contacts, Deals, Campaigns, Tasks, Cases, Events, Calls, Solutions, Products, Vendors, Price_Books, Quotes, Sales_Orders, Purchase_Orders, Invoices, and custom modules. Unsupported modules (Visits, Users, LinkingModules) return NOT_ALLOWED.
  - `id` (string) [maxLen=20] — Server-generated unique identifier for this add tags action. Present only in GET responses; not required in POST requests.
`AutomationAssignOwnerDetails`:
  > Configuration for the assign_owner action. Referenced from AutomationNonAssociateActions.json. MANDATORY: id (state id), and id (action's id inside "details")  is mandatory for update.
  - `module` (object `AutomationModuleRef`) **REQ** — Target module for the ownership assignment. Must match the workflow rule's trigger module for direct assignments, or the lookup field's related module for cross-module assignments. At least api_name or id must be provided; if both are given and they do not match, the API returns AMBIGUITY_DURING_PROCESSING.
  - `assign_to` (array of object) [minItems=1, maxItems=5] **REQ** — Specifies how the new owner is determined. Each entry defines an assignment method  - a specific user, role, group, assignment rule, profile, merge field, or criteria-based filter. For round-robin assignment across multiple users, provide multiple entries of type=user. For criteria-based assignment, provide a single entry of type=criteria with filter conditions.
    oneOf:
      - `AutomationAssignToResourceEntry` — PURPOSE: assign_to entry for resource-based ownership. MANDATORY: type (user|role|group|assignment_rule|profile), resource ({id, name}). For type=profile: associated_to must be 'team_profile'. For round-robin: use multiple entries of type=user.
      - `AutomationAssignToMergeFieldEntry` — PURPOSE: assign_to entry for merge-field-based ownership. Resolves to a user at execution time from a user-type field. MANDATORY: type (const 'merge_field'), details.api_name (merge field token e.g., '${!Leads.Created_By}'). Field must be data_type=ownerlookup or userlookup. GET /settings/fields?module={api_name} to discover.
      - `AutomationAssignToCriteriaEntry` — PURPOSE: assign_to entry for criteria-based ownership. Evaluates filter criteria against the triggering record at execution time. MANDATORY: type (const 'criteria'), details.criteria (filter condition - simple or grouped with AND/OR). Criteria fields must reference valid trigger module fields - GET /settings/fields?module={api_name}.
  - `related_records` (array of object `AutomationRelatedRecord`) [maxItems=5, nullable] — Related modules whose open record ownership should also be transferred when the parent record is reassigned. Common activity modules (Tasks, Calls, Events) are available for all modules. Additional modules depend on the parent module: Accounts can also include Contacts and Deals; Contacts can also include Deals. Null when no related modules are selected for ownership transfer.
  - `notify` (boolean) [default=False] — Whether to send an email notification to the new owner when the record is reassigned. When true, the newly assigned owner receives an email informing them of the ownership change.
  - `apply_assignment_threshold` (boolean) [default=False] — Whether to enforce assignment-threshold rules (record count limits per user) when assigning ownership. When true, the system checks whether the new owner has reached their record limit before applying the assignment. Only effective when the org has assignment thresholds configured.
  - `user_availability_based_on` (array of string) [maxItems=1, nullable] — Restricts assignment to users who are currently available. When set to ["online_status"], only users logged in to the Zoho CRM web interface are eligible for assignment. If the selected user is offline, the assignment is skipped or deferred. Null means no availability check is applied.
    items: [enum=['online_status']]
  - `lookup_field` (object `AutomationLookupFieldRef`) — The lookup field linking the trigger module to the target module. Required only for cross-module assign owner actions (where the action's module differs from the workflow rule's trigger module). For same-module assignments, this field is omitted and the action operates directly on the triggering record.
  - `id` (string) [maxLen=20] — Server-generated unique identifier for this assign owner action. Present only in GET responses; not required in POST or PUT requests.
`AutomationAssignOwnerResource`:
  > Identifies the target user, role, group, assignment rule, or profile by ID and/or name. At least one of id or name must be provided; if both are given and they do not match, the API returns AMBIGUITY_DURING_PROCESSING.
  - `id` (string) **REQ** [maxLen=255] — Unique identifier of the target entity. Obtain from the corresponding API: GET /settings/users (for user), GET /settings/roles (for role), GET /settings/user_groups (for group), GET /settings/automation/assignment_rules (for assignment_rule), or GET /settings/profiles (for profile).
  - `name` (string) [maxLen=255] — Display name of the target entity. Optional in POST/PUT requests (server resolves from id); always present in GET responses.
  - `type` (string) [enum=['user', 'role', 'group', 'assignment_rule', 'profile']] — Type of the target entity. Present in GET responses; not required in POST/PUT requests.
`AutomationAssignToCriteriaEntry`:
  > PURPOSE: assign_to entry for criteria-based ownership. Evaluates filter criteria against the triggering record at execution time. MANDATORY: type (const 'criteria'), details.criteria (filter condition - simple or grouped with AND/OR). Criteria fields must reference valid trigger module fields - GET /settings/fields?module={api_name}.
  - `type` (string) **REQ** [const=criteria] — Assignment method indicating criteria-based evaluation.
  - `details` (object) **REQ** — Contains the filter criteria to evaluate against the triggering record.
    - `criteria` (object `FilterCriterionRequest`) **REQ** — Filter criteria defining when this assignment applies. Can be a simple condition (field + comparator + value) or a grouped condition (group_operator + group array). The field references in criteria must be valid fields of the trigger module  - fetch available fields from GET /settings/fields?module={module_api_name}. For example: {"field": {"api_name": "Department"}, "comparator": "equal", "value": "Engineering"} assigns ownership when the record's Department is Engineering.
  - `resource` (null) — Always null for criteria-based assignments. The owner is determined by the criteria evaluation logic.
  - `allow_agent_user` (boolean) [default=False] — Whether to allow assignment to an agent user or not. When true, the record can be assigned to an agent user also. When false, agent users are excluded from assignment. Applicable only for types: role, group, profile, merge_field, criteria. Not supported for types user and assignment_rule.
`AutomationAssignToMergeFieldEntry`:
  > PURPOSE: assign_to entry for merge-field-based ownership. Resolves to a user at execution time from a user-type field. MANDATORY: type (const 'merge_field'), details.api_name (merge field token e.g., '${!Leads.Created_By}'). Field must be data_type=ownerlookup or userlookup. GET /settings/fields?module={api_name} to discover.
  - `type` (string) **REQ** [const=merge_field] — Assignment method indicating merge field resolution.
  - `details` (object) **REQ** — Contains the merge field reference that resolves to a user at execution time.
    - `api_name` (string) **REQ** [maxLen=255] — Merge field token referencing a user-type field. Must use the format ${!Module.User_Field} ,${!Module.Lookup_Field_API_Name.User_Field} where Field is a user-type field (data_type=ownerlookup or userlookup) from the trigger module. Fetch valid fields from GET /settings/fields?module={module_api_name}. Common user-type fields: Owner, Created_By, Modified_By. Examples: ${!Leads.Created_By}, ${!Deals.Owner}, ${!Contacts.Account_Manager}.
  - `resource` (null) — Always null for merge field assignments. The owner is resolved dynamically from the merge field at execution time.
  - `allow_agent_user` (boolean) [default=False] — Whether to allow assignment to an agent user or not. When true, the record can be assigned to an agent user also. When false, agent users are excluded from assignment. Applicable only for types: role, group, profile, merge_field, criteria. Not supported for types user and assignment_rule.
`AutomationAssignToResourceEntry`:
  > PURPOSE: assign_to entry for resource-based ownership. MANDATORY: type (user|role|group|assignment_rule|profile), resource ({id, name}). For type=profile: associated_to must be 'team_profile'. For round-robin: use multiple entries of type=user.
  - `type` (string) **REQ** [enum=['user', 'role', 'group', 'assignment_rule', 'profile']] — Assignment method. Determines what kind of entity receives ownership. Values: "user" - assign to a specific CRM user (GET /settings/users), for round-robin include multiple assign_to entries of type=user; "role" - assign to a user holding the specified role (GET /settings/roles), system picks an eligible user at execution time; "group" - assign to a member of the specified user group (GET /settings/user_groups); "assignment_rule" - assign using a pre-configured assignment rule (GET /settings/automation/assignment_rules), the rule's criteria and round-robin logic determine the final owner; "profile" - assign to a user matching the specified profile (GET /settings/profiles), must include associated_to=team_profile.
  - `resource` (object `AutomationAssignOwnerResource`) **REQ** — Identifies the target user, role, group, assignment rule, or profile by ID and/or name. At least one of id or name must be provided; if both are given and they do not match, the API returns AMBIGUITY_DURING_PROCESSING.
  - `allow_agent_user` (boolean) [default=False] — Whether to allow assignment to an agent user or not. When true, the record can be assigned to an agent user also. When false, agent users are excluded from assignment. Applicable only for types: role, group, profile, merge_field, criteria. Not supported for types user and assignment_rule.
  - `associated_to` (string) [enum=['team_profile', None], nullable] — Association context for profile-based assignment. Must be "team_profile" when type=profile. Not applicable for other assignment types; if provided for a non-profile type, the API returns DEPENDENT_MISMATCH.
  - `details` (null) — Always null for resource-based assignments. Present in GET responses for schema consistency with other assign_to types.
`AutomationConvertChangeOwner`:
  > New owner assignment for the converted records. Specifies the user (by id) who should own the converted records, which modules should receive the new owner (via related_modules), and whether to enforce assignment thresholds. When omitted, the source record's owner is retained.
  - `id` (string) **REQ** [maxLen=20] — Unique user ID of the new owner. Obtain from GET /users. Must be an active user with permissions on the target modules.
  - `name` (string) [maxLen=255] — Full name of the new owner. Optional  - present in GET responses for display purposes.
  - `related_modules` (array of object `AutomationRelatedRecord`) [maxItems=10] — List of target modules whose records should receive the new owner during conversion. Reuses the same related-record concept as assign_owner. For Leads conversion: Events, Calls, Tasks, Contacts, Deals are valid. For Quotes/SalesOrders conversion: only Events, Calls, Tasks are valid.
  - `apply_assignment_threshold` (boolean) [default=False] — Whether to enforce assignment-threshold rules (record count limits per user) on the new owner for each converted module. When true, the system checks whether the new owner has reached their record limit before assigning ownership.
`AutomationConvertDetails`:
  > Configuration for the convert action. Referenced from AutomationNonAssociateActions.json. MANDATORY: id (state id), and id (action's id inside "details")  is mandatory for update.
  - `add_to_existing_contact` (boolean) [default=False] — MANDATORY for Leads conversion (omitting returns MANDATORY_NOT_FOUND). Whether to link the converted record to an existing Contact instead of creating a new one. Only applicable for Leads module. When true, if a matching Contact exists (based on duplicate-check criteria), the Lead is merged into it rather than creating a new Contact. Not applicable for Quotes or Sales_Orders conversions.
  - `add_to_existing_account` (boolean) [default=False] — MANDATORY for Leads conversion (omitting returns MANDATORY_NOT_FOUND). Whether to link the converted record to an existing Account instead of creating a new one. Only applicable for Leads module. When true, if a matching Account exists (based on Company name), the Lead is linked to it rather than creating a new Account. Not applicable for Quotes or Sales_Orders conversions.
  - `move_attachment_to` (object `AutomationModuleRef`) — Target module to which attachments from the source record should be moved during conversion. For Leads: typically Contacts or Accounts. For Quotes/SalesOrders: the target conversion module. Provide api_name and/or id.
  - `carry_tags` (array of object `AutomationModuleRef`) [maxItems=10] — List of target modules that should inherit tags from the source record during conversion. For Leads: may include Contacts, Accounts, Deals. Each entry identifies a module by api_name and/or id.
  - `field_mappings` (array of object `AutomationFieldMappings`) [maxItems=25] — List of field-value pairs to populate in the converted record(s). Each entry maps a target field to a value using one of the supported types: static, merge_field, or execution_time. For Leads conversion, field mappings can target Contacts, Accounts, and Deals modules. Fetch available fields from GET /settings/fields?module={target_module_api_name}.
  - `create_deal` (boolean) [default=False] — Whether to create a Deal record as part of Leads conversion. Only applicable when the trigger module is Leads. When true, the Deal module field mappings in field_mappings are used to populate the new Deal.
  - `change_owner` (object `AutomationConvertChangeOwner`) — New owner assignment for the converted records. Specifies the user (by id) who should own the converted records, which modules should receive the new owner (via related_modules), and whether to enforce assignment thresholds. When omitted, the source record's owner is retained.
  - `contact_role` (string) [maxLen=20] — Unique ID of the Contact Role to assign when a Deal is created during Leads conversion. Only applicable when create_deal=true. Obtain valid Contact Role IDs from GET /Contacts/roles.
  - `convert_to` (object) — MANDATORY for Quotes and Sales_Orders conversion (omitting returns MANDATORY_NOT_FOUND). Identifies the target module for conversion as an object with api_name and id. For Quotes: convert_to can be {api_name: 'SalesOrders', id: '<module_id>'} or {api_name: 'Invoices', id: '<module_id>'}. For Sales_Orders: convert_to must be {api_name: 'Invoices', id: '<module_id>'}. Obtain the module id from GET /settings/modules. Not applicable for Leads conversion (Leads always convert to Contacts+Accounts, optionally +Deals).
    - `api_name` (string) **REQ** [maxLen=50] — API name of the target module. For Quotes: 'SalesOrders' or 'Invoices'. For Sales_Orders: 'Invoices'.
    - `id` (string) **REQ** [maxLen=20] — Unique 19-digit module ID of the target module. Obtain from GET /settings/modules. Always use the full 19-digit ID as returned by the API; truncated IDs cause INVALID_DATA.
  - `portal_user_type` (object) — Portal user type to assign during Leads conversion. Only applicable when the org has portals configured and the converted Contact should be provisioned as a portal user. The id and name must match an existing portal user type - validated against the org's portal metadata (CrmClientPortalFilterUtil). Not applicable for Quotes or Sales_Orders conversions.
    - `id` (string) **REQ** [maxLen=20] — Unique identifier of the portal user type. Must match an existing portal user type in the org's portal configuration.
    - `name` (string) **REQ** [maxLen=100] — Display name of the portal user type.
  - `apply_restriction` (boolean) [default=False, nullable] — Whether to enforce assignment-threshold rules on the record owner during conversion. Present in GET responses.
  - `id` (string) [maxLen=20] — Server-generated unique identifier for this convert action. Present only in GET responses; not required in POST requests.
`AutomationCreateRecordDetails`:
  > Configuration for the create_record action. Referenced from AutomationNonAssociateActions.json. MANDATORY: id (state id), and id (action's id inside "details")  is mandatory for update.
  - `module` (object `AutomationModuleRef`) **REQ** — Target module in which the new record will be created. Supported modules: Leads, Contacts, Potentials (Deals), Accounts, Products, Cases, custom modules, and team modules. NOT supported: Tasks, Events, Calls - use add_meeting for Events and schedule_call for Calls. Fetch available modules from GET /settings/modules. At least api_name or id must be provided; always use the full 19-digit module ID as returned by the modules API.
  - `layout` (object `AutomationLayoutRef`) **REQ** — Layout to use when creating the record. Determines which fields are available and their validation rules. Fetch valid layouts from GET /settings/layouts?module={module_api_name}. The layout.id is required.
  - `field_mappings` (array of object `AutomationFieldMappings`) [minItems=1, maxItems=25] **REQ** — Field mappings for the new record. Each entry: {"field": {"api_name": "Last_Name"}, "type": "static", "value": "Test"}. Must include all mandatory fields (system_mandatory=true or api_mandatory=true from GET /settings/layouts?module={module}) - missing ones cause REQUIRED_DATA_NOT_FOUND. Mapping types: static - literal values for text, picklist, phone, number fields; NOT for Date/DateTime/ALARM (DEPENDENT_MISMATCH) or unique fields (INVALID_DATA, check unique=true in GET /settings/fields). merge_field - runtime tokens like ${!Leads.Company} for text-based fields; NOT for lookup/owner fields (DEPENDENT_MISMATCH). execution_time - REQUIRED for Date/DateTime/ALARM fields; periods: days, business_days, hours, minutes; sign required for datetime fields.
  - `apply_restriction` (boolean) [default=False, nullable] — Whether to enforce assignment-threshold rules (record count limits per user) on the record owner when creating the record. When true, the system checks whether the owner has reached their record limit before creating the record. Only effective when the org has assignment thresholds configured.
  - `id` (string) [maxLen=20] — Server-generated unique identifier for this create record action. Present only in GET responses; not required in POST requests.
`AutomationFieldAttributes`:
  > Target field to populate when the automation executes. api_name is required. If id is also provided, both must refer to the same field; otherwise the API returns AMBIGUITY_DURING_PROCESSING.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the target field in the destination module — for example, Subject, Due_Date, or Owner — used to identify the field receiving the mapped value within automation actions such as workflow tasks, create_record, and convert.
  - `id` (string) **REQ** [maxLen=255] — Represents the numeric identifier of the target CRM field. Used in conjunction with the field's API name, both of which must resolve to the same field for a mapping to be valid.
`AutomationFieldMappings`:
  discriminator: `type`
    static → #/components/schemas/StaticFieldMapping
    merge_field → #/components/schemas/MergeFieldMapping
    execution_time → #/components/schemas/ExecutionTimeFieldMapping
    composite → #/components/schemas/CompositeFieldMapping
  oneOf:
    - `StaticFieldMapping` — Represents a static-type mapping that assigns a literal value directly to the target field at execution time. The value shape varies by field data type: a plain string for text, picklist, phone, email, URL, number, decimal, currency, and percentage fields (numeric values expressed as strings); an array of strings for multiselectpicklist fields; and an object containing ID and name for ownerlookup fields. Date, datetime, and ALARM fields do not support this type — use execution_time instead, as static on those fields produces a DEPENDENT_MISMATCH error. Fields marked unique in the module settings also require merge_field rather than static for create_record actions.
    - `MergeFieldMapping` — Represents a merge_field-type mapping whose value is resolved at execution time by substituting token references with live field data. Supports direct field tokens (${!Module.Field}), traversal tokens (${!Module.Lookup.Field}), and system tokens (${CURRENTTIME}, ${CURRENTUSER}). Applies to text-based fields such as Subject, Description, and custom text fields. Targeting owner or lookup fields with this type produces a DEPENDENT_MISMATCH error; those fields require a static mapping using an object with a numeric identifier and an optional name. Multiple tokens may be chained with surrounding text for multi-line fields, while single-value fields such as email or URL accept exactly one token.
    - `ExecutionTimeFieldMapping` — Represents an execution_time-type field mapping that computes a date, datetime, or ALARM value at runtime by applying a signed offset to a trigger field or the current time. The value carries an ExecutionTimeValue object specifying the period, unit, trigger_field, and optional time or notify_type properties. A plus sign places the result after the trigger; a minus sign places it before. ALARM fields always require minus. Workflow task actions support only days and business_days as period values.
    - `CompositeFieldMapping` — Represents a composite-type field mapping used exclusively for the Participants field in the Events module via the add_meeting action. The value carries a structured object that encodes participant data and is not applicable to any other field or automation action type.
`AutomationHostUnavailable`:
  > Fallback behavior when the designated meeting host is unavailable. Either assign the record owner as host (assign_record_owner_as_host=true) or create a follow-up task (assign_task with a pre-configured task ID). Exactly one option must be specified; providing both returns INVALID_DATA with field1/field2 conflict, providing neither returns EXPECTED_FIELD_MISSING.
  - `assign_record_owner_as_host` (boolean) — When true, the record owner is automatically assigned as the host/caller if the originally designated host is unavailable. Mutually exclusive with assign_task.
  - `assign_task` (object) — A follow-up task to create when the host is unavailable. Mutually exclusive with assign_record_owner_as_host. The task must be pre-configured in the CRM.
    - `name` (string) [maxLen=255] — Name of the follow-up task.
    - `id` (string) **REQ** [maxLen=20] — Unique ID of the pre-configured task.
`AutomationLayoutRef`:
  > Layout to use when creating the record. Determines which fields are available and their validation rules. Fetch valid layouts from GET /settings/layouts?module={module_api_name}. The layout.id is required.
  - `id` (string) **REQ** [maxLen=20] — Unique layout ID. Required. Obtain from GET /settings/layouts?module={module_api_name}.
  - `name` (string) [maxLen=50, nullable] — Display name of the layout. Optional in requests; present in GET responses.
  - `display_label` (string) [maxLen=50] — Human-readable label of the layout. Present in GET responses.
`AutomationLookupFieldRef`:
  > The lookup field linking the trigger module to the target module. Required only for cross-module assign owner actions (where the action's module differs from the workflow rule's trigger module). For same-module assignments, this field is omitted and the action operates directly on the triggering record.
  - `api_name` (string) [maxLen=255] — API name of the lookup field (e.g., Lookup_1_same, Lookup_2_cont).
  - `id` (string) [maxLen=20] — Unique field ID of the lookup field.
`AutomationMeetingDuration`:
  > Duration of the meeting. Specifies a numeric value and time period (e.g., 1 hour, 30 minutes). Required when All_Day is not set to true in field_mappings. If All_Day is true, meeting_duration must not be provided  - the API returns INVALID_DATA with field1/field2 conflict details.
  - `unit` (integer/int32) **REQ** — The numeric duration value (e.g., 1, 2, 30).
  - `period` (string) **REQ** [maxLen=10, enum=['hours', 'minutes']] — The time unit for the duration. "hours" - duration in hours (e.g., unit=1, period=hours means a 1-hour meeting). "minutes" - duration in minutes (e.g., unit=30, period=minutes means a 30-minute meeting).
`AutomationModuleRef`:
  > Target module for the tag action. Must match the workflow rule's trigger module. Supported modules: Leads, Accounts, Contacts, Deals, Campaigns, Tasks, Cases, Events, Calls, Solutions, Products, Vendors, Price_Books, Quotes, Sales_Orders, Purchase_Orders, Invoices, and custom modules. Unsupported modules (Visits, Users, LinkingModules) return NOT_ALLOWED.
  - `api_name` (string) [maxLen=255] — API name of the module (e.g., Leads, Contacts, Deals, Vendors).
  - `id` (string) [maxLen=20] — Unique module ID (19-digit format). Always use the full ID as returned by GET /settings/modules - truncated or shortened IDs return INVALID_DATA ('the tabId given seems to be invalid'). Optional in requests if api_name is provided; always present in responses.
`AutomationRelatedRecord`:
  > Represents a related module reference, conforming to the AutomationRelatedRecord schema, that identifies a child module whose records should also receive the new owner assignment during the conversion operation. At least one of api_name or id is required to identify the child module.
  - `api_name` (string) **REQ** [maxLen=255, enum=['Events', 'Calls', 'Tasks', 'Contacts', 'Deals']] — API name of the related module. Events, Calls, Tasks - open activity records, available for all modules and actions (assign_owner, convert). Contacts - available for assign_owner when parent is Accounts, and for convert when converting Leads. Deals - available for assign_owner when parent is Accounts or Contacts, and for convert when converting Leads (requires create_deal=true).
  - `id` (string) [maxLen=255] — Unique identifier of the related module. This is the module ID corresponding to the api_name.
`AutomationRemoveTagsDetails`:
  > Configuration for the remove_tags action. Referenced from AutomationNonAssociateActions.json. MANDATORY: id (state id), and id (action's id inside "details")  is mandatory for update.
  - `tags` (array of object `AutomationTagRef`) [minItems=1, maxItems=10] **REQ** — List of tags to remove from the record. All tags must pre-exist in the org  - fetch available tags from GET /settings/tags?module={module_api_name}. If the list is empty after parsing, the API returns FAILURE ('Empty Tag'). If the tag count exceeds the edition limit, the API returns FAILURE ('Invalid Tag Count').
  - `module` (object `AutomationModuleRef`) — Target module for the tag action. Must match the workflow rule's trigger module. Supported modules: Leads, Accounts, Contacts, Deals, Campaigns, Tasks, Cases, Events, Calls, Solutions, Products, Vendors, Price_Books, Quotes, Sales_Orders, Purchase_Orders, Invoices, and custom modules. Unsupported modules (Visits, Users, LinkingModules) return NOT_ALLOWED.
  - `over_write` (boolean) [default=False] — Present in GET responses. Its value is ignored for remove_tags actions.
  - `id` (string) [maxLen=20] — Server-generated unique identifier for this remove tags action. Present only in GET responses; not required in POST or PUT requests.
`AutomationScheduleCallDetails`:
  > Configuration for the schedule_call action. Referenced from AutomationNonAssociateActions.json. MANDATORY: id (state id) is mandatory for update.
  - `module` (object `AutomationModuleRef`) **REQ** — Target module for the call. Must be the Calls module. Provide either api_name ("Calls") or the Calls module id.
  - `layout` (object `AutomationLayoutRef`) **REQ** — Layout to use when creating the Call record. Determines which fields are available and their validation rules. Fetch valid layouts from GET /settings/layouts?module=Calls. The layout.id is required.
  - `field_mappings` (array of object `AutomationFieldMappings`) [minItems=1, maxItems=25] **REQ** — Field mappings for the new Call. Each entry: {"field": {"api_name": "Subject"}, "type": "static", "value": "Follow-up"}. Must include all mandatory fields from GET /settings/layouts?module=Calls. Call_Type is system-mandatory (values: "Outbound", "Inbound", "Missed") - omitting returns REQUIRED_DATA_NOT_FOUND. Common fields: Subject, Call_Type, Call_Purpose, Call_Start_Time, Remind_At. Mapping types: static - literal values for text, picklist fields; NOT for DateTime/ALARM (DEPENDENT_MISMATCH). merge_field - runtime tokens like ${!Leads.Phone} for text-based fields; NOT for lookup/owner (DEPENDENT_MISMATCH). execution_time - REQUIRED for Call_Start_Time and Remind_At; sign required for datetime; periods: days, business_days, hours, minutes.
  - `apply_restriction` (boolean) [default=False, nullable] — Whether to enforce assignment-threshold rules (record count limits per user) on the record owner when creating the Call record. When true, the system checks whether the owner has reached their record limit before creating the record. Only effective when the org has assignment thresholds configured.
  - `id` (string) [maxLen=20] — Server-generated unique identifier for this schedule call action. Present only in GET responses; not required in POST requests.
`AutomationTagRef`:
  > Represents a tag reference, conforming to the AutomationTagRef schema, that identifies a pre-existing org tag to be added to the record. Both id and name are mandatory fields on each entry; the referenced tag must already exist in the org before the action executes.
  - `id` (string) **REQ** [maxLen=20] — Unique identifier of the tag. Obtain from GET /settings/tags?module={module_api_name}. If provided alone, the tag is resolved by ID. If both id and name are provided, they must resolve to the same tag.
  - `name` (string) **REQ** [maxLen=25] — Name of the tag. Obtain from GET /settings/tags?module={module_api_name}. If provided alone, the tag is resolved by name. Must match an existing tag  - providing a non-existent name returns INVALID_DATA. Max 25 characters, cannot contain <, >, commas, or emojis.
  - `color_code` (string) [maxLen=25] — Hex color code of the tag (e.g., '#879BFC'). Optional in requests; present in GET responses. Allowed values: #F17574, #F48435, #E7A826, #A8C026, #63C57E, #1DB9B4, #57B1FD, #879BFC, #D297EE, #FD87BD, #969696, #658BA8, #B88562.
`BetweenFilterCriterionRequest`:
  > Represents a filter criterion for the between and not_between comparators. The value must be an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields. Resolve the data_type from the field's FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `field` (object) **REQ** — Represents the target field definition to which the range filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['between', 'not_between']] — Represents the range comparison operator applied to the criterion, indicating whether the field value falls within or outside the specified bounds.
Possible values:
between - Matches records where the field value falls within the specified range.
not_between - Matches records where the field value falls outside the specified range.
  - `value` (array of object) [minItems=2, maxItems=2] **REQ** — Contains the two boundary values — [lower_bound, upper_bound] — against which the field is evaluated for the between or not_between comparator.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`CompositeFieldMapping`:
  > Represents a composite-type field mapping used exclusively for the Participants field in the Events module via the add_meeting action. The value carries a structured object that encodes participant data and is not applicable to any other field or automation action type.
  - `display_value` (string) [maxLen=500] — The server-computed representation of the mapped value, included in GET responses. Omitted from create and update requests.
  - `field` (object `AutomationFieldAttributes`) **REQ** — Target field to populate when the automation executes. api_name is required. If id is also provided, both must refer to the same field; otherwise the API returns AMBIGUITY_DURING_PROCESSING.
  - `type` (string) **REQ** [const=composite] — Serves as the polymorphic discriminator that identifies this field mapping as a composite mapping; the value must be set to "composite" to select this schema variant.
  - `value` (object) **REQ** — Holds the structured composite object that encodes participant data for the Events module Participants field; the shape of this object varies according to the participant type configuration defined for the automation rule.
`DecisionCreateDetails`:
  > Represents the details configuration object for a kiosk decision state. Contains the path definitions, filter conditions, and criteria groupings that determine the branching logic.
  - `path_details` (array of object `DecisionPathDetails`) [minItems=1, maxItems=10] **REQ** — Represents the list of decision paths the kiosk can follow. Each path includes filter conditions that are evaluated to determine the routing; the default fallback path may have null filter conditions.
    schema: `DecisionPathDetails`
`DecisionCriteriaGrouping`:
  > Represents a single condition grouping evaluated as part of a kiosk decision state. Defines the data source type, evaluation value, and optional criteria details for one logical condition.
  - `sequence_number` (integer/int32) **REQ** [nullable] — The source for the criteria evaluation .

Possible values:

current_record - Criteria evaluated against the current record.

get_record - Criteria evaluated based on whether the Get Records response contains data or not.

kiosk_fields - Criteria evaluated against the screen fields or action fields from Kiosk.

loop_record - Evaluates a field from a loop record.

  - `type` (string) **REQ** [enum=[6 values]] — Represents the data source used for condition evaluation. Possible values:current_record - Evaluates a field from the current CRM record. Possible values: get_record - Evaluates a field from a get_record result. kiosk_fields - Evaluates a kiosk screen field. data_hub - Evaluates a data hub field. created_record - Evaluates a field from a record created earlier in the kiosk. loop_record - Evaluates a field from a loop record.
  - `resource` (object `DecisionResource`) — The resource object identifies the specific data resource that should be used when evaluating the condition. This object is primarily used when the condition type refers to external data sources such as records retrieved using a GetRecord configuration or records created earlier in the kiosk execution. The resource object ensures that the decision condition references the correct record source.
  - `value` (string) **REQ** [enum=['${EMPTY}', '${NOTEMPTY}']] — Indicates whether the evaluated field must contain data.
Possible values:
${NOTEMPTY} - The field must have a value.
${EMPTY} - The field must be empty.

  - `criteria` (object `FilterCriterionRequest`) — The actual comparison logic for this criteria grouping. Supports both simple field-value comparisons (via SimpleFilterCriterionRequest) and nested grouped conditions (via GroupedFilterCriterionRequest). Defined in Criterion.json. Note: The only possible types for the 'value' will be 'value' and 'field' (If you want to compare with any field in the Kiosk itself, you should send the type as 'field' and the format will be <kiosk_api_name>.<screen_field_api_name> in case referring to Kiosk's screen field. Example: 'criteria': {'field': { 'api_name': 'Screen_2_Single_Line_2', 'id': '2296900000013105115', 'field_label': 'Single Line 2', 'data_type': 'text'}, 'comparator': 'equal', 'value': { 'api_name': 'Bug2.Screen_2_Single_Line_2', 'id': '2296900000013105115' },'type': 'field' }. If the type is just 'value', then a simple string is used for comparison. Strictly follow this pattern for Kiosk's criteria overriding any discrepancies in Criterion.json.
`DecisionFilterConditions`:
  > Represents the filter conditions that determine whether a decision path is taken. Contains a logical pattern and a list of criteria groupings that must be evaluated.
  - `pattern` (string) [maxLen=100, minLen=1, nullable] — Represents the logical expression that combines multiple criteria groupings. Each number references a criteria grouping's sequence number, and logical operators such as **and** and **or** determine how conditions are combined. For example, (1and2) requires both grouping 1 and grouping 2 to be satisfied.
  - `criteria_groupings` (array of object `DecisionCriteriaGrouping`) [maxItems=5, nullable] — Represents the list of conditions evaluated as part of the decision state. Each grouping defines one logical condition, and its position is referenced by the pattern field.
`DecisionPathDetails`:
  > Represents the constraint block that requires filter_conditions to be a valid object for all non-default decision paths.
`DecisionResource`:
  > The resource object identifies the specific data resource that should be used when evaluating the condition. This object is primarily used when the condition type refers to external data sources such as records retrieved using a GetRecord configuration or records created earlier in the kiosk execution. The resource object ensures that the decision condition references the correct record source.
  - `name` (string) [maxLen=20, minLen=1, nullable] — Represents the display name of the referenced resource used in the decision condition.
  - `id` (string) [maxLen=19, minLen=1, nullable] — Represents the unique identifier of the resource — a get_record or created-record configuration — used when evaluating the decision condition.
`EqualFilterCriterionRequest`:
  > Represents a filter criterion for the equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders. Accepts scalar or array values. Resolve the data_type from the field's FieldSchema.
  - `field` (object) **REQ** — Represents the target field definition to which the equal filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['equal']] — Represents the equal comparison operator applied to the criterion.
Possible values:
equal - Matches records where the field value equals the specified filter value.
  - `value` (object) **REQ** — Represents the filter value used in the equal comparator. Accepts a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueGeneralPredefined` (string) [enum=['${EMPTY}', '${NOTEMPTY}']] — Represents a predefined placeholder value applicable to any field data_type with the equal comparator.
Possible values:
${EMPTY} - Matches records where the field has no value.
${NOTEMPTY} - Matches records where the field has any non-empty value.
      - `SimpleFilterCriterionValueDateTimePredefined` (string) [enum=[22 values]] — Represents a predefined placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator.
      - `SimpleFilterCriterionValueNDaysPredefined` (string) [maxLen=255, pattern=^\$\{(LAST_N_|NEXT_N_)(DAYS|WEEKS|MONTHS|YEARS):([0-9]+)\}$] — Represents a predefined N-period range placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator. Follows the pattern ${NEXT_N_<PERIOD>:<n>} or ${LAST_N_<PERIOD>:<n>}, where PERIOD is DAYS, WEEKS, MONTHS, or YEARS and n is a positive integer. The current period is always excluded from the range.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`EqualityFilterCriterionRequest`:
  oneOf:
    - `EqualFilterCriterionRequest` — Represents a filter criterion for the equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders. Accepts scalar or array values. Resolve the data_type from the field's FieldSchema.
    - `NotEqualFilterCriterionRequest` — Represents a filter criterion for the not_equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
`ExecutionTimeFieldMapping`:
  > Represents an execution_time-type field mapping that computes a date, datetime, or ALARM value at runtime by applying a signed offset to a trigger field or the current time. The value carries an ExecutionTimeValue object specifying the period, unit, trigger_field, and optional time or notify_type properties. A plus sign places the result after the trigger; a minus sign places it before. ALARM fields always require minus. Workflow task actions support only days and business_days as period values.
  - `display_value` (string) [maxLen=500] — The server-computed representation of the mapped value, included in GET responses. Omitted from create and update requests.
  - `field` (object `AutomationFieldAttributes`) **REQ** — Target field to populate when the automation executes. api_name is required. If id is also provided, both must refer to the same field; otherwise the API returns AMBIGUITY_DURING_PROCESSING.
  - `type` (string) **REQ** [const=execution_time] — Identifies the mapping variant as an execution-time offset. The value is always "execution_time" for this schema and acts as the polymorphic discriminator across the AutomationFieldMappings union.
  - `value` (object `ExecutionTimeValue`) **REQ** — Execution-time object specifying how to compute the date/datetime offset from a reference field.
`ExecutionTimeValue`:
  > Execution-time object specifying how to compute the date/datetime offset from a reference field.
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
`FilterCriterionRequest`:
  oneOf:
    - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
    - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
`FilterFieldBase`:
  > Represents the base field reference used in filter operations, containing minimal required properties. The field's data_type is not part of this object; resolve it from the corresponding FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `id` (string/int64) — Represents the unique ID of the field used for filter operations.
  - `api_name` (string) **REQ** — Represents the API name of the field used for filter application. Supports relationship notation, for example, Deals__r.Stage.
  additionalProperties: any
`GetRecordUpdateDetails`:
  > Represents the details configuration object for updating a kiosk get_records state. Contains the reference to the get_record component that defines which records to retrieve.
  - `get_record` (object) — Represents the reference to the get_record configuration that defines which records to retrieve.
    - `id` (string) [maxLen=255, nullable] — Represents the unique identifier of the get_record configuration.
    - `name` (string) [maxLen=255, nullable] — Represents the display name of the get_record configuration.
`GroupedFilterCriterionRequest`:
  > Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group` (array of object) [minItems=2, maxItems=25] **REQ** — Contains an array of filter conditions grouped together and evaluated with the specified logical operator.
    oneOf:
      - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
      - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group_operator` (string) **REQ** [enum=['AND', 'OR', 'and', 'or']] — Represents the logical operator applied between the filter conditions in the group.
Possible values:
AND - All conditions in the group must be satisfied.
OR - At least one condition in the group must be satisfied.
and - Equivalent to AND; all conditions in the group must be satisfied.
or - Equivalent to OR; at least one condition in the group must be satisfied.
`KioskStateErrorResponse`:
  > Represents the generic error response for kiosk state operations. Contains an error code, error message, and contextual details about the validation failure.
  - `code` (string) **REQ** [enum=[8 values]] — Represents the error category code indicating the type of validation failure.
  - `details` (object) **REQ** — Represents contextual details about the error. The structure varies by error type and may include the affected field path, expected data type, or resource path.
    - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the error.
    - `json_path` (string) [maxLen=1000] — Represents the JSON path pointing to the problematic field in the request body.
    - `expected_data_type` (string) [maxLen=255] — Represents the expected data type when a type mismatch occurs in the request.
    - `maximum_length` (integer/int32) — Represents the maximum allowed length when a field value exceeds the configured limit.
    - `resource_path_index` (integer/int32) — Represents the index in the resource path that is invalid.
    - `permissions` (array of string) [maxItems=100] — Represents the list of required OAuth scopes when access is denied.
      items: [maxLen=255]
    additionalProperties: any
  - `message` (string) **REQ** [maxLen=500] — Represents the error message describing what went wrong.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always 'error' for error responses.
`MergeFieldMapping`:
  > Represents a merge_field-type mapping whose value is resolved at execution time by substituting token references with live field data. Supports direct field tokens (${!Module.Field}), traversal tokens (${!Module.Lookup.Field}), and system tokens (${CURRENTTIME}, ${CURRENTUSER}). Applies to text-based fields such as Subject, Description, and custom text fields. Targeting owner or lookup fields with this type produces a DEPENDENT_MISMATCH error; those fields require a static mapping using an object with a numeric identifier and an optional name. Multiple tokens may be chained with surrounding text for multi-line fields, while single-value fields such as email or URL accept exactly one token.
  - `display_value` (string) [maxLen=500] — The server-computed representation of the mapped value, included in GET responses. Omitted from create and update requests.
  - `field` (object `AutomationFieldAttributes`) **REQ** — Target field to populate when the automation executes. api_name is required. If id is also provided, both must refer to the same field; otherwise the API returns AMBIGUITY_DURING_PROCESSING.
  - `type` (string) **REQ** [const=merge_field] — Identifies the mapping strategy for this field assignment. The value must be `merge_field`, which instructs the automation engine to resolve the field value dynamically from a merge field token at execution time rather than from a static literal.
  - `value` (string) **REQ** [maxLen=1000] — A string containing one or more ${!...} merge-field tokens resolved at runtime.
  - `allow_agent_user` (boolean) [default=False] — Controls whether agent users are eligible for record assignment. Possible values:
**true** — agent users are included in the assignment pool alongside standard users.
**false** — agent users are excluded from assignment.
Applies to mapping types role, group, profile, merge_field, and criteria. Does not apply to user or assignment_rule types.
`MultiSelectLookupFilterCriterionRequest`:
  > Represents a filter criterion for the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup. The value must be an array of SimpleFilterCriterionValueObjectRequest lookup objects.
  - `field` (object) **REQ** — Represents the target field definition to which the multi-select lookup filter criterion is applied. The field must have a data_type of multiuserlookup or multiselectlookup.
  - `comparator` (string) **REQ** [enum=['include_all', 'include_any', 'exclude_all', 'exclude_any']] — Represents the multi-select lookup comparison operator applied to the criterion. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
Possible values:
include_all - Matches records that include all specified lookup values.
include_any - Matches records that include at least one of the specified lookup values.
exclude_all - Matches records that exclude all specified lookup values.
exclude_any - Matches records that exclude at least one of the specified lookup values.
  - `value` (array of object `SimpleFilterCriterionValueObjectRequest`) [minItems=1, maxItems=5] **REQ** — Contains an array of lookup object references used in the multi-select comparison.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`NotEqualFilterCriterionRequest`:
  > Represents a filter criterion for the not_equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
  - `field` (object) **REQ** — Represents the target field definition to which the not-equal filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['not_equal']] — Represents the not-equal comparison operator applied to the criterion.
Possible values:
not_equal - Matches records where the field value does not equal the specified filter value.
  - `value` (object) **REQ** — Represents the filter value used in the not_equal comparator. Accepts a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`OrderingFilterCriterionRequest`:
  > Represents a filter criterion for the less_than, less_equal, greater_than, and greater_equal comparators. The value must be a scalar; arrays and objects are not supported. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
  - `field` (object) **REQ** — Represents the target field definition to which the ordering filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['less_than', 'less_equal', 'greater_than', 'greater_equal']] — Represents the ordering comparison operator applied to the criterion.
Possible values:
less_than - Matches records where the field value is less than the specified filter value.
less_equal - Matches records where the field value is less than or equal to the specified filter value.
greater_than - Matches records where the field value is greater than the specified filter value.
greater_equal - Matches records where the field value is greater than or equal to the specified filter value.
  - `value` (object) **REQ** — Represents the scalar filter value used in the ordering comparator. Arrays and objects are not supported for ordering comparators.
    anyOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`ScreenButton`:
  > Represents a screen button that triggers a transition to another state. Each button has a display name and a style type.
  - `prop_name` (string) **REQ** [enum=['outlineprimary', 'primary', 'default', 'failure', 'outlineredlight']] — Represents the style type of the button.
Possible values:
primary - Displays the button as the primary action on the screen, typically used for actions such as Next, Submit, or Save.

default - Displays the button with the standard appearance, suitable for secondary actions.

outlineprimary - Displays the button with a primary-colored outline, emphasizing the action without making it the primary button.

failure - Displays the button with a solid error-themed style, typically used for destructive or critical actions such as Delete or Reject.

outlineredlight - Displays the button with a red outline, typically used for secondary destructive actions such as Cancel, Discard, or Remove.

  - `name` (string) **REQ** [maxLen=255] — Specify the display label of the button shown to the user.
`ScreenConfigurationUpdate`:
  > Configuration object defining the UI screen that will be rendered to the kiosk user. This object contains all information required to dynamically construct the screen interface including: input elements, interactive components, layout configuration, action buttons, screen metadata

The kiosk runtime uses this configuration to generate the UI dynamically without requiring frontend code changes. Elements key is mandatory for a screen_details JSON while creating screen state.
  - `width` (string) [maxLen=50, pattern=^(670px|1000px)$, nullable] — Represents the visual width of the screen container.
Possible values:
670px - Standard width layout.
1000px - Wide layout.
If provided, must be one of: 670px, 1000px.
  - `buttons` (array of object `ScreenButton`) [maxItems=1, nullable] — Represents the list of action buttons on the screen. Each button triggers a transition to another state. When provided, each button must include a prop_name and name.
  - `title` (string) [maxLen=255, nullable] — Represents the display title shown at the top of the kiosk screen, providing contextual information about the screen's purpose.
  - `button_align` (string) [enum=['right_to_left', 'left_to_right', 'center'], nullable] — Represents the alignment direction of action buttons within the screen footer.\nPossible values:\nleft_to_right - Buttons appear in natural reading order.\nright_to_left - Buttons appear aligned from right.
  - `elements` (array of object `ScreenElementUpdate`) [maxItems=30, nullable] — Represents the list of UI components rendered on the screen, ordered from top to bottom. Supported element types include field, screen_field, text, get_records, zia_insights, and data_hubs.
    schema: `ScreenElementUpdate`
`ScreenCurrency`:
  > Represents the conditional schema constraint that requires the precision field when the rounding_option is round_off.
`ScreenDataHub`:
  > Represents an integration with a data hub query or lookup system.

This allows the screen to fetch and display data from external sources.
  - `ui_type` (integer/int32) [nullable] — Represents the numeric identifier of the UI widget type used to render the data hub component.
  - `read_only` (boolean) [nullable] — Indicates whether the data hub component is read-only.
Possible values:
true - The component is displayed but cannot be edited.
false - The user can interact with the component.

  - `api_name` (string) [maxLen=255, nullable] — Represents the unique API name of the data hub component to be associated with the screen.
  - `field_label` (string) [maxLen=255, nullable] — Represents the display label shown on the screen for the data hub component during execution and preview.
  - `data_type` (string) [maxLen=255, nullable] — Represents the data type of the data hub component.
  - `id` (string) [maxLen=19, nullable] — Represents the unique identifier of the data hub component to be associated with the screen.
  - `required` (boolean) [nullable] — Indicates whether the data hub component is mandatory during kiosk execution.
Possible values:
true - A value must be provided.
false - The component may be skipped.

`ScreenElementUpdate`:
  > Represents the conditional schema constraint that requires the field object when the element type is field.
`ScreenFieldUpdate`:
  > Represents the conditional schema constraint that requires the decimal_place field when the data type is double.
`ScreenGetRecordRef`:
  > Reference to a record retrieval operation called a get_record.

This component fetches records from the CRM system and displays them within the screen. The records are fetched by using user-specified criteria. This should be given if a get_record component created anywhere else in the Kiosk is to be associated in the current screen.
  - `name` (string) [maxLen=255, nullable] — Represents the display name of the get_record component to be associated with the screen.
  - `id` (string) [maxLen=19, nullable] — Represents the unique identifier of the get_record component to be associated with the screen.
`ScreenGlobalPicklist`:
  > Reference to a globally defined picklist.
  - `api_name` (string) [maxLen=255, nullable] — Represents the API name of the shared global picklist.
  - `id` (string) [maxLen=19, nullable] — Represents the unique identifier of the global picklist resource.
`ScreenParentRecordField`:
  > Defines the record used as input for generating the AI insight. (Required)
  - `api_name` (string) [maxLen=250, nullable] — Represents the API name of the record used as input for generating the Zia AI insight.
  - `id` (string) [maxLen=19, nullable] — Represents the unique identifier of the record used as input for generating the Zia AI insight.
`ScreenPickListValue`:
  > Represents a single selectable option in a picklist field. Contains the display value shown to the user and the actual value stored internally.
  - `display_value` (string) [maxLen=255, nullable] — Represents the text displayed to the user for this picklist option.
  - `actual_value` (string) [maxLen=255, nullable] — Represents the value stored internally when this picklist option is selected.
`ScreenSelectedField`:
  > Represents a field selected from a get_record component to retrieve and display on the screen. Contains the field's API name and unique identifier.
  - `api_name` (string) [maxLen=250, nullable] — Represents the API name of the field selected from the record to display on the screen.
  - `id` (string) [maxLen=19, nullable] — Represents the unique identifier of the field selected from the record to display on the screen.
`ScreenTooltipUpdate`:
  > Defines additional help information associated with the field.

Tooltips provide contextual guidance to users explaining what data should be entered.


  - `name` (string) [enum=['info_icon', 'static_text'], nullable] — Represents the type of tooltip presentation for the field. Possible values:
info_icon - Displays an information icon next to the field.
static_text - Displays informational text next to the field.
  - `value` (string) [maxLen=500, nullable] — Represents the text displayed inside the tooltip for the field.
`ScreenUpdateDetails`:
  > Represents the details configuration object for updating a kiosk screen state. Contains the screen_details object with the UI elements, buttons, and layout properties to be updated.
  - `screen_details` (object `ScreenConfigurationUpdate`) — Configuration object defining the UI screen that will be rendered to the kiosk user. This object contains all information required to dynamically construct the screen interface including: input elements, interactive components, layout configuration, action buttons, screen metadata

The kiosk runtime uses this configuration to generate the UI dynamically without requiring frontend code changes. Elements key is mandatory for a screen_details JSON while creating screen state.
`ScreenZiaInsight`:
  > Represents an AI-powered insight component.

This widget can display predictions, recommendations, or analytics generated by the Zia AI engine.
  - `parent_record_field` (object `ScreenParentRecordField`) **REQ** — Defines the record used as input for generating the AI insight. (Required)
  - `read_only` (boolean) [nullable] — Indicates whether the Zia insight component is read-only.
Possible values:
true - The component is displayed but cannot be edited.
false - The user can interact with the component.

  - `api_name` (string) [maxLen=255, nullable] — Represents the unique API name of the Zia insight component to be associated with the screen.
  - `field_label` (string) [maxLen=255, nullable] — Represents the display label shown on the screen for the Zia insight component during execution and preview.
  - `component_name` (string) **REQ** [enum=[9 values]] — Represents the specific type of Zia AI insight component, such as prediction or recommendation.
  - `required` (boolean) [nullable] — Indicates whether the Zia insight component is mandatory during kiosk execution.\nPossible values:\ntrue - A value must be provided.\nfalse - The component may be skipped.
`SetFilterCriterionRequest`:
  > Represents a filter criterion for the in and not_in comparators. The value must be an array of primitive values. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text-based types, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
  - `field` (object) **REQ** — Represents the target field definition to which the set filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['in', 'not_in']] — Represents the set membership comparison operator applied to the criterion.
Possible values:
in - Matches records where the field value is in the specified set of values.
not_in - Matches records where the field value is not in the specified set of values.
  - `value` (array of object) [minItems=1, maxItems=500] **REQ** — Contains an array of primitive filter values used in the set comparison.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`SimpleFilterCriterionRequest`:
  oneOf:
    - `EqualityFilterCriterionRequest` — Represents an equality filter criterion that dispatches to either the EqualFilterCriterionRequest or NotEqualFilterCriterionRequest schema based on the comparator value.
    - `TextFilterCriterionRequest` — Represents a filter criterion for the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value must be a string scalar or array; use SimpleFilterCriterionValueString for text-based field types. Object and Boolean values are not supported. Resolve the data_type from the field's FieldSchema.
    - `OrderingFilterCriterionRequest` — Represents a filter criterion for the less_than, less_equal, greater_than, and greater_equal comparators. The value must be a scalar; arrays and objects are not supported. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
    - `BetweenFilterCriterionRequest` — Represents a filter criterion for the between and not_between comparators. The value must be an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields. Resolve the data_type from the field's FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
    - `SetFilterCriterionRequest` — Represents a filter criterion for the in and not_in comparators. The value must be an array of primitive values. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text-based types, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
    - `MultiSelectLookupFilterCriterionRequest` — Represents a filter criterion for the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup. The value must be an array of SimpleFilterCriterionValueObjectRequest lookup objects.
`SimpleFilterCriterionValueObjectBase`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (string/int64) — Represents the unique ID of the lookup module record.
  - `name` (string) [maxLen=255] — Represents the display name of the lookup module record.
  additionalProperties: any
`SimpleFilterCriterionValueObjectPredefined`:
  oneOf:
      - `name` (string) **REQ** [enum=['${CURRENTUSER}']] — Represents the predefined placeholder for the currently logged-in user.
Possible values:
${CURRENTUSER} - Represents the currently logged-in user.
      - `id` (string) **REQ** [enum=['${CURRENTUSERROLE}']] — Represents the predefined placeholder for the logged-in user's role record ID.
Possible values:
${CURRENTUSERROLE} - Represents the role of the currently logged-in user.
      - `name` (string) [maxLen=255] — Represents an optional display label for the predefined role, such as Logged in User Role.
      additionalProperties: any
`SimpleFilterCriterionValueObjectRequest`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (object) **REQ**
  - `name` (string) [maxLen=255] — Represents the display name of the lookup module record.
  additionalProperties: any
`StaticFieldMapping`:
  > Represents a static-type mapping that assigns a literal value directly to the target field at execution time. The value shape varies by field data type: a plain string for text, picklist, phone, email, URL, number, decimal, currency, and percentage fields (numeric values expressed as strings); an array of strings for multiselectpicklist fields; and an object containing ID and name for ownerlookup fields. Date, datetime, and ALARM fields do not support this type — use execution_time instead, as static on those fields produces a DEPENDENT_MISMATCH error. Fields marked unique in the module settings also require merge_field rather than static for create_record actions.
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
`StaticObjectValue`:
  > Represents an object value used as the static value for ownerlookup and layout fields, containing an ID that identifies the target user or layout and an optional name that the server resolves from the ID when not supplied. Typically used to assign record ownership by providing the user ID.
  - `id` (string) **REQ** [maxLen=255] — The system identifier of the referenced entity, such as a user or layout record. This value drives entity resolution by the automation engine and must be provided when the target field references an entity.
  - `name` (string) [maxLen=255] — The display name of the referenced entity, such as a user full name or a layout label. When omitted from a request payload, the server resolves and populates this property from the supplied ID. The property is present in all GET responses.
  additionalProperties: any
`TextFilterCriterionRequest`:
  > Represents a filter criterion for the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value must be a string scalar or array; use SimpleFilterCriterionValueString for text-based field types. Object and Boolean values are not supported. Resolve the data_type from the field's FieldSchema.
  - `field` (object) **REQ** — Represents the target field definition to which the text filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['like', 'not_like', 'starts_with', 'ends_with', 'contains', 'not_contains']] — Represents the text comparison operator applied to the criterion.
Possible values:
like - Matches records where the field value contains the specified pattern.
not_like - Matches records where the field value does not contain the specified pattern.
starts_with - Matches records where the field value begins with the specified string.
ends_with - Matches records where the field value ends with the specified string.
contains - Matches records where the field value contains the specified string.
not_contains - Matches records where the field value does not contain the specified string.
  - `value` (object) **REQ** — Represents the string filter value used in the text comparator. Accepts a scalar string or an array of string values.
    oneOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.

**Request Body** (required) — application/json `UpdateStateRequest`
> The request body must contain a states array with one object.
  > Represents the request body for updating a kiosk state. The states array contains exactly one state object, with the state ID as the only required field.
  - `states` (array of object `UpdateStatePayload`) [minItems=1, maxItems=1] **REQ** — Represents the array containing exactly one state object to update.
    schema: `UpdateStatePayload`

**Responses:**

- **200**: State updated successfully. — Schema: `UpdateStateResponse` [application/json]
    > Represents the success response returned after a kiosk state update.
    schema: `UpdateStateResponse`
    - `states` (array of object `StateOperationResult`) [maxItems=1] — Represents the array of operation result objects for the updated kiosk states.
      schema: `StateOperationResult`
      - `code` (string) [maxLen=255] — Represents the result code for the operation on this state.
      - `details` (object `StateOperationResultDetails`) — Represents the details of a state operation result. Contains the unique identifier and resource identifier of the created or updated kiosk state.
        schema: `StateOperationResultDetails`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the kiosk state created or updated.
        - `rid` (string/uuid) [maxLen=255] — Represents the resource identifier of the kiosk state.
      - `message` (string) [maxLen=255] — Represents the result message for the operation on this state.
      - `status` (string) [maxLen=255] — Represents the result status for the operation on this state.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad request. Validation failed for the state update. [application/json]
    > Represents the 400 error response for the updateKioskState operation. Contains either a generic error response with a code, message, and details, or a batch validation response with a states array of per-state error objects.
    oneOf:
      - `KioskStateErrorResponse` — Represents the generic error response for kiosk state operations. Contains an error code, error message, and contextual details about the validation failure.
        - `states` (array of object) [maxItems=25] **REQ** — List of individual state validation errors.
          oneOf:
            - `KioskStateErrorResponse` — Represents the generic error response for kiosk state operations. Contains an error code, error message, and contextual details about the validation failure.
            - `KioskStateErrorInvalidGetRecordReference` — Represents the error response returned when the provided get_record component ID is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating the type of validation failure. Always 'INVALID_DATA' when the get_record component ID is invalid.
              - `details` (object) **REQ** — Represents contextual details about the error, including the API name and JSON path of the affected field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path pointing to the problematic field in the request body.
              - `message` (string) **REQ** [enum=['invalid GetRecord id']] — Represents the error message describing the invalid get_record reference.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always 'error' for error responses.
            - `KioskStateErrorAssociationNotAllowed` — Represents the error response returned when the get_record component is already associated with another kiosk state.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code indicating the type of validation failure. Always 'NOT_ALLOWED' when the get_record component is already associated with another state.
              - `details` (object) **REQ** — Represents contextual details about the error, including the API name and JSON path of the affected field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path pointing to the problematic field in the request body.
              - `message` (string) **REQ** [enum=['GetRecord already associated with other component']] — Represents the error message describing the association conflict.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always 'error' for error responses.
            - `KioskStateErrorMandatoryFieldMissing` — Represents the error response returned when the get_record key is present in the request but required details are missing.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code indicating the type of validation failure. Always 'MANDATORY_NOT_FOUND' when required fields are missing.
              - `details` (object) **REQ** — Represents contextual details about the error, including the API name and JSON path of the missing mandatory field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the mandatory field that is missing from the request.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path pointing to the missing mandatory field in the request body.
              - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message describing the missing mandatory field.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Always 'error' for error responses.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.UPDATE

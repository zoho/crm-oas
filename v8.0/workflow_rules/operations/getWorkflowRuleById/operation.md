# GET /settings/automation/workflow_rules/{id}
**Operation:** `getWorkflowRuleById` — Retrieve Workflow Rule by ID

> To retrieve the complete configuration of a specific workflow rule in your Zoho CRM organization, including its trigger type, execution criteria, conditions, instant actions, scheduled actions, and lock status. Use the [Get All Workflow Rules](workflow_rules.yaml#$.paths./settings/automation/workflow_rules.get) operation to obtain the unique ID of the workflow rule to retrieve.


**Parameters:**
- `id` (path, string/string, required): Represents the unique 19-digit numeric ID of the workflow rule. Obtain valid IDs from the List Workflow Rules endpoint.

**Schemas:**
`AddMeetingActionSchema`:
  > Represents a non-associate action that schedules a meeting when the workflow rule condition is triggered.
  - `name` (string) [maxLen=100] — Represents the display name of the add-meeting action as it appears within the workflow rule configuration.
  - `type` (string) **REQ** [const=add_meeting] — Represents the action type discriminator that identifies this action as an add-meeting action within the workflow rule. The value is fixed for this action type and must correspond to a type supported by the target module and trigger event.
  - `details` (object `AutomationAddMeetingDetails`) **REQ** — Configuration for the add_meeting action. Requires the Events module, a layout, and field mappings that include the event title and start date and time. Also requires the meeting duration, unless the event is set to all day, and specifies whether the record owner or another assigned user hosts the meeting. Optionally restricts creation to prevent duplicate records.

  - `related_details` (object `RelatedDetailsNestedSchema`) — Optional. For add_meeting, related_details is not typically used. Applicable sub-fields: best_time (for email_notifications only), followup_details (for tasks only), lookup_field (for field_updates only).
  - `id` (string) [maxLen=20] — Represents the unique ID of the add-meeting action within the workflow rule.
  - `_delete` (null) — Indicates that this add-meeting action should be removed from the workflow rule when set in a PUT request. When this field is provided with a null value, the platform interprets it as a deletion signal and removes the action from the rules action list.
`AddTagsActionSchema`:
  > Represents a non-associate action that adds pre-existing tags to the triggering record when the workflow rule condition is met.
  - `name` (string) [maxLen=100] — Represents the display name of the add-tags action as it appears within the workflow rule configuration.
  - `type` (string) **REQ** [const=add_tags] — Represents the action type discriminator that identifies this action as an add-tags action within the workflow rule. The value is fixed for this action type and must correspond to a type supported by the target module and trigger event.
  - `details` (object `AutomationAddTagsDetails`) **REQ** — PURPOSE: Details object for add_tags action. Adds pre-existing tags to the triggering record. PREREQUISITES: Tags must exist - GET /settings/tags?module={api_name} to list, POST to create first. MANDATORY: tags (array 1-10, each {id, name}). OPTIONAL: over_write (bool, default false - true replaces ALL existing tags), module ({api_name, id}). CONSTRAINTS: Not allowed with convert on Leads (AMBIGUITY_DURING_PROCESSING). over_write=true + remove_tags in same rule = INVALID_DATA. Unsupported: Visits, Users, LinkingModules (NOT_ALLOWED).
  - `related_details` (object `RelatedDetailsNestedSchema`) — Optional. For add_tags, related_details is not typically used. Applicable sub-fields: best_time (for email_notifications only), followup_details (for tasks only), lookup_field (for field_updates only).
  - `id` (string) [maxLen=20] — Represents the unique ID of the add-tags action within the workflow rule.
  - `_delete` (null) — Indicates that this add-tags action should be removed from the workflow rule when set in a PUT request. When this field is provided with a null value, the platform interprets it as a deletion signal and removes the action from the rules action list.
`AssignOwnerActionSchema`:
  > Represents a non-associate action that assigns or reassigns the record owner when the workflow rule condition is triggered.
  - `name` (string) [maxLen=100] — Represents the display name of the AssignOwner action as it appears within the workflow rule configuration.
  - `type` (string) **REQ** [const=assign_owner] — Represents the action type discriminator that identifies this as a AssignOwner action within the workflow rule. The value is fixed for this action type and must be supported by the target module and trigger event.
  - `details` (object `AutomationAssignOwnerDetails`) **REQ** — Configuration for the assign_owner action. Requires a module reference and an assign_to array with one to five entries, each specifying who to assign the record to — a user, role, group, assignment rule, or profile, a merge field, or matching criteria. Optionally sends a notification, includes related records, applies an assignment threshold, or bases assignment on user availability.
  - `related_details` (object `RelatedDetailsNestedSchema`) — Optional. For assign_owner, related_details is not typically used. Applicable sub-fields: best_time (for email_notifications only), followup_details (for tasks only), lookup_field (for field_updates only).
  - `id` (string) [maxLen=20] — Represents the unique ID of the AssignOwner action within the workflow rule.
  - `_delete` (null) — Indicates that this action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
`AssociateActionsNestedSchema`:
  discriminator: `type`
  oneOf:
    - `EmailNotificationAssociateActionSchema` — Represents an associate action that sends a pre-configured email notification when the workflow rule condition is triggered.
    - `FieldUpdateAssociateActionSchema` — Represents an associate action that updates field values using a pre-configured field update action when the workflow rule condition is triggered.
    - `TaskAssociateActionSchema` — Represents an associate action that creates a task based on a pre-configured task template when the workflow rule condition is triggered.
    - `SimpleAssociateActionSchema` — Represents an associate action that references a pre-configured action entity by its unique ID, applicable to action types such as webhooks, functions, and notifications.
`AutomationAddMeetingDetails`:
  > Configuration for the add_meeting action. Requires the Events module, a layout, and field mappings that include the event title and start date and time. Also requires the meeting duration, unless the event is set to all day, and specifies whether the record owner or another assigned user hosts the meeting. Optionally restricts creation to prevent duplicate records.

  - `module` (object `AutomationModuleRef`) **REQ** — Target module for the meeting. Must be the Events module. Provide either api_name ("Events") or the Events module id.
  - `layout` (object `AutomationLayoutRef`) **REQ** — Layout to use when creating the Event record. Determines which fields are available and their validation rules. Fetch valid layouts from GET /settings/layouts?module=Events. The layout.id is required.
  - `field_mappings` (array of object `AutomationFieldMappings`) [minItems=1, maxItems=25] **REQ** — Field mappings for the new Event. Each entry: {"field": {"api_name": "Event_Title"}, "type": "static", "value": "Meeting"}. Must include all mandatory fields from GET /settings/layouts?module=Events. Common fields: Event_Title, Start_DateTime, All_Day, Participants (composite type), Remind_At. End_DateTime is auto-computed from Start_DateTime + meeting_duration - do NOT provide it. Mapping types: static - literal values for text, picklist fields; NOT for DateTime/ALARM (DEPENDENT_MISMATCH). merge_field - runtime tokens like ${!Leads.Company} for text-based fields; NOT for lookup/owner (DEPENDENT_MISMATCH). execution_time - REQUIRED for Start_DateTime and Remind_At; sign required for datetime; periods: days, business_days, hours, minutes. When All_Day=true, period must be "days" and omit meeting_duration.
  - `meeting_duration` (object `AutomationMeetingDuration`) **REQ** — Duration of the meeting. Specifies a numeric value and time period (e.g., 1 hour, 30 minutes). Required when All_Day is not set to true in field_mappings. If All_Day is true, meeting_duration must not be provided  - the API returns INVALID_DATA with field1/field2 conflict details.
  - `host_unavailable` (object `AutomationHostUnavailable`) — Fallback behavior when the designated meeting host is unavailable. Either assign the record owner as host (assign_record_owner_as_host=true) or create a follow-up task (assign_task with a pre-configured task ID). Exactly one option must be specified; providing both returns INVALID_DATA with field1/field2 conflict, providing neither returns EXPECTED_FIELD_MISSING.
  - `apply_restriction` (boolean) [default=False, nullable] — Whether to enforce assignment-threshold rules (record count limits per user) on the record owner when creating the Event record. When true, the system checks whether the owner has reached their record limit before creating the record. Only effective when the org has assignment thresholds configured.
  - `id` (string) [maxLen=20] — Server-generated unique identifier for this add meeting action. Present only in GET responses; not required in POST requests.
`AutomationAddTagsDetails`:
  > PURPOSE: Details object for add_tags action. Adds pre-existing tags to the triggering record. PREREQUISITES: Tags must exist - GET /settings/tags?module={api_name} to list, POST to create first. MANDATORY: tags (array 1-10, each {id, name}). OPTIONAL: over_write (bool, default false - true replaces ALL existing tags), module ({api_name, id}). CONSTRAINTS: Not allowed with convert on Leads (AMBIGUITY_DURING_PROCESSING). over_write=true + remove_tags in same rule = INVALID_DATA. Unsupported: Visits, Users, LinkingModules (NOT_ALLOWED).
  - `over_write` (boolean) [default=False] — Whether to overwrite all existing tags on the record with the specified tags (true) or append to existing tags (false). Default is false. When set to true, any RemoveTags action in the same workflow rule becomes invalid and returns INVALID_DATA ('Remove tag not supported with Overwrite Add Tag').
  - `tags` (array of object `AutomationTagRef`) [minItems=1, maxItems=10] **REQ** — List of tags to add to the record. All tags must pre-exist in the org  - fetch available tags from GET /settings/tags?module={module_api_name}. To create new tags: POST /settings/tags?module={module_api_name}. If the list is empty after parsing, the API returns FAILURE ('Empty Tag'). If the tag count exceeds the edition limit, the API returns FAILURE ('Invalid Tag Count').
  - `module` (object `AutomationModuleRef`) — Target module for the tag action. Must match the workflow rule's trigger module. Supported modules: Leads, Accounts, Contacts, Deals, Campaigns, Tasks, Cases, Events, Calls, Solutions, Products, Vendors, Price_Books, Quotes, Sales_Orders, Purchase_Orders, Invoices, and custom modules. Unsupported modules (Visits, Users, LinkingModules) return NOT_ALLOWED.
  - `id` (string) [maxLen=20] — Server-generated unique identifier for this add tags action. Present only in GET responses; not required in POST requests.
`AutomationAssignOwnerDetails`:
  > Configuration for the assign_owner action. Requires a module reference and an assign_to array with one to five entries, each specifying who to assign the record to — a user, role, group, assignment rule, or profile, a merge field, or matching criteria. Optionally sends a notification, includes related records, applies an assignment threshold, or bases assignment on user availability.
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
`AutomationChatNotificationDetails`:
  > Configuration for the chat notification action. Requires a message, which supports merge fields, and a target channel, user, or field to notify.
  - `message` (string) **REQ** [maxLen=5000] — REQUIRED. Notification message body. Supports merge fields in ${Module.Field} format (e.g., "New deal ${Deals.Deal_Name} created by ${Deals.Owner}!").
  - `notify_to` (object) **REQ** — REQUIRED. Notification target  - a channel, user, or field-based recipient.
    - `type` (string) **REQ** [enum=['user', 'channel', 'fields']] — Target type. 'user'  - send to a specific chat user. 'channel'  - send to a chat channel. 'fields'  - send to users resolved from CRM field values.
    - `id` (string) [maxLen=255] — Required for user/channel types. The integration-specific user or channel ID.
    - `name` (string) [maxLen=255] — Required for user/channel types. Display name of the user or channel (e.g., '#sales-alerts').
    - `module` (object) — Required for type='fields'. The CRM module to resolve field values from. Use GET /settings/modules to discover api_name and id.
      - `id` (string/int64) — Module ID.
      - `api_name` (string) [maxLen=255] — Module API name.
    - `notify_fields` (object) — Required for type='fields'. Field references to resolve notification recipients.
      - `fields` (array of object) [maxItems=10] — Array of field references. Each must have api_name and optionally id. If both given, cross-validated for consistency (AMBIGUITY_DUE_TO if mismatch).
        - `id` (string/int64) — Field ID.
        - `api_name` (string) [maxLen=255] — Field API name. Use GET /settings/fields?module={api_name} to discover.
      - `static_fields` (array of object) [maxItems=10] — Array of static field references.
        - `id` (string/int64) — Static field ID.
        - `api_name` (string) [maxLen=255] — Static field API name.
  - `id` (string) [maxLen=20] — Read-only. Unique identifier for the action, returned in GET responses.
`AutomationCircuitsDetails`:
  > Configuration for the Zoho Circuits action. Requires the ID of the circuit to execute.
  - `circuit_id` (string) **REQ** [maxLen=255] — REQUIRED. Zoho Circuits circuit ID.
  - `id` (string) [maxLen=20] — Read-only. Unique identifier for the action.
`AutomationConvertChangeOwner`:
  > New owner assignment for the converted records. Specifies the user (by id) who should own the converted records, which modules should receive the new owner (via related_modules), and whether to enforce assignment thresholds. When omitted, the source record's owner is retained.
  - `id` (string) **REQ** [maxLen=20] — Unique user ID of the new owner. Obtain from GET /users. Must be an active user with permissions on the target modules.
  - `name` (string) [maxLen=255] — Full name of the new owner. Optional  - present in GET responses for display purposes.
  - `related_modules` (array of object `AutomationRelatedRecord`) [maxItems=10] — List of target modules whose records should receive the new owner during conversion. Reuses the same related-record concept as assign_owner. For Leads conversion: Events, Calls, Tasks, Contacts, Deals are valid. For Quotes/SalesOrders conversion: only Events, Calls, Tasks are valid.
  - `apply_assignment_threshold` (boolean) [default=False] — Whether to enforce assignment-threshold rules (record count limits per user) on the new owner for each converted module. When true, the system checks whether the new owner has reached their record limit before assigning ownership.
`AutomationConvertDetails`:
  > Configuration for converting records. This action is only available when the trigger module is Leads, Quotes, or Sales_Orders. The convert action requires non-null criteria in the condition; null criteria will result in a dependent field missing error. For Leads conversion, the following fields are mandatory: add_to_existing_contact, add_to_existing_account, apply_restriction, and change_owner which is an object containing the apply_assignment_threshold flag. Key optional fields include create_deal for creating a deal, carry_tags which is an array of module references and not a boolean, field_mappings with a maximum of 25 entries, move_attachment_to for specifying a target module, contact_role which is applicable only when create_deal is true, and convert_to which is used for Quotes and SalesOrders conversions. Example configuration for a Leads conversion without creating a deal.
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
`AutomationCreateConnectedRecordDetails`:
  > Configuration for the create_connected_record action. Uses the same structure as create_record — module, layout, and field mappings — but the module must be a valid connected-record child module. Not supported for the Notes, Rebuy, or Competitor Mentions modules.

  - `module` (object) **REQ** — REQUIRED. Target child module for connected record creation. Must be a valid connected-record child module of the rule's module. Use GET /settings/modules to discover api_name and id.
    - `api_name` (string) **REQ** [maxLen=255] — Module API name.
    - `id` (string/int64) — Module ID.
  - `layout` (object `AutomationLayoutRef`) **REQ** — Represents a layout reference, conforming to the AutomationLayoutRef schema, that determines which layout is applied when creating the connected record. The id field is mandatory and governs which fields are available and required for the target module; valid layout identifiers are obtainable from GET /settings/layouts?module={api_name}.
  - `field_mappings` (array of object `AutomationFieldMappings`) [maxItems=25] **REQ** — REQUIRED. Field mapping array (1-25 entries). Use GET /settings/fields?module={api_name} to discover field api_name and id. All mandatory fields for the target module/layout must be included.
  - `apply_restriction` (boolean) — Apply assignment/workflow restrictions. Default true.
  - `id` (string) [maxLen=20] — Read-only. Unique identifier for the action.
`AutomationCreateRecordDetails`:
  > Configuration for the create_record action. Requires a module, a layout, and one to twenty-five field mappings that supply values for the new record fields, using a static value, a merge field, an execution-time offset, or a composite value. All fields marked mandatory by the layout must be included. Optionally restricts creation to prevent duplicate records.

  - `module` (object `AutomationModuleRef`) **REQ** — Target module in which the new record will be created. Supported modules: Leads, Contacts, Potentials (Deals), Accounts, Products, Cases, custom modules, and team modules. NOT supported: Tasks, Events, Calls - use add_meeting for Events and schedule_call for Calls. Fetch available modules from GET /settings/modules. At least api_name or id must be provided; always use the full 19-digit module ID as returned by the modules API.
  - `layout` (object `AutomationLayoutRef`) **REQ** — Layout to use when creating the record. Determines which fields are available and their validation rules. Fetch valid layouts from GET /settings/layouts?module={module_api_name}. The layout.id is required.
  - `field_mappings` (array of object `AutomationFieldMappings`) [minItems=1, maxItems=25] **REQ** — Field mappings for the new record. Each entry: {"field": {"api_name": "Last_Name"}, "type": "static", "value": "Test"}. Must include all mandatory fields (system_mandatory=true or api_mandatory=true from GET /settings/layouts?module={module}) - missing ones cause REQUIRED_DATA_NOT_FOUND. Mapping types: static - literal values for text, picklist, phone, number fields; NOT for Date/DateTime/ALARM (DEPENDENT_MISMATCH) or unique fields (INVALID_DATA, check unique=true in GET /settings/fields). merge_field - runtime tokens like ${!Leads.Company} for text-based fields; NOT for lookup/owner fields (DEPENDENT_MISMATCH). execution_time - REQUIRED for Date/DateTime/ALARM fields; periods: days, business_days, hours, minutes; sign required for datetime fields.
  - `apply_restriction` (boolean) [default=False, nullable] — Whether to enforce assignment-threshold rules (record count limits per user) on the record owner when creating the record. When true, the system checks whether the owner has reached their record limit before creating the record. Only effective when the org has assignment thresholds configured.
  - `id` (string) [maxLen=20] — Server-generated unique identifier for this create record action. Present only in GET responses; not required in POST requests.
`AutomationEmailCreateRecordDetails`:
  > Configuration for the create-record-from-email action. Requires the target module, either Leads or Contacts, and exactly one field mapping that assigns the record owner.

  - `module` (object) **REQ** — REQUIRED. Target module  - only 'Leads' or 'Contacts' allowed.
    - `api_name` (string) **REQ** [enum=['Leads', 'Contacts']] — Module API name. Must be 'Leads' or 'Contacts'.
  - `field_mappings` (array of object) [minItems=1, maxItems=1] **REQ** — REQUIRED. Exactly 1 field mapping entry. More than 1 returns too_many_records, none returns no_data.
    - `field` (object) **REQ** — Field reference. Use GET /settings/fields?module={api_name} to discover.
      - `api_name` (string) [maxLen=255] — Field API name.
      - `id` (string/int64) — Field ID.
    - `value` (object) **REQ** — Owner assignment details.
      - `type` (string) **REQ** [enum=['user', 'role', 'group', 'country']] — Owner assignment type.
      - `resource` (object) — Assignment target reference.
        - `id` (string/int64) — Resource ID.
  - `id` (string) [maxLen=20] — Read-only. Unique identifier for the action.
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
  > Target module for the ownership assignment. Must match the workflow rule's trigger module for direct assignments, or the lookup field's related module for cross-module assignments. At least api_name or id must be provided; if both are given and they do not match, the API returns AMBIGUITY_DURING_PROCESSING.
  - `api_name` (string) [maxLen=255] — API name of the module (e.g., Leads, Contacts, Deals, Vendors).
  - `id` (string) [maxLen=20] — Unique module ID (19-digit format). Always use the full ID as returned by GET /settings/modules - truncated or shortened IDs return INVALID_DATA ('the tabId given seems to be invalid'). Optional in requests if api_name is provided; always present in responses.
`AutomationRelatedRecord`:
  > Identifies a related module whose open records' ownership should be transferred alongside the parent record. Used by assign_owner actions, field_updates (Owner field), and convert actions (change_owner.related_modules). Common activity modules (Tasks, Calls, Events) are available for all modules and actions. Contacts is available for assign_owner when parent is Accounts, and for convert when converting Leads. Deals is available for assign_owner when parent is Accounts or Contacts, and for convert when converting Leads (requires create_deal=true).
  - `api_name` (string) **REQ** [maxLen=255, enum=['Events', 'Calls', 'Tasks', 'Contacts', 'Deals']] — API name of the related module. Events, Calls, Tasks - open activity records, available for all modules and actions (assign_owner, convert). Contacts - available for assign_owner when parent is Accounts, and for convert when converting Leads. Deals - available for assign_owner when parent is Accounts or Contacts, and for convert when converting Leads (requires create_deal=true).
  - `id` (string) [maxLen=255] — Unique identifier of the related module. This is the module ID corresponding to the api_name.
`AutomationRemoveTagsDetails`:
  > Configuration for remove_tags actions. The tags array is required and must contain between 1 and 10 entries, each specifying both the tag identifier and name. Tags must already exist in the system before they can be removed. The module reference is optional but when provided, its API name and identifier must match the trigger module. The over_write field is accepted for type compatibility but its value is ignored for remove_tags operations.

This action is invalid when the same rule contains an add_tags action with over_write set to true. It cannot be used alongside a convert action on Leads modules, as this combination triggers an AMBIGUITY_DURING_PROCESSING error. The remove_tags action is not supported for Visits, Users, or LinkingModules.

Example configuration: {"tags": [{"id": "111111000000050001", "name": "Hot Lead"}], "module": {"api_name": "Leads", "id": "111111000000000175"}}

  - `tags` (array of object `AutomationTagRef`) [minItems=1, maxItems=10] **REQ** — List of tags to remove from the record. All tags must pre-exist in the org  - fetch available tags from GET /settings/tags?module={module_api_name}. If the list is empty after parsing, the API returns FAILURE ('Empty Tag'). If the tag count exceeds the edition limit, the API returns FAILURE ('Invalid Tag Count').
  - `module` (object `AutomationModuleRef`) — Target module for the tag action. Must match the workflow rule's trigger module. Supported modules: Leads, Accounts, Contacts, Deals, Campaigns, Tasks, Cases, Events, Calls, Solutions, Products, Vendors, Price_Books, Quotes, Sales_Orders, Purchase_Orders, Invoices, and custom modules. Unsupported modules (Visits, Users, LinkingModules) return NOT_ALLOWED.
  - `over_write` (boolean) [default=False] — Present in GET responses. Its value is ignored for remove_tags actions.
  - `id` (string) [maxLen=20] — Server-generated unique identifier for this remove tags action. Present only in GET responses; not required in POST or PUT requests.
`AutomationScheduleCallDetails`:
  > Configuration for the schedule_call action. Requires the Calls module, a layout, and field mappings that include the call subject. Optionally restricts creation to prevent duplicate records.

  - `module` (object `AutomationModuleRef`) **REQ** — Target module for the call. Must be the Calls module. Provide either api_name ("Calls") or the Calls module id.
  - `layout` (object `AutomationLayoutRef`) **REQ** — Layout to use when creating the Call record. Determines which fields are available and their validation rules. Fetch valid layouts from GET /settings/layouts?module=Calls. The layout.id is required.
  - `field_mappings` (array of object `AutomationFieldMappings`) [minItems=1, maxItems=25] **REQ** — Field mappings for the new Call. Each entry: {"field": {"api_name": "Subject"}, "type": "static", "value": "Follow-up"}. Must include all mandatory fields from GET /settings/layouts?module=Calls. Call_Type is system-mandatory (values: "Outbound", "Inbound", "Missed") - omitting returns REQUIRED_DATA_NOT_FOUND. Common fields: Subject, Call_Type, Call_Purpose, Call_Start_Time, Remind_At. Mapping types: static - literal values for text, picklist fields; NOT for DateTime/ALARM (DEPENDENT_MISMATCH). merge_field - runtime tokens like ${!Leads.Phone} for text-based fields; NOT for lookup/owner (DEPENDENT_MISMATCH). execution_time - REQUIRED for Call_Start_Time and Remind_At; sign required for datetime; periods: days, business_days, hours, minutes.
  - `apply_restriction` (boolean) [default=False, nullable] — Whether to enforce assignment-threshold rules (record count limits per user) on the record owner when creating the Call record. When true, the system checks whether the owner has reached their record limit before creating the record. Only effective when the org has assignment thresholds configured.
  - `id` (string) [maxLen=20] — Server-generated unique identifier for this schedule call action. Present only in GET responses; not required in POST requests.
`AutomationSocialDetails`:
  > Configuration for the social action, containing the message content with merge field support. Required for commenting or replying actions, and not needed for like or retweet actions.

  - `content` (string) [maxLen=5000] — Message content. Supports merge fields in ${Module.Field} format. REQUIRED for: comment_to_post, reply_to_comment, reply_to_message, reply_to_tweet. NOT required for: like_to_comment, retweet (details can be empty).
  - `id` (string) [maxLen=20] — Read-only. Unique identifier for the action.
`AutomationTagRef`:
  > Represents a tag reference, conforming to the AutomationTagRef schema, that identifies a pre-existing org tag to be added to the record. Both id and name are mandatory fields on each entry; the referenced tag must already exist in the org before the action executes.
  - `id` (string) **REQ** [maxLen=20] — Unique identifier of the tag. Obtain from GET /settings/tags?module={module_api_name}. If provided alone, the tag is resolved by ID. If both id and name are provided, they must resolve to the same tag.
  - `name` (string) **REQ** [maxLen=25] — Name of the tag. Obtain from GET /settings/tags?module={module_api_name}. If provided alone, the tag is resolved by name. Must match an existing tag  - providing a non-existent name returns INVALID_DATA. Max 25 characters, cannot contain <, >, commas, or emojis.
  - `color_code` (string) [maxLen=25] — Hex color code of the tag (e.g., '#879BFC'). Optional in requests; present in GET responses. Allowed values: #F17574, #F48435, #E7A826, #A8C026, #63C57E, #1DB9B4, #57B1FD, #879BFC, #D297EE, #FD87BD, #969696, #658BA8, #B88562.
`AutomationZohoFlowDetails`:
  > Configuration for the Zoho Flow action. Requires the ID and name of the custom action to trigger in Zoho Flow.

  - `custom_action_id` (string/int64) **REQ** — REQUIRED. Zoho Flow custom action ID. Value = `id` from `getCustomActions` response.
  - `custom_action_name` (string) **REQ** [maxLen=255] — REQUIRED. Display name of the Zoho Flow action. Value = `action_name` from `getCustomActions` response.
  - `id` (string) [maxLen=20] — Read-only. Unique identifier for the action.
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
`ChatNotificationActionSchema`:
  > Represents a non-associate action that sends a chat notification to an integrated chat service, such as Slack or Zoho Cliq, when the workflow rule condition is triggered.
  - `name` (string) **REQ** [maxLen=100] — Represents the display name of the ChatNotification action. This field is required.
  - `type` (string) **REQ** [enum=[5 values]] — Represents chat service type. Each service has a limit of 1 action per rule.
  - `details` (object `AutomationChatNotificationDetails`) **REQ** — Configuration for the chat notification action. Requires a message, which supports merge fields, and a target channel, user, or field to notify.
  - `id` (string) [maxLen=20] — Represents the unique ID of the ChatNotification action within the workflow rule.
  - `_delete` (null) — Indicates that this action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
`CircuitsActionSchema`:
  > Represents a non-associate action that executes a Zoho Circuits workflow when the workflow rule condition is triggered.
  - `name` (string) **REQ** [maxLen=100] — Represents the display name of the Circuits action. This field is required.
  - `type` (string) **REQ** [const=circuits] — Represents the action type discriminator that identifies this as a Circuits action within the workflow rule. The value is fixed for this action type and must be supported by the target module and trigger event.
  - `details` (object `AutomationCircuitsDetails`) **REQ** — Configuration for the Zoho Circuits action. Requires the ID of the circuit to execute.
  - `id` (string) [maxLen=20] — Represents the unique ID of the Circuits action within the workflow rule.
  - `_delete` (null) — Indicates that this action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
`CompositeFieldMapping`:
  > Represents a composite-type field mapping used exclusively for the Participants field in the Events module via the add_meeting action. The value carries a structured object that encodes participant data and is not applicable to any other field or automation action type.
  - `display_value` (string) [maxLen=500] — The server-computed representation of the mapped value, included in GET responses. Omitted from create and update requests.
  - `field` (object `AutomationFieldAttributes`) **REQ** — Target field to populate when the automation executes. api_name is required. If id is also provided, both must refer to the same field; otherwise the API returns AMBIGUITY_DURING_PROCESSING.
  - `type` (string) **REQ** [const=composite] — Serves as the polymorphic discriminator that identifies this field mapping as a composite mapping; the value must be set to "composite" to select this schema variant.
  - `value` (object) **REQ** — Holds the structured composite object that encodes participant data for the Events module Participants field; the shape of this object varies according to the participant type configuration defined for the automation rule.
`ConvertActionSchema`:
  > Represents a non-associate action that converts a record to another module type, such as converting a lead to a contact, account, and deal.
  - `name` (string) [maxLen=100] — Represents the display name of the Convert action as it appears within the workflow rule configuration.
  - `type` (string) **REQ** [const=convert] — Represents the action type discriminator that identifies this as a Convert action within the workflow rule. The value is fixed for this action type and must be supported by the target module and trigger event.
  - `details` (object `AutomationConvertDetails`) **REQ** — Configuration for converting records. This action is only available when the trigger module is Leads, Quotes, or Sales_Orders. The convert action requires non-null criteria in the condition; null criteria will result in a dependent field missing error. For Leads conversion, the following fields are mandatory: add_to_existing_contact, add_to_existing_account, apply_restriction, and change_owner which is an object containing the apply_assignment_threshold flag. Key optional fields include create_deal for creating a deal, carry_tags which is an array of module references and not a boolean, field_mappings with a maximum of 25 entries, move_attachment_to for specifying a target module, contact_role which is applicable only when create_deal is true, and convert_to which is used for Quotes and SalesOrders conversions. Example configuration for a Leads conversion without creating a deal.
  - `related_details` (object `RelatedDetailsNestedSchema`) — Optional. For convert, related_details is not typically used. Applicable sub-fields: best_time (for email_notifications only), followup_details (for tasks only), lookup_field (for field_updates only).
  - `id` (string) [maxLen=20] — Represents the unique ID of the Convert action within the workflow rule.
  - `_delete` (null) — Indicates that this action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
`CreateConnectedRecordActionSchema`:
  > Represents a non-associate action that creates a connected record in a child module when the workflow rule condition is triggered.
  - `name` (string) [maxLen=100] — Represents the display name of the CreateConnectedRecord action as it appears within the workflow rule configuration.
  - `type` (string) **REQ** [const=create_connected_record] — Represents the action type discriminator that identifies this as a CreateConnectedRecord action within the workflow rule. The value is fixed for this action type and must be supported by the target module and trigger event.
  - `details` (object `AutomationCreateConnectedRecordDetails`) **REQ** — Configuration for the create_connected_record action. Uses the same structure as create_record — module, layout, and field mappings — but the module must be a valid connected-record child module. Not supported for the Notes, Rebuy, or Competitor Mentions modules.

  - `related_details` (object `RelatedDetailsNestedSchema`) — Optional. Not typically used for create_connected_record.
  - `id` (string) [maxLen=20] — Represents the unique ID of the CreateConnectedRecord action within the workflow rule.
  - `_delete` (null) — Indicates that this action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
`CreateRecordActionSchema`:
  > Represents a non-associate action that creates a new record in a specified CRM module when the workflow rule condition is triggered.
  - `name` (string) [maxLen=100] — Represents the display name of the CreateRecord action as it appears within the workflow rule configuration.
  - `type` (string) **REQ** [const=create_record] — Represents the action type discriminator that identifies this as a CreateRecord action within the workflow rule. The value is fixed for this action type and must be supported by the target module and trigger event.
  - `details` (object `AutomationCreateRecordDetails`) **REQ** — Configuration for the create_record action. Requires a module, a layout, and one to twenty-five field mappings that supply values for the new record fields, using a static value, a merge field, an execution-time offset, or a composite value. All fields marked mandatory by the layout must be included. Optionally restricts creation to prevent duplicate records.

  - `related_details` (object `RelatedDetailsNestedSchema`) — Optional. For create_record, related_details is not typically used. Applicable sub-fields: best_time (for email_notifications only), followup_details (for tasks only), lookup_field (for field_updates only).
  - `id` (string) [maxLen=20] — Represents the unique ID of the CreateRecord action within the workflow rule.
  - `_delete` (null) — Indicates that this action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
`CreatedModifiedByObjectSchema`:
  > Represents the identity details of the CRM user who created or last modified the workflow rule.
  - `name` (string/string) — Represents the name of the CRM user who created or last modified the workflow rule.
  - `id` (string/string) — Represents the unique ID of the CRM user.
`EmailCreateRecordActionSchema`:
  > Represents a non-associate action that creates a record via an email-based trigger, applicable to modules such as Leads or Contacts.
  - `name` (string) [maxLen=100] — Represents the display name of the EmailCreateRecord action as it appears within the workflow rule configuration.
  - `type` (string) **REQ** [const=create_record_email] — Represents the action type discriminator that identifies this as a EmailCreateRecord action within the workflow rule. The value is fixed for this action type and must be supported by the target module and trigger event.
  - `details` (object `AutomationEmailCreateRecordDetails`) **REQ** — Configuration for the create-record-from-email action. Requires the target module, either Leads or Contacts, and exactly one field mapping that assigns the record owner.

  - `id` (string) [maxLen=20] — Represents the unique ID of the EmailCreateRecord action within the workflow rule.
  - `_delete` (null) — Indicates that this action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
`EmailNotificationAssociateActionSchema`:
  > Represents an associate action that sends a pre-configured email notification when the workflow rule condition is triggered.
  - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the email notification. Required when associating an existing email notification with the rule.
  - `name` (string) [maxLen=500] — Represents the display name of the EmailNotificationAssociate action. Returned in GET responses and derived from the associated action configuration.
  - `type` (string) **REQ** [const=email_notifications] — Represents the action type discriminator that identifies this as a EmailNotificationAssociate action within the workflow rule. The value is fixed for this action type and must be supported by the target module and trigger event.
  - `details` (object) — Represents the read-only details of the associated email notification. Returned in GET responses and not required in POST or PUT requests.
    - `module` (object `ModuleOrFieldNestedSchema`) — The module this action applies to.
  - `related_details` (object `EmailNotificationRelatedDetailsSchema`) — Controls whether the email is sent at the best time for the recipient (powered by Data Intelligence). Null when best_time is not enabled.
  - `_delete` (null) — Indicates that this action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
`EmailNotificationRelatedDetailsSchema`:
  oneOf:
      - `best_time` (boolean) — Indicates whether to send the email notification at the best time for the recipient. When set to true, the platform determines the optimal send time.
      type: null — Represents a null value indicating best-time delivery is not configured for this email notification action.
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
`FieldUpdateAssociateActionSchema`:
  > Represents an associate action that updates field values using a pre-configured field update action when the workflow rule condition is triggered.
  - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the field update action. Use the Get Field Updates API to retrieve available IDs.
  - `name` (string) [maxLen=500] — Represents the display name of the FieldUpdateAssociate action. Returned in GET responses and derived from the referenced action configuration.
  - `type` (string) **REQ** [const=field_updates] — Represents the action type discriminator that identifies this as a FieldUpdateAssociate action within the workflow rule. The value is fixed for this action type and must be supported by the target module and trigger event.
  - `details` (object) — Represents the read-only details of the associated field update action. Returned in GET responses and not required in POST or PUT requests.
    - `module` (object `ModuleOrFieldNestedSchema`) — The module this action applies to.
  - `related_details` (object `FieldUpdateRelatedDetailsSchema`) — Specifies the lookup field when the field update targets a related module. Null when the update targets the workflow rule's own module.
  - `_delete` (null) — Indicates that this action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
`FieldUpdateRelatedDetailsSchema`:
  oneOf:
      - `lookup_field` (object `ModuleOrFieldNestedSchema`) — The lookup field linking the rule module to the target module (e.g., Account_Name on Contacts). Provide the field's id and api_name.
      type: null — Represents a null value indicating the field update targets the workflow rule own module with no lookup field required.
`FilterCriterionRequest`:
  oneOf:
    - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
    - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
`FilterFieldBase`:
  > Represents the base field reference used in filter operations, containing minimal required properties. The field's data_type is not part of this object; resolve it from the corresponding FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `id` (string/int64) — Represents the unique ID of the field used for filter operations.
  - `api_name` (string) **REQ** — Represents the API name of the field used for filter application. Supports relationship notation, for example, Deals__r.Stage.
  additionalProperties: any
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
`ModuleOrFieldNestedSchema`:
  > The module that actually triggers the rule. Defaults to the rule's top-level module if omitted. Must be explicitly set when the trigger targets a different module, such as a rule on Leads triggered by a note creation event, which requires the trigger module to reference the Notes module. To discover module API names and identifiers, retrieve the available modules from the system.
  - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the module or field, such as **Leads**, **Contacts**, or a custom field API name.
  - `id` (string) **REQ** [maxLen=20] — Represents the unique numeric ID of the module or field.
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
`NonAssociateActionsNestedSchema`:
  discriminator: `type`
  oneOf:
    - `AssignOwnerActionSchema` — Represents a non-associate action that assigns or reassigns the record owner when the workflow rule condition is triggered.
    - `CreateRecordActionSchema` — Represents a non-associate action that creates a new record in a specified CRM module when the workflow rule condition is triggered.
    - `CreateConnectedRecordActionSchema` — Represents a non-associate action that creates a connected record in a child module when the workflow rule condition is triggered.
    - `AddMeetingActionSchema` — Represents a non-associate action that schedules a meeting when the workflow rule condition is triggered.
    - `ScheduleCallActionSchema` — Represents a non-associate action that schedules a call activity on the triggering record when the workflow rule condition is met.
    - `AddTagsActionSchema` — Represents a non-associate action that adds pre-existing tags to the triggering record when the workflow rule condition is met.
    - `RemoveTagsActionSchema` — Represents a non-associate action that removes one or more tags from the triggering record when the workflow rule condition is met.
    - `ConvertActionSchema` — Represents a non-associate action that converts a record to another module type, such as converting a lead to a contact, account, and deal.
    - `ChatNotificationActionSchema` — Represents a non-associate action that sends a chat notification to an integrated chat service, such as Slack or Zoho Cliq, when the workflow rule condition is triggered.
    - `CircuitsActionSchema` — Represents a non-associate action that executes a Zoho Circuits workflow when the workflow rule condition is triggered.
    - `ZohoFlowActionSchema` — Represents a non-associate action that triggers a Zoho Flow workflow when the workflow rule condition is met.
    - `SocialActionSchema` — Represents a non-associate action that publishes a post to a social network such as Facebook or Twitter when the workflow rule condition is triggered.
    - `EmailCreateRecordActionSchema` — Represents a non-associate action that creates a record via an email-based trigger, applicable to modules such as Leads or Contacts.
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
`RelatedDetailsNestedSchema`:
  oneOf:
      - `best_time` (boolean) — Indicates whether to send the email notification at the best time for the recipient. When set to true, the platform determines the optimal send time.
      - `followup_details` (object) — Represents the followup task configuration, including the trigger condition and delay settings.
        - `condition` (string) [maxLen=255] — Represents the task status condition that triggers the followup task, such as **Completed** or **Not Started**.
        - `unit` (integer/int32) — Represents the numeric time value for the delay before creating the followup task.
        - `period` (string) [maxLen=50] — Represents the time period label for the delay before creating the followup task, such as **days**, **hours**, or **minutes**.
      - `lookup_field` (object `ModuleOrFieldNestedSchema`) — The lookup field linking the rule module to the target module (e.g., Account_Name on Contacts). Provide the field's id and api_name. When the field update targets the same module, related_details is null.
      type: null — Represents a null value indicating no related details are configured for this action.
`RemoveTagsActionSchema`:
  > Represents a non-associate action that removes one or more tags from the triggering record when the workflow rule condition is met.
  - `name` (string) [maxLen=100] — Represents the display name of the RemoveTags action as it appears within the workflow rule configuration.
  - `type` (string) **REQ** [const=remove_tags] — Represents the action type discriminator that identifies this as a RemoveTags action within the workflow rule. The value is fixed for this action type and must be supported by the target module and trigger event.
  - `details` (object `AutomationRemoveTagsDetails`) **REQ** — Configuration for remove_tags actions. The tags array is required and must contain between 1 and 10 entries, each specifying both the tag identifier and name. Tags must already exist in the system before they can be removed. The module reference is optional but when provided, its API name and identifier must match the trigger module. The over_write field is accepted for type compatibility but its value is ignored for remove_tags operations.

This action is invalid when the same rule contains an add_tags action with over_write set to true. It cannot be used alongside a convert action on Leads modules, as this combination triggers an AMBIGUITY_DURING_PROCESSING error. The remove_tags action is not supported for Visits, Users, or LinkingModules.

Example configuration: {"tags": [{"id": "111111000000050001", "name": "Hot Lead"}], "module": {"api_name": "Leads", "id": "111111000000000175"}}

  - `related_details` (object `RelatedDetailsNestedSchema`) — Optional. For remove_tags, related_details is not typically used. Applicable sub-fields: best_time (for email_notifications only), followup_details (for tasks only), lookup_field (for field_updates only).
  - `id` (string) [maxLen=20] — Represents the unique ID of the RemoveTags action within the workflow rule.
  - `_delete` (null) — Indicates that this action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
`ScheduleCallActionSchema`:
  > Represents a non-associate action that schedules a call activity on the triggering record when the workflow rule condition is met.
  - `name` (string) [maxLen=100] — Represents the display name of the ScheduleCall action as it appears within the workflow rule configuration.
  - `type` (string) **REQ** [const=schedule_call] — Represents the action type discriminator that identifies this as a ScheduleCall action within the workflow rule. The value is fixed for this action type and must be supported by the target module and trigger event.
  - `details` (object `AutomationScheduleCallDetails`) **REQ** — Configuration for the schedule_call action. Requires the Calls module, a layout, and field mappings that include the call subject. Optionally restricts creation to prevent duplicate records.

  - `related_details` (object `RelatedDetailsNestedSchema`) — Optional. For schedule_call, related_details is not typically used. Applicable sub-fields: best_time (for email_notifications only), followup_details (for tasks only), lookup_field (for field_updates only).
  - `id` (string) [maxLen=20] — Represents the unique ID of the ScheduleCall action within the workflow rule.
  - `_delete` (null) — Indicates that this action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
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
`SimpleAssociateActionSchema`:
  > Represents an associate action that references a pre-configured action entity by its unique ID, applicable to action types such as webhooks, functions, and notifications.
  - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the pre-configured action entity. Required to associate an existing action with the workflow rule.
  - `name` (string) [maxLen=500] — Represents the display name of the SimpleAssociate action. Returned in GET responses and derived from the referenced action configuration.
  - `type` (string) **REQ** [enum=['webhooks', 'functions', 'sms', 'whatsapp']] — Represents the type of associate action.
Possible values:
webhooks - HTTP callback to an external URL.
functions - Custom function execution.
email_notifications - Automated email notification.
tasks - Task creation action.
  - `details` (object) — Represents the read-only details of the associated action entity. Returned in GET responses and not required in POST or PUT requests.
    - `module` (object `ModuleOrFieldNestedSchema`) — The module this action applies to.
  - `_delete` (null) — Indicates that this action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
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
`SocialActionSchema`:
  > Represents a non-associate action that publishes a post to a social network such as Facebook or Twitter when the workflow rule condition is triggered.
  - `name` (string) [maxLen=100] — Represents the display name of the Social action as it appears within the workflow rule configuration.
  - `type` (string) **REQ** [enum=[6 values]] — Represents the social action type. Facebook actions require Facebook-specific triggers, and Twitter actions require Twitter-specific triggers.
  - `details` (object `AutomationSocialDetails`) — Configuration for the social action, containing the message content with merge field support. Required for commenting or replying actions, and not needed for like or retweet actions.

  - `id` (string) [maxLen=20] — Represents the unique ID of the Social action within the workflow rule.
  - `_delete` (null) — Indicates that this action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
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
`TaskAssociateActionSchema`:
  > Represents an associate action that creates a task based on a pre-configured task template when the workflow rule condition is triggered.
  - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the task action. Required to associate a pre-configured task with the workflow rule.
  - `name` (string) [maxLen=500] — Represents the display name of the TaskAssociate action. Returned in GET responses and derived from the referenced action configuration.
  - `type` (string) **REQ** [const=tasks] — Represents the action type discriminator that identifies this as a TaskAssociate action within the workflow rule. The value is fixed for this action type and must be supported by the target module and trigger event.
  - `details` (object) — Represents the read-only details of the associated task action. Returned in GET responses and not required in POST or PUT requests.
    - `module` (object `ModuleOrFieldNestedSchema`) — The module this action applies to.
  - `related_details` (object `TaskRelatedDetailsSchema`) — Configures a followup task that is automatically created after the original task, based on a status condition and time delay. Null when no followup is configured.
  - `_delete` (null) — Indicates that this action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
`TaskRelatedDetailsSchema`:
  oneOf:
      - `followup_details` (object) — Represents the followup task configuration, including the trigger condition and delay settings.
        - `condition` (string) [maxLen=255] — Represents the task status condition that triggers the followup task, such as **Completed** or **Not Started**.
        - `unit` (integer/int32) — Represents the numeric time value for the delay before creating the followup task.
        - `period` (string) [maxLen=50] — Represents the time period label for the delay before creating the followup task, such as **days**, **hours**, or **minutes**.
      type: null — Represents a null value indicating no followup task is configured for this task action.
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
`WorkflowGroupedFilterCriterion`:
  > Represents a grouped filter criterion containing multiple simple filter conditions evaluated together using a logical operator such as AND or OR.
  - `group` (array of object) [minItems=2, maxItems=25] **REQ** — Represents the array of filter conditions to be evaluated together using the specified logical operator.
    oneOf:
      - `WorkflowSimpleFilterCriterion` — Represents a simple filter criterion for workflow rule queries, specifying the field API name, comparator, and value to match.
      - `WorkflowGroupedFilterCriterion` — Represents a grouped filter criterion containing multiple simple filter conditions evaluated together using a logical operator such as AND or OR.
  - `group_operator` (string) **REQ** [enum=['AND', 'OR']] — Represents the logical operator applied between the filter conditions in the group.
`WorkflowSimpleFilterCriterion`:
  > Represents a simple filter criterion for workflow rule queries, specifying the field API name, comparator, and value to match.
  - `field` (object) **REQ** — Represents the field to which the filter criterion is applied.
  - `comparator` (string) **REQ** [enum=[16 values]] — Represents the comparison operator applied to the filter criterion. **${ANYVALUE}** is a special value supported only in field update triggers; it matches any change to the monitored field value.
  - `value` (object) **REQ**
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates whether the criterion value is a direct value or a system variable placeholder.
`ZohoFlowActionSchema`:
  > Represents a non-associate action that triggers a Zoho Flow workflow when the workflow rule condition is met.
  - `name` (string) **REQ** [maxLen=100] — Represents the display name of the Zoho Flow action. This field is required.
  - `type` (string) **REQ** [const=flow] — Represents the action type discriminator that identifies this as a Zoho Flow action within the workflow rule.
  - `details` (object `AutomationZohoFlowDetails`) **REQ** — Configuration for the Zoho Flow action. Requires the ID and name of the custom action to trigger in Zoho Flow.

  - `id` (string) [maxLen=20] — Represents the unique ID of the Zoho Flow action within the workflow rule.
  - `_delete` (null) — Indicates that this Zoho Flow action should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.

**Responses:**

- **200**: Returns the complete configuration of the specified workflow rule.
 — Schema: `WorkflowRuleSingleGetResponseSchema` [application/json]
    > Represents the response body for a single workflow rule retrieval, containing a single-element array with the full rule details.
    schema: `WorkflowRuleSingleGetResponseSchema`
    - `workflow_rules` (array of object `WorkflowRuleSingleGetSchema`) [maxItems=10] **REQ** — Represents the array containing the single workflow rule retrieved.
      schema: `WorkflowRuleSingleGetSchema`
      - `created_time` (string/date-time) **REQ** [maxLen=255] — Represents the ISO 8601 timestamp indicating when the system created this workflow rule.
      - `execute_when` (object `ExecuteWhenNestedSchema`) **REQ** — Represents the trigger configuration that defines when the workflow rule fires, including the trigger type and its associated details.
        discriminator: `type`
          create → #/components/schemas/ExecuteWhenT1Simple
          edit → #/components/schemas/ExecuteWhenT1Simple
          create_or_edit → #/components/schemas/ExecuteWhenT1Simple
          delete → #/components/schemas/ExecuteWhenT1Simple
          cancel → #/components/schemas/ExecuteWhenT1Simple
          reschedule → #/components/schemas/ExecuteWhenT1Simple
          reassign → #/components/schemas/ExecuteWhenT1Simple
          anyaction → #/components/schemas/ExecuteWhenT1Simple
          deactivate → #/components/schemas/ExecuteWhenT1Simple
          activate → #/components/schemas/ExecuteWhenT1Simple
          marked_as_complete → #/components/schemas/ExecuteWhenT1Simple
          incoming_call_ring → #/components/schemas/ExecuteWhenT1Simple
          incoming_call_start → #/components/schemas/ExecuteWhenT1Simple
          incoming_call_createedit → #/components/schemas/ExecuteWhenT1Simple
          incoming_call_edit → #/components/schemas/ExecuteWhenT1Simple
          outgoing_call_ring → #/components/schemas/ExecuteWhenT1Simple
          outgoing_call_start → #/components/schemas/ExecuteWhenT1Simple
          outgoing_call_edit → #/components/schemas/ExecuteWhenT1Simple
          outgoing_call_createedit → #/components/schemas/ExecuteWhenT1Simple
          missed_call → #/components/schemas/ExecuteWhenT1Simple
          scheduled_call_createedit → #/components/schemas/ExecuteWhenT1Simple
          scheduled_call_edit → #/components/schemas/ExecuteWhenT1Simple
          email_received → #/components/schemas/ExecuteWhenT1Simple
          mail_sent → #/components/schemas/ExecuteWhenT1Simple
          mail_sent_clicked → #/components/schemas/ExecuteWhenT1Simple
          mail_sent_replied → #/components/schemas/ExecuteWhenT1Simple
          mail_sent_opened → #/components/schemas/ExecuteWhenT1Simple
          mail_sent_bounced → #/components/schemas/ExecuteWhenT1Simple
          fb_post_on_page → #/components/schemas/ExecuteWhenT1Simple
          fb_comment_on_page → #/components/schemas/ExecuteWhenT1Simple
          fb_like_on_post → #/components/schemas/ExecuteWhenT1Simple
          fb_send_message → #/components/schemas/ExecuteWhenT1Simple
          tw_mention_on → #/components/schemas/ExecuteWhenT1Simple
          tw_retweet_on_tweet → #/components/schemas/ExecuteWhenT1Simple
          tw_comment_on_tweet → #/components/schemas/ExecuteWhenT1Simple
          tw_send_message → #/components/schemas/ExecuteWhenT1Simple
          voc_incoming_signal → #/components/schemas/ExecuteWhenT1Simple
          field_update → #/components/schemas/ExecuteWhenT2FieldUpdate
          incoming_call_field_update → #/components/schemas/ExecuteWhenT2FieldUpdate
          outgoing_call_field_update → #/components/schemas/ExecuteWhenT2FieldUpdate
          scheduled_call_field_update → #/components/schemas/ExecuteWhenT2FieldUpdate
          stage_automation_field_update → #/components/schemas/ExecuteWhenT2FieldUpdate
          rollup_summary_update → #/components/schemas/ExecuteWhenT2FieldUpdate
          section_update → #/components/schemas/ExecuteWhenT3SectionUpdate
          incoming_call_section_update → #/components/schemas/ExecuteWhenT3SectionUpdate
          outgoing_call_section_update → #/components/schemas/ExecuteWhenT3SectionUpdate
          scheduled_call_section_update → #/components/schemas/ExecuteWhenT3SectionUpdate
          date_or_datetime → #/components/schemas/ExecuteWhenT4DateBased
          overdue → #/components/schemas/ExecuteWhenT5TimeOffset
          email_received_notreplied → #/components/schemas/ExecuteWhenT5TimeOffset
          email_received_opened_notreplied → #/components/schemas/ExecuteWhenT5TimeOffset
          mail_sent_opened_notreplied → #/components/schemas/ExecuteWhenT5TimeOffset
          mail_sent_notreplied → #/components/schemas/ExecuteWhenT5TimeOffset
          mail_sent_notopened → #/components/schemas/ExecuteWhenT5TimeOffset
          recommendation_rebuy → #/components/schemas/ExecuteWhenT5TimeOffset
          score_increase → #/components/schemas/ExecuteWhenT6ScoreUpdate
          score_decrease → #/components/schemas/ExecuteWhenT6ScoreUpdate
          score_update → #/components/schemas/ExecuteWhenT6ScoreUpdate
          zia_scoring_rule → #/components/schemas/ExecuteWhenT6ScoreUpdate
          mail_sent_replied_within → #/components/schemas/ExecuteWhenT7EmailRepliedWithin
        oneOf:
          - `ExecuteWhenT1Simple` — Represents a simple trigger type (T1) that fires on record creation, editing, deletion, or when specific CRM events occur, with optional repeat and cross-module support.
            - `type` (string) **REQ** [enum=[37 values]] — Represents the trigger API name that activates the workflow rule. Supported values vary by module; use the getWorkflowConfigurations endpoint to retrieve supported triggers for the target module.
            - `details` (object) — Represents the optional trigger configuration details, including **repeat** (Boolean) and **trigger_module** (object) for cross-module triggers.
              - `repeat` (boolean) — Indicates whether the rule fires every time the trigger condition is met. When false, the rule fires only on the first occurrence.
              - `trigger_module` (object `ModuleOrFieldNestedSchema`) — The module that actually triggers the rule. Defaults to the rule's top-level module if omitted. Must be explicitly set when the trigger targets a different module, such as a rule on Leads triggered by a note creation event, which requires the trigger module to reference the Notes module. To discover module API names and identifiers, retrieve the available modules from the system.
          - `ExecuteWhenT2FieldUpdate` — Represents a field update trigger type that fires when a specified field value on a record changes according to defined criteria.
            - `type` (string) **REQ** [enum=[6 values]] — Represents the trigger type for field update rules. Availability varies by the target module.
            - `details` (object) **REQ** — Represents the field update trigger details, including the criteria that define which field value change activates the rule.
              - `criteria` (object) **REQ** — Represents the field value change criteria that activate the trigger. Defines which field is monitored and what change condition fires the rule.
                oneOf:
                  - `WorkflowSimpleFilterCriterion` — Represents a simple filter criterion for workflow rule queries, specifying the field API name, comparator, and value to match.
                  - `WorkflowGroupedFilterCriterion` — Represents a grouped filter criterion containing multiple simple filter conditions evaluated together using a logical operator such as AND or OR.
              - `match_all` (boolean) — Controls the logic applied across criteria groups.
Possible values:
true - All criteria groups must match (AND logic).
false - Any one criteria group is sufficient (OR logic).
              - `repeat` (boolean) — Indicates whether the rule fires every time the field update condition is met. When false, the rule fires only on the first occurrence.
              - `trigger_module` (object `ModuleOrFieldNestedSchema`) — The module that actually triggers the rule. Defaults to the rule's top-level module if omitted. Must be explicitly set when the trigger targets a different module  - e.g., a rule on Leads triggered by 'note created' requires trigger_module = {api_name: 'Notes', id: '...'}. Use `getModules` to discover module api_name and id values.
          - `ExecuteWhenT3SectionUpdate` — Represents the trigger type for section update rules. Availability varies by the target module

            - `type` (string) **REQ** [enum=[4 values]] — Represents the trigger type for section update rules. Use getWorkflowConfigurations to verify the trigger is available for the target module.
            - `details` (object) **REQ** — Represents the section update trigger details, including the layout section IDs to monitor.
              - `section_ids` (array of string/int64) [minItems=1, maxItems=10] **REQ** — Represents the array of layout section IDs to monitor for updates. Each ID must correspond to a valid section ID for the target module.
              - `repeat` (boolean) — Indicates whether the rule fires every time a section update
condition is met. When false, the rule fires only on the first
occurrence.

              - `trigger_module` (object `ModuleOrFieldNestedSchema`) — Optional. The module that actually triggers the rule. Defaults to the rule's top-level module if omitted. Must be explicitly set when the trigger targets a different module  - e.g., a rule on Leads triggered by 'note created' requires trigger_module = {api_name: 'Notes', id: '...'}. Use `getModules` to discover module api_name and id values.
          - `ExecuteWhenT4DateBased` — Represents the date or datetime field to monitor for triggering the rule. Must reference an existing date or datetime field on the module.

            - `type` (string) **REQ** [enum=['date_or_datetime']] — Represents the trigger type for date or datetime-based rules, which fire relative to a date field value on the record.
            - `details` (object) **REQ** — Represents the date-based trigger details, including the target date field, time offset, and recurrence configuration.
              - `field` (object) **REQ** — Represents the date or datetime field to monitor for triggering the rule. Use the getFields endpoint to discover available date and datetime fields.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the date or datetime field, such as **Created_Time**, **Modified_Time**, or a custom field API name.
                - `id` (string) [maxLen=20] — Represents the unique ID of the date or datetime field.
              - `period` (string) **REQ** [enum=['minutes', 'hours', 'days', 'weeks', 'months', 'years', 'b_hours', 'b_days']] — Represents the time unit for the offset relative to the monitored date field. For example, **days**, **weeks**, or **months**.
              - `unit` (integer/int32) **REQ** — Represents the offset magnitude relative to the monitored date field value. Negative values indicate before the date; positive values indicate after.
              - `execute_at` (string/time) — Represents the exact time of day at which to fire the trigger, in 24-hour HH:mm format. Applicable only to datetime fields.
              - `recur_cycle` (string) [enum=['once', 'monthly', 'yearly']] — Represents the recurrence frequency for the date-based trigger.
Possible values:
once - Fires once.
monthly - Fires monthly on the same date.
yearly - Fires yearly on the same date.
              - `repeat` (boolean) — Indicates whether the trigger fires repeatedly. When true, the trigger fires on each recurrence as configured.
              - `trigger_module` (object `ModuleOrFieldNestedSchema`) — Specifies the module that triggers the workflow rule. If omitted,
it defaults to the rule's top-level module. Specify this when the trigger
targets a different module. For example, a workflow rule on Leads triggered
when a note is created requires 'trigger_module': {"api_name": "Notes",
'id': '...'}. Use 'getModules' to retrieve the module API name and ID.

          - `ExecuteWhenT5TimeOffset` — Represents the trigger type for time-offset rules. Availability varies by the target module.

            - `type` (string) **REQ** [enum=[7 values]] — Represents the trigger type for time-offset rules. Use getWorkflowConfigurations to verify the trigger is available for the target module.
            - `details` (object) **REQ** — Represents the time offset trigger details, including the time unit and magnitude for the offset.
              - `period` (string) **REQ** [enum=['days', 'hours']] — Represents the time unit for the offset.
Possible values:
days - Offset in days.
hours - Offset in hours.
              - `unit` (integer/int32) **REQ** — Represents the time offset magnitude. Always a positive integer for time-offset triggers, such as 1 for one day or 3 for three hours.
              - `trigger_module` (object `ModuleOrFieldNestedSchema`) — The module that actually triggers the rule. Defaults to
the rule's top-level module if omitted. Must be explicitly set
when the trigger targets a different module  - e.g., a rule on
Leads triggered by 'note created' requires trigger_module =
{api_name: 'Notes', id: '...'}. Use `getModules` to discover
module api_name and id values.

              - `field` (object) — Represents the field reference returned in GET responses for time-offset triggers, including the trigger field details.
                - `id` (string) [maxLen=20] — Represents the field identifier for the time-offset trigger. Returns **-1** when the field is system-determined.
          - `ExecuteWhenT6ScoreUpdate` — Represents a score update trigger type (T6) that fires when a record score changes due to configured scoring rules.
            - `type` (string) **REQ** [enum=['score_increase', 'score_decrease', 'score_update', 'zia_scoring_rule']] — Represents the trigger type for scoring rules. Supports score increase and score decrease trigger events.
            - `details` (object) **REQ** — Represents the score update trigger details, including the Scoring Rule scope and the applicable scoring rules.
              - `type` (string) **REQ** [enum=['All_Rules', 'Selective_Rules']] — Represents the trigger type for scoring rules. Supports score increase and score decrease trigger events.
              - `rules` (array of object) [minItems=1, maxItems=50] — Represents the array of Scoring Rule references to monitor. Required when **type** is set to **Selective_Rules**.
                - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the Scoring Rule.
                - `name` (string) [maxLen=255, readOnly] — Represents the display name of the Scoring Rule. This field is read-only and returned in GET responses.
              - `repeat` (boolean) — Indicates whether the rule fires every time the score condition is met. When false, the rule fires only on the first occurrence.
              - `trigger_module` (object `ModuleOrFieldNestedSchema`) — The module that actually triggers the rule. Defaults to the rule's top-level module if omitted. Must be explicitly set when the trigger targets a different module, such as a rule on Leads triggered by a note creation event, which requires the trigger module to reference the Notes module. To discover module API names and identifiers, retrieve the available modules from the system.
          - `ExecuteWhenT7EmailRepliedWithin` — Represents an email-reply-window trigger type (T7) that fires when a sent email receives a reply within a configured time window.
            - `type` (string) **REQ** [enum=['mail_sent_replied_within']] — Represents the trigger type for email-reply-window rules. Requires a dedicated email module workflow rule.
            - `details` (object) **REQ** — Represents the email-reply-window trigger details, including the time unit and magnitude for the reply window.
              - `period` (string) **REQ** [enum=['days', 'hours']] — Represents the time unit for the reply window.
Possible values:
days - Window measured in days.
hours - Window measured in hours.
              - `unit` (integer/int32) **REQ** — Represents the reply window magnitude, such as 3 for a window of three days or three hours.
              - `trigger_module` (object `ModuleOrFieldNestedSchema`) — The module that actually triggers the rule. Defaults to the rule's top-level module if omitted. Must be explicitly set when the trigger targets a different module  - e.g., a rule on Leads triggered by 'note created' requires trigger_module = {api_name: 'Notes', id: '...'}. Use `getModules` to discover module api_name and id values.
      - `editable` (boolean) **REQ** — Indicates whether the requesting user has permission to edit this workflow rule.
      - `module` (object `ModuleOrFieldNestedSchema`) **REQ** — Represents a CRM module or field reference using its API name and unique numeric ID.
      - `deprecated` (boolean) — Indicates whether this workflow rule is deprecated and should be migrated to a newer configuration.
      - `deletable` (boolean) **REQ** — Indicates whether the requesting user has permission to delete this workflow rule.
      - `description` (string) **REQ** [maxLen=255, nullable] — Represents the user-defined description of the workflow rule. Null if not set.
      - `source` (string) **REQ** [maxLen=255] — Represents the origin of the workflow rule. For example, **crm** for rules created through the CRM UI, or **API** for rules created through the API.
      - `created_by` (object `CreatedModifiedByObjectSchema`) **REQ** — Represents the identity details of the CRM user who created or last modified the workflow rule.
      - `last_executed_time` (string/date-time) **REQ** [nullable] — Represents the ISO 8601 timestamp of the last time this workflow rule was triggered. Null if the rule has never been triggered.
      - `modified_time` (string/date-time) **REQ** [maxLen=255, nullable] — Represents a time offset specification combining a period label and a numeric magnitude, used in time-based workflow trigger configurations.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the workflow rule.
      - `modified_by` (object `CreatedModifiedByObjectSchema`) **REQ** — Represents the identity details of the CRM user who created or last modified the workflow rule.
      - `lock` (object `LockStatusSchema`) **REQ** — Represents the lock configuration of a workflow rule, including the lock state and the identity of the user who applied the lock.
        schema: `LockStatusSchema`
        - `locked_by` (object) — Represents the details of the CRM user who locked the workflow rule.
          oneOf:
            - `LockedByObjectSchema` — Represents the identity of the CRM user who locked the workflow rule, including their display name and unique ID.
              - `name` (string/string) — Represents the name of the CRM user who locked the workflow rule.
              - `id` (string/string) — Represents the unique ID of the CRM user who locked the workflow rule.
              type: null — Represents a null value indicating the workflow rule is not currently locked by any user.
        - `message` (string/string) [nullable] — Represents the note or label indicating the reason or context for locking the rule.
        - `status` (boolean) — Indicates whether the workflow rule is locked.
Possible values:
true - The rule is locked.
false - The rule is not locked.
      - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the workflow rule.
      - `category` (string) [maxLen=255] — Represents the classification category of the workflow rule.
      - `conditions` (array of object `ConditionsNestedSchema`) [maxItems=10] — Represents the array of condition objects that define the criteria for executing the actions of the workflow rule.
        schema: `ConditionsNestedSchema`
        - `sequence_number` (integer/int32) **REQ** — Represents the execution order of this condition within the workflow rule, starting from one. Must be unique across all conditions in the rule.
        - `instant_actions` (object `InstantActionsNestedSchema`) — Actions to execute immediately when the condition is met. At least one of instant_actions or scheduled_actions must be present  - returns MANDATORY_NOT_FOUND if both are absent.
          schema: `InstantActionsNestedSchema`
          - `actions` (array of object) [maxItems=50] **REQ** — Represents the array of action objects configured for this condition. Required and must be non-empty. Each action object specifies the action type and its configuration or reference ID.
            oneOf:
              - `NonAssociateActionsNestedSchema` — Represents an inline action configuration that is defined directly within the workflow rule condition, rather than referencing a pre-created action entity by ID.
              - `AssociateActionsNestedSchema` — Represents an associate action that references a pre-configured action entity by its unique ID. Use the appropriate entity API to retrieve valid IDs.
        - `scheduled_actions` (array of object) [maxItems=5, nullable] — Actions to execute after a configured delay. Scheduled actions require both the trigger and the action type to support scheduling.
          - `execute_after` (object) — Defines the delay before the scheduled actions execute. Required. Cannot be an empty object.
            - `period` (string) **REQ** [enum=[8 values]] — Represents the type of time interval. Required. Must be one of the allowed period values (invalid_schedule_actions_period if invalid). business_hours and business_days are only available when org business hours are configured. The API returns available periods from getWorkflowConfigurations.
            - `unit` (integer/int32) **REQ** — Represents the numeric delay value. Required. Allowed ranges per period (unit_not_allowed_for_period if out of range): minutes: 5-180 (2-180 if 1-min repetition feature is enabled), hours: 0-99, days: 0-2000, weeks: 0-100, months: 0-24, years: 0-10, business_hours: 0-99, business_days: 0-2000. All values must be non-negative (no pre-event offsets for scheduled actions).
          - `actions` (array of object) [maxItems=50] **REQ** — Represents the array of action objects for this scheduled group. Uses the same associate and non-associate action structure as instant actions, but only action types that support scheduled execution are allowed. Per-type limits apply independently to instant and scheduled actions.

            oneOf:
              - `NonAssociateActionsNestedSchema` — Represents an inline action configuration that is defined directly within the workflow rule condition, rather than referencing a pre-created action entity by ID.
              - `AssociateActionsNestedSchema` — Represents an associate action that references a pre-configured action entity by its unique ID. Use the appropriate entity API to retrieve valid IDs.
          - `id` (string) [maxLen=20] — Represents unique Id of the scheduled action
        - `criteria_details` (object `CriteriaDetailsNestedSchema`) — Record matching criteria for this condition. When provided, criteria_details must be a JSON object and cannot be null. To match all records, pass an object with criteria set to null, but do not set criteria_details itself to null. This field is required for certain trigger types, such as related module triggers like Notes on Leads. The convert action type requires criteria_details.criteria to be a non-null filter object. Omit criteria_details entirely or pass criteria as null to match all records when the trigger does not require specific criteria and no convert action is present.
          schema: `CriteriaDetailsNestedSchema`
          - `criteria` (object) — Represents the filter criteria applied to the trigger module records. When null, the rule applies to all records without additional field-level filtering.
            oneOf:
              - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
              - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
                type: null — Represents a null variant indicating no criteria or module filter is applied.
          - `relational_criteria` (object) — Represents the filter criteria applied to a related module when the trigger involves cross-module data, such as emails, calls, or notes.
            - `criteria` (object) — Represents the filter criteria applied to the related module records. Follows the same structure as the top-level criteria field.
              oneOf:
                - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
                - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
                  type: null — Represents a null variant indicating no criteria or module filter is applied.
            - `module_selection` (string) [enum=['all', 'specific', 'unknown', None], nullable] — Represents the scope selector for the related module filter. Required when **relational_criteria** is present.
            - `module` (object) — Represents the related module to filter on. Required when **module_selection** is set to **specific**.
              oneOf:
                - `ModuleOrFieldNestedSchema` — Represents a CRM module or field reference using its API name and unique numeric ID.
                  type: null — Represents a null variant indicating no criteria or module filter is applied.
        - `id` (string/int64) — Represents the unique ID of the condition. Auto-generated on creation. Required on PUT to identify which condition to update.
        - `_delete` (null) — Indicates that this condition should be removed from the workflow rule when set in a PUT request. Provide a null value to signal deletion.
      - `status` (object `ActivationStatusSchema`) **REQ** — Represents the activation state of a workflow rule, indicating whether the rule is currently active.
        schema: `ActivationStatusSchema`
        - `active` (boolean) — Indicates whether the workflow rule is currently active.

Possible values:
true - The workflow rule is active and executes its configured actions when trigger conditions are met.
false - The workflow rule is inactive and does not execute, even when trigger conditions are met.

- **204**: Returns a successful response with no content.


- **403**: The user does not have permission to access this API.
**Resolution:** A Zoho CRM administrator must grant the user the required profile permissions to access workflow rules. — Schema: `NoPermissionSchema` [application/json]
    > Represents the error response returned when the authenticated user does not have permission to access the requested feature or module.
    schema: `NoPermissionSchema`
    - `code` (string) **REQ** [enum=['NO_PERMISSION', 'FEATURE_NOT_SUPPORTED']] — Represents the error code that identifies the specific error condition.
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the response status for the error, typically **error**.
    - `details` (object) **REQ** — Represents error details. For NO_PERMISSION, contains the list of permissions needed. For FEATURE_NOT_SUPPORTED, empty object.
      - `permissions` (array of string) [maxItems=10] — Represents the list of CRM profile permissions required to perform the requested action.
        items: [maxLen=255]

**Scopes:** ZohoCRM.settings.workflow_rules.READ

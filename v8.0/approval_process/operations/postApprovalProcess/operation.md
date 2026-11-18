# POST /settings/approval_process
**Operation:** `postApprovalProcess` — Create Approval Process
> To create an Approval Process in your Zoho CRM organization.

**Schemas:**
`ApproverNotificationChannelAlt1`:
  > Notification settings for informing approvers.
  - `feed` (boolean) **REQ** — Defines whether the update needs to be sent through feeds. (Required)
  - `email` (boolean) **REQ** — Defines whether an Email notification needs to be sent. (Required)
`CliqFieldRef`:
  > Reference to a module field by ID for Cliq notification recipient resolution.
  - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=^[0-9]+$] — Field ID.
`CliqNotificationDetails`:
  > Holds the details for cliq_notifications actions.
  - `message` (string) **REQ** [maxLen=2000] — Message content of the Cliq notification.
  - `notify_to` (object `CliqNotifyTo`) **REQ** — Recipient of the Cliq notification.
`CliqNotifyFields`:
  > Dynamic and static fields for recipient resolution.
  - `fields` (array of object `CliqFieldRef`) [maxItems=100, nullable] — Dynamic field references for recipient resolution.
  - `static_fields` (array of object `CliqStaticFieldRef`) [maxItems=50, nullable] — Static role-based field names (e.g. owner_manager).
`CliqNotifyModule`:
  > Module from which recipient fields are resolved.
  - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=^[0-9]+$] — Module ID.
`CliqNotifyTo`:
  oneOf:
    - `CliqNotifyToUser` — Recipient is a specific user identified by user ID.
    - `CliqNotifyToChannel` — Recipient is a Cliq channel identified by channel ID.
    - `CliqNotifyToFields` — Recipients dynamically resolved from module fields and static role-based fields.
`CliqNotifyToChannel`:
  > Recipient is a Cliq channel identified by channel ID.
  - `id` (string) **REQ** [maxLen=255] — Channel ID.
  - `name` (string) [maxLen=255, nullable] — Channel display name.
  - `type` (string) **REQ** [enum=['channel']] — Recipient type. Must be channel.
`CliqNotifyToFields`:
  > Recipients dynamically resolved from module fields and static role-based fields.
  - `module` (object `CliqNotifyModule`) **REQ** — Module from which recipient fields are resolved.
  - `notify_fields` (object `CliqNotifyFields`) — Dynamic and static fields for recipient resolution.
  - `type` (string) **REQ** [enum=['fields']] — Recipient type. Must be fields.
`CliqNotifyToUser`:
  > Recipient is a specific user identified by user ID.
  - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=^[0-9]+$] — User ID.
  - `name` (string) [maxLen=255, nullable] — User display name.
  - `type` (string) **REQ** [enum=['user']] — Recipient type. Must be user.
`CliqStaticFieldRef`:
  > Reference to a static role-based field by name for Cliq recipient resolution.
  - `name` (string) **REQ** [maxLen=100] — Static field name (e.g. owner_manager).
`CreateActionDetailsAlt1`:
  > Holds the details for create_record actions.
  - `layout` (object `CreateActionLayoutRefAlt1`) **REQ** — Defines layout for new record creation. (Required)
  - `field_mappings` (array of object `CreateActionFieldMappingAlt1`) [maxItems=500] **REQ** — Defines the field mapping of the configured module. (Required)
  - `module` (object `CreateActionModuleRefAlt1`) **REQ** — Module of the create record action. (Required)
`CreateActionFieldMappingAlt1`:
  > Maps a target field to a static value or merge field for create-record actions.
  - `field` (object `CreateActionFieldRefAlt1`) **REQ** — Details of the field. (Required)
  - `type` (string) **REQ** [maxLen=20, enum=['static', 'merge_field']] — Defines the type of value for the field. (Required)
  - `value` (string) **REQ** [maxLen=4] — Value for the field. (Required)
`CreateActionFieldRefAlt1`:
  > Field used for evaluation
  - `api_name` (string) [maxLen=200, pattern=^[A-Za-z][A-Za-z0-9_]*$, nullable] — API name of the field
  - `id` (string) [maxLen=25, nullable] — Id of the field
`CreateActionLayoutRefAlt1`:
  > Defines layout for new record creation. (Required)
  - `name` (string) [maxLen=200, nullable] — Name of the layout.
  - `id` (string/int64) [maxLen=25, minLen=1, pattern=^[0-9]{1,19}$, nullable] — Id of the layout.
`CreateActionModuleRefAlt1`:
  > Module the approval process applies to. (Required)
  - `api_name` (string) [maxLen=200, nullable] — Module API name
  - `id` (string) [maxLen=25, nullable] — Id of the module.
`EditableFieldRefAlt3`:
  > Represents a field permitted for modification, identified by API name and ID.
  - `api_name` (string) [maxLen=25, pattern=^[A-Za-z][A-Za-z0-9_]*$, nullable] — api name of the field.
  - `id` (string) [maxLen=25, nullable] — Id of the field.
`ParallelApprovalOrderActions`:
  > Maps an approval order to the set of actions for stages when the approver type is everyone-parallel.
  - `approval_order` (integer/int32) **REQ** — This defines the approval order. (Required) (Unique)
  - `actions` (array of object `WorkflowActionRef`) [maxItems=10] **REQ** — Actions that are to be executed. (Required)
`PendingApprovalEditPolicyAlt1`:
  > Controls edit permissions while the record is awaiting approval. (Required)
  - `fields` (array of object `EditableFieldRefAlt3`) [maxItems=2, nullable] — List of fields allowed for modification when specific_fields is selected.
  - `update_allowed_for` (string) **REQ** [maxLen=50, enum=['no_fields', 'all_fields', 'specific_fields']] — Controls edit permissions while the record is awaiting approval. (Required)
`PostApprovalWorkflowActionAlt1`:
  oneOf:
      - `name` (string) [maxLen=200, nullable] — Name of the action.
      - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=^[0-9]+$] — Id of the action which needs to be executed. (Required)
      - `type` (string) **REQ** [maxLen=50, enum=['tasks']] — Type of the action which needs to be executed. (Required)
      - `name` (string) [maxLen=200, nullable] — Name of the action.
      - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=^[0-9]+$] — Id of the action which needs to be executed. (Required)
      - `type` (string) **REQ** [maxLen=50, enum=['functions']] — Type of the action which needs to be executed. (Required)
      - `name` (string) [maxLen=200, nullable] — Name of the action.
      - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=^[0-9]+$] — Id of the action which needs to be executed. (Required)
      - `type` (string) **REQ** [maxLen=50, enum=['webhooks']] — Type of the action which needs to be executed. (Required)
      - `name` (string) [maxLen=200, nullable] — Name of the action.
      - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=^[0-9]+$] — Id of the action which needs to be executed. (Required)
      - `type` (string) **REQ** [maxLen=50, enum=['email_notifications']] — Type of the action which needs to be executed. (Required)
      - `name` (string) [maxLen=200, nullable] — Name of the action.
      - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=^[0-9]+$] — Id of the action which needs to be executed. (Required)
      - `type` (string) **REQ** [maxLen=50, enum=['field_updates']] — Type of the action which needs to be executed. (Required)
      - `name` (string) [maxLen=200, nullable] — Name of the action.
      - `details` (object `CreateActionDetailsAlt1`) **REQ** — Holds the details for create_record actions.
      - `type` (string) **REQ** [maxLen=50, enum=['create_record']] — Type of the action which needs to be executed. (Required)
      - `name` (string) [maxLen=200, nullable] — Name of the action.
      - `details` (object `CliqNotificationDetails`) **REQ** — Holds the details for cliq_notifications actions.
      - `type` (string) **REQ** [maxLen=50, enum=['cliq_notifications']] — Type of the action which needs to be executed. (Required)
`RejectionEditPolicyAlt1`:
  > Controls which fields can be updated after the approval has been rejected. (Required)
  - `fields` (array of object `EditableFieldRefAlt3`) [maxItems=2, nullable] — List of fields allowed for modification when specific_fields is selected.
  - `update_allowed_for` (string) **REQ** [maxLen=50, enum=['no_fields', 'all_fields', 'specific_fields']] — Specifies edit permissions once the record is rejected. (Required)
`StageOnApproveAction`:
  > Defines actions executed when a record is approved at a stage.
  - `name` (string) [maxLen=25, nullable] — Name of the action.
  - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=^[0-9]+$] — Id of the action which needs to be executed. (Required)
  - `type` (string) **REQ** [maxLen=50, enum=['field_updates']] — Type of the action which needs to be executed. (Required)
`WorkflowActionRef`:
  > Represents an action to execute within the approval process, identified by ID, name, and type.
  - `name` (string) [maxLen=200, nullable] — Name of the action.
  - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=^[0-9]+$] — Id of the action. (Required)
  - `type` (string) **REQ** [maxLen=20, enum=['field_updates']] — action type which needs to be executed. (Required)

**Request Body** — application/json `ApprovalProcessCollectionPayload`
> The request body must contain an **approval_process** array with one object.
  > Request payload containing a list of approval processes to create or update.
  - `approval_process` (array of object `ApprovalProcessDefinition`) [maxItems=1] **REQ** — List of approval processes to create/update. (Required)
    schema: `ApprovalProcessDefinition`
    - `sequence_number` (integer/int32) [readOnly, nullable] — Defines ordering of the approval process.
    - `module` (object `CreateActionModuleRefAlt1`) **REQ** — Module the approval process applies to. (Required)
    - `name` (string) **REQ** [maxLen=200] — Name of the approval process. (Required)
    - `description` (string) [maxLen=3000, nullable] — Description of the approval process.
    - `active` (boolean) **REQ** — Approval process activate or deactivate status. (Required)
    - `generated_type` (string) [maxLen=50, enum=['custom', 'internal'], nullable] — Defines the process creation type:
custom - User-created
internal - System-generated
    - `rules` (array of object `ApprovalRuleDefinition`) [maxItems=5, nullable] — Each rule defines the logic, approvers, and actions.
      schema: `ApprovalRuleDefinition`
      - `sequence_number` (integer/int32) [readOnly, nullable] — Execution order of the rule.
      - `actions_per_approval` (array of object `ParallelApprovalOrderActions`) [maxItems=10, nullable] — This defines the actions to be executed on each order of approval stages for everyone parallel approver type.
      - `overall_approval_type` (string) **REQ** [maxLen=50, enum=['anyone', 'everyone_parallel', 'everyone_sequential']] — Type of approval execution i.e., anyone, everyone parallel or everyone sequential (Required)
      - `criteria` (object `ApprovalRuleCriteria`) **REQ** — Criteria for executing the rule. (Required)
        schema: `ApprovalRuleCriteria`
        - `comparator` (string) [maxLen=5, nullable] — Condition operator, e.g., equal, not_equal
        - `field` (object `CreateActionFieldRefAlt1`) — Field used for evaluation
        - `value` (string) [maxLen=9, nullable] — value of the field.
      - `name` (string) **REQ** [maxLen=200] — Name of the rule. (Required)
      - `process_admin_configuration` (object `ProcessAdminSettings`) — Permissions and behavior assigned to process administrators.
        schema: `ProcessAdminSettings`
        - `notify_original_approvers_via` (object `ApproverNotificationChannelAlt1`) — Notification settings for informing approvers.
        - `process_admin` (array of object `ProcessAdministratorEntry`) [minItems=1, maxItems=50] **REQ** — List of process admins based on specific user types. (Required)
          schema: `ProcessAdministratorEntry`
          - `resources` (array of object `AdminEntityRef`) [minItems=1, maxItems=50] **REQ** — Details of the resource. (Required)
            schema: `AdminEntityRef`
            - `name` (string) [maxLen=200, nullable] — Name of the resource.
            - `id` (string/int64) **REQ** [maxLen=25, minLen=1, pattern=^[0-9]+$] — Id of the users or groups or roles. (Required)
          - `type` (string) **REQ** [maxLen=50, enum=['users']] — type of the resource. (Required)
        - `record_modification` (object `AdminEditPolicy`) **REQ** — Defines record editing permissions for the process administrators during waiting and after rejection across all stages. (Required)
          schema: `AdminEditPolicy`
          - `update_allowed_for` (string) **REQ** [maxLen=50, enum=['all_fields', 'no_fields', 'approver_stages_record_modification_fields']] — Specifies which fields can be updated during approval. (Required)
      - `actions_upon_final_approval` (object `FinalApprovalAutomation`) — Automation triggers after the entire approval process is completed successfully.
        schema: `FinalApprovalAutomation`
        - `send_default_emails_enabled` (boolean) [nullable] — Defines whether default approval completion email notifications needs to be sent or not.
        - `actions` (array of object `PostApprovalWorkflowActionAlt1`) [maxItems=500, nullable] — List of workflow actions to perform after final approval.
      - `actions_upon_rejection` (object `RejectionAutomation`) — Actions to be executed when a record is rejected.
        schema: `RejectionAutomation`
        - `notify_original_approvers_via` (object `ApproverNotificationChannelAlt1`) — Notification settings for informing previously approved approvers.
        - `rejection_type` (string) [maxLen=50, enum=['all_previous_stages', 'current_stage', 'current_approver_decide'], nullable] — Determines how far the rejection rolls back the approval chain which only applies if the approval type is everyone_sequential.
        - `actions` (array of object `PostApprovalWorkflowActionAlt1`) [maxItems=500, nullable] — Automation triggers after a record in the approval process is rejected.
      - `overall_stages_record_modification` (object `CrossStageEditPolicy`) — Defines allowed fields for editing in a record during waiting & after rejection.
        schema: `CrossStageEditPolicy`
        - `during_approval_waiting` (object `PendingApprovalEditPolicyAlt1`) **REQ** — Controls edit permissions while the record is awaiting approval. (Required)
        - `after_record_rejection` (object `RejectionEditPolicyAlt1`) **REQ** — Controls which fields can be updated after the approval has been rejected. (Required)
      - `approver_stages` (array of object `ApprovalStageDefinition`) [maxItems=10] **REQ** — Represents the multi-stage approval. Each stage includes an approver and associated actions. (Required)
        schema: `ApprovalStageDefinition`
    - `execute_on` (string) **REQ** [maxLen=50, enum=['create', 'edit', 'create_or_edit']] — Specifies when the approval triggers:
create
edit
create_or_edit (Required)

**Responses:**

- **201**: Returns the result of the Approval Process create request, including the status, message, and ID of the created process. — Schema: `ApprovalProcessAcceptedResponse` [application/json]
    > Success response indicating approval process creation accepted, returning result items for each submitted process.
    schema: `ApprovalProcessAcceptedResponse`
    - `approval_process` (array of object `ApprovalProcessCreateResultItem`) [maxItems=1] — Field: approval_process
      schema: `ApprovalProcessCreateResultItem`
      - `code` (string) [maxLen=255] — Field: code
      - `details` (object `ApprovalProcessCreateDetails`) — Contains identifiers and related information returned after creating an approval process.
        schema: `ApprovalProcessCreateDetails`
        - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
      - `message` (string) [maxLen=255] — Field: message
      - `status` (string) [maxLen=255] — Field: status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed due to invalid syntax.
**Resolution:** The request must contain valid values for the fields identified in the response. [application/json]
    > Represents the error response returned when the Approval Process create request is invalid.
    oneOf:
        - `approval_process` (array of object) [maxItems=25] **REQ** — Contains error objects that describe validation failures in the Approval Process create request.
          oneOf:
            - `ApprovalProcessNameMissingError` — Validation error indicating the process name was not provided in the input.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['approval process name is missing']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ApprovalProcessNameLengthError` — Validation error indicating the process name exceeds the allowed length.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `maximum_length` (integer/int32) — Detail field: maximum_length
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['The lenght of name has exceeded the limit']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InactiveProcessCreationNotAllowedError` — Business rule error preventing creation of an approval process in inactive state.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Can not create inactive rule']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InvalidModuleApiNameError` — Validation error indicating the provided module API name is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['the tabName given seems to be invalid']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ExecuteOnMissingError` — Validation error indicating the execute_on field was not provided.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['The required data missing']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ExecuteOnInvalidValueError` — Validation error indicating an invalid value was provided for execute_on.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
                - `supported_values` (array of string) [maxItems=25] — Detail field: supported_values
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['invalid data']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ActiveProcessLimitExceededError` — Limit error indicating the maximum number of active approval processes has been exceeded.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `limit` (integer/int32) — Detail field: limit
                - `limit_due_to` (array of object) [maxItems=25] — Detail field: limit_due_to
                  - `api_name` (string) [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path
              - `message` (string) **REQ** [enum=['active approval processes limit exceeded']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `RuleNameMissingError` — Validation error indicating the rule name was not provided.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['The rule name is missing']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `RuleNameLengthExceededError` — Validation error indicating the rule name exceeds the allowed length.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `maximum_length` (integer/int32) — Detail field: maximum_length
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['The length of name has exceeded the limit']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InvalidRuleCriteriaError` — Validation error indicating the provided rule criteria is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['The given criteria seems to be invalid']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `OverallRecordModificationTypeMismatchError` — Configuration error indicating overall_stages_record_modification applies only to 'anyone' or 'everyone_parallel'.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `dependee` (object) — Detail field: dependee
                  - `api_name` (string) [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=[1 values]] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `StageRecordModificationTypeMismatchError` — Configuration error indicating stage-level record_modification applies only to 'everyone_sequential'.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `dependee` (object) — Detail field: dependee
                  - `api_name` (string) [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['stage record_modification is applicable for everyone_sequential']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ApproverStageLimitExceededError` — Limit error indicating the number of approver stages exceeds the allowed maximum.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `limit` (integer/int32) — Detail field: limit
                - `limit_due_to` (array of object) [maxItems=25] — Detail field: limit_due_to
                  - `api_name` (string) [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path
              - `message` (string) **REQ** [enum=['approver stage limit exceeded']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ApproverTypeUnsupportedDataTypeError` — Validation error indicating an unsupported data type was provided for approver type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `expected_data_type` (string) [maxLen=255] — Detail field: expected_data_type
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['data type not supported']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ApproverTypeInvalidValueError` — Validation error indicating an invalid value was provided for approver type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
                - `supported_values` (array of string) [maxItems=25] — Detail field: supported_values
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['invalid data is given for type']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessInvalidDataErrorResponse11` — invalid group approver id
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['the given group details seems to be invalid']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessInvalidDataErrorResponse12` — invalid role approver id
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['the given role details seems to be invalid']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ApproverLevelMissingError` — Dependency error indicating the level value is missing when levels are configured as approver type.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `dependee` (object) — Detail field: dependee
                  - `api_name` (string) [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Dependent Field missing']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InvalidApproverLevelError` — Validation error indicating the provided approver level is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
                - `range` (object) — Detail field: range
                  - `from` (integer/int32) — Nested detail field: from
                  - `to` (integer/int32) — Nested detail field: to
              - `message` (string) **REQ** [enum=['invalid approver level given']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `FieldIdentifierAmbiguityError` — Error indicating a mismatch between provided field ID and API name caused ambiguity.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `ambiguity_due_to` (array of object) [maxItems=25] — Detail field: ambiguity_due_to
                  - `api_name` (string) [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path
              - `message` (string) **REQ** [enum=['The field api name seems to be invalid', 'given api_name and id not matched']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ApproverLevelDependencyMissingError` — Dependency error requiring either level or level_up_to when approver type is levels.
              - `code` (string) **REQ** [enum=['EXPECTED_DEPENDENT_FIELD_MISSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `dependee` (object) — Detail field: dependee
                  - `api_name` (string) [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path
                - `expected_fields` (array of object) [maxItems=25] — Detail field: expected_fields
                  - `api_name` (string) [maxLen=255] — Nested detail field: api_name
              - `message` (string) **REQ** [enum=['expected dependent field missing']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `OverallEditPolicySectionMissingError` — Configuration error requiring at least one of during_approval_waiting or after_record_rejection under overall_stages_record_modification.
              - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `expected_fields` (array of object) [maxItems=25] — Detail field: expected_fields
                  - `api_name` (string) [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path
              - `message` (string) **REQ** [enum=['Specify atleast one field']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `DuplicateLevelInRequestError` — Uniqueness error indicating the same level value was used more than once within the same request.
              - `code` (string) **REQ** [enum=['ALREADY_USED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `exists_in` (object) — Detail field: exists_in
                  - `api_name` (string) [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['The data is already given in the same request under different key']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `TeamUserNotFoundError` — Validation error indicating the specified team user ID is not available in the given team module.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['team user is not available in the given team module']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `TeamUserApproverTypeNotAllowedError` — Policy error indicating team_user approver type is only applicable to team modules.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['team user is applicable for only team module']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `TeamUserNotAllowedForUsersApproverError` — Policy error indicating a team user cannot be assigned when approver type is users.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['team user cannot be added for users approver type']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ApproverTypeModuleNotSupportedError` — Policy error indicating the selected approver type is only supported for team modules.
              - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['approver type is applicable for only team module']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InvalidProfileReferenceError` — Validation error indicating the provided profile details are invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['the given profile details seems to be invalid']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProfileNotTeamTypeError` — Policy error indicating the given profile does not belong to the required team profile type.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['the given profile details does not belong to team profile type']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `DuplicateApprovalOrderError` — Uniqueness error indicating the approval_order value is duplicated.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=[2 values]] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `GenericMandatoryFieldMissingError` — Generic error indicating one or more required fields are missing.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Required field is missing']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `GenericInvalidDataTypeError` — Generic validation error indicating an invalid data type was provided.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `expected_data_type` (string) [maxLen=255] — Detail field: expected_data_type
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Invalid data type']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `GenericInvalidDataError` — Generic validation error indicating invalid data was provided.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `maximum_length` (integer/int32) — Detail field: maximum_length
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Invalid data']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `GenericExpectedFieldMissingError` — Generic validation error indicating one of the required fields is missing.
              - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `expected_fields` (array of object) [maxItems=25] — Detail field: expected_fields
                  - `api_name` (string) [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path
                - `index` (integer/int32) — Zero-based index of the approval_process item that triggered the error
              - `message` (string) **REQ** [enum=['One of the required fields is missing']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `GenericInvalidDataErrorAlt1` — Generic validation error indicating invalid data was provided.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
                - `supported_values` (array of string) [maxItems=25] — Detail field: supported_values
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['Invalid data']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `GenericDependentFieldMissingError` — Generic validation error indicating a dependent field is missing.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `dependee` (object) — Detail field: dependee
                  - `api_name` (string) [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['Dependent field is missing']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `GenericInvalidDataErrorAlt2` — Generic validation error indicating invalid data was provided.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
                - `minimum_length` (integer/int32) — Detail field: minimum_length
              - `message` (string) **REQ** [enum=['Invalid data']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `BasedOnFieldInvalidDataError1` — Validation error indicating an invalid data was provided for based_on_field.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['the fieldId given seems to be invalid']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessDependentMismatchErrorResponse1` — approval order field value greater than the given approver stages count
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `dependee` (object) **REQ** — Detail field: dependee
                  - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
                - `maximum_length` (integer/int32) **REQ** — Detail field: maximum_length
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['dependent mismatch']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessAlreadyExistsErrorResponse1` — Duplicate sequence_number is given
              - `code` (string) **REQ** [enum=['ALREADY_EXISTS']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `exists_in` (object) — Detail field: exists_in
                  - `api_name` (string) [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) [maxLen=1000] — Nested detail field: json_path
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['duplicate sequence number']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessLimitExceededErrorResponse1` — if actions value in the actions per approval given more than the allowed limit
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `limit` (integer/int32) **REQ** — Detail field: limit
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['limit exceeded']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessInvalidDataErrorResponse5` — This error occurs when the provided rule id is invalid or it is not existing in the given approval process id
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['given action id not found']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessInvalidDataErrorResponse7` — This error occurs when the provided rule id is invalid or it is not existing in the given approval process id
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
                - `range` (object) — Detail field: range
                  - `from` (integer/int32) — Nested detail field: from
                  - `to` (integer/int32) — Nested detail field: to
              - `message` (string) **REQ** [enum=['invalid sequence number']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ActionsLimitExceededError` — Actions limit exceeded error
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Error code
              - `details` (object) **REQ** — Error details
                - `api_name` (string) **REQ** [maxLen=255] — api_name
                - `limit` (integer/int32) **REQ** — limit
                - `json_path` (string) **REQ** [maxLen=1000] — json_path
              - `message` (string) **REQ** [enum=['actions limit exceeded']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `InvalidDataWithSupportedValuesError` — Validation error indicating an invalid value was provided with supported values list.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details
                - `api_name` (string) [maxLen=255] — api_name
                - `json_path` (string) [maxLen=1000] — json_path
                - `supported_values` (array of string) [maxItems=25] — supported_values
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['INVALID_DATA']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ActionsPerApprovalNonLevelTypeError` — when actions_per_approval is given for non level approver type
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `dependee` (object) **REQ** — Detail field: dependee
                  - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['dependent mismatch']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ActionsPerApprovalLevelUpToMissingError` — when actions_per_approval is given for level approver type but level_up_to key missing
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `dependee` (object) **REQ** — Detail field: dependee
                  - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
                - `api_name` (string) **REQ** [maxLen=255] — Detail field: api_name
                - `json_path` (string) **REQ** [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['dependent field missing']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ApproverLevelAndLevelUpToConflictError` — when both level and level_up_to key is present in the request for level approver type
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Detail field: ambiguity_due_to
                  - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
              - `message` (string) **REQ** [enum=['Ambiguity while processing the request']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
      - `ApprovalProcessPayloadTypeError` — Validation error indicating an invalid data type was provided for the approval_process field.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `maximum_length` (integer/int32) — Detail field: maximum_length
          - `api_name` (string) [maxLen=255] — Detail field: api_name
          - `json_path` (string) [maxLen=1000] — Detail field: json_path
        - `message` (string) **REQ** [enum=['invalid data']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied.
**Resolution:** The CRM administrator must grant the Manage Automation permission to the user's profile. — Schema: `ApprovalProcessPermissionDeniedErrorResponse` [application/json]
    > Permission denied is thrown if user doesn't have permission for Manage automation.
    schema: `ApprovalProcessPermissionDeniedErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code
    - `details` (object) **REQ** — Error details with validation information
      - `permissions` (array of string) [maxItems=25] — Detail field: permissions
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.approval_process.CREATE

# PUT /settings/approval_process/{approvalProcessId}
**Operation:** `putSingleApprovalProcess` — Update Approval Process
> To update the configuration of a single Approval Process in your Zoho CRM organization.

**Parameters:**
- `approvalProcessId` (path, string/int64, required) [maxLen=255, minLen=1, pattern=^[0-9]+$]: The unique identifier of the approval process to clone

**Request Body** — application/json `PutSingleApprovalProcessRequest`
> The request body must contain an approval_process array with one object.
  > Request body schema
  - `approval_process` (array of object `ApprovalProcessPutRequestSchema2`) [maxItems=1] **REQ** — a (Required)
    schema: `ApprovalProcessPutRequestSchema2`
    - `sequence_number` (integer/int32) — Field: sequence_number
    - `module` (object `ModuleBase`) **REQ** — Base schema for module
      schema: `ModuleBase`
      - `api_name` (string) [maxLen=255] — Field: api_name
      - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
      additionalProperties: any
    - `name` (string) **REQ** [maxLen=255] — Field: name
    - `description` (string) [maxLen=255] — Field: description
    - `active` (boolean) **REQ** — Field: active
    - `generated_type` (string) [maxLen=255] — Field: generated_type
    - `rules` (array of object `RulesitemBase`) [maxItems=10] — Field: rules
      schema: `RulesitemBase`
      - `sequence_number` (integer/int32) — Field: sequence_number
      - `actions_per_approval` (array of object `ActionsPerApprovalitemBase`) [maxItems=10] — Field: actions_per_approval
        schema: `ActionsPerApprovalitemBase`
        - `approval_order` (integer/int32) — Field: approval_order
        - `actions` (array of object `ActionsitemBase`) [maxItems=25] — Field: actions
          schema: `ActionsitemBase`
          - `name` (string) [maxLen=255] — Field: name
          - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
          - `type` (string) [maxLen=255] — Field: type
          additionalProperties: any
        additionalProperties: any
      - `overall_approval_type` (string) [maxLen=255] — Field: overall_approval_type
      - `criteria` (object `CriteriaBase`) — Base schema for criteria
        schema: `CriteriaBase`
        - `comparator` (string) [maxLen=255] — Field: comparator
        - `field` (object `FieldBase`) — Base schema for field
          schema: `FieldBase`
          - `api_name` (string) [maxLen=255, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Field: api_name
          - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
          additionalProperties: any
        - `value` (string) [maxLen=255] — Field: value
        additionalProperties: any
      - `name` (string) [maxLen=255] — Field: name
      - `process_admin_configuration` (object `ProcessAdminConfigurationBase`) — Base schema for process_admin_configuration
        schema: `ProcessAdminConfigurationBase`
        - `notify_original_approvers_via` (object `NotifyOriginalApproversViaBase`) — Base schema for notify_original_approvers_via
          schema: `NotifyOriginalApproversViaBase`
          - `feed` (boolean) — Field: feed
          - `email` (boolean) — Field: email
          additionalProperties: any
        - `process_admin` (array of object `ProcessAdminitemBase`) [maxItems=25] — Field: process_admin
          schema: `ProcessAdminitemBase`
          - `resources` (array of object `ResourcesitemBase`) [maxItems=25] — Field: resources
            schema: `ResourcesitemBase`
            - `name` (string) [maxLen=255] — Field: name
            - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
            additionalProperties: any
          - `type` (string) [maxLen=255] — Field: type
          additionalProperties: any
        - `record_modification` (object `RecordModificationBase1`) — Base schema for record_modification
          schema: `RecordModificationBase1`
          - `update_allowed_for` (string) [maxLen=255] — Field: update_allowed_for
          additionalProperties: any
        additionalProperties: any
      - `actions_upon_final_approval` (object `ActionsUponFinalApprovalBase`) — Base schema for actions_upon_final_approval
        schema: `ActionsUponFinalApprovalBase`
        - `send_default_emails_enabled` (boolean) — Field: send_default_emails_enabled
        - `actions` (array of object `ActionsitemBase1`) [maxItems=25] — Field: actions
          schema: `ActionsitemBase1`
          - `name` (string) [maxLen=255] — Field: name
          - `details` (object `DetailsBase`) — Base schema for details
            schema: `DetailsBase`
            - `layout` (object `LayoutBase`) — Base schema for layout
              schema: `LayoutBase`
              - `name` (string) [maxLen=255] — Field: name
              - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]{1,19}$] — Field: id
              additionalProperties: any
            - `field_mappings` (array of object `FieldMappingsitemBase`) [maxItems=25] — Field: field_mappings
              schema: `FieldMappingsitemBase`
              - `field` (object `FieldBase2`) — Base schema for field
                schema: `FieldBase2`
                - `api_name` (string) [maxLen=255, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Field: api_name
                - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
                additionalProperties: any
              - `type` (string) [maxLen=255] — Field: type
              - `value` (string) [maxLen=255] — Field: value
              additionalProperties: any
            - `module` (object `ModuleBase1`) — Base schema for module
              schema: `ModuleBase1`
              - `api_name` (string) [maxLen=255] — Field: api_name
              - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
              additionalProperties: any
            additionalProperties: any
          - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
          - `type` (string) [maxLen=255] — Field: type
          additionalProperties: any
        additionalProperties: any
      - `actions_upon_rejection` (object `ActionsUponRejectionBase`) — Base schema for actions_upon_rejection
        schema: `ActionsUponRejectionBase`
        - `notify_original_approvers_via` (object `NotifyOriginalApproversViaBase1`) — Base schema for notify_original_approvers_via
          schema: `NotifyOriginalApproversViaBase1`
          - `feed` (boolean) — Field: feed
          - `email` (boolean) — Field: email
          additionalProperties: any
        - `rejection_type` (string) [maxLen=255] — Field: rejection_type
        - `actions` (array of object `ActionsitemBase2`) [maxItems=25] — Field: actions
          schema: `ActionsitemBase2`
          - `name` (string) [maxLen=255] — Field: name
          - `details` (object `DetailsBase1`) — Base schema for details
            schema: `DetailsBase1`
            - `layout` (object `LayoutBase1`) — Base schema for layout
              schema: `LayoutBase1`
              - `name` (string) [maxLen=255] — Field: name
              - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]{1,19}$] — Field: id
              additionalProperties: any
            - `field_mappings` (array of object `FieldMappingsitemBase1`) [maxItems=25] — Field: field_mappings
              schema: `FieldMappingsitemBase1`
              - `field` (object `FieldBase3`) — Base schema for field
                schema: `FieldBase3`
                - `api_name` (string) [maxLen=255, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Field: api_name
                - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
                additionalProperties: any
              - `type` (string) [maxLen=255] — Field: type
              - `value` (string) [maxLen=255] — Field: value
              additionalProperties: any
            - `module` (object `ModuleBase2`) — Base schema for module
              schema: `ModuleBase2`
              - `api_name` (string) [maxLen=255] — Field: api_name
              - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
              additionalProperties: any
            additionalProperties: any
          - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
          - `type` (string) [maxLen=255] — Field: type
          additionalProperties: any
        additionalProperties: any
      - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
      - `overall_stages_record_modification` (object `OverallStagesRecordModificationBase`) — Base schema for overall_stages_record_modification
        schema: `OverallStagesRecordModificationBase`
        - `during_approval_waiting` (object `DuringApprovalWaitingBase`) — Base schema for during_approval_waiting
          schema: `DuringApprovalWaitingBase`
          - `update_allowed_for` (string) [maxLen=255] — Field: update_allowed_for
          - `fields` (array of object `FieldsitemBase`) [maxItems=25] — Field: fields
            schema: `FieldsitemBase`
            - `api_name` (string) [maxLen=255, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Field: api_name
            - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
            additionalProperties: any
          additionalProperties: any
        - `after_record_rejection` (object `AfterRecordRejectionBase`) — Base schema for after_record_rejection
          schema: `AfterRecordRejectionBase`
          - `update_allowed_for` (string) [maxLen=255] — Field: update_allowed_for
          - `fields` (array of object `FieldsitemBase1`) [maxItems=25] — Field: fields
            schema: `FieldsitemBase1`
            - `api_name` (string) [maxLen=255, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Field: api_name
            - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
            additionalProperties: any
          additionalProperties: any
        additionalProperties: any
      - `approver_stages` (array of object `ApproverStagesitemBase`) [maxItems=10] — Field: approver_stages
        schema: `ApproverStagesitemBase`
        - `sequence_number` (integer/int32) — Field: sequence_number
        - `approver` (object `ApproverBase`) — Base schema for approver
          schema: `ApproverBase`
          - `based_on_field` (object `BasedOnFieldBase`) — Base schema for based_on_field
            schema: `BasedOnFieldBase`
            - `api_name` (string) [maxLen=255, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Field: api_name
            - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
            additionalProperties: any
          - `field` (object `FieldBase1`) — Base schema for field
            schema: `FieldBase1`
            - `api_name` (string) [maxLen=255, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Field: api_name
            - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
            additionalProperties: any
          - `resource` (object `ResourceBase`) — Base schema for resource
            schema: `ResourceBase`
            - `name` (string) [maxLen=255] — Field: name
            - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
            additionalProperties: any
          - `level` (integer/int32) — Field: level
          - `level_up_to` (integer/int32) [nullable] — Value of the level if approver type is level. Determine the role or reporting hierarchy level upto which user should be assigned as user.
          - `everyone_approval_required` (boolean) — Field: everyone_approval_required
          - `type` (string) [maxLen=255] — Field: type
          additionalProperties: any
        - `name` (string) [maxLen=255] — Field: name
        - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
        - `record_modification` (object `RecordModificationBase`) — Base schema for record_modification
          schema: `RecordModificationBase`
          - `during_approval_waiting` (object `DuringApprovalWaitingBase1`) — Base schema for during_approval_waiting
            schema: `DuringApprovalWaitingBase1`
            - `update_allowed_for` (string) [maxLen=255] — Field: update_allowed_for
            - `fields` (array of object `FieldsitemBase2`) [maxItems=25] — Field: fields
              schema: `FieldsitemBase2`
              - `api_name` (string) [maxLen=255, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Field: api_name
              - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
              additionalProperties: any
            additionalProperties: any
          - `after_record_rejection` (object `AfterRecordRejectionBase1`) — Base schema for after_record_rejection
            schema: `AfterRecordRejectionBase1`
            - `update_allowed_for` (string) [maxLen=255] — Field: update_allowed_for
            - `fields` (array of object `FieldsitemBase3`) [maxItems=25] — Field: fields
              schema: `FieldsitemBase3`
              - `api_name` (string) [maxLen=255, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Field: api_name
              - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
              additionalProperties: any
            additionalProperties: any
          additionalProperties: any
        - `actions` (object `ActionsBase`) — Base schema for actions
          schema: `ActionsBase`
          - `on_approve` (array of object `OnApproveitemBase`) [maxItems=25] — Field: on_approve
            schema: `OnApproveitemBase`
            - `name` (string) [maxLen=255] — Field: name
            - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
            - `type` (string) [maxLen=255] — Field: type
            additionalProperties: any
          - `on_approval_trigger` (array of object `OnApprovalTriggeritemBase`) [maxItems=25] — Field: on_approval_trigger
            schema: `OnApprovalTriggeritemBase`
            - `name` (string) [maxLen=255] — Field: name
            - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
            - `type` (string) [maxLen=255] — Field: type
            additionalProperties: any
          additionalProperties: any
        additionalProperties: any
      additionalProperties: any
    - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
    - `execute_on` (string) **REQ** [maxLen=255] — Field: execute_on
    additionalProperties: any

**Responses:**

- **200**: Returns the result of the Approval Process update. — Schema: `Put111111000000908280Response200` [application/json]
    > If approval process update is successful.
    schema: `Put111111000000908280Response200`
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

- **400**: The Approval Process update request is invalid.
**Resolution:** The request body must contain valid values for all fields of the Approval Process. [application/json]
    > Represents the error response returned when the Approval Process update request is invalid.
    oneOf:
        - `approval_process` (array of object) [maxItems=25] **REQ** — Contains the error objects corresponding to the validation failures in the Approval Process update request.
          oneOf:
            - `DuplicateApprovalOrderError` — Uniqueness error indicating the approval_order value is duplicated.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=[2 values]] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ApprovalProcessNameLengthError` — Validation error indicating the process name exceeds the allowed length.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `maximum_length` (integer/int32) — Detail field: maximum_length
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['The lenght of name has exceeded the limit']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessInvalidDataErrorResponse10` — if invalid type is given as input for approver type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `expected_data_type` (string) [maxLen=255] — Detail field: expected_data_type
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
                - `supported_values` (array of string) [maxItems=25] — Detail field: supported_values
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['invalid data']] — Error message
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
            - `ExecuteOnMissingError` — Validation error indicating the execute_on field was not provided.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['The required data missing']] — Error message
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
            - `ApproverTypeInvalidValueError` — Validation error indicating an invalid value was provided for approver type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
                - `supported_values` (array of string) [maxItems=25] — Detail field: supported_values
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['invalid data is given for type']] — Error message
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
            - `ProcessInvalidDataErrorResponse8` — This error occurs when the provided process id is invalid or it is not an existing approval process
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['invalid approval process id']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessInvalidDataErrorResponse3` — This error occurs when the provided rule id is invalid or it is not existing in the given approval process id
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['invalid approval rule id']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessInvalidDataErrorResponse2` — This error occurs when the provided stage id is invalid or it is not existing in the given rule id
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['invalid approval stage id']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessMandatoryNotFoundErrorResponse1` — if process id is not given in input
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['required field not found']] — Error message
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
            - `ProcessNotAllowedErrorResponse3` — This error occurs when module field given in the input.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['module cannot be updated']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessNotAllowedErrorResponse4` — This error occurs when generated_type given in the input.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['generated type cannot be updated']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessNotAllowedErrorResponse1` — The request failed because it attempts to delete the only remaining rule of the approval process. An approval process must contain at least one rule, so deleting all rules is not permitted. Add or retain at least one rule before performing this operation.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['all rules cannot be deleted']] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `ProcessNotAllowedErrorResponse2` — The request failed because it attempts to delete the only remaining approver stage in the rule. Each rule must contain at least retain at least one approver stage before performing this deletion.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — Detail field: api_name
                - `json_path` (string) [maxLen=1000] — Detail field: json_path
              - `message` (string) **REQ** [enum=['all approval stages cannot be deleted']] — Error message
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
            - `ApproverLevelAmbiguityError` — Ambiguity error when both level and level_up_to given for the levels approver type.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Error code
              - `details` (object) **REQ** — Error details with validation information
                - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Detail field: ambiguity_due_to
                  - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
              - `message` (string) **REQ** [enum=['Ambiguity while processing the request']] — Error message
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

- **403**: Permission denied to update the Approval Process.
**Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `ApprovalProcessPermissionDeniedErrorResponse` [application/json]
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

**Scopes:** ZohoCRM.settings.approval_process.UPDATE

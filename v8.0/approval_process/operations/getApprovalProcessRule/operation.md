# GET /settings/approval_process/{approvalProcessId}/rules/{ruleId}
**Operation:** `getApprovalProcessRule` — Retrieve an Approval Process Rule
> To retrieve the configuration of a specific rule within an Approval Process. The response includes the rule name, sequence number, overall approval type, entry criteria, approver stages, process admin configuration, and the actions defined for final approval and rejection.

**Parameters:**
- `approvalProcessId` (path, string/int64, required) [maxLen=255, minLen=1, pattern=^[0-9]+$]: The unique identifier of the approval process to clone
- `ruleId` (path, string/int64, required) [maxLen=255, minLen=1, pattern=^[0-9]+$]: The unique identifier of the approval process to clone

**Schemas:**
`GETActionNested`:
  > Nested schema for action
  - `related_details` (null) — Field: related_details
  - `name` (string) **REQ** [maxLen=255] — Field: name
  - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
  - `type` (string) **REQ** [maxLen=255] — Field: type
`GETActionsNested`:
  > Nested schema for actions
  - `on_approve` (array of object `GETOnApproveNested`) [maxItems=2, nullable] **REQ** — Field: on_approve
  - `on_approval_trigger` (array of object `GETOnApprovalTriggerNested`) [maxItems=1, nullable] **REQ** — Field: on_approval_trigger
`GETActionsNested2`:
  > Nested schema for actions
  - `related_details` (null) **REQ** — Field: related_details
  - `name` (string) **REQ** [maxLen=255] — Field: name
  - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
  - `type` (string) **REQ** [maxLen=255] — Field: type
`GETActionsPerApprovalNested`:
  > Nested schema for actions_per_approval
  - `approval_order` (integer/int32) **REQ** — Field: approval_order
  - `actions` (array of object `GETActionsNested2`) [maxItems=1] **REQ** — Field: actions
`GETAfterRecordRejectionNested`:
  > Nested schema for after_record_rejection
  - `update_allowed_for` (string) **REQ** [maxLen=255] — Field: update_allowed_for
`GETAfterRecordRejectionNested1`:
  > Nested schema for after_record_rejection
  - `update_allowed_for` (string) **REQ** [maxLen=255] — Field: update_allowed_for
`GETBasedOnFieldNested`:
  > Nested schema for based_on_field
  - `api_name` (string) **REQ** [maxLen=255] — Field: api_name
  - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
`GETDuringApprovalWaitingNested`:
  > Nested schema for during_approval_waiting
  - `update_allowed_for` (string) **REQ** [maxLen=255] — Field: update_allowed_for
`GETDuringApprovalWaitingNested1`:
  > Nested schema for during_approval_waiting
  - `update_allowed_for` (string) **REQ** [maxLen=255] — Field: update_allowed_for
  - `fields` (array of object `GETFieldsNested`) [maxItems=2] — Field: fields
`GETFieldsNested`:
  > Nested schema for fields
  - `api_name` (string) **REQ** [maxLen=255] — Field: api_name
  - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
`GETGroupNested`:
  > Nested schema for group
  - `comparator` (string) **REQ** [maxLen=255] — Field: comparator
  - `field` (string) **REQ** [maxLen=255] — Field: field
  - `value` (array of string) [maxItems=2] **REQ** — Field: value
    items: [maxLen=255]
`GETNotifyOriginalApproversViaNested`:
  > Nested schema for notify_original_approvers_via
  - `feed` (boolean) **REQ** — Field: feed
  - `email` (boolean) **REQ** — Field: email
`GETOnApprovalTriggerNested`:
  > Nested schema for on_approval_trigger
  - `related_details` (null) **REQ** — Field: related_details
  - `name` (string) **REQ** [maxLen=255] — Field: name
  - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
  - `type` (string) **REQ** [maxLen=255] — Field: type
`GETOnApproveNested`:
  > Nested schema for on_approve
  - `related_details` (null) **REQ** — Field: related_details
  - `name` (string) **REQ** [maxLen=255] — Field: name
  - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
  - `type` (string) **REQ** [maxLen=255] — Field: type
`GETOverallStagesRecordModificationNested`:
  > Nested schema for overall_stages_record_modification
  - `during_approval_waiting` (object `GETDuringApprovalWaitingNested`) **REQ** — Nested schema for during_approval_waiting
  - `after_record_rejection` (object `GETAfterRecordRejectionNested`) **REQ** — Nested schema for after_record_rejection
`GETRecordModificationNested1`:
  > Nested schema for record_modification
  - `during_approval_waiting` (object `GETDuringApprovalWaitingNested1`) **REQ** — Nested schema for during_approval_waiting
  - `after_record_rejection` (object `GETAfterRecordRejectionNested1`) **REQ** — Nested schema for after_record_rejection
`GETResourceNested`:
  > Nested schema for resource
  - `name` (string) **REQ** [maxLen=255] — Field: name
  - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id

**Responses:**

- **200**: Returns the details of the specified rule within an Approval Process. The response contains a `rules` array with one rule object, which includes the rule name, sequence number, overall approval type, entry criteria, approver stages, process admin configuration, and actions configured upon final approval and rejection. — Schema: `Get947413000014810021Response200` [application/json]
    > If rule exists for the process, then details of the rule is received in the response. Below response is for overall_approval_type = everyone_sequential.

    schema: `Get947413000014810021Response200`
    - `rules` (array of object `GETRulesNested1`) [maxItems=1] **REQ** — Field: rules
      schema: `GETRulesNested1`
      - `sequence_number` (integer/int32) **REQ** — Field: sequence_number
      - `actions_per_approval` (array of object `GETActionsPerApprovalNested`) [maxItems=10] — Field: actions_per_approval
      - `overall_approval_type` (string) **REQ** [maxLen=255] — Field: overall_approval_type
      - `criteria` (object) **REQ**
        oneOf:
          - `GETCriteriaNested` — Nested schema for criteria
            - `group_operator` (string) [maxLen=255] — Field: group_operator
            - `group` (array of object `GETGroupNested`) [maxItems=2] — Field: group
            additionalProperties: any
          - `GETGroupNested` — Nested schema for group
      - `name` (string) **REQ** [maxLen=255] — Field: name
      - `process_admin_configuration` (object `GETProcessAdminConfigurationNested`) **REQ** — Nested schema for process_admin_configuration
        schema: `GETProcessAdminConfigurationNested`
        - `notify_original_approvers_via` (object `GETNotifyOriginalApproversViaNested`) **REQ** — Nested schema for notify_original_approvers_via
        - `process_admin` (array of object `GETProcessAdminNested`) [maxItems=1] **REQ** — Field: process_admin
          schema: `GETProcessAdminNested`
          - `resources` (array of object `GETResourcesNested`) [maxItems=3] **REQ** — Field: resources
            schema: `GETResourcesNested`
            - `name` (string) **REQ** [maxLen=255] — Field: name
            - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
          - `type` (string) **REQ** [maxLen=255] — Field: type
        - `record_modification` (object `GETRecordModificationNested`) **REQ** — Nested schema for record_modification
          schema: `GETRecordModificationNested`
          - `update_allowed_for` (string) **REQ** [maxLen=255] — Field: update_allowed_for
      - `actions_upon_final_approval` (object `GETActionsUponFinalApprovalNested1`) **REQ** — Nested schema for actions_upon_final_approval
        schema: `GETActionsUponFinalApprovalNested1`
        - `actions` (array of object `GETActionNested`) [maxItems=4] **REQ** — Field: actions
      - `actions_upon_rejection` (object `GETActionsUponRejectionNested1`) **REQ** — Nested schema for actions_upon_rejection
        schema: `GETActionsUponRejectionNested1`
        - `notify_original_approvers_via` (object `GETNotifyOriginalApproversViaNested`) **REQ** — Nested schema for notify_original_approvers_via
        - `rejection_type` (string) [maxLen=255] — Field: rejection_type
        - `actions` (array of object `GETActionNested`) [maxItems=5] — Field: actions
      - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
      - `overall_stages_record_modification` (object `GETOverallStagesRecordModificationNested`) — Nested schema for overall_stages_record_modification
      - `approver_stages` (array of object) [maxItems=10] **REQ** — Field: approver_stages
        oneOf:
          - `GETApproverStagesNested` — Nested schema for approver_stages
            - `sequence_number` (integer/int32) **REQ** — Field: sequence_number
            - `approver` (object `GETApproverNested5`) **REQ** — Nested schema for approver
              schema: `GETApproverNested5`
              - `resource` (object `GETResourceNested`) **REQ** — Nested schema for resource
              - `type` (string) **REQ** [maxLen=255] — Field: type
            - `name` (string) **REQ** [maxLen=255] — Field: name
            - `record_modification` (object `GETRecordModificationNested1`) — Nested schema for record_modification
            - `actions` (object `GETActionsNested`) **REQ** — Nested schema for actions
            - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
          - `GETApproverStagesNested1` — Nested schema for approver_stages
            - `sequence_number` (integer/int32) **REQ** — Field: sequence_number
            - `approver` (object `GETApproverNested7`) **REQ** — Nested schema for approver
              schema: `GETApproverNested7`
              - `based_on_field` (object `GETBasedOnFieldNested`) **REQ** — Nested schema for based_on_field
              - `level` (integer/int32) **REQ** — Field: level
              - `everyone_approval_required` (boolean) **REQ** — Field: everyone_approval_required
              - `type` (string) **REQ** [maxLen=255] — Field: type
            - `name` (string) **REQ** [maxLen=255] — Field: name
            - `record_modification` (object `GETRecordModificationNested1`) — Nested schema for record_modification
            - `actions` (object `GETActionsNested`) **REQ** — Nested schema for actions
            - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
          - `GETApproverStagesNested2` — Nested schema for approver_stages
            - `sequence_number` (integer/int32) **REQ** — Field: sequence_number
            - `approver` (object `GETApproverNested8`) **REQ** — Nested schema for approver
              schema: `GETApproverNested8`
              - `based_on_field` (object `GETBasedOnFieldNested`) **REQ** — Nested schema for based_on_field
              - `level_up_to` (string) **REQ** [maxLen=255] — Field: level_up_to
              - `everyone_approval_required` (boolean) **REQ** — Field: everyone_approval_required
              - `type` (string) **REQ** [maxLen=255] — Field: type
            - `name` (string) [maxLen=255] — Field: name
            - `record_modification` (object `GETRecordModificationNested1`) — Nested schema for record_modification
            - `actions` (object `GETActionsNested1`) **REQ** — Nested schema for actions
              schema: `GETActionsNested1`
              - `actions_per_approval` (array of object `GETActionsPerApprovalNested`) [maxItems=10, nullable] **REQ** — Field: actions_per_approval
              - `on_approval_trigger` (array of object `GETOnApprovalTriggerNested`) [maxItems=1, nullable] **REQ** — Field: on_approval_trigger
            - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
          - `GETApproverStagesNested3` — Nested schema for approver_stages
            - `sequence_number` (integer/int32) **REQ** — Field: sequence_number
            - `approver` (object `GETApproverNested9`) **REQ** — Nested schema for approver
              schema: `GETApproverNested9`
              - `based_on_field` (object `GETBasedOnFieldNested`) **REQ** — Nested schema for based_on_field
              - `type` (string) **REQ** [maxLen=255] — Field: type
            - `name` (string) **REQ** [maxLen=255] — Field: name
            - `record_modification` (object `GETRecordModificationNested1`) — Nested schema for record_modification
            - `actions` (object `GETActionsNested`) **REQ** — Nested schema for actions
            - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
          - `GETApproverStagesNested4` — Nested schema for approver_stages
            - `sequence_number` (integer/int32) **REQ** — Field: sequence_number
            - `approver` (object `GETApproverNested4`) **REQ** — Nested schema for approver
              schema: `GETApproverNested4`
              - `field` (object `GETFieldNested`) **REQ** — Nested schema for field
                schema: `GETFieldNested`
                - `api_name` (string) **REQ** [maxLen=255] — Field: api_name
                - `data_type` (string) **REQ** [maxLen=255] — Field: data_type
                - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
              - `type` (string) **REQ** [maxLen=255] — Field: type
            - `name` (string) **REQ** [maxLen=255] — Field: name
            - `record_modification` (object `GETRecordModificationNested1`) — Nested schema for record_modification
            - `actions` (object `GETActionsNested`) **REQ** — Nested schema for actions
            - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
          - `GETApproverStagesNested5` — Nested schema for approver_stages
            - `sequence_number` (integer/int32) **REQ** — Field: sequence_number
            - `approver` (object `GETApproverNested3`) **REQ** — Nested schema for approver
              schema: `GETApproverNested3`
              - `resource` (object `GETResourceNested`) **REQ** — Nested schema for resource
              - `everyone_approval_required` (boolean) **REQ** — Field: everyone_approval_required
              - `type` (string) **REQ** [maxLen=255] — Field: type
            - `name` (string) **REQ** [maxLen=255] — Field: name
            - `record_modification` (object `GETOverallStagesRecordModificationNested`) — Nested schema for overall_stages_record_modification
            - `actions` (object `GETActionsNested`) **REQ** — Nested schema for actions
            - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
          - `GETApproverStagesNested6` — Nested schema for approver_stages
            - `sequence_number` (integer/int32) **REQ** — Field: sequence_number
            - `approver` (object `GETApproverNested6`) **REQ** — Nested schema for approver
              schema: `GETApproverNested6`
              - `resource` (object `GETResourceNested`) **REQ** — Nested schema for resource
              - `everyone_approval_required` (string) **REQ** [maxLen=255] — Field: everyone_approval_required
              - `type` (string) **REQ** [maxLen=255] — Field: type
            - `name` (string) **REQ** [maxLen=255] — Field: name
            - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
            - `record_modification` (object `GETRecordModificationNested1`) — Nested schema for record_modification
            - `actions` (object `GETActionsNested`) **REQ** — Nested schema for actions
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: Returns an empty response when no rule matching the specified rule ID exists for the given Approval Process.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The Approval Process ID provided in the request path is invalid.
**Resolution:** Verify that the Approval Process ID is correct and corresponds to an existing Approval Process in Zoho CRM. — Schema: `RulesInvalidDataErrorResponse1` [application/json]
    > Error response wrapper for single get bad request
    schema: `RulesInvalidDataErrorResponse1`
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
    - `details` (object) **REQ** — Error details with validation information
      - `resource_path_index` (integer/int32) — Detail field: resource_path_index
    - `message` (string) **REQ** [enum=['INVALID_PROCESSID']] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The user does not have permission to retrieve Approval Process rules.
**Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `ApprovalProcessPermissionDeniedErrorResponse` [application/json]
    > Error response wrapper for single get forbidden
    schema: `ApprovalProcessPermissionDeniedErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code
    - `details` (object) **REQ** — Error details with validation information
      - `permissions` (array of string) [maxItems=25] — Detail field: permissions
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.approval_process.READ

# GET /settings/approval_process/{approvalProcessId}/rules
**Operation:** `getApprovalProcessRules` — Get rules for an Approval Process
> To retrieve the rules associated with a specific Approval Process in your Zoho CRM organization. The response returns an array of rule objects, each containing the sequence number, name, overall approval type, entry criteria, approver stages, process admin configuration, record modification settings, and the actions triggered upon final approval or rejection. Use the optional ids query parameter to filter results to a specific subset of rules.

**Parameters:**
- `ids` (query, string/int64, optional) [maxLen=19, minLen=1, pattern=^[0-9]+$]: Approval process ids
- `approvalProcessId` (path, string/int64, required) [maxLen=255, minLen=1, pattern=^[0-9]+$]: The unique identifier of the approval process to clone

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

- **200**: Returns the list of rules configured for the specified Approval Process in Zoho CRM. Each rule object includes the sequence number, name, overall approval type, entry criteria, approver stages, process admin configuration, record modification settings, and actions triggered upon final approval or rejection. — Schema: `GetrulesResponse200` [application/json]
    > If approval process is valid, then rules present in the process will be returned.
    schema: `GetrulesResponse200`
    - `rules` (array of object `GETRulesNested1`) [maxItems=5] **REQ** — Field: rules
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

- **400**: The request contains invalid data.
**Resolution:** Verify that the Approval Process ID in the URL path is a valid, existing identifier. If the ids query parameter is provided, ensure all values are valid long integers. [application/json]
    > Represents the error response returned when the request is invalid. Contains one of two variants: an invalid Approval Process ID in the URL path, or invalid values in the ids query parameter.
    oneOf:
      - `RulesInvalidDataErrorResponse1` — If the approval process Id given in the URL is invalid or not found.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) — Detail field: resource_path_index
        - `message` (string) **REQ** [enum=['INVALID_PROCESSID']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `RulesInvalidDataErrorResponse2` — If param "ids" is given a list of values other than type long, this error response is received.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) **REQ** [maxLen=255] — Detail field: param_name
        - `message` (string) **REQ** [enum=['invalid data', 'invalid param']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied. The authenticated user's CRM profile does not include the permission required to retrieve Approval Process rules.
**Resolution:** A Zoho CRM administrator must grant the permission to the user's CRM profile. — Schema: `ApprovalProcessPermissionDeniedErrorResponse` [application/json]
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

# GET /settings/approval_process/process_configurations
**Operation:** `getProcessConfigurations` — Retrieve the Approval Process configuration limits
> To retrieve the configuration limits for approval processes in your Zoho CRM organization. The response provides the maximum allowed numbers of approval processes, rules, stages, fields, and levels, along with the number of levels currently available, helping you understand the constraints that apply when you create or update approval processes.

**Responses:**

- **200**: Returns the configuration limits for approval processes, including the maximum allowed number of approval processes, rules, stages, fields, and levels, along with the number of levels currently available. — Schema: `GetprocessconfigurationsResponse200` [application/json]
    > Success response is received upon hitting the endpoint.
    schema: `GetprocessconfigurationsResponse200`
    - `approval_process` (array of object `GETApprovalProcessNested`) [maxItems=1] **REQ** — Field: approval_process
      schema: `GETApprovalProcessNested`
      - `total_available_levels` (integer/int32) **REQ** — number of level available in the org. It's based on the company hierarchy preference

role hierarchy: based on the role and it's hierarchy tree. (levels in hierarchy tree - 1)
reporting hierarchy: number of active users - 1. 
      - `maximum_allowed_fields_for_record_modification` (integer/int32) **REQ** — maximum number of fields that can be allowed for editing in record modification setting.
      - `maximum_allowed_levels` (integer/int32) **REQ** — maximum number of level type approver can be configure in each rule
      - `maximum_allowed_stages_per_rule` (integer/int32) **REQ** — maximum number of stages can be configured in each  rule.
      - `maximum_allowed_active_process_per_module` (integer/int32) **REQ** — maximum number of process can be configured for a module in the account.
      - `maximum_allowed_rules_per_process` (integer/int32) **REQ** — maximum number of rules can be configured in each process.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The user does not have permission to access the Approval Process configuration limits.
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

**Scopes:** ZohoCRM.settings.approval_process.READ

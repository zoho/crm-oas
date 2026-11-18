# GET /settings/approval_process/{approvalProcessId}
**Operation:** `getSingleApprovalProcess` — Get a single Approval Process
> To retrieve the full configuration details of a single Approval Process in your Zoho CRM organization by its unique identifier. The response includes the process name, associated module, active status, execution trigger, and the complete list of approval rules defined for the Approval Process.

**Parameters:**
- `approvalProcessId` (path, string/int64, required) [maxLen=255, minLen=1, pattern=^[0-9]+$]: The unique identifier of the approval process to clone

**Responses:**

- **200**: Returns the details of the requested Approval Process. — Schema: `Get947413000014810019Response200` [application/json]
    > If data found for the given approval process Id in the URL, then this response is returned.
    schema: `Get947413000014810019Response200`
    - `approval_process` (array of object `GETApprovalProcessNested3`) [maxItems=1] **REQ** — Field: approval_process
      schema: `GETApprovalProcessNested3`
      - `sequence_number` (integer/int32) **REQ** — Field: sequence_number
      - `created_time` (string) **REQ** [maxLen=255] — Field: created_time
      - `modified_time` (string) **REQ** [maxLen=255] — Field: modified_time
      - `module` (object `GETModuleNested`) **REQ** — Nested schema for module
        schema: `GETModuleNested`
        - `api_name` (string) **REQ** [maxLen=255] — Field: api_name
        - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
      - `name` (string) **REQ** [maxLen=255] — Field: name
      - `description` (string) [maxLen=255] — Field: description
      - `modified_by` (object `GETModifiedByNested`) **REQ** — Nested schema for modified_by
        schema: `GETModifiedByNested`
        - `name` (string) **REQ** [maxLen=255] — Field: name
        - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
      - `active` (boolean) **REQ** — Field: active
      - `generated_type` (string) **REQ** [maxLen=255] — Field: generated_type
      - `rules` (array of object `GETRulesNested3`) [maxItems=5] **REQ** — Field: rules
        schema: `GETRulesNested3`
        - `sequence_number` (integer/int32) **REQ** — Field: sequence_number
        - `overall_approval_type` (string) **REQ** [maxLen=255] — Field: overall_approval_type
        - `name` (string) [maxLen=255] — Field: name
        - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
      - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
      - `created_by` (object `GETCreatedByNested`) **REQ** — Nested schema for created_by
        schema: `GETCreatedByNested`
        - `name` (string) **REQ** [maxLen=255] — Field: name
        - `id` (string/int64) **REQ** [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
      - `execute_on` (string) **REQ** [maxLen=255] — Field: execute_on
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: No matching Approval Process was found for the provided ID. The response contains no body.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied. The user's CRM profile does not have the required permission to access Approval Process settings.
**Resolution:** A CRM administrator must grant the permission to the caller's profile. — Schema: `ApprovalProcessPermissionDeniedErrorResponse` [application/json]
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

# GET /settings/automation/approval_process/actions/count
**Operation:** `getApprovalProcessCount` — Retrieve the count of approval processes for a module
> To retrieve the total, active, and inactive counts of approval processes configured for a specific module in your Zoho CRM organization.

**Parameters:**
- `module` (query, string, required) [maxLen=255]: Specify the API name of the CRM module, such as Leads, Contacts, or Deals, to retrieve the Approval Process count for that module.

**Responses:**

- **200**: Returns the Approval Process count for the specified module, with the total number of approval processes and a breakdown by active and inactive status. — Schema: `ApprovalProcessCountResponseSchema` [application/json]
    > Count of approval processes configured for a module, broken down by active and inactive status.
    schema: `ApprovalProcessCountResponseSchema`
    - `total` (integer/int32) **REQ** — Total number of approval processes configured for the module
    - `active` (integer/int32) **REQ** — Number of currently active approval processes
    - `inactive` (integer/int32) **REQ** — Number of currently inactive approval processes
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed because the module query parameter is missing or its value is not a valid module API name.
**Resolution:** Provide the required module query parameter with a valid CRM module API name, such as Leads, Contacts, or Deals, and resend the request. — Schema: `ApprovalProcessCountInvalidDataErrorResponse` [application/json]
    > Required parameter missing or invalid module
    schema: `ApprovalProcessCountInvalidDataErrorResponse`
    - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING', 'INVALID_MODULE']] — Error code
    - `message` (string) **REQ** [maxLen=1000] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status
    - `details` (object) **REQ** — Error details with validation information
      - `param_name` (string) [enum=['module']] — Detail field: module
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.approval_process.READ

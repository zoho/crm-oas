# POST /settings/approval_process/{approvalProcessId}/actions/clone
**Operation:** `cloneApprovalProcess` — Clone Approval Process
> To clone an existing Approval Process in your Zoho CRM organization, use this endpoint to create a new Approval Process that inherits the same configuration as the original.

**Parameters:**
- `approvalProcessId` (path, string/int64, required) [maxLen=255, minLen=1, pattern=^[0-9]+$]: The unique identifier of the approval process to clone

**Responses:**

- **201**: Returns the details of the cloned Approval Process, including its unique identifier and the status of the clone operation. — Schema: `PostcloneResponse200` [application/json]
    > If cloning of the approval process is successful, this response with new approval process id is received.
    schema: `PostcloneResponse200`
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

- **400**: The request cannot be processed due to an invalid Approval Process ID or an exceeded module limit.
**Resolution:** Verify that the Approval Process ID supplied in the request URL is valid. If the identifier is correct, confirm that the number of Approval Processes for the target module has not reached the allowed limit before retrying the clone operation. [application/json]
    > Represents the error response returned when a clone request fails with a 400 Bad Request status. Contains one of two error variants: an invalid-data error when the Approval Process ID in the request URL is not valid, or a limit-exceeded error when the number of Approval Processes for the specified module has reached the allowed limit.
    oneOf:
      - `ProcessInvalidDataErrorResponse9` — Invalid Id is sent in the URL for cloning.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) — Detail field: resource_path_index
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `CloneLimitExceededErrorResponse1` — If the limit is reached for creating approval process, then this error is thrown.
        - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `limit` (integer/int32) — Detail field: limit
        - `message` (string) **REQ** [enum=['used the entire limit per module']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied. The requesting user does not have the required permissions to clone the Approval Process.
**Resolution:** A Zoho CRM administrator must grant the user the necessary permissions, such as Crm_Implied_Manage_Workflow, before the operation can be retried. — Schema: `ApprovalProcessPermissionDeniedErrorResponse` [application/json]
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

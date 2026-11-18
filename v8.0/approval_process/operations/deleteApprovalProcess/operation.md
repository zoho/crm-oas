# DELETE /settings/approval_process/{approvalProcessId}
**Operation:** `deleteApprovalProcess` — Delete an Approval Process
> To delete a single Approval Process from your Zoho CRM organization using its unique ID.

**Parameters:**
- `approvalProcessId` (path, string/int64, required) [maxLen=255, minLen=1, pattern=^[0-9]+$]: The unique identifier of the approval process to clone

**Responses:**

- **200**: Returns a confirmation that the specified Approval Process was successfully deleted. The response includes an approval_process array containing a SUCCESS status code and the ID of the deleted process. — Schema: `Delete947413000014810019Response200` [application/json]
    > If deletion of the approval process is success.
    schema: `Delete947413000014810019Response200`
    - `approval_process` (array of object `DataNested`) [maxItems=1] — Field: approval_process
      schema: `DataNested`
      - `code` (string) [maxLen=255] — Field: code
      - `details` (object `ApprovalProcessCreateDetails`) — Contains identifiers and related information returned after creating an approval process.
        schema: `ApprovalProcessCreateDetails`
        - `id` (string/int64) [maxLen=255, minLen=1, pattern=^[0-9]+$] — Field: id
      - `message` (string) [maxLen=255] — Field: message
      - `status` (string) [maxLen=255] — Field: status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The provided Approval Process ID is invalid.
**Resolution:** Verify that the approvalProcessId path parameter corresponds to an existing Approval Process and that the ID value is correctly formed. — Schema: `ProcessInvalidDataErrorResponse9` [application/json]
    > Invalid Id is sent in the URL for cloning.
    schema: `ProcessInvalidDataErrorResponse9`
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
    - `details` (object) **REQ** — Error details with validation information
      - `resource_path_index` (integer/int32) — Detail field: resource_path_index
    - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The authenticated user's CRM profile does not have permission to delete Approval Processes.
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

**Scopes:** ZohoCRM.settings.approval_process.DELETE

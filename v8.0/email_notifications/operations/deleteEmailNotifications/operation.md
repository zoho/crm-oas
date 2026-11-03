# DELETE /settings/automation/email_notifications
**Operation:** `deleteEmailNotifications` — Delete Email Notifications
> To delete one or more email notifications configured in your Zoho CRM organization. Email notifications associated with an Approval Process, Workflow Rule, Blueprint, or CommandCenter automation cannot be deleted until they are disassociated from the corresponding automation.

**Parameters:**
- `ids` (query, string, required) [maxLen=250]: Specify the unique IDs of the email notifications to delete. Accepts comma-separated values. Maximum: 10.

**Schemas:**
`BulkDeleteFailureItem`:
  > Represents the result of a failed deletion for a single record ID during a bulk delete operation, including the failure code, status, and error message.
  - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Represents the failure code indicating why the bulk delete operation failed for this record.
Possible values:
INVALID_DATA - The data provided for the record is invalid.
NOT_ALLOWED - The delete operation is not permitted for this record.
  - `details` (object `BulkDeleteResultDetails`) **REQ** — Represents the identifier details for a bulk-delete result item, including the unique ID of the email notification for which the result applies.
  - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the bulk delete operation failed for this record.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the bulk delete operation for this record.
Possible values:
error - Indicates that the delete operation failed for this record.
`BulkDeleteResultDetails`:
  > Represents the identifier details for a bulk-delete result item, including the unique ID of the email notification for which the result applies.
  - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the email notification for which this bulk-delete result applies.
`BulkDeleteSuccessItem`:
  > Represents the result item returned for a record that was successfully deleted in a bulk delete operation.
  - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for a successfully deleted record in a bulk delete operation.
Possible values:
SUCCESS - Indicates that the record was deleted successfully.
  - `details` (object `BulkDeleteResultDetails`) **REQ** — Represents the identifier details for a bulk-delete result item, including the unique ID of the email notification for which the result applies.
  - `message` (string) **REQ** [maxLen=255] — Represents the success message returned when a record is deleted successfully in a bulk delete operation.
  - `status` (string) **REQ** [enum=['success']] — Represents the operation status of a bulk delete item.
Possible values:
success - Indicates that the deletion of the record was completed successfully.

**Responses:**

- **200**: Returns the deletion results for all requested email notification IDs. Each item in the response array confirms a successful deletion with a SUCCESS code and the corresponding notification ID. — Schema: `BulkDeleteSuccessResponse` [application/json]
    > Represents the response returned when all requested email notification definitions are successfully deleted.
    schema: `BulkDeleteSuccessResponse`
    - `email_notifications` (array of object `BulkDeleteSuccessItem`) [maxItems=3] **REQ** — Represents the list of deletion result entries for each email notification ID included in the request.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **207**: Returns a multi-status response. Each item in the array independently indicates success or failure for the corresponding email notification ID in the request. Successful deletions return a SUCCESS code, while failed items include an INVALID_DATA or NOT_ALLOWED code with details. — Schema: `BulkDeleteMixedResponse` [application/json]
    > Represents the partial-success response for a bulk delete request, containing a mix of successful and failed deletion results for the requested email notification IDs.
    schema: `BulkDeleteMixedResponse`
    - `email_notifications` (array of object) [maxItems=10] **REQ** — Represents the per-ID deletion results for the bulk delete request.
      oneOf:
        - `BulkDeleteSuccessItem` — Represents the result item returned for a record that was successfully deleted in a bulk delete operation.
        - `BulkDeleteFailureItem` — Represents the result of a failed deletion for a single record ID during a bulk delete operation, including the failure code, status, and error message.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The bulk delete operation failed for all provided IDs. Resolution: Each requested email notification ID must be valid and must not be associated with an Approval Process, Workflow Rule, Blueprint, or CommandCenter automation before deletion is attempted. — Schema: `BulkDeleteErrorResponse` [application/json]
    > Represents the error response returned when a bulk delete request fails because all provided email notification IDs failed validation or association checks.
    schema: `BulkDeleteErrorResponse`
    - `email_notifications` (array of object `BulkDeleteFailureItem`) [maxItems=10] **REQ** — Represents the list of per-ID failure results for the bulk delete request, where each item describes the validation or association check failure for a specific email notification ID.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to delete email notifications. Resolution: The CRM administrator must grant the manage workflow permission to the user's profile. — Schema: `PermissionDeniedError` [application/json]
    > Represents an error response returned when the requesting user lacks the necessary permissions to perform the operation.
    schema: `PermissionDeniedError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code indicating the reason the request was denied.
Possible values:
NO_PERMISSION - The requesting user does not have the required permission to perform this operation.
    - `details` (object) **REQ** — Represents an object containing additional details about the permission denial, including the specific permissions that were missing.
      - `permissions` (array of string) [maxItems=25] — Represents the list of permissions that the requesting user lacks for the attempted operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the reason the requested operation was denied.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
error - Indicates that the request failed due to insufficient permissions.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.automation_actions.DELETE

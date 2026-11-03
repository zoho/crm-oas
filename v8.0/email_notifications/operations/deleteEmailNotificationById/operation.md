# DELETE /settings/automation/email_notifications/{id}
**Operation:** `deleteEmailNotificationById` — Delete an Email Notification by ID
> Deletes a single email notification configured in your Zoho CRM organization. Email notifications associated with an Approval Process, Workflow Rules, or Blueprint cannot be deleted until they are disassociated from the corresponding automation.

**Parameters:**
- `id` (path, string, required) [maxLen=20]: Specify the unique ID of the email notification to delete.  Notifications associated with active automation cannot be deleted  - returns NOT_ALLOWED

**Responses:**

- **200**: Returns the result of the delete operation for the specified email notification. — Schema: `SingleDeleteSuccessResponse` [application/json]
    > Represents the response returned after successfully deleting a single email notification definition.
    schema: `SingleDeleteSuccessResponse`
    - `email_notifications` (array of object `SingleDeleteSuccessItem`) [maxItems=1] **REQ** — Represents the result of the delete operation for the specified email notification.
      schema: `SingleDeleteSuccessItem`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the delete operation.
Possible values:
SUCCESS - The delete operation completed successfully.
      - `details` (object `BulkDeleteResultDetails`) **REQ** — Represents the identifier details for a bulk-delete result item, including the unique ID of the email notification for which the result applies.
        schema: `BulkDeleteResultDetails`
        - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the email notification for which this bulk-delete result applies.
      - `message` (string) **REQ** [maxLen=255] — Represents the success message returned after the delete operation completes.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the delete operation.
Possible values:
success - The delete operation was completed successfully.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The provided email notification ID is invalid, or the email notification is associated with at least one of an Approval Process, Workflow Rules, or Blueprint. Resolution: The email notification must be disassociated from the corresponding automation before it can be deleted. [application/json]
    oneOf:
      - `SingleDeleteInvalidDataError` — Represents the error response returned when the provided email notification ID is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating the type of failure that occurred.
Possible values:
INVALID_DATA - The provided email notification ID is invalid.
        - `details` (object) **REQ** — Represents additional details about the error, including the index position of the invalid identifier in the request path.
          - `resource_path_index` (integer/int32) — Represents the index position of the invalid email notification ID within the request path context.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the request failed.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for this error.
Possible values:
error - Indicates that the request failed due to invalid data.
      - `SingleDeleteNotAllowedError` — Represents the error response returned when an email notification cannot be deleted because it is associated with an Approval Process, Workflow Rule, or Blueprint.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code indicating that the delete operation is not allowed.
Possible values:
NOT_ALLOWED - The email notification cannot be deleted because it is associated with an Approval Process, Workflow Rule, or Blueprint.
        - `details` (object) **REQ** — Represents additional details about the error, including the position of the affected resource identifier in the request path.
          - `resource_path_index` (integer/int32) — Represents the index position of the associated identifier within the request path context.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the delete operation is not allowed.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response.
Possible values:
error - Indicates that the request resulted in an error.
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

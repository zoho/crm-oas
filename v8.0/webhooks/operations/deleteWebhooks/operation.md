# DELETE /settings/automation/webhooks
**Operation:** `deleteWebhooks` — Delete one or more webhooks
> To delete one or more webhook actions configured in your Zoho CRM account.

Up to 10 webhooks can be deleted in a single API call using the **ids** query parameter. Read-only webhooks created by Zoho extensions cannot be deleted. 

Webhooks associated with active Workflow Rules, Approval Processes, or Blueprints cannot be deleted.

**Parameters:**
- `ids` (query, string, required) [maxLen=250]: Specify the comma-separated list of webhook IDs to delete. Accepts comma-separated values. Refer to the [Get Webhooks](webhooks.yaml#$.paths./settings/automation/webhooks.get) resource for valid values.

**Schemas:**
`WebhookDetailsResponse`:
  > Result details. On success, contains the webhook id.
  - `id` (string) [maxLen=255] — Represents the unique identifier of the webhook.
`WebhookStatusResponse`:
  > Represents the operation result for a webhook create, update, or delete action. On success, code is success, status is success, and details contains the webhook ID.
  - `code` (string) **REQ** [maxLen=255] — Represents the success or error code of the webhook operation.
  - `details` (object `WebhookDetailsResponse`) **REQ** — Result details. On success, contains the webhook id.
  - `message` (string) **REQ** [maxLen=255] — Represents the description of the operation result.
  - `status` (string) **REQ** [maxLen=255] — Represents the operation status.

**Responses:**

- **200**: Returns the list of operation results confirming that all specified webhooks were deleted successfully. — Schema: `BulkDeleteWebhooksSuccessResponse` [application/json]
    > Represents the success response for a bulk webhook deletion where all specified webhooks were deleted.
    schema: `BulkDeleteWebhooksSuccessResponse`
    - `webhooks` (array of object `WebhookStatusResponse`) [maxItems=10] — Represents the list of operation results confirming each webhook deletion.

- **207**: Returns a multi-status response. Each item in the array independently indicates success or failure for the corresponding webhook in the request. The API deleted at least one webhook and rejected at least one deletion. — Schema: `BulkDeletePartialSuccessResponse` [application/json]
    > Represents the HTTP Multi-Status response for bulk webhook deletion when results are mixed, indicating that at least one webhook was deleted and at least one deletion failed.
    schema: `BulkDeletePartialSuccessResponse`
    - `webhooks` (array of object `WebhookStatusResponse`) [maxItems=10] — Represents the list of operation results, containing a mix of success and error entries for each webhook deletion attempt.

- **400**: The request failed because the ids parameter is missing, more than 10 webhook IDs were provided, or one or more webhooks cannot be deleted because they are read-only or associated with active automation rules.

**Resolution:** Ensure the ids parameter is present, contains no more than 10 comma-separated webhook IDs, and that none of the specified webhooks are read-only or associated with active Workflow Rules, Approval Processes, or Blueprints. [application/json]
    > Contains the error response when one or more bulk webhook deletions fail, represented as a union of specific error variants for a missing parameter, an exceeded limit, or disallowed operations.
    oneOf:
      - `RequiredParamMissingIdsError` — Represents the error returned when the required ids query parameter is absent from a bulk DELETE request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for this failure.
Possible values:
**REQUIRED_PARAM_MISSING** - The required ids parameter is missing from the request.
        - `details` (object) **REQ** — Represents the error details containing the name of the missing required parameter.
          - `param_name` (string) [maxLen=255] — Represents the name of the missing required parameter.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message describing the failure.
Possible values:
**One of the expected parameter is missing** - The ids parameter, which is required for this operation, is not present in the request.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
      - `BulkDeleteLimitExceededError` — Represents the error returned when more than 10 webhook IDs are provided in a bulk DELETE request.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The number of webhook IDs in the request exceeds the allowed limit.
        - `details` (object) **REQ** — Represents the error details containing the parameter name and the maximum allowed count.
          - `limit` (integer/int32) — Represents the maximum number of webhook IDs allowed in a single bulk delete request.
          - `param_name` (string) [maxLen=255] — Represents the name of the parameter that exceeded the allowed limit.
        - `message` (string) **REQ** [enum=['Bulk deletion of records limit reached']] — Represents the error message describing the failure.

Possible values:
**Bulk deletion of records limit reached** - The number of webhook IDs in the request exceeds the maximum allowed limit.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.

Possible values:
**error** - Indicates the request did not complete successfully.
        - `webhooks` (array of object) [maxItems=10] **REQ** — Represents the list of error objects for webhooks that could not be deleted, where each item indicates either a read-only restriction or an active automation association.
          oneOf:
            - `BulkDeleteReadOnlyNotAllowedError` — Represents the error entry in a bulk delete response when a webhook in the request is read-only and cannot be deleted.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this failure.
Possible values:
**NOT_ALLOWED** - The webhook is read-only and cannot be deleted.
              - `details` (object) **REQ** — Represents the error details containing the ID of the read-only webhook that cannot be deleted.
                - `id` (string) [maxLen=20] — Represents the ID of the read-only webhook that cannot be deleted.
              - `message` (string) **REQ** [enum=['Insufficient privileges to delete Read only webhook']] — Represents the error message describing the failure.
Possible values:
**Insufficient privileges to delete Read only webhook** - The webhook is read-only and cannot be deleted by the requesting user.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
            - `BulkDeleteAssociatedNotAllowedError` — Represents the error entry in a bulk delete response when a webhook in the request is associated with active automation rules and cannot be deleted.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this failure.
Possible values:
**NOT_ALLOWED** - The requested operation is not allowed because the webhook is associated with an active automation rule.
              - `details` (object) **REQ** — Represents the error details containing the ID of the webhook that cannot be deleted.
                - `id` (string) [maxLen=20] — Represents the ID of the webhook that cannot be deleted.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing the failure.
Possible values:
**This webhook is associated with at least one of Approval Process/Workflow Rules/Blueprint** - The webhook cannot be deleted because it is actively associated with one or more automation rules.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.

- **403**: Permission denied to delete webhooks in this CRM organization.

**Resolution:** The CRM administrator must grant the Manage Workflow permission to the user's profile. — Schema: `NoPermissionErrorResponse` [application/json]
    > Represents the error returned when the requesting user does not have the required CRM profile permission to perform the operation.
    schema: `NoPermissionErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — The requesting user does not have the required CRM profile permission.
    - `details` (object) **REQ** — Represents the error details containing the list of permissions required for this operation.
      - `permissions` (array of string) [maxItems=25] — Represents the list of CRM profile permissions required to perform this operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message describing the failure.

Possible values:
**permission denied** - The requesting user lacks the required CRM profile permission for this operation.
    - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.

**Scopes:** ZohoCRM.settings.automation_actions.DELETE

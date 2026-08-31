# DELETE /settings/automation/webhooks/{webhookId}
**Operation:** `deleteWebhooksById` — Delete a webhook by ID
> To delete a specific webhook configured in your Zoho CRM organization using its unique ID.

Read-only webhooks created by Marketplace extensions cannot be deleted. Webhooks associated with active Workflow Rules, Approval Processes, Blueprints, or Command Center also cannot be deleted.

**Parameters:**
- `webhookId` (path, string, required) [maxLen=20]: Specify the unique ID of the webhook to delete. Refer to the [Get Webhooks](webhooks.yaml#$.paths./settings/automation/webhooks.get) resource for valid values.

**Responses:**

- **200**: Returns the delete operation result for the specified webhook. The webhooks array contains one item indicating whether Zoho CRM deleted the webhook successfully or why it could not be deleted. — Schema: `DeleteWebhookByIdSuccessResponse` [application/json]
    > Represents the success response for deleting a single webhook by its ID.
    schema: `DeleteWebhookByIdSuccessResponse`
    - `webhooks` (array of object `WebhookStatusResponse`) [maxItems=1] — Represents the list containing the operation result for the deleted webhook.
      schema: `WebhookStatusResponse`
      - `code` (string) **REQ** [maxLen=255] — Represents the success or error code of the webhook operation.
      - `details` (object `WebhookDetailsResponse`) **REQ** — Result details. On success, contains the webhook id.
        schema: `WebhookDetailsResponse`
        - `id` (string) [maxLen=255] — Represents the unique identifier of the webhook.
      - `message` (string) **REQ** [maxLen=255] — Represents the description of the operation result.
      - `status` (string) **REQ** [maxLen=255] — Represents the operation status.

- **400**: The webhook ID is invalid, the webhook is read-only, or the webhook is associated with active automation rules or created by a Marketplace extension.

**Resolution:** The webhook ID in the request URL must match an existing webhook. The webhook must not be read-only or associated with active Workflow Rules, Approval Processes, or Blueprints. [application/json]
    > Contains the error response when a single webhook DELETE request fails, covering variants for an invalid webhook ID, not-allowed conditions, and Marketplace restrictions.
    oneOf:
      - `MarketplaceWebhookNotAllowedError` — Represents the error returned when a request attempts to modify or delete a webhook created by a Marketplace extension or CommandCenter.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this failure.
Possible values:
**NOT_ALLOWED** - The webhook was created by a Marketplace extension and cannot be modified or deleted.
        - `details` (object) **REQ** — Represents the error details containing additional context about the marketplace webhook restriction.
          - `resource_path_index` (integer/int32) — Represents the index of the invalid resource in the request URL path for the marketplace webhook.
        - `message` (string) **REQ** [enum=['Webhook  is associated with MarketPlace']] — Represents the error message describing the failure.
Possible values:
**Webhook  is associated with MarketPlace** - The webhook was created by a Marketplace extension and cannot be modified or deleted by the requesting user.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
      - `WebhookAssociatedWithRulesError` — Represents the error returned when a request attempts to delete a webhook that is associated with at least one active Workflow Rule, Approval Process, or Blueprint.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this failure.
Possible values:
**NOT_ALLOWED** - The webhook cannot be modified because it is associated with an active automation rule.
        - `details` (object) **REQ** — Represents the error details identifying the resource path with the associated webhook.
          - `resource_path_index` (integer/int32) — Represents the index of the invalid resource in the request URL path.
        - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing the failure.
Possible values:
**This webhook is associated with at least one of Approval Process/Workflow Rules/Blueprint** - The webhook cannot be deleted or modified because it is actively linked to one or more automation rules.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
      - `ReadOnlyWebhookDeleteNotAllowedError` — Represents the error returned when a request attempts to delete a read-only webhook.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this failure.
Possible values:
**NOT_ALLOWED** - The read-only webhook cannot be deleted.
        - `details` (object) **REQ** — Represents the error details containing the webhook ID that cannot be deleted.
          - `id` (string) [maxLen=20] — Represents the ID of the read-only webhook that cannot be deleted.
        - `message` (string) **REQ** [enum=['Insufficient privileges to delete Read only webhook']] — Represents the error message describing the failure.
Possible values:
**Insufficient privileges to delete Read only webhook** - The requesting user does not have permission to delete this read-only webhook.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
        - `webhooks` (array of object `InvalidWebhookIdError`) [maxItems=1] **REQ** — Represents the array containing the error details for the invalid webhook ID in a single-record DELETE request.
          schema: `InvalidWebhookIdError`
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The webhook ID provided in the request is not valid.
          - `details` (object) **REQ** — Represents the error details identifying the field with the invalid webhook ID.
            - `api_name` (string) [maxLen=255] — Represents the API name of the field with the invalid webhook ID.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field with the invalid webhook ID.
          - `message` (string) **REQ** [enum=['The ID given is invalid']] — Represents the error message describing the failure.
Possible values:
**The ID given is invalid** - The webhook ID in the request does not match any existing webhook.
          - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
      - `InvalidWebhookIdPathError` — Represents the error returned when the webhook ID in the URL path is invalid or does not match an existing webhook.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The webhook ID provided in the path parameter is not valid.
        - `details` (object) **REQ** — Represents the error details identifying the resource with the invalid webhook ID.
          - `resource_path_index` (integer/int32) — Represents the index of the invalid resource in the request URL path.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message describing the failure.
Possible values:
**the id given seems to be invalid** - The webhook ID in the path does not match any existing webhook record.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.

- **403**: Permission denied to delete the specified webhook in this Zoho CRM organization.

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

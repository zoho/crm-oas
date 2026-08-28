# GET /settings/automation/webhooks/{webhookId}
**Operation:** `getWebhookById` — Get webhook by ID
> To retrieve the configuration of a specific webhook in your Zoho CRM organization using its ID.

Use the [Get Webhooks API](webhooks.yaml#$.paths./settings/automation/webhooks.get) first to discover webhook IDs.

**Parameters:**
- `webhookId` (path, string, required) [maxLen=20]: Specify the ID of the webhook to retrieve. Refer to the [Get Webhooks](webhooks.yaml#$.paths./settings/automation/webhooks.get) resource for valid values.

**Schemas:**
`UserDefinedParameter`:
  > A single user-defined parameter appended as a URL query parameter. Note: The API uses plural 'user_defined_parameters' here but singular 'user_defined_parameter' in form_data_content  - both are single objects, not arrays.
  - `name` (string) [maxLen=255] — Represents the key name of the user-defined parameter.
  - `value` (string) [maxLen=255] — Represents the value of the user-defined parameter.
`WebhookCustomParameters`:
  > Represents a static key-value parameter for webhook requests. Used in headers, URL query parameters, or form data fields. The value is a fixed literal sent unchanged with every webhook execution.
  - `name` (string) [maxLen=255] — Represents the parameter key sent in the webhook request.
  - `value` (string) [maxLen=255] — Represents the static literal value sent with every webhook execution.
`WebhookModuleParameters`:
  > Represents a module merge-field parameter for webhook requests. Used in headers, URL query parameters, or form data fields. The value is resolved at runtime from the field of the triggering CRM record.
  - `name` (string) [maxLen=255] — Represents the parameter key sent in the webhook request. The name must be unique within the parameter collection.
  - `value` (string) [maxLen=255] — Represents the merge-field token resolved at runtime from the triggering CRM record. Use the API field names and not display names (for example, use ${!Leads.Last_Name}, not ${!Leads.Last Name}). Invalid API names return INVALID_DATA.

**Responses:**

- **200**: Returns the full configuration of the specified webhook, including **headers**, **body**, **url_parameters**, **authentication**, and **date_time_format**. — Schema: `GetWebhookByIdSuccessResponse` [application/json]
    > Represents the success response for retrieving a single webhook by ID, including the full webhook configuration with headers, body, url_parameters, authentication, and date_time_format.
    schema: `GetWebhookByIdSuccessResponse`
    - `webhooks` (array of object `AutomationWebhooksResponse`) [maxItems=1] — Represents the list containing the single requested webhook object with its full configuration.
      schema: `AutomationWebhooksResponse`
      - `created_time` (string) [maxLen=255] — Represents the ISO 8601 timestamp of when the webhook was created.
      - `headers` (object `WebhookHeaders`) — Headers let you send extra information along with the webhook request. For example, API keys, authentication tokens, or custom values that the external application needs.
        schema: `WebhookHeaders`
        - `custom_parameters` (array of object `WebhookCustomParameters`) [maxItems=10, nullable] — Represents the static key-value pairs sent as HTTP headers with every webhook execution.
        - `module_parameters` (array of object `WebhookModuleParameters`) [maxItems=25, nullable] — Represents the module merge-field parameters sent as HTTP headers. The key must be present but may be an empty array when only custom parameters are needed.
      - `lock_status` (object `AutomationLockStatusResponse`) — Lock status of the webhook. Locked webhooks cannot be edited or deleted.
        schema: `AutomationLockStatusResponse`
        - `locked` (boolean) — Indicates whether the webhook is currently locked. Locked webhooks cannot be edited or deleted.
Possible values:
**true** - The webhook is locked.
**false** - The webhook is not locked.
        - `message` (string) [maxLen=255, nullable] — Represents the reason the webhook is locked. Returns null when the webhook is not locked.
      - `editable` (boolean) — Indicates whether the current user can edit this webhook. Returns false for marketplace and extension-created webhooks.
Possible values:
**true** - The webhook can be edited.
**false** - The webhook cannot be edited.
      - `module` (object `AutomationModuleDetailsResponse`) **REQ** — The parent CRM module that this webhook monitors for trigger events.
        schema: `AutomationModuleDetailsResponse`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM module (for example, Leads, Contacts, Deals).
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the CRM module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
      - `related_module` (object `RelatedModuleReference`) — The child or dependent CRM module linked to this webhook's parent module. Null when no related module is configured.
        schema: `RelatedModuleReference`
        - `api_name` (string) [maxLen=255] — Represents the API name of the related CRM module.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the related CRM module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
      - `url_parameters` (object `WebhookUrlParameters`) — URL parameters for GET/DELETE webhook HTTP methods. Null when http_method is POST or PUT.
        schema: `WebhookUrlParameters`
        - `custom_parameters` (array of object `WebhookCustomParameters`) [maxItems=10] — Represents the static key-value pairs appended as URL query parameters to every webhook request. Each entry must have a unique name.

- name (string, optional)

Specify a name to the custom header.


- value (string, optional)

Specify a value to the custom header.


"custom_parameters": [
    {
        "name": "OAuth",
        "value": "2.0"
    }
]. 


A maximum  of 10 entries is allowed.
        - `module_parameters` (array of object `WebhookModuleParameters`) [maxItems=25] — Represents the module merge-field parameters appended as URL query parameters. Values are resolved at runtime from the triggering CRM record using the merge-field format (for example, ${!Leads.Email}). Use the [Get Fields Metadata](fields.yaml#$.paths./settings/fields.get) resource to retrieve valid field API names.
        - `user_defined_parameters` (object `UserDefinedParameter`) — A single user-defined parameter appended as a URL query parameter. Note: The API uses plural 'user_defined_parameters' here but singular 'user_defined_parameter' in form_data_content  - both are single objects, not arrays.
      - `deletable` (boolean) — Indicates whether the current user can delete this webhook. Returns false for marketplace and extension-created webhooks.
Possible values:
**true** - The webhook can be deleted.
**false** - The webhook cannot be deleted.
      - `description` (string) [maxLen=255, nullable] — Represents the optional user-provided description of the webhook purpose. Returns null when no description has been set.
      - `source` (string) [maxLen=255, nullable] — Represents the origin of the webhook. Returns null for legacy webhooks.
Possible values:
**user** - Created by a CRM user.
**crm** - Created by the CRM system.
**extension** - Created by a Marketplace extension.
      - `body` (object `WebhookRequestBody`) — Define the data that Zoho CRM sends in the body of the webhook request. This is applicable only for POST and PUT HTTP methods
        schema: `WebhookRequestBody`
        - `format` (string) **REQ** [maxLen=25, enum=['JSON', 'XML', 'Text', 'HTML', None], nullable] — Specify the body content format.
Possible values:
**JSON** - JSON format.
**XML** - XML format.
**Text** - Plain text format.
**HTML** - HTML format.
**null** - Valid for form_data and none body types.
        - `raw_data_content` (string) [maxLen=500, nullable] — Represents the raw string content sent as the request body. This field is required when the body type is raw.
        - `type` (string) **REQ** [maxLen=255, enum=['form_data', 'raw', 'none']] — Specify the body type for the webhook request.
Possible values:
**form_data** - Sends data as key-value pairs in the request body.
**raw** - Sends plain text, JSON, HTML, or XML content directly.
**none** - No body content.
        - `form_data_content` (object `FormDataContent`) — Form data content when body type is form_data. Contains module parameters, custom parameters, and an optional user-defined parameter.
          schema: `FormDataContent`
          - `module_parameters` (array of object `WebhookModuleParameters`) [maxItems=25] — Represents the module merge-field parameters resolved at runtime and sent as form data in the webhook request.
          - `user_defined_parameter` (object `UserDefinedParameter`) — A single user-defined key-value parameter sent as a form data field. Note: The API uses singular 'user_defined_parameter' for form_data_content (this field) and plural 'user_defined_parameters' for url_parameters  - both are single objects, not arrays.
          - `custom_parameters` (array of object `WebhookCustomParameters`) [maxItems=10] — Represents the custom static key-value pairs sent as form data in the webhook request.
      - `created_by` (object `AutomationCreatedByResponse`) — The CRM user who created this webhook.
        schema: `AutomationCreatedByResponse`
        - `name` (string) [maxLen=255] — Represents the display name of the user who created the webhook.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the user who created the webhook. Refer to the [Get Users](users.yaml#$.paths./users.get) resource for valid values.
      - `url` (string) **REQ** [maxLen=255] — Represents the destination URL that Zoho CRM sends the webhook request to when triggered.
      - `feature_type` (string) **REQ** [maxLen=255] — Represents the automation feature type this webhook belongs to.
Possible values:
**workflow** - Workflow Rule.
**approval_process** - Approval Process.
**blueprint** - Blueprint.
**kiosk** - Kiosk feature.
**commandcenter_service** - CommandCenter service.
      - `http_method` (string) **REQ** [maxLen=255] — Represents the HTTP method used when the webhook fires.
Possible values:
**GET** - Sends a GET request to the webhook URL.
**POST** - Sends a POST request to the webhook URL.
**PUT** - Sends a PUT request to the webhook URL.
**DELETE** - Sends a DELETE request to the webhook URL.
      - `modified_time` (string) [maxLen=255] — Represents the ISO 8601 timestamp of when the webhook was last modified.
      - `associated` (boolean) — Indicates whether this webhook is currently associated with at least one active Workflow Rule, Approval Process, or Blueprint.
Possible values:
**true** - The webhook is associated with at least one automation rule.
**false** - The webhook is not associated with any automation rule.
      - `name` (string) **REQ** [maxLen=50] — Represents the display name of the webhook.
      - `modified_by` (object `AutomationModifiedByResponse`) — The CRM user who last modified this webhook.
        schema: `AutomationModifiedByResponse`
        - `name` (string) [maxLen=255] — Represents the display name of the user who last modified the webhook.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the user who last modified the webhook. Refer to the [Get Users](users.yaml#$.paths./users.get) resource for valid values.
      - `id` (string) [maxLen=20] — Represents the unique identifier of the webhook.
      - `date_time_format` (object `DateTimeFormatConfig`) — Date and time formatting configuration for this webhook's payloads. Null when no date/datetime merge-fields are used.
        schema: `DateTimeFormatConfig`
        - `datetime_format` (string) [maxLen=255] — Represents the format pattern for datetime merge-field values in the webhook payload.
        - `date_format` (string) [maxLen=255] — Represents the format pattern for date-only merge-field values in the webhook payload.
        - `time_zone` (string) [maxLen=255] — Represents the timezone identifier applied to datetime merge-field values in the webhook payload.
      - `authentication` (object `WebhookAuthenticationDetails`) — Specify authentication details for the webhook endpoint. (Required)
        schema: `WebhookAuthenticationDetails`
        - `connection_name` (string) [maxLen=255, nullable] — Represents the name of the Zoho connection used for authentication. This field is required only when **type** is **connection**.
        - `type` (string) **REQ** [maxLen=255, enum=['general', 'connection']] — Specify the authentication method for the webhook endpoint.
Possible values:
**general** - No credentials required.
**connection** - Uses a pre-configured Zoho connection.

- **204**: Returns no content when no webhook matches the specified ID. The request was valid, but the response body is empty.

- **403**: Permission denied to retrieve webhook details in this Zoho CRM organization.

**Resolution:** The CRM administrator must grant the Manage Webhook permission to the user's profile. — Schema: `NoPermissionErrorResponse` [application/json]
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

**Scopes:** ZohoCRM.settings.automation_actions.READ

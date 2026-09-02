# GET /settings/automation/webhooks
**Operation:** `getWebhooks` — Get webhooks
> To retrieve the list of all webhook action configurations available in your Zoho CRM organization. The response contains summary-level data for each webhook, including the module, URL, HTTP method, feature type, and audit metadata. Use the [Get Webhooks API using ID](webhooks.yaml#$.paths./settings/automation/webhooks/{webhook_ID}.get) to retrieve the full configuration of a specific webhook.

**Parameters:**
- `module` (query, string, optional) [maxLen=100]: Specify the API name of the parent CRM module to filter webhooks. When omitted, webhooks across all modules are returned. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
- `page` (query, integer/int32, optional) [min=1]: Specify the page number for paginated results. Defaults to 1 when omitted. Use together with per_page to navigate large result sets.
- `per_page` (query, integer/int32, optional) [min=1, max=200]: Specify the number of records to return per page. Default and maximum is **200**.
- `sort_by` (query, string, optional) [enum=['Modified_Time']]: Specify the field used to sort the webhook list. Currently only Modified_Time is accepted.
Possible values:
**Modified_Time** - Sort by the last modified timestamp.
- `sort_order` (query, string, optional) [enum=['asc', 'desc']]: Specify the sort direction for list results. Defaults to desc when omitted.
Possible values:
**asc** - Ascending order.
**desc** - Descending order.
- `feature_type` (query, string, optional) [enum=[7 values]]: Specify the automation feature type to filter webhooks. When omitted, webhooks of all feature types are returned.
Possible values:
**workflow** - Workflow Rule.
**approval_process** - Approval Process.
**blueprint_transition** - Blueprint transition.
**blueprint_state** - Blueprint state.
**assignment_rules** - Assignment Rules.
**kiosk** - Kiosk feature.
**commandcenter_service** - CommandCenter service.
- `related_module` (query, string, optional) [maxLen=100]: Specify the API name of a child or dependent module linked to the parent module (for example, Notes or Attachments). When omitted, webhooks across all related modules are returned.
- `filters` (query, string, optional) [maxLen=1000]: Specify the JSON filter expression to narrow webhook results by name. The object must include field (with api_name), comparator, and value keys. The only supported comparator is contains, which performs a case-insensitive partial match on the webhook name.

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

- **200**: Returns a paginated list of webhook summary objects configured in your Zoho CRM organization. Each item contains the module, URL, HTTP method, feature type, and audit metadata. Full configuration fields such as headers, body, authentication, url_parameters, and date_time_format are omitted from this response. — Schema: `GetWebhooksSuccessResponse` [application/json]
    > Represents the paginated success response for listing webhooks. Contains summary-level webhook objects without headers, body, authentication, or date_time_format details.
    schema: `GetWebhooksSuccessResponse`
    - `webhooks` (array of object `AutomationWebhooksResponse`) [maxItems=200] — Represents the list of webhook summary objects returned by the list operation.
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
    - `info` (object `PaginationInfoResponse`) — Pagination metadata for navigating the result set.
      schema: `PaginationInfoResponse`
      - `max_limit` (integer/int32) — Represents the maximum number of records allowed per page for this resource.
      - `per_page` (integer/int32) — Represents the number of records returned per page in the paginated response.
      - `count` (integer/int32) — Represents the total number of webhooks returned in the current page.
      - `page` (integer/int32) — Represents the current page number in the paginated response.
      - `more_records` (boolean) — Indicates whether additional pages of results are available.
Possible values:
**true** - More records exist beyond the current page.
**false** - The current page contains the last records.

- **400**: One or more query parameters contain invalid values.

**Resolution:** The module API name in the request must match a valid CRM module. The **sort_order**, **sort_by**, and **feature_type** values must match the supported enum values for this operation. [application/json]
    > Contains the error response for an invalid query parameter. Each variant in the union indicates which parameter was invalid and why.
    oneOf:
      - `InvalidModuleErrorResponse` — Represents the error returned when the module api_name provided in a query parameter does not match an existing CRM module.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for this failure.
Possible values:
**INVALID_MODULE** - The module API name provided in the request is not recognized.
        - `details` (object) **REQ** — Represents the error details containing the name of the parameter with the invalid module.
          - `param_name` (string) [maxLen=255] — Represents the name of the parameter that contains the invalid module API name.
        - `message` (string) **REQ** [enum=['The value provided to the param is Invalid']] — Represents the error message describing the failure.
Possible values:
**The value provided to the param is Invalid** - The module API name does not match any valid CRM module.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
      - `InvalidDataErrorResponse` — Represents the error returned when a query parameter value is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - A query parameter value provided in the request is not valid.
        - `details` (object) **REQ** — Represents the error details containing the name of the parameter with the invalid value.
          - `param_name` (string) [maxLen=255] — Represents the name of the parameter that contains the invalid value.
        - `message` (string) **REQ** [enum=['The value provided to the param is Invalid']] — Represents the error message describing the failure.
Possible values:
**The value provided to the param is Invalid** - The value submitted for the parameter does not match the expected format or allowed values.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.

- **403**: Permission denied to list webhooks in the Zoho CRM organization.

**Resolution:** The CRM administrator must grant the Manage Workflow permission to the user's profile.
 — Schema: `NoPermissionErrorResponse` [application/json]
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

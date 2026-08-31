# GET /settings/email_templates
**Operation:** `getEmailTemplates` — Email Templates
> To retrieve a paginated list of email templates accessible to the authenticated user in your Zoho CRM organization. The list can be scoped to a specific CRM module using the module parameter, filtered by category (such as favorite, draft, or created_by_me), and refined using a structured filter expression. Results are sortable by last_usage_time, modified_time, or name, and paginated using the page and per_page parameters.

**Parameters:**
- `module` (query, string, optional) [maxLen=255]: Provide the API name of the CRM module to filter Email Templates by. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for module API name.
- `per_page` (query, integer/int32, optional) [max=200, default=200]: Provide the maximum number of Email Template records to return per page. Default value is **200** and the maximum value is **200.**
- `page` (query, integer/int32, optional) [min=1, default=1]: Specify the page number to retrieve in a paginated response. The default value is <b>1</b>.

**Schemas:**
`ErrorItemBase`:
  > Represents the base structure for error response items, containing the code, message, status, and details fields.
  - `code` (string) **REQ** [maxLen=128] — Represents the error code identifier. 
  - `message` (string) **REQ** [maxLen=1024] — Represents the descriptive message explaining the error. 
  - `status` (string) **REQ** [enum=['error', 'warning', 'info']] — Represents the severity level of the error. 

Possible values:

**error** - The request resulted in an error.

**warning** - The request completed with a warning.

**info** - The response carries informational status.

  - `details` (object) **REQ** — Represents additional details about the error. 
`UserRef`:
  > Represents a reference to the Zoho CRM user associated with the Email Template.
  - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user. 
  - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the user. 

**Responses:**

- **200**: Returns a paginated list of email templates matching the specified criteria, along with pagination metadata. — Schema: `EmailTemplateListResponse` [application/json]
    > Successful response for email templates retrieval
    schema: `EmailTemplateListResponse`
    - `email_templates` (array of object `EmailTemplateListItem`) [maxItems=2000] **REQ** — Represents the list of email templates matching the request criteria. 
      schema: `EmailTemplateListItem`
      - `created_time` (string/date-time) **REQ** — Represents the timestamp indicating when Zoho CRM created the Email Template. 
      - `modified_time` (string/date-time) **REQ** — Represents the timestamp indicating when the Email Template was last modified. 
      - `last_usage_time` (string/date-time) **REQ** [nullable] — Represents the timestamp indicating when the Email Template was last used. 
      - `category` (string) **REQ** [enum=['normal', 'draft', 'marketplace', 'plugin', 'system_templates']] — Template category - normal, draft, marketplace, plugin, or default
      - `folder` (object `FolderRef`) **REQ** — Represents a reference to the folder in which the Email Template is stored.
        schema: `FolderRef`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the folder. 
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the folder. 
      - `module` (object `ModuleRef`) **REQ** — Represents a reference to the CRM module associated with the Email Template. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
        schema: `ModuleRef`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module.  Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the module. 
      - `created_by` (object `UserRef`) **REQ** — Represents a reference to the Zoho CRM user associated with the Email Template.
      - `modified_by` (object `UserRef`) **REQ** — Represents a reference to the Zoho CRM user associated with the Email Template.
      - `name` (string) **REQ** [maxLen=75] — Represents the display name of the Email Template. 
      - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the Email Template. 
      - `editor_mode` (string) **REQ** [enum=['plain_text', 'rich_text', 'gallery']] — Represents the editor mode used to create the Email Template. 
Possible values:
**plain_text** - The template uses plain text format.
**rich_text** - The template uses rich text format.
**gallery** - The template uses the gallery drag-and-drop editor.
      - `favorite` (boolean) **REQ** — Indicates whether the Email Template is marked as a favorite by the authenticated user. 
Possible values:
**true** - The template is marked as a favorite.
**false** - The template is not marked as a favorite.
      - `attachments` (array of object) [maxItems=10, nullable] **REQ** — Represents the list of attachments associated with the Email Template. 
        - `size` (string) **REQ** [maxLen=255] — Represents the size of the attachment file. 
        - `file_name` (string) **REQ** [maxLen=255] — Represents the name of the attachment file. 
        - `file_id` (string) **REQ** [maxLen=255] — Represents the unique ID of the attachment file in the Zoho CRM file store. 
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the attachment entry. 
      - `subject` (string) **REQ** [maxLen=250] — Represents the email subject line of the template. 
      - `associated` (boolean) **REQ** — Indicates whether the Email Template is currently associated with one or more CRM components. 
Possible values:
**true** - The template is associated with one or more CRM components.
**false** - The template is not associated with any CRM component.
      - `active` (boolean) **REQ** — Indicates whether the Email Template is active. 
Possible values:
**true** - The template is active.
**false** - The template is inactive/deleted.
      - `consent_linked` (boolean) **REQ** — Indicates whether this Email Template is linked to a consent form. 
Possible values:
**true** - The template is linked to a consent form.
**false** - The template is not linked to a consent form.
      - `last_version_statistics` (object) **REQ** — Represents the email delivery and engagement statistics from the most recent version of the template. 
        - `tracked` (integer/int32) **REQ** — Represents the number of emails sent using this template for which tracking is enabled. 
        - `delivered` (integer/int32) **REQ** — Represents the number of emails delivered successfully when sent using this template. 
        - `opened` (integer/int32) **REQ** — Represents the number of emails opened by recipients when sent using this template. 
        - `bounced` (integer/int32) **REQ** — Represents the number of emails that bounced when sent using this template. 
        - `sent` (integer/int32) **REQ** — Represents the total number of emails sent using this template. 
        - `clicked` (integer/int32) **REQ** — Represents the number of link clicks recorded in emails sent using this template. 
    - `info` (object `InfoBlock`) **REQ** — Represents the pagination metadata for the email templates list response.
      schema: `InfoBlock`
      - `per_page` (integer/int32) **REQ** — Represents the number of Email Template records returned per page. 
      - `page` (integer/int32) **REQ** — Represents the current page number of the paginated response. 
      - `count` (integer/int32) **REQ** — Represents the number of Email Template records returned in the current page. 
      - `more_records` (boolean) **REQ** — Indicates whether additional pages of results are available. 
Possible values:
**true** - More records are available on subsequent pages.
**false** - The current page contains the last available records.

- **204**: No Email Templates match the supplied criteria. The server returns no response body.

- **400**: The request contains an invalid parameter value or references a module that does not exist.
**Resolution:** Verify that the sort_order value is one of the supported options, the module API name is valid, and all filter expressions conform to the required format. — Schema: `GetEmailTemplates400Error` [application/json]
    > Single error item - can be one of multiple error types
    oneOf:
      - `ErrorItemMandatoryNotFoundForGet` — Represents an error item indicating that a required field is absent from a retrieval request.
        schema: `ErrorItemMandatoryNotFoundForGet`
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for the missing mandatory field. The value is **MANDATORY_NOT_FOUND**.
        - `message` (string) **REQ** [maxLen=1024] — Represents the error message describing the missing mandatory field.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status. The value is **error**.
        - `details` (object) **REQ** — None
          oneOf:
              additionalProperties: any
              - `parent_api_name` (string) **REQ** [maxLen=255] — Represents the API name of the parent module for the missing mandatory field.
      - `ErrorItemInvalidDataForGet` — Represents an error item indicating that the provided data or module reference is invalid for a retrieval request.
        schema: `ErrorItemInvalidDataForGet`
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'INVALID_MODULE']] — Represents the error code for the invalid data or module condition. 

Possible values:

**INVALID_DATA** - The provided data is invalid.

**INVALID_MODULE** - The specified module does not exist or is not accessible.

        - `message` (string) **REQ** [maxLen=1024] — Represents the error message describing the invalid data.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status. The value is **error**.
        - `details` (object) **REQ** — Represents additional details about the invalid data error. 
      - `ErrorItemPatternNotMatchedForGet` — Represents an error item indicating that a field value does not match the required pattern in a retrieval request.
        schema: `ErrorItemPatternNotMatchedForGet`
        - `code` (string) **REQ** [enum=['PATTERN_NOT_MATCHED']] — Represents the error code indicating that a value does not match the required pattern. 
Possible values:
**PATTERN_NOT_MATCHED** - The provided value does not conform to the expected format.
        - `message` (string) **REQ** [maxLen=1024] — Represents the error message describing the pattern mismatch.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status. The value is **error**.
        - `details` (object) **REQ** — Represents additional details identifying the field that failed pattern validation. 
          oneOf:
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field whose value did not match the required pattern. 
              additionalProperties: any
      - `ErrorItemInvalidRequest` — Represents an error item indicating that the request payload is invalid or cannot be parsed.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status of the request. 
Possible values:
**error** - The request resulted in an error.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST', 'JSON_PARSE_ERROR', 'INVALID_MODULE']] — Represents the error code for the invalid request condition. 

Possible values:

**INVALID_REQUEST** - The request payload is invalid.

**JSON_PARSE_ERROR** - The request body could not be parsed as valid JSON.

**INVALID_MODULE** - The specified module does not exist or is not accessible.

        - `message` (string) **REQ** [maxLen=1024] — Represents the descriptive error message for the invalid request. 
        - `details` (object) **REQ** — Represents additional details about the invalid request error. 

**Scopes:** ZohoCRM.templates.email.READ

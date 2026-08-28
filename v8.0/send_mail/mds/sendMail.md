# POST /{moduleName}/{id}/actions/send_mail
**Operation:** `sendMail` — Send an email to a record
> To send an email to a specific record in your Zoho CRM organization using a template or custom email content.

**Parameters:**
- `moduleName` (path, string, required) [maxLen=100]: Specify the API name of the Zoho CRM module for which the record exists. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values. Supported modules: Leads, Contacts, Deals, Accounts, Sales Orders, Purchase Orders, Invoices, Quotes, Cases, Vendors, and Custom Modules.
- `id` (path, string, required) [maxLen=100]: Specify the unique ID of the record to send the email to.

**Schemas:**
`EmailUser`:
  > Represents an email user with an email address and an optional display name.
  - `user_name` (string) [maxLen=255] — Represents the display name of the user.
  - `email` (string) **REQ** [maxLen=255] — Represents the email address of the user.
`FlatErrorResponse`:
  > Represents a flat (non-array) error response returned when a request-level error occurs.
  - `code` (string) **REQ** [maxLen=100] — Represents the error code for the request failure. Always returned in the response.
  - `details` (object) — Represents additional context about the error.
  - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the failure. Always returned in the response.
  - `status` (string) [maxLen=100] — Represents the status of the error response.

**Request Body** (required) — application/json `SendMailRequest`
> The request body must contain a data array with one object.
  > Represents the top-level request body for the Send Mail API, containing the email configuration objects.
  - `data` (array of object) [maxItems=1] **REQ** — Contains the list of email configuration objects to send.
    - `from` (object `EmailUser`) **REQ** — Represents an email user with an email address and an optional display name.
    - `to` (array of object `EmailUser`) [maxItems=50] **REQ** — Represents the list of primary recipients of the email.
    - `cc` (array of object `EmailUser`) [maxItems=50] — Represents the list of CC (carbon copy) recipients for the email.
    - `bcc` (array of object `EmailUser`) [maxItems=50] — Represents the list of BCC (blind carbon copy) recipients for the email.
    - `reply_to` (object `EmailUser`) — Represents an email user with an email address and an optional display name.
    - `subject` (string) [maxLen=1000] — Represents the subject line of the email.
    - `content` (string) [maxLen=100000] — Represents the body content of the email.
    - `mail_format` (string) [enum=['html', 'text']] — Represents the format of the email body. Possible values: **html** - HTML-formatted email. **text** - Plain text email.
    - `org_email` (boolean) — Indicates whether to send the email using the organization email address instead of the sender individual email address. Possible values: **true** - Sends the email using the organization email address. **false** - Sends the email using the sender individual email address.
    - `scheduled_time` (string/date-time) — Represents the scheduled date and time to send the email, in ISO 8601 date-time format.
    - `consent_email` (boolean) — Indicates whether the email is a GDPR consent email. Possible values: **true** - The email is a GDPR consent request. **false** - The email is not a GDPR consent request.
    - `template` (object) — Represents the Email Template to use for the email. Refer to the [Get Email Templates](email_templates.yaml#$.paths./settings/email_templates.get) resource for valid values.
      - `id` (string) [maxLen=100] — Represents the unique identifier of the Email Template. Refer to the [Get Email Templates](email_templates.yaml#$.paths./settings/email_templates.get) resource for valid values.
    - `inventory_details` (object) — Represents the inventory template details to attach to the email.
      - `inventory_template` (object) — Represents the inventory template to attach to the email. Refer to the [Get Inventory Templates](inventory_templates.yaml#$.paths./settings/inventory_templates.get) resource for valid values.
        - `id` (string) [maxLen=100] — Represents the unique identifier of the inventory template. Refer to the [Get Inventory Templates](inventory_templates.yaml#$.paths./settings/inventory_templates.get) resource for valid values.
        - `name` (string) [maxLen=100] — Represents the name of the inventory template.
      - `paper_type` (string) [enum=['default', 'A4', 'us_letter']] — Represents the paper size for the inventory template attachment. Possible values: **default** - Uses the default paper size. **A4** - A4 paper size. **us_letter** - US Letter paper size.
      - `view_type` (string) [enum=['portrait', 'landscape']] — Represents the page orientation for the inventory template attachment. Possible values: **portrait** - Portrait orientation. **landscape** - Landscape orientation.
    - `data_subject_request` (object) — Represents the GDPR data subject request associated with the email.
      - `id` (string) [maxLen=100] — Represents the unique identifier of the GDPR data subject request.
      - `type` (string) [enum=['access', 'rectify', 'export']] — Represents the type of GDPR data subject request. Possible values: **access** - A data access request. **rectify** - A data rectification request. **export** - A data export request.
    - `attachments` (array of object) [maxItems=10] — Represents the list of files to attach to the email, referenced by their Zoho File System (ZFS) IDs.
      - `id` (string) [maxLen=255] — Represents the unique identifier of the file in the Zoho File System (ZFS).

**Responses:**

- **200**: Returns the result of the email send operation, including a status code and message for each email. — Schema: `SuccessResponse` [application/json]
    > Represents the response returned after the email sends successfully.
    schema: `SuccessResponse`
    - `data` (array of object) [maxItems=10] — Represents the list of mail-send results, one item per email request.
      - `code` (string) [enum=['SUCCESS']] — Represents the status code for the send operation. Possible values: **SUCCESS** - The email was sent successfully.
      - `status` (string) [enum=['success']] — Represents the status of the email send operation. Possible values: **success** - The email was sent successfully.
      - `message` (string) [maxLen=500] — Represents the status message for the send operation.
      - `details` (object) — Represents additional metadata returned for the send operation, including the message identifier.
        - `message_id` (string) [maxLen=255] — Represents the unique message identifier assigned to the sent email.

- **400**: The request contains invalid or missing field values. **Resolution:** The required fields must be present in the request and all field values must be valid. [application/json]
    oneOf:
      - `StandardErrorResponse` — Represents a standard error response that wraps one or more error detail objects in a data array.
        - `data` (array of object `ErrorDetail`) [maxItems=10] **REQ** — Represents the list of error details returned for the failed request. Always returned in the response.
          schema: `ErrorDetail`
          - `code` (string) [maxLen=100] — Represents the error code for the specific issue encountered.
          - `details` (object) — Represents additional context about the error.
          - `message` (string) [maxLen=1000] — Represents the error message describing the issue.
          - `status` (string) [maxLen=100] — Represents the status of the error response.
      - `FlatErrorResponse` — Represents a flat (non-array) error response returned when a request-level error occurs.

- **403**: Permission denied to send email using this account. **Resolution:** The CRM administrator must grant the required permission to the user's profile, and the OAuth token must include the ZohoCRM.send_mail.all.CREATE scope. — Schema: `FlatErrorResponse` [application/json]
    > Represents a flat (non-array) error response returned when a request-level error occurs.

**Scopes:** ZohoCRM.send_mail.all.CREATE

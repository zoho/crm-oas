# GET /{module}/{recordId}/Emails/actions/download_attachments
**Operation:** `downloadEmailAttachments` — Download an email attachment
> To download the binary content of an attachment that belongs to an email associated with a record in your Zoho CRM organization.

**Parameters:**
- `module` (path, string, required) [maxLen=100]: Specify the API name of the CRM module that contains the record associated with the email. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for module details.
- `recordId` (path, string, required) [maxLen=20]: Specify the unique ID of the record that the email is associated with.
- `user_id` (query, integer/int64, required): Specify the unique ID of the user who sent the email. Refer to the [Get Users](users.yaml#$.paths./users.get) resource for valid values.
- `message_id` (query, string, required) [maxLen=500]: The message ID you get in the response when you send an email. Refer to the "message_id" key in the response of [Send Mail API](send_mail.yaml#$.paths.//{moduleName}/{id}/actions/send_mail.post) or [Get Emails](emails.yaml#$.paths./{moduleApiName}/{id}/Emails.get) of a Record API to get the message ID.
- `id` (query, string, required) [maxLen=1000]: Specify the unique ID of the attachment to download.
- `name` (query, string, required) [maxLen=150]: Specify the file name of the attachment to download. You can get this from the response of [Get Emails API](emails.yaml#$.paths./{moduleApiName}/{id}/Emails.get).

**Responses:**

- **200**: Returns the binary content of the requested email attachment as an octet stream. [application/octet-stream]
    > Represents the binary content of the requested email attachment, returned as an octet stream.
    type: string/binary — Represents the binary content of the requested email attachment, returned as an octet stream.

- **400**: The request is missing a mandatory parameter or contains an invalid parameter value.
**Resolution:** The mandatory query parameters (**user_id**, **message_id**, **id**, and **name**) must be provided with valid values, and the **module** and **record_ID** path parameters must reference an existing record.
 [application/json]
    > Represents the error payload returned when the request missed a mandatory parameter or fails validation.
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Represents the outcome of the request. 
**Possible values:**
**error** - Indicates that the request failed.

        - `code` (string) **REQ** [maxLen=50] — Represents the error code that identifies the specific validation failure.
        - `message` (string) **REQ** [maxLen=500] — Represents the message describing the cause of the validation failure. 
        - `details` (object) — Contains additional contextual information about the validation failure, such as the parameter or field that triggered the error.
        - `status` (string) **REQ** [enum=['error']] — Represents the outcome of the request. 
Possible values:
**error** - Indicates that the request failed.

        - `code` (string) **REQ** [const=MANDATORY_NOT_FOUND] — Represents the error code indicating that a mandatory parameter was not provided in the request. Always returned in the response.
Possible values:
**MANDATORY_NOT_FOUND** - Indicates that one or more mandatory parameters are missing from the request.

        - `message` (string) **REQ** [maxLen=500] — Represents the message describing which mandatory parameter is missing from the request. 

- **401**: The OAuth access token supplied in the request is invalid or has expired.
**Resolution:** A new access token must be generated with the required scopes for this API.
 — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response returned by Zoho CRM APIs, containing the failure status, code, message, and contextual details.
    schema: `ErrorResponse`
    - `status` (string) **REQ** [enum=['error']] — Represents the outcome of the request.
Possible values:
**error** - Indicates that the request failed.

    - `code` (string) **REQ** [maxLen=100] — Represents the error code that identifies the specific failure condition. 
    - `message` (string) **REQ** [maxLen=1000] — Represents the message describing the cause of the failure. 
    - `details` (object) — Contains additional contextual information about the failure, such as the parameter name or field that triggered the error.

**Scopes:** ZohoCRM.modules.emails.READ, ZohoCRM.modules.leads.READ

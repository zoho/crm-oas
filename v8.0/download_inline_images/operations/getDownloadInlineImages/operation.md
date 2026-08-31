# GET /{module}/{recordId}/Emails/actions/download_inline_images
**Operation:** `getDownloadInlineImages` — Download an inline image from an email
> To download an inline image embedded in an email associated with a record in your Zoho CRM organization.

**Parameters:**
- `module` (path, string, required) [maxLen=50]: Specify the API name of the module to which the record belongs. Supported modules include Leads, Accounts, Contacts, Deals, Quotes, Invoices, Sales Orders, Purchase Orders, and custom modules.
- `recordId` (path, string, required) [maxLen=100]: Specify the unique ID of the record associated with the email containing the inline image.
- `user_id` (query, integer/int64, required): The unique ID of the record owner whose email you want to retrieve. Use the [Get Users API](users.yaml#$.paths./users.get) to get the user's ID.
- `message_id` (query, string, required) [maxLen=500]: Specify the message ID of the email containing the inline image. Refer to the **message_id** key in the response of [Send Mail API](send_mail.yaml#$.paths./{moduleName}/{id}/actions/send_mail.post) or [Get Emails API](emails.yaml#$.paths./{moduleApiName}/{id}/Emails.get) to obtain this ID.
- `id` (query, string, required) [maxLen=1000]: Specify the unique ID of the inline image to download. Refer to the **img_id** property in the **content** key of the [Get Emails API](emails.yaml#$.paths./{moduleApiName}/{id}/Emails.get) response to obtain this ID.

**Responses:**

- **200**: Returns the binary data of the requested inline image file. [image/png]
    > Contains the binary data of the inline image file embedded in the email.
    type: string/binary — Contains the binary data of the inline image file embedded in the email.

- **400**: The request contains invalid parameters or references an invalid module.
**Resolution:** Ensure that you have provided valid values to the parameters and module name.
 [application/json]
    > Represents the error response returned when the inline image download request fails due to invalid parameters or missing data.
    - `status` (string) **REQ** [enum=['error']] — Indicates the outcome of the API request. 
Possible values:
**error** - The request failed due to an error condition.

    - `code` (string) **REQ** [enum=[6 values]] — Represents the error code identifying the type of issue. 
Possible values:
**INVALID_URL_PATTERN** - The request URL format is incorrect.
**INVALID_DATA** - The provided data is invalid.
**INVALID_REQUEST_METHOD** - The HTTP method is not supported for this endpoint.
**INVALID_TOKEN** - The access token is invalid or expired.
**INVALID_MODULE** - The specified module does not exist or is not accessible.
**REQUIRED_PARAM_MISSING** - A required parameter is missing from the request.

    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the issue. 
    - `details` (object) **REQ** — Contains additional context about the error, such as the specific field or parameter that caused the issue. 
      - `resource_path_index` (integer/int32) — Represents the zero-based index of the path segment in the request URL that caused the error.
      additionalProperties: any

**Scopes:** ZohoCRM.modules.emails.READ, ZohoCRM.modules.leads.all, ZohoCRM.modules.contacts.all, ZohoCRM.modules.deals.all

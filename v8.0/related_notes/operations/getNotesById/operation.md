# GET /{parentRecordModule}/{parentRecordId}/Notes/{noteId}
**Operation:** `getNotesById` — Specific Related Note
> Retrieves details of a specific note record associated with a CRM record in your Zoho CRM organization.

**Parameters:**
- `parentRecordModule` (path, string, required) [maxLen=50, pattern=^[A-Za-z_][A-Za-z0-9_]*$]: Specify the API name of the parent record module. Refer to [Get Modules](modules.yaml#$.paths./settings/modules.get) for the list of supported modules.
- `parentRecordId` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique numeric ID of the parent record.
- `noteId` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique numeric ID of the note record.

**Responses:**

- **200**: Returns the details of the specified note. [application/json]
    > Response payload containing the details of the requested note record.
    - `data` (array of object) [maxItems=1] **REQ** — JSON array representing the list containing the requested note record.
      - `id` (string/int64) **REQ** — Represents the unique identifier of the note.
      - `Note_Title` (string) [maxLen=120, nullable] — Represents the title of the note.
      - `Note_Content` (string) [maxLen=65535, nullable] — Represents the content of the note.
      - `$attachments` (array of object) [maxItems=50, nullable] — Represents the list of file attachments associated with the note.
        - `$file_id` (string) [maxLen=255] — Represents the unique file identifier of the attachment.
        - `File_Name` (string) [maxLen=255] — Represents the name of the attached file.
        - `Size` (string/int64) — Represents the size of the attached file in bytes.
        - `id` (string/int64) — Represents the unique identifier of the attachment record.
        additionalProperties: any
      - `Parent_Id` (object) — Represents the parent record associated with the note.
        - `module` (object) **REQ** — Represents the module of the parent record.
          - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the parent record module. Refer to [Get Modules](modules.yaml#$.paths./settings/modules.get) for the list of supported modules.
          - `id` (string/int64) **REQ** — Represents the unique identifier of the parent record module.
        - `name` (string) [maxLen=255] — Represents the name of the parent record.
        - `id` (string/int64) **REQ** — Specify the unique ID of the parent record. Refer to Refer the [GET Records API](record.yaml#.$path./{module}.get) to get valid record IDs.
      additionalProperties: any

- **204**: The request was successful but there are no notes to return for the specified parent record.

- **400**: The request parameters are invalid. Resolution: Ensure the module name, parent record ID, and note ID in the path are valid. — Schema: `BadRequestError` [application/json]
    > Error response for single note retrieval failures
    schema: `BadRequestError`
    - `code` (string) **REQ** [enum=['INVALID_MODULE', 'INVALID_DATA', 'NOT_SUPPORTED']] — Represents the error code for this response.
    - `details` (object) **REQ** — Contains additional details about the error.
    - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
    - `status` (string) **REQ** [enum=['error']] — Indicates the status of the response.

- **401**: Authentication failed. Resolution: Verify that the OAuth token is valid and that the required scope is included. [application/json]
    > Error response schema for 401 Unauthorized responses.
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE', 'OAUTH_SCOPE_MISMATCH']] — Represents the error code for this response.
    - `details` (object) **REQ** — Contains additional details about the error.
    - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

- **404**: The requested resource could not be found. Resolution: Verify that the URL pattern in the request is correct. [application/json]
    > Error response schema for 404 Not Found responses.
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code for this response.
    - `details` (object) **REQ** — Contains additional details about the error.
    - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
    - `status` (string) **REQ** [enum=['error']] — Indicates status of the response.

- **500**: An unexpected error occurred on the server. Resolution: Retry the request after a brief delay. If the error persists, contact Zoho CRM support. [application/json]
    > Error response schema for 500 Internal Server Error responses.
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Represents the error code for this response.
    - `details` (object) **REQ** — Contains additional details about the error.
    - `message` (string) **REQ** [maxLen=500] — Specifies the error message for this response.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

**Scopes:** ZohoCRM.modules.Leads.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Contacts.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Accounts.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Deals.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Tasks.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Events.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Calls.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Products.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Vendors.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Campaigns.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Cases.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Solutions.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Pricebooks.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Quotes.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Salesorders.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Purchaseorders.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Custom.READ, ZohoCRM.modules.notes.READ

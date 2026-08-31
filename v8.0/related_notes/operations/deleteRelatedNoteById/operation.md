# DELETE /{parentRecordModule}/{parentRecordId}/Notes/{noteId}
**Operation:** `deleteRelatedNoteById` — Related Note
> Deletes a specific note record associated with a parent record using the note ID in the path.

**Parameters:**
- `parentRecordModule` (path, string, required) [maxLen=50, pattern=^[A-Za-z_][A-Za-z0-9_]*$]: Specify the API name of the parent record module. Refer to [Get Modules](modules.yaml#$.paths./settings/modules.get) for the list of supported modules.
- `parentRecordId` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique numeric ID of the parent record.
- `noteId` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique numeric ID of the note record.

**Responses:**

- **200**: Returns the action status for the deleted note. [application/json]
    > Success response for single note deletion, containing the action status and identifier of the deleted note.
    - `data` (array of object) [maxItems=200] **REQ** — A JSON array representing the list of action status objects for the deleted note.
      - `code` (string) **REQ** [enum=['SUCCESS']] — The result code indicating the outcome of the requested note deletion.
      - `message` (string) **REQ** [maxLen=500] — Represents the result message for deleting the requested note.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of this note deletion.
      - `details` (object) **REQ** — Contains the details of the deleted note record.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the deleted note.

- **400**: The request parameters are invalid. Resolution: Ensure the module name, parent record ID, and note ID in the path are valid. — Schema: `BadRequestError` [application/json]
    > Error response for single note deletion failures
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

**Scopes:** ZohoCRM.modules.Leads.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Contacts.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Accounts.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Deals.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Tasks.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Events.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Calls.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Products.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Vendors.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Campaigns.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Cases.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Solutions.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Pricebooks.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Quotes.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Salesorders.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Purchaseorders.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Custom.READ, ZohoCRM.modules.notes.DELETE

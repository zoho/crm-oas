# GET /{moduleApiName}/{recordId}/Attachments
**Operation:** `getAttachments` — Retrieve All Attachments
> Retrieves all attachments associated with a specific record in a module.

**Parameters:**
- `recordId` (path, string, required) [maxLen=64]: Specify the unique identifier of the record. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve record IDs.

- `moduleApiName` (path, string, required) [maxLen=64]: Specify the API name of the module (e.g., `Leads`, `Contacts`, `Accounts`). Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module API names.

- `fields` (query, string, optional) [maxLen=100000]: Specify the fields to retrieve. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to retrieve the field IDs.

**Schemas:**
`ErrorResponse`:
  > Generic error response structure
  - `status` (string) **REQ** [enum=['error']] — Represents the error status.
  - `code` (string) **REQ** [enum=[10 values]] — Represents the error code.
  - `message` (string) **REQ** [enum=[12 values]] — Represents the error message.
  - `details` (object) **REQ** — Represents the additional error details.
    - `param_name` (string) [maxLen=100] — Represents the name of the parameter causing the error.
    - `resource_path_index` (integer/int32) — Represents the index of the resource path causing the error

**Responses:**

- **200**: Successfully retrieved list of attachments — Schema: `AttachmentListResponse` [application/json]
    > Response containing list of attachments for a record
    schema: `AttachmentListResponse`
    - `data` (array of object `AttachmentObject`) [maxItems=1000] **REQ** — Array of attachment objects
      schema: `AttachmentObject`
      - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Represents the unique numeric identifier of the attachment
      - `File_Name` (string) [maxLen=250] — Represents the name of the attached file
      - `Size` (string) [maxLen=50000, pattern=^[0-9]+$] — Represents the size of the attachment in bytes
      - `Created_Time` (string/date-time) **REQ** — Represents the timestamp when the attachment was created (ISO 8601 with timezone)
      - `Created_By` (object) **REQ** — User who created the attachment.
        - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — User ID. Use the [Users API](users.yaml#$.paths./users/bulk.get) to retrieve user IDs.

        - `name` (string) **REQ** [maxLen=250] — Represents the user display name
        - `email` (string/email) [maxLen=100] — Represents the user email address
      - `Modified_Time` (string/date-time) **REQ** — Represents the timestamp when the attachment was last modified (ISO 8601 with timezone)
      - `Modified_By` (object) **REQ** — User who last modified the attachment.
        - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — User ID. Use the [Users API](users.yaml#$.paths./users/bulk.get) to retrieve user IDs.

        - `name` (string) **REQ** [maxLen=250] — Represents the user display name
        - `email` (string/email) [maxLen=100] — Represents the user email address
      - `Owner` (object) — Owner of the attachment
        - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Owner user ID. Use the [Users API](users.yaml#$.paths./users/bulk.get) to retrieve user IDs.

        - `name` (string) **REQ** [maxLen=250] — Represents the owner display name
        - `email` (string/email) [maxLen=100] — Represents the owner email address
      - `Parent_Id` (object) — Parent record information
        - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Parent record ID. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve record IDs.

        - `name` (string) **REQ** [maxLen=250] — Represents the parent record name
      - `$field_states` (object) [nullable] — Represents the field states metadata
      - `$editable` (boolean) — Indicates if the attachment is editable
      - `$file_id` (string) [maxLen=255, nullable] — Represents the file identifier for the attachment
      - `$type` (string) [maxLen=50] — Represents the type of the attachment. Possible values: `File` for uploaded files, or `Link URL` for URL-based attachments.
      - `$se_module` (string) [maxLen=100] — Represents the source module name
      - `$state` (string) [maxLen=50] — Represents the current state of the attachment
      - `$link_url` (string/uri) [maxLen=2000, nullable] — Represents the URL for link-type attachments. Null for file attachments.
      - `$sharing_permission` (string) [maxLen=50] — Represents the sharing permission level for the attachment
    - `info` (object `Info`) **REQ** — Pagination information for list responses
      schema: `Info`
      - `per_page` (integer/int32) **REQ** [min=1, max=200] — Represents the number of records per page
      - `next_page_token` (string) **REQ** [maxLen=1024, nullable] — Represents the token to retrieve the next page of results
      - `count` (integer/int32) **REQ** [min=0] — Represents the number of records returned in the current response
      - `page` (integer/int32) **REQ** [min=1] — Represents the current page number
      - `previous_page_token` (string) **REQ** [maxLen=1024, nullable] — Represents the token to retrieve the previous page of results
      - `page_token_expiry` (string/date-time) **REQ** [nullable] — Represents the expiry timestamp for the page tokens
      - `more_records` (boolean) **REQ** — Indicates whether more records are available

- **400**: Bad request - invalid input parameters or request body — Schema: `ErrorResponse` [application/json]
    > Generic error response structure

- **401**: Unauthorized - authentication credentials are missing or invalid — Schema: `ErrorResponse` [application/json]
    > Generic error response structure

- **403**: Forbidden - insufficient permissions to perform the operation — Schema: `ErrorResponse` [application/json]
    > Generic error response structure

- **404**: Not found - the specified record or attachment does not exist — Schema: `ErrorResponse` [application/json]
    > Generic error response structure

- **429**: Too many requests - rate limit exceeded — Schema: `ErrorResponse` [application/json]
    > Generic error response structure

- **500**: Internal server error - unexpected server failure — Schema: `ErrorResponse` [application/json]
    > Generic error response structure

- **503**: Service unavailable - server is temporarily unable to handle the request — Schema: `ErrorResponse` [application/json]
    > Generic error response structure

**Scopes:** ZohoCRM.modules.attachments.READ, ZohoCRM.modules.attachments.ALL

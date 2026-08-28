# POST /{moduleApiName}/{recordId}/Attachments
**Operation:** `uploadAttachment` — Upload an Attachment
> Uploads an attachment by providing either a file or a valid URL. Maximum request body size: 100MB.

**Parameters:**
- `recordId` (path, string, required) [maxLen=64]: Specify the unique identifier of the record. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve record IDs.

- `moduleApiName` (path, string, required) [maxLen=64]: Specify the API name of the module (e.g., `Leads`, `Contacts`, `Accounts`). Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module API names.


**Schemas:**
`ErrorResponse`:
  > Generic error response structure
  - `status` (string) **REQ** [enum=['error']] — Represents the error status.
  - `code` (string) **REQ** [enum=[10 values]] — Represents the error code.
  - `message` (string) **REQ** [enum=[12 values]] — Represents the error message.
  - `details` (object) **REQ** — Represents the additional error details.
    - `param_name` (string) [maxLen=100] — Represents the name of the parameter causing the error.
    - `resource_path_index` (integer/int32) — Represents the index of the resource path causing the error

**Request Body** (required) — multipart/form-data
> Request payload for uploadAttachment. Provide multipart form-data fields as documented for this operation.
  oneOf:
      - `file` (string/binary) **REQ** — The file to upload as an attachment
      - `attachmentUrl` (string) **REQ** [maxLen=3000] — The URL of the attachment to be linked
      - `title` (string) [maxLen=255, minLen=1, nullable] — Optional title for the attachment

**Responses:**

- **200**: Attachment uploaded successfully — Schema: `AttachmentSuccessResponse` [application/json]
    > Successful attachment operation response
    schema: `AttachmentSuccessResponse`
    - `data` (array of object) [maxItems=100] **REQ** — Array of upload results
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the response code
      - `details` (object) **REQ** — Details of the uploaded attachment
        - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Represents the attachment identifier
        - `Modified_Time` (string/date-time) **REQ** — Represents the last modification timestamp
        - `Created_Time` (string/date-time) **REQ** — Represents the creation timestamp
        - `Modified_By` (object) **REQ** — Represents the user who last modified the attachment
          - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Represents the user ID
          - `name` (string) **REQ** [maxLen=250] — Represents the user display name
        - `Created_By` (object) **REQ** — Represents the user who created the attachment
          - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — User ID. Use the [Users API](users.yaml#$.paths./users/bulk.get) to retrieve user IDs.

          - `name` (string) **REQ** [maxLen=250] — Represents the user display name
      - `message` (string) **REQ** [enum=['attachment uploaded successfully']] — Represents the success message
      - `status` (string) **REQ** [enum=['success']] — Represents the operation status

- **400**: Bad request - invalid input parameters or request body — Schema: `ErrorResponse` [application/json]
    > Generic error response structure

- **401**: Unauthorized - authentication credentials are missing or invalid — Schema: `ErrorResponse` [application/json]
    > Generic error response structure

- **403**: Forbidden - insufficient permissions to perform the operation — Schema: `ErrorResponse` [application/json]
    > Generic error response structure

- **404**: Not found - the specified record or attachment does not exist — Schema: `ErrorResponse` [application/json]
    > Generic error response structure

- **413**: Request entity is too large, file size exceeds 100MB limit — Schema: `BodySizeLimitError` [application/json]
    > Error response for body size limit exceeded
    schema: `BodySizeLimitError`
    - `status` (string) **REQ** [enum=['error']] — Represents the error status.
    - `code` (string) **REQ** [enum=['BODY_SIZE_REACHED', 'FILE_SIZE_MORE_THAN_ALLOWED_SIZE']] — Represents the error code
    - `message` (string) **REQ** [enum=[3 values]] — Represents the error message
    - `details` (object) **REQ** — Represents the additional error details

- **429**: Too many requests - rate limit exceeded — Schema: `ErrorResponse` [application/json]
    > Generic error response structure

- **500**: Internal server error - unexpected server failure — Schema: `ErrorResponse` [application/json]
    > Generic error response structure

- **503**: Service unavailable - server is temporarily unable to handle the request — Schema: `ErrorResponse` [application/json]
    > Generic error response structure

**Scopes:** ZohoCRM.modules.attachments.CREATE, ZohoCRM.modules.attachments.ALL

# GET /{moduleApiName}/{recordId}/Attachments/{id}
**Operation:** `getAttachmentById` — Download a specific attachment file
> Download the file content of a specific attachment by its ID. This endpoint returns the actual file (image, PDF, document, etc.). Returns an error for link attachments, as they cannot be downloaded.

**Parameters:**
- `recordId` (path, string, required) [maxLen=64]: Specify the unique identifier of the record. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve record IDs.

- `moduleApiName` (path, string, required) [maxLen=64]: Specify the API name of the module (e.g., `Leads`, `Contacts`, `Accounts`). Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module API names.

- `id` (path, string, required) [maxLen=64]: Specify the unique identifier of the attachment. Use the [Get Attachments](attachments.yaml#$.paths./{moduleApiName}/{recordId}/Attachments.get) resource to retrieve attachment IDs.


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

- **200**: Successfully downloaded attachment file [application/octet-stream] (also: image/png, image/jpeg, application/pdf)
    > The binary content of the attachment file
    type: string/binary — The binary content of the attachment file
  *Alt schema for image/png*:
      type: string/binary — PNG image file
  *Alt schema for image/jpeg*:
      type: string/binary — JPEG image file
  *Alt schema for application/pdf*:
      type: string/binary — PDF document file

- **204**: No Content - Invalid attachment ID

- **400**: Bad request - invalid parameters or link attachment download attempt [application/json]
    > Wrapper for get attachment by ID error responses
    oneOf:
        - `code` (string) **REQ** [enum=['DOWNLOAD_NOT_ALLOWED']] — Represents the error code
        - `details` (object) **REQ** — Represents the additional error details
          - `param_name` (string) [maxLen=100] — Represents the name of the missing parameter
        - `message` (string) **REQ** [enum=['As it is a linked attachment, you can not download it']] — Represents the error message
        - `status` (string) **REQ** [enum=['error']] — Represents the error status
        - `status` (string) **REQ** [enum=['error']] — Represents the error status
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `message` (string) **REQ** [enum=['the related id given seems to be invalid']] — Error message
        - `details` (object) **REQ** — Represents the additional error details
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path causing the error
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code
        - `details` (object) **REQ** — Represents the additional error details
          - `resource_path_index` (integer/int32) **REQ** — Index of the resource path causing the error
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.

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

**Scopes:** ZohoCRM.modules.attachments.READ

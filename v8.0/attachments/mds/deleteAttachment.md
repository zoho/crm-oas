# DELETE /{moduleApiName}/{recordId}/Attachments/{id}
**Operation:** `deleteAttachment` — Delete Link Attachment
> Deletes a link attachment associated with a specific record in a module. Note that only link attachments can be deleted using this endpoint; file attachments cannot be deleted through this API.

**Parameters:**
- `recordId` (path, string, required) [maxLen=64]: Specify the unique identifier of the record. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve record IDs.

- `moduleApiName` (path, string, required) [maxLen=64]: Specify the API name of the module (e.g., `Leads`, `Contacts`, `Accounts`). Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module API names.

- `id` (path, string, required) [maxLen=64]: Specify the unique identifier of the attachment. Use the [Get Attachments](attachments.yaml#$.paths./{moduleApiName}/{recordId}/Attachments.get) resource to retrieve attachment IDs.


**Responses:**

- **200**: Successful deletion response [application/json]
    - `data` (array of object) [maxItems=100] **REQ** — Array of deletion results
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the response code indicating success
      - `details` (object) **REQ** — Represents the details of the deleted attachment
        - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — ID of the deleted attachment. Use the [Get Attachments](attachments.yaml#$.paths./{moduleApiName}/{recordId}/Attachments.get) resource to retrieve attachment IDs.

      - `message` (string) **REQ** [enum=['record deleted']] — Represents the success message
      - `status` (string) **REQ** [enum=['success']] — Represents the operation status

- **400**: Error response for invalid request, including invalid record ID, invalid module name, or attachment already deleted. [application/json]
    > Wrapper for delete attachment error responses
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the Error code indicating invalid module
        - `message` (string) **REQ** [enum=['the related id given seems to be invalid', 'record not deleted']] — Represents the error message describing the issue
        - `details` (object) **REQ** — Represents the additional error details
          - `resource_path_index` (integer/int32) **REQ** — Index of the resource path causing the error
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code indicating invalid module
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message describing the issue
        - `details` (object) **REQ** — Represents the additional error details
          - `resource_path_index` (integer/int32) **REQ** — Index of the resource path causing the error

**Scopes:** ZohoCRM.modules.attachments.DELETE, ZohoCRM.modules.attachments.ALL

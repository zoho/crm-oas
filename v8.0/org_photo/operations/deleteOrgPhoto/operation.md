# DELETE /org/photo
**Operation:** `deleteOrgPhoto` — Delete the organization photo
> To delete the organization photo from your Zoho CRM organization.

**Responses:**

- **200**: Returns the deletion status for the organization photo. [application/json]
    > Response schema for a successful organization photo deletion.
    - `status` (string) [enum=['success']] — Status of the operation
    - `code` (string) [enum=['SUCCESS']] — Response code
    - `message` (string) [maxLen=1000] — Success message
    - `details` (object) — Success response containing the deletion status for the organization photo.
      - `status` (string) [enum=['success']] — Represents the status of the response.
      - `code` (string) [enum=['SUCCESS']] — The result code for this operation.
      - `message` (string) [maxLen=1000] — The success message for this operation.
      - `details` (object) — Contains additional details about the operation result.

- **400**: The request is invalid. Resolution: Verify that the request URL, token, and data are valid. [application/json]
    > Error response schema for 400 bad request errors.
    - `status` (string) [enum=['error']] — Represents the status of the response.
    - `code` (string) [enum=[5 values]] — The error code for this response.
    - `message` (string) [maxLen=1000] — Indicates the error message for this response.
    - `details` (object) — Contains additional details about the error.

- **403**: The user does not have permission to delete the organization photo. Resolution: Verify that the OAuth token includes the ZohoCRM.org.DELETE scope. [application/json]
    > Error response schema for 403 permission-denied errors.
    - `status` (string) [enum=['error']] — Indicates the status of the response.
    - `code` (string) [enum=['NO_PERMISSION']] — Represents the error code for this response.
    - `message` (string) [maxLen=1000] — Represents the error message for this response.
    - `details` (object) — Contains additional details about the permission error.
      - `permissions` (array of string) [maxItems=100] — Represents the list of required permissions for this operation.
        items: [maxLen=500]

**Scopes:** ZohoCRM.org.DELETE

# POST /files
**Operation:** `uploadFiles` — Upload files to ZFS
> To upload one or more files to the Zoho File System (ZFS) in your Zoho CRM account. The API returns an encrypted file ID for each uploaded file, which you can use to attach the file to a file upload field, image upload field, or record image field through the Create or Update Records API. The file is uploaded using multipart/form-data with a required 'file' field containing the binary data of the file to be uploaded. The response includes the file ID, name, status, and other details. Can upload 10 files in a single request by repeating the 'file' field. Maximum file size is 20 MB.

**Parameters:**
- `inline` (query, string, optional) [enum=['inline']]: Specify the upload type for inline images. Possible values: **inline** - Upload the file as an inline image for use in email templates or rich-text fields.

**Request Body** (required) — multipart/form-data
  > Multipart form data for uploading one or more files to the Zoho File System.
  - `file` (array of string/binary) [maxItems=10] **REQ** — Upload one or more files using repeated **file** keys in the multipart form data.

**Responses:**

- **200**: Returns an array of upload results, one per file, containing the encrypted file ID for CRM record association and the upload status confirmation. [application/json]
    > Represents the response schema for a successful file upload to the Zoho File System.
    - `data` (array of object) [minItems=1, maxItems=10] **REQ** — Contains the array of upload results, one object per file submitted in the request. The order corresponds to the order of files in the multipart request.
      - `status` (string) **REQ** [enum=['success']] — Represents the upload result status. Possible values: **success** - The file uploaded to ZFS without errors.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the success code for the upload operation. Possible values: **SUCCESS** - The file uploaded to ZFS without errors.
      - `message` (string) **REQ** [maxLen=500] — Represents the success message confirming the file upload.
      - `details` (object) **REQ** — Contains the file metadata for the uploaded file, including the unique identifier for CRM record association.
        - `name` (string) **REQ** [maxLen=500, minLen=1] — Represents the original filename as provided in the upload request.
        - `id` (string) **REQ** [maxLen=150, minLen=1] — Unique file identifier in ZFS. Use this ID to attach the file to CRM records or retrieve it via GET /files

- **400**: The file upload request is malformed or invalid.Bad Request - The file upload request is malformed or invalid. Returns `failure_in_attachment_handling` when the 'file' field is missing or contains no file data. Returns `INVALID_REQUEST` when request constraints are violated, such as exceeding the 10-file limit per request. **Resolution:** Verify that the request includes a **file** field with valid binary file data in multipart/form-data format, and that the request does not exceed ten files. [application/json]
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Represents the overall result status of the API request. Possible values: **error** - The request failed due to a validation or processing issue.
        - `code` (string) **REQ** [enum=['failure_in_attachment_handling']] — Represents the error code for the upload failure. Possible values: **failure_in_attachment_handling** - The **file** field is missing or contains no file data.
        - `message` (string) **REQ** [enum=['Problem in uploading attachment. kindly upload the file properly']] — Represents the error message prompting proper file upload.
        - `details` (object) **REQ** — Contains additional error context. Typically empty for this error type.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall result status of the API request. Possible values: **error** - The request failed due to a validation or processing issue.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Represents the error code for the request violation. Possible values: **INVALID_REQUEST** - The request violates API constraints such as exceeding the ten-file limit.
        - `message` (string) **REQ** [enum=[1 values]] — Represents the error message requesting verification of request parameters.
        - `details` (object) **REQ** — Contains additional error context. Typically empty for this error type.

- **415**: Unsupported Media Type / File Size Exceeded - Returned when one or more uploaded files exceed the maximum allowed size of 20 MB per file. The API rejects the entire request if any single file violates this constraint. **Resolution:** Verify that each file in the request is within the 20 MB size limit before uploading and that it is of a supported media type. [application/json]
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Represents the overall result status of the API request. Possible values: **error** - The request failed due to a validation or processing issue.
        - `code` (string) **REQ** [enum=['FILE_SIZE_MORE_THAN_ALLOWED_SIZE']] — Represents the error code for the file size violation. Possible values: **FILE_SIZE_MORE_THAN_ALLOWED_SIZE** - One or more files exceed the 20 MB maximum file size limit.
        - `message` (string) **REQ** [enum=['Please check if the size of the file is in the correct range']] — Represents the error message prompting file size verification.
        - `details` (object) **REQ** — Contains additional error context. Typically empty for this error type.

**Scopes:** ZohoCRM.files.CREATE

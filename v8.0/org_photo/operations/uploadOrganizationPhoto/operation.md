# POST /org/photo
**Operation:** `uploadOrganizationPhoto` — Upload Organization Photo
> To upload a photo for your Zoho CRM organization.

**Request Body** (required) — multipart/form-data
> The request body must include the image file in multipart/form-data format.
  > Request body schema for uploading the organization photo.
  - `file` (object) **REQ** — Specify the image file to upload as the organization photo. 

**Responses:**

- **200**: Returns the upload status for the organization photo. [application/json]
    > Response schema for a successful organization photo upload.
    - `status` (string) [enum=['success']] — Status of the operation
    - `code` (string) [enum=['SUCCESS']] — Response code
    - `message` (string) [maxLen=1000] — Success message
    - `details` (object) — Success response containing the upload status for the organization photo.
      - `status` (string) [enum=['success']] — Specifies the status of the response.
      - `code` (string) [enum=['SUCCESS']] — Represents the result code for this operation.
      - `message` (string) [maxLen=1000] — Indicates the success message for this operation.
      - `details` (object) — Contains additional details about the operation result.

- **400**: The request is invalid. Resolution: Verify that the request URL, token, and data are valid. [application/json]
    > Error response schema for 400 bad request errors.
    - `status` (string) [enum=['error']] — Represents the status of the response.
    - `code` (string) [enum=[5 values]] — Specifies the error code for this response.
    - `message` (string) [maxLen=1000] — Represents the error message for this response.
    - `details` (object) — Contains additional details about the error.
      - `expected_type` (string) [maxLen=50] — Expected data type for the file field when INVALID_DATA error occurs

- **403**: The user does not have permission to upload the organization photo. Resolution: Verify that the OAuth token includes the ZohoCRM.org.CREATE scope. [application/json]
    > Error response schema for 403 permission-denied errors.
    - `status` (string) [enum=['error']] — Represents the status of the response.
    - `code` (string) [enum=['NO_PERMISSION']] — Indicates the error code for this response.
    - `message` (string) [maxLen=1000] — Represents the error message for this response.
    - `details` (object) — Contains additional details about the permission error.
      - `permissions` (array of string) [maxItems=100] — Specifies the permission items required for this operation.
        items: [maxLen=50]

- **413**: The file size exceeds the maximum allowed limit. Resolution: Upload a file within the maximum allowed size. [application/json]
    > Error response schema for 413 file size exceeded errors.
    - `status` (string) [enum=['error']] — Represents the status of the response.
    - `code` (string) [enum=['FILE_SIZE_EXCEEDS']] — Represents the error code for this response.
    - `message` (string) [maxLen=1000] — Represents the error message for this response.
    - `details` (object) — Contains additional details about the file size error.
      - `size` (integer/int32) — Represents the maximum allowed file size in bytes.

- **415**: The file type is unsupported or the image resolution exceeds the allowed limit. Resolution: Upload an image file with a supported format and resolution. [application/json]
    > Error response schema for 415 unsupported media type errors.
    oneOf:
        - `status` (string) [enum=['error']] — Represents the status of the response.
        - `code` (string) [enum=['FILE_RESOLUTION_EXCEEDS']] — Represents the error code for this response.
        - `message` (string) [maxLen=1000] — Represents the error message for this response.
        - `details` (object) — Contains additional details about the resolution error.
          - `resolution` (integer/int32) — Represents the maximum allowed image resolution in pixels.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Specifies the error code for this response.
        - `message` (string) **REQ** [maxLen=1000] — Indicates the error message for this response.
        - `details` (object) **REQ** — Contains additional details about the error.

**Scopes:** ZohoCRM.org.CREATE

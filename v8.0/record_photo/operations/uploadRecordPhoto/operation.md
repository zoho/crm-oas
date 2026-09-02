# POST /{module}/{record}/photo
**Operation:** `uploadRecordPhoto` — Upload a record photo
> To upload a photo for a specific record in your Zoho CRM organization.

**Parameters:**
- `module` (path, string, required) [maxLen=50]: Specify the API name of the module for which you want to manage the record photo. Refer to the [Get Modules Metadata API](modules.yaml#$.paths./settings/modules.get) to retrieve the module's API name.
- `record` (path, string/int64, required): Specify the unique identifier of the record for which you want to manage the photo. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the record IDs.
- `restrict_triggers` (query, string, optional) [maxLen=100]: (Optional) Comma-separated list of automation triggers to suppress during the operation. Accepted values are `workflow`, `approval`, `blueprint`, `pathfinder`, and `orchestration`.

**Request Body** (required) — multipart/form-data
> The request body must be a multipart/form-data payload containing the **file** field with the binary photo data to upload for the record.
  > Represents the schema for the photo upload request, containing the photo file in multipart/form-data format.
  - `file` (string/binary) **REQ** — Specify the photo file to upload for the record.

**Responses:**

- **200**: Returns a success response confirming that the record photo was uploaded. [application/json]
    > Represents the success response returned when the record photo is uploaded successfully.
    - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the success code for the photo upload operation. Possible values: **SUCCESS**. 
    - `message` (string) **REQ** [maxLen=1000] — Represents the success message describing the result of the upload operation.
    - `status` (string) **REQ** [enum=['success']] — Represents the status of the response. Possible values: **success**. 
    - `details` (object) **REQ** — Represents additional details about the upload operation.

- **400**: The request is invalid due to an incorrect URL pattern, data, module name, or insufficient permissions.
**Resolution:** The module API name and record ID in the request URL must be valid. The requesting user must have the required permission, and the record must not be locked, under review, or pending approval. [application/json]
    > Represents the error response returned when the photo upload request fails due to an invalid request or a business rule violation.
    - `code` (string) **REQ** [enum=[7 values]] — Represents the error code indicating the type of request error. Possible values: **INVALID_URL_PATTERN**, **INVALID_DATA**, **INVALID_MODULE**, **CANNOT_PERFORM_ACTION**, **NOT_REVIEWED**, **NOT_APPROVED**, **RECORD_LOCKED**. 
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the request failure.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error**. 
    - `details` (object) **REQ** — Represents additional details about the error. Contains the invalid identifier or resource path index when applicable.
      oneOf:
        - `RecordPhotoErrorDetailsEmpty` (object) — Represents an empty details object returned when no additional error context is available for the error response.
          - `id` (string) **REQ** [maxLen=100] — Represents the invalid identifier that caused the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the invalid resource path in the request URL.

- **413**: The uploaded file exceeds the maximum allowed size.
**Resolution:** The photo file size must be within the maximum allowed limit before uploading. [application/json]
    > Represents the error response returned when the uploaded photo file exceeds the maximum allowed size.
    - `code` (string) **REQ** [enum=['FILE_SIZE_EXCEEDS']] — Represents the error code indicating that the uploaded file exceeds the maximum allowed size. Possible values: **FILE_SIZE_EXCEEDS**. 
    - `details` (object) **REQ** — Represents additional details about the file size error, including the size of the file that exceeded the limit.
      - `size` (integer/int32) **REQ** — Represents the size of the uploaded file that exceeded the maximum allowed limit.
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the file size violation.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error**. 

- **415**: The uploaded file has an unsupported format or its resolution exceeds the maximum allowed limit.
**Resolution:** The photo file must be a supported image type and within the maximum allowed resolution. [application/json]
    > Represents the error response returned when the uploaded photo file has an unsupported format or its resolution exceeds the allowed limit.
    - `code` (string) **REQ** [enum=['FILE_RESOLUTION_EXCEEDS', 'INVALID_DATA']] — Represents the error code indicating an unsupported media type or invalid file format. Possible values: **FILE_RESOLUTION_EXCEEDS**, **INVALID_DATA**. 
    - `details` (object) **REQ** — Represents additional details about the media type error. Contains the file resolution that exceeded the limit when applicable.
      oneOf:
          - `resolution` (integer/int32) **REQ** — Represents the resolution of the uploaded file that exceeded the maximum allowed limit.
        - `RecordPhotoErrorDetailsEmpty` (object) — Represents an empty details object returned when no additional error context is available for the error response.
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the media type or file format issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error**. 

**Scopes:** ZohoCRM.modules.CREATE

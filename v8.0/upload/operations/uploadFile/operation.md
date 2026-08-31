# POST /upload
**Operation:** `uploadFile` — Upload a file to CRM
> To upload a CSV file in ZIP format for bulk write API. The response contains the **file_id**. Use this ID while making the bulk write request.

**Parameters:**
- `X-CRM-ORG` (header, integer/int32, required): Static CRM organization identifier. This value is fixed per account and shared during onboarding.
- `feature` (header, string, required) [enum=['bulk-write']]: Specify the feature for which the file upload is being performed.
Possible values: 
**bulk-write** - Indicates a bulk write operation.

**Request Body** (required) — multipart/form-data
> The request body must contain the ZIP file to upload as a multipart/form-data payload. The file must be in ZIP format and must not exceed 25 MB.
  > Specify the multipart/form-data payload containing the ZIP file to upload for the bulk write operation.
  - `file` (object) **REQ** — Specify the file to upload. The file must be a ZIP archive containing one or more CSV files, with a maximum of **25,000 records** per file. The maximum file size is **25 MB.**  If there are more records, make a separate API call by with a ZIP file containing the next 25,000 records in the module.
Please note that the **Subform** and **multi-module lookup (MxN linking module)** fields are treated as separate modules in Zoho CRM. This is a parent-child modulecase, for example, the Contacts module is the parent module, and the subform within it is the child module. So, **prepare separate CSV files for parent and child modules**, then ZIP them together into a ZIP file and upload.
For more details on preparing the input file for parent-child record imports, refer to [Kaizen #131 - Bulk Write for parent-child records using Scala SDK.](https://help.zoho.com/portal/en/community/topic/kaizen-131-bulk-write-for-parent-child-records-scala-sdk) 

**Responses:**

- **200**: Returns the details of the uploaded file, including the **file ID** and creation timestamp. [application/json]
    > Represents the response returned when a file is uploaded successfully.
    - `status` (string) **REQ** [enum=['success']] — Represents the status of the upload operation. 
 Possible values:
**success** - The file was uploaded successfully.
    - `code` (string) **REQ** [enum=['FILE_UPLOAD_SUCCESS']] — Represents the result code for the upload operation.
Possible values: 
**FILE_UPLOAD_SUCCESS** - The file was uploaded successfully.
    - `message` (string) **REQ** [enum=['file uploaded.']] — Represents the message confirming the outcome of the upload operation.
    - `details` (object) **REQ** — Represents the details of the uploaded file, including the file ID and creation time.
      - `file_id` (string) **REQ** [maxLen=255] — Represents the unique ID assigned to the uploaded file. Use this ID in the Create Bulk Write Job request.
      - `created_time` (string/date-time) **REQ** — Represents the date and time when the file was uploaded, in ISO 8601 format.

- **400**: The request is invalid. 
Resolution: Check the request for missing or invalid headers, unsupported features, or an invalid file format, and resubmit. [application/json]
    > Represents the error response returned when the file upload request fails.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the upload operation.  
Possible values: 
**error** - The upload operation failed.
    - `code` (string) **REQ** [enum=[4 values]] — Represents the error code for the upload failure. 
Possible values: 
**INVALID_DATA** - The request data is invalid.
**NOT_SUPPORTED_FEATURE** - The specified feature is not supported. 
**MANDATORY_NOT_FOUND** - A required field is missing. 
**INVALID_FILE_FORMAT** - The uploaded file format is not supported.
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the reason for the upload failure.
    - `details` (object) — Represents additional details about the upload failure, when provided.

**Scopes:** ZohoFiles.files.ALL

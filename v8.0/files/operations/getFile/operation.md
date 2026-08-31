# GET /files
**Operation:** `getFile` — Retrieve a file from ZFS
> To retrieve the binary content of a file stored in Zoho File System (ZFS) using its unique file ID. The file ID is provided as a required query parameter 'id'. If the file exists, the API returns the file's binary data along with appropriate headers indicating the MIME type and content disposition for download. If the file ID does not correspond to any file in ZFS, a 204 No Content response is returned. This endpoint is used to download files that have been previously uploaded to ZFS and associated with Zoho CRM records.

**Parameters:**
- `id` (query, string, optional) [maxLen=150]: Specify the encrypted file ID received in the response when uploading files to the Zoho File System. Use the [ZFC API](files.yaml#$.paths./files.get) to retrieve the File IDs.

**Responses:**

- **200**: Successfully uploaded file to Zoho File System. Returns the uploaded file as binary content with appropriate headers indicating the file type and disposition [application/octet-stream]
    > Binary content of the requested file, returned with the appropriate MIME type header.
    type: string/binary — Binary content of the requested file, returned with the appropriate MIME type header.
  Headers:
    - `Content-Type` (string) — MIME type of the uploaded file (e.g., application/pdf, image/png, text/plain).
    - `Content-Disposition` (string) — Indicates how the content should be displayed. Includes the original filename for download purposes.

- **204**: The specified file ID does not match any file in the Zoho File System. No Content - Returned when the provided file ID does not match any file in the Zoho File System. This occurs when the 'id' parameter contains an invalid file identifier, an empty string, or references a file that has been deleted or never existed. **Resolution:** Verify that the **id** parameter contains a valid encrypted file ID from a previous upload response.

- **400**: The request is missing required parameters. **For regular file mode**: The **id** parameter is missing. **For email template mode** (when `type=email_template`): One or more of the required parameters (`file_id`, `template_id`, `attach_id`) are missing. **Resolution:** For regular file retrieval, include the **id** query parameter. For email template attachments, ensure all required parameters are present: `type=email_template`, `file_id`, `template_id`, and `attach_id`. [application/json]
    oneOf:
      - `RequiredParamMissingResponse` — Returned when the required **id** query parameter is not present in the request URL.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall result status of the API request. Possible values: **error** - The request failed due to a validation or processing issue.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code returned by the API.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message describing the issue.
        - `details` (object) **REQ** — Contains additional context about the error, including the name of the missing parameter.
          - `param_name` (string) **REQ** [enum=['id']] — Represents the name of the required parameter that is missing from the request.

**Scopes:** ZohoCRM.files.READ

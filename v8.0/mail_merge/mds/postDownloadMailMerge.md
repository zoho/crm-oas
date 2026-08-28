# POST /{moduleApiName}/{recordId}/actions/download_mail_merge
**Operation:** `postDownloadMailMerge` — Download mail merge document
> To download the merged document created from a mail merge template for a specific record in your Zoho CRM organization. You can choose the output format as **pdf**, **html**, or **docx**, and optionally set a password for PDF documents.

**Parameters:**
- `moduleApiName` (path, string, required) [maxLen=255]: Specify the API name of the CRM module for which you want to perform the mail merge action. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
- `recordId` (path, integer/int64, required): Specify the unique ID of the record for which you want to perform the mail merge action.

**Request Body** — application/json `PostdownloadmailmergeRequest`
> The request body must contain a **download_mail_merge** array with one object specifying the mail merge template and its optional output settings.
  > Represents the request body schema for the download mail merge operation.
  - `download_mail_merge` (array of object `DownloadMailMergeNested`) [maxItems=1] **REQ** — Represents the list of download mail merge request objects. Contains one object per request.
    schema: `DownloadMailMergeNested`
    - `mail_merge_template` (object `MailMergeTemplateNested`) **REQ** — To pass template name (Required)
      schema: `MailMergeTemplateNested`
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the mail merge template to use for the operation.
    - `output_format` (string) [maxLen=4, enum=['pdf', 'html', 'docx']] — Represents the output format for the downloaded document.
Possible values:
**pdf** - Downloads the document in PDF format.
**html** - Downloads the document in HTML format.
**docx** - Downloads the document in DOCX format.

    - `file_name` (string) [maxLen=255] — Represents the file name for the downloaded mail merge document.

**Responses:**

- **200**: Returns the result of the download mail merge operation, indicating that the merged document generation was initiated successfully. [application/json]
    > Represents the response body for a successful download mail merge request.
    - `download_mail_merge` (array of object) [maxItems=1] — Represents the list of download mail merge response objects.
      - `code` (string) [maxLen=255] — Represents the response code indicating the result of the download mail merge operation.
      - `message` (string) [maxLen=255] — Represents the message describing the result of the download mail merge operation.
      - `status` (string) [maxLen=255] — Represents the status of the download mail merge operation.

- **400**: The download mail merge request could not be processed due to invalid input. 
**Resolution**: Verify that the request body contains all required fields with valid values, and that the module API name and record ID in the URL are correct.
 [application/json]
    > Represents the error response body for an invalid download mail merge request.
    oneOf:
      - `ExpectedParamMissingError` — Represents an error response when at least one of the expected request parameters is absent.
        - `code` (string) **REQ** [enum=['EXPECTED_PARAM_MISSING']] — Represents the error code for the failed operation. 
        - `details` (object) **REQ** — Represents the error details listing the expected parameters, at least one of which must be provided.
          - `param_names` (array of string) [maxItems=25] **REQ** — Represents the list of expected parameter names, at least one of which must be included in the request.
            items: [maxLen=255]
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message. 
        - `status` (string) **REQ** [enum=['error']] — Represents the error response status.
      - `InvalidDataUrlError` — Represents an error response when invalid data is provided in the request URL.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this error type. 
        - `details` (object) **REQ** — Represents the error details identifying the URL path segment with invalid data.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the URL path segment that contains invalid data.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message. 
        - `status` (string) **REQ** [enum=['error']] — Represents the error response status. 
      - `InvalidModuleParamError` — Represents an error response when the module name provided in a request parameter is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for this error type. 
        - `details` (object) **REQ** — Represents the error details identifying the parameter with an invalid module name.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter that contains the invalid module name.
        - `message` (string) **REQ** [enum=['module name given seems to be invalid']] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Represents the error response status. 
      - `InvalidRequestMethodError` — Represents an error response when the HTTP request method used is not supported for the endpoint.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Represents the error code for the failed operation. 
        - `details` (object) **REQ** — Represents the error details for an invalid request method error. 
        - `message` (string) **REQ** [enum=['The http request method type is not a valid one']] — Represents the error message. 
        - `status` (string) **REQ** [enum=['error']] — Represents the error response status. 
        - `download_mail_merge` (array of object) [maxItems=25] **REQ** — Represents the list of error objects for the download mail merge operation.
          oneOf:
            - `MandatoryFieldNotFoundError` — Represents an error response when a required field is missing from the request.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this error type. 
              - `details` (object) **REQ** — Represents the error details identifying the missing mandatory field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing mandatory field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the missing mandatory field in the request.
              - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message. 
              - `status` (string) **REQ** [enum=['error']] — Represents the error response status.
            - `InvalidDataTypeError` — Represents an error response when a field value has an invalid data type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the requested operation. 
              - `details` (object) **REQ** — Represents the error details with field validation information.
                - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type for the field that failed validation.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that has an invalid data type.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that has an invalid data type.
              - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message. 
              - `status` (string) **REQ** [enum=['error']] — Represents the error response status. 
            - `InvalidDataMaxLengthError` — Represents an error response when a field value exceeds the maximum allowed length.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the failed request. 
              - `details` (object) **REQ** — Represents the error details with field validation information.
                - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the field that failed validation.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that failed validation.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that failed validation.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message describing the failure. 
              - `status` (string) **REQ** [enum=['error']] — Represents the error response status. 

**Scopes:** ZohoCRM.settings.mailmerge.CREATE, ZohoWriter.documentEditor.ALL, ZohoWriter.merge.ALL

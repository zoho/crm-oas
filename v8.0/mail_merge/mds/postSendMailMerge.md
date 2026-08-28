# POST /{moduleApiName}/{recordId}/actions/send_mail_merge
**Operation:** `postSendMailMerge` — Send mail merge email
> To send a personalized email to one or more recipients using a mail merge template associated with a specific record in your Zoho CRM organization. You can include recipients in the To, CC, and BCC fields, and optionally attach the merged document either as an inline image or a separate file.

**Parameters:**
- `moduleApiName` (path, string, required) [maxLen=255]: Specify the API name of the CRM module for which you want to perform the mail merge action. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
- `recordId` (path, integer/int64, required): Specify the unique ID of the record for which you want to perform the mail merge action.

**Request Body** — application/json `PostsendmailmergeRequest`
> The request body must contain a **send_mail_merge** array with one object specifying the mail merge template, recipient addresses, and optional email content settings.
  > Represents the request body schema for the send mail merge operation.
  - `send_mail_merge` (array of object `SendMailMergeNested`) [maxItems=1] **REQ** — Represents the list of send mail merge request objects. Contains one object per request.
    schema: `SendMailMergeNested`
    - `bcc_email` (array of object `BccEmailNested`) [maxItems=1] — Represents the list of email addresses to include in the BCC field of the mail merge email.
      schema: `BccEmailNested`
      - `type` (string) **REQ** [maxLen=5, enum=['email']] — Represents the type of the address.
Possible values:
**email** - Indicates that the value is an email address.

      - `value` (string/email) **REQ** [maxLen=255, pattern=^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$] — Represents the email address to include in the BCC list for the mail merge email.
    - `mail_merge_template` (object `MailMergeTemplateNested`) **REQ** — Mailmerge Object to pass Template details (Required)
      schema: `MailMergeTemplateNested`
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the mail merge template to use for the operation.
    - `subject` (string) [maxLen=255] — Represents the subject line of the mail merge email.
    - `cc_email` (array of object `CcEmailNested`) [maxItems=1] — Represents the list of email addresses to include in the CC field of the mail merge email.
      schema: `CcEmailNested`
      - `type` (string) **REQ** [maxLen=5, enum=['email']] — Represents the type of the address.
Possible values:
**email** - Indicates that the value is an email address.

      - `value` (string/email) **REQ** [maxLen=255, pattern=^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$] — Represents the email address to include in the CC list for the mail merge email.
    - `attachment_name` (string) [maxLen=255] — Represents the name of the attachment to include in the mail merge email.
    - `to_address` (array of object `ToAddressNested`) [maxItems=2] — Represents the list of email addresses to send the mail merge email to.
      schema: `ToAddressNested`
      - `type` (string) **REQ** [maxLen=5, enum=['email']] — Represents the type of the address.
Possible values:
**email** - Indicates the value is an email address.

      - `value` (string/email) **REQ** [maxLen=255, pattern=^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$] — Represents the recipient email address for the mail merge email.
    - `type` (string) [maxLen=10, enum=['inline', 'attachment']] — Represents the attachment type for the mail merge email.
Possible values:
**inline** - Includes the mail merge document as an inline image in the email.
**attachment** - Attaches the mail merge document as a separate file in the email.

    - `message` (string) [maxLen=100000] — Represents the body or content of the email you want to send. It can include up to **100,000 characters**.


    - `from_address` (object `FromAddressNested`) — The email ID you want to use to send emails from. This email address must be the one of the org-verified email addresses or the current user's email ID.
      schema: `FromAddressNested`
      - `type` (string) **REQ** [maxLen=5, enum=['email']] — Represents the type of the address.
Possible values:
**email** - Indicates the value is an email address.

      - `value` (string/email) **REQ** [maxLen=255, pattern=^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$] — Represents the sender email address used to send the mail merge email.

**Responses:**

- **200**: Returns the result of the send mail merge operation, indicating that the email sending was initiated successfully. — Schema: `PostsendmailmergeResponse200` [application/json]
    > Represents the response body returned upon successful initiation of the send mail merge operation.
    schema: `PostsendmailmergeResponse200`
    - `send_mail_merge` (array of object `SendMailMergeNested1`) [maxItems=1] — Represents the list of send mail merge response objects.
      schema: `SendMailMergeNested1`
      - `code` (string) [maxLen=255] — Represents the response code indicating the result of the send mail merge operation.
      - `details` (object `DetailsNested`) — Represents the response details returned upon successful initiation of the send mail merge operation.
        schema: `DetailsNested`
        - `report_link` (string/uri) [maxLen=255] — Represents the URL of the mail merge job report.
      - `message` (string) [maxLen=255] — Represents the message describing the result of the send mail merge operation.
      - `status` (string) [maxLen=255, enum=['success', 'error']] — Represents the status of the send mail merge operation.
Possible values:
**success** - The mail merge email was initiated successfully.
**error** - The mail merge email failed to initiate.


- **400**: The send mail merge request could not be processed due to invalid input. 
**Resolution**: Verify that the request body contains all required fields with valid values, and that the module API name and record ID in the URL are correct.
 [application/json]
    > Represents the error response body for an invalid send mail merge request.
    oneOf:
      - `InvalidModulePathError` — Represents an error response when the module name provided in the URL path is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for the failed operation request. 
        - `details` (object) **REQ** — Represents the error details identifying the invalid module in the request URL.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the URL path segment that contains the invalid module name.
        - `message` (string) **REQ** [enum=['module name given seems to be invalid']] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Represents the error response status. 
      - `RequiredParamMissingError` — Represents an error response when a required URL or query parameter is not provided in the request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for this error type.
        - `details` (object) **REQ** — Represents the error details identifying the missing required parameter.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the required parameter that is missing from the request.
        - `message` (string) **REQ** [enum=['mandatory param missing']] — Represents the error message. 
        - `status` (string) **REQ** [enum=['error']] — Represents the error response status. 
      - `InvalidDataParamError` — Represents an error response when invalid data is provided in a request parameter.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the failed operation. 
        - `details` (object) **REQ** — Represents the error details identifying the parameter with invalid data.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the request parameter that contains invalid data.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message. 
        - `status` (string) **REQ** [enum=['error']] — Represents the error response status.
      - `InvalidRequestMethodError` — Represents an error response when the HTTP request method used is not supported for the endpoint.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Represents the error code for the failed operation. 
        - `details` (object) **REQ** — Represents the error details for an invalid request method error. 
        - `message` (string) **REQ** [enum=['The http request method type is not a valid one']] — Represents the error message. 
        - `status` (string) **REQ** [enum=['error']] — Represents the error response status. 
        - `send_mail_merge` (array of object) [maxItems=25] **REQ** — Represents the list of error objects for the send mail merge request.
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

**Scopes:** ZohoCRM.settings.mailmerge.CREATE, ZohoWriter.documentEditor.ALL, ZohoWriter.merge.ALL, ZohoCRM.settings.emails.ALL

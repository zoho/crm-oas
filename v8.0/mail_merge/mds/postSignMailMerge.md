# POST /{moduleApiName}/{recordId}/actions/sign_mail_merge
**Operation:** `postSignMailMerge` — Send mail merge document for signing
> To send a merged document to one or more recipients for signing or approval using a mail merge template associated with a specific record in your Zoho CRM organization. Before using this operation for the first time, you must access the Merge and Sign dialog in the Zoho Writer UI once.

**Parameters:**
- `moduleApiName` (path, string, required) [maxLen=255]: Specify the API name of the CRM module for which you want to perform the mail merge action. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
- `recordId` (path, integer/int64, required): Specify the unique ID of the record for which you want to perform the mail merge action.

**Request Body** — application/json `PostsignmailmergeRequest`
> The request body must contain a **sign_mail_merge** array with one object specifying the mail merge template, the file name, and the list of signers.
  > Represents the request body schema for the sign mail merge operation.
  - `sign_mail_merge` (array of object `SignMailMergeNested`) [maxItems=1] **REQ** — Represents the list of sign mail merge request objects. Contains one object per request.
    schema: `SignMailMergeNested`
    - `sign_in_order` (boolean) — Indicates whether recipients must act on the document in a specified sequence.
Possible values:
**true** - The document first goes for approval, then for signing in the defined order.
**false** - Zoho Sign sends the document to all recipients simultaneously.

    - `signers` (array of object `SignersNested`) [maxItems=3] — The details of the users you want to sign the document.
- recipient_name **string, mandatory** - the name of the user who has to sign or approve the document.
- **action_type** string, mandatory - the type of action you want the user to perform. The possible values are sign to **sign** the document, and **approve** to approve the document.
- **recipient** JSON object, mandatory
    - **value** string, mandatory - the email ID of the user who has to sign or approve the document.

> **Note**
> The values for the fields **recipient_name** and **recipient.value** will be taken from the mail merge template. If you want to override the values in the template, you must specify the values of these fields in the input body.
      schema: `SignersNested`
      - `recipient` (object `RecipientNested`) **REQ** — Recipient Object (Required)
        schema: `RecipientNested`
        - `type` (string) **REQ** [maxLen=11, enum=['email', 'merge_field']] — Represents the type of recipient identifier.
Possible values:
**email** - The recipient is identified by a direct email address.
**merge_field** - The recipient is identified by a mail merge field reference.

        - `value` (string) **REQ** [maxLen=255] — Represents the email address or mail merge field reference for the recipient. When **type** is **email**, provide a valid email address. When **type** is **merge_field**, provide a merge field reference such as **${!Leads.Email}**.
      - `recipient_name` (string) **REQ** [maxLen=255] — Represents the name of the recipient who must sign or approve the document.
      - `action_type` (string) **REQ** [maxLen=7, enum=['sign', 'approve']] — Represents the action the recipient must perform on the mail merge document.
Possible values:
**sign** - The recipient must sign the document.
**approve** - The recipient must approve the document.

    - `mail_merge_template` (object `MailMergeTemplateNested`) **REQ** — To pass Template details (Required)
      schema: `MailMergeTemplateNested`
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the mail merge template to use for the operation.
    - `file_name` (string) **REQ** [maxLen=255] — Represents the name of the file to send for signing or approval.

**Responses:**

- **200**: Returns the result of the sign mail merge operation, indicating that the document was sent for signing or approval successfully. — Schema: `PostsignmailmergeResponse200` [application/json]
    > Represents the response body returned upon successful initiation of the sign mail merge operation.
    schema: `PostsignmailmergeResponse200`
    - `sign_mail_merge` (array of object `SignMailMergeNested1`) [maxItems=1] — Represents the list of sign mail merge response objects.
      schema: `SignMailMergeNested1`
      - `code` (string) [maxLen=255] — Represents the response code indicating the result of the sign mail merge operation.
      - `details` (object `DetailsNested1`) — Represents the response details returned upon successful initiation of the sign mail merge operation.
        schema: `DetailsNested1`
        - `sign_resource_id` (string) [maxLen=255] — Represents the unique ID of the sign request resource created for the sign mail merge operation.
        - `report_link` (string/uri) [maxLen=255] — Represents the URL of the sign mail merge job report.
      - `message` (string) [maxLen=255] — Represents the message describing the result of the sign mail merge operation.
      - `status` (string) [maxLen=255, enum=['success', 'error']] — Represents the status of the sign mail merge operation.
Possible values:
**success** - The sign mail merge document was sent successfully.
**error** - The sign mail merge document failed to send.


- **400**: The sign mail merge request could not be processed due to invalid input. 
**Resolution**: Verify that the request body contains all required fields with valid values, and that the module API name and record ID in the URL are correct.
 [application/json]
    > Represents the error response body for an invalid sign mail merge request.
    oneOf:
      - `ExpectedFieldMissingError` — Represents an error response when at least one of the expected fields is absent from the request.
        - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Represents the error code for the failed operation. 
        - `details` (object) **REQ** — Represents the error details listing the expected fields, at least one of which must be provided.
          - `expected_fields` (array of object) [maxItems=25] **REQ** — Represents the list of expected fields, at least one of which must be included in the request.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the expected field.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the expected field in the request body.
        - `message` (string) **REQ** [enum=['specify atleast one field']] — Represents the error message. 
        - `status` (string) **REQ** [enum=['error']] — Represents the error response status. 
      - `InvalidDataParamError` — Represents an error response when invalid data is provided in a request parameter.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the failed operation. 
        - `details` (object) **REQ** — Represents the error details identifying the parameter with invalid data.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the request parameter that contains invalid data.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message. 
        - `status` (string) **REQ** [enum=['error']] — Represents the error response status.
      - `InvalidModulePathError` — Represents an error response when the module name provided in the URL path is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for the failed operation request. 
        - `details` (object) **REQ** — Represents the error details identifying the invalid module in the request URL.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the URL path segment that contains the invalid module name.
        - `message` (string) **REQ** [enum=['module name given seems to be invalid']] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Represents the error response status. 
        - `sign_mail_merge` (array of object) [maxItems=25] **REQ** — Represents the list of error objects for the sign mail merge request.
          oneOf:
            - `MandatoryFieldNotFoundBodyError` — Represents an error response when a required field is absent from the request body.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this error type. 
              - `details` (object) **REQ** — Represents the error details identifying the missing mandatory field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing mandatory field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the missing mandatory field in the request body.
              - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message. 
              - `status` (string) **REQ** [enum=['error']] — Represents the error response status. 
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
      - `InvalidRequestMethodError` — Represents an error response when the HTTP request method used is not supported for the endpoint.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Represents the error code for the failed operation. 
        - `details` (object) **REQ** — Represents the error details for an invalid request method error. 
        - `message` (string) **REQ** [enum=['The http request method type is not a valid one']] — Represents the error message. 
        - `status` (string) **REQ** [enum=['error']] — Represents the error response status. 

**Scopes:** ZohoCRM.settings.mailmerge.CREATE, ZohoWriter.documentEditor.ALL, ZohoWriter.merge.ALL, ZohoSign.documents.ALL

# POST /{module}/{recordId}/actions/associate_email
**Operation:** `associateEmail` — Associate Email
> Associates an email with a specific record in a module, creating a link between the email and the CRM record.

**Parameters:**
- `module` (path, string, required) [maxLen=100]: The API name of the module containing the record. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module API names.

- `recordId` (path, string, required) [maxLen=100]: The unique ID of the record to associate the email with. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve record IDs.


**Schemas:**
`EmailAddress`:
  > Object representing an email address and display name.
  - `user_name` (string) [maxLen=255] — The display name of the email recipient or sender.
  - `email` (string/email) **REQ** [maxLen=255] — The actual email address.
`InvalidModuleError`:
  > Error response returned when the module name provided in the request path does not exist or is invalid.
  - `code` (string) [maxLen=50, enum=['INVALID_MODULE']] — Error code indicating the type of failure. Always INVALID_MODULE for this error.
  - `details` (object) — Details providing additional context about the invalid module error.
    - `resource_path_index` (integer/int32) — The zero-based index position in the resource path where the invalid module name was detected.
  - `message` (string) [maxLen=255, enum=['the module name given seems to be invalid']] — Human-readable message describing the invalid module error.
  - `status` (string) [maxLen=50, enum=['error']] — Status of the operation. Always "error" for this failure.

**Request Body** (required) — application/json `AssociateEmailRequest`
> Payload containing the email details to be associated with the record.
  > Request body for associating an email with a record.
  - `data` (array of object `EmailObject`) [minItems=1, maxItems=50] **REQ** — List of email objects to associate with the record.
    schema: `EmailObject`
    - `from` (object `EmailAddress`) **REQ** — Object representing an email address and display name.
    - `to` (array of object `EmailAddress`) [maxItems=50] **REQ** — Primary recipients of the email.
    - `cc` (array of object `EmailAddress`) [maxItems=50] — Carbon copy recipients of the email.
    - `bcc` (array of object `EmailAddress`) [maxItems=50] — Blind carbon copy recipients of the email.
    - `subject` (string) **REQ** [maxLen=500] — The subject line of the email.
    - `content` (string) **REQ** [maxLen=32000] — The email body content.
    - `mail_format` (string) [enum=['text', 'html'], default=text] — The format of the email content.
    - `original_message_id` (string) **REQ** [maxLen=255] — The unique identifier of the email from the mail server. This is used to prevent duplicate email associations.
    - `sent` (boolean) **REQ** — Indicates whether the email was sent (true) or received (false) by the CRM user.
    - `date_time` (string/date-time) **REQ** [maxLen=50] — The timestamp of the email (ISO 8601 format).
    - `attachments` (array of object `AttachmentRef`) [maxItems=20] — List of attachments associated with the email. Use the [Files API](files.yaml#$.paths./files.get) to retrieve attachment IDs.
      schema: `AttachmentRef`
      - `id` (string) **REQ** [maxLen=100] — The attachment ID. Use the [Files API](files.yaml#$.paths./files.get) to retrieve attachment IDs.


**Responses:**

- **201**: Email associated successfully with the record. — Schema: `ActionResponse` [application/json]
    > Generic wrapper for multiple record action responses.
    schema: `ActionResponse`
    - `Emails` (array of object) [maxItems=50] — Array of result statuses for each email association operation.
      - `code` (string) [maxLen=50, enum=['SUCCESS']] — Status code indicating the result of the operation. Possible values:SUCCESS, ERROR.
      - `details` (object) — Contextual details about the operation result.
        - `message_id` (string) **REQ** [maxLen=255] — The original message ID of the email that was processed.
      - `message` (string) [maxLen=255] — Human-readable message describing the operation result.
      - `status` (string) [maxLen=50, enum=['success']] — Operation status. Possible values:success, error.

- **400**: Bad Request - The request could not be processed due to invalid input. Review the error details and correct the issues before retrying. [application/json]
    oneOf:
      - `InvalidModuleError` — Error response returned when the module name provided in the request path does not exist or is invalid.
      - `MaximumLengthError` — Details about a failed API request.
        - `code` (string) [maxLen=50, enum=['INVALID_DATA']] — Error code.
        - `message` (string) [maxLen=255] — Human-readable error message describing the issue.
        - `status` (string) [maxLen=50, enum=['error']] — Error status. Always "error".
        - `details` (object) — Detailed error context, including field-specific validation information.
          - `maximum_length` (integer/int32) **REQ** — The maximum allowed length for the field that failed validation.
          - `api_name` (string) **REQ** [maxLen=100] — The API name of the field or module that caused the validation error.
          - `json_path` (string) **REQ** [maxLen=255] — The JSON path of the field that caused the validation error.
      - `MandatoryNotFoundError` — Error response returned when a required field is missing in the request payload. The Emails array contains per-item error details.
        - `Emails` (array of object) [maxItems=1] — Array of per-email error results indicating which required fields are missing.
          - `code` (string) [maxLen=50, enum=['MANDATORY_NOT_FOUND']] — Error code indicating the type of validation failure. For example, MANDATORY_NOT_FOUND.
          - `details` (object) — Detailed error context identifying the missing required field.
            - `api_name` (string) [maxLen=100] — The API name of the missing required field.
            - `json_path` (string) [maxLen=255] — The JSON path of the missing required field in the request payload.
          - `message` (string) [maxLen=255] — Human-readable message describing the validation error.
          - `status` (string) [maxLen=50] — Status of the operation. Always "error" for validation failures.
      - `InvalidDataError` — Details about a failed API request.
        - `code` (string) [maxLen=50, enum=['INVALID_DATA']] — Error code.
        - `message` (string) [maxLen=255, enum=['the related id given seems to be invalid']] — Human-readable error message describing the issue.
        - `status` (string) [maxLen=50, enum=['error']] — Error status. Always "error".
        - `details` (object) — Detailed error context, including field-specific validation information.
      - `InvalidValueErrorDetails` — Error response returned when the request payload contains invalid data. The Emails array contains per-item error details.
        - `code` (string) [maxLen=50, enum=['INVALID_DATA']] — Error code indicating the type of validation failure. For example, INVALID_DATA.
        - `details` (object) — Detailed error context identifying the invalid field.
          - `api_name` (string) [maxLen=100] — The API name of the invalid field.
          - `json_path` (string) [maxLen=255] — The JSON path of the invalid field in the request payload.
        - `message` (string) [maxLen=255, enum=['invalid data']] — Human-readable message describing the validation error.
        - `status` (string) [maxLen=50, enum=['error']] — Status of the operation. Always "error" for validation failures.

- **404**: Not Found - The specified module does not exist or is not accessible. Verify the module name and retry. — Schema: `InvalidModuleError` [application/json]
    > Error response returned when the module name provided in the request path does not exist or is invalid.

**Scopes:** ZohoCRM.modules.emails.CREATE

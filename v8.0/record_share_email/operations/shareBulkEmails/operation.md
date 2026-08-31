# POST /{moduleApiName}/actions/share_emails
**Operation:** `shareBulkEmails` — Share Record Emails
> To share email threads linked to multiple CRM records with colleagues in the same organization. Accepts up to 100 record IDs per request. Supports partial success - each record in the response is processed independently, and individual results indicate success or failure.

**Parameters:**
- `moduleApiName` (path, string, required) [enum=['Leads', 'Contacts', 'Accounts', 'Deals', 'CustomModule1']]: Specify the API name of the module that contains the records whose emails you want to share. Refer to [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve available module API names.

**Request Body** (required) — application/json
> The request body must contain an **ids** array with up to 100 record IDs whose emails you want to share.
  > Represents the request body schema for sharing emails in bulk, containing an array of record IDs.
  - `ids` (array of string/string) [maxItems=100] **REQ** — Specify the list of record IDs whose emails you want to share. Accepts up to 100 record IDs per request.

**Responses:**

- **200**: Returns the list of per-record results when all email sharing operations in the bulk request complete successfully. [application/json]
    > Represents the 200 response schema for the shareBulkEmails operation, containing an array of per-record email sharing results.
    - `data` (array of object) [maxItems=100] — Represents the list of per-record email sharing results. Always present in the response.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the email sharing operation.
Possible values: **SUCCESS** - the email sharing completed successfully. Always present in the response.
      - `details` (object) **REQ** — Represents the details of the record that was shared. Always present in the response.
        - `id` (string/string) **REQ** — Represents the unique identifier of the shared record. Always present in the response.
      - `message` (string) **REQ** [enum=['Successfully shared']] — Represents the result message for the email sharing operation. Always present in the response.
      - `status` (string) **REQ** [enum=['success']] — Represents the overall operation status.
Possible values: **success** - the email sharing completed successfully. Always present in the response.

- **207**: Returns a mix of success and failure results when some email sharing operations succeed and others fail. Inspect each item in the `data` array for the individual outcome. [application/json]
    > Represents the 207 partial success response schema for the shareBulkEmails operation, where each item indicates an individual record's outcome.
    - `data` (array of object) [maxItems=100] — Represents the list of per-record results for the partial success response. Always present in the response.
      oneOf:
          - `code` (string) **REQ** [enum=['ALREADY_SHARED']] — Represents the result code for a record whose emails are already shared.
Possible values: **ALREADY_SHARED** - the emails for this record are already shared with colleagues.
          - `details` (object) **REQ** — Represents additional details about the already-shared record. Always present in the response.
            - `id` (string/string) **REQ** — Represents the unique identifier of the already-shared record. Always present in the response.
          - `message` (string) **REQ** [enum=['Emails are already shared to the colleagues already']] — Represents the message describing the already-shared status. Always present in the response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status for this result item.
Possible values: **error** - the emails are already shared. Always present in the response.
          - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for a successfully shared record.
Possible values: **SUCCESS** - the email sharing completed successfully for this record.
          - `details` (object) **REQ** — Represents the details of the successfully shared record. Always present in the response.
            - `id` (string/string) **REQ** — Represents the unique identifier of the successfully shared record. Always present in the response.
          - `message` (string) **REQ** [enum=['Successfully shared']] — Represents the result message for the successfully shared record. Always present in the response.
          - `status` (string) **REQ** [enum=['success']] — Represents the status for this result item.
Possible values: **success** - the email sharing completed for this record. Always present in the response.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the result code for a record that failed validation.
Possible values: **INVALID_DATA** - the record ID is invalid or not found.
          - `details` (object) **REQ** — Represents additional details about the invalid record. Always present in the response.
            - `id` (string/string) **REQ** — Represents the unique identifier of the invalid record. Always present in the response.
          - `message` (string) **REQ** [enum=['the related id given seems to be invalid']] — Represents the error message for the invalid data result. Always present in the response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status for this result item.
Possible values: **error** - the record ID is invalid. Always present in the response.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the result code for a record where the operation is not allowed.
Possible values: **NOT_ALLOWED** - the operation is not permitted for this record.
          - `details` (object) **REQ** — Represents additional error context for the not-allowed result. Always present in the response.
            - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path element associated with this error. Always present in the response.
          - `message` (string/string) **REQ** — Represents the error message for the not-allowed result. Always present in the response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status for this result item.
Possible values: **error** - the operation is not allowed. Always present in the response.
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the result code for a duplicate record ID.
Possible values: **DUPLICATE_DATA** - this record ID appears more than once in the request.
          - `details` (object) **REQ** — Represents additional details about the duplicate record. Always present in the response.
            - `id` (string/string) **REQ** — Represents the unique identifier of the duplicate record. Always present in the response.
          - `message` (string) **REQ** [enum=['Duplicate Data']] — Represents the message for the duplicate data result. Always present in the response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status for this result item.
Possible values: **error** - a duplicate record ID was found. Always present in the response.

- **400**: The request failed for all records. Possible causes include invalid record IDs, duplicate IDs, or a NOT_ALLOWED condition. Resolution: Review the error details and correct the request before retrying. [application/json]
    > Represents the 400 error response schema for the shareBulkEmails operation, returned when per-record or request-level validation fails.
    oneOf:
        - `data` (array of object) [maxItems=100] — Represents the list of per-record INVALID_DATA results returned when record IDs fail validation.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the result code for a record that failed validation.
Possible values: **INVALID_DATA** - the record ID is invalid or not found.
          - `details` (object) **REQ** — Represents additional details about the invalid record. Always present in the response.
            - `id` (string/string) — Represents the unique identifier of the invalid record. Always present in the response.
          - `message` (string) **REQ** [enum=['the related id given seems to be invalid']] — Represents the error message for the invalid data result. Always present in the response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status for this error result.
Possible values: **error** - the record ID is invalid. Always present in the response.
        - `data` (array of object) [maxItems=100] — Represents the list of per-record NOT_ALLOWED results returned when the operation is not permitted.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the result code for a record where the operation is not permitted.
Possible values: **NOT_ALLOWED** - the operation is not allowed for this record.
          - `details` (object) **REQ** — Represents additional error context for the not-allowed result. Always present in the response.
            - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path element where the error occurred. Always present in the response.
          - `message` (string/string) **REQ** — Represents the error message for the not-allowed result. Always present in the response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status for this error result.
Possible values: **error** - the operation is not allowed. Always present in the response.
        - `data` (array of object) [maxItems=100] — Represents the list of per-record DUPLICATE_DATA results returned when duplicate record IDs are submitted.
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the result code for a duplicate record ID.
Possible values: **DUPLICATE_DATA** - this record ID appears more than once in the request.
          - `details` (object) **REQ** — Represents additional details about the duplicate record. Always present in the response.
            - `id` (string/string) **REQ** — Represents the unique identifier of the duplicate record. Always present in the response.
          - `message` (string) **REQ** [enum=['Duplicate Data']] — Represents the error message for the duplicate data result. Always present in the response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status for this error result.
Possible values: **error** - a duplicate record ID was found. Always present in the response.

- **403**: The authenticated user lacks the required module CREATE permission. Resolution: Ensure the access token includes the correct `ZohoCRM.modules.{moduleName}.CREATE` scope. [application/json]
    > Represents the NO_PERMISSION error response when the authenticated user lacks the required module CREATE permission.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for this response.
Possible values: **NO_PERMISSION** - the authenticated user lacks the required module CREATE permission. Always present in the response.
    - `details` (object) **REQ** — Represents additional context about the missing permission. Always present in the response.
      - `permissions` (array of string/string) [maxItems=10] — Represents the list of required permission identifiers that the user lacks.
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message describing the missing permission. Always present in the response.
    - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. Always present in the response.

**Scopes:** ZohoCRM.modules.Leads.CREATE, ZohoCRM.modules.Contacts.CREATE, ZohoCRM.modules.Accounts.CREATE, ZohoCRM.modules.Deals.CREATE, ZohoCRM.modules.Tasks.CREATE, ZohoCRM.modules.Events.CREATE, ZohoCRM.modules.Calls.CREATE, ZohoCRM.modules.Products.CREATE, ZohoCRM.modules.Vendors.CREATE, ZohoCRM.modules.Campaigns.CREATE, ZohoCRM.modules.Cases.CREATE, ZohoCRM.modules.Solutions.CREATE, ZohoCRM.modules.Quotes.CREATE, ZohoCRM.modules.Invoices.CREATE, ZohoCRM.modules.Forecasts.CREATE, ZohoCRM.modules.Activities.CREATE, ZohoCRM.modules.Notes.CREATE, ZohoCRM.modules.Attachments.CREATE, ZohoCRM.modules.custom.CREATE, ZohoCRM.modules.CREATE

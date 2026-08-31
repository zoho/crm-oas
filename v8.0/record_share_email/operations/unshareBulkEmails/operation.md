# POST /{moduleApiName}/actions/unshare_emails
**Operation:** `unshareBulkEmails` — Unshare emails in bulk
> To revoke email sharing for multiple CRM records in a single request. Accepts up to 100 record IDs per request. The `data` array in the 207 response contains an item for each record, indicating success or failure.

**Parameters:**
- `moduleApiName` (path, string, required) [enum=['Leads', 'Contacts', 'Accounts', 'Deals', 'CustomModule1']]: Specify the API name of the module that contains the records whose email sharing you want to revoke. Refer to [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve available module API names.

**Request Body** (required) — application/json
> The request body must contain an **ids** array with up to 100 record IDs whose email sharing you want to revoke.
  > Represents the request body schema for unsharing emails in bulk, containing an array of record IDs.
  - `ids` (array of string/string) [maxItems=100] **REQ** — Specify the list of record IDs whose email sharing you want to revoke. Accepts up to 100 record IDs per request.

**Responses:**

- **207**: Returns a mix of success and failure results when some email unsharing operations succeed and others fail. Inspect each item in the `data` array for the individual outcome. [application/json]
    > Represents the 207 partial success response schema for the unshareBulkEmails operation, where each item indicates an individual record's outcome.
    - `data` (array of object) [maxItems=100] — Represents the list of per-record results for the bulk email unsharing operation. Always present in the response.
      oneOf:
          - `code` (string) **REQ** [enum=['NOT_SHARED']] — Represents the result code for a record whose emails are not currently shared.
Possible values: **NOT_SHARED** - the emails for this record are not shared with colleagues.
          - `details` (object) **REQ** — Represents additional details about the record. Always present in the response.
            - `id` (string/string) **REQ** — Represents the unique identifier of the record. Always present in the response.
          - `message` (string) **REQ** [enum=['Emails are not  shared to the colleagues already']] — Represents the message describing the not-shared status. Always present in the response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status for this result item.
Possible values: **error** - the emails are not currently shared. Always present in the response.
          - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for a successfully unshared record.
Possible values: **SUCCESS** - the email sharing was successfully revoked for this record.
          - `details` (object) **REQ** — Represents the details of the record whose email sharing was revoked. Always present in the response.
            - `id` (string/string) **REQ** — Represents the unique identifier of the successfully unshared record. Always present in the response.
          - `message` (string) **REQ** [enum=['Sharing revoked successfully']] — Represents the result message for the successfully unshared record. Always present in the response.
          - `status` (string) **REQ** [enum=['success']] — Represents the status for this result item.
Possible values: **success** - the email sharing was revoked for this record. Always present in the response.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the result code for a record that failed validation.
Possible values: **INVALID_DATA** - the record ID is invalid or not found.
          - `details` (object) **REQ** — Represents additional details about the invalid record. Always present in the response.
            - `id` (string/string) **REQ** — Represents the unique identifier of the invalid record. Always present in the response.
          - `message` (string) **REQ** [enum=['the related id given seems to be invalid']] — Represents the error message for the invalid data result. Always present in the response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status for this result item.
Possible values: **error** - the record ID is invalid. Always present in the response.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the result code for a record where the operation is not allowed.
Possible values: **NOT_ALLOWED** - the unsharing operation is not permitted for this record.
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

- **403**: The authenticated user lacks the required module DELETE permission. Resolution: Ensure the access token includes the correct `ZohoCRM.modules.{moduleName}.DELETE` scope. [application/json]
    > Represents the NO_PERMISSION error response when the authenticated user lacks the required module DELETE permission.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for this response.
Possible values: **NO_PERMISSION** - the authenticated user lacks the required module DELETE permission. Always present in the response.
    - `details` (object) **REQ** — Represents additional context about the missing permission. Always present in the response.
      - `permissions` (array of string/string) [maxItems=10] — Represents the list of required permission identifiers that the user lacks.
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message describing the missing permission. Always present in the response.
    - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. Always present in the response.

**Scopes:** ZohoCRM.modules.Leads.DELETE, ZohoCRM.modules.Contacts.DELETE, ZohoCRM.modules.Accounts.DELETE, ZohoCRM.modules.Deals.DELETE, ZohoCRM.modules.Tasks.DELETE, ZohoCRM.modules.Events.DELETE, ZohoCRM.modules.Calls.DELETE, ZohoCRM.modules.Products.DELETE, ZohoCRM.modules.Vendors.DELETE, ZohoCRM.modules.Campaigns.DELETE, ZohoCRM.modules.Cases.DELETE, ZohoCRM.modules.Solutions.DELETE, ZohoCRM.modules.Quotes.DELETE, ZohoCRM.modules.Invoices.DELETE, ZohoCRM.modules.Forecasts.DELETE, ZohoCRM.modules.Activities.DELETE, ZohoCRM.modules.Notes.DELETE, ZohoCRM.modules.Attachments.DELETE, ZohoCRM.modules.custom.DELETE, ZohoCRM.modules.DELETE

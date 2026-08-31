# POST /{moduleApiName}/{id}/actions/share_emails
**Operation:** `shareEmails` — Share Record Emails
> To share email threads linked to a specific CRM record with colleagues in the same organization. Requires custom email sharing to be enabled in the organization and a valid email configuration for the user.

**Parameters:**
- `moduleApiName` (path, string, required) [enum=['Leads', 'Contacts', 'Accounts', 'Deals', 'CustomModule1']]: Specify the API name of the module that contains the record whose emails you want to share. Refer to [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve available module API names.
- `id` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique identifier of the record whose emails you want to manage. The ID must belong to a record in the specified module. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the record IDs.

**Responses:**

- **200**: Returns the per-record email sharing result after the operation completes successfully. [application/json]
    > Represents the 200 response schema for the shareEmails operation, containing an array of per-record email sharing results.
    - `data` (array of object) [maxItems=100] — Represents the list of per-record email sharing results. Always present in the response.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the email sharing operation.
Possible values: **SUCCESS** - the email sharing completed successfully. Always present in the response.
      - `details` (object) **REQ** — Represents the details of the record that was shared. Always present in the response.
        - `id` (string/string) **REQ** — Represents the unique identifier of the shared record. Always present in the response.
      - `message` (string) **REQ** [enum=['Successfully shared']] — Represents the result message for the email sharing operation. Always present in the response.
      - `status` (string) **REQ** [enum=['success']] — Represents the overall operation status.
Possible values: **success** - the email sharing completed successfully. Always present in the response.

- **400**: The request failed. Possible causes include an invalid record ID, an invalid or unsupported module, emails already being shared, a missing email configuration, or custom email sharing not being enabled. Resolution: Review the error code and details to correct the request before retrying. [application/json]
    > Represents the 400 error response schema for the shareEmails operation, returned when input validation fails.
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
Possible values: **INVALID_DATA** - a field value failed validation. Always present in the response.
        - `details` (object) **REQ** — Represents additional context about the validation error. Always present in the response.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path element where the error occurred. Always present in the response.
        - `message` (string) **REQ** [enum=['the related id given seems to be invalid']] — Represents the error message describing the validation failure. Always present in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. Always present in the response.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for this response.
Possible values: **INVALID_MODULE** - the specified module name is not valid. Always present in the response.
        - `details` (object) **REQ** — Represents additional context about the invalid module error. Always present in the response.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path element where the error occurred. Always present in the response.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message describing the invalid module. Always present in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. Always present in the response.
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the error code for this response.
Possible values: **NOT_SUPPORTED** - the specified module does not support email sharing. Always present in the response.
        - `details` (object) **REQ** — Represents additional context about the unsupported module error. Always present in the response.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path element where the error occurred. Always present in the response.
        - `message` (string) **REQ** [enum=['the given module is not supported in api']] — Represents the error message describing the unsupported module. Always present in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. Always present in the response.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this response.
Possible values: **NOT_ALLOWED** - the organization has not enabled custom email sharing. Always present in the response.
        - `details` (object) **REQ** — Represents additional error context. Always present in the response.
        - `message` (string) **REQ** [enum=['User did not enable custom sharing']] — Represents the error message when custom email sharing is not enabled. Always present in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. Always present in the response.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this response.
Possible values: **NOT_ALLOWED** - no email configuration exists for this user. Always present in the response.
        - `details` (object) **REQ** — Represents additional error context. Always present in the response.
        - `message` (string) **REQ** [enum=['Email Configuration does not exist']] — Represents the error message when no email configuration exists. Always present in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. Always present in the response.
        - `data` (array of object) [maxItems=100] — Represents the list of per-record already-shared results. Always present in the response.
          - `code` (string) **REQ** [enum=['ALREADY_SHARED']] — Represents the result code.
Possible values: **ALREADY_SHARED** - the emails for this record are already shared with colleagues.
          - `details` (object) **REQ** — Represents additional details about the already-shared record. Always present in the response.
            - `id` (string/string) **REQ** — Represents the unique identifier of the already-shared record. Always present in the response.
          - `message` (string) **REQ** [enum=['Emails are already shared to the colleagues already']] — Represents the message describing the already-shared status. Always present in the response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status for this result item.
Possible values: **error** - the emails are already shared. Always present in the response.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
Possible values: **INVALID_DATA** - a field value has an incorrect data type. Always present in the response.
        - `details` (object) **REQ** — Represents additional context about the data type error. Always present in the response.
          - `expected_data_type` (string/string) **REQ** — Represents the expected data type for the field. Always present in the response.
          - `api_name` (string/string) **REQ** — Represents the API name of the field that has an incorrect data type. Always present in the response.
        - `message` (string/string) **REQ** — Represents the error message describing the data type mismatch. Always present in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. Always present in the response.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this response.
Possible values: **NOT_ALLOWED** - the operation is not permitted. Always present in the response.
        - `details` (object) **REQ** — Represents additional error context. Always present in the response.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path element where the error occurred. Always present in the response.
        - `message` (string/string) **REQ** — Represents the error message describing why the operation is not allowed. Always present in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. Always present in the response.

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

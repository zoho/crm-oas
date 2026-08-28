# POST /{moduleApiName}/{id}/actions/unshare_emails
**Operation:** `unshareEmails` — Unshare Record Emails
> To revoke email sharing for a specific CRM record, making the linked email threads no longer visible to colleagues. Requires custom email sharing to be enabled in the organization and a valid email configuration for the user.

**Parameters:**
- `moduleApiName` (path, string, required) [enum=['Leads', 'Contacts', 'Accounts', 'Deals', 'CustomModule1']]: Specify the API name of the module that contains the record whose email sharing you want to revoke. Refer to [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve available module API names.
- `id` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique identifier of the record whose emails you want to manage. The ID must belong to a record in the specified module. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the record IDs.

**Responses:**

- **200**: Returns the per-record email unsharing result after the operation completes successfully. [application/json]
    > Represents the 200 response schema for the unshareEmails operation, containing an array of per-record email unsharing results.
    - `data` (array of object) [maxItems=100] — Represents the list of per-record email unsharing results. Always present in the response.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the email unsharing operation.
Possible values: **SUCCESS** - the email sharing was successfully revoked. Always present in the response.
      - `details` (object) **REQ** — Represents the details of the record whose email sharing was revoked. Always present in the response.
        - `id` (string/string) **REQ** — Represents the unique identifier of the unshared record. Always present in the response.
      - `message` (string) **REQ** [enum=['Sharing revoked successfully']] — Represents the result message for the email unsharing operation. Always present in the response.
      - `status` (string) **REQ** [enum=['success']] — Represents the overall operation status.
Possible values: **success** - the email sharing was successfully revoked. Always present in the response.

- **400**: The request failed. Possible causes include an invalid record ID, an invalid or unsupported module, a missing email configuration, or custom email sharing not being enabled. Resolution: Review the error code and details to correct the request before retrying. [application/json]
    > Represents the 400 error response schema for the unshareEmails operation, returned when input validation fails.
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

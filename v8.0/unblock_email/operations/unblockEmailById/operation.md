# POST /{module}/{id}/actions/unblock_email
**Operation:** `unblockEmailById` — Unblock email for a single record
> To unblock a soft-bounced email address for a single record in your Zoho CRM organization. When an email sent from CRM bounces temporarily, the Email field on the affected record is blocked. This operation removes that block so email communication with the record can resume.

**Parameters:**
- `module` (path, string, required) [enum=['Leads']]: Represents the module API name. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get valid values. 
- `id` (path, string, required) [maxLen=50]: Represents the unique ID of the record. Use the [Get Records API](record.yaml#$.paths./{module}.get) to get valid values.

**Request Body** (required) — application/json
> The request body contains the data required to perform the operation. 
  > Specify the email fields to unblock for the record.
  - `unblock_fields` (array of string) [maxItems=1] **REQ** — To unblock emails, specify one or both of the system-defined
fields : **Email** and **Secondary_Email**.


> **Note**

> - The permanently blocked emails cannot be unblocked.

> - A temporarily blocked email can be unblocked up to **5
times**.

> - A **custom email field** cannot be unblocked.

> - You cannot merge records that are **locked** or in an
**Approval Process/Review Process**.

    items: [enum=['Email']]

**Responses:**

- **200**: Returns the result of the email unblock operation, including the status code, record details, and a confirmation message. [application/json]
    > Contains the result of the email unblock operation for the specified record.
    - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the status code of the unblock operation.
    - `details` (object) **REQ** — Contains the details of the record for which the email was unblocked.
      - `id` (string) **REQ** [maxLen=50] — Represents the unique identifier of the record for which the email was unblocked.
    - `message` (string) **REQ** [maxLen=255] — Represents the descriptive message returned by the server for the unblock operation.
    - `status` (string) **REQ** [maxLen=255] — Represents the overall status of the unblock operation for the record.

- **400**: The request is invalid.


**Resolution:** A valid module API name and record ID must be
specified in the request URL, and the OAuth token must include the
required scope.
 [application/json]
    > Contains one of several error response structures returned when the unblock request fails due to invalid parameters, authentication issues, or data validation errors.
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Represents the response status indicating an error occurred.
        - `code` (string) **REQ** [enum=[4 values]] — Represents the error code returned by the server.

Possible values:

**INVALID_URL_PATTERN** - The request URL is
incorrect.

**INVALID_DATA** - The request contains invalid data.

**INVALID_REQUEST_METHOD** - The HTTP method is not
valid for this endpoint.

**INVALID_TOKEN** - The OAuth token is invalid or
expired.

        - `message` (string) **REQ** [enum=['invalid oauth token']] — Represents the error message returned by the server indicating the issue.
        - `details` (object) **REQ** — Contains additional context about the error, such as the field or parameter that caused the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the response status indicating an error occurred.
        - `code` (string) **REQ** [enum=[4 values]] — Represents the error code returned by the server.

Possible values:

**INVALID_URL_PATTERN** - The request URL is
incorrect.

**INVALID_DATA** - The request contains invalid data.

**INVALID_REQUEST_METHOD** - The HTTP method is not
valid for this endpoint.

**INVALID_MODULE** - The specified module name is not
valid.

        - `message` (string) **REQ** [enum=[3 values]] — Represents the error message describing the reason the request failed, such as an invalid token, invalid record, or invalid module name.
        - `details` (object) **REQ** — Contains additional context about the error, including the index of the resource in the request path that caused the failure.
          - `resource_path_index` (integer/int32) — Represents the zero-based index of the resource segment in the request path that triggered the error.
        - `status` (string) **REQ** [enum=['error']] — Represents the response status indicating an error occurred.
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'INVALID_MODULE', 'MANDATORY_NOT_FOUND']] — Represents the error code returned by the server.

Possible values:

**INVALID_DATA** - The request contains invalid data.

**INVALID_MODULE** - The specified module name is not
valid.

**MANDATORY_NOT_FOUND** - A required field is missing
from the request body.

        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the validation or data issue encountered by the server.
        - `details` (object) **REQ** — Contains additional context about the validation error, including the expected data type and the field that caused the failure.
          oneOf:
              - `expected_data_type` (string) [maxLen=255] — Represents the data type expected by the server for the field that caused the error.
              - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the validation error.
              - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field in the request body that caused the validation error.
              - `api_name` (string) [maxLen=255] — Represents the API name of the field that caused the validation error.
              - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field in the request body that caused the validation error.

**Scopes:** ZohoCRM.modules.leads.UPDATE, ZohoCRM.modules.accounts.UPDATE, ZohoCRM.modules.contacts.UPDATE, ZohoCRM.modules.deals.UPDATE, ZohoCRM.modules.quotes.UPDATE, ZohoCRM.modules.salesorders.UPDATE, ZohoCRM.modules.purchaseorders.UPDATE, ZohoCRM.modules.custom.UPDATE, ZohoCRM.modules.cases.UPDATE

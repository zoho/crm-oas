# GET /{moduleApiName}/{id}/__emails_sharing_details
**Operation:** `getEmailSharingDetail` — Get email sharing details for a record
> To retrieve the email sharing details for a specific record in your Zoho CRM organization, including the users whose email accounts are accessible and the available email filter options for the record's email view.

**Parameters:**
- `moduleApiName` (path, string, required) [enum=['Leads', 'Contacts', 'Accounts', 'Deals', 'CustomModule1']]: Specifies the **API name** of the module for which you want to retrieve the email sharing details. 
Possible values: **Leads**, **Contacts**, **Accounts**, **Deals**, **CustomModule1**. 
Refer to the [Retrieve CRM module metadata](modules.json#$.paths./settings/modules.get) resource for valid values.
- `id` (path, string, required) [maxLen=100]: Specify the **ID** of the **record** for which you want to retrieve the email sharing details.

**Responses:**

- **200**: Returns the email sharing configuration for the requested record, including the users with accessible email accounts and the available email filter options. [application/json]
    > Represents the response body for the **Get Email Shared Details** operation, containing the email sharing configuration for the requested record.
    - `__emails_sharing_details` (array of object) [maxItems=1] — A JSON array representing the list of email sharing configurations for the record, including the users whose emails can be shared and the available email filter options.
      - `shared_from_users` (array of object) [maxItems=50, nullable] **REQ** — Specifies the list of users whose email accounts are accessible when viewing the record's emails. Always returned in the response.
        - `name` (string) **REQ** [maxLen=250] — Represents the name of the user with email access.
        - `_type` (string) **REQ** [enum=['imap', 'pop', 'api']] — Represents the type of email account used by the user. Possible values: **imap**, **pop**, **api**. Always returned in the response.
        - `id` (string) **REQ** [maxLen=100] — Represents the unique ID of the user. Always returned in the response.
      - `available_types` (array of string) [minItems=1, maxItems=5] **REQ** — Represents the available email filter options for the record's email view. Always returned in the response.
        items: [enum=[5 values]]

- **400**: The request contains invalid data or an unrecognized module API name. 
**Resolution:** The module API name in the request URL must match one of the supported modules, and the record ID must be valid. [application/json]
    > Represents the error response body returned when the request fails due to invalid input or an unrecognized module.
    - `code` (string) **REQ** [enum=['INVALID_DATA', 'INVALID_MODULE']] — Represents the error code that identifies the type of error. Possible values: **INVALID_DATA**, **INVALID_MODULE**. Always returned in the response.
    - `message` (string) **REQ** [enum=[3 values]] — Represents the error message that describes the cause of the error. Possible values: **The given data is invalid.**, **The module API name is invalid.**. Always returned in the response.
    - `details` (object) **REQ** — Represents an object containing additional context about the error, such as the path segment where the issue occurred. Always returned in the response.
      - `resource_path_index` (integer/int32) — Represents the index of the path segment in the request URL where the error occurred.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error**. Always returned in the response.

**Scopes:** ZohoCRM.modules.ALL, ZohoCRM.modules.emails.READ

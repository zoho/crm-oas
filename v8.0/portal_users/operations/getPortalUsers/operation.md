# GET /settings/portals/{portal}/user_type/{userType}/users
**Operation:** `getPortalUsers` — List portal users
> To retrieve the list of portal users in your Zoho CRM organization for the specified portal and user type, with optional filtering by source.

**Parameters:**
- `portal` (path, string, required) [maxLen=255]: Specify the unique identifier of the portal. Refer to the [Get Portals](https://www.zoho.com/crm/developer/docs/api/v8/get-portals.html) resource for valid values.
- `userType` (path, integer/int64, required) [maxLen=255]: Specify the user type of the portal users. Refer to the [Get Portal User Types](https://www.zoho.com/crm/developer/docs/api/v8/get-user-types.html) resource for valid values.
- `page` (query, integer/int32, optional): Represents the number of records to return per page.
- `per_page` (query, integer/int32, optional): Represents number of records to return per page.
- `Source__s` (query, string, optional) [maxLen=255]: Represents the source of the user record.
- `filters` (query, string, optional) [maxLen=255]: Represents the filters of the user record.
- `personality_ids` (query, string, optional) [maxLen=255]: Represents the list of portal user record IDs to filter the results.
- `type` (query, string, optional) [maxLen=255]: Represents the filter type for the portal users.

**Responses:**

- **200**: Returns the list of portal users for the specified portal and user type. [application/json]
    > Response containing the list of portal users and pagination metadata.
    - `users` (array of object) [maxItems=10000] **REQ** — Represents the list of portal user objects.
      - `personality_id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the portal user record.
      - `confirm` (boolean) **REQ** — Indicates whether the portal user has confirmed their account. Possible values: **true**, **false**. 
      - `status_reason__s` (string) **REQ** [maxLen=500] — Represents the reason for the current status of the portal user.
      - `created_time` (string/date-time) **REQ** — Represents the date and time of portal user creation.
      - `module` (string) **REQ** [maxLen=100] — Represents the API name of the CRM module associated with the portal user.
      - `name` (string) **REQ** [maxLen=255] — Represents the full name of the portal user.
      - `active` (boolean) **REQ** — Indicates whether the portal user is currently active. Possible values: **true**, **false**. 
      - `email` (string/email) **REQ** — Represents the email address of the portal user.
      - `Source__s` (string) **REQ** [maxLen=255] — Represents the source of the portal user record.
    - `info` (object) **REQ** — Represents pagination metadata for the response.
      - `total_count` (integer/int32) **REQ** — Represents the total number of portal users available for the specified portal and user type.

- **204**: No portal users found for the specified portal and user type. The portal has no users yet.

- **400**: Invalid request - a query parameter value does not match the expected format. Resolution: Check the error details for the parameter name and correct the value. [application/json]
    > Response schema for this operation.
    oneOf:
        - `code` (string) **REQ** [enum=['PATTERN_NOT_MATCHED']] — Represents the error code. Possible values: **PATTERN_NOT_MATCHED**. 
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
        - `details` (object) **REQ** — Represents additional details about the error.
          - `api_name` (string) [maxLen=255] — Represents the API name of the parameter that caused the error.
          - `json_path` (string) [maxLen=255] — Represents the JSON path to the parameter that caused the error. Returned when available.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**. 
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Represents the error code. Possible values: **API_NOT_SUPPORTED**. 
        - `details` (object) **REQ** — Represents additional details about the error.
          - `unsupported_environment` (string) **REQ** [maxLen=255] — Represents the name of the environment where this API is not supported.
        - `message` (string) **REQ** [enum=['api not supported in sandbox']] — Represents the error message. Possible values: **api not supported in sandbox**. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**. 

- **403**: Permission denied. Resolution: The CRM administrator must grant the **ZohoCRM.settings.clientportal** scope permission to the user's profile. [application/json]
    > Response schema for this operation.
    oneOf:
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code. Possible values: **NO_PERMISSION**. 
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**. 
        - `portal_invite` (array of object) [maxItems=100] **REQ** — Represents the list of portal invitation permission error objects.
          - `code` (string) **REQ** [maxLen=255] — Represents the status code of the operation.
          - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
        - `portal_invite` (array of object) [maxItems=100] **REQ** — Represents the list of portal invitation permission error objects.
        - `portal_invite` (array of object) [maxItems=100] — Represents the list of portal invitation permission error objects.

**Scopes:** ZohoCRM.settings.clientportal.READ

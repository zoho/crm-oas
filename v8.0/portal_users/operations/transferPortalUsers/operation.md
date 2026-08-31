# POST /settings/portals/{portal}/user_type/{userType}/users/action/transfer
**Operation:** `transferPortalUsers` — Transfer portal users from one user group to another
> To transfer one or more portal users from one user type group to another within the same portal in your Zoho CRM organization.

**Parameters:**
- `portal` (path, string, required) [maxLen=255]: Specify the unique identifier of the portal. Refer to the [Get Portals](https://www.zoho.com/crm/developer/docs/api/v8/get-portals.html) resource for valid values.
- `userType` (path, integer/int64, required) [maxLen=255]: Specify the user type of the portal users. Refer to the [Get Portal User Types](https://www.zoho.com/crm/developer/docs/api/v8/get-user-types.html) resource for valid values.
- `transfer_To` (query, string/int64, required): The ID of the user type to which you want to transfer the users.
- `personality_ids` (query, string/int64, required): The ID of the user type to which you want to transfer the users.

**Responses:**

- **200**: Returns the transfer result for the requested portal users. [application/json]
    > Response containing the transfer result for each requested portal user.
    - `users` (array of object) [maxItems=100] **REQ** — Represents the list of transferred portal user results. Contains one result object per transferred user.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the error code. Possible values: **SUCCESS**. 
      - `details` (object) **REQ** — Represents additional details about the operation result.
        - `personality_id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the portal user record.
      - `message` (string) **REQ** [maxLen=1000] — Represents the success or informational message for this operation result.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation. Possible values: **success**. 

- **400**: Invalid request - the transfer failed due to missing or invalid parameters. Resolution: Check the error code and ensure all required parameters are provided. [application/json]
    > Response schema for this operation.
    oneOf:
        - `code` (string) **REQ** [maxLen=255, enum=['REQUIRED_PARAM_MISSING', 'INVALID_DATA']] — Represents the error code. Possible values: **REQUIRED_PARAM_MISSING**, **INVALID_DATA**. 
        - `details` (object) **REQ** — Represents additional details about the error.
          - `transfer_To` (string) [maxLen=255] — Represents the identifier of the destination user type provided in the request. Returned when available.
          - `param` (string) [enum=['personality_ids', 'transfer_To']] — Represents the name of the missing or invalid parameter. Possible values: **personality_ids**, **transfer_To**. Returned when available.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
        - `status` (string) **REQ** [maxLen=255] — Represents the status of the response.
        - `users` (array of object) [maxItems=100] **REQ** — Represents the list of transfer error results. Each object contains error details for a failed transfer.
          - `code` (string) **REQ** [maxLen=255, enum=['INVALID_DATA']] — Represents the error code. Possible values: **INVALID_DATA**. 
          - `details` (object) **REQ** — Represents additional details about the error.
            - `personality_id` (string) **REQ** [maxLen=255] — Represents the identifier of the portal user record associated with the error. Returned when available.
          - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
          - `status` (string) **REQ** [maxLen=255] — Represents the status of the response.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Represents the error code. Possible values: **API_NOT_SUPPORTED**. 
        - `details` (object) **REQ** — Represents additional details about the error.
          - `unsupported_environment` (string) **REQ** [maxLen=255] — Represents the name of the environment where this API is not supported.
        - `message` (string) **REQ** [enum=['api not supported in sandbox']] — Represents the error message. Possible values: **api not supported in sandbox**. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**. 

- **403**: Permission denied. Resolution: The CRM administrator must grant the **ZohoCRM.settings.clientportal** scope permission to the user's profile. [application/json]
    > Error response returned when the authenticated user does not have the required permission to perform the operation.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code. Possible values: **NO_PERMISSION**. 
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
    - `details` (object) **REQ** — Represents additional details about the error.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**. 

**Scopes:** ZohoCRM.settings.clientportal.CREATE

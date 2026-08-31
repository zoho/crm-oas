# DELETE /settings/portals/{portal}/user_type/{userType}/users
**Operation:** `deletePortalUsers` — delete portal users
> To delete one or more portal users from your Zoho CRM organization for the specified portal and user type.

**Parameters:**
- `portal` (path, string, required) [maxLen=255]: Specify the unique identifier of the portal. Refer to the [Get Portals](https://www.zoho.com/crm/developer/docs/api/v8/get-portals.html) resource for valid values.
- `userType` (path, integer/int64, required) [maxLen=255]: Specify the user type of the portal users. Refer to the [Get Portal User Types](https://www.zoho.com/crm/developer/docs/api/v8/get-user-types.html) resource for valid values.
- `personality_ids` (query, string/int64, optional) [maxLen=255]: List for record IDs of portal users to be deleted.

**Responses:**

- **200**: Returns the deletion result for the requested portal users. [application/json]
    > Response containing the deletion result for each requested portal user.
    - `users` (array of object) [maxItems=200] **REQ** — Represents the list of deleted portal user results. Contains one result object per requested deletion.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the error code. Possible values: **SUCCESS**. 
      - `message` (string) **REQ** [maxLen=1000] — Represents the success or informational message for this operation result.
      - `details` (object) **REQ** — Represents additional details about the operation result.
        - `personality_id` (string) [maxLen=255] — Represents the unique identifier of the portal user record.
      - `status` (string) **REQ** [enum=['error', 'success']] — Represents the status of the operation. Possible values: **error**, **success**. 

- **400**: Invalid request - the deletion failed due to a validation error. Resolution: Check the error code and correct the request before retrying. [application/json]
    > Response schema for this operation.
    oneOf:
        - `users` (array of object) [maxItems=200] — Represents the list of deletion error results. Each object contains error details for a failed deletion.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. Possible values: **INVALID_DATA**. 
          - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
          - `details` (object) **REQ** — Represents additional details about the error.
            - `personality_id` (string/int64) — Represents the identifier of the portal user record associated with the error. Returned when available.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**. 
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

**Scopes:** ZohoCRM.settings.clientportal.DELETE

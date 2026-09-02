# PUT /settings/portals/{portal}/user_type/{userType}/users/{recordId}/actions/change_status
**Operation:** `changePortalUsersStatus` — Change status of portal users
> Changing portal users status.

**Parameters:**
- `portal` (path, string, required) [maxLen=255]: Specify the unique identifier of the portal. Refer to the [Get Portals](https://www.zoho.com/crm/developer/docs/api/v8/get-portals.html) resource for valid values.
- `userType` (path, integer/int64, required) [maxLen=255]: Specify the user type of the portal users. Refer to the [Get Portal User Types](https://www.zoho.com/crm/developer/docs/api/v8/get-user-types.html) resource for valid values.
- `recordId` (path, integer/int64, required): Specify the unique identifier of the CRM record for which you want to perform the portal action.
- `active` (query, boolean, required): **true** activates the user in the portal, and **false** deactivates the user in the portal.

**Responses:**

- **200**: Returns the status change result for the portal user. [application/json]
    > Response containing the status change result for the portal user.
    - `change_status` (array of object) [maxItems=100] **REQ** — Represents the list of portal user status change results. Contains one result object per requested status change.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the error code. Possible values: **SUCCESS**. 
      - `details` (object) **REQ** — Represents additional details about the operation result.
        - `personality_id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the portal user record.
      - `message` (string) **REQ** [maxLen=1000] — Represents the success or informational message for this operation result.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation. Possible values: **success**. 

- **400**: Invalid request - the status change failed due to a validation error. Resolution: Check the error code and correct the request parameters before retrying. [application/json]
    > Response schema for this operation.
    oneOf:
        - `code` (string) **REQ** [maxLen=255, enum=['ALREADY_ACTIVATED', 'INVALID_DATA', 'LIMIT_EXCEEDED', 'NOT_ALLOWED']] — Represents the error code. Possible values: **ALREADY_ACTIVATED**, **INVALID_DATA**, **LIMIT_EXCEEDED**, **NOT_ALLOWED**. 
        - `details` (object) **REQ** — Represents additional details about the error.
          - `resource_path_index` (string) [maxLen=255] — Represents the record identifier associated with the error. Returned when available.
          - `limit` (integer/int32) — Represents the configured portal user limit for this portal. Returned when available.
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

**Scopes:** ZohoCRM.settings.clientportal.UPDATE

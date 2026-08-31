# PUT /settings/portals/{portal}/user_type/{userType}/users/actions/change_status
**Operation:** `changePortalUsersStatusBulk` — Portal User Status
> To activate or deactivate multiple portal users in bulk in your Zoho CRM organization for the specified portal and user type.

**Parameters:**
- `portal` (path, string, required) [maxLen=255]: Specify the unique identifier of the portal. Refer to the [Get Portals](https://www.zoho.com/crm/developer/docs/api/v8/get-portals.html) resource for valid values.
- `userType` (path, integer/int64, required) [maxLen=255]: Specify the user type of the portal users. Refer to the [Get Portal User Types](https://www.zoho.com/crm/developer/docs/api/v8/get-user-types.html) resource for valid values.

**Request Body** — application/json
> The request body must contain a **change_status** array. You can include the personality identifiers and new active status for the portal users.
  > Request body for changing status of portal users
  - `change_status` (array of object) [maxItems=100] **REQ** — Represents the list of portal user status change results. Contains one result object per requested status change.
    - `users` (array of object) [maxItems=100] **REQ** — Represents the list of portal user objects.
      - `active` (boolean) **REQ** — Indicates whether the portal user is currently active. Possible values: **true**, **false**.
      - `personality_id` (string) **REQ** [maxLen=255] — Specify the unique identifier of the portal user record.

**Responses:**

- **200**: Returns the status change result for the portal user. [application/json]
    > Response containing the status change result for the portal user.
    - `change_status` (array of object) [maxItems=100] **REQ** — Represents the list of portal user status change results. Contains one result object per requested status change.
      - `code` (string) **REQ** [enum=['SCHEDULED']] — Represents the error code. Possible values: **SCHEDULED**. 
      - `details` (object) **REQ** — Represents additional details about the operation result.
        - `job_id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the scheduled invitation job.
      - `message` (string) **REQ** [maxLen=1000] — Represents the success or informational message for this operation result.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation. Possible values: **success**. 

- **400**: This API is not supported in sandbox environments. Resolution: The request must be made from a production Zoho CRM organization, not a sandbox. [application/json]
    > Error response returned when the API is invoked in an unsupported environment, such as a sandbox.
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

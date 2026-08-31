# POST /{module}/actions/portal_invite
**Operation:** `inviteUsers` — Invite portal users
> To send portal invitations in bulk to CRM records in your Zoho CRM organization for the specified module, scheduling them as asynchronous invitation jobs.

**Parameters:**
- `module` (path, string, required) [maxLen=255]: Specify the API name of the CRM module for which you want to manage portal users. Refer to the [Get Modules](https://www.zoho.com/crm/developer/docs/api/v8/modules-api.html) resource for valid values.

**Request Body** (required) — application/json
> The request body must contain a **portal_invite** array. You can include up to 100 invitation objects, each containing a **data** array of user records to invite.
  > Request body for inviting portal users
  - `portal_invite` (array of object) [maxItems=100] **REQ** — Specify the list of portal invitation objects. Each object must contain a **data** array of user records to invite.
    - `data` (array of object) [maxItems=100] **REQ** — Specify the list of user records to include in this invitation batch.
      - `id` (string/int64) **REQ** [maxLen=255] — Specify the unique identifier of the CRM record to invite as a portal user.
      - `user_type_id` (string/int64) **REQ** [maxLen=255] — Specify the unique identifier of the portal user type to assign. Refer to the [Get Portal User Types](https://www.zoho.com/crm/developer/docs/api/v8/get-user-types.html) resource for valid values.
      - `type` (string) **REQ** [enum=['reinvite', 'invite']] — Specify the invitation action type. Possible values: **invite** (new invitation), **reinvite** (re-send invitation).
      - `language` (string) [enum=[30 values], nullable] — Specify the locale code of the language for the invitation email. Omit or set to null to use the portal's default language.

**Responses:**

- **200**: Returns the scheduled invitation job information. [application/json]
    > Response for portal user invitation requests
    - `portal_invite` (array of object) [maxItems=100] **REQ** — Represents the list of portal invitation response objects. Contains one object per invitation batch.
      - `code` (string) **REQ** [enum=['SCHEDULED']] — Represents the error code. Possible values: **SCHEDULED**. 
      - `details` (object) **REQ** — Represents additional details about the operation result.
        - `job_id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the scheduled invitation job.
      - `message` (string) **REQ** [maxLen=1000] — Represents the success or informational message for this operation result.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation. Possible values: **success**. 

- **400**: Invalid request - one or more fields in the invitation request are invalid or missing. Resolution: Check the error code and correct the request body before retrying. [application/json]
    > Response schema for this operation.
    oneOf:
        - `portal_invite` (array of object) [maxItems=100] **REQ** — Represents the list of portal invitation error objects. Contains one error object per failed invitation.
          - `code` (string) **REQ** [maxLen=255, enum=['MANDATORY_NOT_FOUND', 'INVALID_DATA']] — Represents the error code. Possible values: **MANDATORY_NOT_FOUND**, **INVALID_DATA**. 
          - `details` (object) **REQ** — Represents additional details about the error.
          - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
          - `status` (string) **REQ** [maxLen=255] — Represents the status of the response.
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

**Scopes:** ZohoCRM.settings.clientportal.CREATE

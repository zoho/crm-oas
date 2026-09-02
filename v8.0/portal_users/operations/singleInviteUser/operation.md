# POST /{module}/{recordId}/actions/portal_invite
**Operation:** `singleInviteUser` — Invite portal users
> To send a portal invitation to a single CRM record in your Zoho CRM organization, inviting or re-inviting the record as a portal user for the specified user type.

**Parameters:**
- `module` (path, string, required) [maxLen=255]: Specify the API name of the CRM module for which you want to manage portal users. Refer to the [Get Modules](https://www.zoho.com/crm/developer/docs/api/v8/modules-api.html) resource for valid values.
- `recordId` (path, integer/int64, required): Specify the unique identifier of the CRM record for which you want to perform the portal action.
- `language` (query, string, optional) [enum=[29 values]]: Preferred language for the invitation
- `user_type_id` (query, string, required) [maxLen=255]: The ID of the user type you want to assign this user with. Use the [Get User Types API](https://www.zoho.com/crm/developer/docs/api/v8/get-user-types.html) for this ID.
- `type` (query, string, required) [enum=['reinvite', 'invite']]: Represents whether the user is invited the first time or is re-invited. The possible values are invite and reinvite.

**Responses:**

- **200**: Returns the result of the single portal user invitation. [application/json]
    > Response for portal user invitation requests
    - `portal_invite` (array of object) [maxItems=100] **REQ** — Represents the list of portal invitation response objects. Contains one object per invitation batch.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the error code. Possible values: **SUCCESS**. 
      - `details` (object) **REQ** — Represents additional details about the operation result.
        - `record_id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the CRM record associated with this invitation.
      - `message` (string) [maxLen=1000] — Represents the success or informational message for this operation result.
      - `status` (string) [enum=['success']] — Represents the status of the operation. Possible values: **success**.

- **400**: Invalid request - the portal invitation failed due to a validation error. Resolution: Check the error code for the specific failure reason and correct the request. [application/json]
    > Response schema for this operation.
    oneOf:
        - `code` (string) **REQ** [maxLen=255, enum=[7 values]] — Represents the error code. Possible values: **CANNOT_PROCESS**, **INVALID_DATA**, **REQUIRED_PARAM_MISSING**, **LICENSE_LIMIT_EXCEEDED**, **NOT_REVIEWED**, **NOT_APPROVED**, **DUPLICATE_DATA**. 
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

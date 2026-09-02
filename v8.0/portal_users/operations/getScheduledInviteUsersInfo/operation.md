# GET /{module}/actions/portal_invite
**Operation:** `getScheduledInviteUsersInfo` — Invite portal users
> To retrieve the status of a scheduled portal invitation job in your Zoho CRM organization using the job identifier returned when invitations were scheduled.

**Parameters:**
- `module` (path, string, required) [maxLen=255]: Specify the API name of the CRM module for which you want to manage portal users. Refer to the [Get Modules](https://www.zoho.com/crm/developer/docs/api/v8/modules-api.html) resource for valid values.
- `job_id` (query, string, optional) [maxLen=255]: The ID of the job you received in the response of the [Bulk Invite Users to a Portal API](https://www.zoho.com/crm/developer/docs/api/v8/portal-bulk-invite-users.html). When you do not include this parameter, the response will contain an array of all the jobs that were scheduled previously. 
If you give an incorrect job_id, you will get an empty response(HTTP 204).

**Responses:**

- **200**: Returns the status of the scheduled portal invitation job. [application/json]
    > Response for portal user invitation requests
    - `portal_invite` (array of object) [maxItems=100] **REQ** — Represents the list of portal invitation response objects. Contains one object per invitation batch.
      - `data` (array of object) [maxItems=200] **REQ** — Represents the list of individual invitation results for this job batch.
        - `details` (object) — Represents additional details about the operation result.
          - `id` (string) [maxLen=255] — Represents the unique identifier of the CRM record.
        - `code` (string) [enum=[8 values]] — Represents the error code. Possible values: **SUCCESS**, **CANNOT_PROCESS**, **INVALID_DATA**, **REQUIRED_PARAM_MISSING**, **LICENSE_LIMIT_EXCEEDED**, **NOT_REVIEWED**, **NOT_APPROVED**, **DUPLICATE_DATA**.
        - `message` (string) [maxLen=1000] — Represents the success or informational message for this operation result.
        - `status` (string) [enum=['success', 'error']] — Represents the status of the operation. Possible values: **success**, **error**.
      - `job_id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the scheduled invitation job.
      - `status` (string) **REQ** [enum=['scheduled', 'completed', 'in_progress']] — Represents the status of the operation. Possible values: **scheduled**, **completed**, **in_progress**. 

- **400**: This API is not supported in sandbox environments. Resolution: The request must be made from a production Zoho CRM organization, not a sandbox. [application/json]
    > Error response returned when the API is invoked in an unsupported environment, such as a sandbox.
    - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Represents the error code. Possible values: **API_NOT_SUPPORTED**. 
    - `details` (object) **REQ** — Represents additional details about the error.
      - `unsupported_environment` (string) **REQ** [maxLen=255] — Represents the name of the environment where this API is not supported.
    - `message` (string) **REQ** [enum=['api not supported in sandbox']] — Represents the error message. Possible values: **api not supported in sandbox**. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**. 

**Scopes:** ZohoCRM.settings.clientportal.READ

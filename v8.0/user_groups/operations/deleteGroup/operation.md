# DELETE /settings/user_groups/{group}
**Operation:** `deleteGroup` — Delete a user group
> To delete an existing user group from your Zoho CRM organization. The deletion may be immediate or scheduled for background processing, depending on group size and active references.

**Parameters:**
- `group` (path, string, required) [enum=['1234567890']]: Specify the unique ID of the user group to operate on. From API v9 onwards, UUID format is also accepted. Example: `1234567890`.

**Responses:**

- **200**: User group deletion completed. Returns a success code with the group ID if deleted immediately, or a scheduled status with a job ID if queued for processing. [application/json]
    > Response schema for a successful user group deletion or scheduled deletion.
    - `user_groups` (array of object) [maxItems=1] **REQ** — Represents the array containing the result of the user group deletion operation. 
      - `code` (string) **REQ** [enum=['SUCCESS', 'SCHEDULED']] — Represents the result code for the user group deletion operation. 
Possible values:
**SUCCESS** - The user group deletion completes immediately.
**SCHEDULED** - The user group deletion queues for background processing; the response includes a **job ID**.
      - `message` (string) **REQ** [maxLen=500] — Represents the result message for the user group deletion operation. 
      - `status` (string) **REQ** [enum=['success', 'scheduled']] — Represents the status of the user group deletion operation. 
Possible values:
**success** - The user group deletion completes immediately.
**scheduled** - The user group deletion queues for background processing.
      - `details` (object) **REQ** — Represents additional details about the deletion result, containing either the deleted group ID or a scheduled job ID. 
        oneOf:
            - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user group for which deletion completes immediately. Present in immediate-deletion responses.
            - `job_id` (string) **REQ** [maxLen=19] — Represents the ID of the scheduled deletion job. Present when the deletion is queued for background processing.

- **400**: The request failed due to an invalid or missing group ID. **Resolution:** Provide a valid numeric user group ID in the **group** path parameter. [application/json]
    > Response schema for a failed user group deletion, covering both invalid group ID and missing group ID errors.
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request failure. 
Possible values:
**INVALID_DATA** - The group ID in the URL is invalid or does not reference an existing user group.
        - `details` (object) **REQ** — Represents additional details about the request error. 
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the path segment where the invalid resource ID was found. 
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the request failure. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. 
Possible values:
**error** - The request failed because the group ID is invalid.
        - `user_groups` (array of object) [maxItems=1] **REQ** — Represents the array containing the error details for the failed deletion operation. 
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the deletion operation. 
Possible values:
**error** - The user group deletion failed.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for the deletion failure. 
Possible values:
**MANDATORY_NOT_FOUND** - The group ID is missing from the request URL.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the deletion failure. 
          - `details` (object) **REQ** — Represents additional details about the deletion error, including the name of the missing parameter. 
            - `param_name` (string) **REQ** [maxLen=100] — Represents the name of the missing request parameter. 

- **404**: The request URL does not match any configured endpoint pattern. **Resolution:** Verify the request URL follows the pattern /settings/user_groups/{group}. [application/json]
    > Response schema for an invalid URL pattern error.
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code for the URL pattern failure. 
Possible values:
**INVALID_URL_PATTERN** - The request URL does not match any configured API endpoint.
    - `details` (object) **REQ** — Represents additional details about the URL pattern error. 
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the URL pattern failure. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the request. 
Possible values:
**error** - The request URL pattern was invalid.

**Scopes:** ZohoCRM.settings.user_groups.DELETE

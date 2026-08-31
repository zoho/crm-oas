# DELETE /settings/global_picklists
**Operation:** `deleteGlobalPicklists` — Delete a Global Picklist
> Deletes a single global picklist by numeric id. This request is asynchronous: a 202 Accepted indicates deletion has been scheduled and the response includes a job_id in details. There is no status-check endpoint currently. If the provided id is not present or deletion has already been scheduled, a 400 Bad Request is returned with error details.

**Parameters:**
- `ids` (query, string/int64, required): Numeric id of the global picklist to delete. Accepts a single numeric id (e.g. 12345).

**Responses:**

- **202**: Accepted - deletion scheduled. Response contains job_id in details. No status endpoint is provided. [application/json]
    > Response object for scheduled deletion of a global picklist.
    - `global_picklists` (array of object) [maxItems=1] **REQ** — Array containing the scheduled deletion response.
      - `code` (string) **REQ** [enum=['SCHEDULED']] — Response code indicating the operation was scheduled.
      - `message` (string) **REQ** [maxLen=255] — Human-readable message about the scheduled operation.
      - `details` (object) **REQ** — Additional details about the scheduled deletion.
        - `job_id` (string) **REQ** [maxLen=100] — Background job identifier for the scheduled deletion.
      - `status` (string) **REQ** [enum=['success']] — Status of the operation.

- **400**: Bad Request - canonical error shapes for invalid id, already scheduled, conversion in progress, association limits, or system-defined restrictions. [application/json]
    > Error response object for bad request containing global picklist deletion errors.
    - `global_picklists` (array of object) [maxItems=1] — Array of global picklist deletion error details.
      - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Error code indicating the type of validation or constraint failure.
      - `details` (object) **REQ** — Additional error-specific details.
        - `id` (string) **REQ** [maxLen=100] — The id of the global picklist that caused the error.
      - `message` (string) **REQ** [maxLen=255] — Human-readable message describing the error.
      - `status` (string) **REQ** [enum=['error']] — Status of the error response.

- **403**: Forbidden [application/json]
    > Error response object containing code, message, details, and status.
    - `code` (string) **REQ** [maxLen=50] — Error code indicating the type of error.
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `details` (object) **REQ** — Additional details about the error.
      - `permissions` (array of string) [maxItems=1] — List of permissions required to access the resource.
        items: [enum=['Crm_Implied_Customize_Zoho_CRM']]
    - `status` (string) **REQ** [maxLen=100, enum=['error']] — Status of the error response.

- **500**: Internal Server Error [application/json]
    > Internal server error response object containing code, message, details, and status.
    - `code` (string) **REQ** [maxLen=50] — Error code indicating the type of error.
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `details` (object) **REQ** — Additional details about the error.
    - `status` (string) **REQ** [enum=['error']] — Status of the error response.

**Scopes:** ZohoCRM.settings.global_picklist.DELETE

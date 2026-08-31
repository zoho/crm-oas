# DELETE /settings/business_hours/shift_hours/{shift}
**Operation:** `deleteSingleShiftHour` — Delete a shift hour
> Deletes the shift hour identified by the `shift` path parameter. Once deleted, the shift hour configuration and all of its user assignments are removed.

**Parameters:**
- `shift` (path, string, required) [maxLen=50]: Represents the unique identifier of the shift hour to retrieve, update, or delete.

**Responses:**

- **200**: Returned when the shift hour is deleted successfully. — Schema: `ShiftHoursSuccessResponse` [application/json]
    > Response body details
    schema: `ShiftHoursSuccessResponse`
    - `shift_hours` (array of object) [maxItems=50] **REQ** — Lists the shift hour configurations in the request or response. 
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the response code of the operation.
      - `message` (string) **REQ** [maxLen=100] — Represents the message that describes the outcome of the operation.
      - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
        - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the shift hour affected by the operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation.

- **400**: Returned when the request fails validation. The response identifies the failing field and the reason. [application/json]
    > Represents the request or response body for the operation.
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
    - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
      - `resource_path_index` (integer/int32) — Represents the zero-based index of the path parameter that caused the error.
    - `message` (string) **REQ** [enum=['Invalid ID']] — Represents the message that describes the outcome of the operation.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.

- **403**: Returned when the requesting user does not hold the CRM profile permission required to manage shift hours. [application/json]
    > Represents the forbidden response returned when the requesting user does not hold the CRM profile permission required to manage shift hours.
    - `code` (string) [enum=['NO_PERMISSION']] — Represents the response code that identifies the outcome of the operation.
    - `details` (object) — Represents additional details about the outcome of the operation.
      - `permissions` (array of string) [maxItems=50] — Lists the CRM profile permissions that the user must hold to access this API.
        items: [enum=['Crm_Implied_Manage_Users']]
    - `message` (string) [maxLen=100] — Represents the message that describes the outcome of the operation.
    - `status` (string) [enum=['error']] — Represents the status of the operation.

**Scopes:** ZohoCRM.settings.business_hours.DELETE

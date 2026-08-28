# PUT /settings/business_hours
**Operation:** `updateBusinessHours` — Business Hours Configuration
> Updates the existing business hours configuration with revised working days, operating hours, or timezone settings.

**Schemas:**
`ErrorResponse`:
  > Standard error response structure for business hours API operations.
  - `code` (string) **REQ** [enum=[10 values]] — Error code
  - `details` (object) **REQ** — Additional contextual information about the error
  - `message` (string) **REQ** [maxLen=255] — Error message
  - `status` (string) **REQ** [enum=['error']] — Error status

**Request Body** (required) — application/json
  > Business hours update request body
  - `business_hours` (object) **REQ** — The business hours configuration object containing all settings for the organization's working schedule.
    - `week_starts_on` (string) [enum=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']] — The day on which the organization's work week begins.
    - `type` (string) [enum=['24_by_7', '24_by_5', 'custom']] — The type of business hours configuration: '24_by_7' for 24/7 operation, '24_by_5' for 24-hour weekday operation, or 'custom' for a customized schedule.
    - `business_days` (array of string) [minItems=1, maxItems=7, uniqueItems] — The specific days of the week on which the organization is open for business.
      items: [enum=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]
    - `same_as_everyday` (boolean) — If true, the same operating hours apply to all business days. If false, hours vary by day and are defined in custom_timing.
    - `daily_timing` (array of string) [minItems=2, maxItems=2] — Default working hours applied to all business days (start and end time)
      items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
    - `custom_timing` (array of object) [maxItems=7] — Different business hours for different days when same_as_everyday is false
      - `days` (string) **REQ** [enum=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']] — Specific day of the week for custom business hours
      - `business_timing` (array of string) [minItems=2, maxItems=2] **REQ** — Start and end time for business hours on this specific day
        items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
      - `_delete` (boolean) — Set to true to delete the custom timing for this specific business day

**Responses:**

- **200**: Business hours operation completed successfully. [application/json]
    > Standard success response for business hours operations
    - `business_hours` (object) — Business hours response object
      - `status` (string) **REQ** [enum=['success']] — Status of the operation
      - `code` (string) **REQ** [enum=['SUCCESS']] — Code representing the operation status
      - `message` (string) **REQ** [enum=['Business Hours saved successfully']] — Message representing the operation status
      - `details` (object) **REQ** — Details of the created business hours
        - `id` (string) **REQ** [maxLen=255] — Unique identifier of the created business hours

- **400**: The request could not be processed due to invalid data, missing required fields, or business rule violations. — Schema: `BusinessHoursErrorResponses` [application/json]
    oneOf:
        - `business_hours` (object `ErrorResponse`) **REQ** — Standard error response structure for business hours API operations.
      - `ErrorResponse` — Standard error response structure for business hours API operations.

- **403**: Access denied. The authenticated user does not have the required permissions to manage business hours settings. [application/json]
    > Forbidden response schema
    - `code` (string) [enum=['NO_PERMISSION']] — Error code
    - `details` (object) — Additional contextual information about the error,
      - `permissions` (array of string) [maxItems=5] — List of missing permissions
        items: [enum=['Crm_Implied_Manage_Users']]
    - `message` (string) [maxLen=255] — Error message
    - `status` (string) [enum=['error']] — Error status

**Scopes:** ZohoCRM.settings.business_hours.UPDATE

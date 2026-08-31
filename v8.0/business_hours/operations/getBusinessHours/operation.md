# GET /settings/business_hours
**Operation:** `getBusinessHours` — Business Hours Configuration
> Retrieves the current business hours configuration, including working days, operating hours, and timezone details.

**Responses:**

- **200**: Successfully retrieved business hours configuration [application/json]
    > Business hours retrieval response
    - `business_hours` (object) **REQ** — The business hours configuration object containing all settings for the organization's working schedule.
      - `week_starts_on` (string) **REQ** [enum=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']] — The day on which the organization's work week begins.
      - `type` (string) **REQ** [enum=['24_by_7', '24_by_5', 'custom']] — The type of business hours configuration: '24_by_7' for 24/7 operation, '24_by_5' for 24-hour weekday operation, or 'custom' for a customized schedule.
      - `id` (string) **REQ** [maxLen=255, pattern=^[0-9]+$] — The unique identifier assigned to this business hours configuration.
      - `timezone` (string) **REQ** [maxLen=100] — Timezone for business hours (IANA timezone identifier)
      - `business_days` (array of string) [minItems=1, maxItems=7, uniqueItems] **REQ** — The specific days of the week on which the organization is open for business.
        items: [enum=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]
      - `same_as_everyday` (boolean) **REQ** — If true, the same operating hours apply to all business days. If false, hours vary by day and are defined in custom_timing.
      - `daily_timing` (array of string) [minItems=2, maxItems=2, nullable] **REQ** — Default working hours applied to all business days (start and end time)
        items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
      - `custom_timing` (array of object) [maxItems=7, nullable] **REQ** — Different business hours for different days when same_as_everyday is false
        - `days` (string) **REQ** [enum=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']] — Specific day of the week for custom business hours
        - `business_timing` (array of string) [minItems=2, maxItems=2] **REQ** — Start and end time for business hours on this specific day
          items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]

- **204**: No business hours configuration exists for this organization.

**Scopes:** ZohoCRM.settings.business_hours.READ

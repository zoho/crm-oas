# GET /settings/holidays
**Operation:** `getHolidays` — Holidays
> To retrieve the list of holidays configured in Zoho CRM. Business holidays apply to all users, while shift holidays are specific to configured shift schedules. Returns paginated results.

**Tags:** Holidays

**Parameters:**
- `year` (query, integer/int32, optional) [min=2000, max=2100]: Specify the year for which to filter holidays.
- `type` (query, string, optional) [enum=['business_holiday', 'shift_holiday']]: Specify the type of holidays to retrieve.
Possible values: business_holiday, shift_holiday.
- `shift_id` (query, string, optional) [maxLen=30, minLen=1, pattern=^[0-9]+$]: Specify the unique identifier of the shift hour whose holidays to retrieve. Required when the type parameter is set to shift_holiday.
- `page` (query, integer/int32, optional) [min=1]: Specify the page number for paginated results. Defaults to 1.

**Responses:**

- **200**: Returns a paginated list of holidays matching the specified filter criteria. [application/json]
    > Represents the response body containing the list of holidays and pagination metadata.
    - `holidays` (array of object) [maxItems=100] **REQ** — Contains the list of holidays matching the specified filter criteria. 
      - `name` (string) **REQ** [maxLen=80, minLen=1, pattern=^[^#%^&*]+$] — Represents the name of the holiday. 
      - `date` (string/date) **REQ** — Represents the date of the holiday in **YYYY-MM-DD** format. 
      - `type` (string) **REQ** [enum=['business_holiday', 'shift_holiday']] — The type of holiday that you want to fetch. The possible values are **business_holiday** and **shift_holiday**.
      - `shift_hour` (object) **REQ** — Represents the shift hour associated with this holiday. Contains null for business holidays. 
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the shift hour. Always present when the shift_hour object is included in the response.
        - `id` (string) **REQ** [maxLen=255, pattern=^[0-9]+$] — Represents the unique identifier of the shift hour. Always present when the shift_hour object is included in the response.
      - `id` (string) **REQ** [maxLen=255, pattern=^[0-9]+$] — Represents the unique identifier of the holiday record. 
      - `year` (integer/int32) **REQ** [min=2000, max=2100] — Represents the year in which the holiday falls. 
    - `info` (object) — Contains pagination metadata for the response.
      - `per_page` (integer/int32) [min=1] — Represents the number of holiday records returned per page.
      - `page` (integer/int32) [min=1] — Represents the current page number in the paginated results. Page numbers begin at one.
      - `count` (integer/int32) [min=0] — Represents the total number of holiday records returned in this page of results.
      - `more_records` (boolean) — Indicates whether more holiday records are available on subsequent pages.

- **204**: No holidays were found matching the specified filter criteria.

- **400**: One or more query parameter values do not match the expected format. **Resolution** The request must include valid values for all query parameters. [application/json]
    > Represents the error response body returned when a query parameter value fails validation.
    - `code` (string) [enum=['PATTERN_NOT_MATCHED']] — Indicates the validation error type. Possible values: **PATTERN_NOT_MATCHED**.
    - `details` (object) — Contains additional details about the validation error, such as the affected parameter name.
    - `message` (string) [maxLen=255] — Describes the specific validation error that occurred.
    - `status` (string) [enum=['error']] — Indicates the response status. Possible values: **error**.

**Scopes:** ZohoCRM.settings.business_hours.READ

# GET /settings/holidays/{holidayId}
**Operation:** `getHoliday` — A specific holiday
> To retrieve the complete details of a specific holiday record from Zoho CRM using its unique identifier.

**Tags:** Holidays

**Parameters:**
- `holidayId` (path, string, required) [maxLen=30, minLen=1, pattern=^[0-9]+$]: Specify the unique identifier of the holiday.
- `year` (query, integer/int32, optional) [min=2000, max=2100]: Specify the year for which to filter holidays.
- `type` (query, string, optional) [enum=['business_holiday', 'shift_holiday']]: Specify the type of holidays to retrieve.
Possible values: business_holiday, shift_holiday.
- `shift_id` (query, string, optional) [maxLen=30, minLen=1, pattern=^[0-9]+$]: Specify the unique identifier of the shift hour whose holidays to retrieve. Required when the type parameter is set to shift_holiday.

**Responses:**

- **200**: Returns the details of the requested holiday record. [application/json]
    > Represents the response body containing the details of the requested holiday record.
    - `holidays` (array of object) [maxItems=100] **REQ** — Contains the holiday record matching the specified identifier. 
      - `name` (string) **REQ** [maxLen=80] — Represents the name of the holiday. 
      - `date` (string/date) **REQ** — Represents the date of the holiday in **YYYY-MM-DD** format. 
      - `type` (string) **REQ** [enum=['business_holiday', 'shift_holiday']] — Indicates the type of holiday. Possible values: **business_holiday, shift_holiday**. 
      - `shift_hour` (object) **REQ** — Represents the shift hour associated with this holiday. Contains null for business holidays. 
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the shift hour. Always present when the shift_hour object is included in the response.
        - `id` (string) **REQ** [maxLen=255] — Specifies the unique identifier of the shift hour. Always present when the shift_hour object is included in the response.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the holiday record. 
      - `year` (integer/int32) **REQ** — Specifies the year in which the holiday falls. 
    - `info` (object) — Contains pagination metadata for the response.
      - `per_page` (integer/int32) — Represents the number of holiday records returned per page.
      - `page` (integer/int32) — Indicates the current page number in the paginated results. Page numbers begin at one.
      - `count` (integer/int32) — Represents the total number of holiday records returned in this page of results.
      - `more_records` (boolean) — Indicates whether more holiday records are available on subsequent pages.

- **204**: No holiday was found for the specified identifier.

**Scopes:** ZohoCRM.settings.business_hours.READ

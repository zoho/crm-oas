# DELETE /settings/holidays/{holidayId}
**Operation:** `deleteHoliday` — Holiday
> To permanently delete a holiday from Zoho CRM using its unique identifier. The deletion cannot be undone.

**Tags:** Holidays

**Parameters:**
- `holidayId` (path, string, required) [maxLen=30, minLen=1, pattern=^[0-9]+$]: Specify the unique identifier of the holiday.
- `year` (query, integer/int32, optional) [min=2000, max=2100]: Specify the year for which to filter holidays.

**Responses:**

- **200**: Returns the result of the delete operation. — Schema: `HolidaysSuccessResponse` [application/json]
    > Represents the success response body the API returns after creating holidays.
    schema: `HolidaysSuccessResponse`
    - `holidays` (array of object) [maxItems=100] **REQ** — Contains the result for each holiday included in the create request. 
      - `code` (string) **REQ** [enum=['SUCCESS']] — Indicates the result code for the holiday operation. Possible values: SUCCESS. 
      - `details` (object) **REQ** — Contains the details of the processed holiday, including its unique identifier. 
        - `id` (string) [maxLen=255] — Represents the unique identifier of the created holiday.
      - `message` (string) **REQ** [maxLen=255] — Describes the result of the holiday creation operation. 
      - `status` (string) **REQ** [enum=['success']] — Indicates the status of the holiday creation operation. Possible values: success. 

- **400**: Invalid holiday ID. **Resolution** The holiday ID in the request path must be a valid identifier of an existing holiday record. [application/json]
    > Represents the error response body returned when the holiday ID fails validation.
    - `code` (string) [enum=['INVALID_DATA']] — Indicates the validation error type. Possible values: **INVALID_DATA**.
    - `details` (object) — Contains additional details about the validation error, including the path index of the invalid resource identifier.
    - `message` (string) [maxLen=255] — Describes the specific validation error that occurred.
    - `status` (string) [enum=['error']] — Indicates the response status. Possible values: **error**.

**Scopes:** ZohoCRM.settings.business_hours.DELETE

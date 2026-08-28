# PUT /settings/holidays/{holidayId}
**Operation:** `updateHoliday` — A specific holiday
> To update the name or date of a specific holiday record in Zoho CRM using its unique identifier.

**Tags:** Holidays

**Parameters:**
- `holidayId` (path, string, required) [maxLen=30, minLen=1, pattern=^[0-9]+$]: Specify the unique identifier of the holiday.

**Schemas:**
`InvalidDataResponse`:
  > Represents the error response body returned when a holiday request fails due to validation errors.
  - `code` (string) [enum=['DUPLICATE_DATA', 'INVALID_DATA', 'DEPENDENT_FIELD_MISSING']] — Indicates the validation error type. Possible values: DUPLICATE_DATA, INVALID_DATA, DEPENDENT_FIELD_MISSING.
  - `details` (object) — Contains additional information about the validation error.
  - `message` (string) [maxLen=255] — Describes the specific validation error that occurred.
  - `status` (string) [enum=['error']] — Indicates the response status. Possible values: error.

**Request Body** (required) — application/json
> The request body must contain a holidays array with one object.
  > Represents the request body schema for updating a single holiday.
  - `holidays` (array of object) [minItems=1, maxItems=1] — Specify the updated details for the holiday.
    - `name` (string) [maxLen=80, minLen=1, pattern=^[^#%^&*]+$, nullable] — Specify the new name for the holiday.
    - `date` (string/date) [nullable] — Specify the new date for the holiday in **YYYY-MM-DD** format.

**Responses:**

- **200**: Returns the result of the holiday update operation. [application/json]
    > Represents the response body the API returns after updating the holiday.
    - `holidays` (array of object) [maxItems=100] **REQ** — Contains the result for the updated holiday. 
      - `code` (string) **REQ** [enum=['SUCCESS']] — Indicates the result code for the holiday update. Possible values: **SUCCESS**. 
      - `details` (object) **REQ** — Contains the details of the updated holiday, including its unique identifier. 
        - `id` (string) [maxLen=255] — Represents the unique identifier of the updated holiday.
      - `message` (string) **REQ** [maxLen=255] — Describes the result of the holiday update operation. 
      - `status` (string) **REQ** [enum=['success']] — Indicates the status of the holiday update. Possible values: success. 

- **400**: One or more holiday fields in the request failed validation. **Resolution** All field values must conform to the expected format and constraints. [application/json]
    > Represents the error response body returned when the holiday update fails validation.
    oneOf:
        - `holidays` (array of object `InvalidDataResponse`) [maxItems=100] **REQ** — Contains the validation errors for holidays in the request. 
      - `InvalidDataResponse` — Represents the error response body returned when a holiday request fails due to validation errors.

**Scopes:** ZohoCRM.settings.business_hours.UPDATE

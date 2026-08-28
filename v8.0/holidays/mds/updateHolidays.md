# PUT /settings/holidays
**Operation:** `updateHolidays` — Multiple Holidays
> To update one or more existing holiday records in Zoho CRM by providing each holiday ID with the updated field values.

**Tags:** Holidays

**Request Body** (required) — application/json
> The request body must contain a holidays array. You can include a maximum of **100** objects per request.
  oneOf:
      - `holidays` (array of object) [minItems=1, maxItems=100] **REQ** — Specify the list of holidays to update. Each entry must include the holiday **ID**.
        - `name` (string) [maxLen=80, minLen=1, pattern=^[^#%^&*]+$] — Specify the updated name for the holiday.
        - `date` (string/date) — Specify the updated date for the holiday in **YYYY-MM-DD** format.
        - `type` (string) [enum=['business_holiday', 'shift_holiday']] — Specify the updated type of holiday. Possible values: **business_holiday, shift_holiday**.
        - `shift_hour` (object) — Specify the updated shift hour associated with this holiday. Required when the type field is set to shift_holiday.
          - `name` (string) **REQ** [maxLen=255] — Specify the name of the shift hour.
          - `id` (string) **REQ** [maxLen=255, pattern=^[0-9]+$] — Specify the unique identifier of the shift hour. Use the [Get Shift Hours API](shift_hours.yaml#$.paths./settings/business_hours/shift_hours.get) to get the ID of the shift hour.
        - `id` (string) **REQ** [maxLen=255, pattern=^[0-9]+$] — Specify the unique identifier of the holiday to update.
      - `info` (object) — Contains optional pagination context included in the request schema.
        - `per_page` (integer/int32) — Specify the number of records to include per page.
        - `page` (integer/int32) — Specify the page number to retrieve.
        - `count` (integer/int32) — Specify the total count of records.
        - `more_records` (boolean) — Specify whether more records are available on subsequent pages.

**Responses:**

- **200**: Returns the result of the bulk holiday update operation. [application/json]
    > Represents the response body the API returns after updating one or more holidays.
    - `holidays` (array of object) [maxItems=100] **REQ** — Contains the operation result for each holiday submitted in the update request. 
      - `code` (string) [maxLen=255] — Indicates the validation error type. Possible values: DUPLICATE_DATA, DEPENDENT_FIELD_MISSING, INVALID_DATA.
      - `details` (object) — Contains additional details about the update operation result.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the updated holiday.
      - `message` (string) [maxLen=255] — Describes the result of the update operation for this holiday.
      - `status` (string) [maxLen=255] — Indicates the status of the update operation for this holiday.

- **207**: Returned when a batch request partially succeeds — some items succeed and some fail. Each item in the holidays array carries its own code, status, message, and details. — Schema: `HolidaysSuccessResponse` [application/json]
    > Represents the success response body the API returns after creating holidays.
    schema: `HolidaysSuccessResponse`
    - `holidays` (array of object) [maxItems=100] **REQ** — Contains the result for each holiday included in the create request. 
      - `code` (string) **REQ** [enum=['SUCCESS']] — Indicates the result code for the holiday operation. Possible values: SUCCESS. 
      - `details` (object) **REQ** — Contains the details of the processed holiday, including its unique identifier. 
        - `id` (string) [maxLen=255] — Represents the unique identifier of the created holiday.
      - `message` (string) **REQ** [maxLen=255] — Describes the result of the holiday creation operation. 
      - `status` (string) **REQ** [enum=['success']] — Indicates the status of the holiday creation operation. Possible values: success. 

- **400**: One or more holidays in the request failed validation. **Resolution** Each holiday must include a valid ID, and all updated field values must conform to the expected format and constraints. [application/json]
    > Represents the error response body when one or more holidays fail validation during the bulk update.
    - `holidays` (array of object) [maxItems=100] — Contains the validation error result for each holiday in the request.
      - `code` (string) [enum=['DUPLICATE_DATA', 'DEPENDENT_FIELD_MISSING', 'INVALID_DATA']] — Indicates the validation error type. Possible values: DUPLICATE_DATA, DEPENDENT_FIELD_MISSING, INVALID_DATA.
      - `details` (object) — Contains additional details about the validation error, such as the affected field name and JSON path.
      - `message` (string) [maxLen=255] — Describes the specific validation error for this holiday.
      - `status` (string) [enum=['error']] — Indicates the response status for this holiday. Possible values: error.

- **403**: The user does not have sufficient permission to perform the requested operation. **Resolution** The CRM administrator must grant the required permission to the user's profile. [application/json]
    > Represents the error response body returned when the user lacks permission to perform the requested operation.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Indicates the error code for the permission violation. Possible values: NO_PERMISSION. 
    - `details` (object) — Contains additional information about the permission error.
    - `message` (string) **REQ** [maxLen=255] — Describes the specific permission requirement that was not met. 
    - `status` (string) **REQ** [enum=['error']] — Indicates the response status. Possible values: error. 

**Scopes:** ZohoCRM.settings.business_hours.UPDATE

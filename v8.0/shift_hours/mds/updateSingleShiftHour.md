# PUT /settings/business_hours/shift_hours/{shift}
**Operation:** `updateSingleShiftHour` — Update a shift hour
> Updates the configuration of the shift hour identified by the `shift` path parameter. The request body specifies the fields to change, such as the time zone, active days, timing, break windows, holidays, or user assignments. The updated timing must fall within the configured business hours.

**Parameters:**
- `shift` (path, string, required) [maxLen=50]: Represents the unique identifier of the shift hour to retrieve, update, or delete.

**Schemas:**
`ShiftHoursSuccessResponse`:
  > Response body details
  - `shift_hours` (array of object) [maxItems=50] **REQ** — Lists the shift hour configurations in the request or response. 
    - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the response code of the operation.
    - `message` (string) **REQ** [maxLen=100] — Represents the message that describes the outcome of the operation.
    - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
      - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the shift hour affected by the operation.
    - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation.

**Request Body** (required) — application/json
> Represents the request body for updating one or more shift hour configurations. 
  > Represents the request body for updating one or more shift hour configurations. Each entry in `shift_hours` updates an existing shift with its timing, break hours, optional holidays, and assigned users.
  - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations to be created or updated in the request. 
    - `break_hours` (array of object) [maxItems=50] — Lists the break windows scheduled within the shift hour. A shift can have at most two break windows.
      - `break_days` (array of string) [maxItems=7] — Lists the days of the week on which the break hour applies.
        items: [enum=['Monday', 'Thursday', 'Friday', 'Sunday', 'Wednesday', 'Tuesday', 'Saturday']]
      - `daily_timing` (array of string) [maxItems=50] — Represents the start and end time of the break
in `HH:MM` 24-hour format, applied uniformly to
every day the break is scheduled. 


This field is **mandatory** when the parent
**same_as_everyday** is **true**. A day can have
at most two breaks and the total break time on a
day cannot exceed two hours.

        items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
      - `custom_timing` (array of object) [maxItems=50] — Lists per-day break timing overrides. This field is **mandatory** when the parent **same_as_everyday** is **false**. A day can have at most two breaks and the total break time on a day cannot exceed two hours.
        - `break_timing` (array of string) [maxItems=7] — Represents the start and end time of the break on the specified day
in `HH:MM` 24-hour format. A break must be
longer than 15 minutes and shorter than 2
hours.

          items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
        - `days` (string) [enum=['Monday', 'Thursday', 'Friday', 'Sunday', 'Wednesday', 'Tuesday', 'Saturday']] — Represents the day of the week to which
this custom break timing applies.


**Possible values**: 

- Monday

- Tuesday

- Wednesday

- Thursday

- Friday

- Saturday

- Sunday

      - `same_as_everyday` (string) [maxLen=100] — Indicates whether the shift hour follows the same timing on every active day. When the value is **true**, the **daily_timing** array becomes mandatory; when the value is **false**, the **custom_timing** array becomes mandatory.
    - `daily_timing` (array of string) [maxItems=50] — Represents the start and end time of the shift in `HH:MM` 24-hour
format, applied uniformly to every active day. This
field is **mandatory** when **same_as_everyday** is
**true**.

      items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
    - `shift_days` (array of string) [maxItems=7] — Lists the days of the week on which the shift hour is
active. You can set shift timing only on the days your
organization operates.


**Possible values**: 

- Monday

- Tuesday

- Wednesday

- Thursday

- Friday

- Saturday

- Sunday

      items: [enum=['Monday', 'Thursday', 'Friday', 'Sunday', 'Wednesday', 'Tuesday', 'Saturday']]
    - `custom_timing` (array of object) [maxItems=50] — Lists per-day shift timing overrides. This field is **mandatory** when **same_as_everyday** is **false**.
      - `shift_timing` (array of string) [maxItems=7] — Represents the start and end time of the shift on the specified
day in `HH:MM` 24-hour format. 

        items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
      - `days` (string) [enum=['Monday', 'Thursday', 'Friday', 'Sunday', 'Wednesday', 'Tuesday', 'Saturday']] — Represents the day of the week to which this
custom shift timing applies.


**Possible values**: 

- Monday

- Tuesday

- Wednesday

- Thursday

- Friday

- Saturday

- Sunday

    - `timezone` (string) [maxLen=100] — Represents the time zone in which the shift hours are scheduled. 
    - `name` (string) [maxLen=80] — Represents the name of the shift hour. The name must be unique within the organization and must not contain the special characters.
    - `same_as_everyday` (boolean) — Indicates whether the shift hour follows the same
timing on every active day. 


**Possible values**:

- **true** - the shift hour uses the same timing every
day, and **daily_timing** becomes mandatory.

- **false** - the shift hour uses different timing for
different days, and **custom_timing** becomes
mandatory.

    - `holidays` (array of object) [maxItems=50] — Lists the holidays observed during the shift hour. The holiday date must fall between the current and the next financial year.
      - `date` (string/date) — Represents the date of the holiday in `YYYY-MM-DD` format.
      - `name` (string) [maxLen=80] — Represents the name of the holiday. The name must not contain the special characters.
    - `users` (array of object) [maxItems=200] — Lists the users assigned to the shift hour. 
      - `id` (string) [maxLen=100] — Represents the unique identifier of the user assigned to the shift hour.

**Responses:**

- **200**: Returned when the shift hour update completes successfully. — Schema: `ShiftHoursSuccessResponse` [application/json]
    > Response body details

- **207**: Returned when a batch request partially succeeds where some items succeed and some fail. Each item in the shift_hours array carries its own code, status, message, and details. — Schema: `ShiftHoursSuccessResponse` [application/json]
    > Represents the response body that contains the shift hour configurations and the aggregate count of shifts with assigned users.

- **400**: Returned when the request fails validation. The response identifies the failing field and the reason. [application/json]
    > Represents the error response body for the operation.
    oneOf:
        - `shift_hours` (array of object) [maxItems=100] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=[6 values]] — Represents the response code that identifies the outcome of the operation.
          - `message` (string) **REQ** [maxLen=255] — Represents the message that describes the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=100] — Represents the JSON path of the field that caused the error.
            additionalProperties: any
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
        - `message` (string) **REQ** [maxLen=255] — Represents the message that describes the outcome of the operation.
        - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
          - `resource_path_index` (integer/int32) **REQ** — Represents the zero-based index of the path parameter that caused the error.
          additionalProperties: any
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.

- **403**: Returned when the requesting user does not hold the CRM profile permission required to manage shift hours. [application/json]
    > Represents the forbidden response returned when the requesting user does not hold the CRM profile permission required to manage shift hours.
    - `code` (string) [enum=['NO_PERMISSION']] — Represents the response code that identifies the outcome of the operation.
    - `details` (object) — Represents additional details about the outcome of the operation.
      - `permissions` (array of string) [maxItems=50] — Lists the CRM profile permissions that the user must hold to access this API.
        items: [enum=['Crm_Implied_Manage_Users']]
    - `message` (string) [maxLen=100] — Represents the message that describes the outcome of the operation.
    - `status` (string) [enum=['error']] — Represents the status of the operation.

**Scopes:** ZohoCRM.settings.business_hours.UPDATE

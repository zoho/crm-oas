# POST /settings/business_hours/shift_hours
**Operation:** `createShifts` — Add shift hours
> Creates one or more shift hour configurations for the organization. Each shift hour specifies the name, time zone, active days, timing, optional break windows, optional holidays, and optional user assignments. The shift hour timing must fall within the configured business hours, and the request is rejected if business hours are not enabled for the org.

**Schemas:**
`ShiftHoursSuccessResponse`:
  > Represents the response body that contains the shift hour configurations and the aggregate count of shifts with assigned users.
  - `shift_hours` (array of object) [maxItems=50] **REQ** — Lists the shift hour configurations in the request or response. 
    - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the response code of the operation.
    - `message` (string) **REQ** [maxLen=100] — Represents the message that describes the outcome of the operation.
    - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
      - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the shift hour affected by the operation.
    - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation.

**Request Body** (required) — application/json
> The request body contains the data required to perform the operation. 
  > Represents the request body for creating one or more shift hour configurations. Each entry in `shift_hours` defines a shift with its timing, break hours, optional holidays, and assigned users.
  - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations to be created or updated in the request. Each entry specifies a shift hour with its timing, break hours, holidays, and assigned users.
    - `break_hours` (array of object) [maxItems=50] — Lists the break windows scheduled within the shift hour. Each entry specifies the days the break applies to and the break timing for those days. A shift can have at most two break windows.
      - `break_days` (array of string) [maxItems=7] — Lists the days of the week on which the break applies.
        items: [enum=['Monday', 'Thursday', 'Friday', 'Sunday', 'Wednesday', 'Tuesday', 'Saturday']]
      - `daily_timing` (array of string) [maxItems=50] — Represents the start and end time of the break
in `HH:MM` 24-hour format, applied uniformly to
every day the break is scheduled. This field is
**mandatory** when the parent
**same_as_everyday** is **true**. 


> **Note**

> A day can have at most two breaks and the
total break time on a day cannot exceed two
hours.

        items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
      - `custom_timing` (array of object) [maxItems=50] — Lists per-day break timing overrides. Each entry specifies the day of the week and the start and end time of the break on that day. This field is **mandatory** when the parent **same_as_everyday** is **false**. 
        - `break_timing` (array of string) [maxItems=7] **REQ** — Represents the start and end time of the break on the specified day
in `HH:MM` 24-hour format. A break must be
longer than 15 minutes and shorter than 2
hours.

          items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
        - `days` (string) **REQ** [enum=['Monday', 'Thursday', 'Friday', 'Sunday', 'Wednesday', 'Tuesday', 'Saturday']] — Represents the day of the week to which
this custom break timing applies.


**Possible values**: 

- Monday

- Tuesday

- Wednesday

- Thursday

- Friday

- Saturday

- Sunday

      - `same_as_everyday` (string) **REQ** [maxLen=100] — Indicates whether the shift hour follows the same timing on every active day. When the value is **true**, the **daily_timing** array becomes mandatory; when the value is **false**, the **custom_timing** array becomes mandatory.
    - `daily_timing` (array of string) [maxItems=50] — Represents the start and end time of the shift in `HH:MM` 24-hour
format, applied uniformly to every active day. This
field is **mandatory** when **same_as_everyday** is
**true**.

      items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
    - `shift_days` (array of string) [maxItems=7] — Lists the days of the week on which the shift hour is active. You can set shift timing only on the days your organization operates.
      items: [enum=['Monday', 'Thursday', 'Friday', 'Sunday', 'Wednesday', 'Tuesday', 'Saturday']]
    - `custom_timing` (array of object) [maxItems=50] — Lists per-day shift timing overrides. Each entry specifies the day of the week and the start and end time of the shift on that day. This field is mandatory when **same_as_everyday** is **false**.
      - `shift_timing` (array of string) [maxItems=7] **REQ** — Represents the start and end time of the shift on the specified
day in `HH:MM` in the 24-hour format. 

        items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
      - `days` (string) **REQ** [enum=['Monday', 'Thursday', 'Friday', 'Sunday', 'Wednesday', 'Tuesday', 'Saturday']] — Represents the day of the week to which this
custom shift timing applies.


Possible values: 

- Monday

- Tuesday

- Wednesday

- Thursday

- Friday

- Saturday

- Sunday

    - `timezone` (string) **REQ** [maxLen=100] — Represents the time zone in which the shift hours are scheduled. Use a valid IANA time zone identifier such as `Asia/Kolkata` or `America/New_York`.
    - `name` (string) **REQ** [maxLen=80] — Represents the name of the shift hour. The name must be unique within the organization and must not contain the special characters.
    - `same_as_everyday` (boolean) **REQ** — Indicates whether the shift hour follows the same
timing on every active day. 


**Possible values**:

-  `true` - the shift hour uses the same timing every
day, and `daily_timing` becomes mandatory.

- `false` - the shift hour uses different timing for
different days, and `custom_timing` becomes mandatory.

    - `holidays` (array of object) [maxItems=50] — Lists the holidays observed during the shift hour. Each entry specifies the date and the name of the holiday. The holiday date must fall between the current and the next financial year.
      - `date` (string/date) **REQ** — Represents the date of the holiday in `YYYY-MM-DD` format.
      - `name` (string) **REQ** [maxLen=80] — Represents the name of the holiday. The name must not contain the special characters.
    - `users` (array of object) [maxItems=200] — Lists the users assigned to the shift hour. Each entry specifies the user and the date from which the assignment becomes effective.
      - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the user assigned to the shift hour.

**Responses:**

- **201**: Returned when the shift hour create, update, or delete operation completes successfully. — Schema: `ShiftHoursSuccessResponse` [application/json]
    > Represents the response body that contains the shift hour configurations and the aggregate count of shifts with assigned users.

- **207**: Returned when a batch request partially succeeds where some items succeed and some fail. Each item in the shift_hours array carries its own code, status, message, and details. — Schema: `ShiftHoursSuccessResponse` [application/json]
    > Represents the response body that contains the shift hour configurations and the aggregate count of shifts with assigned users.

- **400**: Returned when the request fails validation. The response identifies the failing field and the reason. [application/json]
    > Represents the request or response body for the operation.
    oneOf:
        - `shift_hours` (array of object) [maxItems=1] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `limit` (integer/int32) **REQ** [enum=[50]] — Represents the maximum number of shift hours
that can be configured.

Possible values: **50**.

            - `limit_due_to` (array of object) [maxItems=50] **REQ** — Lists the fields that caused the limit to be exceeded.
              - `api_name` (string) **REQ** [enum=['shift_hours']] — Represents the API name of the field that caused the error.
              - `json_path` (string) **REQ** [enum=['$.shift_hours']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['Shift hours Limit exceeds']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=1] — Lists the shift hour configurations returned in the response. Each entry represents one shift hour with its timing, break hours, holidays, and assigned users.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
          - `message` (string) **REQ** [enum=['Business hours is not enabled']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['name']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].name']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['Shift Name already exists']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['timezone']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].timezone']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['required field not found']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['name']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].name']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['required field not found']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['same_as_everyday']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=[2 values]] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['required field not found']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `dependee` (object) **REQ** — Represents the field that the failing field depends on.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
              - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path of the field that caused the error.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['Daily timing required for "Same hours everyday" mode']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `dependee` (object) **REQ** — Represents the field that the failing field depends on.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
              - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path of the field that caused the error.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['required field not found']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['shift_days']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].shift_days']] — Represents the JSON path of the field that caused the error.
            - `maximum_length` (integer/int32) [enum=[7]] — Represents the maximum length permitted for the field that caused the error.
          - `message` (string) **REQ** [enum=['invalid data']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['ALREADY_USED']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['shift_days', 'days', 'break_days']] — Represents the API name of the field that
caused the error.


**Possible values**: 

- shift_days

- days

- break_days

            - `json_path` (string) **REQ** [enum=[4 values]] — Represents the JSON path of the field that caused the error.
            - `exists_in` (object) — Represents the existing entry that the duplicate value conflicts with.
              - `api_name` (string) [enum=['shift_days', 'days', 'break_days']] — Represents the API name of the field
that caused the error.


**Possible values**: 

- shift_days

- days

- break_days

              - `json_path` (string) [enum=[4 values]] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['Please avoid duplicate days']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `dependee` (object) **REQ** — Represents the field that the failing field depends on.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
              - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path of the field that caused the error.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['Custom timing required for "Different hours everyday" mode']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['shift_timing', 'break_timing']] — Represents the API name of the field that
caused the error.


**Possible values**: 

- shift_timing

- break_timing

            - `json_path` (string) **REQ** [enum=[2 values]] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['required field not found']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['days']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=[2 values]] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['required field not found']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['custom_timing', 'shift_timing', 'break_timing']] — Represents the API name of the field that
caused the error.


**Possible values**: 

- custom_timing

- shift_timing

- break_timing

            - `json_path` (string) **REQ** [enum=[6 values]] — Represents the JSON path of the field that caused the error.
            - `minimum_length` (integer/int32) [enum=[2]] — Represents the minimum length required for the field that caused the error.
            - `maximum_length` (integer/int32) [enum=[2, 7]] — Represents the maximum length permitted for the field that caused the error.
          - `message` (string) **REQ** [enum=[5 values]] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['daily_timing']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=[5 values]] — Represents the JSON path of the field that caused the error.
            - `minimum_length` (integer/int32) [enum=[2]] — Represents the minimum length required for the field that caused the error.
            - `maximum_length` (integer/int32) [enum=[2]] — Represents the maximum length permitted for the field that caused the error.
          - `message` (string) **REQ** [enum=[3 values]] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['break_hours']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].break_hours[1]']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['Break Hours timing is over lapped']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `maximum_length` (integer/int32) **REQ** [enum=[2]] — Represents the maximum length permitted for the field that caused the error.
            - `api_name` (string) **REQ** [enum=['break_hours']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].break_hours']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['INVALID_DATA']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['date']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$shift_hours[0].holidays[0].date']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['Date Should be between current and next financial year']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['name']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].holidays[0].name']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['required field not found']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['date']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].holidays[0].date']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['required field not found']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=100] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['id']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].users[0].id']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['required field not found']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['id']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].users[0].id']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['Invalid user id']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['effective_from']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].users[0].effective_from']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['Effective from should be greater than current date']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['effective_from']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].users[0].effective_from']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['Effective from should be less than 6 months']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `maximum_length` (integer/int32) **REQ** [enum=[80]] — Represents the maximum length permitted for the field that caused the error.
            - `api_name` (string) **REQ** [enum=['name']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].name']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['invalid data']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['timezone']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].timezone']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['Invalid Timezone given']] — Represents the message that describes the outcome of the operation
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['shift_days', 'days', 'break_days', 'custom_timing']] — Represents the API name of the field that
caused the error.


**Possible values**: 

- shift_days

- days

- break_days

- custom_timing

            - `json_path` (string) **REQ** [enum=[6 values]] — Represents the JSON path of the field that caused the error.`, `$.shift_hours[0].custom_timing[0].days`, `$.shift_hours[0].break_hours[0].break_days[0]`, `$.shift_hours[0].break_hours[0].break_days`, `$.shift_hours[0].break_hours[0].custom_timing[0].days`, `$.shift_hours[0].break_hours[0].custom_timing`.
            - `supported_values` (array of string) [maxItems=50] — Lists the values that are accepted for the field that caused the error.
              items: [enum=['Monday', 'Thursday', 'Friday', 'Sunday', 'Wednesday', 'Tuesday', 'Saturday']]
            additionalProperties: any
          - `message` (string) **REQ** [enum=['Invalid days', 'invalid data']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['daily_timing', 'custom_timing', 'days']] — Represents the API name of the field that
caused the error.


**Possible values** : 

- daily_timing

- custom_timing

- days

            - `json_path` (string) **REQ** [enum=[4 values]] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['The timing of the break hours fall outside the shift']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response.
          - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `dependee` (object) **REQ** — Represents the field that the failing field depends on.
              - `api_name` (string) **REQ** [enum=['break_timing', 'daily_timing']] — Represents the API name of the field
that caused the error.


**Possible values**: 

- break_timing

- daily_timing

              - `json_path` (string) **REQ** [enum=[2 values]] — Represents the JSON path of the field that caused the error.
            - `api_name` (string) **REQ** [enum=['break_timing', 'daily_timing']] — Represents the API name of the field that
caused the error.


**Possible values**: 

- break_timing

- daily_timing

            - `json_path` (string) **REQ** [enum=[2 values]] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['break timing should be greater than 15 minutes and less than 2 hours']] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.
        - `shift_hours` (array of object) [maxItems=50] — Lists the shift hour configurations returned in the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the response code that identifies the outcome of the operation.
          - `details` (object) **REQ** — Represents additional details about the outcome of the operation.
            - `api_name` (string) **REQ** [enum=['name']] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [enum=['$.shift_hours[0].name', '$.shift_hours[0].holidays[0].name']] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=[2 values]] — Represents the message that describes the outcome of the operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation.

- **403**: Returned when the requesting user does not hold the CRM profile permission required to manage shift hours. [application/json]
    > Represents the forbidden response returned when the requesting user does not hold the CRM profile permission required to manage shift hours.
    - `code` (string) [enum=['NO_PERMISSION']] — Represents the response code that identifies the outcome of the operation.
    - `details` (object) — Represents additional details about the outcome of the operation.
      - `permissions` (array of string) [maxItems=50] — Lists the CRM profile permissions that the user must hold to access this API.
        items: [enum=['Crm_Implied_Manage_Users']]
    - `message` (string) [maxLen=100] — Represents the message that describes the outcome of the operation.
    - `status` (string) [enum=['error']] — Represents the status of the operation.

**Scopes:** ZohoCRM.settings.business_hours.CREATE

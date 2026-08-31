# GET /settings/business_hours/shift_hours/{shift}
**Operation:** `getSingleShiftHour` — Get a shift hour
> Retrieves the configuration of the shift hour identified by the `shift` path parameter, including its timing, break hours, holidays, time zone, and the users assigned to it.

**Parameters:**
- `shift` (path, string, required) [maxLen=50]: Represents the unique identifier of the shift hour to retrieve, update, or delete.

**Responses:**

- **200**: Returned when the requested shift hour configuration is retrieved successfully. [application/json]
    > Represents the error response body for the operation.
    - `shift_hours` (array of object) [maxItems=50] **REQ** — Lists the shift hour configurations returned in the response. 
      - `same_as_everyday` (boolean) **REQ** — Indicates whether the shift hour follows the same
timing on every active day. 


**Possible values**:

- **true** - the shift hour uses the same timing
every day, and **daily_timing** becomes mandatory.

- **false** - the shift hour uses different timing
for different days, and **custom_timing** becomes
mandatory.

      - `shift_days` (array of string) [maxItems=7] **REQ** — Lists the days of the week on which the shift hour is active. You can set shift timing only on the days your organization operates.
        items: [enum=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]
      - `daily_timing` (array of string) [maxItems=50, nullable] **REQ** — Represents the start and end time of the shift in `HH:MM` 24-hour
format, applied uniformly to every active day. This
field is **mandatory** when **same_as_everyday** is
**true**.

        items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
      - `custom_timing` (array of object) [maxItems=50, nullable] **REQ** — Lists per-day shift timing overrides. This field is **mandatory** when **same_as_everyday** is **false**.
        - `days` (string) **REQ** [maxLen=100] — Represents the day of the week to which this
custom shift timing applies.


**Possible values**: 

- Monday

- Tuesday

- Wednesday

- Thursday

- Friday

- Saturday

- Sunday

        - `shift_timing` (array of string) [maxItems=7] **REQ** — Represents the start and end time of the shift on the specified
day in `HH:MM` 24-hour format. 

          items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
      - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the shift hour.
      - `break_hours` (array of object) [maxItems=50, nullable] **REQ** — Lists the break windows scheduled within the shift hour. A shift can have at most two break windows.
        - `same_as_everyday` (boolean) **REQ** — Indicates whether the break hour follows the
same timing on every day the break is
scheduled. 


**Possible values**:

- **true** - the break hour uses the same
timing every day, and **daily_timing** becomes
mandatory.

- **false** - the break hour uses different
timing for different days, and
**custom_timing** becomes mandatory.

        - `break_days` (array of string) [maxItems=7] **REQ** — Lists the days of the week on which the break hour applies.
          items: [maxLen=100]
        - `daily_timing` (array of string) [maxItems=50] **REQ** — Represents the start and end time of the break
in `HH:MM` 24-hour format, applied uniformly
to every day the break is scheduled. 


This field is **mandatory** when the parent
**same_as_everyday** is **true**. A day can
have at most two breaks and the total break
time on a day cannot exceed two hours.

          items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
        - `custom_timing` (array of object) [maxItems=50, nullable] **REQ** — Lists per-day break timing overrides. 

 This field is **mandatory** when the parent **same_as_everyday** is **false**. A day can have at most two breaks and the total break time on a day cannot exceed two hours.
          - `days` (string) **REQ** [maxLen=100] — Represents the day of the week to which
this custom break timing applies.


**Possible values**: 

- Monday

- Tuesday

- Wednesday

- Thursday

- Friday

- Saturday

- Sunday

          - `break_timing` (array of string) [maxItems=7] **REQ** — Represents the start and end time of the break on the specified day
in `HH:MM` 24-hour format. A break must
be longer than 15 minutes and shorter
than 2 hours.

            items: [maxLen=5, pattern=^([0-1][0-9]|2[0-3]):[0-5][0-9]$]
        - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the break hour within the shift hour.
      - `users` (array of object) [maxItems=200, nullable] **REQ** — Lists the users assigned to the shift hour. Each entry specifies the user and the date from which the assignment becomes effective.
        - `role` (object) **REQ** — Represents the role information of the user assigned to the shift hour.
          - `name` (string) **REQ** [maxLen=100] — Represents the name of the role assigned to the user.
          - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the role assigned to the user.
        - `name` (string) **REQ** [maxLen=100] — Represents the full name of the user assigned to the shift hour.
        - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the user assigned to the shift hour.
        - `email` (string) **REQ** [maxLen=100] — Represents the email address of the user assigned to the shift hour.
        - `zuid` (string) **REQ** [maxLen=100] — Represents the unique identifier of the user assigned to the shift hour.
        - `effective_from` (string/date) **REQ** — Represents the date from which the user assignment to the shift hour becomes effective, in `YYYY-MM-DD` format. The date must be in the future and must not be more than six months ahead of the current date.
      - `holidays` (array of object) [maxItems=50, nullable] **REQ** — Lists the holidays observed during the shift hour. The holiday date must fall between the current and the next financial year.
        - `date` (string/date) **REQ** — Represents the date of the holiday in `YYYY-MM-DD` format.
        - `year` (object) **REQ** — Represents the year of the holiday.
        - `name` (string) **REQ** [maxLen=80] — Represents the name of the holiday. The name must not contain the special characters.
        - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the holiday.
        - `userFmt` (string) **REQ** [maxLen=100] — Represents the holiday date formatted using the date format configured for the requesting user.
      - `users_count` (integer/int32) **REQ** — Represents the number of users currently assigned to the shift hour.
      - `timezone` (string) **REQ** [maxLen=100] — Represents the time zone in which the shift hours are scheduled. 
      - `name` (string) **REQ** [maxLen=80] — Represents the name of the shift hour. The name must be unique within the organization and must not contain the special characters.
    - `shift_count` (object) **REQ** — Represents aggregate counts that summarize the shift hour configurations returned in the response.
      - `total_shift_with_user` (integer/int32) **REQ** — Represents the total number of shift hours that have at least one user assigned.

- **204**: Returned when no shift hours are configured for the organization, or when the requested shift hour does not exist.

- **403**: Returned when the requesting user does not hold the CRM profile permission required to manage shift hours. [application/json]
    > Represents the forbidden response returned when the requesting user does not hold the CRM profile permission required to manage shift hours.
    - `code` (string) [enum=['NO_PERMISSION']] — Represents the response code that identifies the outcome of the operation.
    - `details` (object) — Represents additional details about the outcome of the operation.
      - `permissions` (array of string) [maxItems=50] — Lists the CRM profile permissions that the user must hold to access this API.
        items: [enum=['Crm_Implied_Manage_Users']]
    - `message` (string) [maxLen=100] — Represents the message that describes the outcome of the operation.
    - `status` (string) [enum=['error']] — Represents the status of the operation.

**Scopes:** ZohoCRM.settings.business_hours.READ

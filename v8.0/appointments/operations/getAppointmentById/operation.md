# GET /Appointments__s/{appointmentId}
**Operation:** `getAppointmentById` — Get an Appointment Record by ID

> To retrieve the details of a single appointment record from your Zoho CRM organization.


**Parameters:**
- `appointmentId` (path, string, required) [maxLen=100]: Specify the unique identifier of the appointment record. Use the [Get Appointments API](appointments.yaml#$.paths./Appointments__s.get) to retrieve all appointment records and obtain the ID of the required appointment record.

**Schemas:**
`ErrorResponseCore2271053024`:
  > Represents the error response returned when the appointment ID in the request URL is invalid.
  - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code returned for the invalid URL pattern failure.
  - `details` (object) **REQ** — Represents the error details object for the invalid URL pattern failure.
  - `message` (string) **REQ** [enum=['Please check if the URL trying to access is a correct one']] — Represents the error message describing the invalid URL pattern failure.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status for the invalid URL pattern failure.

**Responses:**

- **200**: Returns the details of the specified appointment record, including fields such as Owner, Service_Name, Appointment_For, Appointment_Name, and Status.
 — Schema: `GetappointmentssResponse200` [application/json]
    > Represents the success response for the request to retrieve appointment records, containing the list of appointment objects.
    schema: `GetappointmentssResponse200`
    - `data` (array of object `GETDataNested`) [minItems=1, maxItems=200] **REQ** — Represents the list of appointment records returned by the GET request.
      schema: `GETDataNested`
      - `Owner` (object `GETOwnerNested`) **REQ** — Represents the service member assigned as the appointment owner, including the user ID, full name, and email address.
        schema: `GETOwnerNested`
        - `name` (string) **REQ** [maxLen=255] — Represents the full name of the appointment owner.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the appointment owner.
        - `email` (string) **REQ** [maxLen=255] — Represents the email address of the appointment owner.
      - `$currency_symbol` (string) [maxLen=255] — Represents the currency symbol for the CRM organization's primary currency.
      - `Address` (string) [maxLen=255, nullable] — Represents the address where the service is delivered when the appointment location is Client Address.
      - `Appointment_Start_Time` (string) **REQ** [maxLen=120] — Represents the scheduled start date and time of the appointment.
      - `Cancellation_Reason` (string) [maxLen=120, nullable] — Denotes who cancelled the appointment.
Possible Values: 'By Customer' and 'By Team'. The default value is 'By Customer'.
      - `$field_states` (string) [maxLen=255, nullable] — Represents the state of fields with conditional visibility or special behavior.
      - `Appointment_For` (object `GETAppointmentForNested`) **REQ** — Represents the customer for whom the appointment was created, including the record ID, name, and module information.
        schema: `GETAppointmentForNested`
        - `module` (object `GETModuleNested`) **REQ** — Represents the module details for the Appointment_For customer record, including the module API name and ID.
          schema: `GETModuleNested`
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module for the customer record.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the module.
        - `name` (string) **REQ** [maxLen=255] — Represents the full name of the customer.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the customer record.
      - `Rescheduled_To` (string) [maxLen=120, nullable] — Represents the new appointment start time after rescheduling.
      - `$sharing_permission` (string) [maxLen=255] — Represents the sharing permission level of the appointment record for the current user.
      - `Reschedule_Reason` (string) [maxLen=120, nullable] — Denotes who rescheduled the appointment.
Possible Values: 'By Customer' and 'By Team'. The default value is 'By Customer'.
      - `Job_Sheet_Name__s` (string) [maxLen=255, nullable] — Represents the name of the job sheet created for the completed appointment.
      - `Additional_Information` (string) [maxLen=32000, nullable] — Represents any additional details about the appointment or customer requirements.
      - `Last_Activity_Time` (string) [maxLen=120, nullable] — Represents the date and time of the last activity on the appointment record.
      - `Job_Sheet_Created__s` (boolean) — Indicates whether a job sheet has been created for this appointment. 
**Possible values**:
- true - A job sheet has been created.
- false - No job sheet has been created.
      - `Cancelled_Time` (string) [maxLen=120, nullable] — Represents the date and time when the appointment was cancelled.
      - `Cancellation_Note` (string) [maxLen=2000, nullable] — Represents the note explaining the reason for cancelling the appointment.
      - `Modified_By` (object `GETModifiedByNested`) — Represents the user who last modified the appointment record, including the user ID, full name, and email address.
        schema: `GETModifiedByNested`
        - `name` (string) **REQ** [maxLen=255] — Represents the full name of the user who last modified the record.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the user who last modified the record.
        - `email` (string) **REQ** [maxLen=255] — Represents the email address of the user who last modified the appointment record.
      - `Reschedule_Count` (integer/int32) — Represents the number of times the appointment has been rescheduled.
      - `Rescheduled_By` (object) [nullable] — Represents the user who rescheduled the appointment.
      - `Date_1` (string) [maxLen=20, nullable] — Represents an additional date field for the appointment record.
      - `id` (string) [maxLen=255] — Represents the unique ID of the appointment record.
      - `Rescheduled_Time` (string) [maxLen=120, nullable] — Represents the date and time when the appointment was rescheduled.
      - `Remind_At` (array of object) [maxItems=100, nullable] — Represents the list of reminder configurations for the appointment.
        - `period` (string) [enum=['minutes', 'hours', 'days']] — Represents the unit of time for the reminder.
**Possible values**:
- minutes - The reminder is sent a specified number of minutes before the appointment.
- hours - The reminder is sent a specified number of hours before the appointment.
- days - The reminder is sent a specified number of days before the appointment.
        - `unit` (integer/int32) — Represents the numeric value of the reminder time. The value of a unit key can be only from **0 to 100**.
      - `Appointment_End_Time` (string) [maxLen=120] — Represents the scheduled end date and time of the appointment.
      - `Status` (string) [maxLen=120] — Represents the current status of the appointment.
      - `Modified_Time` (string) [maxLen=120] — Represents the date and time when the appointment record was last modified.
      - `Service_Name` (object `GETServiceNameNested`) **REQ** — Represents the service for which the appointment was created, including the service ID and name.
        schema: `GETServiceNameNested`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the service for which the appointment was created.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the service.
      - `Created_Time` (string) [maxLen=120] — Represents the date and time when the appointment record was created.
      - `Rescheduled_From` (string) [maxLen=120, nullable] — Denotes the previous appointment time from which the appointment was rescheduled to the new time. The Rescheduled_From time should be lesser than the new appointment time. The value should be given in the ISO 8601 format.
      - `Cancelled_By` (object) [nullable] — Represents the user who cancelled the appointment.
      - `$editable` (boolean) — Indicates whether the current user has permission to edit the appointment record.
      - `Appointment_Name` (string) **REQ** [maxLen=255] — Represents the name of the appointment record.
      - `Duration` (integer/int32) — Represents the duration of the appointment in minutes.
      - `Job_Sheet_Section__s` (string) [maxLen=120, nullable] — Represents the job sheet section displayed to the user for a completed appointment.
      - `Record_Status__s` (string) [maxLen=255] — Represents the availability status of the appointment record.
      - `$status` (string) [maxLen=120] — Represents the Custom View status indicator for the appointment record.
      - `Job_Sheet_Description__s` (string) [maxLen=32000, nullable] — Represents the description of the job sheet associated with the completed appointment.
      - `Created_By` (object `GETCreatedByNested`) — Represents the user who created the appointment record, including the user ID, full name, and email address.
        schema: `GETCreatedByNested`
        - `name` (string) **REQ** [maxLen=255] — Represents the full name of the user who created the record.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the user who created the record.
        - `email` (string) **REQ** [maxLen=255] — Represents the email address of the user who created the appointment record.
      - `Tag` (array of string) [maxItems=10] — Represents the list of tags associated with the appointment record.
        items: [maxLen=2000]
      - `Location` (string) **REQ** [maxLen=120] — Represents the location where the appointment service is offered.
      - `Reschedule_Note` (string) [maxLen=2000, nullable] — Represents the note explaining the reason for rescheduling the appointment.
      - `Contact_Name__s` (string) [maxLen=255, nullable] — Represents the name and unique ID of the contact associated with the appointment.
      additionalProperties: any
    additionalProperties: any

- **400**: The request was not processed because the module API name or the appointment ID in the request URL is invalid.

**Resolution:** Verify that the module API name in the request URL is correct. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the valid module API name, and confirm that the appointment ID corresponds to an existing record.
 [application/json]
    > Represents the error response body when the module API name or the appointment ID in the request URL is invalid. Contains one of two error such as an INVALID_MODULE error when the module name is unrecognized, or an INVALID_URL_PATTERN error when the appointment ID cannot be resolved.
    oneOf:
      - `ErrorResponseCore1604218709` — Represents the error when the module API name in the request URL is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents the details about the path parameter that caused the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the path parameter in the request URL that is invalid.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message describing the invalid module name.
        - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
      - `ErrorResponseCore2271053024` — Represents the error response returned when the appointment ID in the request URL is invalid.

- **404**: The request was not processed because the URL or the appointment ID is invalid.

**Resolution:** Verify that the appointment ID in the request URL corresponds to an existing appointment record in the organization.
 — Schema: `ErrorResponseCore2271053024` [application/json]
    > Represents the error response returned when the appointment ID in the request URL is invalid.

**Scopes:** ZohoCRM.modules.appointments.READ

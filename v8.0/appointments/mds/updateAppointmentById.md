# PUT /Appointments__s/{appointmentId}
**Operation:** `updateAppointmentById` — Update an Appointment Record by ID
> To update a single appointment record by its ID in your Zoho CRM organization.

**Parameters:**
- `id` (query, number, optional) [enum=[111115000000147180]]: Specify the ID of the appointment record to update. Use the [Get Appointments API](appointments.yaml#$.paths./Appointments__s.get) to get the ID.
- `appointmentId` (path, string, required) [maxLen=100]: Specify the unique identifier of the appointment record. Use the [Get Appointments API](appointments.yaml#$.paths./Appointments__s.get) to retrieve all appointment records and obtain the ID of the required appointment record.

**Schemas:**
`CreatedByNested`:
  > appointment created by
  - `name` (string) [maxLen=255, nullable] — Represents the full name of the user who created the appointment record.

  - `id` (string) [maxLen=255, nullable] — Represents the unique identifier of the user who created the appointment record.

  - `email` (string/email) [maxLen=33, nullable] — Represents the email address of the user who created the appointment record.

`ModifiedByNested`:
  > modified by
  - `name` (string) [maxLen=255, nullable] — Represents the full name of the user who last modified the appointment record.
  - `id` (string) [maxLen=255, nullable] — Represents the unique ID of the user who last modified the appointment record.
  - `email` (string/email) [maxLen=33, nullable] — Represents the email address of the user who last modified the appointment record.

**Request Body** — application/json `PutappointmentssRequest`
> The request body must contain a **data** array with the appointment fields to update for the record.
  > Represents the request body schema for updating appointment records.
  - `data` (array of object `DataNested`) [minItems=1, maxItems=100] **REQ** — Represents the data array containing the appointment objects to update. 
    schema: `DataNested`
    - `Owner` (object `OwnerNested`) **REQ** — Represents the ID of the service member who will provide the service for this appointment. (Required)
      schema: `OwnerNested`
      - `name` (string) [maxLen=100, nullable] — Represents the full name of the appointment owner.
      - `id` (string) [maxLen=100, nullable] — Represents the unique ID of the appointment owner.
      - `email` (string/email) [maxLen=100, nullable] — Represents the email address of the appointment owner.
    - `Address` (string) [maxLen=255, nullable] — All three appointment records deleted successfully.

    - `$currency_symbol` (string) [maxLen=1, nullable] — Represents the currency symbol associated with the CRM organization's primary currency.

    - `Appointment_Start_Time` (string/date-time) **REQ** [maxLen=120] — Represents the scheduled start date and time of the appointment, expressed in ISO 8601 format.
    - `Cancellation_Reason` (string) [maxLen=120, nullable] — Represents who cancelled the appointment.
**Possible values**:
- By Customer - The appointment was cancelled by the customer.
- By Team - The appointment was cancelled by the service team.
    - `Appointment_For` (object `AppointmentForNested`) **REQ** — Contains the name, ID and the module's API name of the customer for whom you are creating the appointment. (Required)
      schema: `AppointmentForNested`
      - `name` (string) [maxLen=2, nullable] — Represents the full name of the customer record in the associated module.

      - `id` (string) [maxLen=18, nullable] — Represents the list of result objects for each appointment deletion is attempted. Each item is either a success confirmation or an error response.
Test7
      - `module` (object `ModuleNested`) — module name
        schema: `ModuleNested`
        - `api_name` (string) [maxLen=8, nullable] — Represents the API name of the module for the customer record.
        - `id` (string) [maxLen=18, nullable] — Represents the unique ID of the module.
    - `$field_states` (string) [maxLen=255, nullable] — Represents the state of fields that have conditional visibility or special behavioral rules applied within the appointment record.
    - `Rescheduled_To` (string) [maxLen=120, nullable] — Represents the new start time of the appointment after rescheduling, expressed in ISO 8601 format.
    - `$sharing_permission` (string) [maxLen=11, nullable] — Represents the sharing permission level granted to the current user for the appointment record.
    - `Reschedule_Reason` (string) [maxLen=120, nullable] — Represents who rescheduled the appointment.
**Possible values**:
- By Customer - The appointment was rescheduled by the customer.
- By Team - The appointment was rescheduled by the service team.
    - `Job_Sheet_Name__s` (string) [maxLen=120, nullable] — Represents the name of the job sheet created for the completed appointment.
    - `Additional_Information` (string) [maxLen=32000, nullable] — Represents any supplementary details about the appointment or specific customer requirements that do not belong to a standard field.
    - `Last_Activity_Time` (string) [maxLen=120, nullable] — Represents the date and time of the last activity recorded on the appointment.
    - `Job_Sheet_Created__s` (boolean) [nullable] — Indicates whether a job sheet has been created for this appointment.
**Possible values**:
- true - A job sheet has been created and is associated with the appointment.
- false - No job sheet has been created for the appointment.
    - `Cancelled_Time` (string) [maxLen=120, nullable] — Represents the date and time when the appointment was cancelled.
    - `Cancellation_Note` (string) [maxLen=2000, nullable] — INVALID_DATA error where appointment ID is invalid or already deleted.

    - `Modified_By` (object `ModifiedByNested`) — modified by
    - `Reschedule_Count` (integer/int32) [nullable] — Represents the number of times the appointment has been rescheduled.
    - `$state` (string) [maxLen=4, nullable] — Represents the save state of the appointment record, indicating whether the record is in a draft, saved, or transitional state.
    - `Rescheduled_By` (object) — Represents the user who rescheduled the appointment.
      - `name` (string) [maxLen=255, nullable] — Represents the full name of the user who rescheduled the appointment.
      - `id` (string) [maxLen=255, nullable] — Represents the unique identifier of the user who rescheduled the appointment.
      - `email` (string/email) [maxLen=33, nullable] — Represents the email address of the user who rescheduled the appointment.
    - `Date_1` (string) [maxLen=20, nullable] — Delete one or more appointment records.

    - `id` (string) [maxLen=18, readOnly, nullable] — Represents the unique identifier of the appointment record.
    - `Rescheduled_Time` (string) [maxLen=120, nullable] — Represents the date and time when the appointment was rescheduled.
    - `Remind_At` (array of object) [maxItems=100, nullable] — Contains the list of reminder configurations for the appointment, each specifying a time unit and reminder period.
      - `period` (string) [enum=['minutes', 'hours', 'days']] — Represents the unit of time for the reminder.
Possible values:
**minutes** - Reminder in minutes.
**hours** - Reminder in hours.
**days** - Reminder in days.
      - `unit` (integer/int32) — Represents the numeric value of the reminder time.
    - `Appointment_End_Time` (string/date-time) [maxLen=120, nullable] — Represents the scheduled end date and time of the appointment, expressed in ISO 8601 format.
    - `Status` (string) [maxLen=120, nullable] — Represents the current status of the appointment.
Possible values:
**Scheduled** - The appointment is booked and upcoming.
**Overdue** - The appointment has passed its scheduled time without completion.
**Completed** - The appointment has been completed.
**Cancelled** - The appointment has been cancelled.
    - `Modified_Time` (string/date-time) [maxLen=120, nullable] — Represents the date and time when the appointment record was last modified.
    - `Service_Name` (object `ServiceNameNested`) **REQ** — Contains the name and distinctive ID of the service for which you are creating the appointment. (Required)
      schema: `ServiceNameNested`
      - `name` (string) [maxLen=100, nullable] — Represents the name of the service for which the appointment is created.
      - `id` (string) [maxLen=100, nullable] — Represents the unique ID of the service.
    - `Created_Time` (string/date-time) [maxLen=120, nullable] — Invalid HTTP request method type used in the request.

    - `Rescheduled_From` (string) [maxLen=120, nullable] — Represents the previous start time of the appointment before it was rescheduled, expressed in ISO 8601 format.
    - `Cancelled_By` (object) [nullable] — Invalid module API name provided in the request.

    - `Duration` (integer/int32) [nullable] — Represents the duration of the appointment in minutes.
    - `Appointment_Name` (string) [maxLen=225, nullable] — Partial deletion where one record deleted, one failed with INVALID_DATA

    - `$editable` (boolean) [nullable] — Indicates whether the current user has permission to edit the appointment record.
**Possible Values**:
- true - The current user has edit access to the appointment record.
- false - The current user does not have edit access to the appointment record.
    - `Job_Sheet_Section__s` (string) [maxLen=120, nullable] — Represents the job sheet section displayed to the user for a completed appointment.
    - `Record_Status__s` (string) [maxLen=9, nullable] — Represents the availability status of the appointment record.
    - `$status` (string) [maxLen=7, nullable] — The request could not be processed due to an invalid appointment ID, an invalid module name, or an unsupported HTTP request method.

**Resolution:** For INVALID_DATA, make a GET Appointments API call and provide a valid appointment ID. For INVALID_REQUEST_METHOD, use only the DELETE method. For INVALID_MODULE, verify that the module API name in the request is correct.
    - `Job_Sheet_Description__s` (string) [maxLen=32000, nullable] — Represents the description of the job sheet associated with the completed appointment.
    - `Tag` (array of string) [maxItems=100, nullable] — Represents the list of tags associated with the appointment record.
      items: [maxLen=2000]
    - `Created_By` (object `CreatedByNested`) — appointment created by
    - `Location` (string) [maxLen=120, enum=['Client Address', 'Business Address'], nullable] — Represents the location where the appointment service is offered.
Possible values:
**Client Address** - The service is delivered at the customer's address.
**Business Address** - The service is delivered at the business location.
    - `Reschedule_Note` (string) [maxLen=2000, nullable] — Represents the note explaining the reason for rescheduling the appointment.

**Responses:**

- **200**: Returns a confirmation of the successful appointment record update, including the record ID, creation and modification timestamps, and the associated user details. — Schema: `PutappointmentssResponse200` [application/json]
    > Represents the success response for the request to update appointment records.
    schema: `PutappointmentssResponse200`
    - `data` (array of object `DataNested1`) [minItems=1, maxItems=100] — Represents the list of result objects for each updated appointment record.
      schema: `DataNested1`
      - `code` (string) [maxLen=255] — Represents the result code for the operation.
      - `details` (object `DetailsNested`) — Represents the details of an appointment record, including its ID, creation timestamp, and last modification timestamp.
        schema: `DetailsNested`
        - `Modified_Time` (string) [maxLen=120] — Represents the date and time when the appointment record was last modified.
        - `Modified_By` (object `ModifiedByNested`) — Represents the user who last modified the appointment record, including the user ID, full name, and email address.
        - `Created_Time` (string) [maxLen=120] — Represents the date and time when the appointment record was created.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the appointment record.
        - `Created_By` (object `CreatedByNested`) — Represents the user who created the appointment record, including the user ID, full name, and email address.
      - `message` (string) [maxLen=255] — Represents the result message for the operation.
      - `status` (string) [maxLen=255] — Indicates the status of the operation.

- **400**: One or more request fields are invalid or missing.

**Resolution:** Ensure that all required fields are present and that field values conform to the validation requirements for the appointment update. [application/json]
    > Represents the error response body for a failed appointment update request, containing either a wrapped list of validation errors or a single request-level error.
    oneOf:
        - `data` (array of object) [maxItems=25] **REQ** — Contains the error objects returned for the appointment update request.
          oneOf:
            - `ErrorResponseCore1720623915` — Represents the error when a required appointment field is missing from the request.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCore622374562` — Represents the error when Rescheduled_From and Appointment_Start_Time have the same value.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_UNCHANGED']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `dependee` (object) **REQ** — Represents the dependent field that triggers this constraint.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggers the dependency constraint.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggers the dependency constraint.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=[2 values]] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCore261228299` — Represents the error when the Rescheduled_From field is empty while Reschedule_Reason is provided.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING', 'DEPENDENT_MISMATCH']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `dependee` (object) **REQ** — Represents the dependent field that triggers this constraint.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggers the dependency constraint.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggers the dependency constraint.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=[2 values]] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCore1207168962` — Represents the error when the selected service is unavailable at the specified appointment time.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=['Service is not available on the given time']] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCore1818284114` — Represents the error when the appointment time does not fall within the configured business hours.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=['Appointment time does not falls under business hours']] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCore1277582131` — Represents the error when the appointment owner is not a member of the service specified in Service_Name.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `dependee` (object) **REQ** — Represents the dependent field that triggers this constraint.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggers the dependency constraint.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggers the dependency constraint.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=['Appointment Owner is not a part of Service Members']] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCore1593946428` — Represents the error when the Appointment_For field value is not a valid JSON object.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the expected data type for the field that has an incorrect value.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=['invalid data', 'INVALID_DATA']] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCore2114620743` — Represents the error when the module API name provided in Appointment_For does not exist in the multi-module lookup.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=[3 values]] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCore1332683101` — Represents the error when cancellation information fields are updated without setting the Status to Cancelled.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `dependee` (object) **REQ** — Represents the dependent field that triggers this constraint.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggers the dependency constraint.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggers the dependency constraint.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCore1090893661` — Represents the error when an appointment is marked as completed without a job sheet.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=['Appointment cannot be marked as completed without creating the jobsheet']] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCore653152835` — Represents the error when the appointment Status is set to Completed before the appointment end time.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `dependee` (object) **REQ** — Represents the dependent field that triggers this constraint.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggers the dependency constraint.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggers the dependency constraint.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=['Appointment cannot be marked as completed before the appointment ends']] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCore899638570` — Represents the error when a job sheet is created for an appointment that has not been completed.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `dependee` (object) **REQ** — Represents the dependent field that triggers this constraint.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggers the dependency constraint.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggers the dependency constraint.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=[2 values]] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCore496791912` — Represents the error when the appointment Status is set to Overdue before the appointment end time.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `dependee` (object) **REQ** — Represents the dependent field that triggers this constraint.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggers the dependency constraint.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggers the dependency constraint.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=['Appointment cannot be marked as overdue before the appointment ends']] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCore201487910` — Represents the error when the appointment start time is set to a past date.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `dependee` (object) **REQ** — Represents the dependent field that triggers this constraint.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggers the dependency constraint.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggers the dependency constraint.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=['Appointment cannot be scheduled for past dates']] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCore55175210` — Represents the error when the required unit key is missing from a Remind_At object.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this response.
              - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
              - `message` (string) **REQ** [enum=['mandatory key missing']] — Represents the error message describing the validation failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
            - `ErrorResponseCoreRecordLocked` — Represents the error response returned when the appointment record is locked and cannot be modified.
              - `code` (string) **REQ** [enum=['RECORD_LOCKED']] — Represents the error code returned for the record-locked failure.
              - `details` (object) **REQ** — Represents the error details associated with the locked record, including the field name, action, and JSON path that triggered the failure.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the record-locking error.
                - `action` (string) **REQ** [enum=['record_locking']] — Represents the action that was attempted on the locked record.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that triggered the record-locked error.
              - `message` (string) **REQ** [enum=['Sorry, you cannot perform this operation as the record is locked.']] — Represents the error message describing the record-locked failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status for the record-locked failure.
      - `ErrorResponseCore1944579470` — Represents the error when the appointment ID specified in the request URL is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents the details about the invalid path parameter.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the path parameter in the request URL that contains an invalid ID.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message indicating that the appointment ID is invalid.
        - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
      - `ErrorResponseCore1009543207` — Represents the error when the request data array exceeds the maximum allowed length.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents the details about the request data that caused the validation error.
          - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed number of items in the data array.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that contains invalid data.
          - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that contains invalid data.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the invalid data.
        - `status` (string) **REQ** [enum=['error']] — Indicates the response status.

- **403**: The user does not have permission to update the specified appointment.

**Resolution:** Contact the system administrator to grant the required update permissions to the user profile. [application/json]
    > Represents the error response body returned when an appointment update is denied due to insufficient permissions, containing either a list of action-level permission errors or a record-level permission error.
    oneOf:
      - `PutappointmentByIdError403` — Represents the error response for Forbidden failures when updating a single appointment, containing a list of permission-error objects.
        - `data` (array of object `ErrorResponseCoreNoPermission`) [maxItems=25] **REQ** — Represents the list of permission-error objects returned for the failed appointment update action.
          schema: `ErrorResponseCoreNoPermission`
          - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned for the permission-denied failure.
          - `details` (object) **REQ** — Represents the error details for the permission-denied failure, including the list of required permissions.
            - `permissions` (array of string) [maxItems=50] **REQ** — Represents the list of permissions required to perform the appointment action.
              items: [maxLen=255]
          - `message` (string) **REQ** [enum=['permission denied', 'record not accessible']] — Represents the error message describing the permission-denied failure.
          - `status` (string) **REQ** [enum=['error']] — Indicates the response status for the permission-denied failure.
      - `ErrorResponseCoreNoPermissionFlat` — Represents the flat error response returned when the appointment record is not accessible due to insufficient permissions.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned for the flat permission-denied failure.
        - `details` (object) **REQ** — Represents the error details for the flat permission-denied failure, including the resource path index.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path in the request that triggered the permission-denied error.
        - `message` (string) **REQ** [enum=['record not accessible']] — Represents the error message describing the flat permission-denied failure.
        - `status` (string) **REQ** [enum=['error']] — Indicates the response status for the flat permission-denied failure.

**Scopes:** ZohoCRM.modules.appointments.UPDATE

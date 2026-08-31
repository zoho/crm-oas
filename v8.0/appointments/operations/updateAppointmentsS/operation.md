# PUT /Appointments__s
**Operation:** `updateAppointmentsS` — Update appointment records

> To update one or more appointment records in your Zoho CRM organization. You can update a maximum of 100 appointments per API call.


**Schemas:**
`CreatedByNested`:
  > appointment created by
  - `name` (string) [maxLen=255, nullable] — Represents the full name of the user who created the appointment record.

  - `id` (string) [maxLen=255, nullable] — Represents the unique identifier of the user who created the appointment record.

  - `email` (string/email) [maxLen=33, nullable] — Represents the email address of the user who created the appointment record.

`DetailsNested`:
  > Represents the details of an appointment record, including its ID, creation timestamp, and last modification timestamp.
  - `Modified_Time` (string) [maxLen=120] — Represents the date and time when the appointment record was last modified.
  - `Modified_By` (object `ModifiedByNested`) — Represents the user who last modified the appointment record, including the user ID, full name, and email address.
  - `Created_Time` (string) [maxLen=120] — Represents the date and time when the appointment record was created.
  - `id` (string) [maxLen=255] — Represents the unique identifier of the appointment record.
  - `Created_By` (object `CreatedByNested`) — Represents the user who created the appointment record, including the user ID, full name, and email address.
`ErrorResponseCore1009543207`:
  > Represents the error when the request data array exceeds the maximum allowed length.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
  - `details` (object) **REQ** — Represents the details about the request data that caused the validation error.
    - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed number of items in the data array.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that contains invalid data.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that contains invalid data.
  - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the invalid data.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
`ErrorResponseCore1544688711`:
  > Represents the error when the appointment ID provided in the request is invalid.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
  - `details` (object) **REQ** — Represents the details about the field that caused the validation failure.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request that caused the error.
  - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message describing the validation failure.
  - `status` (string) **REQ** [enum=['error']] — Indicates the response status.
`ModifiedByNested`:
  > modified by
  - `name` (string) [maxLen=255, nullable] — Represents the full name of the user who last modified the appointment record.
  - `id` (string) [maxLen=255, nullable] — Represents the unique ID of the user who last modified the appointment record.
  - `email` (string/email) [maxLen=33, nullable] — Represents the email address of the user who last modified the appointment record.
`Post207multistatusResponse207`:
  > Represents a successful result item in the Multi-Status response, containing the result code, details, message, and status.
  - `details` (object `DetailsNested`) — Represents the details of an appointment record, including its ID, creation timestamp, and last modification timestamp.
  - `code` (string) [maxLen=255] — Represents the result code for the appointment record operation.
  - `message` (string) [maxLen=255] — Represents the result message for the appointment record operation.
  - `status` (string) [maxLen=255] — Indicates the result status of the appointment record operation.

**Request Body** — application/json `PutappointmentssRequest`
> The request body must contain a **data** array with one or more appointment objects to update. You can include a maximum of **100** objects per request. Each object must include the **ID** field to identify the appointment record to update.

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

- **200**: Returns a confirmation for each successfully updated appointment record, including the record ID, creation and modification timestamps, and the identities of the users who created and last modified the record.
 — Schema: `PutappointmentssResponse200` [application/json]
    > Represents the success response for the request to update appointment records.
    schema: `PutappointmentssResponse200`
    - `data` (array of object `DataNested1`) [minItems=1, maxItems=100] — Represents the list of result objects for each updated appointment record.
      schema: `DataNested1`
      - `code` (string) [maxLen=255] — Represents the result code for the operation.
      - `details` (object `DetailsNested`) — Represents the details of an appointment record, including its ID, creation timestamp, and last modification timestamp.
      - `message` (string) [maxLen=255] — Represents the result message for the operation.
      - `status` (string) [maxLen=255] — Indicates the status of the operation.

- **207**: Returns a mixed-status response when the batch contains both successfully updated appointment records and records that failed the update. Each item in the response array is either a success object or an error object with an INVALID_DATA code indicating an invalid appointment ID.
 [application/json]
    > Represents the Multi-Status response body returned when the update request produces a mix of successfully updated and failed appointment updates. The response contains at least one success and at least one error.

    - `data` (array of object) [minItems=2, maxItems=200] **REQ** — Represents the list of result objects returned for each appointment update attempt. Each item is either a success response for a successfully updated record or an error response for a failed update.

      oneOf:
        - `Post207multistatusResponse207` — Represents a successful result item in the Multi-Status response, containing the result code, details, message, and status.
        - `ErrorResponseCore1544688711` — Represents the error when the appointment ID provided in the request is invalid.

- **400**: The request was not processed due to invalid or missing fields. 

**Resolution:** Verify that all required fields are present and that field values satisfy the validation requirements for the requested appointment update operation.
 [application/json]
    > Represents the error response body returned when the PUT request to update appointment records fails. 

The response is one of two variants: a wrapped array of per-record validation error objects, or a flat error object for request-level failures.

    oneOf:
        - `data` (array of object) [maxItems=25] **REQ** — Contains the list of error objects for appointment records that failed validation during the update request. Each object corresponds to one failed record.

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
            - `PostappointmentssDependentFieldMissingCancellationStatusErrorItem` — Represents an error item returned when a cancellation information field is provided without the required dependent field in the create appointment request.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code for the dependent-field-missing failure.
              - `details` (object) **REQ** — Represents the error details for the dependent-field-missing failure, including the dependee field and the missing dependent field.
                - `dependee` (object) **REQ** — Represents the details of the field that triggers the dependency requirement.
                  - `api_name` (string) **REQ** [enum=['Cancellation_Reason']] — Represents the API name of the field that triggers the dependency requirement.
                  - `json_path` (string) **REQ** [enum=['$.data[0].Cancellation_Reason']] — Represents the JSON path to the field that triggers the dependency requirement.
                - `api_name` (string) **REQ** [enum=['Status']] — Represents the API name of the missing dependent field.
                - `json_path` (string) **REQ** [enum=['$.data[0].Status']] — Represents the JSON path to the missing dependent field in the request.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing the dependent-field-missing failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status for the dependent-field-missing failure.
            - `PostappointmentssDependentMismatchCancellationStatusErrorItem` — Represents an error item returned when cancellation information fields are provided in the request but the appointment Status is not set to Cancelled.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code for the dependent-mismatch failure.
              - `details` (object) **REQ** — Represents the error details for the dependent-mismatch failure, including the dependee field and the mismatched field.
                - `dependee` (object) **REQ** — Represents the details of the field whose value determines the dependency.
                  - `api_name` (string) **REQ** [enum=['Cancellation_Reason']] — Represents the API name of the field whose value determines the dependency.
                  - `json_path` (string) **REQ** [enum=['$.data[0].Cancellation_Reason']] — Represents the JSON path to the field whose value determines the dependency.
                - `api_name` (string) **REQ** [enum=['Status']] — Represents the API name of the field that caused the dependency mismatch.
                - `json_path` (string) **REQ** [enum=['$.data[0].Status']] — Represents the JSON path to the field that caused the dependency mismatch in the request.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing the dependent-mismatch failure.
              - `status` (string) **REQ** [enum=['error']] — Indicates the response status for the dependent-mismatch failure.
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
            - `ErrorResponseCore1009543207` — Represents the error when the request data array exceeds the maximum allowed length.
      - `ErrorResponseCore1009543207` — Represents the error when the request data array exceeds the maximum allowed length.

- **403**: The authenticated user does not have the required Zoho CRM profile permission to perform the requested appointment action. A NOT_ALLOWED error is also returned when the operation attempts to reschedule or change the status of an appointment that is already completed or cancelled.

**Resolution:** A CRM administrator must grant the appropriate appointment-action permissions in the Zoho CRM user's profile.
 [application/json]
    > Represents the error response returned when the authenticated user lacks permission to update appointments, containing a list of error objects that describe the permission failure.

    - `data` (array of object `ErrorResponseCoreNoPermission`) [maxItems=25] **REQ** — Contains the list of error objects returned when the caller lacks permission to update the requested appointment records.

      schema: `ErrorResponseCoreNoPermission`
      - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned for the permission-denied failure.
      - `details` (object) **REQ** — Represents the error details for the permission-denied failure, including the list of required permissions.
        - `permissions` (array of string) [maxItems=50] **REQ** — Represents the list of permissions required to perform the appointment action.
          items: [maxLen=255]
      - `message` (string) **REQ** [enum=['permission denied', 'record not accessible']] — Represents the error message describing the permission-denied failure.
      - `status` (string) **REQ** [enum=['error']] — Indicates the response status for the permission-denied failure.

**Scopes:** ZohoCRM.modules.appointments.UPDATE

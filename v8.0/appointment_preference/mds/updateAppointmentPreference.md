# PUT /settings/appointment_preferences
**Operation:** `updateAppointmentPreference` — Update Appointment Preferences
> To update the appointment preference settings in your Zoho CRM organization, including booking constraints, job sheet requirements, deal creation configuration, and record-sharing settings.

**Request Body** (required) — application/json
> Contains the input data required to process the request. 
  > Contains the appointment preference settings to update in the Zoho CRM organization.
  - `appointment_preferences` (object) — Specify the appointment preferences to configure for the Zoho CRM organization.
    - `show_job_sheet` (boolean) — Represents whether filling out the job sheet is mandatory for marking an appointment as 'completed'. You can mandate job sheets only when **when_duration_exceeds: ask_appointment_provider_to_complete**.
Possible values:
**true** - Job sheet is mandatory for appointment completion.
**false** - Job sheet is not mandatory for appointment completion.

    - `when_duration_exceeds` (string) [enum=['mark_as_complete', 'ask_appointment_provider_to_complete']] — Represents who has to mark the appointment as 'Completed' when the service duration gets over.
Possible values:
**mark_as_complete** - The appointment is automatically marked as 'completed'.
**ask_appointment_provider_to_complete** - User have to manually mark the appointment as 'completed'.

    - `when_appointment_completed` (string) [enum=['do_not_create_deal', 'create_deal']] — Represents whether a deal has to be created, when an appointment is completed.
Possible values:
**create_deal** - Deal is created when any appointment is marked 'Completed'.
**do_not_create_deal** - Deal is not created when any appointment is marked 'Completed'.

    - `allow_booking_outside_service_availability` (boolean) **REQ** — Denotes if you can create appointments outside service availability.
Possible values:
**true** - You can create appointments outside service availability.
**false** - You cannot create appointments outside service availability.

    - `allow_booking_outside_businesshours` (boolean) **REQ** — Denotes if you can create appointments outside business hours. You can configure this preference only when **allow_booking_outside_service_availability:true**.
Possible values:
**true** - You can create appointments outside business hours.
**false** - You cannot create appointments outside business hours.

    - `sharing_enabled` (boolean) — Set to true to enable sharing of the associated record in appointments with the appointment owner. When set to true, sharing_details must also be provided.
    - `sharing_details` (object) — Sharing configuration for appointment-associated records. Defines the permission level granted to the appointment owner for the associated record. Required when sharing_enabled is set to true.
      - `permission` (string) **REQ** [enum=['read_only', 'read_write', 'full_access']] — The permission level granted to the appointment owner for the associated record.
    - `deal_record_configuration` (object) **REQ** — Specify the configuration for creating Deal records when an appointment is completed, including the layout and field mappings.
      - `layout` (object) **REQ** — Specify the Deals module layout to use when creating deal records from completed appointments.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Specify the unique identifier of the Deals module layout. You can get the ID using the [Get Layouts API](layouts.yaml#$.paths./settings/layouts.get).
        - `name` (string) [maxLen=50] — Specify the name of the Deals module layout.
      - `field_mappings` (array of object) [maxItems=100] **REQ** — Specify the field mappings that define how appointment and service data populates the Deals module fields when a deal is created.
        - `type` (string) **REQ** [enum=['static', 'merge_field']] — Specify the type of field mapping to use.
Possible values:
**static** - Set a fixed value for the deal field regardless of appointment data.
**merge_field** - Map the deal field value from appointment or service module data.

        - `value` (object) **REQ** — Denotes the value of the Deals fields. The format of this key's value depends on the mapping **type**.

**Value for merge_field**: The datatype of this value is a string. To merge any field from a module, it should be specified like this **${module_api_name.field_api_name}**.
Example: ${Appointments__s.Appointment_Name}

**Value for static**: The datatype of this value is a JSON object. It contains the name and ID of the entity.

When you want to give static values that look up to a different module, make a GET API call of the specific module and provide the relevant ID and name of the record. You can also give standard text values enclosed in a string.

          oneOf:
              type: string [maxLen=1000] — Specify a merge-field expression that references appointment or service module data using the format **${!module_api_name.field_api_name}**.
              additionalProperties: any
        - `field` (object) **REQ** — Specify the Deals module field to which the appointment data is mapped. Use the [Get Fields API](fields.yaml#$.paths./settings/fields.get) call to fetch the API name and ID of the field. 
          - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — Provide the API name of the Deals module field.
          - `id` (string/int64) **REQ** — Provide the Unique ID of the Deals module field. Use the [Get Fields API](fields.yaml$#.paths./settings/fields.get) to get the valid API name and ID of the field.

**Responses:**

- **200**: Returns the status confirmation after successfully updating the appointment preferences. [application/json]
    > Returns the status information confirming the outcome of the appointment preferences update.
    - `appointment_preferences` (object) **REQ** — Represents the response details confirming the outcome of the update operation. 
      - `status` (string) **REQ** [enum=['success']] — Indicates whether the appointment preferences update was successful. 
Possible values:
**success** - The appointment preferences were updated successfully.

      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the response code for the update operation. 
Possible values:
**SUCCESS** - The appointment preferences were updated successfully.

      - `message` (string) **REQ** [enum=['Appointments preferences updated successfully']] — Represents the success message for the update operation. 
Possible values:
**Appointments preferences updated successfully**

      - `details` (object) **REQ** — Represents additional metadata about the update operation. 

- **400**: The request contains missing mandatory fields or invalid data.
**Resolution:** The request body must include all required fields with valid values. Refer to the details key in the error response for the specific field and JSON path.
 [application/json]
    > Returns the error details when the appointment preferences update request is invalid or incomplete.
    - `appointment_preferences` (object) **REQ** — Represents the error details returned when the appointment preference update fails validation. 
      oneOf:
          - `status` (string) [enum=['error']] — Indicates the outcome of the request.
Possible values:
**error** - The request failed due to a validation error.

          - `code` (string) [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned when a required field is missing from the request.
Possible values:
**MANDATORY_NOT_FOUND** - A required field is absent from the request body.

          - `message` (string) [maxLen=1000] — Represents the error message describing the missing mandatory field.
          - `details` (object) — Represents the details identifying the missing mandatory field, including its API name and JSON path.
            - `api_name` (string) [maxLen=100] — Represents the API name of the missing mandatory field.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path to the missing mandatory field in the request body.
          - `status` (string) [enum=['error']] — Indicates the outcome of the request.
Possible values:
**error** - The request failed due to invalid data.

          - `code` (string) [enum=['INVALID_DATA']] — Represents the error code returned when an invalid value is provided in the request.
Possible values:
**INVALID_DATA** - The request contains a field with an invalid value or unsupported data type.

          - `message` (string) [maxLen=1000] — Represents the error message describing the invalid data issue.
          - `details` (object) — Represents the details identifying the field with invalid data, including the expected data type and JSON path.
            - `expected_data_type` (string) [maxLen=255] — Represents the expected data type for the field that received invalid data.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field that contains invalid data.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field with invalid data in the request body.
          - `status` (string) [enum=['error']] — Indicates the outcome of the request.
Possible values:
**error** - The request failed due to a dependent field mismatch.

          - `code` (string) [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when a field value conflicts with the value of a dependent field.
Possible values:
**DEPENDENT_MISMATCH** - The submitted value for a field is incompatible with the current value of a field it depends on.

          - `message` (string) [maxLen=1000] — Represents the error message describing the dependent field conflict.
          - `details` (object) — Represents the details identifying the field with the conflicting value and the dependee field, including their API names and JSON paths.
            - `dependee` (object) — Represents the details of the dependee field whose value conflicts with the submitted request.
              - `api_name` (string) [maxLen=100] — Represents the API name of the dependee field.
              - `json_path` (string) [maxLen=1000] — Represents the JSON path to the dependee field in the request body.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field with the conflicting value.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field with the conflicting value in the request body.
          - `status` (string) [enum=['error']] — Indicates the outcome of the request.
Possible values:
**error** - The request failed due to a missing dependent field.

          - `code` (string) [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code returned when a required dependent field is absent from the request.
Possible values:
**DEPENDENT_FIELD_MISSING** - A field that depends on another field being present is missing from the request body.

          - `message` (string) [maxLen=1000] — Represents the error message describing the missing dependent field.
          - `details` (object) — Represents the details identifying the missing dependent field and the dependee field that requires it.
            - `dependee` (object) — Represents the details of the dependee field whose presence requires the missing dependent field.
              - `api_name` (string) [maxLen=100] — Represents the API name of the dependee field.
              - `json_path` (string) [maxLen=1000] — Represents the JSON path to the dependee field in the request body.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field that is missing from the request.
            - `json_path` (string) [maxLen=1000] — Represents the JSON path to the missing dependent field in the request body.

**Scopes:** ZohoCRM.settings.modules.UPDATE

# PUT /Services__s/{id}
**Operation:** `updateServiceSById` — Update a specific service record by ID
> To update a single service record in your Zoho CRM organization, identified by its unique ID. Only the fields supplied in the request payload are modified on the targeted service.

**Parameters:**
- `affected_data` (query, boolean, optional) [enum=[True]] {style=form, explode=True}: Specify whether to include the affected_data details in the response. Set to true to receive the IDs of records whose process flows were affected by the update.
- `id` (path, string, required) [maxLen=100] {style=simple, explode=False}: Specify the unique ID of the service record to be retrieved, updated, or deleted.

**Schemas:**
`ActiveServicesLimitExceededError`:
  > Error response returned when the request exceeds the maximum number of active services.
  - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Error response returned when the module name in the request URL is invalid or a required query parameter is missing from the request. Contains one of: `InvalidModuleNameError` or `RequiredParamMissingError`.

  - `details` (object) **REQ** — Represents the details providing additional context about the active services limit violation.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `limit` (integer/int32) **REQ** — Represents the maximum number of active services permitted for the organization.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
  - `message` (string) **REQ** [enum=['You cannot create more than 500 active services']] — Represents the error message describing the active services limit violation.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response, indicating that an error occurred.
`AvailableDatesInHolidayOrNonBusinessDayError`:
  > Error response returned when an Available_Dates entry falls on a holiday or a non-business day.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when available dates fall on a holiday or non-business day.
  - `details` (object) **REQ** — Represents the details providing additional context about the invalid availability date configuration.
    - `dependee` (object) **REQ** — Represents the dependent field for which the validation failed.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
  - `message` (string) **REQ** [enum=['Available Dates value in holiday or Not in BusinessDays']] — Represents the error message describing that the available dates fall on a holiday or outside business days.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response, indicating that an error occurred.
`AvailableDaysNotInBusinessDaysError`:
  > Error response returned when the Available_Days list contains a day that is not configured as a business day.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when the available days are not within the configured business days.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `dependee` (object) **REQ** — Represents the dependent field for which the validation failed.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
  - `message` (string) **REQ** [enum=['The given Available Days are not there in business days']] — Represents the error message describing that the given available days are not within the configured business days.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response, indicating that an error occurred.
`AvailableStatusUnavailableFromFutureError`:
  > Error response returned when the service Status is Available but Unavailable_From key's value is not later than the current date.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when the Unavailable From date does not meet the required future date condition while the service status is available.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `dependee` (object) **REQ** — Represents the dependent field for which the validation failed.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
  - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing that the Unavailable From date must be greater than the current date when the service status is available.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response, indicating that an error occurred.
`AvailableStatusUnavailableWindowRuleError`:
  > Error response returned when the service status is Available, but the values specified for the unavailable period are invalid. When the service status is Available, both Unavailable_From and Unavailable_Till must be null, or only Unavailable_From may be specified.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when the unavailability window configuration violates the required rule while the service status is available.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `dependee` (object) **REQ** — Represents the dependent field for which the validation failed.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
  - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing that when the service status is available, either both Unavailable From and Unavailable Till must be null, or only Unavailable From can have a value.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response, indicating that an error occurred.
`DependentFieldMissingError`:
  > Error response returned when a dependent service field required for the current Status or Availability_Type is missing.
  - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['Dependent Field missing']] — Represents the error message describing that a dependent field required by the submitted field is missing from the request.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`DuplicateDataError`:
  > Error response returned when a service field is set to a value that duplicates an existing record.
  - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `api_name` (string) [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
    - `duplicate_record` (object) — Represents the existing record that duplicates the requested value.
    - `more_records` (object) — Indicates whether additional duplicate records exist beyond the one reported.
    additionalProperties: any
  - `message` (string) **REQ** [enum=['Data is duplicate', 'duplicate data']] — Represents the error message describing that the request contains duplicate data for an existing record.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`DurationNotSatisfyServiceTimingError`:
  > Error response returned when the service Duration does not fit within the configured availability timing.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['Duration does not satisfy the service timing']] — Represents the error message describing that the service duration does not satisfy the configured service timing requirements.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`InvalidAvailabilityTypeNotInPicklistError`:
  > Error response returned when the Availability_Type value is not one of the supported picklist options.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['The given Availability Type is not in picklist']] — Represents the error message describing that the provided availability type value is not a valid picklist option.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`InvalidCustomTimeError`:
  > Error response returned when a custom time provided in the service availability timings is invalid.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=[' The given custom time is invalid']] — Represents the error message for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`InvalidDataForFieldError`:
  > Error response returned when the value provided for a service field does not satisfy its field-level validation requirements.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `maximum_length` (integer/int32) — Represents the maximum length permitted for the offending field.
    - `limit` (integer/int32) — Represents the limit that the request exceeded.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=[4 values]] — Represents the error message for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`InvalidDataGenericError`:
  > Error response returned when a service field carries data that does not pass validation.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type expected for the invalid field.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`InvalidDataTypeGenericError`:
  > Error response returned when a service field is set to a value of the incorrect data type.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type expected for the invalid field.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`InvalidDurationRangeError`:
  > Error response returned when the service Duration is greater than 24 hours or less than 5 minutes.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['Duration value should not be greater than 24hrs or less than 5mins']] — Represents the error message for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`InvalidRequestPayloadError`:
  > Error response returned when the request body for a service update is invalid or fails payload-level validation.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
    - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of values supported for the offending field.
      items: [maxLen=255]
  - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`JobSheetNotConfiguredError`:
  > Error response returned when Job Sheet has not been enabled in the Services preferences and a job sheet field is provided.
  - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['Job Sheet is not configured in services preferences']] — Represents the error message for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`JobSheetSectionDependentMismatchError`:
  > Error response returned when Job_Sheet_Section__s is provided but Job_Sheet_Required is not set to Yes.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details block providing validation context for the error.
    - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing that the job sheet section depends on a field value that does not match the submitted configuration.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`MandatoryFieldMissingError`:
  > Error response returned when a required service field is missing from the request payload.
  - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message describing that a mandatory field is missing from the request.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`MembersAssociationLimitExceededError`:
  > Error response returned when more than 100 users are associated with a single service.
  - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `limit` (integer/int32) **REQ** — Represents the limit that the request exceeded.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['More than 100 users cannot be associated']] — Represents the error message describing that the number of member associations exceeds the allowed limit.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`MembersNotActiveError`:
  > Error response returned when one of the users provided in the Members array is inactive.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `user_status` (string) **REQ** [maxLen=255] — Represents the current status of the referenced user (for example, inactive or unconfirmed).
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['Members is not Active']] — Represents the error message describing that one or more referenced members are not active.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`MembersNotConfirmedError`:
  > Error response returned when one of the users provided in the Members array has not confirmed their CRM account.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `user_status` (string) **REQ** [maxLen=255] — Represents the current status of the referenced user (for example, inactive or unconfirmed).
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['Members is not Confirmed']] — Represents the error message describing that one or more referenced members have not confirmed their membership.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`NotInUseStatusWithFutureUnavailableFromError`:
  > Error response returned when the service Status is Not In Use but Unavailable_From is later than the current date.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing that the service cannot have a future Unavailable From date when the status is Not in Use.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`OwnerBase`:
  > Base schema for the service owner. Identifies the user who owns the service record by name, ID, and email. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
  - `name` (string) [maxLen=100, enum=['Madeshwaran G'], nullable] — Specify the display name of the user who owns the service record.
  - `id` (string) [maxLen=100, enum=['4671651000000635001'], nullable] — Specify the unique ID of the user who owns the service record. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
  - `email` (string) [maxLen=100, enum=['madeshwaran.g@zohocorp.com'], nullable] — Specify the email address of the user who owns the service record.
  additionalProperties: any
`PastEndDateStatusConflictError`:
  > Error response returned when Available_Till is earlier than the current date and the service Status is being set to Available, Scheduled, or Temporarily Unavailable.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing that the service status cannot be changed because the end date has already passed.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`RecordLockedError`:
  > Error response returned when the requested service record is locked and cannot be updated.
  - `code` (string) **REQ** [enum=['RECORD_LOCKED']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details block providing validation context for the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `action` (string) **REQ** [maxLen=255] — Represents the action that was attempted on the locked record.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['Sorry, you cannot perform this operation as the record is locked.']] — Represents the error message describing that the service record is locked and cannot be modified.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`RequiredFieldNotFoundError`:
  > Error response returned when a required service field cannot be located in the request payload.
  - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message describing that a required field was not found in the request.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`ScheduledServiceStatusRestrictionError`:
  > Error response returned when a scheduled service is being marked as Not In Use or Temporarily Unavailable, which is not permitted.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=[2 values]] — Represents the error message describing that the service status cannot be changed because the service has a scheduled appointment.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`ScheduledStatusPastStartDateError`:
  > Error response returned when the service Status is Scheduled but Available_From is earlier than the current date.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing that the service cannot be set to Scheduled status because the start date has already passed.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`ServiceAvailabilityInvalidStatusChangeError`:
  > Error response returned when the requested Status change is rejected because the service availability configuration is not valid.
  - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['As service availability is not valid, status cannot be changed']] — Represents the error message describing that the requested service status change is not allowed.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`ServiceTimeNotInBusinessTimingError`:
  > Error response returned when the service availability timing falls outside the configured business hours.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['Service available time does not satisfy the business timing']] — Represents the error message describing that the specified service time falls outside the configured business hours.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`ServiceUnavailableTillFutureError`:
  > Error response returned when Unavailable_Till is not greater than the current time during a service update.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=[2 values]] — Represents the error message describing that the Unavailable Till date must be in the future.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`ToValueMustBeGreaterThanFromError`:
  > Error response returned when an Available_Till date is not greater than the corresponding Available_From date.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['To value must be Greater than From value']] — Represents the error message describing that the To value must be greater than the From value.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`UnavailableFromTimeOutsideAvailabilityError`:
  > Error response returned when Unavailable_From does not fall within the service availability window.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['Unavailable From time does not fall within service availability']] — Represents the error message describing that the Unavailable From time falls outside the service availability window.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`UnavailableTillTimeOutsideAvailabilityError`:
  > Error response returned when Unavailable_Till does not fall within the service availability window.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['Unavailable Till time does not fall within service availability']] — Represents the error message for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
`UnavailableWindowOrderError`:
  > Error response returned when Unavailable_Till is not earlier than Unavailable_From.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
  - `details` (object) **REQ** — Represents the details providing validation context for the error.
    - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
      - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
  - `message` (string) **REQ** [enum=['Unavailable Till must be lesser than Unavailable From']] — Represents the error message for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 

**Request Body** — application/json `PutservicessRequest`
> The request body must contain a data array with one object representing the service record to update.
  > Request body schema for updating a single service. Contains a data array with exactly one service object that carries the fields to be updated.
  - `data` (array of object `DataNestedV2`) [minItems=1, maxItems=1] **REQ** — Specify the array containing the single service object to be updated.
    schema: `DataNestedV2`
    - `Job_Sheet_Required` (string) [maxLen=3, enum=['Yes', 'No'], nullable] — Specify whether a job sheet is required for the service. 

**Possible values**: Yes, No.

    - `Status` (string) [maxLen=100, enum=['Available', 'Temporarily Unavailable', 'Not in Use', 'Scheduled'], nullable] — Specify the operational status of the service. 


**Possible values**: 

- Available - service is active and accepting bookings.

- Not in Use - service is currently inactive.

- Scheduled - service is queued to become Available on
Available_From.

- Temporarily Unavailable - service is paused for the
Unavailable_From-to-Unavailable_Till window.

    - `Owner` (object `OwnerNestedV2`) — Service owner schema used in update requests, where the email of the owner is required.
      schema: `OwnerNestedV2`
      - `name` (string) [maxLen=100, enum=['Madeshwaran G'], nullable] — Specify the display name of the user who owns the service record.
      - `id` (string) [maxLen=100, enum=['4671651000000635001'], nullable] — Specify the unique ID of the user who owns the service record. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
      - `email` (string) **REQ** [maxLen=100, enum=['madeshwaran.g@zohocorp.com'], nullable] — Specify the email address of the user who owns the service record.
      additionalProperties: any
    - `Description` (string) [maxLen=32000, nullable] — Specify a description of the service.
    - `Available_Timings` (string) [maxLen=4, nullable] — Specify the available time windows for the service. The total available time must be at least equal to the service Duration.
    - `Service_Name` (string) [maxLen=120, nullable] — Specify the name of the service.
    - `Available_From` (string) [maxLen=100, nullable] — Specify the date from which the service is available, in YYYY-MM-DD format. The key is mandatory when Availability_Type is Specific Date Range.
    - `Available_Till` (string) [maxLen=100, enum=['2026-01-13', '2026-01-29'], nullable] — Specify the date until which the service is available, in YYYY-MM-DD format. The key is mandatory when Availability_Type is Specific Date Range.
    - `Available_Days` (array of string) [maxItems=7, nullable] — Specify the list of business days on which the service is available. The key is mandatory when Availability_Type is Specific Day(s).
      items: [maxLen=255]
    - `Tax` (array of string) [maxItems=2, nullable] — Specify the taxes applied to the service cost.
      items: [maxLen=255]
    - `Duration` (integer/int32) [nullable] — Specify the duration of the service, in minutes. Must be greater than 5 minutes and less than 24 hours.
    - `Job_Sheet_Section__s` (string) [maxLen=255, nullable] — Specify the job sheet section associated with the service. It can be set only when Job_Sheet_Required is Yes.
    - `Unavailable_From` (string) [maxLen=25, nullable] — Specify the date and time from which the service becomes unavailable. Must fall within the service availability window.
    - `Record_Image` (string) [maxLen=255, nullable] — Specify the record image to associate with the service.
    - `Price` (integer/int32) [nullable] — Specify the price charged for the service in the organization currency.
    - `id` (string) [maxLen=100, nullable] — Specify the unique ID of the service record being updated.
    - `Tag` (array of string) [maxItems=100, nullable] — Specify the tag names to associate with the service record. Refer to the [Get tags](tags.yaml#$.paths./settings/tags.get) resource for valid values.
      items: [maxLen=2000]
    - `Availability_Type` (string) [maxLen=19, enum=[4 values], nullable] — Specify how the service availability is defined. 


**Possible values**:  Specific Day(s), Specific Date Range, Every
Business Days, Specific Date(s).

    - `Available_Dates` (array of string) [maxItems=20, nullable] — Specify the list of dates on which the service is available. The key is mandatory when Availability_Type is Specific Date(s).
      items: [maxLen=255]
    - `Members` (array of object `MembersitemBase`) [maxItems=100, nullable] — Specify the users who deliver the service. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
      schema: `MembersitemBase`
      - `id` (string) [maxLen=100, nullable] — Specify the unique relationship ID of the member entry on the service record.
      - `Members` (object `MembersBase`) — Base schema for a member of the service. Identifies the user by module, name, and ID. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
        schema: `MembersBase`
        - `module` (string) [maxLen=100, nullable] — Specify the source module of the member. Typically set to the module Users.
        - `name` (string) [maxLen=100, enum=['Madeshwaran G'], nullable] — Specify the display name of the user who delivers the service.
        - `id` (string) [maxLen=100, enum=['4671651000000635001'], nullable] — Specify the unique ID of the user who delivers the service. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
        additionalProperties: any
      additionalProperties: any
    - `Location` (string) [maxLen=1000, enum=['Business Address', 'Business Address and Client Address', 'Client Address'], nullable] — Specify where the service is delivered. 

**Possible values**: Client Address, Business Address, Business
Address and Client Address.

    - `Unavailable_Till` (string) [maxLen=255, nullable] — Specify the date and time until which the service remains unavailable. Must fall within the service availability window.
    additionalProperties: any

**Responses:**

- **200**: Returns a success status with the updated service record's ID, audit metadata (creation and modification timestamps and users), and the affected_data block reflecting the applied changes. — Schema: `PutServiceByIdResponse200` [application/json]
    > Wrapped response for a single service update request. Contains a data array with one status object carrying the success code, persisted ID, audit metadata, and affected_data block.
    schema: `PutServiceByIdResponse200`
    - `data` (array of object `DataNested1`) [minItems=1, maxItems=1] — Represents the per-record status array containing the result for the updated service record.
      schema: `DataNested1`
      - `code` (string) [maxLen=255] — Represents the operation result code for the service record. 
      - `details` (object `DetailsNested`) — Represents the details as a per-record status item. Carries audit metadata (Modified_Time, Modified_By, Created_Time, Created_By) and the persisted record ID.
        schema: `DetailsNested`
        - `Modified_Time` (string) [maxLen=255] — Represents the timestamp when the service record was last modified.
        - `Modified_By` (object `ModifiedByNested`) — Represents the user who last modified the service record, identified by name and ID. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
          schema: `ModifiedByNested`
          - `name` (string) [maxLen=255] — Represents the display name of the user who modified the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
          - `id` (string) [maxLen=255] — Represents the unique ID of the user who modified the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        - `Created_Time` (string) [maxLen=255] — Represents the timestamp when the service record was first saved to the organization.
        - `id` (string) [maxLen=255] — Represents the unique ID of the affected service record.
        - `Created_By` (object `CreatedByNested`) — Represents the user who created the service record, identified by name and ID. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
          schema: `CreatedByNested`
          - `name` (string) [maxLen=255] — Represents the display name of the user who created the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
          - `id` (string) [maxLen=255] — Represents the unique ID of the user who created the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        additionalProperties: any
      - `message` (string) [maxLen=255] — Represents the result message for the operation result.
      - `status` (string) [maxLen=255] — Represents the status of the operation. 

- **400**: The request could not be processed because the service record contains invalid field values, is missing a required dependent field, violates a service-availability constraint, or has exceeded the active service limit.

**Resolution:** The error response identifies the offending field and error code; correct the corresponding values in the request payload and resubmit the request. [application/json]
    > Represents the bad-request error response for the Update Service by ID endpoint, returned when the request payload or query parameters fail validation.
    oneOf:
      - `DataError` — Standard error response object returned when a request fails. Contains the error code, the message, the status, and a details block identifying the offending field.
        - `code` (string) **REQ** [maxLen=255] — Represents the error code returned when a data validation error occurs.
        - `details` (object) **REQ** — Represents the details providing validation context for the error.
          - `api_name` (string) [maxLen=255] — Represents the API name of the field that triggered the error.
          - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that triggered the error.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message returned when the request fails.
        - `status` (string) **REQ** [maxLen=1000] — Represents the status of the response, indicating that an error occurred.
        additionalProperties: any
        - `data` (array of object) [maxItems=25] **REQ** — Represents the per-record error array returned for each failed service record in the request.
          oneOf:
            - `InvalidDataTypeGenericError` — Error response returned when a service field is set to a value of the incorrect data type.
            - `InvalidDataForFieldError` — Error response returned when the value provided for a service field does not satisfy its field-level validation requirements.
            - `DuplicateDataError` — Error response returned when a service field is set to a value that duplicates an existing record.
            - `RecordLockedError` — Error response returned when the requested service record is locked and cannot be updated.
            - `AvailableDaysNotInBusinessDaysError` — Error response returned when the Available_Days list contains a day that is not configured as a business day.
            - `ServiceTimeNotInBusinessTimingError` — Error response returned when the service availability timing falls outside the configured business hours.
            - `InvalidDataGenericError` — Error response returned when a service field carries data that does not pass validation.
            - `DurationNotSatisfyServiceTimingError` — Error response returned when the service Duration does not fit within the configured availability timing.
            - `DependentFieldMissingError` — Error response returned when a dependent service field required for the current Status or Availability_Type is missing.
            - `MembersAssociationLimitExceededError` — Error response returned when more than 100 users are associated with a single service.
            - `ActiveServicesLimitExceededError` — Error response returned when the request exceeds the maximum number of active services.
            - `JobSheetSectionDependentMismatchError` — Error response returned when Job_Sheet_Section__s is provided but Job_Sheet_Required is not set to Yes.
            - `ToValueMustBeGreaterThanFromError` — Error response returned when an Available_Till date is not greater than the corresponding Available_From date.
            - `AvailableDatesInHolidayOrNonBusinessDayError` — Error response returned when an Available_Dates entry falls on a holiday or a non-business day.
            - `MembersNotConfirmedError` — Error response returned when one of the users provided in the Members array has not confirmed their CRM account.
            - `MembersNotActiveError` — Error response returned when one of the users provided in the Members array is inactive.
            - `AvailableStatusUnavailableFromFutureError` — Error response returned when the service Status is Available but Unavailable_From key's value is not later than the current date.
            - `ScheduledServiceStatusRestrictionError` — Error response returned when a scheduled service is being marked as Not In Use or Temporarily Unavailable, which is not permitted.
            - `NotInUseStatusWithFutureUnavailableFromError` — Error response returned when the service Status is Not In Use but Unavailable_From is later than the current date.
            - `ScheduledStatusPastStartDateError` — Error response returned when the service Status is Scheduled but Available_From is earlier than the current date.
            - `PastEndDateStatusConflictError` — Error response returned when Available_Till is earlier than the current date and the service Status is being set to Available, Scheduled, or Temporarily Unavailable.
            - `UnavailableFromTimeOutsideAvailabilityError` — Error response returned when Unavailable_From does not fall within the service availability window.
            - `UnavailableTillTimeOutsideAvailabilityError` — Error response returned when Unavailable_Till does not fall within the service availability window.
            - `InvalidRequestPayloadError` — Error response returned when the request body for a service update is invalid or fails payload-level validation.
            - `InvalidDurationRangeError` — Error response returned when the service Duration is greater than 24 hours or less than 5 minutes.
            - `JobSheetNotConfiguredError` — Error response returned when Job Sheet has not been enabled in the Services preferences and a job sheet field is provided.
            - `ServiceAvailabilityInvalidStatusChangeError` — Error response returned when the requested Status change is rejected because the service availability configuration is not valid.
            - `InvalidAvailabilityTypeNotInPicklistError` — Error response returned when the Availability_Type value is not one of the supported picklist options.
            - `MandatoryFieldMissingError` — Error response returned when a required service field is missing from the request payload.
            - `ServiceUnavailableTillFutureError` — Error response returned when Unavailable_Till is not greater than the current time during a service update.
            - `AvailableStatusUnavailableWindowRuleError` — Error response returned when the service status is Available, but the values specified for the unavailable period are invalid. When the service status is Available, both Unavailable_From and Unavailable_Till must be null, or only Unavailable_From may be specified.
            - `UnavailableWindowOrderError` — Error response returned when Unavailable_Till is not earlier than Unavailable_From.
            - `RequiredFieldNotFoundError` — Error response returned when a required service field cannot be located in the request payload.
            - `InvalidCustomTimeError` — Error response returned when a custom time provided in the service availability timings is invalid.
      - `InvalidDataTypeForDataFieldError` — Error response returned when the value provided for the data field has an invalid data type.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
        - `details` (object) **REQ** — Represents the details providing validation context for the error.
          - `maximum_length` (integer/int32) **REQ** — Represents the maximum length permitted for the offending field.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
          - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message for the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 

- **403**: The authenticated user does not have permission to update the service record, the Job Sheet preference has not been configured in service settings, or the service's availability dates are in the past.

**Resolution:** For permission errors, the user should contact the system administrator to obtain the required access. For Job Sheet errors, the administrator must enable the Job Sheet preference in service settings. For past-dated availability errors, the service's availability dates must be updated before marking the service as available or temporarily unavailable. — Schema: `PutservicesByIdError400Wrapper` [application/json]
    > Represents the error response for a single service update request. It contains a data array with one or more error objects describing the validation failures that caused the request to fail.
    schema: `PutservicesByIdError400Wrapper`
    - `data` (array of object) [maxItems=25] **REQ** — Represents the array of error objects, with each entry corresponding to a validation failure encountered during the service update request.
      oneOf:
        - `InvalidDataTypeGenericError` — Error response returned when a service field is set to a value of the incorrect data type.
        - `InvalidDataForFieldError` — Error response returned when the value provided for a service field does not satisfy its field-level validation requirements.
        - `DuplicateDataError` — Error response returned when a service field is set to a value that duplicates an existing record.
        - `RecordLockedError` — Error response returned when the requested service record is locked and cannot be updated.
        - `AvailableDaysNotInBusinessDaysError` — Error response returned when the Available_Days list contains a day that is not configured as a business day.
        - `ServiceTimeNotInBusinessTimingError` — Error response returned when the service availability timing falls outside the configured business hours.
        - `InvalidDataGenericError` — Error response returned when a service field carries data that does not pass validation.
        - `DurationNotSatisfyServiceTimingError` — Error response returned when the service Duration does not fit within the configured availability timing.
        - `DependentFieldMissingError` — Error response returned when a dependent service field required for the current Status or Availability_Type is missing.
        - `MembersAssociationLimitExceededError` — Error response returned when more than 100 users are associated with a single service.
        - `ActiveServicesLimitExceededError` — Error response returned when the request exceeds the maximum number of active services.
        - `JobSheetSectionDependentMismatchError` — Error response returned when Job_Sheet_Section__s is provided but Job_Sheet_Required is not set to Yes.
        - `ToValueMustBeGreaterThanFromError` — Error response returned when an Available_Till date is not greater than the corresponding Available_From date.
        - `AvailableDatesInHolidayOrNonBusinessDayError` — Error response returned when an Available_Dates entry falls on a holiday or a non-business day.
        - `MembersNotConfirmedError` — Error response returned when one of the users provided in the Members array has not confirmed their CRM account.
        - `MembersNotActiveError` — Error response returned when one of the users provided in the Members array is inactive.
        - `AvailableStatusUnavailableFromFutureError` — Error response returned when the service Status is Available but Unavailable_From key's value is not later than the current date.
        - `ScheduledServiceStatusRestrictionError` — Error response returned when a scheduled service is being marked as Not In Use or Temporarily Unavailable, which is not permitted.
        - `NotInUseStatusWithFutureUnavailableFromError` — Error response returned when the service Status is Not In Use but Unavailable_From is later than the current date.
        - `ScheduledStatusPastStartDateError` — Error response returned when the service Status is Scheduled but Available_From is earlier than the current date.
        - `PastEndDateStatusConflictError` — Error response returned when Available_Till is earlier than the current date and the service Status is being set to Available, Scheduled, or Temporarily Unavailable.
        - `UnavailableFromTimeOutsideAvailabilityError` — Error response returned when Unavailable_From does not fall within the service availability window.
        - `UnavailableTillTimeOutsideAvailabilityError` — Error response returned when Unavailable_Till does not fall within the service availability window.
        - `InvalidRequestPayloadError` — Error response returned when the request body for a service update is invalid or fails payload-level validation.
        - `InvalidDurationRangeError` — Error response returned when the service Duration is greater than 24 hours or less than 5 minutes.
        - `JobSheetNotConfiguredError` — Error response returned when Job Sheet has not been enabled in the Services preferences and a job sheet field is provided.
        - `ServiceAvailabilityInvalidStatusChangeError` — Error response returned when the requested Status change is rejected because the service availability configuration is not valid.
        - `InvalidAvailabilityTypeNotInPicklistError` — Error response returned when the Availability_Type value is not one of the supported picklist options.
        - `MandatoryFieldMissingError` — Error response returned when a required service field is missing from the request payload.
        - `ServiceUnavailableTillFutureError` — Error response returned when Unavailable_Till is not greater than the current time during a service update.
        - `AvailableStatusUnavailableWindowRuleError` — Error response returned when the service status is Available, but the values specified for the unavailable period are invalid. When the service status is Available, both Unavailable_From and Unavailable_Till must be null, or only Unavailable_From may be specified.
        - `UnavailableWindowOrderError` — Error response returned when Unavailable_Till is not earlier than Unavailable_From.
        - `RequiredFieldNotFoundError` — Error response returned when a required service field cannot be located in the request payload.
        - `InvalidCustomTimeError` — Error response returned when a custom time provided in the service availability timings is invalid.

**Scopes:** ZohoCRM.modules.services.UPDATE

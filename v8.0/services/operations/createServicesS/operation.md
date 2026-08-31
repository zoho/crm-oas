# POST /Services__s
**Operation:** `createServicesS` — Create service records in Zoho CRM
> To create one or more service records in your Zoho CRM organization, submitting up to 100 service objects per request, each configurable with a name, duration, price, location, members, availability type, and availability window.

**Schemas:**
`CreatedByNested`:
  > Represents the user who created the service record, identified by name and ID. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
  - `name` (string) [maxLen=255] — Represents the display name of the user who created the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
  - `id` (string) [maxLen=255] — Represents the unique ID of the user who created the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
`DetailsNested`:
  > Represents the details as a per-record status item. Carries audit metadata (Modified_Time, Modified_By, Created_Time, Created_By) and the persisted record ID.
  - `Modified_Time` (string) [maxLen=255] — Represents the timestamp when the service record was last modified.
  - `Modified_By` (object `ModifiedByNested`) — Represents the user who last modified the service record, identified by name and ID. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
  - `Created_Time` (string) [maxLen=255] — Represents the timestamp when the service record was first saved to the organization.
  - `id` (string) [maxLen=255] — Represents the unique ID of the affected service record.
  - `Created_By` (object `CreatedByNested`) — Represents the user who created the service record, identified by name and ID. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
  additionalProperties: any
`MembersNested`:
  > Represents a member who delivers the service. Identifies the user by name and ID. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
  - `name` (string) [maxLen=120, nullable] — Specify the display name of the user who delivers the service.
  - `Members` (object `MembersNested`) — contains member details
  - `id` (string) [maxLen=18, nullable] — Specify the unique ID of the user who delivers the service. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
`ModifiedByNested`:
  > Represents the user who last modified the service record, identified by name and ID. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
  - `name` (string) [maxLen=255] — Represents the display name of the user who modified the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
  - `id` (string) [maxLen=255] — Represents the unique ID of the user who modified the service record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.

**Request Body** — application/json `PostservicessRequest`
> The request body must contain a data array. You can include a maximum of 100 objects per request.
  > Request body schema for creating services. Contains a data array of service objects to be created and an optional skip_mandatory flag.
  - `data` (array of object `DataNested`) [minItems=1, maxItems=100] **REQ** — Specify the array of service objects to be created. You can include up to 100 objects.
    schema: `DataNested`
    - `Job_Sheet_Required` (string) [maxLen=3, enum=['Yes', 'No'], nullable] — Specify whether a job sheet is required for the service. **Possible values**: Yes, No.

    - `Owner` (object `OwnerNested`) — owner of the service
      schema: `OwnerNested`
      - `full_name` (string) [maxLen=120, nullable] — Specify the full name of the user who owns the service record.
      - `name` (string) [maxLen=120, nullable] — Specify the display name of the user who owns the service record.
      - `id` (string) [maxLen=18, nullable] — Specify the unique ID of the user who owns the service record. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
    - `Available_Timings` (array of object `AvailableTimingsNested`) [maxItems=4, nullable] — Specify the available time windows for the service on each available day or date. The total available time must be at least equal to the service Duration. If not mentioned, the configured business hours are used.
      schema: `AvailableTimingsNested`
      - `From` (string) [maxLen=5, nullable] — Specify the start of the availability time window in HH:MM (24-hour) format.
      - `To` (string) [maxLen=5, nullable] — Specify the end of the availability time window in HH:MM (24-hour) format.
    - `Description` (string) [maxLen=32000, nullable] — Specify a description of the service.
    - `Available_From` (string/date) [maxLen=100, nullable] — Specify the date from which the service is available, in YYYY-MM-DD format. The key is mandatory when Availability_Type is Specific Date Range.
    - `Service_Name` (string) **REQ** [maxLen=120] — Specify the name of the service. The key accepts alphanumeric characters.
    - `Available_Till` (string/date) [maxLen=100, nullable] — Specify the date until which the service is available, in YYYY-MM-DD format. The key is mandatory when Availability_Type is Specific Date Range.
    - `Available_Days` (array of string) [maxItems=7, nullable] — Specify the list of business days on which the service is available. This key is mandatory when Availability_Type is Specific Day(s).
      items: [maxLen=225]
    - `Duration` (integer/int32) **REQ** — Specify the duration of the service, in minutes. Must be greater than 5 minutes and less than 24 hours.
    - `Tax` (array of object `TaxNested`) [maxItems=2, nullable] — Specify the taxes applied to the service cost. Each entry carries a tax ID and the tax value label.
      schema: `TaxNested`
      - `id` (null) — Specify the unique ID of the tax applied to the service cost.
      - `value` (string) [maxLen=100, nullable] — Specify the display label of the tax applied to the service cost.
    - `Price` (integer/int32) **REQ** — Specify the price charged for the service in the organization currency, with up to 16 digits and 2 decimal places.
    - `Layout` (object `LayoutNested`) — Layout id
      schema: `LayoutNested`
      - `id` (string) [maxLen=18, nullable] — Specify the unique ID of the layout to use for the service record. Refer to the [Get layouts](layouts.yaml#$.paths./settings/layouts.get) resource for valid values.
    - `zia_suggested_users` (object) [nullable] — Specify the Zia-suggested users payload associated with the service record.
    - `Availability_Type` (string) **REQ** [maxLen=100, enum=[4 values]] — Specify how the service availability is defined. 


**Possible values**: 

- Every Business Days - service is available on every business day.

- Specific Date Range - service is available within an
Available_From and Available_Till range.

- Specific Date(s) - service is available on the dates listed in
Available_Dates.

- Specific Day(s) - service is available on the weekdays listed in
Available_Days.

    - `$zia_owner_assignment` (string) [maxLen=32, nullable] — Specify the Zia owner-assignment recommendation behavior for the service record.
    - `Members` (array of object `MembersNested`) [maxItems=5] **REQ** — Specify the users who deliver the service. Refer to the [Get users](users.yaml#$.paths./users.get) resource for valid values.
    - `Available_Dates` (array of string) [maxItems=20, nullable] — Specify the list of dates on which the service is available, in YYYY-MM-DD format. This key is mandatory when Availability_Type is Specific Date(s).
      items: [maxLen=255]
    - `Location` (string) **REQ** [maxLen=100, enum=['Business Address', 'Business Address and Client Address', 'Client Address']] — Specify where the service is delivered. 


**Possible values**: Client Address, Business Address, Business
Address and Client Address.

  - `skip_mandatory` (boolean) [nullable] — Specify whether to skip mandatory-field validation when creating service records.

**Responses:**

- **201**: Returns a data array confirming the successful creation of each service record. Each item contains the success code, the ID assigned to the created record, and audit metadata including the creation and last-modified timestamps and the users who performed those actions. — Schema: `PostservicessResponse201` [application/json]
    > Wrapped response for a service create request. Contains a per-record status array with the success code, persisted ID, and audit metadata for each service record processed.
    schema: `PostservicessResponse201`
    - `data` (array of object `DataNested1`) [minItems=1, maxItems=100] — Represents the per-record status array, with one entry for each service record processed in the create request.
      schema: `DataNested1`
      - `code` (string) [maxLen=255] — Represents the operation result code for the service record. 
      - `details` (object `DetailsNested`) — Represents the details as a per-record status item. Carries audit metadata (Modified_Time, Modified_By, Created_Time, Created_By) and the persisted record ID.
      - `message` (string) [maxLen=255] — Represents the result message for the operation result.
      - `status` (string) [maxLen=255] — Represents the status of the operation. 

- **207**: Returns a multi-status response when the submitted service records yield mixed outcomes. Each item in the data array independently indicates success or failure for its corresponding record. Successful operation include the created record's ID and audit metadata, while failed items include the error code and a description of the validation failure. [application/json]
    > Represents the multi-status response returned when some service records were created successfully and others encountered errors. Contains a data array with one entry per service record submitted in the request; each entry independently indicates success or failure for its corresponding record.
    - `data` (array of object) [minItems=1, maxItems=100] **REQ** — Contains one entry per service record submitted in the request, indicating success or failure for the corresponding record.
      oneOf:
        - `Post207multistatusResponse207` — Represents a success item in a multi-status response. Carries the success code, message, status, and details for the corresponding service record in the request.
          - `details` (object `DetailsNested`) — Represents the details as a per-record status item. Carries audit metadata (Modified_Time, Modified_By, Created_Time, Created_By) and the persisted record ID.
          - `code` (string) [maxLen=255] — Represents the operation result code for the service record. 
          - `message` (string) [maxLen=255] — Represents the result message for the operation result.
          - `status` (string) [maxLen=255] — Represents the status of the operation. 
        - `MandatoryFieldNotFoundMultiStatusError` — Multi-status error item returned when a service record in a bulk operation is missing a required field.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned for the failed request.
          - `details` (object) **REQ** — Represents the details providing validation context for the error.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
            additionalProperties: any
          - `message` (string) **REQ** [maxLen=100] — Represents the error message describing that a mandatory field was not found in the multi-status request.
          - `status` (string) **REQ** [maxLen=100] — Represents the status of the response. 
          additionalProperties: any

- **400**: The request could not be processed because one or more service records contain invalid data, fail a field-level validation check, or violate a service-availability constraint.

**Resolution:** The caller must inspect each error item to identify the offending field, correct the request payload accordingly, and resubmit the request. [application/json]
    > Represents the bad-request error response returned when the request payload or query parameters fail validation. Contains one of several error structures depending on whether the failure is a top-level data-type error, a per-record validation error, or an invalid value for a data field.
    oneOf:
      - `DataError` — Standard error response object returned when a request fails. Contains the error code, the message, the status, and a details block identifying the offending field.
        - `code` (string) **REQ** [maxLen=255] — Represents the error code returned when a data validation error occurs.
        - `details` (object) **REQ** — Represents the details providing validation context for the error.
          - `api_name` (string) [maxLen=255] — Represents the API name of the field that triggered the error.
          - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that triggered the error.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message returned when the request fails.
        - `status` (string) **REQ** [maxLen=1000] — Represents the status of the response, indicating that an error occurred.
        additionalProperties: any
        - `data` (array of object) [maxItems=25] **REQ** — Contains one error entry for each service record in the request that failed validation, describing the specific reason the record was rejected.
          oneOf:
            - `InvalidDataTypeGenericError` — Error response returned when a service field is set to a value of the incorrect data type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type expected for the invalid field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message for the failure.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `InvalidDataForFieldError` — Error response returned when the value provided for a service field does not satisfy its field-level validation requirements.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `maximum_length` (integer/int32) — Represents the maximum length permitted for the offending field.
                - `limit` (integer/int32) — Represents the limit that the request exceeded.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=[4 values]] — Represents the error message for the failure.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `DuplicateDataError` — Error response returned when a service field is set to a value that duplicates an existing record.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
                - `duplicate_record` (object) — Represents the existing record that duplicates the requested value.
                - `more_records` (object) — Indicates whether additional duplicate records exist beyond the one reported.
                additionalProperties: any
              - `message` (string) **REQ** [enum=['Data is duplicate', 'duplicate data']] — Represents the error message describing that the request contains duplicate data for an existing record.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `MandatoryFieldMissingError` — Error response returned when a required service field is missing from the request payload.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message describing that a mandatory field is missing from the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `AvailableStatusUnavailableFromFutureError` — Error response returned when the service Status is Available but Unavailable_From key's value is not later than the current date.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when the Unavailable From date does not meet the required future date condition while the service status is available.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `dependee` (object) **REQ** — Represents the dependent field for which the validation failed.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing that the Unavailable From date must be greater than the current date when the service status is available.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response, indicating that an error occurred.
            - `ServiceUnavailableTillFutureError` — Error response returned when Unavailable_Till is not greater than the current time during a service update.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=[2 values]] — Represents the error message describing that the Unavailable Till date must be in the future.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `AvailableStatusUnavailableWindowRuleError` — Error response returned when the service status is Available, but the values specified for the unavailable period are invalid. When the service status is Available, both Unavailable_From and Unavailable_Till must be null, or only Unavailable_From may be specified.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when the unavailability window configuration violates the required rule while the service status is available.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `dependee` (object) **REQ** — Represents the dependent field for which the validation failed.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing that when the service status is available, either both Unavailable From and Unavailable Till must be null, or only Unavailable From can have a value.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response, indicating that an error occurred.
            - `UnavailableWindowOrderError` — Error response returned when Unavailable_Till is not earlier than Unavailable_From.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['Unavailable Till must be lesser than Unavailable From']] — Represents the error message for the failure.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `NotInUseStatusWithFutureUnavailableFromError` — Error response returned when the service Status is Not In Use but Unavailable_From is later than the current date.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing that the service cannot have a future Unavailable From date when the status is Not in Use.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `ScheduledStatusPastStartDateError` — Error response returned when the service Status is Scheduled but Available_From is earlier than the current date.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing that the service cannot be set to Scheduled status because the start date has already passed.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `PastEndDateStatusConflictError` — Error response returned when Available_Till is earlier than the current date and the service Status is being set to Available, Scheduled, or Temporarily Unavailable.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing that the service status cannot be changed because the end date has already passed.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `UnavailableFromTimeOutsideAvailabilityError` — Error response returned when Unavailable_From does not fall within the service availability window.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['Unavailable From time does not fall within service availability']] — Represents the error message describing that the Unavailable From time falls outside the service availability window.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `UnavailableTillTimeOutsideAvailabilityError` — Error response returned when Unavailable_Till does not fall within the service availability window.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['Unavailable Till time does not fall within service availability']] — Represents the error message for the failure.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `InvalidRequestPayloadError` — Error response returned when the request body for a service update is invalid or fails payload-level validation.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
                - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of values supported for the offending field.
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message for the failure.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `InvalidAvailabilityTypeNotInPicklistError` — Error response returned when the Availability_Type value is not one of the supported picklist options.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['The given Availability Type is not in picklist']] — Represents the error message describing that the provided availability type value is not a valid picklist option.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `AvailableDaysNotInBusinessDaysError` — Error response returned when the Available_Days list contains a day that is not configured as a business day.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when the available days are not within the configured business days.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `dependee` (object) **REQ** — Represents the dependent field for which the validation failed.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
              - `message` (string) **REQ** [enum=['The given Available Days are not there in business days']] — Represents the error message describing that the given available days are not within the configured business days.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response, indicating that an error occurred.
            - `ServiceTimeNotInBusinessTimingError` — Error response returned when the service availability timing falls outside the configured business hours.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['Service available time does not satisfy the business timing']] — Represents the error message describing that the specified service time falls outside the configured business hours.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `InvalidDataGenericError` — Error response returned when a service field carries data that does not pass validation.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type expected for the invalid field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message for the failure.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `InvalidDurationRangeError` — Error response returned when the service Duration is greater than 24 hours or less than 5 minutes.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['Duration value should not be greater than 24hrs or less than 5mins']] — Represents the error message for the failure.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `JobSheetNotConfiguredError` — Error response returned when Job Sheet has not been enabled in the Services preferences and a job sheet field is provided.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['Job Sheet is not configured in services preferences']] — Represents the error message for the failure.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `DurationNotSatisfyServiceTimingError` — Error response returned when the service Duration does not fit within the configured availability timing.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['Duration does not satisfy the service timing']] — Represents the error message describing that the service duration does not satisfy the configured service timing requirements.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `RequiredFieldNotFoundError` — Error response returned when a required service field cannot be located in the request payload.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message describing that a required field was not found in the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `DependentFieldMissingError` — Error response returned when a dependent service field required for the current Status or Availability_Type is missing.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['Dependent Field missing']] — Represents the error message describing that a dependent field required by the submitted field is missing from the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `MembersAssociationLimitExceededError` — Error response returned when more than 100 users are associated with a single service.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `limit` (integer/int32) **REQ** — Represents the limit that the request exceeded.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['More than 100 users cannot be associated']] — Represents the error message describing that the number of member associations exceeds the allowed limit.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `ActiveServicesLimitExceededError` — Error response returned when the request exceeds the maximum number of active services.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Error response returned when the module name in the request URL is invalid or a required query parameter is missing from the request. Contains one of: `InvalidModuleNameError` or `RequiredParamMissingError`.

              - `details` (object) **REQ** — Represents the details providing additional context about the active services limit violation.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `limit` (integer/int32) **REQ** — Represents the maximum number of active services permitted for the organization.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
              - `message` (string) **REQ** [enum=['You cannot create more than 500 active services']] — Represents the error message describing the active services limit violation.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response, indicating that an error occurred.
            - `JobSheetSectionDependentMismatchError` — Error response returned when Job_Sheet_Section__s is provided but Job_Sheet_Required is not set to Yes.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details block providing validation context for the error.
                - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message describing that the job sheet section depends on a field value that does not match the submitted configuration.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `ToValueMustBeGreaterThanFromError` — Error response returned when an Available_Till date is not greater than the corresponding Available_From date.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['To value must be Greater than From value']] — Represents the error message describing that the To value must be greater than the From value.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `AvailableDatesInHolidayOrNonBusinessDayError` — Error response returned when an Available_Dates entry falls on a holiday or a non-business day.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned when available dates fall on a holiday or non-business day.
              - `details` (object) **REQ** — Represents the details providing additional context about the invalid availability date configuration.
                - `dependee` (object) **REQ** — Represents the dependent field for which the validation failed.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error.
              - `message` (string) **REQ** [enum=['Available Dates value in holiday or Not in BusinessDays']] — Represents the error message describing that the available dates fall on a holiday or outside business days.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response, indicating that an error occurred.
            - `InvalidCustomTimeError` — Error response returned when a custom time provided in the service availability timings is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=[' The given custom time is invalid']] — Represents the error message for the failure.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `MembersNotConfirmedError` — Error response returned when one of the users provided in the Members array has not confirmed their CRM account.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `user_status` (string) **REQ** [maxLen=255] — Represents the current status of the referenced user (for example, inactive or unconfirmed).
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['Members is not Confirmed']] — Represents the error message describing that one or more referenced members have not confirmed their membership.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `MembersNotActiveError` — Error response returned when one of the users provided in the Members array is inactive.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `user_status` (string) **REQ** [maxLen=255] — Represents the current status of the referenced user (for example, inactive or unconfirmed).
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=['Members is not Active']] — Represents the error message describing that one or more referenced members are not active.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
            - `ScheduledServiceStatusRestrictionError` — Error response returned when a scheduled service is being marked as Not In Use or Temporarily Unavailable, which is not permitted.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code returned for the failed request.
              - `details` (object) **REQ** — Represents the details providing validation context for the error.
                - `dependee` (object) **REQ** — Represents the dependent field whose value causes the validation failure.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
              - `message` (string) **REQ** [enum=[2 values]] — Represents the error message describing that the service status cannot be changed because the service has a scheduled appointment.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
      - `InvalidDataTypeForDataFieldError` — Error response returned when the value provided for the data field has an invalid data type.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request.
        - `details` (object) **REQ** — Represents the details providing validation context for the error.
          - `maximum_length` (integer/int32) **REQ** — Represents the maximum length permitted for the offending field.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that triggered the error.
          - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that triggered the error in the request payload.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message for the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 

**Scopes:** ZohoCRM.modules.services.CREATE

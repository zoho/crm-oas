# PUT /settings/service_preferences
**Operation:** `updateServicePreference` — Update service preferences
> Updates the service preference settings of the organization. Use this API to enable or disable the job sheet, which controls whether a job sheet can be generated for a service appointment once the appointment is marked complete.

**Request Body** (required) — application/json
> The request body contains the data required to perform the operation. 
  > Represents the request wrapper used to update the service preference settings of the organization.
  - `service_preferences` (object) **REQ** — Represents the service preference settings to update for the organization.
    - `job_sheet_enabled` (boolean) **REQ** — Denotes whether you want to enable the job sheet for the
organization. When the job sheet is enabled, a job sheet
can be generated for a service appointment once the
appointment is marked complete.


Possible values:


- **true**: enables the job sheet for the organization.
This is the default value.

- **false**: disables the job sheet for the
organization.


**Responses:**

- **200**: The service preference settings of the organization were updated successfully. [application/json]
    > Represents the response wrapper returned after the API updates the service preference settings of the organization.
    - `service_preferences` (object) **REQ** — Represents the result of updating the service preference settings of the organization.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the update operation.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the code that indicates the result of the update operation.

      - `message` (string) **REQ** [enum=['Services preferences updated successfully']] — Represents the message that describes the result of the update operation.
      - `details` (object) **REQ** — Represents additional details about the update operation. This object is empty when the update is successful.

- **400**: The request to update the service preference settings failed because of a missing mandatory field or invalid data in the request payload. [application/json]
    > Represents the error response returned when the request to update service preferences is invalid.
    oneOf:
        - `service_preferences` (object) — Represents the error details returned when the request to update service preferences fails because of a missing mandatory field or invalid data.
          oneOf:
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned when a mandatory field is missing in the request.
              - `message` (string) **REQ** [maxLen=1000] — Represents the message that describes the missing mandatory field.
              - `details` (object) **REQ** — Represents the details of the missing mandatory field.
                - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the missing mandatory field.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the missing mandatory field in the request payload.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the request contains invalid data.
              - `message` (string) **REQ** [maxLen=1000] — Represents the message that describes the invalid data error.
              - `details` (object) **REQ** — Represents the details of the invalid field in the request payload.
                oneOf:
                    - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the invalid field.
                    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field in the request payload.
                    - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the invalid field.
                    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field in the request payload.
                    - `expected_data_type` (string) **REQ** [enum=['boolean']] — Represents the data type expected for the invalid field.
        additionalProperties: any
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.

        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the request contains invalid data.

        - `message` (string) **REQ** [maxLen=1000] — Represents the message that describes the invalid data error.
        - `details` (object) **REQ** — Represents the details of the invalid field in the request payload.
          oneOf:
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the invalid field.
              - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field in the request payload.
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the invalid field.
              - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the invalid field in the request payload.
              - `expected_data_type` (string) **REQ** [enum=['boolean']] — Represents the data type expected for the invalid field.
        additionalProperties: any

**Scopes:** ZohoCRM.settings.modules.UPDATE

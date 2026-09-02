# POST /{module}/actions/enrol_in_cadences
**Operation:** `postEnrolInCadences` — Enroll Records to Cadences
> Enrolls CRM records into one or more cadences.
**Notes**
- Only Manual Enrollment cadences can be enrolled through this API.
- Available only in Enterprise edition and above.
- Supports Leads, Contacts, Deals, Vendors, and custom modules.
- A request may contain up to 5 cadence IDs.
- A request may contain up to 100 record IDs.

**Parameters:**
- `module` (path, string, required) [maxLen=100]: Specify the API name of the module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.

**Schemas:**
`CadencesNested`:
  > Represents a Cadence in the operation result, including its unique ID and name.
  - `name` (string) [maxLen=255] — Represents the name of the Cadence.
  - `id` (string) [maxLen=255] — Represents the unique ID of the Cadence.
`DetailsNested`:
  > Represents the details of a successful per-record operation result, including the record ID and the associated Cadences.
  - `cadences` (array of object `CadencesNested`) [maxItems=2] — Specify the list of Cadences associated with the operation result.
  - `id` (string) [maxLen=255] — Represents the unique ID of the record.
`SuccessDataNested`:
  > Represents a successful per-record operation result.
  - `code` (string) [maxLen=255] — Represents the result code for the record operation.
  - `details` (object `DetailsNested`) — Represents the details of a successful per-record operation result, including the record ID and the associated Cadences.
  - `message` (string) [maxLen=255] — Represents the message indicating the outcome of the record operation.
  - `status` (string) [maxLen=255] — The status of the record operation.

**Request Body** — application/json `PostCadencesRequest`
> The request body must contain a Cadence IDs array and a record IDs array for the enrollment request.
  > Represents the request payload for enrolling or un-enrolling records in one or more Cadences.
  - `cadences_ids` (array of string) [maxLen=255, maxItems=5] **REQ** — A list of Cadence IDs to use for the enrollment or un-enrollment operation.
    items: [maxLen=255]
  - `ids` (array of string) [maxItems=100] **REQ** — Specify the list of record IDs to enroll in or un-enroll from the specified Cadences.
    items: [maxLen=255]

**Responses:**

- **200**: Returns the enrollment result for all records in the request. — Schema: `PostcadencesResponse200` [application/json]
    > Represents the successful response body for a Cadence enrollment or un-enrollment operation.
    schema: `PostcadencesResponse200`
    - `data` (array of object `SuccessDataNested`) [maxItems=100] — Represents the list of operation results for the request.

- **202**: The enrollment request was accepted and queued for background processing. The response body contains a SCHEDULED status marker. — Schema: `PostcadencesResponse202` [application/json]
    > Represents the asynchronous acceptance response returned when the enrollment or unenrollment request is queued for background processing.
    schema: `PostcadencesResponse202`
    - `data` (array of object `ScheduledDataNested`) [maxItems=1] — Represents a single-entry array containing the SCHEDULED status marker for the queued enrollment request.
      schema: `ScheduledDataNested`
      - `code` (string) [maxLen=255, enum=['SCHEDULED']] — Represents the processing status code. For 202 responses, this is always **SCHEDULED**.
      - `details` (object) — Represents additional details about the scheduled operation. This object is currently empty and reserved for future use.
      - `message` (string) [maxLen=255] — Represents the message describing the current processing state of the enrollment request.
      - `status` (string) [maxLen=255, enum=['success']] — Represents the overall status of the scheduled operation. For 202 responses, this is always **success**.

- **207**: Returns a multi-status response when some records were enrolled successfully and others failed. Each item in the data array independently indicates success or failure for the corresponding record. — Schema: `PostcadencesResponse207` [application/json]
    > Specify the multi-status response body for a Cadence enrollment or un-enrollment operation where some records succeeded and others failed.
    schema: `PostcadencesResponse207`
    - `data` (array of object) [maxItems=100] — Specify the list of per-record operation results. Each item indicates success or failure for the corresponding record in the request.
      oneOf:
        - `SuccessDataNested` — Represents a successful per-record operation result.
        - `ErrorDataNested` — Represents a failed per-record operation result in a multi-status response.
          - `code` (string) [maxLen=255, enum=['INVALID_DATA']] — Indicates the error code for the per-record failure. Possible values: **INVALID_DATA**.
          - `details` (object) — JSON object specifying the details of the per-record error, including the affected field name and JSON path.
            - `api_name` (string) [maxLen=255, enum=['ids']] — Represents the API name of the request field that caused the per-record error. Possible values: **ids**.
            - `json_path` (string) [maxLen=255] — Indicates the JSON path to the specific value in the request that triggered the per-record error.
            additionalProperties: any
          - `message` (string) [maxLen=255] — Represents the error message describing the reason for the per-record failure.
          - `status` (string) [maxLen=255, enum=['error']] — Indicates the status of the per-record result. Possible values: **error**.

- **400**: The request could not be processed due to invalid or unsupported input.
**Resolution:** The record IDs and Cadence IDs must be valid, the API must be accessed from a supported domain, and the specified Cadences must support manual enrollment. [application/json]
    > Represents one of the possible error responses for a 400 Bad Request status, indicating an invalid or unsupported request parameter.
    oneOf:
      - `ErrorResponseApiNotSupportedClientPortal` — Represents the error response returned when the authenticated user is a Client Portal user, which is an unsupported user type for this API.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Represents the error code. The value is **API_NOT_SUPPORTED**.
        - `details` (object) **REQ** — Represents the error details containing the unsupported login user type.
          - `unsupported_login_user_type` (string) **REQ** [maxLen=255] — Represents the login user type that is not supported by this API.
        - `message` (string) **REQ** [enum=['api not supported for client portal user']] — Represents the error message describing the unsupported user type.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status. The value is **error**.
      - `ErrorResponseApiNotSupportedDomain` — Represents the error response returned when the caller's Zoho data-center domain does not support the Cadence execution API.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Represents the error code. The value is **API_NOT_SUPPORTED**.
        - `details` (object) **REQ** — Represents the error details including the list of supported domains for this API.
          - `supported_domains` (array of string) [maxItems=25] **REQ** — Represents the list of Zoho data-center domains that support the Cadence execution API.
            items: [maxLen=255]
        - `message` (string) **REQ** [enum=['api not supported']] — Represents the error message describing the domain restriction.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status. The value is **error**.
      - `ErrorResponseLimitExceededCadenceIds` — Represents the LIMIT_EXCEEDED error returned when the Cadence IDs array exceeds the allowed maximum of 5 per request.
        - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code identifying the type of limit violation. The value is **LIMIT_EXCEEDED**.
        - `details` (object) **REQ** — Represents the error details containing the limit value and the fields that caused the limit violation.
          - `limit` (integer/int32) **REQ** — Represents the maximum allowed count for the Cadence IDs array per request.
          - `limit_due_to` (array of object) [maxItems=25] **REQ** — Represents the list of fields responsible for the limit violation.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the limit violation.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the limit violation.
        - `message` (string) **REQ** [enum=['Limit Exceeded, You cannot give more than 5 cadences ids']] — Represents the error message describing the limit violation.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status. The value is **error**.
      - `ErrorResponseLimitExceededRecordIds` — Represents the error response returned when the **ids** array exceeds the allowed maximum of 100 record IDs per request.
        - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code. The value is **LIMIT_EXCEEDED**.
        - `details` (object) **REQ** — Represents the error details containing the limit value and the fields that caused the limit violation.
          - `limit` (integer/int32) **REQ** — Represents the maximum allowed count for the **ids** array.
          - `limit_due_to` (array of object) [maxItems=25] **REQ** — Represents the list of fields responsible for the limit violation.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the limit violation.
            - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the limit violation.
        - `message` (string) **REQ** [enum=['Limit Exceeded, You cannot give more than 100 record ids']] — Represents the error message describing the limit violation.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status. The value is **error**.
      - `ErrorResponseNotAllowed` — Represents the error response returned when a Cadence does not support manual enrollment - only manual_enrollment type Cadences are supported by this API.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code. The value is **NOT_ALLOWED**.
        - `details` (object) **REQ** — Represents the error details identifying the Cadence that does not support manual enrollment.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the NOT_ALLOWED error.
          - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field associated with the NOT_ALLOWED error.
        - `message` (string) **REQ** [enum=['id given is not manual enrollment cadence']] — Represents the error message describing why the operation is not allowed for this Cadence.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status. The value is **error**.
      - `ErrorResponseInvalidDataCadenceIds` — Represents the INVALID_DATA error returned when the Cadence IDs array contains an invalid ID or has the wrong data type.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. The value is **INVALID_DATA**.
        - `details` (object) **REQ** — Represents the error details with validation information for the invalid Cadence ID.
          - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the Cadence ID value.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that contains the invalid Cadence ID.
          - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that contains the invalid Cadence ID.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the invalid Cadence ID.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status. The value is **error**.
      - `ErrorResponseMandatoryNotFound` — Represents the MANDATORY_NOT_FOUND error indicating that a required top-level array - record IDs or Cadence IDs - was missing from the request body.
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code. The value is **MANDATORY_NOT_FOUND**.
        - `details` (object) **REQ** — Represents the error details identifying the missing required field.
          - `api_name` (string) **REQ** [maxLen=255, enum=['ids', 'cadences_ids']] — Represents the API name of the missing required field.
          - `json_path` (string) **REQ** [maxLen=1000, enum=['$.ids', '$.cadences_ids']] — Represents the JSON path of the missing required field.
        - `message` (string) **REQ** [enum=['Record ids not found', 'Cadences ids not found']] — Represents the error message describing the missing field.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status. The value is **error**.
      - `ErrorResponseDataInvalidDataType` — Represents the INVALID_DATA error returned when the **ids** or Cadence IDs field has the wrong data type - for example, a string was supplied where an array is expected.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. The value is **INVALID_DATA**.
        - `details` (object) **REQ** — Represents the error details containing the expected data type information.
          - `expected_data_type` (string) **REQ** [maxLen=255, enum=['jsonarray']] — Represents the data type expected for the field.
          - `api_name` (string) **REQ** [maxLen=255, enum=['ids', 'cadences_ids']] — Represents the API name of the field with the wrong data type.
          - `json_path` (string) **REQ** [maxLen=1000, enum=['$.ids', '$.cadences_ids']] — Represents the JSON path of the field with the wrong data type.
        - `message` (string) **REQ** [enum=['Record ids not found', 'Cadences ids not found']] — Represents the error message describing the data type mismatch.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status. The value is **error**.
      - `ErrorResponseDataInvalidId` — Represents the INVALID_DATA error returned when an individual record ID or Cadence ID in the request arrays is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code. The value is **INVALID_DATA**.
        - `details` (object) **REQ** — Represents the error details identifying the invalid ID.
          - `api_name` (string) **REQ** [maxLen=255, enum=['ids', 'cadences_ids']] — Represents the API name of the field containing the invalid ID.
          - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field containing the invalid ID.
          - `expected_data_type` (string) [maxLen=255, enum=['bigint', 'jsonarray']] — Represents the expected data type for the field. Present when the error is caused by a data type mismatch.
        - `message` (string) **REQ** [enum=[3 values]] — Represents the error message describing the invalid ID.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status. The value is **error**.
      - `ErrorResponseDataInvalidIdArray` — Represents the array-form error response returned when one or more record IDs in the **ids** array are invalid.
        - `data` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the list of per-record error entries for each invalid record ID.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the invalid record ID. The value is **INVALID_DATA**.
          - `details` (object) **REQ** — Represents the error details identifying the invalid record ID.
            - `api_name` (string) **REQ** [maxLen=255, enum=['ids', 'cadences_ids']] — Represents the API name of the field containing the invalid record ID.
            - `json_path` (string) **REQ** [maxLen=1000, pattern=^\$\.(ids|cadences_ids)\[[0-9]+\]$] — Represents the JSON path of the field containing the invalid record ID.
          - `message` (string) **REQ** [enum=[3 values]] — Represents the error message for the invalid record ID.
          - `status` (string) **REQ** [enum=['error']] — Represents the error status. The value is **error**.

- **403**: The requesting user does not have the required permission to perform Cadence enrollment.
**Resolution:** The CRM administrator must grant the **Crm_Implied_Manage_UnEnroll_Series** permission to the user's profile. — Schema: `ErrorResponse403` [application/json]
    > Represents the error response for a 403 Forbidden status, indicating insufficient permissions to perform the enrollment operation.
    schema: `ErrorResponse403`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the permission failure. Possible values: **NO_PERMISSION**. 
    - `details` (object) **REQ** — Indicates the error details containing the CRM permissions required to perform this operation. 
      - `permissions` (array of string) [maxItems=25] — Represents the list of CRM permissions required to perform this operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['No permission']] — Represents the error message for the permission failure. Possible values: **No permission**. 
    - `status` (string) **REQ** [enum=['error']] — Indicates the error status. Possible values: **error**. 

**Scopes:** ZohoCRM.modules.Leads.CREATE, ZohoCRM.modules.Contacts.CREATE, ZohoCRM.modules.Accounts.CREATE, ZohoCRM.modules.Deals.CREATE, ZohoCRM.modules.Vendors.CREATE, ZohoCRM.modules.Quotes.CREATE, ZohoCRM.modules.custom.CREATE

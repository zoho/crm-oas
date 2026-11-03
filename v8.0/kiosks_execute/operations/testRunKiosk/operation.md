# POST /settings/kiosks/{kioskId}/actions/test_run
**Operation:** `testRunKiosk` — Initiate a Test Run for a Kiosk
> To initiate a test run for a kiosk before publishing it in your Zoho CRM organization.
This operation executes all configured kiosk states and actions on live CRM data in real time. Actions such as creating, updating, or deleting records and sending email notifications are performed immediately and cannot be automatically reversed.
The response returns the first state of the kiosk. To advance through the remaining states, use the [Update Kiosk Execution API](kiosk_execute.yaml#$.paths./settings/kiosks/{kioskId}/executions/{executionId}/actions/execute.put) with the execution details returned in the response.
Retrieve the kiosk ID using the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) before calling this endpoint.
Administrator profile, or a profile with the Module Customization or Manage Automation  permission should be enabled.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=19]: Specify the unique identifier of the kiosk for which you want to perform the operation.

**Request Body** — application/json `KioskTestRunPayload`
> The request body must contain a kiosk_test_run array with one object.
  > Represents the request payload for a kiosk test run, containing one or more test run entries.
  - `kiosk_test_run` (array of object `KioskTestRunEntry`) [maxItems=1] **REQ** — Contains one or more test run entries, each providing the data context for initiating a kiosk test run.
    schema: `KioskTestRunEntry`
    - `data` (object `ExecuteDataContainer`) — Contains information about the current record module if any
      schema: `ExecuteDataContainer`
      - `Current_Record` (object `ExecuteCurrentRecordRef`) — The Current_Record field provides the record context for the Kiosk execution.
        schema: `ExecuteCurrentRecordRef`
        - `id` (string) [maxLen=19, nullable] — Represents the unique identifier of the current module record referenced during execution.

      - `id` (string) [maxLen=18, nullable] — Represents the unique identifier of the kiosk execution instance.

**Responses:**

- **200**: Returns a kiosk_test_run array containing the result of the test run initiation, including the status code, a descriptive message, the execution record ID, the next executable state, and any dependent states executed during the run. — Schema: `KioskTestRunSuccessResponse` [application/json]
    > Represents the response for a successful kiosk test run, including the status, message, and details of the next executable state.
    schema: `KioskTestRunSuccessResponse`
    - `kiosk_test_run` (array of object `TestRunStatusItem`) [maxItems=1] — Contains the result of the test run, including status, message, and details of the next executable state.
      schema: `TestRunStatusItem`
      - `code` (string) [maxLen=255] — Represents the status code returned for the test run entry.
      - `details` (object `TestRunExecutionDetails`) — Provides details of a test run execution, including the next executable state, any dependent states that were executed, and the execution record ID.
        schema: `TestRunExecutionDetails`
        - `next_executable_state` (object `NextExecutableStateInfo`) — An array of dependent states that were executed during the test run. Each object contains information about the state and the transition taken.
          schema: `NextExecutableStateInfo`
          - `name` (string) [maxLen=255] — Represents the display name of the next executable kiosk state.
          - `id` (string) [maxLen=255] — Contains the unique identifier of the next executable kiosk state.
        - `executed_dependent_states` (array of object) [maxItems=10, nullable] — Contains the list of dependent states that were executed as part of the test run, or null if no dependent states were triggered.
          - `name` (string) **REQ** [maxLen=255] — Field: name
          - `id` (string) **REQ** [maxLen=255] — Field: id
          - `rid` (string/uuid) [maxLen=255] — Field: rid
          - `type` (string) [maxLen=255] — Field: type
          - `transition` (object) **REQ** — Field: transition
            - `name` (string) **REQ** [maxLen=255] — Field: name
            - `id` (string) **REQ** [maxLen=255] — Field: id
            - `rid` (string/uuid) [maxLen=255] — Field: rid
          - `details` (object) — Field: details — optional state-specific details
        - `id` (string) [maxLen=255] — Contains the unique identifier of the test run execution record.
      - `message` (string) [maxLen=255] — Contains the message describing the outcome of the test run entry.
      - `status` (string) [maxLen=255] — Indicates the overall status of the test run entry result.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: **No such Kiosk exists.**

**Resolution:** Specify a valid kiosk ID in the request path. Retrieve valid kiosk IDs using the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) .

**invalid data.**

**Resolution:** Verify that the kiosk_test_run field in the request body is a valid array within the maximum length permitted.
 [application/json]
    > Represents one of two error shapes returned when the request is invalid: an invalid kiosk identifier error, which includes a resource path index in the details, or an invalid data error for the kiosk_test_run field, which includes the field name, maximum length, and JSON path in the details.
    oneOf:
      - `KioskTestRunInvalidKioskError` — Returned when the specified kiosk identifier is invalid for a test run. Contains the error code, message, status, and details identifying the invalid path segment.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the specified kiosk identifier is invalid for a test run.

Possible values:
INVALID_DATA - The kiosk ID provided in the request URL does not correspond to an existing kiosk.

        - `details` (object) **REQ** — Contains validation details identifying the path segment that contains the invalid kiosk identifier.
          - `resource_path_index` (integer/int32) **REQ** — Indicates the zero-based index of the URL path segment that contains the invalid kiosk identifier.
        - `message` (string) **REQ** [enum=['No such Kiosk exists']] — Represents the error message returned when the specified kiosk does not exist.

Possible values:
No such Kiosk exists - The kiosk ID provided in the request URL does not match any existing kiosk record.
        - `status` (string) **REQ** [enum=['error']] — Represents the response status returned when the specified kiosk identifier is invalid.

Possible values:
error - The request failed because the kiosk ID does not correspond to an existing kiosk.
      - `KioskTestRunInvalidDataTypeError` — Indicates that the kiosk_test_run field in the request body has an invalid data type. Contains the error code, message, status, and validation details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the kiosk_test_run field has an invalid data type.

Possible values:
INVALID_DATA - One or more fields in the test run request body contain a value of an unexpected data type.
        - `details` (object) **REQ** — Contains validation details identifying the field that carries the invalid data type.
          - `maximum_length` (integer/int32) **REQ** — Indicates the maximum number of items allowed in the kiosk_test_run payload that triggered the invalid data type error.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that contains the invalid data type value.
          - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request body that contains the invalid data type value.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message returned when the kiosk_test_run field has an invalid data type.

Possible values:
invalid data - The kiosk_test_run field in the request body contains a value that does not match the expected data type.
        - `status` (string) **REQ** [enum=['error']] — Represents the response status returned when the kiosk_test_run field has an invalid data type.

Possible values:
error - The request failed because the kiosk_test_run field contains a value of an invalid data type.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.CREATE

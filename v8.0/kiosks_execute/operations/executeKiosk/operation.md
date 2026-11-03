# POST /settings/kiosks/{kioskId}/actions/execute
**Operation:** `executeKiosk` — Execute a Kiosk
> The execute Kiosk API is used to trigger the execution of a published Kiosk in Zoho CRM.
This API returns only the first executable state of the Kiosk. To continue the execution through the remaining states, call the [Update a Kiosk Execution API](kiosks_execute.yaml#$.paths./settings/kiosks/{kiosk_id}/executions/{execution_id}/actions/execute.put) until the execution is complete.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=19]: Specify the unique identifier of the kiosk for which you want to perform the operation.

**Request Body** — application/json `KioskExecuteActionPayload`
> The request body must contain a kiosk_execute array with one object. The object accepts an optional data field that provides the record context for the Kiosk execution, including the current record ID.
  > Represents the request payload for executing a kiosk, containing one or more execute action entries.
  - `kiosk_execute` (array of object `ExecuteActionEntry`) [maxItems=1] **REQ** — The request body must be a JSON object containing the kiosk_execute array. The array contains the  data required to execute the Kiosk.
    schema: `ExecuteActionEntry`
    - `data` (object `ExecuteDataContainer`) — Specify the data context for the Kiosk execution. If not provided, the Kiosk will execute without a record context.
      schema: `ExecuteDataContainer`
      - `Current_Record` (object `ExecuteCurrentRecordRef`) — The Current_Record field provides the record context for the Kiosk execution.
        schema: `ExecuteCurrentRecordRef`
        - `id` (string) [maxLen=19, nullable] — Represents the unique identifier of the current module record referenced during execution.

      - `id` (string) [maxLen=18, nullable] — Represents the unique identifier of the kiosk execution instance.

**Responses:**

- **200**: Returns the execution result for the published Kiosk, including the next executable state, the executed_dependent_states value, and the unique identifier of the execution record. — Schema: `KioskExecuteActionSuccessResponse` [application/json]
    > Indicates a successful execute action and provides details about the next executable kiosk state.
    schema: `KioskExecuteActionSuccessResponse`
    - `kiosk_execute` (array of object `ExecuteActionStatusItem`) [maxItems=1] — Contains the result of the execute action, including the status, message, and details of the next executable state.
      schema: `ExecuteActionStatusItem`
      - `code` (string) [maxLen=255] — Represents the status code returned for the execute action result.
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
      - `message` (string) [maxLen=255] — Represents the message describing the outcome of the execute action.
      - `status` (string) [maxLen=255] — Represents the response status indicating whether the execute action succeeded or encountered an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The specified Kiosk ID or request body is invalid.
**Resolution:** A valid Kiosk ID must be specified in the request URL, and the request body must contain a value of the correct data type. [application/json]
    > Represents one of the possible error response shapes returned for a 400 Bad Request on Kiosk execution. Either the specified Kiosk ID does not match any existing Kiosk, or the request body contains a value with an invalid data type.
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
      - `ExecuteInvalidDataTypeError` — Returned when the execute action payload contains fields with invalid data types.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the payload contains fields with invalid data types.

Possible values:
INVALID_DATA - One or more fields in the request body carry a value of an unexpected data type.
        - `details` (object) **REQ** — Contains validation details identifying the data type discrepancy that caused the error.
          - `expected_data_type` (string) **REQ** [maxLen=255] — Indicates the data type that the field was expected to carry, as defined by the kiosk execution schema.

        - `message` (string) **REQ** [enum=['body']] — Represents the error message describing the source of the invalid data type violation.

Possible values:
body - The invalid data type was detected in the request body.
        - `status` (string) **REQ** [enum=['error']] — Represents the response status returned when an invalid data type error occurs.

Possible values:
error - The request failed due to one or more fields containing values of an unexpected data type.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.CREATE

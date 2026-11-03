# PUT /settings/kiosks/{kioskId}/executions/{executionId}/actions/execute
**Operation:** `executeKioskState` — Update a Kiosk Execution
> To execute a transition in an ongoing Kiosk execution by submitting the required transition and runtime data, and proceed to the next step of the Kiosk in your Zoho CRM.
The Kiosk must be in the published status and have an active execution to update its execution state. To obtain the execution_ID, execute the Kiosk using the [Execute a Kiosk API](kiosks_execute.yaml#$.paths./settings/kiosks/{kioskId}/actions/execute.post). If an execution is already in progress, invoke the [Get Executions of a Kiosk API](kiosks_execute.yaml#$.paths./settings/kiosks/{kioskId}/executions.post) to retrieve the execution_ID.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=19]: Specify the unique identifier of the kiosk for which you want to perform the operation.
- `executionId` (path, string, required) [maxLen=19]: Specify the unique ID of the execution.

**Request Body** — application/json `KioskExecutionActionPayload`
> The request body must contain a kiosk_executions array with one object. Each object must include a transition (with a required transition ID) and may include a data object with the current record context and execution ID.
  > Represents the request payload for advancing a kiosk execution state, containing one or more execution action entries.
  - `kiosk_executions` (array of object `ExecutionActionEntry`) [maxItems=1] **REQ** — Contains one or more execution action entries, each specifying the transition and data context for advancing the kiosk execution to the next state.
    schema: `ExecutionActionEntry`
    - `data` (object `ExecuteDataContainer`) — Contains information about the current execution
      schema: `ExecuteDataContainer`
      - `Current_Record` (object `ExecuteCurrentRecordRef`) — The Current_Record field provides the record context for the Kiosk execution.
        schema: `ExecuteCurrentRecordRef`
        - `id` (string) [maxLen=19, nullable] — Represents the unique identifier of the current module record referenced during execution.

      - `id` (string) [maxLen=18, nullable] — Represents the unique identifier of the kiosk execution instance.
    - `transition` (object `ExecutionTransitionReference`) **REQ** — Contains the transition information for next execution (Required)
      schema: `ExecutionTransitionReference`
      - `name` (string) [maxLen=50, nullable] — Represents the display name of the transition that triggers the current execution step.
      - `id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the transition that triggers the current execution step.

**Responses:**

- **200**: Returns a kiosk_executions array confirming that the transition was executed successfully. Each item includes the execution status code, a message, and a details object containing the next executable state and any dependent states that were executed. — Schema: `KioskExecutionActionSuccessResponse` [application/json]
    > Indicates that an execution action completed successfully and provides details of the next executable state and execution ID.
    schema: `KioskExecutionActionSuccessResponse`
    - `kiosk_executions` (array of object `ExecutionActionStatusItem`) [maxItems=1] — Contains the result of the execution action, including the status, message, and details of the next executable state.
      schema: `ExecutionActionStatusItem`
      - `code` (string) [maxLen=255] — Represents the status code returned for the execution action result.
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
      - `message` (string) [maxLen=255] — Contains the message describing the outcome of the execution action.
      - `status` (string) [maxLen=255] — Indicates the overall status of the execution action result.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Invalid Kiosk transition given for execution.
**Resolution:** A valid transition ID belonging to the current executable state must be specified in the request body.

No such Kiosk exists.
**Resolution:** A valid kiosk ID must be specified in the request URL.

Invalid Kiosk execution ID.
**Resolution:** A valid execution ID must be specified in the request URL. [application/json]
    > Represents the error response body returned when the kiosk execution request contains invalid input, such as an invalid kiosk ID, transition ID, or execution ID.
    oneOf:
        - `kiosk_executions` (array of object) [maxItems=25] **REQ** — Represents the list of error objects returned when the kiosk execution request fails.
          oneOf:
            - `ExecutionInvalidTransitionError` — Returned when an invalid transition ID is provided for continuing the kiosk execution.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when an invalid transition ID is provided for kiosk execution.

Possible values:
INVALID_DATA - The transition ID specified in the request does not correspond to a valid kiosk transition.
              - `details` (object) **REQ** — Contains validation details identifying the field that carries the invalid transition ID.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that contains the invalid transition ID value.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field in the request body that contains the invalid transition ID value.
              - `message` (string) **REQ** [enum=['Invalid Kiosk transition given for execution']] — Represents the error message returned when an invalid kiosk transition is specified.

Possible values:
Invalid Kiosk transition given for execution - The transition ID provided does not correspond to a valid transition for the current kiosk execution state.
              - `status` (string) **REQ** [enum=['error']] — Represents the response status returned when an invalid transition error occurs.

Possible values:
error - The request failed because the specified transition ID is not valid for the current kiosk execution state.
            - `ExecutionNotAllowedError` — Returned when the given transition does not belong to the current kiosk state.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code
              - `details` (object) **REQ** — Error details (empty for this error type)
              - `message` (string) **REQ** [maxLen=1000] — Error message
              - `status` (string) **REQ** [enum=['error']] — Error status
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
      - `ExecutionInvalidIdError` — Indicates that the provided execution ID is invalid for the kiosk execution operation.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Indicates the error code identifying the nature of the failure.

Possible values:
INVALID_DATA - The execution ID provided in the request does not correspond to a valid kiosk execution record.
        - `details` (object) **REQ** — Contains validation details identifying the invalid execution ID path segment in the request URL.
          - `resource_path_index` (integer/int32) **REQ** — Indicates the zero-based index of the URL path segment that contains the invalid execution ID value.
        - `message` (string) **REQ** [enum=['Invalid Kiosk execution id']] — Represents the error message returned when the execution ID is invalid.

Possible values:
Invalid Kiosk execution ID - The execution ID provided in the request URL does not match any existing kiosk execution record.
        - `status` (string) **REQ** [enum=['error']] — Represents the response status returned when the execution ID is invalid.

Possible values:
error - The request failed because the provided execution ID does not correspond to a valid kiosk execution record.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.UPDATE

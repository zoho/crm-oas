# GET /settings/kiosks/{kioskId}/executions/{executionId}
**Operation:** `getKioskExecution` — Retrieve a kiosk execution record
> To retrieve the details of a specific kiosk execution in your Zoho CRM organization. The response includes all elements and metadata for the state currently being executed, along with the owner of the execution, the execution start and end times, the current or most recently executed state, and the transition that can be executed next. The kiosk must be in published status and have at least one active execution. Available in Standard, Professional, Enterprise, and Ultimate editions.

**Parameters:**
- `kioskId` (path, string, required) [maxLen=19]: Specify the unique identifier of the kiosk for which you want to perform the operation.
- `executionId` (path, string, required) [maxLen=19]: Specify the unique ID of the execution.
- `include_inner_details` (query, string, optional) [maxLen=500]: Specify additional inner details to include in the response. Accepts a comma-separated list of dot-notation paths indicating which nested properties should return extended information.
- `navigated_from_back` (query, boolean, optional): Indicates whether the execution was navigated from a back action.

**Responses:**

- **200**: Returns the elements and metadata for the state being executed within the specified kiosk execution. — Schema: `KioskExecutionViewResponse` [application/json]
    > Represents the response for a specific kiosk execution state view, containing the elements and metadata for the state being executed.
    schema: `KioskExecutionViewResponse`
    - `kiosk_executions` (array of object `KioskExecutionView`) [maxItems=1] **REQ** — Contains the details of the execution state being rendered, including elements, layout, and data.
      schema: `KioskExecutionView`
      - `executable_info` (object `PreviewExecutableInfo`) **REQ** — Provides the current state and available transitions for the executable context of a kiosk preview.
        schema: `PreviewExecutableInfo`
        - `state` (object `PreviewStateSummary`) **REQ** — Represents a summary of a kiosk state referenced in the preview, including the state ID and display name.
          schema: `PreviewStateSummary`
          - `name` (string) **REQ** [maxLen=255] — Represents the display name of the kiosk state referenced in the preview.
          - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the kiosk state referenced in the preview.
        - `transitions` (array of object `PreviewTransitionSummary`) [maxItems=1] **REQ** — Specifies the list of transitions available from the current state. Each transition contains the display name, unique ID, prop_name,is_connected_end.
          schema: `PreviewTransitionSummary`
          - `prop_name` (string) **REQ** [maxLen=255, enum=['primary', 'default', 'outlineprimary', 'failure', 'outlineredlight']] — Specifies the type of button displayed on the Kiosk screen. Each button corresponds to a transition path that the user can select from the current screen.
**Possible values:**

**primary** - Displays the button as the primary action on the screen, typically used for actions such as Next, Submit, or Save.

**default** - Displays the button with the standard appearance, suitable for secondary actions.

**outlineprimary** - Displays the button with a primary-colored outline, emphasizing the action without making it the primary button.

**failure** - Displays the button with a solid error-themed style, typically used for destructive or critical actions such as Delete or Reject.

**outlineredlight** - Displays the button with a red outline, typically used for secondary destructive actions such as Cancel, Discard, or Remove.

          - `is_connected_end` (boolean) **REQ** — Indicates whether this transition leads to a connected end state in the kiosk flow.

Possible values:
true - The transition leads to a connected end state.
false - The transition leads to an intermediate state in the kiosk flow.

          - `name` (string) **REQ** [maxLen=255] — Represents the display name of the transition in the kiosk preview.
          - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the transition in the kiosk preview.
      - `data` (object `ExecutionDataBlock`) **REQ** — Contains the runtime data available during the Kiosk execution. This object includes system-generated values (such as execution details, owner information, and record references) along with dynamically generated key-value pairs. The dynamic keys correspond to the API names of the configured Kiosk fields, GetRecords elements, and other runtime values available in the current execution. The fields returned vary depending on the Kiosk configuration and the execution context.
        schema: `ExecutionDataBlock`
        - `Kiosk_End_Time` (string) **REQ** [maxLen=255] — Represents the date and time at which the kiosk execution session ended.
        - `Owner` (object `ExecutionOwnerDetail`) **REQ** — Represents detailed owner information for a kiosk execution, including name, ID, and email address.
          schema: `ExecutionOwnerDetail`
          - `name` (string) **REQ** [maxLen=255] — Represents the full name of the owner associated with the kiosk execution.
          - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the owner associated with the kiosk execution.
          - `email` (string) **REQ** [maxLen=255] — Represents the email address of the owner associated with the kiosk execution.
        - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier for the kiosk execution instance.
        - `Kiosk_Start_Time` (string) **REQ** [maxLen=255] — Represents the date and time at which the kiosk execution session began.
      - `elements` (array of object `ExecutionElement`) [maxItems=1] **REQ** — An array of UI elements and data sources configured in the Kiosk. Each element has a type field that determines its structure.
        schema: `ExecutionElement`
        - `type` (string) **REQ** [maxLen=255] — Indicates the type classification of the execution element.
        - `value` (string) **REQ** [maxLen=255] — Contains the value associated with the execution element.
      - `width` (string) **REQ** [maxLen=255, enum=['670px', '1000px', None], nullable] — Indicates the display width of the kiosk execution state screen.
      - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the kiosk execution view record.
      - `kiosk` (object `PreviewKioskSummary`) **REQ** — Represents a minimal summary of the kiosk in the preview, including the kiosk name and ID.
        schema: `PreviewKioskSummary`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the kiosk associated with the preview.
        - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the kiosk associated with the preview.
      - `title` (string) **REQ** [maxLen=255] — Represents the display title of the kiosk execution state screen.
      - `button_align` (string) **REQ** [maxLen=255, enum=['right_to_left', 'left_to_right', 'center', None], nullable] — The alignment of action buttons. Possible values: right_to_left - Buttons are aligned from right to left. left_to_right - Buttons are aligned from left to right. center - Buttons are aligned to the center.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: No such Kiosk exists.
**Resolution:** Verify that the **kioskId** path parameter in the request URL is a valid and existing kiosk ID. [application/json]
    > Contains the error response returned when the kiosk ID in the request does not correspond to an existing kiosk.
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
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.READ

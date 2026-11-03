# GET /settings/kiosks/{kioskId}/executions
**Operation:** `getKioskExecutions` — List kiosk executions
> To retrieve all active executions for a specific kiosk in your Zoho CRM organization. For each execution, the response includes the user who ran the kiosk, the execution start and end times, the current or most recently visited state, and the transition available to execute next. Multiple concurrent executions, such as those initiated by different users, are also returned.

The kiosk must be in published status and have at least one active execution for the request to return results. An execution is considered complete only when the user navigates through all screens and closes the kiosk on the final screen; completed executions are excluded from the response. Executions closed before reaching the final screen remain active and continue to appear in the response.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=19]: Specify the unique identifier of the kiosk for which you want to perform the operation.
- `page` (query, integer/int32, optional): Page number for pagination.
- `per_page` (query, integer/int32, optional): Number of results per page.
- `include_inner_details` (query, string, optional) [maxLen=500]: Specify additional inner details to include in the response. Accepts a comma-separated list of dot-notation paths indicating which nested properties should return extended information.

**Responses:**

- **200**: Returns a list of active kiosk execution records for the specified kiosk, along with pagination details. — Schema: `KioskExecutionsListResponse` [application/json]
    > Represents a paginated list of kiosk execution records along with pagination metadata.
    schema: `KioskExecutionsListResponse`
    - `kiosk_executions` (array of object `KioskExecutionRecord`) [maxItems=4] **REQ** — Contains the list of kiosk execution records returned for the specified kiosk.
      schema: `KioskExecutionRecord`
      - `Kiosk_End_Time` (string) **REQ** [maxLen=255] — The timestamp indicating when the most recently executed state of the Kiosk ended, in ISO 8601 format. The response is sorted in descending order of this field, with the most recent executions listed first.
      - `Owner` (object `PreviewOwnerSummary`) **REQ** — Contains information about the owner of the record who initiated this kiosk execution.
        schema: `PreviewOwnerSummary`
        - `name` (string) **REQ** [maxLen=255] — Represents the full name of the record owner in the preview.
        - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the record owner in the preview.
      - `executable_info` (object `ExecutionExecutableInfo`) **REQ** — Contains information about the current state of the Kiosk execution and the transition that can be executed next.
        schema: `ExecutionExecutableInfo`
        - `state` (object `PreviewStateSummary`) **REQ** — Represents a summary of a kiosk state referenced in the preview, including the state ID and display name.
          schema: `PreviewStateSummary`
          - `name` (string) **REQ** [maxLen=255] — Represents the display name of the kiosk state referenced in the preview.
          - `id` (string) **REQ** [maxLen=255] — Contains the unique identifier of the kiosk state referenced in the preview.
        - `transitions` (array of object `ExecutionTransitionSummary`) [maxItems=1] **REQ** — An array of available next transitions from the current state. Each transition object contains the unique identifier of an available transition from the current state.
          schema: `ExecutionTransitionSummary`
          - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the kiosk transition referenced in the execution record.
      - `id` (string) **REQ** [maxLen=255] — The unique identifier of the available transition.
      - `Kiosk_Start_Time` (string) **REQ** [maxLen=255] — Represents the date and time at which the kiosk execution record session began.
    - `info` (object `PaginationInfo`) **REQ** — Represents pagination metadata for list responses, including the current page number, records per page, total count, and whether more records are available.
      schema: `PaginationInfo`
      - `per_page` (integer/int32) **REQ** — Indicates the maximum number of kiosk execution records returned per page.
      - `count` (integer/int32) **REQ** — Indicates the number of kiosk execution records returned in the current page.
      - `page` (integer/int32) **REQ** — Indicates the current page number in the paginated list of execution records.
      - `more_records` (boolean) **REQ** — Indicates whether more execution records are available beyond the current page.

Possible values:
true - Additional execution records exist beyond the current page.
false - No additional execution records exist; the current page is the last.

  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: No such Kiosk exists.
**Resolution:** The kiosk ID in the request URL must be a valid and existing kiosk identifier. A list of valid kiosk IDs can be retrieved using the [Get Kiosks API]( kiosks.yaml#$.paths./settings/kiosks.get).
 [application/json]
    > Represents the error response body for a 400 Bad Request on this operation. The oneOf schema resolves to the KioskTestRunInvalidKioskError shape when the specified kiosk identifier does not exist.
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

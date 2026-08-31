# DELETE /actions/watch
**Operation:** `disableNotifications` — Disable notification channels
> To disable one or more notification channels in your Zoho CRM organization.

**Parameters:**
- `channel_ids` (query, string, optional) [maxLen=512]: Specify a comma-separated list of channel IDs identifying the notification channels to disable.

**Schemas:**
`ErrorDetails`:
  > Represents the detailed error information associated with a specific parameter or field that caused the request to fail.
  - `api_name` (string) [maxLen=64] — Represents the API name of the parameter or field that caused the error.
  - `expected_data_type` (string) [maxLen=64] — Represents the expected data type for the parameter or field that caused the error.
  - `json_path` (string) [maxLen=256] — Represents the JSON path indicating the location of the error in the request payload.
  - `ambiguity_due_to` (array of object) [maxItems=2] — Represents the list of fields that caused ambiguity during request processing.
    - `api_name` (string) **REQ** [maxLen=64] — Represents the API name of the field that caused ambiguity.
    - `json_path` (string) **REQ** [maxLen=256] — Represents the JSON path indicating the location of the ambiguous field in the request payload.
  - `expected_fields` (array of object) [maxItems=2] — Represents the list of fields required when at least one of several expected fields is missing.
    - `api_name` (string) **REQ** [maxLen=64] — Represents the API name of the required field.
    - `json_path` (string) **REQ** [maxLen=256] — Represents the JSON path indicating the location of the required field in the request payload.
  - `dependee` (object) — Represents the details of a required dependent field that was missing from the request.
    - `api_name` (string) **REQ** [maxLen=64] — Represents the API name of the missing dependent field.
    - `json_path` (string) **REQ** [maxLen=256] — Represents the JSON path indicating the location of the missing dependent field in the request payload.
  - `supported_values` (array of string) [maxItems=2] — Represents the list of supported values for the parameter or field that caused the error.
    items: [maxLen=64]
  - `maximum_length` (integer/int32) — Represents the maximum allowed length for the parameter or field that caused the error.
`ErrorResponse`:
  > Represents the standard error response structure returned when a request fails.
  - `code` (string) **REQ** [enum=[19 values]] — Represents the specific error code identifying the type of failure.
  - `details` (object `ErrorDetails`) — Represents the detailed error information associated with a specific parameter or field that caused the request to fail.
  - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
  - `status` (string) **REQ** [enum=['error'], default=error] — Represents the response status.
**Possible values:**
**error** - Indicates an error response.

**Responses:**

- **200**: Returns the disable results for each notification channel processed in the request. [application/json]
    > Contains the disable results for each notification channel processed in the request.
    - `watch` (array of object) [maxItems=200] **REQ** — Represents the list of results for each disabled notification channel.
      - `code` (string) **REQ** [maxLen=32] — Represents the result code for the channel disable operation.
      - `details` (object) **REQ** — Contains the resource details of the disabled notification channel.
        - `resource_uri` (string) **REQ** [maxLen=255] — Represents the URI of the CRM resource associated with the disabled notification channel.
        - `resource_id` (string) **REQ** [maxLen=64] — Represents the unique identifier of the CRM resource associated with the disabled notification channel.
        - `channel_id` (string) **REQ** [maxLen=64] — Represents the identifier of the notification channel that was disabled.
      - `message` (string) **REQ** [maxLen=255] — Represents the status message for the channel disable result.
      - `status` (string) **REQ** [maxLen=32] — Represents the status of the channel disable result.

- **207**: Returns a mix of success and error results when some notification channels were created successfully and others failed. [application/json]
    > Contains the partial create results, where each entry in the watch array is either a success or an error.
    - `watch` (array of object) [maxItems=50] — Represents the list of result entries, where each item is either a successful create result or an error response.
      oneOf:
          - `code` (string) [enum=['SUCCESS']] — Represents the result code for a successful operation.
**Possible values:**
**SUCCESS** - The operation completed successfully.
          - `details` (object) — Created event channel details.
          - `message` (string) [maxLen=255] — Result message.
          - `status` (string) [enum=['success']] — Status string.
        - `ErrorResponse` — Represents the standard error response structure returned when a request fails.

- **400**: One or more request parameters are invalid or missing. [application/json]
    oneOf:
      - `ErrorResponse` — Represents the standard error response structure returned when a request fails.
        - `watch` (array of object `ErrorResponse`) [maxItems=50] — Represents the list of error entries returned when a batch operation encounters validation errors.

- **401**: The access token is missing, invalid, or does not have the required OAuth scope. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned when a request fails.

- **429**: The request rate limit has been exceeded. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned when a request fails.

- **500**: An unexpected error occurred while processing the request. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned when a request fails.

**Scopes:** ZohoCRM.notifications.DELETE, ZohoCRM.notifications.ALL

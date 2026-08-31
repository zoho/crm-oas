# PUT /actions/watch
**Operation:** `updateNotificationDetails` — Update full notification details
> To replace all properties of an existing notification channel in your Zoho CRM organization.

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

**Request Body** (required) — application/json
> The request body must contain a watch array. You can include a maximum of 50 objects per request.
  > Contains the complete notification channel configurations that will replace the existing settings.
  - `watch` (array of object) [maxItems=50] — Specify the list of notification channel replacements.
    - `channel_id` (string) **REQ** [maxLen=64] — Specify the identifier of the notification channel to update. Always returned in the response.
    - `notify_url` (string) **REQ** [maxLen=255] — Specify the callback URL for the notification channel.
    - `channel_expiry` (string/date-time) — Specify the expiry date and time for the notification channel.
    - `events` (array of string) [maxItems=50] **REQ** — Specify the complete list of CRM module events to subscribe to, replacing the current event list.
      items: [maxLen=128]
    - `notification_condition` (array of object) [maxItems=2] — Specify the field-selection conditions to replace the existing conditions for the notification channel.
      - `type` (string) **REQ** [enum=['field_selection']] — Specify the condition type.
Possible values:
field_selection - The condition uses field selection criteria.
    - `notify_on_related_action` (boolean) — Indicate whether the notification channel should be triggered by actions on records related to the subscribed module.
Possible values:
true - Notifications are sent for related record actions.
false - Notifications are sent only for direct record actions.
    - `return_affected_field_values` (boolean) — Indicate whether the notification payload should include the changed field values from the affected record.
Possible values:
true - The notification payload includes updated field values.
false - The notification payload does not include field values.
    - `token` (string) [maxLen=256] — Specify the verification token to be included in notification callbacks.

**Responses:**

- **200**: Returns the replacement results for each notification channel submitted in the request. [application/json]
    > Contains the results of the full notification channel replacement.
    - `watch` (array of object) [maxItems=50] **REQ** — Represents the list of replacement results, one entry per channel submitted in the request.
      - `code` (string) **REQ** [maxLen=32] — Represents the result code for the channel replacement operation.
      - `details` (object) **REQ** — Contains the event channel details for the replaced notification channel.
        - `events` (array of object) [maxItems=50] **REQ** — Represents the list of event-channel subscriptions for the replaced notification channel.
          - `channel_expiry` (string/date-time) **REQ** — Represents the expiry date and time of the replaced notification channel. Always returned in the response.
          - `resource_uri` (string) **REQ** [maxLen=255] — Represents the URI of the CRM resource for the replaced event channel subscription. Always returned in the response.
          - `resource_id` (string) **REQ** [maxLen=64] — Represents the unique identifier of the CRM resource for the replaced event channel subscription. Always returned in the response.
          - `resource_name` (string) **REQ** [maxLen=128] — Represents the name of the CRM resource for the replaced event channel subscription. Always returned in the response.
          - `channel_id` (string) **REQ** [maxLen=64] — Represents the identifier of the notification channel after replacement. Always returned in the response.
      - `message` (string) **REQ** [maxLen=255] — Represents the status message for the channel replacement result.
      - `status` (string) **REQ** [maxLen=32] — Represents the status of the channel replacement result.

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

**Scopes:** ZohoCRM.notifications.UPDATE, ZohoCRM.notifications.ALL

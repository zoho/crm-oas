# GET /actions/watch
**Operation:** `getNotifications` — List active notification channels
> To retrieve the list of active notification channels configured for your Zoho CRM organization.

**Parameters:**
- `module` (query, string, optional) [maxLen=64]: Specify the API name of the CRM module to filter the notification channel list. Refer to the [Get Modules](https://www.zoho.com/crm/developer/docs/api/v8/modules-api.html) resource for valid values.
- `channel_id` (query, string, optional) [maxLen=64]: Specify the unique identifier of a single notification channel to filter the results.

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

- **200**: Returns the list of active notification channels configured for the user. [application/json]
    > Contains the list of active notification channels and pagination information for the response.
    - `watch` (array of object) [maxItems=200] — Represents the list of active notification channels for the authenticated user.
      - `notify_on_related_action` (boolean) — Indicates whether the notification channel is triggered by actions on records related to the subscribed module.
Possible values:
true - Notifications are sent for related record actions.
false - Notifications are sent only for direct record actions.
      - `channel_expiry` (string/date-time) — Represents the expiry date and time of the notification channel.
      - `return_affected_field_values` (boolean) — Indicates whether the notification payload includes the changed field values from the affected record.
Possible values:
true - The notification payload includes the updated field values.
false - The notification payload does not include field values.
      - `resource_uri` (string) [maxLen=255] — Represents the URI of the CRM resource associated with the notification channel.
      - `resource_id` (string) [maxLen=64] — Represents the unique identifier of the CRM resource associated with the notification channel.
      - `notify_url` (string) [maxLen=255] — Represents the callback URL to which notifications are delivered when subscribed events occur.
      - `resource_name` (string) [maxLen=128] — Represents the name of the CRM resource associated with the notification channel.
      - `fields` (array of object) [maxItems=100, nullable] — Represents the list of record fields included in the notification payload.
      - `notification_condition` (array of object) [maxItems=2, nullable] — Represents the list of field-selection conditions that determine which record changes trigger a notification on this channel.
        - `field_selection` (object) — Represents the field selection configuration, including the grouping operator and the list of field criteria.
          - `group_operator` (string) [maxLen=3] — Represents the logical operator applied to the field condition groups within the field selection configuration.
          - `group` (array of object) [maxItems=2] — Represents the list of field condition groups used to filter which record field changes trigger the notification.
            - `field` (object) — Represents the CRM field that the condition monitors for changes.
              - `api_name` (string) [maxLen=128] — Represents the API name of the CRM field being monitored in the condition.
              - `id` (string) [maxLen=64] — Represents the unique identifier of the CRM field being monitored in the condition.
            - `group_operator` (string) [enum=['and', 'or', None], nullable] — Represents the logical operator applied to the conditions within this sub-group.
Possible values:
and - All conditions in the sub-group must be satisfied.
or - Any condition in the sub-group must be satisfied.
null - No grouping operator is applied.
            - `group` (array of object) [maxItems=10, nullable] — Represents an optional nested sub-group of field conditions within the parent group.
        - `module` (object) — Represents the CRM module context associated with the field-selection condition.
          - `api_name` (string) [maxLen=255] — Represents the API name of the CRM module associated with the condition.
          - `id` (string) [maxLen=64] — Represents the unique identifier of the CRM module associated with the condition.
        - `type` (string) [maxLen=32] — Represents the type of notification condition.
      - `channel_id` (string) [maxLen=64] — Represents the unique identifier of the notification channel.
      - `events` (array of string) [maxItems=10] — Represents the list of CRM module events for which notifications are triggered on this channel.
        items: [maxLen=128]
      - `token` (string) [maxLen=255, nullable] — Represents the verification token used to authenticate notifications sent to the callback URL.
    - `info` (object) — Represents the pagination metadata for the notification channel list, including the current page, record count per page, and whether additional pages are available.
      - `per_page` (integer/int32) [max=200] — Represents the number of notification channel records returned per page.
      - `count` (integer/int32) [max=100] — Represents the number of notification channel records included in the current response.
      - `page` (integer/int32) [max=100] — Represents the current page number in the paginated response.

**Note**
Use the page and per_page parameter to fetch records according to their position in the CRM. Let's assume that the user has to fetch 400 records. The maximum number of records that one can get for an API call is 200. So, for records above the 200th position, they cannot be fetched. By using the page (1, 2, 3 and 4) and per_page (100) parameter, the user can fetch all 400 records using 4 API calls.
      - `more_records` (boolean) — Indicates whether more notification channel records are available beyond the current page.
Possible values:
true - Additional notification channels are available.
false - No additional notification channels are available.

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

**Scopes:** ZohoCRM.notifications.READ

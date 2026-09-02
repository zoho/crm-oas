# POST /Events/{event}/actions/cancel
**Operation:** `cancelMeetings` — Cancel a Meeting
> To cancel a meeting and send an email regarding the meeting cancellation to the participants. A meeting can only be cancelled if attendees have already been invited and the meeting has not passed its scheduled end time. To check the cancellation status of a meeting, refer to the $event_cancelled key in the response from the [Get Records API](record.yaml#$.paths./module.get).

**Parameters:**
- `event` (path, string, required) [maxLen=255]: This refers to the Event's id that need to be cancel

**Request Body** (required) — application/json
  > The request body for the cancel meeting operation.
  - `data` (array of object) [maxItems=10] **REQ** — Array containing the cancellation notification preference. Mandatory.
    - `send_cancelling_mail` (boolean) **REQ** — Indicates whether to send a meeting cancellation notification email to all participants. Mandatory. Possible values: true - Sends a cancellation notification email to all participants. false - Cancels the meeting without sending a notification email
    - `cancelled_by` (object) — The user who cancelled the meeting. If specified, send_cancelling_mail must be true.
      - `id` (string) **REQ** [maxLen=255] — The ID of the user who cancelled the meeting.

**Responses:**

- **200**: The meeting was cancelled successfully. [application/json]
    > Successful response containing the cancellation result.
    - `data` (array of object) [maxItems=10] **REQ** — Array containing the cancellation result for the meeting.
      - `code` (string) **REQ** [enum=['SUCCESS']] — The status code of the operation.
      - `message` (string) **REQ** [maxLen=255] — A message describing the result of the operation.
      - `status` (string) **REQ** [enum=['success']] — The status of the operation.
      - `details` (object) **REQ** — Object containing the ID of the cancelled meeting.
        - `id` (string) **REQ** [maxLen=255] — The unique identifier of the cancelled meeting.

- **400**: The request failed due to an invalid request method, missing mandatory fields, invalid meeting ID, an already cancelled meeting, no participants, meeting past end time, insufficient permissions, or daily email limit exceeded. [application/json]
    > One of the possible error responses for the cancel meeting operation.
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — The error code identifying the type of error.
        - `message` (string) **REQ** [maxLen=255] — A message describing the error.
        - `details` (object) **REQ** — Error details.
        - `status` (string) **REQ** [enum=['error']] — The status of the response (error).
        - `data` (array of object) [maxItems=10] **REQ** — List of error details
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code
          - `message` (string) **REQ** [maxLen=255] — A message describing the error
          - `details` (object) **REQ** — Object containing the API name and JSON path of the missing mandatory field.
            - `api_name` (string) **REQ** [maxLen=255] — The API name of the missing mandatory field.
            - `json_path` (string) **REQ** [maxLen=255] — The JSON path to the missing mandatory field in the request body.
          - `status` (string) **REQ** [enum=['error']] — The status of the response (error).
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code identifying the type of error.
        - `message` (string) **REQ** [maxLen=255] — A message describing the error.
        - `details` (object) **REQ** — Object containing the API name and JSON path of the invalid field.
          - `expected_data_type` (string) [maxLen=255] — Expected data type
          - `api_name` (string) **REQ** [maxLen=255] — The API name of the field with the invalid value.
          - `json_path` (string) **REQ** [maxLen=255] — The JSON path to the field with the invalid value.
        - `status` (string) **REQ** [enum=['error']] — The status of the response (error).
        - `data` (array of object) [maxItems=10] **REQ** — Contains the list of error details.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — The error code identifying the type of error.
          - `message` (string) **REQ** [maxLen=255] — A message describing the error.
          - `details` (object) **REQ** — Error details
          - `status` (string) **REQ** [enum=['error']] — The status of the response (error).
        - `data` (array of object) [maxItems=10] **REQ** — List of error details
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — The error code identifying the type of error.
          - `message` (string) **REQ** [maxLen=255] — A message describing the error
          - `details` (object) **REQ** — Error details
            - `reason` (string) **REQ** [enum=['no_participants_invited']] — The reason for the error.
            - `id` (string) **REQ** [maxLen=255] — Record ID
          - `status` (string) **REQ** [enum=['error']] — The status of the response (error).
        - `data` (array of object) [maxItems=10] **REQ** — List of error details
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — The error code identifying the type of error.
          - `message` (string) **REQ** [maxLen=255] — A message describing the error.
          - `details` (object) **REQ** — Error details
            - `reason` (string) **REQ** [enum=['completed_meeting']] — Reason for the error
            - `id` (string) **REQ** [maxLen=255] — Record ID
          - `status` (string) **REQ** [enum=['error']] — Error Status
        - `data` (array of object) [maxItems=10] **REQ** — Contains the list of error details.
          - `code` (string) **REQ** [enum=['CANNOT_PERFORM_ACTION']] — Contains the error code.
          - `message` (string) **REQ** [maxLen=255] — Contains a message describing the error.
          - `details` (object) **REQ** — Error details
          - `status` (string) **REQ** [enum=['error']] — Contains the status of the error.
        - `code` (string) **REQ** [enum=['DAILY_LIMIT_EXCEEDED']] — The error code identifying the type of error.
        - `message` (string) **REQ** [maxLen=255] — A message describing the error.
        - `details` (object) **REQ** — Error details.
        - `status` (string) **REQ** [enum=['error']] — The status of the response (error).
        - `data` (array of object) [maxItems=10] **REQ** — List of error details
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
          - `message` (string) **REQ** [maxLen=255] — Error message
          - `details` (object) **REQ** — Error details
            - `id` (string) **REQ** [maxLen=255] — The invalid record ID
          - `status` (string) **REQ** [enum=['error']] — Error Status
        - `data` (array of object) [maxItems=10] **REQ** — List of error details
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
          - `message` (string) **REQ** [maxLen=255] — Error message
          - `details` (object) **REQ** — Error details
            - `expected_data_type` (string) [maxLen=255] — Expected data type
            - `api_name` (string) **REQ** [maxLen=255] — Detail_field - api_name
            - `json_path` (string) **REQ** [maxLen=255] — Detail_field - json_path
          - `status` (string) **REQ** [enum=['error']] — Error Status
        - `data` (array of object) [maxItems=10] **REQ** — List of error details
          - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code
          - `message` (string) **REQ** [maxLen=255] — Error message
          - `details` (object) **REQ** — Error details
            - `dependee` (object) **REQ** — The field that the current field depends on
              - `api_name` (string) **REQ** [maxLen=255] — Detail_field - api_name
              - `json_path` (string) **REQ** [maxLen=255] — Detail_field - json_path
            - `api_name` (string) **REQ** [maxLen=255] — Detail_field - api_name
            - `json_path` (string) **REQ** [maxLen=255] — Detail_field - json_path
          - `status` (string) **REQ** [enum=['error']] — Error Status

- **401**: The access token is invalid, expired, or does not have the required scope. [application/json]
    oneOf:
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — The error code identifying the type of error.
        - `message` (string) **REQ** [maxLen=255] — A message describing the error.
        - `details` (object) **REQ** — Error details.
        - `status` (string) **REQ** [enum=['error']] — The status of the response (error).

- **403**: Forbidden - The user does not have permission to perform this action. [application/json]
    > permission denied. The user does not have permission to cancel the meeting. Contact your system administrator.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code
    - `message` (string) **REQ** [maxLen=255] — Error message
    - `details` (object) **REQ** — Error details
      - `permissions` (array of string) [maxItems=10] **REQ** — Required permissions
        items: [maxLen=255]
    - `status` (string) **REQ** [enum=['error']] — Error Status

- **404**: The request URL is incorrect or the resource was not found. [application/json]
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — The error code identifying the type of error.
        - `message` (string) **REQ** [maxLen=255] — A message describing the error.
        - `details` (object) **REQ** — Error details.
        - `status` (string) **REQ** [enum=['error']] — The status of the response (error).

**Scopes:** ZohoCRM.Modules.Events.UPDATE

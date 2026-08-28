# PUT /Notes
**Operation:** `updateNotesModule` — Update Notes
> Updates one or more existing note records. Either note content or note title must be provided (at least one is mandatory) for each note.

**Request Body** (required) — application/json
> Request body containing note data to update
  > Request payload for updating notes
  - `data` (array of object) [maxItems=100] **REQ** — Array of note objects to update
    - `id` (string/int64) **REQ** — Unique identifier of the note to update
    - `Note_Content` (string) [maxLen=65535, nullable] — The content/body of the note
    - `Note_Title` (string) [maxLen=120, nullable] — The title of the note
    additionalProperties: any

**Responses:**

- **200**: Success - Note(s) successfully updated [application/json]
    > Success response for note update
    - `data` (array of object) [maxItems=100] **REQ** — Array of update results
      - `code` (string) **REQ** [enum=['SUCCESS']] — Result code
      - `message` (string) **REQ** [maxLen=500] — Result message
      - `status` (string) **REQ** [enum=['success']] — Status of the operation
      - `details` (object) **REQ** — Updated note details
        - `id` (string/int64) **REQ** — Unique identifier of the updated note
        - `Modified_Time` (string/date-time) **REQ** — Timestamp when the note was last modified
        - `Created_Time` (string/date-time) **REQ** — Timestamp recording note creation
        - `Created_By` (object) **REQ** — User who created the note
          - `name` (string) **REQ** [maxLen=255] — Name of the user
          - `id` (string/int64) **REQ** — Unique identifier of the user
        - `Modified_By` (object) **REQ** — User who last modified the note
          - `name` (string) **REQ** [maxLen=255] — Name of the user
          - `id` (string/int64) **REQ** — Unique identifier of the user

- **207**: Multi-Status - Partial success with some records updated and some failed [application/json]
    > Multi-status response for note update with mixed results
    - `data` (array of object) [maxItems=100] **REQ** — Array of update results with mixed success and error statuses
      oneOf:
          - `code` (string) **REQ** [enum=['SUCCESS']] — Result code
          - `message` (string) **REQ** [maxLen=500] — Result message
          - `status` (string) **REQ** [enum=['success']] — Status of the operation
          - `details` (object) **REQ** — Updated note details
            - `id` (string/int64) **REQ** — Unique identifier of the updated note
            - `Modified_Time` (string/date-time) **REQ** — Timestamp when the note was last modified
            - `Created_Time` (string/date-time) **REQ** — Timestamp recording note creation
            - `Created_By` (object) **REQ** — User who created the note
              - `name` (string) **REQ** [maxLen=255] — Name of the user
              - `id` (string/int64) **REQ** — Unique identifier of the user
            - `Modified_By` (object) **REQ** — User who last modified the note
              - `name` (string) **REQ** [maxLen=255] — Name of the user
              - `id` (string/int64) **REQ** — Unique identifier of the user
          - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING', 'MANDATORY_NOT_FOUND', 'INVALID_DATA']] — Error code
          - `message` (string) **REQ** [maxLen=500] — Error message
          - `status` (string) **REQ** [enum=['error']] — Status of the operation
          - `details` (object) **REQ** — Error details

- **400**: Bad Request - Invalid parameters or malformed request [application/json]
    oneOf:
      - `ExpectedFieldMissingError` — Error response for missing expected fields
        - `data` (array of object) [maxItems=100] **REQ** — Array of error results
          - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Error code indicating the type of error
          - `details` (object) **REQ** — Additional details about the error
            - `expected_fields` (array of object) [maxItems=2] **REQ** — List of expected fields that are missing
              - `api_name` (string) **REQ** [maxLen=255] — API name of the expected field
              - `json_path` (string) **REQ** [maxLen=500] — JSON path to the expected field
          - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
          - `status` (string) **REQ** [enum=['error']] — Status of the response
      - `MandatoryNotFoundError` — Error response for mandatory field not found
        - `data` (array of object) [maxItems=100] **REQ** — Array of error results
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code indicating the type of error
          - `details` (object) **REQ** — Additional details about the error
            - `api_name` (string) **REQ** [maxLen=255] — The API name of the missing mandatory field
            - `json_path` (string) **REQ** [maxLen=500] — The JSON path to the missing field
          - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
          - `status` (string) **REQ** [enum=['error']] — Status of the response
      - `InvalidDataError` — Error response for invalid field data
        - `data` (array of object) [maxItems=100] **REQ** — Array of error results
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating the type of error
          - `details` (object) **REQ** — Additional details about the error, can include various constraint information
          - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
          - `status` (string) **REQ** [enum=['error']] — Status of the response
      - `InvalidDataLimitExceededError` — Error response when data array exceeds maximum limit
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating the type of error
        - `details` (object) **REQ** — Additional details about the error
          - `maximum_length` (integer/int32) **REQ** — Maximum allowed number of elements in data array
          - `api_name` (string) **REQ** [maxLen=255] — API name of the field that exceeded the limit
          - `json_path` (string) **REQ** [maxLen=500] — JSON path to the field that exceeded the limit
        - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
        - `status` (string) **REQ** [enum=['error']] — Status of the response
      - `NotAllowedError` — Error response when operation is not allowed
        - `data` (array of object) [maxItems=100] **REQ** — Array of error results
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code indicating the type of error
          - `details` (object) **REQ** — Additional details about the error
            - `api_name` (string) **REQ** [maxLen=255] — API name of the field
            - `json_path` (string) **REQ** [maxLen=500] — JSON path to the field
          - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
          - `status` (string) **REQ** [enum=['error']] — Status of the response
      - `CannotPerformActionError` — Error response when user cannot perform action on a record
        - `data` (array of object) [maxItems=100] **REQ** — Array of error results
          - `code` (string) **REQ** [enum=['CANNOT_PERFORM_ACTION']] — Error code indicating the type of error
          - `details` (object) **REQ** — Additional details about the error
          - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
          - `status` (string) **REQ** [enum=['error']] — Status of the response

- **401**: Unauthorized - Authentication failed [application/json]
    > Error response for authentication failures
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE', 'OAUTH_SCOPE_MISMATCH']] — Error code indicating the type of error
    - `details` (object) **REQ** — Additional details about the error
    - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
    - `status` (string) **REQ** [enum=['error']] — Status of the response

- **404**: Not Found - The requested resource does not exist [application/json]
    > Error response for not found requests
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Error code indicating the type of error
    - `details` (object) **REQ** — Additional details about the error
    - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
    - `status` (string) **REQ** [enum=['error']] — Status of the response

- **500**: Internal Server Error - An unexpected error occurred on the server [application/json]
    > Error response for internal server errors
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Error code indicating the type of error
    - `details` (object) **REQ** — Additional details about the error
    - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
    - `status` (string) **REQ** [enum=['error']] — Status of the response

**Scopes:** ZohoCRM.modules.notes.UPDATE

# POST /Notes
**Operation:** `createNotesModule` — Create Notes
> Creates one or more note records.

**Request Body** (required) — application/json
> Request body containing note data to create
  > Request payload for creating notes
  - `data` (array of object) [maxItems=100] **REQ** — Array of note objects to create
    - `Note_Content` (string) [maxLen=65535, nullable] — The content/body of the note
    - `Note_Title` (string) [maxLen=120, nullable] — The title of the note
    - `Parent_Id` (object) — Parent record information
      - `module` (object) **REQ** — Module information of the parent record
        - `api_name` (string) [maxLen=50] — API name of the parent module
        - `id` (string/int64) — Module ID
      - `id` (string/int64) **REQ** — Unique identifier of the parent record
    additionalProperties: any

**Responses:**

- **201**: Created - Note(s) successfully created [application/json]
    > Success response for note creation
    - `data` (array of object) [maxItems=100] **REQ** — Array of creation results
      - `code` (string) **REQ** [enum=['SUCCESS']] — Result code
      - `message` (string) **REQ** [maxLen=500] — Result message
      - `status` (string) **REQ** [enum=['success']] — Status of the operation
      - `details` (object) **REQ** — Created note details
        - `id` (string/int64) **REQ** — Unique identifier of the created note
        - `Modified_Time` (string/date-time) **REQ** — Timestamp when the note was last modified
        - `Created_Time` (string/date-time) **REQ** — Timestamp recording note creation
        - `Created_By` (object) **REQ** — User who created the note
          - `name` (string) **REQ** [maxLen=120] — Name of the user
          - `id` (string/int64) **REQ** — Unique identifier of the user
        - `Modified_By` (object) **REQ** — User who last modified the note
          - `name` (string) **REQ** [maxLen=255] — Name of the user
          - `id` (string/int64) **REQ** — Unique identifier of the user

- **207**: Multi-Status - Partial success with some records created and some failed [application/json]
    > Multi-status response for note creation with mixed results
    - `data` (array of object) [maxItems=100] **REQ** — Array of creation results with mixed success and error statuses
      oneOf:
          - `code` (string) **REQ** [enum=['SUCCESS']] — Result code
          - `message` (string) **REQ** [maxLen=500] — Result message
          - `status` (string) **REQ** [enum=['success']] — Status of the operation
          - `details` (object) **REQ** — Created note details
            - `id` (string/int64) **REQ** — Unique identifier of the created note
            - `Modified_Time` (string/date-time) **REQ** — Timestamp when the note was last modified
            - `Created_Time` (string/date-time) **REQ** — Timestamp recording note creation
            - `Created_By` (object) **REQ** — User who created the note
              - `name` (string) **REQ** [maxLen=255] — Name of the user
              - `id` (string/int64) **REQ** — Unique identifier of the user
            - `Modified_By` (object) **REQ** — User who last modified the note
              - `name` (string) **REQ** [maxLen=255] — Name of the user
              - `id` (string/int64) **REQ** — Unique identifier of the user
          - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING', 'INVALID_DATA']] — Error code
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
      - `FileSizeExceedsError` — Error response when attachment file size exceeds the limit
        - `data` (array of object) [maxItems=100] **REQ** — Array of error results
          - `code` (string) **REQ** [enum=['FILE_SIZE_EXCEEDS']] — Error code indicating the type of error
          - `details` (object) **REQ** — Additional details about the error
            - `api_name` (string) **REQ** [maxLen=255] — API name of the field
            - `json_path` (string) **REQ** [maxLen=255] — JSON path to the field
          - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
          - `status` (string) **REQ** [enum=['error']] — Status of the response

- **401**: Unauthorized - Authentication failed [application/json]
    > Error response for authentication failures
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE', 'OAUTH_SCOPE_MISMATCH']] — Error code indicating the type of error
    - `details` (object) **REQ** — Additional details about the error
    - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
    - `status` (string) **REQ** [enum=['error']] — Status of the response

- **403**: Forbidden - User lacks required permissions — Schema: `NoPermissionError` [application/json]
    > Error response when user lacks required permissions
    schema: `NoPermissionError`
    - `data` (array of object) [maxItems=100] **REQ** — Array of error results
      - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code indicating the type of error
      - `details` (object) **REQ** — Additional details about required permissions
        - `permissions` (array of string) [maxItems=10] **REQ** — List of required permissions
          items: [maxLen=255]
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

**Scopes:** ZohoCRM.modules.notes.CREATE

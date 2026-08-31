# PUT /Notes/{id}
**Operation:** `updateNoteById` — Update a Specific Note
> Updates a specific note by its ID. Either note content or note title must be provided (at least one is mandatory).

**Parameters:**
- `id` (path, string/int64, required): Unique identifier of the note. Use the [Get Notes API](notes.yaml#$.paths./Notes.get) to retrieve the note IDs.

**Request Body** (required) — application/json
> Request body containing note data to update
  > Request payload for updating a note
  - `data` (array of object) [maxItems=1] **REQ** — Array containing the note to update (single item only)
    - `Note_Content` (string) [maxLen=65535, nullable] — The content/body of the note
    - `Note_Title` (string) [maxLen=120, nullable] — The title of the note
    additionalProperties: any

**Responses:**

- **200**: Success - Note successfully updated [application/json]
    > Success response for note update
    - `data` (array of object) [maxItems=1] **REQ** — Array of update results
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

- **400**: Bad Request - Invalid parameters or malformed request [application/json]
    oneOf:
      - `ExpectedFieldMissingErrorSingle` — Error response for missing expected fields in single record operations
        - `data` (array of object) [maxItems=1] **REQ** — Array of error results for single record
          - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Error code indicating the type of error
          - `details` (object) **REQ** — Additional details about the error
            - `expected_fields` (array of object) [maxItems=2] **REQ** — List of expected fields that are missing
              - `api_name` (string) [maxLen=255] — API name of the expected field
              - `json_path` (string) [maxLen=500] — JSON path to the expected field
          - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
          - `status` (string) **REQ** [enum=['error']] — Status of the response
      - `InvalidDataErrorSingle` — Error response for invalid data in single record operations
        - `data` (array of object) [maxItems=1] **REQ** — Array of error results for single record
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating the type of error
          - `details` (object) **REQ** — Additional details about the error
          - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
          - `status` (string) **REQ** [enum=['error']] — Status of the response
      - `InvalidIdError` — Error response when an invalid record ID is provided
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating the type of error
        - `details` (object) **REQ** — Additional details about the error
          - `resource_path_index` (integer/int32) **REQ** — Index in the resource path where the invalid ID was found
        - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
        - `status` (string) **REQ** [enum=['error']] — Status of the response
      - `NotAllowedErrorSingle` — Error response when operation is not allowed in single record operations
        - `data` (array of object) [maxItems=1] **REQ** — Array of error results for single record
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code indicating the type of error
          - `details` (object) **REQ** — Additional details about the error
            - `api_name` (string) **REQ** [maxLen=255] — API name of the field
            - `json_path` (string) **REQ** [maxLen=500] — JSON path to the field
          - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
          - `status` (string) **REQ** [enum=['error']] — Status of the response
      - `CannotPerformActionErrorSingle` — Error response when user cannot perform action on a record in single record operations
        - `data` (array of object) [maxItems=1] **REQ** — Array of error results for single record
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

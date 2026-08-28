# DELETE /Notes
**Operation:** `deleteNotesModule` — Notes
> Permanently deletes one or more notes using comma-separated note IDs.

**Parameters:**
- `ids` (query, string, optional) [maxLen=1024]: Comma-separated list of note IDs to retrieve specific notes. Use the [Get Notes API](notes.yaml#$.paths./Notes.get) to retrieve the note IDs.

**Responses:**

- **200**: Success - Note(s) successfully deleted [application/json]
    > Success response for note deletion
    - `data` (array of object) [maxItems=100] **REQ** — Array of deletion results
      - `code` (string) **REQ** [enum=['SUCCESS']] — Result code
      - `message` (string) **REQ** [maxLen=500] — Result message
      - `status` (string) **REQ** [enum=['success']] — Status of the operation
      - `details` (object) **REQ** — Deleted note details
        - `id` (string/int64) **REQ** — Unique identifier of the deleted note

- **207**: Multi-Status - Partial success with some records deleted and some failed [application/json]
    > Multi-status response for note deletion with mixed results
    - `data` (array of object) [maxItems=100] **REQ** — Array of deletion results with mixed success and error statuses
      oneOf:
          - `code` (string) **REQ** [enum=['SUCCESS']] — Result code
          - `message` (string) **REQ** [maxLen=500] — Result message
          - `status` (string) **REQ** [enum=['success']] — Status of the operation
          - `details` (object) **REQ** — Deleted note details
            - `id` (string/int64) **REQ** — Unique identifier of the deleted note
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
          - `message` (string) **REQ** [maxLen=500] — Error message
          - `status` (string) **REQ** [enum=['error']] — Status of the operation
          - `details` (object) **REQ** — Error details
            - `id` (string/int64) — Unique identifier of the note that failed to delete
            additionalProperties: any

- **400**: Bad Request - Invalid parameters or missing required parameter [application/json]
    oneOf:
      - `RequiredParamMissingError` — Error response for required parameter missing
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Error code indicating the type of error
        - `details` (object) **REQ** — Additional details about the error
          - `param_name` (string) [maxLen=255] — The name of the missing parameter
          additionalProperties: any
        - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
        - `status` (string) **REQ** [enum=['error']] — Status of the response
      - `InvalidDataError` — Error response for invalid field data
        - `data` (array of object) [maxItems=100] **REQ** — Array of error results
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating the type of error
          - `details` (object) **REQ** — Additional details about the error, can include various constraint information
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

**Scopes:** ZohoCRM.modules.notes.DELETE

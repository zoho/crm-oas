# DELETE /Notes/{id}
**Operation:** `deleteNoteById` — Delete a Specific Note
> Permanently deletes a specific note by its ID.

**Parameters:**
- `id` (path, string/int64, required): Unique identifier of the note. Use the [Get Notes API](notes.yaml#$.paths./Notes.get) to retrieve the note IDs.

**Responses:**

- **200**: Success - Note successfully deleted [application/json]
    > Success response for note deletion
    - `data` (array of object) [maxItems=1] **REQ** — Array of deletion results
      - `code` (string) **REQ** [enum=['SUCCESS']] — Result code
      - `message` (string) **REQ** [maxLen=500] — Result message
      - `status` (string) **REQ** [enum=['success']] — Status of the operation
      - `details` (object) **REQ** — Deleted note details
        - `id` (string/int64) **REQ** — Unique identifier of the deleted note

- **400**: Bad Request - Invalid data [application/json]
    oneOf:
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

# GET /Notes/{id}
**Operation:** `getNoteById` — Get a Specific Note
> Retrieves details of a specific note by its ID.

**Parameters:**
- `id` (path, string/int64, required): Unique identifier of the note. Use the [Get Notes API](notes.yaml#$.paths./Notes.get) to retrieve the note IDs.
- `fields` (query, string, optional) [maxLen=1024]: Comma-separated list of field API names to include in the response

**Responses:**

- **200**: Successfully retrieved the note [application/json]
    > Response containing a single note
    - `data` (array of object) [maxItems=1] **REQ** — Array containing the single requested note
      - `id` (string/int64) **REQ** — Unique identifier of the note
      - `Note_Title` (string) [maxLen=120, nullable] — The title of the note
      - `Note_Content` (string) [maxLen=65535] — The content/body of the note
      - `$attachments` (array of object) [maxItems=5, nullable] — Attachments associated with the note
        - `$file_id` (string) [maxLen=255] — Unique file identifier for the attachment
        - `File_Name` (string) [maxLen=255] — Name of the attached file
        - `Size` (string/int64) — File size in bytes
        - `id` (string/int64) — Unique identifier of the attachment record
        additionalProperties: any
      - `Parent_Id` (object) — Parent record information
        - `module` (object) **REQ** — Module information of the parent record
          - `api_name` (string) **REQ** [maxLen=50] — API name of the parent module
          - `id` (string/int64) **REQ** — Module ID
        - `name` (string) **REQ** [maxLen=255] — Name of the parent record
        - `id` (string/int64) **REQ** — Unique identifier of the parent record
      additionalProperties: any

- **204**: No content - The request was successful but there are no records to return

- **400**: Bad Request - Invalid parameters or malformed request — Schema: `RequiredParamMissingError` [application/json]
    > Error response for required parameter missing
    schema: `RequiredParamMissingError`
    - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Error code indicating the type of error
    - `details` (object) **REQ** — Additional details about the error
      - `param_name` (string) [maxLen=255] — The name of the missing parameter
      additionalProperties: any
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

**Scopes:** ZohoCRM.modules.notes.READ

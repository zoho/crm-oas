# GET /Notes
**Operation:** `getNotesModule` — Notes
> Retrieves a list of notes.

**Parameters:**
- `fields` (query, string, optional) [maxLen=1024]: Comma-separated list of field API names to include in the response
- `ids` (query, string, optional) [maxLen=1024]: Comma-separated list of note IDs to retrieve specific notes. Use the [Get Notes API](notes.yaml#$.paths./Notes.get) to retrieve the note IDs.
- `per_page` (query, integer/int32, optional): Number of records per page
- `page` (query, integer/int32, optional): Page number for pagination
- `page_token` (query, string, optional) [maxLen=2000]: Page token for retrieving records beyond the 2000-record limit.
- `sort_order` (query, string, optional) [enum=['asc', 'desc']]: Sort order (ascending or descending)
- `sort_by` (query, string, optional) [enum=['Modified_Time', 'Created_Time', 'id']]: Field name to sort results by

**Responses:**

- **200**: Successful response with note records [application/json]
    > Response containing note data and pagination information
    - `data` (array of object) [maxItems=200] **REQ** — Array of note records
      - `id` (string/int64) **REQ** — Unique identifier of the note
      - `Note_Title` (string) [maxLen=120, nullable] — The title of the note
      - `Note_Content` (string) [maxLen=65535, nullable] — The content/body of the note
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
    - `info` (object) **REQ** — Pagination metadata
      - `page` (integer/int32) **REQ** — Current page number
      - `per_page` (integer/int32) **REQ** — Number of records per page
      - `count` (integer/int32) **REQ** — Number of records in current page
      - `more_records` (boolean) **REQ** — Indicates if more records are available
      - `next_page_token` (string) [maxLen=2000, nullable] — Token for retrieving the next page of note records.
      - `previous_page_token` (string) [maxLen=2000, nullable] — Token for retrieving the previous page of note records.
      - `page_token_expiry` (string/date-time) [nullable] — Expiry time of page tokens
      - `sort_by` (string) [maxLen=50] — Field by which the results are sorted
      - `sort_order` (string) [enum=['asc', 'desc']] — Sort order of the results

- **204**: No content - The request was successful but there are no records to return

- **400**: Bad Request - Invalid parameters or malformed request [application/json]
    oneOf:
      - `RequiredParamMissingError` — Error response for required parameter missing
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Error code indicating the type of error
        - `details` (object) **REQ** — Additional details about the error
          - `param_name` (string) [maxLen=255] — The name of the missing parameter
          additionalProperties: any
        - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
        - `status` (string) **REQ** [enum=['error']] — Status of the response
      - `DiscretePaginationLimitExceededError` — Error response for pagination limit exceeded
        - `code` (string) **REQ** [enum=['DISCRETE_PAGINATION_LIMIT_EXCEEDED']] — Error code indicating the type of error
        - `details` (object) **REQ** — Additional details about the pagination limit
          - `limit` (integer/int32) — Maximum number of records that can be retrieved without page_token
          additionalProperties: any
        - `message` (string) **REQ** [maxLen=500] — Error message returned when the operation fails.
        - `status` (string) **REQ** [enum=['error']] — Status of the response
      - `ExpiredValueError` — Error response when a token or value has expired
        - `code` (string) **REQ** [enum=['EXPIRED_VALUE']] — Error code indicating the type of error
        - `details` (object) **REQ** — Additional details about the expired value
          - `param_name` (string) **REQ** [maxLen=100] — Name of the parameter with expired value
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

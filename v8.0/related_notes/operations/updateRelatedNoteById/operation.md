# PUT /{parentRecordModule}/{parentRecordId}/Notes/{noteId}
**Operation:** `updateRelatedNoteById` — Related Note
> Updates an existing note associated with a specific parent record. Either note content or note title must be provided (at least one is mandatory).

**Parameters:**
- `parentRecordModule` (path, string, required) [maxLen=50, pattern=^[A-Za-z_][A-Za-z0-9_]*$]: Specify the API name of the parent record module. Refer to [Get Modules](modules.yaml#$.paths./settings/modules.get) for the list of supported modules.
- `parentRecordId` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique numeric ID of the parent record.
- `noteId` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique numeric ID of the note record.

**Request Body** (required) — application/json
> The request body must contain a data array with one note object including at least one of Note_Title or Note_Content.
  > Request payload for updating the title and content of a specific note.
  - `data` (array of object) [maxItems=1] **REQ** — Specify the note fields to update.
    - `Note_Content` (string) [maxLen=65535] — Specify the updated content of the note.
    - `Note_Title` (string) [maxLen=120] — Specify the updated title of the note.
    additionalProperties: any

**Responses:**

- **200**: Returns the action status and details of the updated note. [application/json]
    > Success response for single note update, containing the action status and details of the updated note.
    - `data` (array of object) [maxItems=200] **REQ** — Represents the list of action status objects for the updated note.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for this note update.
      - `message` (string) **REQ** [maxLen=500] — Represents the result message for this note update.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of this note update.
      - `details` (object) **REQ** — Contains the details of the updated note record.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the updated note.
        - `Modified_Time` (string/date-time) **REQ** — Represents the date and time when the note was last modified.
        - `Created_Time` (string/date-time) **REQ** — Represents the creation date and time of the note.
        - `Created_By` (object) **REQ** — Represents the user who created the note.
          - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who created the note.
          - `id` (string/int64) **REQ** — Represents the ID of the user who created the note.
        - `Modified_By` (object) **REQ** — Represents the user who last modified the note.
          - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who last modified the note.
          - `id` (string/int64) **REQ** — Represents the ID of the user who last modified the note.

- **400**: The request data is invalid. Resolution: Ensure the request body includes valid values and that at least one of Note_Title or Note_Content is provided. [application/json]
    > Validation error response for the PUT single note update request.
    oneOf:
      - `BadRequestError` — Error response schema for 400 bad request errors, covering INVALID_MODULE, INVALID_DATA, and NOT_SUPPORTED error codes.
        - `code` (string) **REQ** [enum=['INVALID_MODULE', 'INVALID_DATA', 'NOT_SUPPORTED']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional details about the error.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
        - `status` (string) **REQ** [enum=['error']] — Indicates the status of the response.
      - `ExpectedFieldMissingError` — Error response schema returned when both Note_Content and Note_Title are absent from the request, violating the at-least-one requirement.
        - `data` (array of object) [maxItems=200] **REQ** — Represents the list of error objects for each note in the request.
          - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Represents the error code for this response.
          - `details` (object) **REQ** — Contains the list of expected fields that are missing from the request.
            - `expected_fields` (array of object) [maxItems=2] **REQ** — A list of fields from which at least one must be provided. Returned when none of the required fields are present in the request.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing expected field.
              - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the missing expected field.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
          - `status` (string) **REQ** [enum=['error']] — The status of the response.
      - `NotAllowedErrorSingle` — Error response schema for single-record update operations where the action is not permitted on the specified note.
        - `data` (array of object) [maxItems=1] **REQ** — Represents the list of error objects for the note in the request.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this response.
          - `details` (object) **REQ** — Contains additional details identifying the field on which the operation is not allowed.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the not-allowed operation.
            - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field associated with the not-allowed operation.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `CannotPerformActionErrorSingle` — Error response schema for single-record operations where the user cannot perform the requested action on the specified note.
        - `data` (array of object) [maxItems=1] **REQ** — Represents the list of error objects for the note in the request.
          - `code` (string) **REQ** [enum=['CANNOT_PERFORM_ACTION']] — Represents the error code for this response.
          - `details` (object) **REQ** — Contains additional details about the cannot-perform-action error.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

- **401**: Authentication failed. Resolution: Verify that the OAuth token is valid and that the required scope is included. [application/json]
    > Error response schema for 401 Unauthorized responses.
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE', 'OAUTH_SCOPE_MISMATCH']] — Represents the error code for this response.
    - `details` (object) **REQ** — Contains additional details about the error.
    - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

- **404**: The requested resource could not be found. Resolution: Verify that the URL pattern in the request is correct. [application/json]
    > Error response schema for 404 Not Found responses.
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code for this response.
    - `details` (object) **REQ** — Contains additional details about the error.
    - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
    - `status` (string) **REQ** [enum=['error']] — Indicates status of the response.

- **500**: An unexpected error occurred on the server. Resolution: Retry the request after a brief delay. If the error persists, contact Zoho CRM support. [application/json]
    > Error response schema for 500 Internal Server Error responses.
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Represents the error code for this response.
    - `details` (object) **REQ** — Contains additional details about the error.
    - `message` (string) **REQ** [maxLen=500] — Specifies the error message for this response.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

**Scopes:** ZohoCRM.modules.Leads.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Contacts.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Accounts.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Deals.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Tasks.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Events.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Calls.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Products.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Vendors.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Campaigns.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Cases.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Solutions.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Pricebooks.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Quotes.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Salesorders.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Purchaseorders.READ, ZohoCRM.modules.notes.UPDATE, ZohoCRM.modules.Custom.READ, ZohoCRM.modules.notes.UPDATE

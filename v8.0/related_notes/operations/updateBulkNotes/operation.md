# PUT /{parentRecordModule}/{parentRecordId}/Notes
**Operation:** `updateBulkNotes` — Related Notes
> Updates one or more notes associated with a specific CRM record in your Zoho CRM organization. Either note content or note title must be provided (at least one is mandatory) for each note.

**Parameters:**
- `parentRecordModule` (path, string, required) [maxLen=50, pattern=^[A-Za-z_][A-Za-z0-9_]*$]: Specify the API name of the parent record module. Refer to [Get Modules](modules.yaml#$.paths./settings/modules.get) for the list of supported modules.
- `parentRecordId` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique numeric ID of the parent record.

**Request Body** (required) — application/json
> The request body must contain a data array with one or more note objects, each including a valid note ID.
  > Request payload for updating one or more notes.
  - `data` (array of object) [maxItems=200] **REQ** — Specify the notes to update.
    - `id` (string/int64) **REQ** — Specify the unique identifier of the note to update.
    - `Note_Content` (string) [maxLen=65535] — Specify the updated content of the note.
    - `Note_Title` (string) [maxLen=120] — Specify the updated title of the note.
    additionalProperties: any

**Responses:**

- **200**: Returns the action status for each updated note. [application/json]
    > Success response for bulk note update, containing the action status for each updated note.
    - `data` (array of object) [maxItems=200] **REQ** — Represents the list of action status objects for each note updated in this request.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for this note update.
      - `message` (string) **REQ** [maxLen=500] — Indicates the result message for this note update.
      - `status` (string) **REQ** [enum=['success']] — Specifies the status of this note update.
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

- **207**: Returns mixed results where some notes were updated successfully and others failed. [application/json]
    > Mixed-status response for bulk note update where some notes were updated successfully and others failed.
    - `data` (array of object) [maxItems=200] **REQ** — Represents the list of mixed action status objects for each note in this request.
      oneOf:
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
          - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING', 'MANDATORY_NOT_FOUND', 'INVALID_DATA']] — Represents the error code for this note update failure.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message for this note update failure.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of this note update failure.
          - `details` (object) **REQ** — Contains additional details about the note update error.

- **400**: The request data is invalid. Resolution: Ensure each note object includes a valid ID and at least one of Note_Title or Note_Content. [application/json]
    > Validation error response for the PUT bulk update notes request.
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
      - `MandatoryNotFoundError` — Error response schema returned when a mandatory field, such as `id`, is missing from the request body.
        - `data` (array of object) [maxItems=200] **REQ** — Represents the list of error objects for each note in the request.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this response.
          - `details` (object) **REQ** — Contains additional details identifying the missing mandatory field.
            - `api_name` (string) [maxLen=255] — Represents the API name of the missing mandatory field.
            - `json_path` (string) [maxLen=500] — Specifies the JSON path to the missing mandatory field.
            additionalProperties: any
          - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `InvalidDataError` — Error response schema returned when a field value fails validation, such as exceeding the maximum length.
        - `data` (array of object) [maxItems=200] **REQ** — Represents the list of error objects for each note in the request.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
          - `details` (object) **REQ** — Contains additional validation details about the invalid field, including constraint information.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `NotAllowedError` — Error response schema returned when an operation is not permitted, such as sharing a note with a portal user whose parent record is inaccessible.
        - `data` (array of object) [maxItems=200] **REQ** — Represents the list of error objects for each note in the request.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this response.
          - `details` (object) **REQ** — Contains additional details identifying the field on which the operation is not allowed.
            - `api_name` (string) **REQ** [maxLen=255] — The API name of the field associated with the not-allowed operation.
            - `json_path` (string) **REQ** [maxLen=500] — The JSON path to the field associated with the not-allowed operation.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `CannotPerformActionError` — Error response schema returned when the user lacks permission to perform the requested action on a note, such as modifying another user's note.
        - `data` (array of object) [maxItems=200] **REQ** — Represents the list of error objects for each note in the request.
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

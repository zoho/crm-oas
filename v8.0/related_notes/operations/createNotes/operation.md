# POST /{parentRecordModule}/{parentRecordId}/Notes
**Operation:** `createNotes` — Related Notes
> Creates one or more notes associated with a specific parent record. Either note content or note title must be provided (at least one is mandatory).

**Parameters:**
- `parentRecordModule` (path, string, required) [maxLen=50, pattern=^[A-Za-z_][A-Za-z0-9_]*$]: Specify the API name of the parent record module. Refer to [Get Modules](modules.yaml#$.paths./settings/modules.get) for the list of supported modules.
- `parentRecordId` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique numeric ID of the parent record.

**Request Body** (required) — application/json
> The request body must contain a data array with one or more note objects.
  > Request payload for creating one or more notes.
  - `data` (array of object) [maxItems=200] **REQ** — A JSON array containing the notes to create.
    - `Note_Content` (string) [maxLen=65535] — Specify the content of the note.
    - `Note_Title` (string) [maxLen=120] — Provide the title of the note.
    - `Parent_Id` (object) — Specify the parent record for this note.
      - `module` (object) **REQ** — Represents the details of the requested module. It is mandatory to specify either the API name or the unique ID of the requested module. Refer to [GET Modules API](modules.yaml#$.paths./settings/modules.get)  to get the details.
        - `api_name` (string) [maxLen=50] — Specify the API name of the parent record module. Refer to [Get Modules](modules.yaml#$.paths./settings/modules.get) for the list of supported modules.
        - `id` (string/int64) — Specify the unique identifier of the parent record module.
      - `id` (string/int64) **REQ** — Specify the unique ID of the parent record. Refer to Refer the [GET Records API](record.yaml#.$path./{module}.get) to get valid record IDs.
    additionalProperties: any

**Responses:**

- **201**: Returns the action status for each newly created note. [application/json]
    > Success response for note creation, containing the action status for each created note.
    - `data` (array of object) [maxItems=200] **REQ** — JSON array representing the list of action status objects for each note created in this request.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for this note creation.
      - `message` (string) **REQ** [maxLen=500] — Represents the result message for this note creation.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of this note creation.
      - `details` (object) **REQ** — Contains the details of the created note record.
        - `id` (string/int64) **REQ** — The unique identifier of the created note.
        - `Modified_Time` (string/date-time) **REQ** — Specifies the date and time when the note was last modified.
        - `Created_Time` (string/date-time) **REQ** — Represents the creation date and time of the note.
        - `Created_By` (object) **REQ** — Specifies the user who created the note.
          - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who created the note.
          - `id` (string/int64) **REQ** — Indicaates the ID of the user who created the note.
        - `Modified_By` (object) **REQ** — Represents the user who last modified the note.
          - `name` (string) **REQ** [maxLen=255] — Specifies the name of the user who last modified the note.
          - `id` (string/int64) **REQ** — Represents the ID of the user who last modified the note.

- **207**: Returns mixed results where some notes were created successfully and others failed validation. [application/json]
    > Mixed-status response for note creation where some notes were created successfully and others failed.
    - `data` (array of object) [maxItems=200] **REQ** — JSON array representing the list of mixed action status objects for each note in this request.
      oneOf:
          - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for this note creation.
          - `message` (string) **REQ** [maxLen=500] — Represents the result message for this note creation.
          - `status` (string) **REQ** [enum=['success']] — Represents the status of this note creation.
          - `details` (object) **REQ** — Contains the details of the created note record.
            - `id` (string/int64) **REQ** — Represents the unique identifier of the created note.
            - `Modified_Time` (string/date-time) **REQ** — Represents the date and time when the note was last modified.
            - `Created_Time` (string/date-time) **REQ** — Represents the creation date and time of the note.
            - `Created_By` (object) **REQ** — Represents the user who created the note.
              - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who created the note.
              - `id` (string/int64) **REQ** — Represents the ID of the user who created the note.
            - `Modified_By` (object) **REQ** — Represents the user who last modified the note.
              - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who last modified the note.
              - `id` (string/int64) **REQ** — Represents the ID of the user who last modified the note.
          - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING', 'INVALID_DATA']] — Represents the error code for this note creation failure.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message for this note creation failure.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of this note creation failure.
          - `details` (object) **REQ** — Contains additional details about the note creation error.

- **400**: The request data is invalid. Resolution: Ensure the request body contains valid field values, and that at least one of Note_Title or Note_Content is provided. [application/json]
    > Validation error response for the POST create notes request.
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
      - `FileSizeExceedsError` — Error response schema returned when the total size of attachments in the request exceeds the 20 MB limit.
        - `data` (array of object) [maxItems=200] **REQ** — Represents the list of error objects for each note in the request.
          - `code` (string) **REQ** [enum=['FILE_SIZE_EXCEEDS']] — Represents the error code for this response.
          - `details` (object) **REQ** — Contains additional details identifying the attachment field that exceeded the size limit.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the attachment field that exceeded the size limit.
            - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path to the attachment field that exceeded the size limit.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

- **401**: Authentication failed. Resolution: Verify that the OAuth token is valid and that the required scope is included. [application/json]
    > Error response schema for 401 Unauthorized responses.
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE', 'OAUTH_SCOPE_MISMATCH']] — Represents the error code for this response.
    - `details` (object) **REQ** — Contains additional details about the error.
    - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

- **403**: Permission denied to create notes. Resolution: Verify that the OAuth token includes the ZohoCRM.modules.notes.CREATE scope. — Schema: `NoPermissionError` [application/json]
    > Error response schema returned when the user does not have the required permission to perform the operation, such as the Crm_Implied_Create_Attachments permission.
    schema: `NoPermissionError`
    - `data` (array of object) [maxItems=200] **REQ** — Represents the list of error objects for each note in the request.
      - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for this response.
      - `details` (object) **REQ** — Contains the list of required permissions that the user does not have.
        - `permissions` (array of string) [maxItems=10] **REQ** — Represents the list of required permissions for this operation.
          items: [maxLen=255]
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

**Scopes:** ZohoCRM.modules.Leads.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Contacts.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Accounts.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Deals.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Tasks.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Events.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Calls.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Products.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Vendors.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Campaigns.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Cases.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Solutions.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Pricebooks.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Quotes.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Salesorders.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Purchaseorders.READ, ZohoCRM.modules.notes.CREATE, ZohoCRM.modules.Custom.READ, ZohoCRM.modules.notes.CREATE

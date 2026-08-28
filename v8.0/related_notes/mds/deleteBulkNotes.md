# DELETE /{parentRecordModule}/{parentRecordId}/Notes
**Operation:** `deleteBulkNotes` — Related Notes
> Deletes one or more notes associated with a specific parent record using comma-separated note IDs in the query parameter.

**Parameters:**
- `parentRecordModule` (path, string, required) [maxLen=50, pattern=^[A-Za-z_][A-Za-z0-9_]*$]: Specify the API name of the parent record module. Refer to [Get Modules](modules.yaml#$.paths./settings/modules.get) for the list of supported modules.
- `parentRecordId` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique numeric ID of the parent record.
- `ids` (query, string, required) [maxLen=2000, pattern=^[0-9]+(,[0-9]+)*$]: Specify a comma-separated list of note record IDs to delete.

**Responses:**

- **200**: Returns the action status for each deleted note. [application/json]
    > Success response for bulk note deletion, containing the action status for each deleted note.
    - `data` (array of object) [maxItems=200] **REQ** — JSON array representing the list of action status objects for each note deleted in this request.
      - `code` (string) **REQ** [enum=['SUCCESS']] — The result code indicating the outcome of the requested note deletion.
      - `message` (string) **REQ** [maxLen=500] — Represents the result message for this requested note deletion
      - `status` (string) **REQ** [enum=['success']] — Represents the status of this requested note deletion.
      - `details` (object) **REQ** — Contains the details of the deleted note record.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the deleted note.

- **207**: Returns mixed results where some notes were deleted successfully and others failed. [application/json]
    > Mixed-status response for bulk note deletion where some notes were deleted successfully and others failed.
    - `data` (array of object) [maxItems=200] **REQ** — Represents the list of mixed action status objects for each note in this request.
      oneOf:
          - `code` (string) **REQ** [enum=['SUCCESS']] — The result code indicating the outcome of deleting the requested note.
          - `message` (string) **REQ** [maxLen=500] — Represents the result message for deleting the requested note.
          - `status` (string) **REQ** [enum=['success']] — Represents the status of deleting the note.
          - `details` (object) **REQ** — Contains the details of the deleted note record.
            - `id` (string/int64) **REQ** — Represents the unique identifier of the deleted note.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this note deletion failure.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message for failure of the requested note deletion.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of failure of note deletion.
          - `details` (object) **REQ** — Contains additional details about the note deletion error.
            - `id` (string/int64) — Represents the identifier of the note that failed to delete.
            additionalProperties: any

- **400**: The request parameters are invalid. **Resolution:** Ensure the ids parameter contains valid note IDs that belong to the specified parent record. [application/json]
    > Validation error response for the DELETE bulk notes request.
    oneOf:
      - `BadRequestError` — Error response schema for 400 bad request errors, covering INVALID_MODULE, INVALID_DATA, and NOT_SUPPORTED error codes.
        - `code` (string) **REQ** [enum=['INVALID_MODULE', 'INVALID_DATA', 'NOT_SUPPORTED']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional details about the error.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
        - `status` (string) **REQ** [enum=['error']] — Indicates the status of the response.
      - `RequiredParamMissingError` — Error response schema for requests where a required query parameter is absent.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional details about the missing parameter.
          - `param_name` (string) [maxLen=255] — Represents the name of the required parameter that is missing from the request.
          additionalProperties: any
        - `message` (string) **REQ** [maxLen=500] — Represents the error message for this response.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `InvalidDataError` — Error response schema returned when a field value fails validation, such as exceeding the maximum length.
        - `data` (array of object) [maxItems=200] **REQ** — Represents the list of error objects for each note in the request.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
          - `details` (object) **REQ** — Contains additional validation details about the invalid field, including constraint information.
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

**Scopes:** ZohoCRM.modules.Leads.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Contacts.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Accounts.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Deals.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Tasks.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Events.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Calls.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Products.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Vendors.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Campaigns.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Cases.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Solutions.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Pricebooks.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Quotes.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Salesorders.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Purchaseorders.READ, ZohoCRM.modules.notes.DELETE, ZohoCRM.modules.Custom.READ, ZohoCRM.modules.notes.DELETE

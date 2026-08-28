# GET /{parentRecordModule}/{parentRecordId}/Notes
**Operation:** `getNotes` — Related Notes
> Retrieves a paginated list of notes associated with a specific parent record in a CRM module.

**Parameters:**
- `parentRecordModule` (path, string, required) [maxLen=50, pattern=^[A-Za-z_][A-Za-z0-9_]*$]: Specify the API name of the parent record module. Refer to [Get Modules](modules.yaml#$.paths./settings/modules.get) for the list of supported modules.
- `parentRecordId` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique numeric ID of the parent record.
- `fields` (query, string, optional) [maxLen=1000, pattern=^[A-Za-z_][A-Za-z0-9_]*(,[A-Za-z_][A-Za-z0-9_]*)*$]: A comma-separated list of field API names to return in the response. If not specified, all available fields are included in the response.
- `page` (query, integer/int32, optional) [min=1, max=10000, default=1]: Specify the page number for pagination. The value must be **1 or greater**.
- `perPage` (query, integer/int32, optional) [min=1, max=200, default=200]: To get the list of records available per page. The default and the maximum possible value is **200.**
- `sort_by` (query, string, optional) [maxLen=50, enum=['id', 'Created_Time', 'Modified_Time']]: Specify the field name to sort the note records by.
Possible values:
id - Sort by the note ID.
Created_Time - Sort by the creation date and time.
Modified_Time - Sort by the last modification date and time.
- `sort_order` (query, string, optional) [maxLen=10, enum=['asc', 'desc']]: The order in which results are returned.
Possible values:
**asc** - Returns results in ascending order.
**desc** - Returns results in descending order.

**Responses:**

- **200**: Returns the list of notes associated with the specified parent record. [application/json]
    > Response payload containing the list of note records and pagination metadata for the specified parent record.
    - `data` (array of object) [maxItems=200] **REQ** — Represents the list of note records returned for the specified parent record.
      - `id` (string/int64) **REQ** — Represents the unique identifier of the note.
      - `Note_Title` (string) [maxLen=255, nullable] — Represents the title of the note.
      - `Note_Content` (string) [maxLen=65535, nullable] — The content of the note.
      - `$attachments` (array of object) [maxItems=5, nullable] — Represents the list of file attachments associated with the note.
        - `$file_id` (string) [maxLen=255] — Specifies the unique file identifier of the attachment.
        - `File_Name` (string) [maxLen=255] — Specifies the name of the attached file.
        - `Size` (string/int64) — Represents the size of the attached file in bytes.
        - `id` (string/int64) — Indicates the unique identifier of the attachment record.
        additionalProperties: any
      - `Parent_Id` (object) — Represents the parent record associated with the note.
        - `module` (object) **REQ** — Represents the module of the parent record.
          - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the parent record module. Refer to [Get Modules](modules.yaml#$.paths./settings/modules.get) for the list of supported modules.
          - `id` (string/int64) **REQ** — Represents the unique identifier of the parent record module.
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the parent record.
        - `id` (string/int64) **REQ** — Specify the unique ID of the parent record. Refer to Refer the [GET Records API](record.yaml#.$path./{module}.get) to get valid record IDs.
      additionalProperties: any
    - `info` (object) **REQ** — Represents the pagination metadata for this response.
      - `page` (integer/int32) **REQ** — Specifies the current page number.
      - `per_page` (integer/int32) **REQ** — Represents the number of records returned per page.
      - `count` (integer/int32) **REQ** — The number of note records returned in the current page.
      - `more_records` (boolean) **REQ** — Represents whether more note records are available beyond the current page.
      - `next_page_token` (string) [maxLen=1024, nullable] — Indicates the token used to retrieve the next page of results.
      - `previous_page_token` (string) [maxLen=500, nullable] — Represents the token used to retrieve the previous page of results.
      - `page_token_expiry` (string/date-time) [nullable] — Represents the expiry date and time of the page tokens.

- **204**: The request was successful but there are no notes to return for the specified parent record.

- **400**: The request parameters are invalid. Resolution: Ensure the module name, parent record ID, and query parameters are valid. [application/json]
    > Validation error response for the GET notes request.
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
      - `DiscretePaginationLimitExceededError` — Error response returned when a request exceeds the discrete pagination limit without providing a **page_token**.
        - `code` (string) **REQ** [enum=['DISCRETE_PAGINATION_LIMIT_EXCEEDED']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional details about the pagination limit.
          - `limit` (integer/int32) — Represents the maximum number of records that can be retrieved without a page_token parameter.
          additionalProperties: any
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

**Scopes:** ZohoCRM.modules.Leads.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Contacts.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Accounts.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Deals.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Tasks.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Events.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Calls.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Products.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Vendors.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Campaigns.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Cases.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Solutions.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Pricebooks.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Quotes.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Salesorders.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Purchaseorders.READ, ZohoCRM.modules.notes.READ, ZohoCRM.modules.Custom.READ, ZohoCRM.modules.notes.READ

# GET /settings/recycle_bin/{recordId}
**Operation:** `getRecycleBinRecord` — Get a recycle-bin record
> To retrieve metadata for a single record from the Recycle Bin in your Zoho CRM account using its unique ID. The response includes the display name, source module, deletion timestamp, original owner, and the user who deleted the record.

**Parameters:**
- `recordId` (path, string, required) [maxLen=500]: Specify the unique ID of the recycle-bin record you want to retrieve. The **recordId** in the URL takes precedence over any **filters** or **ids** values supplied as query parameters.

**Schemas:**
`ErrorResponse`:
  > Error payload returned when a recycle-bin request fails, including the error code, the error message, and context-specific details.
  - `status` (string) **REQ** [enum=['error']] — Indicates that the API request failed. Possible values: **error**.
  - `code` (string) **REQ** [enum=[5 values]] — Error code identifying why the request failed. Possible values: **INVALID_DATA**, **EXPECTED_FIELD_MISSING**, **EXPECTED_PARAM_MISSING**, **AMBIGUITY_DURING_PROCESSING**, **AUTHORIZATION_FAILED**.
  - `message` (string) **REQ** [maxLen=500] — Message that describes the cause of the error.
  - `details` (object) **REQ** — Provides additional context about the error, such as the offending parameter, field, JSON path, expected data type, or record ID. The populated keys depend on the **code** value.
    - `param_name` (string) [enum=['filters', 'ids']] — Represents the name of the request parameter that caused the error. Possible values: **filters**, **ids**.
    - `api_name` (string) [maxLen=100] — Represents the API name of the field that caused the error.
    - `json_path` (string) [maxLen=1000] — Represents the JSON path to the request body field that caused the error.
    - `expected_data_type` (string) [enum=['jsonarray', 'jsonobject', 'string']] — Represents the data type expected for the offending field when the error is due to an invalid data type. Possible values: **jsonarray**, **jsonobject**, **string**.
    - `param_names` (array of string) [maxItems=2] — List of request parameter names that are expected but missing when the error is **EXPECTED_PARAM_MISSING**.
      items: [enum=['filters', 'ids', 'restore_all_records']]
    - `expected_fields` (array of object) [maxItems=3] — List of fields that are expected in the request body when the error is **EXPECTED_FIELD_MISSING**.
      - `api_name` (string) [maxLen=100] — Represents the API name of the expected field.
      - `json_path` (string) [maxLen=1000] — Represents the JSON path of the expected field within the request body.
    - `ambiguity_due_to` (array of object) [maxItems=2] — List of factors that caused ambiguity when the error is **AMBIGUITY_DURING_PROCESSING**, typically because two or more mutually exclusive restoration modes were supplied.
      - `api_name` (string) [maxLen=100] — Represents the API name of the ambiguity factor.
      - `json_path` (string) [maxLen=1000] — Represents the JSON path of the ambiguity factor within the request body.
    - `id` (string/int64) — Represents the record identifier associated with the error.
    - `resource_path_index` (integer/int32) — Represents the zero-based index of the resource path segment that caused the error.

**Responses:**

- **200**: Returns metadata for the requested recycle-bin record, including its display name, source module, deletion timestamp, owner, and the user who deleted it. [application/json]
    > Represents the response payload for a request to retrieve a single recycle-bin record, containing the record metadata under **recycle_bin**.
    - `recycle_bin` (array of object) [maxItems=1] **REQ** — Represents the list containing the single recycle-bin record matching the requested **recordId**.
      - `display_name` (string) **REQ** [maxLen=500] — Represents the display name of the deleted record as it appeared in its source module.
      - `deleted_time` (string/date-time) **REQ** — Represents the date and time at which the record was moved to the Recycle Bin, in ISO 8601 format.
      - `owner` (object) **REQ** — Represents the user who owned the record at the time of deletion. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the owning user.
        - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the owning user.
      - `module` (object) **REQ** — Represents the source module of the deleted record. Refer to the [Get modules](modules.yaml#$.paths./settings/modules.get) endpoint for details.
        - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the module the record originally belonged to.
        - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the module the record originally belonged to.
      - `deleted_by` (object) **REQ** — Represents the user who deleted the record. Refer to the [Get users](users.yaml#$.paths./users.get) endpoint for details.
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user who deleted the record.
        - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the user who deleted the record.
      - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the recycle-bin record.

- **400**: The request contains invalid parameters or payload. See the response body for the specific error code, message, and offending field. **Resolution:** The caller must inspect the **code** and **details** fields, correct the offending input, and reissue the request. [application/json]
    oneOf:
      - `ErrorResponse` — Error payload returned when a recycle-bin request fails, including the error code, the error message, and context-specific details.
        - `recycle_bin` (array of object `ErrorResponse`) [minItems=1, maxItems=200] — Represents the list of error entries, one per invalid input item, with at least one entry and at most 200 entries.

- **401**: The OAuth token does not include the required scope to read recycle-bin records. **Resolution:** A new access token must be generated with the **ZohoCRM.settings.recycle_bin.READ** scope. [application/json]
    > Represents the error payload returned when the OAuth token does not include the scope required to read recycle-bin records.
    - `status` (string) **REQ** [enum=['error']] — Indicates that the request was not authorized. Possible values: **error** - The OAuth token does not include the required scope.
    - `code` (string) **REQ** [maxLen=100] — Represents the error code identifying the authorization failure.
    - `message` (string) **REQ** [maxLen=500] — Represents the message describing the authorization failure.
    - `details` (object) **REQ** — Represents additional context about the authorization failure. This is an empty object for OAuth scope mismatches.

- **404**: The request URL does not match a valid endpoint pattern for retrieving a recycle-bin record in Zoho CRM. **Resolution:** The request path must be verified and reissued as a GET request to the correct endpoint. [application/json]
    > Represents the error payload returned when the request URL does not match the valid endpoint pattern for retrieving a recycle-bin record.
    - `status` (string) **REQ** [enum=['error']] — Indicates that the requested URL pattern is invalid. Possible values: **error** - The request did not match a valid endpoint pattern.
    - `code` (string) **REQ** [maxLen=100] — Represents the error code identifying why the URL pattern is invalid.
    - `message` (string) **REQ** [maxLen=500] — Represents the message describing the URL pattern issue.
    - `details` (object) **REQ** — Represents additional context about the invalid URL pattern. This is an empty object for URL pattern errors.

**Scopes:** ZohoCRM.settings.recycle_bin.READ

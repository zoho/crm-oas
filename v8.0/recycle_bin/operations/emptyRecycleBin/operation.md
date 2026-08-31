# POST /settings/recycle_bin/actions/empty
**Operation:** `emptyRecycleBin` — Empty the Recycle Bin
> To permanently delete every record from the Recycle Bin in your Zoho CRM account. This action is irreversible - the records cannot be restored after this operation completes. When the Recycle Bin contains 1000 or fewer records, including child records such as Notes and Attachments, Zoho CRM deletes the records immediately and returns a 200 response. When the count exceeds 1000, the deletion runs as a background job and returns a 202 response. Only users with the Admin profile can empty the Recycle Bin.

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

- **200**: Returns a confirmation that Zoho CRM has emptied the Recycle Bin immediately. The response includes the **SUCCESS** result code and the success status. [application/json]
    > Represents the success payload returned when Zoho CRM deletes every record in the Recycle Bin immediately in a single synchronous call.
    - `code` (string) **REQ** [maxLen=100, enum=['SUCCESS']] — Represents the result code for the empty operation. Possible values: **SUCCESS** - Every record in the Recycle Bin was permanently deleted.
    - `details` (object) **REQ** — Represents additional details about the empty operation. This is an empty object when the operation completes successfully.
    - `message` (string) **REQ** [maxLen=500] — Represents the message confirming that the Recycle Bin was emptied.
    - `status` (string) **REQ** [enum=['success']] — Indicates the outcome of the empty operation. Possible values: **success** - Every record in the Recycle Bin was permanently deleted.

- **202**: Indicates that the empty Recycle Bin action has been accepted and scheduled as a background job. Zoho CRM returns this response when the Recycle Bin contains more than 1000 records, including child records. [application/json]
    > Represents the accepted payload returned when the empty Recycle Bin action is scheduled as a background job.
    - `code` (string) **REQ** [maxLen=100, enum=['SCHEDULED']] — Represents the result code indicating that the empty operation is scheduled as a background job. Possible values: **SCHEDULED** - The empty Recycle Bin action was queued as a background job.
    - `details` (object) **REQ** — Represents additional details about the scheduled empty operation. This is an empty object when the job is queued.
    - `message` (string) **REQ** [maxLen=500] — Represents the message confirming that the empty Recycle Bin action has been scheduled as a background job.
    - `status` (string) **REQ** [enum=['success']] — Indicates the outcome of the scheduling request. Possible values: **success** - The empty Recycle Bin action was accepted and queued as a background job.

- **400**: The request contains invalid parameters or payload. See the response body for the specific error code, message, and offending field. **Resolution:** The caller must inspect the **code** and **details** fields, correct the offending input, and reissue the request. [application/json]
    oneOf:
      - `ErrorResponse` — Error payload returned when a recycle-bin request fails, including the error code, the error message, and context-specific details.
        - `recycle_bin` (array of object `ErrorResponse`) [minItems=1, maxItems=200] — Represents the list of error entries, one per invalid input item, with at least one entry and at most 200 entries.

- **401**: The OAuth token does not include the required scope to empty the Recycle Bin. **Resolution:** A new access token must be generated with the **ZohoCRM.settings.recycle_bin.UPDATE** scope. [application/json]
    > Represents the error payload returned when the OAuth token does not include the scope required to empty the Recycle Bin.
    - `status` (string) **REQ** [enum=['error']] — Indicates that the request was not authorized. Possible values: **error** - The OAuth token does not include the required scope.
    - `code` (string) **REQ** [maxLen=100] — Represents the error code identifying the cause of the authorization failure.
    - `message` (string) **REQ** [maxLen=500] — Represents the message describing the cause of the authorization failure.
    - `details` (object) **REQ** — Represents additional context about the authorization failure. This is an empty object for scope mismatch errors.

- **404**: The request URL does not match a valid endpoint pattern for emptying the Recycle Bin in Zoho CRM. **Resolution:** The request path must be verified and reissued as a POST request to the correct empty Recycle Bin endpoint. [application/json]
    > Represents the error payload returned when the request targets an invalid URL pattern for the empty Recycle Bin action.
    - `status` (string) **REQ** [enum=['error']] — Indicates that the requested URL pattern is invalid. Possible values: **error** - The request did not match a valid endpoint pattern.
    - `code` (string) **REQ** [maxLen=100] — Represents the error code identifying why the URL pattern is invalid.
    - `message` (string) **REQ** [maxLen=500] — Represents the message describing the URL pattern issue.
    - `details` (object) **REQ** — Represents additional context about the invalid URL pattern. This is an empty object for URL pattern errors.

**Scopes:** ZohoCRM.settings.recycle_bin.UPDATE

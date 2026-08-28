# DELETE /settings/recycle_bin
**Operation:** `deleteRecycleBinRecords` — Delete recycle-bin records
> To permanently delete one or more records from the Recycle Bin in your Zoho CRM account. When deleting a parent record, Zoho CRM also removes all its associated child records from the Recycle Bin, such as Notes and Attachments. When the total number of records to delete is 1000 or fewer, the operation completes immediately and returns a 200 response with per-item results. When the total exceeds 1000, the deletion runs as a background job and returns a 202 response. Partial successes return a 207 multi-status response with individual success and error entries per record.

**Parameters:**
- `filters` (query, string, required) [maxLen=2000]: Specify the URL-encoded filter expression that scopes the operation to recycle-bin records matching the supplied conditions. The expression is a JSON object with a top-level **AND** group of field conditions covering **display_name**, **module**, **deleted_by**, or **deleted_time**.

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
`ResultList`:
  > Wrapper that returns the per-item results of a recycle-bin operation under the **recycle_bin** array.
  - `recycle_bin` (array of object) [maxItems=200] **REQ** — List of per-item results for the operation. Each entry is either a success result or a scheduled-job result.
    oneOf:
      - `SuccessResponse` — Per-item result returned when a single recycle-bin record is processed successfully.
      - `ScheduledResponse` — Result returned when a recycle-bin operation is queued as a background job because it cannot complete synchronously.
`ScheduledResponse`:
  > Result returned when a recycle-bin operation is queued as a background job because it cannot complete synchronously.
  - `code` (string) **REQ** [enum=['SCHEDULED']] — Result code indicating that the operation is scheduled. Possible values: **SCHEDULED**.
  - `message` (string) **REQ** [maxLen=500] — Represents the message confirming that the operation has been queued as a background job.
  - `details` (object) **REQ** — Represents additional details about the scheduled operation. This is typically an empty object or contains a record ID associated with the scheduled job.
  - `status` (string) **REQ** [enum=['success']] — Indicates that the request to schedule the operation succeeded. Possible values: **success**.
`SuccessResponse`:
  > Per-item result returned when a single recycle-bin record is processed successfully.
  - `status` (string) **REQ** [enum=['success']] — Indicates that the per-item operation succeeded. Possible values: **success**.
  - `code` (string) **REQ** [maxLen=100, enum=['SUCCESS']] — Result code for the per-item operation. Possible values: **SUCCESS**.
  - `message` (string) **REQ** [maxLen=500] — Represents the message that describes the outcome of the per-item operation.
  - `details` (object) **REQ** — Represents additional details about the per-item operation, including the affected record ID.
    - `id` (string) [maxLen=500] — Represents the unique identifier of the recycle-bin record that the per-item result refers to.

**Responses:**

- **200**: Returns the per-item results for each recycle-bin record that Zoho CRM permanently removes. The **recycle_bin** array contains one entry per processed record, each with the deletion status, result code, message, and the affected record ID. — Schema: `ResultList` [application/json]
    > Wrapper that returns the per-item results of a recycle-bin operation under the **recycle_bin** array.

- **202**: Indicates that the deletion has been accepted and scheduled as a background job. Zoho CRM returns this response when the total number of records to delete, including child records such as Notes and Attachments, exceeds 1000, or when the **filters** parameter is used. — Schema: `ResultList` [application/json]
    > Wrapper that returns the per-item results of a recycle-bin operation under the **recycle_bin** array.

- **207**: Returns a per-item multi-status response when some records in the bulk request succeeded and others failed. The **recycle_bin** array contains both success and error entries. [application/json]
    > Multi-status payload that combines per-item success and error entries when a bulk request partially succeeds.
    - `recycle_bin` (array of object) [maxItems=200] **REQ** — Represents the list of per-item results, where each entry is either a **SuccessResponse** for a successful item or an **ErrorResponse** for a failed item.
      oneOf:
        - `SuccessResponse` — Per-item result returned when a single recycle-bin record is processed successfully.
        - `ErrorResponse` — Error payload returned when a recycle-bin request fails, including the error code, the error message, and context-specific details.

- **400**: The request contains invalid parameters or payload. See the response body for the specific error code, message, and offending field. **Resolution:** The caller must inspect the **code** and **details** fields, correct the offending input, and reissue the request. [application/json]
    oneOf:
      - `ErrorResponse` — Error payload returned when a recycle-bin request fails, including the error code, the error message, and context-specific details.
        - `recycle_bin` (array of object `ErrorResponse`) [minItems=1, maxItems=200] — Represents the list of error entries, one per invalid input item, with at least one entry and at most 200 entries.

**Scopes:** ZohoCRM.settings.recycle_bin.DELETE

# DELETE /settings/recycle_bin/{recordId}
**Operation:** `deleteRecycleBinRecord` — Delete a recycle-bin record permanently
> To permanently delete a single record from the Recycle Bin in your Zoho CRM account using its unique ID. Deleting a parent record also removes all its associated child records from the Recycle Bin, such as Notes and Attachments. This operation is irreversible - the record cannot be restored after deletion. When the total number of records to delete, including child records, exceeds 1000, the operation runs as a background job.

**Parameters:**
- `recordId` (path, string, required) [maxLen=100]: Specify the unique ID of the recycle-bin record you want to delete permanently.

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

- **200**: Returns the per-item result confirming that the recycle-bin record was permanently deleted. The **recycle_bin** array contains one entry with the deletion status and the deleted record ID. [application/json]
    > Represents the response payload for a successful permanent deletion of a single recycle-bin record, containing the per-item result under the **recycle_bin** array.
    - `recycle_bin` (array of object) [maxItems=200] **REQ** — Represents the list of per-item results for the deletion request, with one entry for the single deleted record.
      - `status` (string) **REQ** [enum=['success', 'error']] — Indicates whether the deletion succeeded or failed for the record. Possible values: **success** - The record was permanently deleted. **error** - The deletion failed for this record.
      - `code` (string) **REQ** [enum=['SUCCESS', 'CANNOT_DELETE']] — Represents the result code for the deletion. Possible values: **SUCCESS** - The record was permanently deleted. **CANNOT_DELETE** - The record could not be permanently deleted.
      - `message` (string) **REQ** [maxLen=500] — Represents the message describing the outcome of the deletion request.
      - `details` (object) **REQ** — Represents additional details about the per-item deletion result, including the ID of the affected record.
        - `id` (string) **REQ** [maxLen=500] — Represents the unique identifier of the recycle-bin record that was permanently deleted.
        additionalProperties: any

- **400**: The request contains invalid parameters or payload. See the response body for the specific error code, message, and offending field. **Resolution:** The caller must inspect the **code** and **details** fields, correct the offending input, and reissue the request. [application/json]
    oneOf:
      - `ErrorResponse` — Error payload returned when a recycle-bin request fails, including the error code, the error message, and context-specific details.
        - `recycle_bin` (array of object `ErrorResponse`) [minItems=1, maxItems=200] — Represents the list of error entries, one per invalid input item, with at least one entry and at most 200 entries.

**Scopes:** ZohoCRM.settings.recycle_bin.DELETE

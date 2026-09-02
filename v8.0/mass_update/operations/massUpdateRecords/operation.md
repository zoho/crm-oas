# POST /{module}/actions/mass_update
**Operation:** `massUpdateRecords` — Mass update records
> To update a specific field value across multiple records of a module in your Zoho CRM organization in a single API call. The operation supports two modes. In the non-scheduler mode, the caller supplies a list of record IDs in the `ids` array and the system updates those records synchronously, with a maximum of 500 records per request. In the scheduler mode, the caller supplies a Custom View ID in `cvid` and the request schedules an asynchronous background job that processes up to 50,000 records matching the view; the response returns a `job_id` that can be passed to the corresponding GET endpoint to track the job's progress. The Deals module accepts up to three fields per request; all other supported modules accept only one field per request. Email, lookup, multi-line, layout, and line item fields cannot be mass updated.

**Parameters:**
- `module` (path, string, required) [enum=[18 values]]: Specify the API name of the CRM module on which the mass update operation must be performed. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to fetch the valid API name of the module. 

**Request Body** (required) — application/json
> The request body contains the data required to perform the operation.


Mass update of records happens in two ways:


**Scheduler type**: When you specify a custom view ID and territory
ID, a job is scheduled in the background and the system returns a
"job_id". Use this job_id in the [Get Mass Update Status
API](mass_update.yaml#$.paths./{module}/actions/mass_update.get) to
get the status of the job. You can update a maximum of **50,000
records** in this type.


**Non-scheduler type**: When you specify the record IDs, system
updates the records instantly. You can update a maximum of **500
records** in a single API call in this type of mass update.

  - `data` (array) **REQ** [maxItems=1] — Specify the array of objects, where each object maps a field's API name to the new value to be applied across the targeted records. The key must be provided along with either `ids` or `cvid`.
  - `ids` (array) [maxItems=500] — Specify the record IDs to be mass updated synchronously. Use
`ids` for non-scheduler updates that target a small batch of
records and require immediate processing. Use the [Get
Records API](record.yaml#$.paths./{module}.get) to get the
valid IDs of the required records.


> **Note**:

> - You can use either **ids** key or the **cvid** key, you
cannot use them both in a request.

> - Scheduler type(using record IDs):

>    - You can mass update a maximum of 50,000 records in a
single API call.

>    - Automation rules are triggered automatically when the
record count is less than 1000. When the record count is
greater than 1000, automation rules do not get triggered.

>    - If some of the records have invalid data, only those
records will not be processed in the API call.

> - Non-scheduler type(using CVID and territory ID):

>    - You can mass update a maximum of 500 records in a
single API call.

>    - Automation rules such as approvals, blueprints, and
workflows are triggered automatically.

>    - When you want to mass update records in a territory,
you must specify the custom view ID.

> - You cannot mass update Email, lookup fields, layout
fields, multi-line fields, and line items.

> - You can mass update up to three fields in the Deals
module and only one field in all other modules in a single
API call.

  - `cvid` (string/int64) [pattern=^[0-9]+$] — Specify the Custom View ID whose matching records must be mass updated. Use `cvid` to schedule an asynchronous background job that processes the records in the Custom View. Use the [Get Custom View API](custom_views.yaml#$.paths./settings/custom_views.get) to get the ID of the requires custom view. 

The response returns a `job_id` that can be passed to [Get Mass Update Status API](mass_update.yaml#$.paths./{module}/actions/mass_update.get) to track the progress of the scheduled job.

> **Note**:
> The cvid key is supported for mass update via API in the following editions:
> - Enterprise
> - Ultimate
> - CRM Plus
> - Zoho One Enterprise

  - `territory` (object) — Specify the territory whose records must be mass updated. This key is valid only when you provide a Custom View ID in `cvid`.
  oneOf:
      - `territory` (object) — Ensures that the `territory` key is not provided along with the `ids` key.

**Responses:**

- **200**: Returns the outcome of the mass update operation. [application/json]
    > Represents the response wrapper returned when the mass update operation is accepted, containing one or more outcome entries for the processed records or the scheduled job.
    - `data` (array of object) [maxItems=500] **REQ** — Represents the array that contains one response object per record processed or one entry describing the scheduled job.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the individual entry.
      - `details` (object) **REQ** — Represents additional details about the response. 
        oneOf:
            - `job_id` (string/int64) **REQ** [pattern=^[0-9]+$] — Represents the unique ID of the scheduled mass update job. Pass this value as the `job_id` query parameter to [Get Mass Update Status API](mass_update.yaml#$.paths./{module}/actions/mass_update.get) to retrieve the job's current status and record counts.
            - `id` (string/int64) **REQ** [pattern=^[0-9]+$] — Represents the unique ID of the record that the mass update operation modified.
            - `Modified_Time` (string/date-time) **REQ** — Represents the date and time, in ISO 8601 format, when the record was last modified by the mass update operation.
            - `Modified_By` (object) **REQ** — Represents the user who performed the mass update on the record.
              - `id` (string/int64) **REQ** [pattern=^[0-9]+$] — Represents the unique ID of the user who modified the record.
              - `name` (string/string) **REQ** — Represents the display name of the user who modified the record.
            - `Created_By` (object) **REQ** — Represents the user who originally created the record.
              - `id` (string/int64) **REQ** [pattern=^[0-9]+$] — Represents the unique ID of the user who created the record.
              - `name` (string/string) **REQ** — Represents the display name of the user who created the record.
            - `Created_Time` (string/date-time) **REQ** — Represents the date and time, in ISO 8601 format, when the record was originally created.
      - `message` (string/string) **REQ** — Represents the message describing the result of the operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation for this entry.

- **207**: Returns a multi-status response when some records are updated successfully while others fail. [application/json]
    > Represents the response wrapper returned when a non-scheduler-type mass update results in mixed responses, containing at least one successfully updated record and at least one failed record.
    - `data` (array of object) [minItems=2, maxItems=500] **REQ** — Represents the array that contains one response object per record processed, indicating whether the mass update succeeded or failed for that record.
      - `code` (string) **REQ** [enum=[6 values]] — Represents the result code for the individual
record.

Possible values:

SUCCESS - The record was updated successfully.

MANDATORY_NOT_FOUND - A required property is missing
from the payload for the record.

INVALID_DATA - The request data is invalid for the
record.

MAPPING_MISMATCH - The provided value violates a
field mapping relationship for the record.

RECORD_LOCKED - The record is locked and cannot be
updated.

CONVERTED_RECORD - The record has already been
converted and cannot be updated.

      - `details` (object) **REQ** — Represents additional details about the response. For an updated record, it contains the record ID along with its creation and modification details. For a failed record, it contains the details of the failure, such as the ID of the record that could not be updated.
      - `message` (string) **REQ** [maxLen=255] — Represents the message describing the result of the operation for this record.
      - `status` (string) **REQ** [enum=['success', 'error']] — Represents the status of the operation for this
record.

Possible values:

success - The record was updated.

error - The record was not updated.


- **400**: Returns an error when the mass update request cannot be processed, either at the request level (such as a scheduling conflict or an unsupported module) or for individual records (such as missing mandatory fields, invalid data, locked records, or converted records). [application/json]
    > Represents the error response wrapper for a failed mass update request. The response is one of the request-level error variants (`ALREADY_SCHEDULED`, `INVALID_MODULE`) or a per-record error envelope that lists individual record failures.
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the response.
        - `message` (string) **REQ** [enum=['the cvid given seems to be invalid']] — Represents the error message for the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall status of the API response.
        - `details` (object) **REQ** — Represents additional details identifying the invalid cvid request key.
          - `api_name` (string) **REQ** [enum=['cvid']] — Represents the API name of the key that caused the error.
          - `json_path` (string) **REQ** [enum=['$.cvid']] — Represents the JSON path to the invalid key in the request.
        - `code` (string) **REQ** [enum=['ALREADY_SCHEDULED']] — Represents the error code returned when a mass update job is already running for the provided Custom View.
        - `message` (string/string) **REQ** — Represents the error message indicating that a mass update job is already scheduled for the provided Custom View.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall status of the API response.
        - `details` (object) **REQ** — Represents additional details about the scheduling conflict, including the request parameter that triggered the error.
          - `api_name` (string) **REQ** [enum=['cvid']] — Represents the API name of the key that caused the scheduling conflict.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned when the module specified in the request URL is invalid or not supported by the Mass Update API.
        - `message` (string/string) **REQ** — Represents the error message describing the module validation failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall status of the API response.
        - `details` (object) **REQ** — Represents additional details about the invalid module, including the index of the unsupported segment in the request path.
          - `resource_path_index` (integer/int32) **REQ** — Represents the zero-based index of the unsupported segment in the request URL path.
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the error code returned when the module specified in the request URL is not supported by the Mass Update API.
        - `message` (string) **REQ** [enum=[2 values]] — Represents the error message indicating that the module is not supported by the Mass Update API.
        - `status` (string) **REQ** [enum=['error']] — Represents the overall status of the API response.
        - `details` (object) **REQ** — Represents additional details about the unsupported module, including the index of the unsupported segment in the request path.
          - `resource_path_index` (integer/int32) **REQ** [const=0] — Represents the zero-based index of the unsupported segment in the request URL path.
        - `data` (array of object) [maxItems=500] **REQ** — Represents the array of per-record error responses returned when one or more records fail to be mass updated.
          oneOf:
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned when a required property is missing from the payload for a record.
              - `details` (object) **REQ** — Represents additional details about the missing mandatory property.
              - `message` (string/string) **REQ** — Represents the error message indicating that a required property is missing from the payload.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation for this record.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the request data fails validation for a record.
              - `details` (object) **REQ** — Represents additional details about the invalid data, including the invalid record ID, field API name, or the constraint that was violated.
                - `id` (string/int64) [pattern=^[0-9]+$] — Represents the unique ID of the record for which the validation failed.
                - `limit` (integer/int32) [min=1] — Represents the maximum allowed limit that was exceeded for the field.
                - `maximum_length` (integer/int32) [min=1] — Represents the maximum number of characters allowed for the field value.
                - `maximum_decimal_place` (integer/int32) [min=0] — Represents the maximum number of decimal places allowed for the field value.
                - `range` (object) — Represents the inclusive numeric range within which the field value must fall.
                  - `from` (integer/int64) **REQ** — Represents the minimum allowed value, inclusive, for the field.
                  - `to` (integer/int64) **REQ** — Represents the maximum allowed value, inclusive, for the field.
              - `message` (string/string) **REQ** — Represents the error message describing the validation failure for the record.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation for this record.
              - `code` (string) **REQ** [enum=['MAPPING_MISMATCH']] — Represents the error code returned when the provided value violates a field mapping relationship.
              - `details` (object) **REQ** — Represents additional details about the mapping mismatch, including the API name of the field that does not match the mapping, the field that owns the mapping relationship, and the JSON path of the mismatched element.
                - `mapped_field` (string/string) — Represents the field that owns the mapping relationship.
                - `api_name` (string/string) — Represents the API name of the field whose value does not match the mapping.
                - `json_path` (string/string) — Represents the JSON path to the mismatched element in the request body.
              - `message` (string/string) **REQ** — Represents the error message describing the mapping mismatch.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation for this record.
              - `code` (string) **REQ** [enum=['NOT_SUPPORTED', 'INVALID_MODULE']] — Represents the error code returned when the
requested operation or module is not
supported by the Mass Update API.

Possible values:

NOT_SUPPORTED - The requested operation is
not supported for the targeted record or
module.

INVALID_MODULE - The module is not supported
by the Mass Update API.

              - `message` (string/string) **REQ** — Represents the error message describing why the operation or module is not supported.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation for this record.
              - `details` (object) **REQ** — Represents additional details about the unsupported request, including the index of the unsupported segment in the request URL path.
              - `code` (string) **REQ** [enum=['RECORD_LOCKED']] — Represents the error code returned when the record is locked and cannot be updated.
              - `message` (string/string) **REQ** — Represents the error message indicating that the record is locked.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation for this record.
              - `details` (object) **REQ** — Represents additional details about the locked record, including the ID of the locked record and the action that placed the lock.
                - `action` (string) **REQ** [enum=['record_locking']] — Represents the action that placed the lock on the record.
                - `id` (string/int64) **REQ** [pattern=^[0-9]+$] — Represents the unique ID of the locked record that could not be updated.
              - `code` (string) **REQ** [enum=['CONVERTED_RECORD']] — Represents the error code returned when the record has already been converted and cannot be updated.
              - `message` (string/string) **REQ** — Represents the error message indicating that the record has already been converted and cannot be updated.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation for the record.
              - `details` (object) **REQ** — Represents additional details about the converted record, including its unique ID.
                - `id` (string/int64) **REQ** [pattern=^[0-9]+$] — Represents the unique ID of the record that has already been converted.

**Scopes:** ZohoCRM.mass_update.UPDATE, ZohoCRM.mass_update.Leads.UPDATE

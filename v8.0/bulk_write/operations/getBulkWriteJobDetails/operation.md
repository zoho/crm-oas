# GET /write/{jobId}
**Operation:** `getBulkWriteJobDetails` — Get bulk write job details
> To retrieve the details of a previously created bulk write job in your Zoho CRM organization, including its current status, per-resource and per-file processing counts, the creator, and the download URL of the result archive once the job completes. The download URL remains accessible for up to seven days after the job completes.

**Parameters:**
- `jobId` (path, string, required) [maxLen=100]: Specify the unique identifier of the bulk write job whose details you want to retrieve.

**Responses:**

- **200**: Returns the full state and processing result of the bulk write job identified by the supplied **jobId**, including the per-resource and per-file counts and the download URL of the result archive. [application/json]
    > Represents the full state and processing result of a bulk write job, including the overall status, the per-resource processing summary, the job creator, and the download URL of the result archive.
    - `status` (string) **REQ** [maxLen=50] — Represents the current overall status of the bulk write job.  Sample values include **ADDED**, **INPROGRESS**, **COMPLETED**, and **SKIPPED**.
    - `character_encoding` (string) [maxLen=50] — Represents the character encoding used to read the uploaded file. Returned with the value detected automatically by Zoho CRM, or with the value supplied in the original create request when it was specified.
    - `resource` (array of object) [maxItems=100] **REQ** — Represents the list of resource entries processed by the bulk write job, one entry per resource configuration submitted in the create request. 
      - `status` (string) **REQ** [enum=['COMPLETED', 'ADDED', 'INPROGRESS', 'SKIPPED']] — Represents the processing status of this resource entry. 
Possible values:
**COMPLETED** - All records in the resource were processed successfully.
**ADDED** - The resource was queued for processing.
**INPROGRESS** - The resource is currently being processed.
**SKIPPED** - The resource was skipped without being processed.
      - `type` (string) **REQ** [enum=['data']] — Represents the type of the processed resource. 
Possible values:
**data** - Indicates that the resource contained record data.
      - `module` (object) **REQ** — Represents the target CRM module into which the resource was written. 
        - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the target CRM module into which records were written.  Refer to the [Modules](modules.yaml#$.paths./settings/modules.get) resource for details.
        - `id` (string) [maxLen=100] — Represents the unique identifier of the target CRM module. Refer to the [Modules](modules.yaml#$.paths./settings/modules.get) resource for details.
      - `ignore_empty` (boolean) — Indicates whether empty cells in the uploaded file were skipped when updating records.
Possible values:
**true** - Empty values in a column were ignored and only non-empty values were written.
**false** - Empty values in a column were written to the corresponding field.
      - `field_mappings` (array of object) [maxItems=500] — Represents the field mappings applied between columns in the uploaded file and fields on the target module for this resource.
        - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field on the target module that received the column value. Refer to the [Fields API](fields.yaml#$.paths./settings/fields.get) resource for details.
        - `index` (integer/int32) **REQ** — Represents the zero-based column index in the uploaded file whose value was written to the mapped field.
        - `format` (string) [maxLen=100, nullable] — Represents the value format applied to the column when the field requires a specific date, datetime, numeric, or currency pattern. Returned as **null** when no explicit format was supplied.
        - `find_by` (string) [maxLen=100, nullable] — Represents the field that the bulk write job used to match existing records for this mapping. Returned as **null** when no matching key was supplied.
        - `default_value` (object) — Represents the default value used to populate the field when the corresponding column in the file was empty.
          - `value` (string) **REQ** [maxLen=500] — Represents the default value that replaces empty cells in the mapped column.
        - `parent_column_index` (integer/int32) [nullable] — Represents the column index of the parent record reference when the mapped field is part of a subform or related record. Returned as **null** when no parent column was supplied.
        - `module` (string) [maxLen=100, nullable] — Represents the related module API name supplied for lookup-style mappings that resolve values against a sibling module. Returned as **null** when no related module was supplied.
      - `file` (object) — Represents the per-file processing summary for this resource entry. 
        - `status` (string) **REQ** [enum=['COMPLETED', 'ADDED', 'INPROGRESS', 'SKIPPED']] — Represents the processing status of the file within this resource entry. 
Possible values:
**COMPLETED** - The file was fully processed.
**ADDED** - The file was queued for processing.
**INPROGRESS** - The file is currently being processed.
**SKIPPED** - The file was skipped.
        - `name` (string) **REQ** [maxLen=255] — Represents the file name read from the uploaded archive. 
        - `added_count` (integer/int32) **REQ** — Represents the number of records that were created from the file. 
        - `skipped_count` (integer/int32) **REQ** — Represents the number of records that were skipped during processing.  The error column in the result file explains why each record was skipped.
        - `updated_count` (integer/int32) **REQ** — Represents the number of records that were updated from the file. 
        - `total_count` (integer/int32) **REQ** — Represents the total number of records that were created, updated, or skipped during processing. 
      - `code` (string) [maxLen=100] — Represents the result code returned by Zoho CRM for the processing of this resource entry.
    - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the bulk write job. 
    - `result` (object) — Represents the result metadata of the completed bulk write job, including the **download URL** of the result archive.
      - `download_url` (string) **REQ** [maxLen=500] — Represents the URL from which the result archive of the bulk write job can be downloaded. The download URL is accessible for up to **seven** days after job completion.
    - `created_by` (object) **REQ** — Represents the Zoho CRM user who created the bulk write job. 
      - `name` (string) **REQ** [maxLen=100] — Represents the display name of the Zoho CRM user who created the bulk write job.  Refer to the [Users API](users.yaml#$.paths./users.get) endpoint for details.
      - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the Zoho CRM user who created the bulk write job.  Refer to the [Users API](users.yaml#$.paths./users.get) endpoint for details.
    - `operation` (string) **REQ** [maxLen=50] — Represents the type of bulk write operation performed by the job, such as **insert**, **update**, or **upsert**. 
    - `created_time` (string/date-time) **REQ** — Represents the ISO 8601 timestamp at which Zoho CRM created the bulk write job. 
    - `callback` (object) **REQ** — Represents the callback configuration registered for the bulk write job, used to notify the configured URL when the job completes or fails. 
      - `url` (string) **REQ** [enum=['http://requestbin.fullcontact.com/1fcimk51']] — Represents the URL that receives the job completion notification.
Possible values:
http://requestbin.fullcontact.com/1fcimk51 - Sample callback URL recorded for the job.
      - `method` (string) **REQ** [enum=['post']] — Represents the HTTP method used to invoke the callback URL.
Possible values:
post - The callback URL is invoked with an HTTP POST request.

**Scopes:** ZohoCRM.bulk.CREATE

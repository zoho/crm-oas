# GET /read/{jobId}
**Operation:** `getBulkReadJobDetails` — Get bulk read job details
> To retrieve the details of a bulk read job in Zoho CRM. Use this API to check the current state of a bulk read job and obtain the download URL once the job is complete. Specify the unique job ID that Zoho CRM returned when you created the job.

**Parameters:**
- `jobId` (path, string, required) [maxLen=100]: Specify the unique identifier of the bulk read job.

**Responses:**

- **200**: The bulk read job details were successfully retrieved. [application/json]
    > Represents the response returned when the bulk read job details are successfully retrieved.
    - `data` (array of object) [maxItems=1000] **REQ** — Represents the list of bulk read job details returned in the response. 
      - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the bulk read job. 
      - `operation` (string) **REQ** [maxLen=500] — Specifies the type of action the API completed. Sample - "operation" : "read”.
      - `state` (string) **REQ** [enum=['COMPLETED', 'ADDED', 'QUEUED', 'IN PROGRESS']] — Represents the current processing state of the bulk read job. 
Possible values:
**ADDED** - The job has been created and is awaiting processing.
**QUEUED** - The job is queued and scheduled for processing.
**IN PROGRESS** - The job is currently being processed.
**COMPLETED** - The job has finished processing and the result is available for download.
      - `query` (object) **REQ** — Represents the query configuration used to create the bulk read job, including the module, filter criteria, and field selections. 
        - `module` (object) **REQ** — Represents the CRM module from which records are exported. 
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM module. 
          - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the CRM module. 
        - `cvid` (string) [maxLen=100] — Represents the unique identifier of the Custom View used to pre-filter the records for the bulk read job.
        - `fields` (array of string) [maxItems=1000] — Represents the list of field API names included in the exported data.
          items: [maxLen=500]
        - `page` (integer/int32) **REQ** — Specifies the page number of records to export. 
        - `criteria` (object) — Represents the filter criteria used to narrow the records exported in the bulk read job.
          - `group_operator` (string) **REQ** [enum=['or', 'and']] — Specifies the logical operator used to combine conditions within the criteria group. 
Possible values:
**and** - All filter conditions must be satisfied.
**or** - At least one filter condition must be satisfied.
          - `group` (array of object) [maxItems=1000] **REQ** — Indicates the list of filter conditions applied to the bulk read query. 
            - `field` (object) **REQ** — Represents the field used in the filter condition. 
              - `api_name` (string) **REQ** [maxLen=255] — Indicates the API name of the filter field. 
              - `id` (string) **REQ** [maxLen=100, nullable] — Represents the unique identifier of the filter field. 
            - `id` (string) [maxLen=100, nullable] — Represents the position identifier of the filter condition within the criteria group. 
            - `value` (string) **REQ** [maxLen=500] — Represents the value used in the filter condition. 
            - `type` (string) **REQ** [enum=['value']] — Specifies the data type of the filter field. 
            - `comparator` (string) **REQ** [enum=['equal', 'contains', 'ends_with', 'not_contains', 'not_equal', 'starts_with']] — Indicates the comparison operator used in the filter condition. 
      - `created_by` (object) **REQ** — Represents the user who created the bulk read job. 
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user who created the job. 
        - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the user who created the job. 
      - `created_time` (string/date-time) **REQ** — Represents the date and time when Zoho CRM created the bulk read job, in ISO 8601 format. 
      - `result` (object) — specifies the export result details of the bulk read job, including the download URL and pagination information. Present when the job has completed or partially completed.
        - `page` (integer/int32) **REQ** — Represents the page number of the exported result. 
        - `count` (integer/int32) **REQ** — Specifies the total number of records exported in the bulk read job. 
        - `download_url` (string) **REQ** [maxLen=2048] — Specifies the URL to download the exported file. 
        - `per_page` (integer/int32) **REQ** — Represents the number of records per page in the exported result. 
        - `more_records` (boolean) **REQ** — Indicates whether additional records are available beyond the current page. 
        - `next_page_token` (string) [maxLen=500] — Represents a token used to retrieve the next page of exported records in subsequent requests.
      - `file_type` (string) **REQ** [enum=['csv']] — Indicates the format of the exported file. 
Possible values:
**csv** - The records are exported in CSV format.

- **404**: The specified bulk read job was not found. [application/json]
    > Indicates the error response returned when the specified bulk read job does not exist.
    - `code` (string) **REQ** [enum=['RESOURCE_NOT_FOUND']] — Represents the error code indicating that the requested bulk read job was not found. 
Possible values:
**RESOURCE_NOT_FOUND** - The bulk read job with the specified ID does not exist.
    - `details` (object) **REQ** — Specifies additional details about the resource not found error. 
      - `resource` (string) **REQ** [maxLen=500] — Represents the type of resource that was not found. 
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the resource not found issue. 
    - `status` (string) **REQ** [enum=['error']] — Specifies the status of the API request. 
Possible values:
**error** - Indicates that the request failed.

**Scopes:** ZohoCRM.bulk.READ, ZohoCRM.modules.ALL

# GET /{module}/{masterRecordId}/actions/merge
**Operation:** `getMergeJobStatus` — Get Merge Job Status
> To retrieve the status of a scheduled merge job in your Zoho CRM organization. Use the optional job_id query parameter to filter results to a specific job.

**Parameters:**
- `job_id` (query, string, optional) [maxLen=50, pattern=^[0-9]+$]: The ID represents the unique identifier of your scheduled merge job, which you get from the response of the [Merge Records API](find_and_merge.yaml#$.paths./{module}/{masterRecordId}/actions/merge.get). 
- `masterRecordId` (path, string, required) [maxLen=50, pattern=^[0-9]+$]: Specify the unique identifier of the master record to be retained after the merge operation. 
- `module` (path, string, required) [enum=['Accounts', 'Contacts', 'Leads', 'Deals', 'Cases', 'Campaigns']]: Specify the CRM module name containing the records to be merged.
Possible values:
**Accounts** - Accounts module.
**Contacts** - Contacts module.
**Leads** - Leads module.
**Deals** - Deals module.
**Vendors** - Cases module.
Additionally, **custom modules** are also supported in this API.  


**Responses:**

- **200**: Returns the current status of merge jobs for the specified master record.  [application/json]
    > Represents the response body containing the list of merge job status records for the specified master record. 
    - `merge` (array of object) [maxItems=100] **REQ** — Contains the list of merge job status objects returned for the specified master record.  
      - `job_id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Represents the unique identifier of the merge job.  
      - `status` (string) **REQ** [enum=['SCHEDULED', 'running', 'completed', 'failed']] — Represents the current processing status of the merge job. 
Possible values:
**SCHEDULED** - The merge job is queued and waiting to be processed.
**running** - The merge job is currently being processed.
**completed** - The merge job has finished successfully.
**failed** - The merge job encountered an error and did not complete. 


- **204**: Indicates that no merge jobs were found for the specified master record. 

- **400**: Returned when the request contains invalid parameters, module, or a business rule prevents the merge operation. 
**Resolution**: The request must be corrected based on the error code and the message returned in the response body. 
 [application/json]
    > Represents the error response body returned when the request fails due to validation errors, invalid data, or business rule violations. 
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'INVALID_MODULE', 'NOT_ALLOWED']] — Represents the error code that identifies the type of failure. 
Possible values:
**INVALID_DATA** - The request contains invalid or malformed data.
**INVALID_MODULE** - The specified module name is not valid.
**NOT_ALLOWED** - The requested operation is not permitted. 

        - `details` (object) — Contains additional context information about the error, such as the field API name, JSON path, and constraint limits that caused the validation failure. 
          - `resource_path_index` (integer/int32) — Represents the zero-based index of the path parameter that caused the error, where 0 corresponds to the module API name parameter and 1 corresponds to the master record ID in the parameter. 
          - `api_name` (string) [maxLen=100] — Represents the API name of the field or resource that caused the validation error. 
          - `json_path` (string) [maxLen=200] — Represents the JSON path to the field in the request that caused the validation error. 
          - `maximum_length` (integer/int32) — Represents the maximum allowed length for the field that caused the validation error. 
          - `minimum_length` (integer/int32) — Represents the minimum required length for the field that caused the validation error. 
        - `message` (string) **REQ** [maxLen=500] — Represents the error message that describes the issue in detail.  
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.  
**error** - The request failed due to a validation error or other issue.
        - `merge` (array of object) [maxItems=10] **REQ** — Contains the list of error details for each merge operation that failed validation.  
          - `code` (string) **REQ** [enum=[6 values]] — Represents the error code that identifies the type of failure for the merge operation.  
Possible values:
**MANDATORY_NOT_FOUND** - A required field or property is missing from the request.
**NOT_ALLOWED** - The operation is not permitted due to a business rule constraint.
**INVALID_DATA** - The request contains invalid data.
**DUPLICATE_DATA** - Duplicate values were detected for a field that must be unique.
**DEPENDENT_FIELD_MISSING** - A field that depends on another field is missing from the request.
**LIMIT_EXCEEDED** - A size or count limit has been exceeded.

          - `details` (object) — Contains detailed information about the field or resource that caused the error in the merge operation. 
            - `api_name` (string) [maxLen=100] — Represents the API name of the field that caused the validation error in the merge operation. 
            - `json_path` (string) [maxLen=200] — Represents the JSON path to the field in the request body that caused the validation error. 
            - `resource_path_index` (integer/int32) — Represents the zero-based index of the path parameter that caused the error. 
            - `maximum_length` (integer/int32) — Represents the maximum allowed length for the field that caused the validation error. 
            - `minimum_length` (integer/int32) — Represents the minimum required length for the field that caused the validation error. 
            - `MAXIMUM_SIZE` (string) [maxLen=50] — Represents the maximum allowed size for file or image uploads associated with the merge operation. 
            - `limit_due_to` (array of object) [maxItems=20] — Contains the list of fields whose combined file sizes caused the upload size limit to be exceeded. 
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contributed to exceeding the upload size limit.  
              - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path to the field in the request body that contributed to exceeding the upload size limit.  
            - `data` (array of object) [maxItems=10] — Contains the list of records that are associated with external configurations, such as CPQ rules, that prevent the merge operation from completing. 
              - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Represents the unique numeric identifier of the child record that has CPQ associations preventing the merge.  
              - `_associated_places` (array of object) [maxItems=50] — Contains the list of CPQ configurations or external rule associations that prevent this record from being merged. 
                - `type` (string) **REQ** [maxLen=100] — Represents the type of CPQ configuration that is associated with the record, such as product configurators or pricing rules.  
                - `resources` (array of object) [maxItems=50] **REQ** — Contains the list of CPQ resources, such as product configurators or pricing rules, that are associated with the record.  
                  - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Represents the unique numeric identifier of the CPQ resource.  
                  - `name` (string) **REQ** [maxLen=200] — Represents the display name of the CPQ resource.  
            - `dependee` (object) — Contains the API name and JSON path of the field that another field depends on, returned when a dependent field is missing from the request. 
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that the missing dependent field depends on.  
              - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path to the field that the missing dependent field depends on.  
          - `message` (string) **REQ** [maxLen=500] — Represents the error message that describes the specific validation failure for this merge operation.  
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the merge operation. 
Possible values: 
**error** - The merge operation failed due to a validation error.


**Scopes:** ZohoCRM.modules.custom.READ, ZohoCRM.modules.leads.READ, ZohoCRM.modules.contacts.READ, ZohoCRM.modules.accounts.READ, ZohoCRM.modules.potentials.READ, ZohoCRM.modules.vendors.READ

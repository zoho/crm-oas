# POST /__composite_requests
**Operation:** `createCompositeRequest` — Process multiple API requests in a single call
> To bundle multiple Zoho CRM API requests into a single HTTP call, reducing network round-trips and enabling request chaining. You can reference the output of one sub-request in another using the format **@{sub_request_id:JSONPath}** to build dependent workflows. When **rollback_on_fail** is enabled, all successful sub-requests are rolled back if any subsequent sub-request fails.


**Request Body** (required) — application/json
> Specify the data that the API requires to process the request.
  > Specify the composite request configuration, including execution options and the array of sub-requests to process.
  - `rollback_on_fail` (boolean) [default=False] — Specify whether to rollback the composite API request if any of the sub-requests fail. The default value is false.
Possible values:
**true** - Rollback all operations if any sub-request fails. Workflow automation actions execute only after all sub-requests succeed.
**false** - Process each sub-request independently without rollback.
This key cannot be **true** when **parallel_execution** is **true**.

  - `parallel_execution` (boolean) [default=True] — Specify whether  to process all independent sub-requests (sub-requests with no dependencies/references) in parallel. The default value is true. If "rollback_on_fail" is true, then the default value of this key is false.
Possible values:
**true** - Execute independent sub-requests in parallel.
**false** - Execute sub-requests sequentially.
This key cannot be **true** when **rollback_on_fail** is **true**.

  - `__composite_requests` (array of object) [maxItems=5] **REQ** — Specify the API requests to execute as sub-requests within the composite call.
    - `method` (string) **REQ** [enum=['GET', 'POST', 'PUT', 'DELETE', 'PATCH']] — Specify the HTTP method for the corresponding sub-request.
Possible values:
**GET** - Retrieve data from the API.
**POST** - Create a new resource.
**PUT** - Update an existing resource.
**DELETE** - Remove a resource.
**PATCH** - Partially update a resource.

    - `uri` (string) **REQ** [maxLen=2048, pattern=/crm(/.*)?/v[0-9]+([.][0-9]+)?/.*] — Specify the URI path of the corresponding sub-request. The URI must follow the pattern **/crm/{version}/{endpoint}** with the regex `/crm(/.*)?/v[0-9]+([.][0-9]+)?/.*`.
    - `sub_request_id` (string) [maxLen=100, pattern=[a-zA-Z0-9][a-zA-Z0-9_]*] — Specify a unique identifier for the sub-request. Use this ID to reference the output of this sub-request. The accepted regex is `[a-zA-Z0-9][a-zA-Z0-9_]*`.
    - `headers` (object) — Specify the HTTP headers for the sub-request. The **authorization** and **x-crm-org** headers are restricted and cannot be used.
    - `params` (object) — Specify the parameters for the sub-request.
    - `body` (object) — Specify the request body for the sub-request.

> **Note**
> - **Using References in Composite API Requests**: You can reference the output of one sub-request in another within the same API call.
> - **Reference Structure**: `@{sub_request_id:JSONPath}`
>   Where,
>   - `sub_request_id` is the ID of the sub-request whose response you want to reference.
>   - `JSONPath` is the path to the specific field in that response.
>   For example, if you create a Lead in one sub-request (sub_request_id : 1) and need to update it in another, you can use `@{1:$.data[0].details.id}` to dynamically fetch the Lead ID from sub-request 1 and use it in sub-request 2 to modify the same record. 
> - The `rollback_on_fail` and `parallel_execution` keys cannot both be set to `true`. If both are enabled, the API returns the `AMBIGUITY_DURING_PROCESSING` error.
> - All Delete APIs (except Notification APIs) support only record IDs in the URL. Bulk delete operations are not supported.
> - When `rollback_on_fail` is `false`:
>   - Workflows, approvals, and other automation actions are triggered as intended.
>   - The Composite API consumes one API credit.
> - When `rollback_on_fail` is `true`:
>    - **Workflows**
>      - Automation actions execute only after all sub-requests complete successfully and no rollback occurs. If one or more sub-requests fail and a rollback happens, the automation actions are not triggered.
>      - For example, consider the case where a workflow is triggered every time a lead is created with the company name starting with 'S'. In sub-request 1, a lead is created, whose Company name starts with 'S', and sub-request 2 edits the newly created record's company name so that it does not start with 'S'. Only after executing both the sub-requests the workflow will be executed. But in this case, the workflow will not be triggered because the newly created Lead's company name is already updated in sub-request 2, and the criterion for the workflow is not met. Consider another case, where in sub-request 1, a lead is created, whose Company name is 'Silicon Solutions', and sub-request 2 edits this newly created record's website. If none of the other sub-requests change the company name of this newly created record, after executing all the sub-requests successfully, the workflow will be triggered.
>    - When a rollback occurs, the Composite API consumes one API credit.
>    - When all sub-requests succeed, the Composite API consumes two API credits.
> - Each Composite API request consumes **five concurrency credits**, regardless of the number of sub-requests.
> - Each composite API reduces the sub-concurrency by one, while the sub-requests consume their respective sub-concurrencies.

### Allowed APIs
The following table gives the list of APIs allowed in a composite request. For these APIs, there are restrictions on the number of records that you can create, update, or delete in a composite request.

|  API | No. of records allowed |
| --- | --- |
| Get Org, Get Metadata, Convert a Lead, Get Layout Rules, Get Validation Rules, Get Custom Links, Get/Add/Update Roles, Get Profiles, Get Records' Count, Get/Update Blueprint, Get Variables/Variable Groups, Get Tags, Add/Remove Tags for a record, Get List of Attachments, Delete Photo, Get Currencies, Get Shared Record Details, Get Assignment Rules, Get/Add/Update Pipeline, Get Wizards, Get List of From Addresses, Delete Notifications | No Restriction | 
| Add/Update/Delete Users, Update/Delink Related Records, Add/Delete Variables, Create/Update/Delete Notes, Create/Update/Merge Tags, Add/Update Currency, Add/Update/PATCH Notifications, Create/Update/Upsert/Delete Records | 1 |
| Get Territories, Get Notes, Get Email/Inventory Templates, Get Notifications, Get/Search Records, Get Related Records, Get records through a COQL query, Get Deleted Records, Get Users | 25 |


**Responses:**

- **200**: Returns the response when all sub-requests in the composite call are executed successfully. [application/json]
    > Contains the successful response for a composite request where all sub-requests were executed successfully.
    - `__composite_requests` (array of object) [maxItems=5] **REQ** — Contains the response for each sub-request in the composite call. 
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the response code for the sub-request. 
Possible values:
**SUCCESS** - The sub-request was executed successfully.

      - `message` (string) **REQ** [maxLen=1000] — Represents the response message for the sub-request. 
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the sub-request execution. 
Possible values:
**success** - The sub-request was processed successfully.

      - `details` (object) **REQ** — Contains the detailed response information for the sub-request, including the HTTP response from the wrapped API call. 
        - `response` (object) **REQ** — Contains the response details from the wrapped API call, including the status code, headers, and body. 
          - `headers` (object) **REQ** — Contains the response headers from the wrapped API call. 
          - `body` (object) **REQ** — Contains the response body from the wrapped API call. 
          - `status_code` (integer/int32) **REQ** — Represents the status code from the wrapped API call. 

- **207**: Returns a multi-status response when some sub-requests succeed and others fail. Each item in the response array independently indicates success or failure for the corresponding sub-request. [application/json]
    > Contains the partial success response when some sub-requests succeed and others fail in the composite call.
    - `__composite_requests` (array of object) [maxItems=5] **REQ** — Contains the mixed success and error responses for individual sub-requests. Each item corresponds to a sub-request and indicates whether it succeeded or failed. 

- **400**: The request failed due to invalid input.
**Resolution:** Validate the request body structure, ensure all the field values  are valid, and verify that **rollback_on_fail** and **parallel_execution** are not both set to **true**.
 [application/json]
    > Contains the error response for composite request failures due to invalid input data or configuration.
    oneOf:
        - `code` (string) **REQ** [enum=[10 values]] — Represents the error code for the failed request. 
Possible values:
**DUPLICATE_DATA** - Duplicate data detected.
**NOT_SUPPORTED** - The requested operation is not supported.
**REQUEST_TIMEOUT** - The request timed out.
**LOOPING_FOUND** - Circular dependency detected among sub-requests.
**INVALID_DATA** - The input data is invalid.
**PROCESSING_STOPPED** - Processing was stopped due to an error.
**INVALID_REFERENCE** - An invalid reference was used.
**ROLLBACK_PERFORMED** - A rollback was performed due to a sub-request failure.
**MANDATORY_NOT_FOUND** - A required field is missing.
**AMBIGUITY_DURING_PROCESSING** - Ambiguous configuration detected.

        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the request.
Possible values:
**error** - The request failed.

        - `details` (object) **REQ** — Contains contextual information about the error, including the JSON path to the problematic field and the specific validation failure details. 
          oneOf:
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name or key that caused the validation error. 
              - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the key that caused the error within the request body. 
              - `expected_data_type` (string) **REQ** [maxLen=50] — Represents the expected data type for the field that failed validation. 
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name or key for the missing mandatory field. 
              - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the missing mandatory key within the request body. 
              - `ambiguity_due_to` (array of object) [maxItems=10] **REQ** — Contains the list of ambiguous references that caused the processing error. 
                - `api_name` (string) **REQ** [maxLen=100] — Represents the API name or key that has the ambiguous reference.
                - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the ambiguous reference within the request body. 
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name or key that exceeded the maximum allowed length. 
              - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field that exceeded the maximum allowed length. 
              - `maximum_length` (integer/int32) **REQ** [enum=[5]] — Represents the maximum allowed length for the field. For the composite requests array, this value is **five**. 
              - `allowed_services` (array of string) [maxItems=50] **REQ** — Contains the list of allowed API services that can be invoked in composite sub-requests. 
                items: [maxLen=100]
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name or key that failed the regular expression validation. 
              - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field that failed the regular expression validation. 
              - `regex` (string) **REQ** [maxLen=200] — Represents the regular expression pattern that the field value failed to match. 
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name or key that contains restricted parameters. 
              - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the sub-request containing restricted parameters.
              - `restricted_params` (array of string) [maxItems=50] **REQ** — Contains the list of query parameters that are restricted and cannot be used in composite sub-requests. 
                items: [maxLen=100]
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name or key that contains restricted headers.
              - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the sub-request containing restricted headers. 
              - `restricted_headers` (array of string) [maxItems=50] **REQ** — Contains the list of HTTP headers that are restricted and cannot be used in composite sub-requests. 
                items: [maxLen=100]
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name or key that contains an invalid reference expression.
              - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field containing the invalid reference expression. 
              - `reference` (string) **REQ** [maxLen=200] — Contains the invalid reference expression. Reference expressions use the format **@{sub_request_id:$.JSONPath}** to chain data between sub-requests. 

              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name or key that is part of a circular dependency. 
              - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the sub-request involved in the circular dependency. 
              - `sub_request_indexes` (array of integer/int32) [maxItems=10] **REQ** — Contains the array indexes of sub-requests that form a circular dependency chain. 
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name or key that caused the validation error. 
              - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field that caused the error within the request body. 
              - `regex` (string) **REQ** [maxLen=200] — Represents the regular expression pattern that the field value failed to match. 
              - `expected_data_type` (string) **REQ** [maxLen=50] — Represents the expected data type for the field that failed validation. 
              - `rollbacked_by_sub_request_index` (integer/int32) **REQ** — Represents the index of the sub-request that triggered the rollback operation. 
              - `sub_request_version` (integer/int32) **REQ** — Represents the API version used in the sub-request that caused the version mismatch. 
              - `composite_request_version` (integer/int32) **REQ** — Represents the API version used for the composite request. 
              - `dependent_data` (array of object) [maxItems=10] **REQ** — Contains information about sub-request dependencies when parallel execution is requested but sub-requests have interdependencies. 
                - `sub_request_id` (string) **REQ** [maxLen=100] — Represents the ID of the sub-request that has dependencies on other sub-requests. 
                - `referred_sub_request_ids` (array of string) [maxItems=5] **REQ** — Contains the IDs of sub-requests that this sub-request depends on through references. 
                  items: [maxLen=100]
        - `__composite_requests` (array of object) [maxItems=5] **REQ** — Provides an array of error responses for individual sub-requests.
          - `code` (string) **REQ** [enum=[11 values]] — Represents the error code indicating the type of error. 
          - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the request.
Possible values:
**error** - The request failed.

          - `details` (object) **REQ** — Contains the detailed response information for the sub-request, including the HTTP response from the wrapped API call. 
            oneOf:
                - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the key that has invalid data type.
                - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field that has invalid data type.
                - `expected_data_type` (string) **REQ** [maxLen=50] — Provides the expected data type for the field. 
                - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the mandatory key that is missing.
                - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the mandatory key that is missing.
                - `ambiguity_due_to` (array of object) [maxItems=10] **REQ** — List of ambiguous references causing the error.
                  - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the key that caused ambiguity.
                  - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the key that caused ambiguity.
                - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the key that exceeds the maximum length.
                - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the key that exceeds the maximum length.
                - `maximum_length` (integer/int32) **REQ** [enum=[5]] — The allowed maximum length is **five**. 
                - `allowed_services` (array of string) [maxItems=50] **REQ** — Provides the list of allowed services.
                  items: [maxLen=100]
                - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the key that has invalid regex.
                - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the key that has invalid regex.
                - `regex` (string) **REQ** [maxLen=200] — Represents the regular expression pattern that the field value failed to match.
                - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the restricted parameter. 
                - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON Path of the restricted parameter. 
                - `restricted_params` (array of string) [maxItems=50] **REQ** — Provides the list of restricted parameters. 


                  items: [maxLen=100]
                - `api_name` (string) **REQ** [maxLen=100] — Provides the API name of the restricted header.
                - `json_path` (string) **REQ** [maxLen=500] — Provides the JSON path of the restricted header.
                - `restricted_headers` (array of string) [maxItems=50] **REQ** — Provides the list of restricted headers.
                  items: [maxLen=100]
                - `api_name` (string) **REQ** [maxLen=100] — Provides the API name of the key with invalid reference. 
                - `json_path` (string) **REQ** [maxLen=500] — Provides the JSON path of the key with invalid reference. 
                - `reference` (string) **REQ** [maxLen=200] — Contains the invalid reference expression. Reference expressions use the format @{sub_request_id:$.JSONPath} to chain data between sub-requests.

                - `api_name` (string) **REQ** [maxLen=100] — Provides the API name of the keys that involved in dependencies.
                - `json_path` (string) **REQ** [maxLen=500] — Provides the JSON path of the keys that involved in dependencies.
                - `sub_request_indexes` (array of integer/int32) [maxItems=10] **REQ** — Represents the indexes of sub-requests involved in the loop.
                - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the key with invalid data.
                - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path of the key with invalid data.
                - `regex` (string) **REQ** [maxLen=200] — Represents the regular expression pattern that the field value failed to match.
                - `expected_data_type` (string) **REQ** [maxLen=50] — Provides the expected data type for the key. 
                - `rollbacked_by_sub_request_index` (integer/int32) **REQ** — Represents the index of the sub-request that triggered the rollback.
                - `sub_request_version` (integer/int32) **REQ** — Represents the version of the sub-request.
                - `composite_request_version` (integer/int32) **REQ** — Provides the version of the composite request.
                - `dependent_data` (array of object) [maxItems=10] **REQ** — Contains the information about dependent sub-requests.
                  - `sub_request_id` (string) **REQ** [maxLen=100] — Provides the ID of the dependent sub-request.
                  - `referred_sub_request_ids` (array of string) [maxItems=5] **REQ** — Provides the IDs of sub-requests the error depends on.
                    items: [maxLen=100]

**Scopes:** ZohoCRM.composite_requests.CUSTOM

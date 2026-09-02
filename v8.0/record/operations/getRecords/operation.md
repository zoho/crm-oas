# GET /{module}
**Operation:** `getRecords` — Get records from a specified module
> Retrieves records from the specified module in your Zoho CRM organization. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module ID and API name. Use "sort_by" and "sort_order" to control the sorting of records. To fetch up to 2000 records, use "page" (1-10) and "per_page" (maximum 200). To fetch more than 2000 records, use the "page_token" returned in the response. Consecutive page tokens can be used to navigate through up to 100,000 records. The "$has_more" key is returned when fetching a specific record and indicates whether more records are available in subforms, multi-select lookup fields, and multi-user lookup fields. To retrieve details of a related list, use the [Get Related Records API](related_records.yaml#$.paths./{parentRecordModule}/{parentRecord}/{relatedList}.get).

**Tags:** Records

**Parameters:**
- `module` (path, string, required) [maxLen=25]: Specify the API name of the module. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module ID and API name.
- `fields` (query, string, required): Specify a comma-separated list of field API names to include in the response. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to retrieve the field IDs and API names.
- `territory_id` (query, string/int64, optional): Specify the unique ID of the territory. Use the [Get Territories API](territories.yaml#$.paths./settings/territories.get) to retrieve the territory ID.
- `ids` (query, array, optional) [minItems=1, uniqueItems] {style=form, explode=False}: Specify a comma-separated list of record IDs. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the record IDs.
- `cvid` (query, string/int64, optional): Specify the unique ID of the Custom View. Use the [Get Custom Views Metadata API](custom_views.yaml#$.paths./settings/custom_views.get) to retrieve the Custom View IDs.
- `filters` (query, object, optional): Specify the filter criteria for retrieving specific Custom Views. Accepts a filter object to narrow down results based on Custom View properties.
- `cross_filters` (query, array, optional) [minItems=0, maxItems=3] {style=deepObject, explode=True}: Specify the filter criteria for retrieving specific Custom Views. Accepts a filter object to narrow down results based on Custom View properties.
- `filterId` (query, string/int64, optional) [maxLen=20]: The filter identifier
- `per_page` (query, integer/int32, optional) [min=1, max=200]: Specify the number of records to return per page. Maximum is 200.
- `page` (query, integer/int32, optional) [min=1]: Specify the page number to retrieve. Starts at 1.
- `page_token` (query, string, optional) [maxLen=96]: Specify the page token to retrieve records beyond the first 2,000 results. Use the **next_page_token** value from a previous response to access the next page of results.
- `sort_order` (query, string, optional) [enum=['desc', 'asc']]: Specify the sort order for the records.<br/> <b>Possible values:</b> <br/>desc - Returns records in descending order.<br/> asc - Returns records in ascending order.
- `sort_by` (query, string, optional) [enum=['id', 'Created_Time', 'Modified_Time']]: Specify the field to sort records by.  Possible values:**id** - Sorts by record ID.  **Created_Time** - Sorts by creation timestamp.  **Modified_Time** - Sorts by last modification timestamp.
- `converted` (query, string, optional) [enum=['false', 'true', 'both']]: Specify whether to retrieve converted, unconverted, or both types of records.  Possible values:**false** - Returns only unconverted records.  **true** - Returns only converted records.  **both** - Returns both converted and unconverted records.
- `include_child` (query, boolean, optional): Specify whether to include records assigned to child territories of the specified territory.

**Responses:**

- **200**: Returns the list of records retrieved from the specified module, including pagination metadata in the **info** object. — Schema: `RecordGETSuccessResponse` [application/json]
    > Represents the response schema for the record GET success operation.
    schema: `RecordGETSuccessResponse`
    - `data` (array of object `RecordGETDataItem`) [minItems=1, maxItems=100] **REQ** — Represents the data value.
      schema: `RecordGETDataItem`
      - `id` (string/int64) — Represents the unique identifier of the RecordGETDataItem record.
      - `Owner` (object) — Represents the owner value.
        - `name` (string) **REQ** [maxLen=101] — Represents the owner value.
        - `id` (string/int64) **REQ** — Represents the owner value.
        - `email` (string) [maxLen=256] — Represents the owner value.
      - `Created_Time` (string/date-time) — Represents the timestamp when the record was originally created.
      - `Modified_Time` (string/date-time) — Represents the timestamp when the record was last modified.
      - `Created_By` (object) — Contains information about the user who originally created the record.
        - `name` (string) **REQ** [maxLen=101] — Contains information about the user who originally created the record.
        - `id` (string/int64) **REQ** — Contains information about the user who originally created the record.
        - `email` (string) [maxLen=255] — Contains information about the user who originally created the record.
      - `Modified_By` (object) — Contains information about the user who last modified the record.
        - `name` (string) **REQ** [maxLen=101] — Contains information about the user who last modified the record.
        - `id` (string/int64) **REQ** — Contains information about the user who last modified the record.
        - `email` (string) [maxLen=255] — Contains information about the user who last modified the record.
      - `Wizard` (object) — Represents the wizard value.
        - `id` (string/int64) **REQ** [maxLen=19] — Represents the wizard value.
      - `$state` (string) [maxLen=255] — This will be as Save or Draft. 'save' indicates the record is not in any active Blueprint
      - `$wizard_connection_path` (string) [maxLen=2000, nullable] — $wizard_connection_path information denoted by comma separated connection ids between wizard screens.
      additionalProperties: any
    - `info` (object) **REQ** — Represents the info value.
      - `page` (integer/int32) **REQ** — Represents the info value.
      - `call` (boolean) — Represents the info value.
      - `per_page` (integer/int32) **REQ** — Represents the info value.
      - `count` (integer/int32) **REQ** — Represents the info value.
      - `more_records` (boolean) **REQ** — Represents the info value.
      - `email` (boolean) — Represents the info value.
      - `sort_by` (string) **REQ** [maxLen=255] — Represents the info value.
      - `sort_order` (string) **REQ** [enum=['asc', 'desc']] — Represents the info value.
      - `next_page_token` (string) **REQ** [maxLen=500, nullable] — Represents the info value.
      - `previous_page_token` (string) **REQ** [maxLen=500, nullable] — Represents the info value.
      - `page_token_expiry` (string/date-time) **REQ** [nullable] — Represents the info value.

- **204**: Returns an empty response when the request is successful but no records match the specified criteria.

- **400**: The request could not be processed due to invalid input or a missing required parameter.  **Resolution:** The request must include all required parameters with valid values. [application/json]
    > Represents the error response returned when a Get Records operation fails due to a validation, pagination, or processing error. The specific error variant is resolved via the discriminator on the **code** field.
    oneOf:
      - `InvalidDataGETError` — Represents the error response returned when the operation fails due to a invalid data GET error.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `param_name` (string) **REQ** — Contains additional context about the error.
          additionalProperties: any
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
      - `InvalidDataSortByError` — This error happens when attempting to retrieve records with information that doesn't match expected requirements. For example, an invalid sort_by parameter.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — A unique identifier for this specific type of error that helps identify what went wrong.
        - `message` (string) **REQ** — A clear explanation in plain language describing exactly why the request couldn't be completed.
        - `details` (object) **REQ** — Extra information that helps pinpoint the exact problem, such as which field had the invalid data.
          - `param_name` (string) **REQ** — Name of the parameter that contained invalid data.
          - `supported_values` (array of string) **REQ** — A list of valid values that can be used for the parameter in question.
            items: [maxLen=255]
          additionalProperties: any
        - `status` (string) **REQ** [enum=['error']] — Indicates whether the request was successful or failed. This will show 'error' because something went wrong.
      - `TokenBoundDataMismatchGETError` — Represents the error response returned when the operation fails due to a token bound data mismatch GET error.
        - `code` (string) **REQ** [enum=['TOKEN_BOUND_DATA_MISMATCH']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `param_name` (string) **REQ** — Contains additional context about the error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
      - `InvalidModuleGETError` — Represents the error response returned when the operation fails due to a invalid module GET error.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
      - `RequiredParamMissingGETError` — Represents the error response returned when the operation fails due to a required parameter missing GET error.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `param_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
      - `LimitExceededGETError` — Represents the error response returned when the operation fails due to a limit exceeded GET error.
        - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `limit` (integer/int32) **REQ** — Contains additional context about the error.
          - `param_name` (string) **REQ** — Contains additional context about the error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
      - `ExpiredValueGETError` — Represents the error response returned when the operation fails due to a expired value GET error.
        - `code` (string) **REQ** [enum=['EXPIRED_VALUE']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
          - `json_path` (string) **REQ** — Contains additional context about the error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
      - `PatternNotMatchedGetError` — Error indicating a pattern was not matched when retrieving records.
        - `code` (string) **REQ** [enum=['PATTERN_NOT_MATCHED']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `param_name` (string) **REQ** [maxLen=255] — Contains additional context about the error.
      - `DiscretePaginationLimitExceededGETError` — Represents the error response returned when the operation fails due to a discrete pagination limit exceeded GET error.
        - `code` (string) **REQ** [enum=['DISCRETE_PAGINATION_LIMIT_EXCEEDED']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `limit` (integer/int32) **REQ** — Contains additional context about the error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
      - `AmbiguityDuringProcessingGETError` — Represents the error response returned when the operation fails due to a ambiguity during processing GET error.
        - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `ambiguity_due_to` (array of object) **REQ** — Contains additional context about the error.
            - `param_name` (string) **REQ** — Parameter name of the ambiguous field.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
      - `PaginationLimitExceededGETError` — Represents the error response returned when the operation fails due to a pagination limit exceeded GET error.
        - `code` (string) **REQ** [enum=['PAGINATION_LIMIT_EXCEEDED']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `param_name` (string) **REQ** — Contains additional context about the error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.

- **401**: Authentication failed because the OAuth token is missing, expired, or does not include the required scope. **Resolution:** A new access token must be generated with the required scope for this operation. — Schema: `RecordUnauthorizedResponse` [application/json]
    > Represents the response schema for the record unauthorized operation.
    schema: `RecordUnauthorizedResponse`
    - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

- **403**: Permission denied to retrieve records from the specified module.  **Resolution:** The CRM administrator must grant the required module access permission to the user's profile. — Schema: `RecordPermissionResponse` [application/json]
    > Represents the response schema for the record permission operation.
    schema: `RecordPermissionResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.
      - `permissions` (array of string) [minItems=1, maxItems=100] **REQ** — Contains additional context about the error.
        items: [maxLen=255]

- **404**: The request URL does not match any valid API endpoint pattern.  **Resolution:** The API endpoint URL must be verified for correct format and path parameters. — Schema: `RecordInvalidURLResponse` [application/json]
    > Represents the response schema for the record invalid URL operation.
    schema: `RecordInvalidURLResponse`
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

- **500**: An unexpected server error occurred while processing the request.  **Resolution:** The request can be retried after some time. If the error persists, Zoho CRM support must be contacted. — Schema: `RecordInternalErrorResponse` [application/json]
    > Represents the error response returned when the operation fails due to a record internal response error.
    schema: `RecordInternalErrorResponse`
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

**Scopes:** ZohoCRM.modules.READ

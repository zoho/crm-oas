# POST /read
**Operation:** `createBulkReadJob` — Create a bulk read job
> To create a bulk read job in Zoho CRM. A bulk read job exports records from a specified CRM module to a CSV or ICS file. The job runs asynchronously; use the Get Bulk Read Job Details API to monitor the job status, and use the Download Bulk Read Result API to retrieve the exported file once the job is complete.

**Request Body** (required) — application/json
> The JSON request body used to configure and create a bulk read job in Zoho CRM.
  > Represents the request payload used to configure and create a bulk read job in Zoho CRM.
  - `callback` (object) — Specify the callback configuration to receive a POST notification when the bulk read job completes or fails.
    - `url` (string/uri) **REQ** — Specify a valid URL that accepts HTTP POST requests to receive the bulk read job completion notification.
    - `method` (string) **REQ** [enum=['post']] — Specify the HTTP method for the callback request.
Possible values:
**post** - Sends the callback notification as an HTTP POST request.
  - `query` (object) **REQ** — Specify the query parameters for the bulk read job, including the target module, optional field selection, optional Custom View, and optional filter criteria.
    - `module` (object) **REQ** — Specify the CRM module from which to export records. Refer to the [Get Modules](modules.json#$.paths./settings/modules.get) resource for valid values.
      - `api_name` (string) **REQ** [maxLen=255] — Specify the API name of the CRM module to export records from.
    - `cvid` (string) [maxLen=100, nullable] — Represents the unique ID of the Custom View to filter records for the bulk read job. Refer to the [Get Custom Views](custom_views.json#$.paths./settings/custom_views.get) resource for valid values.
    - `fields` (array of string) [maxItems=1000] — Specify the list of field API names to include in the exported records. Refer to the [Get Fields](fields.json#$.paths./settings/fields.get) resource for valid values. **Note:** If exporting Events as an **ICS file**, do not include this key.
      items: [maxLen=500]
    - `page` (integer/int32) [nullable] — Specify the page number of records to export in the bulk read job. The default value is **1** and means that the first **200,000** records matching your query will get exported. If you want to fetch the records from the range **200,001 to 400,000**, then mention the value as **'2'.**
    - `criteria` (object) — Specify the filter criteria to narrow down the records exported in the bulk read job.
      - `group_operator` (string) **REQ** [enum=['or', 'and']] — Specify the logical operator to combine the filter conditions in the **group** array.
Possible values:
**and** - All conditions must be satisfied.
**or** - At least one condition must be satisfied.
      - `group` (array of object) [maxItems=1000] **REQ** — Specify the list of filter conditions to apply to the bulk read export. Each condition must include a **field**, **value**, and **comparator**.
        - `field` (object) **REQ** — Specify the field to apply the filter condition on. Refer to the [Get Fields](fields.json#$.paths./settings/fields.get) resource for valid values.
          - `api_name` (string) **REQ** [maxLen=255] — Specify the API name of the field to use in the filter condition.
        - `value` (string) **REQ** [maxLen=500] — Specify the value to compare the field against in this filter condition.
        - `type` (string) [enum=['value']] — Specify the type of the filter condition.
Possible values:
**value** - Compares the field against a static value.
        - `comparator` (string) **REQ** [enum=['equal', 'contains', 'ends_with', 'not_contains', 'not_equal', 'starts_with']] — Specify the comparison operator to apply between the field and value in this filter condition.
Possible values:
**equal** - Records where the field value exactly matches the specified value.
**not_equal** - Records where the field value does not match the specified value.
**contains** - Records where the field value contains the specified value.
**not_contains** - Records where the field value does not contain the specified value.
**starts_with** - Records where the field value starts with the specified value.
**ends_with** - Records where the field value ends with the specified value.
  - `file_type` (string) [enum=['csv', 'ics']] — Specify the file format for the exported records.
Possible values:
**csv** - Exports records in CSV format.
**ics** - Exports records in ICS format, applicable only when exporting from the **Events** module.

**Responses:**

- **201**: The bulk read job was successfully created. The response includes the job ID and initial state. [application/json]
    > Represents the response returned when a bulk read job is successfully created.
    - `data` (array of object) [maxItems=1000] **REQ** — Represents the list of job creation result objects. 
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the job creation request. 
Possible values:
**success** - Zoho CRM created the bulk read job successfully.
      - `code` (string) **REQ** [enum=['ADDED_SUCCESSFULLY']] — Represents the status code for the job creation result.
Possible values:
**ADDED_SUCCESSFULLY** - Zoho CRM created the bulk read job successfully. 
      - `message` (string) **REQ** [enum=['Added successfully.']] — Represents the result message for the job creation. 
Possible values:
**Added successfully.** - Zoho CRM created the bulk read job successfully.
      - `details` (object) **REQ** — Represents the details of the newly created bulk read job. 
        - `id` (string) **REQ** [maxLen=100] — Represents the unique ID of the created bulk read job. 
        - `operation` (string) **REQ** [maxLen=500, enum=['read']] — Represents the type of bulk operation performed. 
Possible values:
**read** - Indicates a bulk read (export) operation.
        - `state` (string) **REQ** [enum=['COMPLETED', 'ADDED', 'IN PROGRESS', 'FAILURE']] — Represents the current state of the bulk read job. 
Possible values:
**ADDED** - The job has been accepted and is queued for processing.
**IN PROGRESS** - The job is currently being processed.
**COMPLETED** - The job has finished processing successfully.
**FAILURE** - The job encountered an error during processing.
        - `created_by` (object) **REQ** — Represents the user who created the bulk read job. Refer to the [Get Users](users.json#$.paths./users.get) endpoint for details. 
          - `id` (string) **REQ** [maxLen=100] — Represents the unique ID of the user who created the bulk read job. 
          - `name` (string) [maxLen=256] — Represents the name of the user who created the bulk read job.
        - `created_time` (string/date-time) **REQ** — Represents the date and time when Zoho CRM created the bulk read job. 
    - `info` (object) **REQ** — Represents additional metadata about the bulk read job creation response. 

- **400**: The request to create the bulk read job failed due to client-side validation errors. [application/json]
    > Represents the error response returned when the bulk read job creation request fails due to client-side validation errors.
    oneOf:
        - `code` (string) **REQ** [enum=['REQUEST_BODY_NOT_SUPPORTED']] — Represents the error code indicating that the request body format is not supported. 
Possible values:
**REQUEST_BODY_NOT_SUPPORTED** - The request body structure does not conform to the expected format.
        - `details` (object) **REQ** — Represents additional details about the error. 
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request. 
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=[2 values]] — Represents the error code indicating a criteria comparator incompatibility issue. 
Possible values:
**FIELD_COMPARATOR_IN_CRITERIA_NOT_SUPPORTED** - The comparator used for the specified field is not supported in the filter criteria.
**COMPARATOR_AND_VALUE_IN_CRITERIA_NOT_COMPATIBLE** - The comparator and value combination used in the filter criteria is not compatible.
        - `details` (object) **REQ** — Represents additional details about the criteria incompatibility error. 
          oneOf:
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the criteria error. 
              - `comparator` (string) **REQ** [maxLen=500] — Represents the comparator used in the criteria filter where the incompatibility was detected. 
              - `type` (string) **REQ** [maxLen=500] — Represents the data type of the field associated with the criteria error. 
              - `value` (object) **REQ** — Represents the value used in the criteria filter. 
                oneOf:
                    type: string [maxLen=500] — Represents a criteria field value of type string.
                    type: array of object [maxItems=1000]
                    type: boolean — Represents a criteria field value of type Boolean.
                    type: number — Represents a criteria field value of type number.
              - `comparator` (string) **REQ** [maxLen=500] — Represents the comparator used in the criteria filter where the incompatibility was detected. 
              - `type` (string) **REQ** [maxLen=500] — Represents the data type of the field associated with the criteria error. 
              - `value` (object) **REQ** — Represents the value used in the criteria filter. 
                oneOf:
                    - `name` (string) [maxLen=25] — Represents the name of the lookup value used in the criteria filter.
                    type: string [maxLen=500] — Represents a criteria field value of type string.
                    type: array of object [maxItems=1000]
                    type: boolean — Represents a criteria field value of type Boolean.
                    type: number — Represents a criteria field value of type number.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the criteria error. 
              - `comparator` (string) [maxLen=500] — Represents the comparator used in the criteria filter where the incompatibility was detected.
              - `type` (string) [maxLen=500] — Represents the data type of the field associated with the criteria error.
              - `value` (object) — Represents the value used in the criteria filter.
              - `field` (object) **REQ** — Represents the field associated with the criteria error. 
                - `api_name` (string) [maxLen=255] — Represents the API name of the field.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field for which the comparator is not supported. 
              - `supported` (array of string) [maxItems=1000] **REQ** — Represents the list of supported options for the specified field. 
                items: [maxLen=500]
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the criteria incompatibility issue. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request. 
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['AMBIGUOUS_CRITERIA', 'AMBIGUOUS_GROUP_IN_CRITERIA']] — Represents the error code indicating ambiguity in the filter criteria.
Possible values:
**AMBIGUOUS_CRITERIA** - The filter criteria is ambiguous and cannot be processed.
**AMBIGUOUS_GROUP_IN_CRITERIA** - A criteria group is ambiguous and cannot be processed.
        - `details` (object) **REQ** — Represents additional details about the ambiguous criteria error. 
          oneOf:
              - `api_name` (string) [maxLen=500] — Represents the API name of the field associated with the ambiguous criteria.
              - `comparator` (string) [maxLen=500] — Represents the comparator used in the ambiguous criteria filter.
              - `type` (string) [maxLen=500] — Indicates the data type of the field associated with the ambiguous criteria.
              - `value` (object) — Specifies the value used in the ambiguous criteria filter.
              - `field` (object) — Indicates the field associated with the ambiguous criteria.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field with ambiguous criteria. 
              - `type` (string) **REQ** [maxLen=500] — The data type of the field with ambiguous criteria. 
              - `comparator` (string) **REQ** [maxLen=25] — Represents the comparator used in the ambiguous criteria filter. 
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the ambiguous criteria. 
              - `type` (string) **REQ** [maxLen=500] — Specifies the data type of the field with ambiguous criteria. 
              - `value` (object) — Represents the value associated with the ambiguous criteria.
                oneOf:
                    type: string [maxLen=500] — Represents a criteria field value of type string.
              - `group` (array of object) [maxItems=1000] — Represents the ambiguous criteria group.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field in the criterion. 
                - `comparator` (string) **REQ** [maxLen=500] — Represents the comparator used in the criterion.
                - `type` (string) **REQ** [maxLen=500] — Represents the data type of the field in the criterion. 
                - `value` (object) **REQ** — Represents the value used in the criterion.
                  oneOf:
                      type: string [maxLen=500] — Represents a criteria field value of type string.
                - `field` (object) — Represents the field associated with the criterion.
                  - `api_name` (string) [maxLen=255] — Represents the API name of the field.
              - `group_operator` (string) [maxLen=500] — Represents the logical operator used to combine criteria within the group.
              - `group` (array of object) [maxItems=2] — Represents the ambiguous criteria group.
                - `comparator` (string) [maxLen=500] — Represents the comparator used in the criterion.
                - `type` (string) [maxLen=500] — Represents the data type of the field in the criterion.
                - `value` (string) [maxLen=25] — Represents the value used in the criterion.
                - `field` (object) — Represents the field associated with the criterion.
                  - `api_name` (string) [maxLen=255] — Represents the API name of the field.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the ambiguous criteria issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['INVALID_CALLBACK_METHOD', 'INVALID_CALLBACK_URL']] — Represents the error code indicating a callback configuration issue.
Possible values:
**INVALID_CALLBACK_METHOD** - The HTTP method specified for the callback URL is not valid.
**INVALID_CALLBACK_URL** - The callback URL specified in the request is not valid.
        - `details` (object) **REQ** — Represents additional details about the callback configuration error, including the list of supported callback methods.
          - `supported_callback_methods` (array of string) [maxItems=1000] — Represents the list of supported HTTP methods for callbacks.
            items: [maxLen=500]
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the callback configuration issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['GROUP_OPERATOR_NOT_SUPPORTED']] — Represents the error code indicating that the group operator used in the filter criteria is not supported. 
Possible values:
**GROUP_OPERATOR_NOT_SUPPORTED** - The logical operator used to combine criteria groups is not supported.
        - `details` (object) **REQ** — Represents additional details about the unsupported group operator error, including the  list of supported operators. 
          - `supported` (array of string) [maxItems=1000] **REQ** — Represents the list of supported group operators for the filter criteria.
            items: [maxLen=500]
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the unsupported group operator issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['PAGE_RANGE_EXCEEDED']] — Represents the error code indicating that the requested page number exceeds the allowed range.
Possible values:
**PAGE_RANGE_EXCEEDED** - The page number specified in the bulk read request exceeds the maximum allowed range.
        - `details` (object) **REQ** — Represents additional details about the page range exceeded error, including the maximum allowed page limit.
          - `max_limit` (integer/int32) **REQ** — Represents the maximum page number allowed for bulk read requests.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the page range exceeded issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Represents the error code indicating that the request is invalid.
Possible values:
**INVALID_REQUEST** - The bulk read request is malformed or contains invalid parameters.
        - `details` (object) **REQ** — Represents additional details about the invalid request error. 
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the invalid request issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request. 
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['MODULE_NOT_SUPPORTED']] — Represents the error code indicating that the specified module is not supported for bulk read operations.
Possible values:
**MODULE_NOT_SUPPORTED** - The module specified in the bulk read request does not support bulk read operations.
        - `details` (object) **REQ** — Represents additional details about the unsupported module error.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the unsupported module issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['CVID_NOT_SUPPORTED']] — Represents the error code indicating that the specified Custom View ID is not supported.
Possible values:
**CVID_NOT_SUPPORTED** - The Custom View ID (cvid) specified in the bulk read request is not supported.
        - `details` (object) **REQ** — Represents additional details about the unsupported Custom View error. 
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the unsupported Custom View ID issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=[21 values]] — Represents the error code for the bulk read request failure.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the request failure. 
        - `details` (object) **REQ** — Represents additional details about the error. 
          oneOf:
              - `criteria` (object) **REQ** — Represents the criteria object associated with the error. 
                - `field` (object) — Represents the field associated with the invalid criteria.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module or field associated with the error.
              - `module` (string) **REQ** [maxLen=255] — Represents the name of the module associated with the error.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field or module associated with the error.
              - `reason` (string) **REQ** [maxLen=500] — Represents the reason for the error.
              - `module` (string) [maxLen=500] — Represents the name of the module associated with the error.
              - `comparator` (string) **REQ** [maxLen=500] — Represents the comparator associated with the error.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
              - `supported` (array of string) [maxItems=1000] **REQ** — Represents the list of supported options for the specified field.
                items: [maxLen=500]
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the error.
              - `field_label` (string) **REQ** [maxLen=255] — Represents the display label of the field associated with the error.
        - `code` (string) **REQ** [enum=['INVALID_CRITERIA']] — Represents the error code indicating that the filter criteria in the request is invalid.
Possible values:
**INVALID_CRITERIA** - The criteria provided in the bulk read job request is not valid.
        - `details` (object) **REQ** — Represents additional details about the invalid criteria error, including the field and criteria values that caused the issue. 
          - `field` (object) — Represents the field object associated with the invalid criteria condition.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field associated with the invalid criteria.
            - `id` (string) **REQ** [maxLen=100] — Represents the unique ID of the field associated with the invalid criteria.
          - `api_name` (string) [maxLen=255] — Represents the API name of the field involved in the invalid criteria condition.
          - `comparator` (string) [maxLen=500] — Represents the comparator used in the invalid criteria condition.
          - `type` (string) [maxLen=500] — Represents the type of the criteria condition that caused the error.
          - `value` (object) — Represents the value used in the invalid criteria condition.
            oneOf:
                - `name` (string) [maxLen=25] — Represents the display name of the value involved in the invalid criteria condition.
                type: string [maxLen=500] — Represents a criteria field value of type string.
                type: boolean — Represents a criteria field value of type Boolean.
                type: array of string [maxItems=1000]
                  type: string [maxLen=500] — Represents a single item in the array value associated with the invalid criteria condition.
                  items: [maxLen=500]
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the invalid criteria issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['VALUE_TYPE_NOT_SUPPORTED']] — Represents the error code indicating that the value type used in the filter criteria is not supported.
Possible values:
**VALUE_TYPE_NOT_SUPPORTED** - The data type of the value provided for a criteria field is not supported.
        - `details` (object) **REQ** — Represents additional details about the unsupported value type error, including the field API name and the list of supported value types.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field for which the value type is not supported.
          - `supported` (array of string) [maxItems=1000] **REQ** — Represents the list of supported value types for the specified field.
            items: [maxLen=500]
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the unsupported value type issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['FIELD_NOT_SUPPORTED']] — Represents the error code indicating that the specified field is not supported for use in the bulk read criteria.
Possible values:
**FIELD_NOT_SUPPORTED** - The field specified in the filter criteria is not supported for bulk read operations.
        - `details` (object) **REQ** — Represents additional details about the unsupported field error, including the API name of the field.
          - `api_name` (string) [maxLen=255] — Represents the API name of the field that is not supported.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the unsupported field issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['MODULE_NOT_AVAILABLE']] — Represents the error code indicating that the specified module is not available in the CRM organization.
Possible values:
**MODULE_NOT_AVAILABLE** - The module specified in the bulk read request is not available.
        - `details` (object) **REQ** — Represents additional details about the unavailable module error.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module that is not available.
          - `reason` (string) [maxLen=500] — Represents the reason why the module is not available.
          - `module` (string) [maxLen=500] — Represents the name of the module associated with the error.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the unavailable module issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['FIELD_NOT_AVAILABLE']] — Represents the error code indicating that the specified field is not available in the CRM organization.
Possible values:
**FIELD_NOT_AVAILABLE** - The field specified in the bulk read request is not available.
        - `details` (object) **REQ** — Represents additional details about the unavailable field error.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the unavailable field issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['CRITERIA_LIMIT_EXCEEDED']] — Represents the error code indicating that the number of filter criteria groups exceeds the maximum allowed limit.
Possible values:
**CRITERIA_LIMIT_EXCEEDED** - The number of criteria groups in the bulk read request exceeds the maximum limit.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the criteria limit exceeded issue.
        - `details` (object) **REQ** — Represents additional details about the criteria limit exceeded error.
          - `max_limit` (integer/int32) [enum=[25]] — Represents the maximum number of filter criteria groups allowed in a bulk read request.
Possible values:
**25** - The maximum number of criteria groups permitted per request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['VALUE_LIMIT_EXCEEDED_IN_CRITERIA']] — Represents the error code indicating that the number of values in the filter criteria exceeds the maximum allowed limit.
Possible values:
**VALUE_LIMIT_EXCEEDED_IN_CRITERIA** - The number of values provided in the bulk read criteria exceeds the maximum limit of 200.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the value limit exceeded issue.
        - `details` (object) **REQ** — Represents additional details about the value limit exceeded error.
          - `max_limit` (integer/int32) [enum=[200]] — Represents the maximum number of values allowed in the filter criteria.
Possible values:
**200** - The maximum number of criteria values permitted per request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['VALUE_IN_CRITERIA_NOT_SUPPORTED']] — Represents the error code indicating that a value used in the filter criteria is not supported.
Possible values:
**VALUE_IN_CRITERIA_NOT_SUPPORTED** - The value provided for the criteria field is not supported.
        - `details` (object) **REQ** — Represents additional details about the unsupported criteria value error, including the field information, comparator, and value used.
          - `field` (object) — Represents the field associated with the unsupported criteria value.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field. 
            - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the field. 
          - `api_name` (string) [maxLen=255] — Represents the API name of the field associated with the unsupported criteria value.
          - `comparator` (string) [maxLen=500] — Represents the comparator used in the criteria filter where the unsupported value was detected.
          - `type` (string) [maxLen=500] — Represents the data type of the field associated with the unsupported criteria value.
          - `value` (object) — Represents the value that is not supported in the filter criteria.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the unsupported criteria value issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating that the criteria contains invalid data. 
Possible values:
**INVALID_DATA** - The data provided in the bulk read criteria is invalid.
        - `details` (object) **REQ** — Represents additional details about the invalid data error. 
          oneOf:
              - `field` (object) — Represents the field associated with the invalid data error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field. 
                - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the field. 
              - `api_name` (string) [maxLen=255] — Represents the API name of the field associated with the invalid data error.
              - `comparator` (string) [maxLen=500] — Represents the comparator used in the criteria filter where the invalid data was detected.
              - `type` (string) [maxLen=500] — Represents the data type of the field associated with the invalid data error.
              - `value` (object) — Represents the value that caused the invalid data error.
              - `api_name` (string) [maxLen=255] — Represents the API name of the field associated with the invalid data error.
              - `supported_values` (array of string) [maxItems=2] — Represents the list of valid values accepted for the specified field.
                items: [maxLen=25]
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the invalid data issue. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request. 
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) **REQ** [enum=['FIELD_IN_CRITERIA_NOT_SUPPORTED']] — Represents the error code indicating that a field used in the filter criteria is not supported. 
Possible values:
**FIELD_IN_CRITERIA_NOT_SUPPORTED** - The field specified in the filter criteria is not supported for bulk read operations.
        - `details` (object) **REQ** — Represents additional details about the unsupported criteria field error. 
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that is not supported in the filter criteria. 
          - `comparator` (string) **REQ** [maxLen=500] — Represents the comparator used with the unsupported criteria field. 
          - `value` (string) **REQ** [maxLen=500] — Represents the value used with the unsupported criteria field. 
          - `type` (string) **REQ** [maxLen=500] — Represents the data type of the unsupported criteria field. 
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the unsupported criteria field issue. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request. 
Possible values:
**error** - Indicates that the request failed.

**Scopes:** ZohoCRM.bulk.READ, ZohoCRM.modules.ALL

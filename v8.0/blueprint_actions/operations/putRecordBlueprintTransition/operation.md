# PUT /{moduleApiName}/{recordId}/actions/blueprint
**Operation:** `putRecordBlueprintTransition` — Update a single Blueprint transition for a record
> To update a single Blueprint transition for a record in your Zoho CRM organization.

**Parameters:**
- `moduleApiName` (path, string, required) [maxLen=255]: Specify the API name of the module that contains the record. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
- `recordId` (path, string, required) [maxLen=255]: Specify the unique ID of the record for which you want to retrieve or execute Blueprint transitions.

**Schemas:**
`ErrorInvalidDataMaxLength`:
  > Represents the error returned when the value of a field in the transition data exceeds the maximum allowed length. The **details** object identifies the field by its API name and JSON path and states the maximum length allowed.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request. Possible value: **INVALID_DATA**.
  - `details` (object) **REQ** — Represents the validation details that identify the field that failed and the reason for the failure.
    - `maximum_length` (integer/int32) **REQ** — Represents the maximum number of characters allowed for the field identified by **api_name**.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field for which the value exceeds the maximum allowed length.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field for which the value exceeds the maximum allowed length.
  - `message` (string) **REQ** [enum=['Invalid data', 'invalid data']] — Represents the error message that describes the failure. Possible values: **Invalid data**, **invalid data**.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request. Possible value: **error**.
`ErrorInvalidDataType`:
  > Represents the error returned when the value of a field in the transition data is not of the expected data type. The **details** object identifies the field by its API name and JSON path and states the expected data type.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the failed request. Possible value: **INVALID_DATA**.
  - `details` (object) **REQ** — Represents the validation details that identify the field that failed and the expected data type.
    - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type expected for the field identified by **api_name**.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field for which the value is not of the expected data type.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the request element that contains the invalid value.
  - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message that describes the cause of the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed transition request.
`ErrorMandatoryNotFound`:
  > Represents the error returned when a mandatory field is missing in the transition data.
  - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code that identifies the cause of the failure.

Possible values:
MANDATORY_NOT_FOUND - A mandatory field is missing in the transition data.
  - `details` (object) **REQ** — Represents additional details about the error, including the API name and JSON path of the missing mandatory field.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing mandatory field.
    - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the missing mandatory field in the request payload.
  - `message` (string) **REQ** [enum=['Required field is missing', 'required field not found']] — Represents the error message that describes the failure.

Possible values:
Required field is missing - A mandatory field is missing in the transition data.
required field not found - A mandatory field is missing in the transition data.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.

Possible values:
error - The request failed.
`ErrorRecordNotInProcess`:
  > Represents the error returned when the record is not part of an active Blueprint process.
  - `code` (string) **REQ** [enum=['RECORD_NOT_IN_PROCESS']] — Represents the error code returned when the record is not part of an active Blueprint process.
Possible values:
RECORD_NOT_IN_PROCESS - The record is not associated with an active Blueprint process.
  - `details` (object) **REQ** — Represents additional details of the error that occurred when the record is not part of an active Blueprint process.
  - `message` (string) **REQ** [enum=['record not in process']] — Represents the error message indicating that the record is not part of an active Blueprint process.
Possible values:
record not in process - The specified record is not associated with an active Blueprint process.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The request failed because the record is not part of an active Blueprint process.
`ErrorTransitionCriteriaFailed`:
  > Represents the error returned when a transition is executed without its criteria being met.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a transition is executed without its criteria being met.
Possible values:
INVALID_DATA - The record data does not satisfy the criteria configured for the transition.
  - `details` (object) **REQ** — Represents additional details of the error that occurred when the transition criteria are not met.
  - `message` (string) **REQ** [enum=['transition criteria failed']] — Represents the error message indicating that the transition criteria were not met.
Possible values:
transition criteria failed - The record data does not satisfy the criteria configured for the transition.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The operation failed because the transition criteria are not met.

**Request Body** — application/json `PutblueprintRequest`
> Specify the details required to update the Blueprint transition for the record. The payload carries the record's field values in the data object and can include related Notes and Attachments.
  > Represents the request body for executing a Blueprint transition on a record, carrying the Blueprint transition data to process.
  - `blueprint` (array of object `BlueprintNested`) [maxItems=1] **REQ** — Contains the Blueprint transition object to be processed for the record.
    schema: `BlueprintNested`
    - `state` (string) **REQ** [maxLen=50, enum=['draft', 'completed']] — Represents the state in which the transition is saved.
Possible values:
**draft** - The transition is saved as a draft.
**completed** - The transition is saved as completed.
    - `data` (object) — Represents the object that contains the field values required for the transition. Supports CheckLists and subform during fields, where the subform API name is the dynamic key and its value is an array of subform records. This value can be null when the transition payload supplies no during fields.
      oneOf:
        - `DataNested` — Represents the object that contains the field values required for the transition. Keys are field API names. Values can be: (a) primitive field values (string, number, Boolean, or null), (b) arrays for subform during fields or multi-record fields (for example, **Tag**, **Subform_1**) where each element is a key-value map, or (c) an associated module object whose properties include the associated module's field values and nested subform arrays (for example, **data.Sales_Order** with nested **Ordered_Items**).
          - `CheckLists` (array of object `ChecklistsNested`) [maxItems=100, nullable] — Represents the array of checklist items for the transition. Each item contains question-answer pairs.
          additionalProperties: (object)
            oneOf:
                type: array of object `SubformRecordNested` [maxItems=100]
                  schema: `SubformRecordNested`
                  additionalProperties: any
                additionalProperties: any
                type: string [maxLen=4000] — String field value for a regular blueprint during field.
                type: number — Numeric field value for a regular blueprint during field.
                type: boolean — Boolean field value for a regular blueprint during field.
                type: null — Null field value for a regular blueprint during field.
          type: null — Represents a null value, used when the transition payload supplies no during fields.
    - `transition_id` (string) **REQ** [maxLen=25] — Represents the unique ID of the Blueprint transition to execute.

**Responses:**

- **200**: Zoho CRM updates the Blueprint transition successfully. If the number of fields in the input does not meet the required number, Zoho CRM saves the transition partially. — Schema: `PutblueprintResponse200` [application/json]
    > Represents the response returned when a Blueprint transition is executed on a record, indicating the outcome of the transition execution with its status, code, message, and details.
    schema: `PutblueprintResponse200`
    - `code` (string) **REQ** [maxLen=255] — Represents the status code of the Blueprint transition execution, such as **SUCCESS**.
    - `details` (object) **REQ** — Contains additional details about the outcome of the Blueprint transition execution.
    - `message` (string) **REQ** [maxLen=255] — Represents the response message describing the outcome of the Blueprint transition execution.
    - `status` (string) **REQ** [maxLen=255] — Indicates the status of the Blueprint transition execution, such as **SUCCESS**.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed due to invalid syntax or an invalid value in the Blueprint request-body object.
**Resolution:** The client verifies the request structure and the transition_id field inside the Blueprint request-body object, then resends the request. [application/json]
    > Represents the error response for a Blueprint transition update request that fails due to invalid syntax.
    oneOf:
        - `blueprint` (array of object) [maxItems=25] **REQ** — Contains the errors that occur when the Blueprint transition update fails, such as when field validation fails or a field value's data type mismatches.
          oneOf:
            - `ErrorInvalidDataValidation` — Represents the error returned when the transition data fails validation, such as a missing mandatory field value. The **details** object lists every validation error identified in the request.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the transition data fails validation.
              - `details` (object) **REQ** — Represents the details of the validation errors in the transition data.
                - `validation_error` (array of object) [maxItems=25] **REQ** — Contains the list of validation errors identified in the transition data.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field or related list for which the validation failed.
                  - `message` (string) **REQ** [maxLen=255] — Represents the validation failure message for the field identified by **api_name**, such as a missing mandatory value.
                  - `info_message` (string) **REQ** [maxLen=255] — Represents additional information about the validation failure.
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message returned for the invalid transition data.

Possible values:
invalid data - The transition data failed validation.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.

Possible values:
error - The request failed.
            - `ErrorInvalidTransition` — Represents the error returned when the transition ID provided in the transition data is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code that identifies the cause of the failure.

Possible values:
INVALID_DATA - The transition ID provided in the transition data is invalid.
              - `details` (object) **REQ** — Represents additional details about the error. This object is empty for this error.
              - `message` (string) **REQ** [enum=['invalid transition']] — Represents the error message that describes the failure.

Possible values:
invalid transition - The transition ID provided in the transition data is invalid.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.

Possible values:
error - The request failed.
            - `ErrorNotAllowedParallelTransition` — Represents the error response returned when a parallel Blueprint transition is performed directly. A parallel transition cannot be executed directly.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when a parallel Blueprint transition is performed directly.
Possible values:
NOT_ALLOWED - Parallel transitions cannot be performed directly.
              - `details` (object) **REQ** — Represents the additional details of the error, including the API name of the parallel transition that cannot be performed directly.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the parallel transition that cannot be performed directly.
              - `message` (string) **REQ** [enum=['cannot perform the parallel transition directly']] — Represents the error message returned when a parallel transition cannot be performed directly.
Possible values:
cannot perform the parallel transition directly - The requested parallel transition cannot be executed directly.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The request failed.
            - `ErrorNotAllowedAutomaticTransition` — Represents the error response returned when an automatic Blueprint transition is performed directly. Automatic transitions run as part of the Blueprint process and cannot be executed directly.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when an automatic Blueprint transition is performed directly.
Possible values:
NOT_ALLOWED - Automatic transitions cannot be performed directly.
              - `details` (object) **REQ** — Represents the additional details of the error, including the API name of the automatic transition that cannot be performed directly.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the automatic Blueprint transition that cannot be performed directly.
              - `message` (string) **REQ** [enum=['cannot perform automatic transition']] — Represents the error message returned when an automatic Blueprint transition is performed directly.
Possible values:
cannot perform automatic transition - Automatic transitions run as part of the Blueprint process and cannot be executed directly.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The transition request failed.
            - `ErrorTransitionCriteriaFailed` — Represents the error returned when a transition is executed without its criteria being met.
            - `ErrorNoPermission` — Represents the error response returned when the user's CRM profile does not have permission to perform the Blueprint transition.
              - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code that identifies the cause of the failure.

Possible values:
NO_PERMISSION - The user's CRM profile does not have permission to perform the transition.
              - `details` (object) **REQ** — Represents the additional details of the error. This object is empty for this error.
              - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message returned when the transition cannot be performed because the user lacks the required permission.
Possible values:
permission denied - The user's CRM profile does not have permission to perform the Blueprint transition.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The transition request failed.
            - `ErrorMandatoryNotFound` — Represents the error returned when a mandatory field is missing in the transition data.
            - `ErrorInvalidDataType` — Represents the error returned when the value of a field in the transition data is not of the expected data type. The **details** object identifies the field by its API name and JSON path and states the expected data type.
            - `ErrorInvalidDataMaxLength` — Represents the error returned when the value of a field in the transition data exceeds the maximum allowed length. The **details** object identifies the field by its API name and JSON path and states the maximum length allowed.
            - `ErrorInvalidDataWithSupportedValues` — Represents the error returned when a field in the transition data contains an invalid value. The **details** object identifies the field by its API name and JSON path and lists the values it supports.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code that identifies the failure.

Possible values:
INVALID_DATA - The transition data contains an invalid value.
              - `details` (object) **REQ** — Represents additional details about the invalid value in the transition data, including the API name of the field, its path in the request JSON, and the values it supports.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that contains the invalid value.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that contains the invalid value.
                - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of values that the field identified by **api_name** supports.
                  items: [maxLen=255, enum=['draft', 'completed']]
              - `message` (string) **REQ** [enum=['Invalid data', 'invalid data']] — Represents the error message returned for the invalid value in the transition data.

Possible values:
Invalid data - The transition data contains an invalid value.
invalid data - The transition data contains an invalid value.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request, fixed to **error**.
            - `ManadatoryParamError` — Represents the error response returned when a mandatory parameter is missing from the request, with the error code, message, status, and details identifying the missing parameter.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned when a mandatory parameter is missing from the request.
Possible values:
**MANDATORY_NOT_FOUND** - A mandatory parameter is missing from the request.
              - `details` (object) **REQ** — Contains the error details with validation information, including the name of the missing mandatory parameter.
                - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the mandatory parameter that is missing from the request.
              - `message` (string) **REQ** [enum=['mandatory param missing']] — Represents the error message describing the issue.
Possible values:
**mandatory param missing** - A mandatory parameter is missing from the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
**error** - The request failed.
            - `ErrorRecordNotInProcess` — Represents the error returned when the record is not part of an active Blueprint process.
      - `ErrorInvalidDataType` — Represents the error returned when the value of a field in the transition data is not of the expected data type. The **details** object identifies the field by its API name and JSON path and states the expected data type.
      - `ErrorInvalidRecordId` — Represents the error returned when the record ID specified in the request URL is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the record ID in the request URL is invalid.
Possible values:
INVALID_DATA - The record ID specified in the request URL is invalid.
        - `details` (object) **REQ** — Represents additional details about the error, including validation information. This object is empty for this error.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message returned when the record ID in the request URL is invalid.
Possible values:
the ID given seems to be invalid - The record ID specified in the request URL is invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The request failed because the record ID in the request URL is invalid.
      - `ErrorInvalidModule` — Represents the error returned when the module API name specified in the request URL does not correspond to a valid module.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned for this failure, fixed to **INVALID_MODULE** when the module API name given in the request is invalid.
        - `details` (object) **REQ** — Contains additional details about the validation failure, including the index of the request path segment that holds the invalid module name.
          - `resource_path_index` (integer/int32) **REQ** — Indicates the zero-based index of the request path segment that contains the invalid module name.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message returned when the module API name in the request URL is invalid.
Possible values:
the module name given seems to be invalid - The module API name specified in the request URL does not correspond to a valid module.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The request failed because the module API name in the request URL is invalid.
      - `ErrorInvalidRequest` — Represents the error returned when the request body or request parameters are invalid or malformed.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Represents the error code returned when the request body or request parameters are invalid or malformed.
Possible values:
INVALID_REQUEST - The request body or request parameters are invalid or malformed.
        - `details` (object) **REQ** — Represents additional details about the error, including validation information. This object is empty for this error.
        - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned when the request body or request parameters are invalid or malformed.
Possible values:
unable to process your request. please verify whether you have entered proper method name, parameter and parameter values. - The request cannot be processed because the method name, parameter, or parameter values are invalid or malformed.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The request failed because the request body or request parameters are invalid or malformed.
      - `ErrorRecordNotInProcess` — Represents the error returned when the record is not part of an active Blueprint process.
      - `ErrorMandatoryNotFound2` — Represents the error response returned when a mandatory field is missing in the transition data.
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code that identifies the cause of the failure.

Possible values:
MANDATORY_NOT_FOUND - A mandatory field is missing in the transition data.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message that describes the failure.

Possible values:
Required field is missing - A mandatory field is missing in the transition data.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.

Possible values:
error - The request failed because a mandatory field is missing in the transition data.
      - `ErrorTransitionCriteriaFailed` — Represents the error returned when a transition is executed without its criteria being met.
      - `ErrorMandatoryNotFound` — Represents the error returned when a mandatory field is missing in the transition data.
      - `ErrorInvalidDataMaxLength` — Represents the error returned when the value of a field in the transition data exceeds the maximum allowed length. The **details** object identifies the field by its API name and JSON path and states the maximum length allowed.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The client does not have access rights to update Blueprint data on the record.
**Resolution:** The system administrator grants the required Blueprint permission to the user's Zoho CRM profile before the client retries the request. — Schema: `ErrorModuleNotSupported` [application/json]
    > Represents the error response returned when the module specified in the request URL is not supported by this API.
    schema: `ErrorModuleNotSupported`
    - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the error code that identifies the cause of the failure.

Possible values:
NOT_SUPPORTED - The given module is not supported in the API.
    - `details` (object) **REQ** — Represents additional details about the error, including the index of the request path segment that caused the failure.
      - `resource_path_index` (integer/int32) **REQ** — Represents the zero-based index of the request path segment that caused the failure.
    - `message` (string) **REQ** [enum=['the given module is not supported in api']] — Represents the error message that describes the failure.
Possible values:
the given module is not supported in API - The module in the request URL is not supported by this API.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.

Possible values:
error - The request failed because the given module is not supported in the API.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.modules.Leads.UPDATE, ZohoCRM.modules.Accounts.UPDATE, ZohoCRM.modules.Contacts.UPDATE, ZohoCRM.modules.Deals.UPDATE, ZohoCRM.modules.Campaigns.UPDATE, ZohoCRM.modules.Tasks.UPDATE, ZohoCRM.modules.Cases.UPDATE, ZohoCRM.modules.Events.UPDATE, ZohoCRM.modules.Solutions.UPDATE, ZohoCRM.modules.Products.UPDATE, ZohoCRM.modules.Vendors.UPDATE, ZohoCRM.modules.Pricebooks.UPDATE, ZohoCRM.modules.Quotes.UPDATE, ZohoCRM.modules.Salesorders.UPDATE, ZohoCRM.modules.Purchaseorders.UPDATE, ZohoCRM.modules.Invoices.UPDATE, ZohoCRM.modules.Notes.UPDATE, ZohoCRM.modules.Custom.UPDATE

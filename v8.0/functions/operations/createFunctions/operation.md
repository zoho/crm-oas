# POST /settings/functions
**Operation:** `createFunctions` — Function
> Use this API to create a function in your Zoho CRM account. Create Deluge, Java, Node.js, or Python functions with metadata and code. Deluge code can be JSON-embedded (`_code`) or uploaded as a .ds file; others require a ZIP package.

**Note:**
- Up to **20,000** functions per organization.
- Deluge: provide code via `_code` or the `code` form-data .ds file; if both are given, `code` takes precedence.
- If neither is given, the function is created as **active** with a default implementation, e.g. for **Cleanup Duplicates** (Standalone):

 string standalone.cleanup_duplicates()
 {
  return "";
 }

- Deluge declaration: lowercase function name (underscores for spaces) + lowercase category, e.g. **string standalone.restore_deal_by_name(...)**; return type must match the category default.
- Java, Node.js, Python: upload a ZIP via `code`. On compilation errors, the function is saved as a draft and **207 Partial Success** is returned.


**Schemas:**
`InvalidDataExpDataTypeError`:
  > The error response returned when a field value fails data type validation, identified by the **INVALID_DATA** error code.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code identifying the type of validation failure. Possible values: **INVALID_DATA** - The field value does not match the expected data type or format.
  - `details` (object) **REQ** — The details of the validation error, including the expected data type, maximum length, API name, and JSON path of the field that caused the error.
    - `expected_data_type` (string) **REQ** [maxLen=255] — The data type that the field expects, as determined by the field's schema definition.
    - `maximum_length` (integer/int32) **REQ** — The maximum number of characters or digits permitted for the field that failed validation.
    - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the data type error.
    - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the data type error.
  - `message` (string) **REQ** [enum=['Invalid data type']] — The error message describing the issue. Possible values: **Invalid data type** - The value provided for the field does not match the expected data type.
  - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
`InvalidDataMaxLenError`:
  > An error response returned when submitted data exceeds the maximum allowed length, including the error code, status, message, and validation details.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code identifying the type of validation failure. Possible values: **INVALID_DATA** - Indicates that the submitted data is invalid.
  - `details` (object) **REQ** — The validation details associated with the error, including the maximum allowed length, the API name of the field, and the JSON path to the invalid value.
    - `maximum_length` (integer/int32) **REQ** — The maximum number of characters allowed for the field that caused the error.
    - `api_name` (string) **REQ** [maxLen=255] — API name of the field that caused the error.
    - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
  - `message` (string) **REQ** [enum=['Invalid data']] — The error message returned when the submitted data exceeds the maximum allowed length for a field. Possible values: Invalid data - The submitted value exceeds the maximum character length defined for the field.
  - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: error - Indicates that the request failed due to invalid data.

**Request Body** — multipart/form-data
> The request body must contain a **multipart/form-data** payload with the function metadata and an optional code file attachment.
  > Represents the multipart form-data payload for creating a function, containing a **code** file upload and a **metadata** object with the function's configuration details.
  - `code` (string/binary) — Upload the function implementation. This parameter is optional for Deluge functions; if omitted, the function is created without an implementation. For Java, Node.js, and Python functions, upload the function package as a ZIP file.
  - `metadata` (object `PostfunctionsRequest`) — JSON string containing the metadata of the function being created. Includes function name, description, category, API name, runtime, and optional inline script (_code) for Deluge. Deluge code can also be uploaded as a .ds file via the `code` multipart form field. For non-Deluge runtimes, attach the code package as a ZIP via the `code` multipart form field.
    schema: `PostfunctionsRequest`
    - `functions` (array of object `FunctionsNested`) [maxItems=1, nullable] — The list of function metadata objects included in the request.
      schema: `FunctionsNested`
      - `_code` (string) [maxLen=2097152, minLen=1, nullable] — Inline function script content as a string. Applicable only for Deluge runtime — Deluge functions are auto-published when this field is set. For non-Deluge runtimes (Java, NodeJS, Python), upload a ZIP code package via the `code` multipart form field instead.
      - `api_name` (string) [maxLen=100, minLen=3, pattern=^[A-Za-z][A-Za-z0-9_-]*$, nullable] — The unique programmatic identifier for the function.
      - `name` (string) [maxLen=100, minLen=3, pattern=^[A-Za-z][A-Za-z0-9 _-]*$, nullable] — The display name of the function.
      - `description` (string) [maxLen=3000, nullable] — The description of the function's purpose and behavior.
      - `runtime` (string) [enum=['Deluge 1.0', 'Java 8', 'Java 17', 'NodeJS 8', 'NodeJS 22', 'Python 3.12'], nullable] — The execution runtime environment for the function. Possible values: **Deluge 1.0** - Deluge scripting language, version 1.0. **Java 8** - Java language runtime, version 8. **Java 17** - Java language runtime, version 17. **NodeJS 8** - Node.js runtime, version 8. **NodeJS 22** - Node.js runtime, version 22. **Python 3.12** - Python language runtime, version 3.12.
      - `category` (string) [enum=[8 values], nullable] — The trigger category that determines how and when the function executes. Possible values: **Button** - Triggered when a user clicks a button on a record. **Automation** - Triggered by an automated Workflow or rule. **Schedule** - Triggered at a scheduled time. **Related List** - Triggered from a related list on a record. **Standalone** - Executed independently without a specific trigger context. **Signals** - Triggered by a signal event. **Validation Rule** - Triggered as part of a Validation Rule evaluation. **Dynamic** - Triggered dynamically based on runtime conditions.
    - `publish` (object `PublishNested`) — This object will be used for function publish
      schema: `PublishNested`
      - `changelog` (string) [maxLen=250, nullable] — Changelog message for revision tracking. For Deluge functions, recorded as part of the auto-publish. For non-Deluge functions, recorded when the publish step succeeds.

**Responses:**

- **201**: Returns a confirmation that the function was created successfully. — Schema: `PostfunctionsResponse201` [application/json]
    > The response returned after a function is successfully created in the Zoho CRM organization. For Deluge functions, the function is auto-published upon creation. For non-Deluge functions that include a publish object, the function is created and published; omitting the publish object keeps the function as a draft.
    schema: `PostfunctionsResponse201`
    - `functions` (array of object `FunctionsNested1`) [maxItems=1] **REQ** — The list of function creation result objects returned by the operation.
      schema: `FunctionsNested1`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the operation result code. Possible values: **SUCCESS** - The operation completed successfully.
      - `details` (object `DetailsNested`) **REQ** — Details object returned in success responses, containing the unique identifier of the affected resource.
        schema: `DetailsNested`
        - `id` (string/int64) — Represents the unique identifier of the function that was created, updated, or deleted.
      - `message` (string) **REQ** [maxLen=255] — Represents the message describing the outcome of the operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation. Possible values: **success** - The operation completed without errors.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **207**: Returns a partial success response. The function record was created, but publishing failed due to a compilation error in the uploaded code. — Schema: `PostfunctionsResponse207` [application/json]
    > Represents a partial success response for function creation, where the function was created as a draft but the publish step failed due to compilation errors in the uploaded code.
    schema: `PostfunctionsResponse207`
    - `functions` (array of object `FunctionsNested207`) [maxItems=1] **REQ** — Contains the partial success details for the created function.
      schema: `FunctionsNested207`
      - `code` (string) [maxLen=255] — Represents the operation result code for the partial-success response, indicating whether the draft save and publish steps succeeded or failed.
      - `details` (object `DetailsNested207`) — Represents the details returned in a 207 partial success response, including the function ID and any compilation errors that caused the publish step to fail.
        schema: `DetailsNested207`
        - `id` (string/int64) **REQ** — Represents the unique identifier of the function that was created or updated.
        - `errors` (object `CodeFileNonDelugeCompilationErrors`) — Represents the error response returned when a non-Deluge function's code fails to compile during a publish attempt. Contains the error code **COMPILATION_ERROR**, along with details that include the file, line, and message for each compilation error.
          schema: `CodeFileNonDelugeCompilationErrors`
          - `code` (string) **REQ** [enum=['COMPILATION_ERROR']] — Represents the error code for the response. Possible values: **COMPILATION_ERROR** - Indicates the function's code failed to compile.
          - `details` (object) **REQ** — Represents the error details for the compilation failure, including the list of individual errors found in the code.
            - `errors` (array of object) [maxItems=5000] **REQ** — The list of compilation errors found in the function code.
              - `file` (string) [maxLen=5000] — Relative file path within the code package where the error occurred.
              - `line` (integer/int32) — Line number in the source file where the error occurred.
              - `message` (string) **REQ** [maxLen=5000] — The description of the compilation error.
          - `message` (string) **REQ** [enum=['function publish failed due to compilation errors']] — The error message returned when a function publish operation fails due to compilation errors. Possible values: **function publish failed due to compilation errors** - Indicates that the function could not be published because the code contains compilation errors.
          - `status` (string) **REQ** [enum=['error']] — The status of the response when a compilation error occurs. Possible values: **error** - Indicates that the operation failed due to a compilation error.
      - `message` (string) [maxLen=255] — Represents the message describing the outcome of the operation, indicating that the draft was saved but the publish step failed.
      - `status` (string) [maxLen=255] — Represents the overall status of the operation, reflecting the outcome of the draft save step regardless of whether the subsequent publish step succeeded.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed due to invalid syntax. **Resolution:** The request body must be corrected to use valid syntax before resubmitting. [application/json]
    > Contains the error details returned when the function creation request fails due to a 400 Bad Request condition, including the error code, message, and field-level dependency information.
    oneOf:
      - `ErrorResponseNoClientPortalSupport` — The error response returned when the requested API is not supported for client portal users.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — The error code identifying the cause of the failure. Possible values: **API_NOT_SUPPORTED** - The requested API is not supported for the current user type.
        - `details` (object) **REQ** — Additional error details associated with the failure, including information about the unsupported login user type.
          - `unsupported_login_user_type` (string) **REQ** [maxLen=255] — The type of login user that is not supported for this API.
        - `message` (string) **REQ** [enum=['api not supported for client portal user']] — The error message returned when the requested API is not supported for client portal users. Possible values: **api not supported for client portal user** - The API cannot be used by client portal users.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
      - `AttachedFileNotSupportedError` — Represents the error response returned when an attached file type is not supported by Zoho CRM.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of validation failure. Possible values: **INVALID_DATA** - Indicates the attached file type is not valid.
        - `details` (object) **REQ** — Represents the additional details about the validation failure, including information on supported file formats.
          - `supported_formats` (array of string) [maxItems=25] **REQ** — Represents the list of file formats supported for attachment in Zoho CRM.
            items: [maxLen=255]
        - `message` (string) **REQ** [enum=['attached file is not permitted']] — Represents the error message for the attached-file-not-supported condition. Possible values: **attached file is not permitted** - The attached file type is not allowed.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates that the request resulted in an error.
        - `functions` (array of object) [maxItems=25] **REQ** — Array of error objects
          oneOf:
            - `MandatoryNotFoundError` — The error response returned when a mandatory field is missing in a wrapped functions object.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — The error code identifying the type of error. Possible values: **MANDATORY_NOT_FOUND** - Indicates that a required field was not found in the request.
              - `details` (object) **REQ** — The details of the validation error, including the API name and JSON path of the missing mandatory field.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field for which the mandatory value was not found.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the mandatory-not-found error.
              - `message` (string) **REQ** [enum=['required field not found']] — The error message describing the issue. Possible values: **required field not found** - Indicates that a required field was not found in the request.
              - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
            - `DuplicateDataError` — Represents the error response returned when a submitted value duplicates an existing value in a unique field.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code for the duplicate data error. Possible values: **DUPLICATE_DATA** - Indicates that the submitted value already exists in a unique field.
              - `details` (object) **REQ** — Represents the details of the duplicate data error, including the API name and JSON path of the field that caused the conflict.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field for which the duplicate data error was triggered.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field for which the duplicate data error was triggered.
              - `message` (string) **REQ** [enum=['name duplicate', 'Api name duplicate']] — The error message describing the duplicate data violation. Possible values: **name duplicate** - The display name already exists. **Api name duplicate** - The API name already exists.
              - `status` (string) **REQ** [enum=['error']] — The status of the error response. Possible values: **error** - Indicates that the request resulted in an error.
            - `InlineScriptCompilationError` — Error returned when the inline Deluge script has compilation errors.
              - `code` (string) **REQ** [enum=['COMPILATION_ERROR']] — The error code for the compilation failure. Possible values: **COMPILATION_ERROR** - Indicates that the inline script failed to compile.
              - `details` (object) **REQ** — The details of the compilation error, including the field API name, the JSON path to the field, and the list of errors found in the script.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the compilation error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the compilation error.
                - `errors` (array of object) [maxItems=5000] **REQ** — The list of compilation errors found in the inline script.
                  - `code` (integer/int32) — The numeric error code returned by the compiler for the compilation error.
                  - `line` (integer/int32) **REQ** — The line number in the source script where the compilation error occurred.
                  - `index` (integer/int32) **REQ** — The character index position within the line where the compilation error occurred.
                  - `message` (string) **REQ** [maxLen=255] — The description of the compilation error.
              - `message` (string) **REQ** [enum=['function have compilation errors']] — The error message returned when an inline script fails compilation. Possible values: **function have compilation errors** - The inline script contains one or more compilation errors.
              - `status` (string) **REQ** [enum=['error']] — The status of the inline script compilation response. Possible values: **error** - Indicates that the compilation request resulted in an error.
            - `FeatureNotEnabledError` — The error response returned when a requested feature is not enabled in the CRM organization.
              - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — The error code identifying the feature-not-enabled condition. Possible values: **FEATURE_NOT_ENABLED** - The requested feature is not enabled in the CRM organization.
              - `details` (object) **REQ** — Additional details about the error, including the API name and JSON path of the field associated with the feature-not-enabled condition.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field associated with the feature-not-enabled error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field associated with the feature-not-enabled error.
              - `message` (string) **REQ** [enum=['feature is not enabled yet']] — The error message describing the feature-not-enabled condition.
              - `status` (string) **REQ** [enum=['error']] — The status of the error response. Possible values: **error** - Indicates that the request failed due to a feature or permission error.
            - `InlineCodeNotAllowedError` — The error response returned when inline code is not permitted for the requested function type.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — The error code indicating the reason for the failure. Possible values: **NOT_ALLOWED** - The requested operation is not allowed.
              - `details` (object) **REQ** — The details of the error, including the API name and JSON path of the field that caused the failure.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['_code not allowed']] — The error message describing the reason for the failure. Possible values: **_code not allowed** - Indicates that inline code is not permitted for this operation.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates the request resulted in an error.
            - `InvalidDataMinLenError` — An error response returned when the supplied data does not meet the minimum length requirement, including the error **code**, **status**, **message**, and **details** properties.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code identifying the type of validation failure. Possible values: **INVALID_DATA** - The submitted data does not meet the minimum length requirement for the field.
              - `details` (object) **REQ** — The validation details associated with the error, including the expected data type, maximum length, API name, and JSON path of the field that failed validation.
                - `expected_data_type` (string) [maxLen=255] — The data type expected for the field that triggered the validation error.
                - `maximum_length` (integer/int32) **REQ** — The maximum allowed length for the field that triggered the validation error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the validation error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path to the field that caused the validation error.
              - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the validation failure. Possible values: **invalid data** - The submitted field value does not meet the minimum length requirement.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: **error** - Indicates the request resulted in an error.
            - `InvalidDataExpDataTypeError` — The error response returned when a field value fails data type validation, identified by the **INVALID_DATA** error code.
            - `InvalidDataMaxLenError` — An error response returned when submitted data exceeds the maximum allowed length, including the error code, status, message, and validation details.
            - `InvalidDataSupportedValuesError` — Represents an error response returned when a field value fails a supported-values constraint validation.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code for this response. Possible values: **INVALID_DATA** - Indicates that the submitted field value does not satisfy the supported-values constraint.
              - `details` (object) **REQ** — The details of the validation error, including the field API name, expected data type, supported values, and the JSON path to the invalid field.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field for which the supported-values validation failed.
                - `expected_data_type` (string) [maxLen=255] — The expected data type for the field that caused the validation error.
                - `supported_values` (array of string) [maxItems=25] **REQ** — The list of valid values accepted for the field that caused the error.
                  items: [maxLen=255]
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['Invalid data', 'invalid data']] — The error message describing the invalid data condition.
              - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
            - `InvalidDataRegexPatternError` — An error response returned when a field value fails regex pattern validation.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code for this response. Possible values: **INVALID_DATA** - Indicates that the submitted field value does not meet the required data constraints.
              - `details` (object) **REQ** — The validation details for the field that caused the error, including its API name, expected data type, length constraints, regex pattern, and JSON path.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that failed validation.
                - `expected_data_type` (string) [maxLen=255] — The expected data type for the field that failed validation.
                - `maximum_length` (integer/int32) — The maximum allowed length for the field that failed regex pattern validation.
                - `minimum_length` (integer/int32) — The minimum required length for the field that failed regex pattern validation.
                - `regex` (string) **REQ** [maxLen=255] — The regular expression pattern that the field value must match.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the regex pattern validation error.
              - `message` (string) **REQ** [enum=['Invalid data', 'invalid data']] — The error message describing the invalid data condition.
              - `status` (string) **REQ** [enum=['error']] — The status of the API response for this error. Possible values: **error** - Indicates the request failed due to an invalid data regex pattern.
            - `InvalidDataWithMinAndMaxError` — An error response returned when a field value fails validation against minimum and maximum length constraints.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code identifying the type of validation failure. Possible values: **INVALID_DATA** - Indicates the submitted field value does not meet the required data constraints.
              - `details` (object) **REQ** — The details of the validation error, including the field API name, its JSON path, and the minimum and maximum length constraints that were violated.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field for which the validation error occurred.
                - `maximum_length` (integer/int32) — The maximum allowed length for the field that caused the validation error.
                - `minimum_length` (integer/int32) **REQ** — The minimum required length for the field that caused the validation error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the validation error.
              - `message` (string) **REQ** [enum=['invalid data', 'Invalid data']] — The error message describing the invalid data condition.
              - `status` (string) **REQ** [enum=['error']] — The status of the API response for this error. Possible values: **error** - Indicates the request failed due to invalid data.
            - `DependentMisMatchError` — Represents an error returned when a field value is incompatible with its dependent field configuration. Certain field categories are not supported for specific dependent field combinations.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — The error code for this error type. Possible values: **DEPENDENT_MISMATCH** - Indicates that a field value is incompatible with its dependent field configuration.
              - `details` (object) **REQ** — The details of the dependency mismatch error, including information about the mismatched field and its supported values.
                - `dependee` (object) **REQ** — The dependent field that triggered the mismatch, identified by its API name and JSON path.
                  - `api_name` (string) **REQ** [maxLen=255] — The API name of the dependent field that caused the mismatch.
                  - `json_path` (string) **REQ** [maxLen=1000] — The JSON path of the dependee field associated with the dependency mismatch.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the dependency mismatch error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the dependency mismatch error.
                - `supported_values` (array of string) [maxItems=25] **REQ** — The list of valid values for the field given the current dependee selection.
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['Dependent Field is not matching']] — The error message returned when a dependent field value does not match the expected condition. Possible values: **Dependent Field is not matching** - The value provided for a dependent field does not satisfy the dependency constraint.
              - `status` (string) **REQ** [enum=['error']] — The status of the API response for this error. Possible values: **error** - Indicates that the request resulted in an error due to a dependent field mismatch.
      - `CodeFileCompilationError` — Represents an error returned when a non-Deluge function has compilation errors during inline script validation.
        - `code` (string) **REQ** [enum=['COMPILATION_ERROR']] — The error code identifying the type of compilation failure. Possible values: **COMPILATION_ERROR** - Indicates that a compilation error was encountered during inline script validation.
        - `details` (object) **REQ** — The error details associated with the compilation failure, including the parameter name and the list of errors found in the function code.
          - `param_name` (string) **REQ** [maxLen=255] — The name of the parameter that caused the compilation error.
          - `errors` (array of object) [maxItems=5000] **REQ** — The list of compilation errors found in the function code.
            - `line` (integer/int32) **REQ** — Line number in the source file where the error occurred.
            - `index` (integer/int32) **REQ** — Character index position within the line where the error occurred.
            - `message` (string) **REQ** [maxLen=255] — The description of the compilation error at the associated line and character index.
        - `message` (string) **REQ** [enum=['function have compilation errors']] — The error message for the compilation failure. Possible values: **function have compilation errors** - Indicates that the code file contains one or more compilation errors.
        - `status` (string) **REQ** [enum=['error']] — The error status of the compilation response. Possible values: **error** - Indicates that a compilation error occurred.
      - `ErrorResponseFeatureNotSupported` — The error response returned when a requested feature is not supported for the current edition.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_SUPPORTED']] — The error code for this response. Possible values: **FEATURE_NOT_SUPPORTED** - Indicates that the requested feature is not supported for the current edition.
        - `details` (object) **REQ** — Additional details about the error.
        - `message` (string) **REQ** [enum=['Your License does not support this feature']] — The error message returned when the feature is not supported. Possible values: **Your License does not support this feature** - Indicates that the current license does not include the requested feature.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
      - `FxCreateLimitError` — Represents the error response returned when the function creation limit has been reached in the Zoho CRM organization.
        - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code identifying the type of limit error. Possible values: **LIMIT_EXCEEDED** - Indicates that the function creation limit has been exceeded.
        - `details` (object) **REQ** — Represents the details of the error, including the limit value that was exceeded.
          - `limit` (integer/int32) **REQ** — Represents the maximum number of functions allowed in the Zoho CRM organization.
        - `message` (string) **REQ** [enum=['function creation limit reached']] — Represents the error message describing the limit violation. Possible values: **function creation limit reached** - Indicates that the maximum number of functions allowed in the organization has been reached.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates the request resulted in an error.
      - `InvalidDataMetaDataError` — Represents an error response returned when a request field contains an invalid data type, including the error code, status, message, and validation details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of validation failure. Possible values: **INVALID_DATA** - Indicates that a request field contains an invalid data type.
        - `details` (object) **REQ** — Represents the validation details for the failed field, including the expected data type and the parameter name that caused the error.
          - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type that the field requires for a valid request.
          - `param_name` (string) **REQ** [maxLen=255] — Name of the parameter that caused the error.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the invalid data issue. Possible values: **invalid data** - Indicates that the submitted data failed validation.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for this error. Possible values: **error** - Indicates that the request resulted in an error.
      - `FileNameLengthError` — The error response returned when an attached code file name exceeds the maximum allowed length.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code identifying the type of error. Possible values: **INVALID_DATA** - Indicates that the provided data is invalid.
        - `details` (object) **REQ** — Represents the validation details for the file name length error, including the maximum allowed length and the name of the parameter that caused the error.
          - `maximum_length` (integer/int32) **REQ** — The maximum allowed length for the file name parameter.
          - `param_name` (string) **REQ** [maxLen=255] — Name of the parameter that caused the error.
        - `message` (string) **REQ** [enum=['attached file name exceeds the maximum length']] — The error message describing the file name length violation. Possible values: attached file name exceeds the maximum length - Indicates that the attached file name is longer than the permitted maximum length.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response for this error. Possible values: error - Indicates that the request resulted in an error.
      - `FileNameRegexError` — Represents the error returned when the uploaded file name does not match the expected naming pattern.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response. Possible values: **INVALID_DATA** - Indicates that the uploaded file name does not match the expected naming pattern.
        - `details` (object) **REQ** — The validation details for the file name regex error, including the regex pattern and the name of the parameter that failed validation.
          - `regex` (string) **REQ** [maxLen=255] — Regular expression pattern the field value must match.
          - `param_name` (string) **REQ** [maxLen=255] — Name of the parameter that caused the error.
        - `message` (string) **REQ** [enum=['attached file name not matched with the regex']] — The error message describing the file name validation failure. Possible values: **attached file name not matched with the regex** - The attached file name does not match the required regular expression pattern.
        - `status` (string) **REQ** [enum=['error']] — The status of the response for a file name regex validation failure. Possible values: **error** - Indicates that the request failed due to a file name validation error.
      - `CodePackageExistError` — Error returned when another function already exists with the same code package file name.
        - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — The error code returned when a duplicate code package file name is detected. Possible values: **DUPLICATE_DATA** - Indicates that another function already exists with the same code package file name.
        - `details` (object) **REQ** — The error details containing validation information about the request. Contains a **param_name** field identifying the parameter that caused the conflict.
          - `param_name` (string) **REQ** [maxLen=255] — The name of the parameter that caused the code package conflict error.
        - `message` (string) **REQ** [enum=['code package with the same file name already exists']] — The error message describing the conflict. Possible values: **code package with the same file name already exists** - Indicates that a code package with an identical file name already exists in the system.
        - `status` (string) **REQ** [enum=['error']] — The status of the response for this error. Possible values: **error** - Indicates that the request resulted in an error.
      - `CodePackageInvalidError` — Error returned when the uploaded code package is missing required language-specific files, contains unsupported files, or is otherwise invalid or corrupted.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure. Possible values: **INVALID_DATA** - Indicates the uploaded code package is invalid or contains unsupported content.
        - `details` (object) **REQ** — Represents the error details associated with the invalid code package, including information about the parameter that caused the failure.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter that caused the code package validation error.
        - `message` (string) **REQ** [enum=['code package is invalid or corrupted']] — Represents the error message describing the issue. Possible values: **code package is invalid or corrupted** - The uploaded code package is invalid or corrupted.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for this error. Possible values: **error** - Indicates the request resulted in an error.
      - `CodePackageFileNotFoundError` — Represents an error response returned when a required file is not found in the uploaded code package.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of error. Possible values: **INVALID_DATA** - Indicates the request contains invalid data.
        - `details` (object) **REQ** — Represents additional details about the validation error, including the name of the parameter that caused the issue.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter that caused the file-not-found error.
        - `message` (string) **REQ** [enum=['required file not found in the uploaded code package']] — Represents the error message describing the issue. Possible values: **required file not found in the uploaded code package** - Indicates that a required file is missing from the uploaded code package.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
      - `CodePackageFileInvalidError` — Represents an error response returned when one or more files in the uploaded code package are invalid or unsupported.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure. Possible values: **INVALID_DATA** - Indicates that one or more files in the uploaded code package are invalid or unsupported.
        - `details` (object) **REQ** — Represents the error details associated with the invalid code package file. Contains the **param_name** property identifying the parameter that caused the error.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter that caused the code package file validation error.
        - `message` (string) **REQ** [enum=['one or more files in the uploaded code package are invalid or unsupported']] — Represents the error message describing the issue with the uploaded code package.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error** - Indicates the operation encountered an error.
      - `FileNotAllowedError` — Represents the error response returned when an attached file type is not permitted for the operation.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of validation failure. Possible values: **INVALID_DATA** - Indicates that the attached file type is not allowed.
        - `details` (object) **REQ** — The validation details for the file attachment error, including the list of supported file formats and the name of the parameter that caused the error.
          - `supported_formats` (array of string) [maxItems=25] **REQ** — List of supported file formats.
            items: [maxLen=255]
          - `param_name` (string) **REQ** [maxLen=255] — The name of the parameter that caused the file attachment error.
        - `message` (string) **REQ** [enum=['attached file is not permitted']] — The error message returned when the attached file is not permitted. Possible values: attached file is not permitted - Indicates that the uploaded file type is not allowed.
        - `status` (string) **REQ** [enum=['error']] — The status of the error response. Possible values: **error** - Indicates the request resulted in an error.
      - `UnableToProcessError` — Represents an error response returned when the request cannot be processed.
        - `code` (string) **REQ** [enum=['CANNOT_PROCESS']] — Represents the error code for the operation. Possible values: **CANNOT_PROCESS** - The request could not be processed.
        - `details` (object) **REQ** — Represents additional details about the error, including any validation information associated with the request.
        - `message` (string) **REQ** [enum=['Unable to process your request']] — Represents the error message returned when the request cannot be processed. Possible values: **Unable to process your request** - Indicates that the server was unable to process the submitted request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for this error condition. Possible values: **error** - Indicates that the request resulted in an error.
      - `InitFxAdminOnlyAllowedError` — Represents the error response returned when the requested operation is restricted to administrators only.
        - `code` (string) **REQ** [enum=['CANNOT_PROCESS']] — Represents the error code identifying this error condition. Possible values: **CANNOT_PROCESS** - Indicates that the requested operation could not be processed.
        - `details` (object) **REQ** — Additional details about the error.
        - `message` (string) **REQ** [enum=['initial function creation is restricted to administrators']] — The error message describing the reason for the failure. Possible values: **initial function creation is restricted to administrators** - Indicates that only administrators are permitted to perform the initial function creation.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
      - `InvalidDataPublishError` — Represents an error response returned when a field value in a publish request contains an invalid data type.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code for the invalid data failure. Possible values: **INVALID_DATA** - Indicates that the field value provided in the request does not match the expected data type.
        - `details` (object) **REQ** — The details of the validation error, including the expected data type, maximum length, field API name, and JSON path of the field that failed validation.
          - `expected_data_type` (string) [maxLen=255] — The data type expected for the field that caused the validation error.
          - `maximum_length` (integer/int32) — The maximum character length allowed for the field that caused the validation error.
          - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the invalid data error.
          - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the invalid data error.
        - `message` (string) **REQ** [enum=['invalid data']] — The error message describing the invalid data condition. Possible values: **invalid data** - Indicates the request payload contains one or more fields with invalid data.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response for this error condition. Possible values: **error** - Indicates the request resulted in an error due to invalid data.
      - `RequireParamMissingError` — Represents the error response returned when a required request parameter is missing from the API call.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code identifying the failure type. Possible values: **REQUIRED_PARAM_MISSING** - Indicates that a required parameter was not included in the request.
        - `details` (object) **REQ** — Represents additional details about the missing parameter, including the name of the parameter that caused the error.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the required parameter that is missing from the request.
        - `message` (string) **REQ** [enum=['One of the expected param is missing', 'mandatory param missing']] — Represents the error message describing the missing parameter condition. Possible values: **One of the expected param is missing** - Indicates that at least one required parameter was not provided. **mandatory param missing** - Indicates that a mandatory parameter is absent from the request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates that the request failed due to a missing required parameter.
        - `functions` (object) **REQ**
          oneOf:
            - `InvalidDataExpDataTypeError` — The error response returned when a field value fails data type validation, identified by the **INVALID_DATA** error code.
            - `InvalidDataMaxLenError` — An error response returned when submitted data exceeds the maximum allowed length, including the error code, status, message, and validation details.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to create a function in the Zoho CRM organization. **Resolution:** The CRM administrator must grant the required permission to the user's profile. [application/json]
    > Represents the error response returned when the request is denied due to insufficient permissions.
    oneOf:
      - `NoDevPermissionError` — An error response returned when the requesting user lacks the required permission to perform the operation.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — The error code for the permission denial response. Possible values: **NO_PERMISSION** - The requesting user does not have permission to perform the operation.
        - `details` (object) **REQ** — Additional details about the permission denial error, including the permissions required to perform the operation.
          - `permissions` (array of string) [maxItems=25] **REQ** — The list of permissions required to perform the operation that was denied.
            items: [maxLen=255]
        - `message` (string) **REQ** [enum=['permission denied']] — The error message describing the permission denial. Possible values: **permission denied** - Indicates that the requesting user lacks the required permission to perform the operation.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
      - `UserEmailNotConfirmedError` — Represents the error response returned when the requesting user's email address has not been confirmed.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for this response. Possible values: **NO_PERMISSION** - Indicates the operation was not permitted.
        - `details` (object) **REQ** — Represents additional details about the error. This object is empty for this error type.
        - `message` (string) **REQ** [enum=['User email not confirmed']] — Represents the error message for this response. Possible values: **User email not confirmed** - Indicates the user's email address has not been confirmed.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates the request resulted in an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **413**: The request payload exceeds the maximum size the server accepts. **Resolution:** Reduce the file size before resubmitting. — Schema: `CodeFileSizeError` [application/json]
    > Represents an error response returned when the uploaded code file exceeds the maximum permitted size limit.
    schema: `CodeFileSizeError`
    - `code` (string) **REQ** [enum=['FILE_SIZE_EXCEEDS']] — Represents the error code for the file size violation. Possible values: **FILE_SIZE_EXCEEDS** - The uploaded file exceeds the maximum permitted size limit.
    - `details` (object) **REQ** — The error details containing file size validation information.
      - `size` (integer/int32) **REQ** — Maximum allowed file size in kilobytes.
    - `message` (string) **REQ** [enum=['file size exceeds']] — The error message for the file size violation. Possible values: **file size exceeds** - Indicates that the uploaded file exceeds the allowed size limit.
    - `status` (string) **REQ** [enum=['error']] — The status of the response. Possible values: **error** - Indicates that the request encountered an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.functions.CREATE

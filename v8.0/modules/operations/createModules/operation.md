# POST /settings/modules
**Operation:** `createModules` — Create a custom module
> To create a custom module in your Zoho CRM organization. Only one module can be created per request. The required permission depends on the access type: **Crm_Implied_Customize_Zoho_CRM** for org-based modules and **Crm_Implied_Create_Team_Module** for team-based modules. Submitting the same api_name multiple times will result in validation errors. The optional access_type controls module access model (org_based/team_based).

**Request Body** (required) — application/json
> The request body must contain a modules array with one object. Only single module creation is supported per request. access_type is optional and defaults to org_based. For team_based modules, do not pass profiles.
  > Represents the request body structure for creating a custom module, containing the module definition in the **modules** array.
  - `modules` (array of object) [minItems=1, maxItems=1] **REQ** — Specify the module definitions to create. Only one module definition object can be included per request.

**Responses:**

- **201**: Returns the success result of the module creation, including the unique identifier of the newly created module. [application/json]
    > Represents the response body returned when a custom module is successfully created, containing the resulting module details in a modules array.
    - `modules` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the array containing the result of the single module creation request. Contains exactly one item for each module creation request.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the status code of the module creation operation.
Possible values:
**SUCCESS** - The module creation completed successfully.
      - `details` (object) **REQ** — Represents the details of the created module, including its unique identifier.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the newly created module.
      - `message` (string) **REQ** [enum=['module created successfully']] — Represents the confirmation message for the module creation operation.
Possible values:
**module created successfully** - The module creation completed without errors.
      - `status` (string) **REQ** [enum=['success']] — Represents the overall status of the module creation operation.
Possible values:
**success** - The module creation completed successfully.

- **400**: The request failed validation.
**Resolution:** Verify that all required fields are provided with valid values. Returned when input data fails validation (invalid module properties, duplicate api_name, missing required fields, field length exceeded, unsupported operations, or mandatory fields not found). All modules in the batch must be valid; no partial success occurs. [application/json]
    > Contains the error response when the module creation request fails validation.
    oneOf:
        - `modules` (array of object) [maxItems=1] **REQ** — Represents the array of error responses for each module that failed validation
          oneOf:
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code returned when the request contains duplicate data.
Possible values:
**DUPLICATE_DATA** - A duplicate value was found for **singular_label**, **plural_label**, or **api_name**.
              - `details` (object) **REQ** — Represents the details identifying the field that caused the duplicate data error, including its API name and location in the request.
                - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the field for which a duplicate value was found.
                - `json_path` (string) **REQ** [maxLen=100] — Represents the JSONPath expression identifying the location of the duplicate field in the request body.
              - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the duplicate data constraint violation.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.
Possible values:
**error** - The module creation request failed due to a duplicate data constraint.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned when a mandatory field is absent from the request.
Possible values:
**MANDATORY_NOT_FOUND** - A required field is missing from the request.
              - `details` (object) **REQ** — Represents additional information identifying the mandatory field that is missing, including its API name and location in the request.
                - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the mandatory field that is missing from the request.
                - `json_path` (string) **REQ** [maxLen=100] — Represents the JSONPath expression identifying the location in the request where the mandatory field should be specified.
              - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the missing mandatory field.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.
Possible values:
**error** - The module creation request failed due to a missing mandatory field.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code returned when a required dependent field is missing from the request.
Possible values:
**DEPENDENT_FIELD_MISSING** - A dependent field required by the specified configuration is absent.
              - `details` (object) **REQ** — Represents additional information identifying the dependent field that is missing, including its API name and location in the request.
                - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the dependent field that is missing from the request.
                - `json_path` (string) **REQ** [maxLen=100] — Represents the JSONPath expression identifying the location in the request where the dependent field should be specified.
              - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the missing dependent field.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.
Possible values:
**error** - The module creation request failed due to a missing dependent field.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the request contains invalid or malformed data.
Possible values:
**INVALID_DATA** - The request contains an invalid data type, invalid profile ID, or values that exceed allowed field lengths.
              - `details` (object) **REQ** — Represents additional information about the invalid field, including its API name, location in the request, expected data type, and maximum allowed length.
                - `maximum_length` (integer/int32) — Represents the maximum number of characters allowed for the field that exceeded the length constraint.
                - `expected_data_type` (string) [maxLen=50] — Represents the expected data type for the field that contains invalid data.
                - `api_name` (string) [maxLen=50] — Represents the API name of the field that contains invalid data.
                - `json_path` (string) [maxLen=100] — Represents the JSONPath expression identifying the location of the invalid field in the request body.
              - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the invalid data that caused the request to fail.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.
Possible values:
**error** - The module creation request failed due to invalid or malformed data.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when the requested operation is not permitted.
Possible values:
**NOT_ALLOWED** - The operation is not allowed.
              - `details` (object) **REQ** — Represents additional information about the error, including the location of the field or operation that is not allowed.
                - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the field or operation that is not allowed.
                - `json_path` (string) **REQ** [maxLen=100] — Represents the JSONPath expression identifying the location of the disallowed field or operation in the request body.
              - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing why the operation is not allowed.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.
Possible values:
**error** - The module creation request failed because the operation is not permitted.
              - `code` (string) **REQ** [enum=['RESERVED_KEYWORD_NOT_ALLOWED']] — Represents the error code returned when a reserved system keyword appears in the **api_name** field.
Possible values:
**RESERVED_KEYWORD_NOT_ALLOWED** - The value contains a reserved system keyword.
              - `details` (object) **REQ** — Represents additional information identifying the field that contains the reserved keyword, including its API name and location in the request.
                - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the field containing the reserved keyword.
                - `json_path` (string) **REQ** [maxLen=100] — Represents the JSONPath expression identifying the location of the field containing the reserved keyword in the request body.
              - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the reserved keyword violation.
              - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.
Possible values:
**error** - The module creation request failed due to a reserved keyword violation.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Represents the error code returned when the API version used is not supported.
Possible values:
**API_NOT_SUPPORTED** - The requested API version is not supported.
        - `details` (object) **REQ** — Represents additional context about the API version incompatibility, including the minimum supported version.
          - `supported_version` (integer/int32) **REQ** — Represents the minimum API version that supports this operation.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the API version incompatibility.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.
Possible values:
**error** - The module creation request failed because the API version is not supported.
        - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code returned when the request contains a duplicate value for a unique field.
Possible values:
**DUPLICATE_DATA** - A duplicate value was found for **singular_label**, **plural_label**, or **api_name**.
        - `details` (object) **REQ** — Represents additional information identifying the field that caused the duplicate data error, including its API name and location in the request.
          - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the field for which a duplicate value was found.
          - `json_path` (string) **REQ** [maxLen=100] — Represents the JSONPath expression that locates the duplicate field within the request payload.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the duplicate data constraint violation.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.
Possible values:
**error** - The module creation request failed due to a duplicate data constraint.
        - `code` (string) **REQ** [enum=['RESERVED_KEYWORD_NOT_ALLOWED']] — Represents the error code returned when a reserved system keyword appears in the **api_name** field at the top level.
Possible values:
**RESERVED_KEYWORD_NOT_ALLOWED** - The value contains a reserved keyword.
        - `details` (object) **REQ** — Represents additional information about the field that uses the reserved keyword, including its API name and location.
          - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the field containing the reserved keyword.
          - `json_path` (string) **REQ** [maxLen=100] — Represents the JSONPath expression identifying the location of the reserved keyword field in the request.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the reserved keyword violation.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.
Possible values:
**error** - The module creation request failed due to a reserved keyword violation.
        - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code returned when the module creation limit for the current edition has been reached.
Possible values:
**LIMIT_EXCEEDED** - The maximum number of custom modules allowed for this edition has been reached.
        - `details` (object) **REQ** — Represents additional context about the exceeded module creation limit for the current edition.
          - `limit` (integer/int32) **REQ** — Represents the maximum number of custom modules allowed for the current edition.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the module creation limit exceeded.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.
Possible values:
**error** - The module creation request failed because the edition limit has been reached.

- **401**: The access token does not include the required scope for this operation.
**Resolution:** A new access token must be generated with the **ZohoCRM.settings.modules.CREATE** scope. [application/json]
    > Represents the error response body returned when the OAuth access token does not include the required scope for this operation.
    - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code returned when the OAuth token does not include the required scope.
Possible values:
**OAUTH_SCOPE_MISMATCH** - The access token does not include the required scope for this operation.
    - `details` (object) **REQ** — Represents additional context about the OAuth scope issue encountered during the request.
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the OAuth scope mismatch.
    - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.
Possible values:
**error** - The module creation request failed because the OAuth token lacks the required scope.

- **403**: No permission to create custom modules.
**Resolution:** The CRM administrator must grant the required module-creation permission to the user's profile. [application/json]
    > Represents the error response body returned when the user's CRM profile lacks the required permission to create a custom module. Crm_Implied_Customize_Zoho_CRM is required for org_based creation, and Crm_Implied_Create_Team_Module is required for team_based creation.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned when the user lacks the required CRM permission to create a custom module.
Possible values:
**NO_PERMISSION** - The user's profile does not have the required permission for this operation.
    - `details` (object) **REQ** — Represents additional information about the missing permissions required to create the module.
      - `permissions` (array of string) [maxItems=1] **REQ** — Represents the list of permission identifiers that the user lacks for the requested access type.
Possible values:
**Crm_Implied_Customize_Zoho_CRM** - Required for org-based module creation.
**Crm_Implied_Create_Team_Module** - Required for team-based module creation.
        items: [enum=['Crm_Implied_Customize_Zoho_CRM', 'Crm_Implied_Create_Team_Module']]
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the permission denial.
    - `status` (string) **REQ** [enum=['error']] — Represents the error status of the response.
Possible values:
**error** - The module creation request failed because the user lacks the required permission.

**Scopes:** ZohoCRM.settings.modules.CREATE

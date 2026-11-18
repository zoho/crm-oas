# POST /settings/wizards
**Operation:** `createWizard` — Wizards
> Creates a wizard configuration for a specified module.

**Request Body** (required) — application/json
> Provide the wizard configuration to create, including module, profiles, containers, screens, segments, buttons, and conditional rules.
  > The request body to create a wizard.
  - `wizards` (array of object) [maxItems=1] **REQ** — The definition of the wizard structure.
    - `module` (object) **REQ** — Module information for which the wizard is configured. Either api_name or id must be provided.
    - `name` (string) **REQ** [maxLen=30] — Unique name of the wizard used in the API.
    - `profiles` (array) [maxItems=50] — Profiles that are allowed to access this wizard.
    - `portal_user_types` (array) [maxItems=50] — Specify the list of client portal user types allowed to access this wizard. Either `profiles` or `portal_user_types` must be provided.
    - `active` (boolean) **REQ** — Indicates whether the wizard is currently enabled.
    - `containers` (array) **REQ** [maxItems=7] — Containers that define the layout and flow of the wizard.
    anyOf:
        additionalProperties: any
        additionalProperties: any

**Responses:**

- **201**: The response body after a successful wizard creation. [application/json]
    > The definition of the response body structure after a successful wizard creation.
    - `wizards` (array of object) [maxItems=1] **REQ** — The wizards that have been created.
      - `status` (string) **REQ** [enum=['success']] — This describes whether the wizard creation was successful or not.
      - `code` (string) **REQ** [enum=['SUCCESS']] — This represents the success or error codes of the request.
      - `message` (string) **REQ** [maxLen=255] — This describes the message returned from the server after wizard a successful wizard creation.
      - `details` (object) **REQ** — Additional information about the request payload after successful execution.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the wizard.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad Request. The wizard definition is invalid or fails one or more validation checks. [application/json]
    > Validation error response returned when wizard creation fails.
    oneOf:
        - `wizards` (array of object) [maxItems=1] **REQ** — List of validation results for each wizard in the request body.
          oneOf:
              - `status` (string) **REQ** [enum=['error']] — Indicates that the request failed.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Error code for dependent field missing validation failure.
              - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
              - `details` (object) **REQ** — Additional details about the field or value that failed validation.
                - `api_name` (string) [maxLen=255] — API name of the field involved in the error, if applicable.
                - `json_path` (string) **REQ** [maxLen=255] — JSON path pointing to the invalid field in the request payload.
                - `expected_data_type` (string) [maxLen=100] — Expected data type for the field, when the error is related to type mismatch.
                - `regex` (string) [maxLen=500] — Validation pattern that the value must satisfy, if applicable.
                - `merge_field` (string) [maxLen=255] — Merge field value that caused the validation error, if applicable.
                - `maximum_length` (integer/int32) — Maximum allowed length for the field, when the provided value is too long.
                - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the field.
                - `dependee` (object) — Details of the field that another field depends on, for DEPENDENT_FIELD_MISSING errors.
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the depended-on field.
                  - `json_path` (string) **REQ** [maxLen=255] — JSON path of the depended-on field in the request payload.
              - `status` (string) **REQ** [enum=['error']] — Indicates that the request failed.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code for invalid data validation failure.
              - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
              - `details` (object) **REQ** — Additional details about the field or value that failed validation.
                - `api_name` (string) [maxLen=255] — API name of the field involved in the error, if applicable.
                - `json_path` (string) **REQ** [maxLen=255] — JSON path pointing to the invalid field in the request payload.
                - `expected_data_type` (string) [maxLen=100] — Expected data type for the field, when the error is related to type mismatch.
                - `regex` (string) [maxLen=500] — Validation pattern that the value must satisfy, if applicable.
                - `merge_field` (string) [maxLen=255] — Merge field value that caused the validation error, if applicable.
                - `maximum_length` (integer/int32) — Maximum allowed length for the field, when the provided value is too long.
                - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the field.
                - `dependee` (object) — Details of the field that another field depends on, for DEPENDENT_FIELD_MISSING errors.
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the depended-on field.
                  - `json_path` (string) **REQ** [maxLen=255] — JSON path of the depended-on field in the request payload.
              - `status` (string) **REQ** [enum=['error']] — Indicates that the request failed.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code for invalid data validation failure.
              - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
              - `details` (object) **REQ** — Additional details including the list of accepted values for the field.
                - `api_name` (string) **REQ** [maxLen=255] — API name of the field that received an invalid value.
                - `json_path` (string) **REQ** [maxLen=255] — JSON path pointing to the invalid field in the request payload.
                - `supported_values` (array of string) [maxItems=50] **REQ** — List of accepted values for the field.
                  items: [maxLen=255]
              - `status` (string) **REQ** [enum=['error']] — Indicates that the request failed.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code for mandatory not found validation failure.
              - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
              - `details` (object) **REQ** — Additional details about the field or value that failed validation.
                - `api_name` (string) [maxLen=255] — API name of the field involved in the error, if applicable.
                - `json_path` (string) **REQ** [maxLen=255] — JSON path pointing to the invalid field in the request payload.
                - `expected_data_type` (string) [maxLen=100] — Expected data type for the field, when the error is related to type mismatch.
                - `regex` (string) [maxLen=500] — Validation pattern that the value must satisfy, if applicable.
                - `merge_field` (string) [maxLen=255] — Merge field value that caused the validation error, if applicable.
                - `maximum_length` (integer/int32) — Maximum allowed length for the field, when the provided value is too long.
                - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the field.
                - `dependee` (object) — Details of the field that another field depends on, for DEPENDENT_FIELD_MISSING errors.
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the depended-on field.
                  - `json_path` (string) **REQ** [maxLen=255] — JSON path of the depended-on field in the request payload.
              - `status` (string) **REQ** [enum=['error']] — Indicates that the request failed.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Error code for duplicate data validation failure.
              - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
              - `details` (object) **REQ** — Additional details about the field or value that failed validation.
                - `api_name` (string) [maxLen=255] — API name of the field involved in the error, if applicable.
                - `json_path` (string) **REQ** [maxLen=255] — JSON path pointing to the invalid field in the request payload.
                - `expected_data_type` (string) [maxLen=100] — Expected data type for the field, when the error is related to type mismatch.
                - `regex` (string) [maxLen=500] — Validation pattern that the value must satisfy, if applicable.
                - `merge_field` (string) [maxLen=255] — Merge field value that caused the validation error, if applicable.
                - `maximum_length` (integer/int32) — Maximum allowed length for the field, when the provided value is too long.
                - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the field.
                - `dependee` (object) — Details of the field that another field depends on, for DEPENDENT_FIELD_MISSING errors.
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the depended-on field.
                  - `json_path` (string) **REQ** [maxLen=255] — JSON path of the depended-on field in the request payload.
              - `status` (string) **REQ** [enum=['error']] — Indicates that the request failed.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code for dependent field mismatch validation failure.
              - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
              - `details` (object) **REQ** — Additional details about the field that has a dependency mismatch.
                - `api_name` (string) **REQ** [maxLen=255] — API name of the field that caused the dependency mismatch.
                - `json_path` (string) **REQ** [maxLen=255] — JSON path pointing to the invalid field in the request payload.
                - `dependee` (object) **REQ** — Details of the field whose value caused the mismatch condition.
                  - `api_name` (string) **REQ** [maxLen=255] — API name of the dependee field.
                  - `json_path` (string) **REQ** [maxLen=255] — JSON path of the dependee field in the request payload.
        - `status` (string) **REQ** [enum=['error']] — Indicates that the request failed.
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code for mandatory not found validation failure.
        - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
        - `details` (object) **REQ** — Additional details about the error.
          - `api_name` (string) **REQ** [maxLen=255] — API name of the field involved in the error, if applicable.
          - `json_path` (string) **REQ** [maxLen=255] — JSON path pointing to the invalid field in the request payload.
          - `expected_data_type` (string) [maxLen=100] — Expected data type for the field, when the error is related to type mismatch.
          - `regex` (string) [maxLen=500] — Validation pattern that the value must satisfy, if applicable.
          - `merge_field` (string) [maxLen=255] — Merge field value that caused the validation error, if applicable.
          - `maximum_length` (integer/int32) — Maximum allowed length when the provided value is too long.
          - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Identifier that caused the error, such as a layout, field, or profile ID.
          - `dependee` (object) — Details of the field that another field depends on, for DEPENDENT_FIELD_MISSING errors.
            - `api_name` (string) **REQ** [maxLen=255] — API name of the depended-on field.
            - `json_path` (string) **REQ** [maxLen=255] — JSON path of the depended-on field in the request payload.
        - `status` (string) **REQ** [enum=['error']] — Indicates that the request failed.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code for invalid data validation failure.
        - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
        - `details` (object) **REQ** — Additional details about the error.
          - `api_name` (string) **REQ** [maxLen=255] — API name of the field involved in the error, if applicable.
          - `json_path` (string) **REQ** [maxLen=255] — JSON path pointing to the invalid field in the request payload.
          - `expected_data_type` (string) [maxLen=100] — Expected data type for the field, when the error is related to type mismatch.
          - `regex` (string) [maxLen=500] — Validation pattern that the value must satisfy, if applicable.
          - `merge_field` (string) [maxLen=255] — Merge field value that caused the validation error, if applicable.
          - `maximum_length` (integer/int32) — Maximum allowed length when the provided value is too long.
          - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Identifier that caused the error, such as a layout, field, or profile ID.
          - `dependee` (object) — Details of the field that another field depends on, for DEPENDENT_FIELD_MISSING errors.
            - `api_name` (string) **REQ** [maxLen=255] — API name of the depended-on field.
            - `json_path` (string) **REQ** [maxLen=255] — JSON path of the depended-on field in the request payload.
        - `status` (string) **REQ** [enum=['error']] — Indicates that the request failed.
        - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Error code for dependent field missing validation failure.
        - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
        - `details` (object) **REQ** — Additional details about the error.
          - `api_name` (string) **REQ** [maxLen=255] — API name of the field involved in the error, if applicable.
          - `json_path` (string) **REQ** [maxLen=255] — JSON path pointing to the invalid field in the request payload.
          - `expected_data_type` (string) [maxLen=100] — Expected data type for the field, when the error is related to type mismatch.
          - `regex` (string) [maxLen=500] — Validation pattern that the value must satisfy, if applicable.
          - `merge_field` (string) [maxLen=255] — Merge field value that caused the validation error, if applicable.
          - `maximum_length` (integer/int32) — Maximum allowed length when the provided value is too long.
          - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Identifier that caused the error, such as a layout, field, or profile ID.
          - `dependee` (object) — Details of the field that another field depends on, for DEPENDENT_FIELD_MISSING errors.
            - `api_name` (string) **REQ** [maxLen=255] — API name of the depended-on field.
            - `json_path` (string) **REQ** [maxLen=255] — JSON path of the depended-on field in the request payload.
        - `status` (string) **REQ** [enum=['error']] — Indicates that the request failed.
        - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Error code for duplicate data validation failure.
        - `message` (string) **REQ** [maxLen=255] — Human-readable description of the validation error.
        - `details` (object) **REQ** — Additional details about the error.
          - `api_name` (string) **REQ** [maxLen=255] — API name of the field involved in the error, if applicable.
          - `json_path` (string) **REQ** [maxLen=255] — JSON path pointing to the invalid field in the request payload.
          - `expected_data_type` (string) [maxLen=100] — Expected data type for the field, when the error is related to type mismatch.
          - `regex` (string) [maxLen=500] — Validation pattern that the value must satisfy, if applicable.
          - `merge_field` (string) [maxLen=255] — Merge field value that caused the validation error, if applicable.
          - `maximum_length` (integer/int32) — Maximum allowed length when the provided value is too long.
          - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Identifier that caused the error, such as a layout, field, or profile ID.
          - `dependee` (object) — Details of the field that another field depends on, for DEPENDENT_FIELD_MISSING errors.
            - `api_name` (string) **REQ** [maxLen=255] — API name of the depended-on field.
            - `json_path` (string) **REQ** [maxLen=255] — JSON path of the depended-on field in the request payload.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **401**: Authentication credentials are missing or invalid. [application/json]
    > Represents the error response returned when authentication credentials are missing or invalid.
    oneOf:
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Error code indicating OAuth scope mismatch.
        - `details` (object) **REQ** — Empty details object.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
        - `status` (string) **REQ** [enum=['error']] — Status indicating failure.
        - `code` (string) **REQ** [enum=['INVALID_TOKEN']] — Error code indicating an invalid token.
        - `details` (object) **REQ** — Empty details object.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
        - `status` (string) **REQ** [enum=['error']] — Status indicating failure.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The authenticated user does not have permission to create wizards. [application/json]
    > Error returned when the user lacks permission to perform the operation.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code indicating insufficient permissions.
    - `details` (object) **REQ** — Details about the required permissions.
      - `permissions` (array of string) [maxItems=50] **REQ** — List of permissions required.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `status` (string) **REQ** [enum=['error']] — Status indicating failure.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **404**: Returned when the requested URL does not match any valid endpoint. [application/json]
    > Schema for URL-related errors.
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Indicates that the request failed.
        - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Error code indicating that the requested URL is invalid.
        - `message` (string) **REQ** [maxLen=255] — Human-readable explanation of why the URL was rejected.
        - `details` (object) **REQ** — Additional contextual error information, if any.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.wizards.CREATE

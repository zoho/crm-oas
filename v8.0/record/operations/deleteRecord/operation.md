# DELETE /{module}/{recordId}
**Operation:** `deleteRecord` — Delete a specific record by ID
> To permanently delete a specific record by its unique ID from the specified module in your Zoho CRM organization. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the record IDs.

**Tags:** Records

**Parameters:**
- `module` (path, string, required) [maxLen=25]: Specify the API name of the module. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module ID and API name.
- `recordId` (path, string/int64, required): Specify the unique ID of the record. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the record IDs.

**Responses:**

- **200**: Returns the deletion status for each record successfully deleted. — Schema: `RecordDeleteByIdSuccessResponse` [application/json]
    > Represents the response schema for the record delete by ID success operation.
    schema: `RecordDeleteByIdSuccessResponse`
    - `data` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the data value.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the data value.
      - `message` (string) **REQ** — Represents the data value.
      - `status` (string) **REQ** [enum=['success']] — Represents the data value.
      - `details` (object) **REQ** — Represents the data value.
        - `id` (string/int64) **REQ** — Represents the data value.

- **400**: The request could not be processed because of an invalid module, missing parameters, or invalid record IDs.
**Resolution:** The request must include valid module API name and record IDs. — Schema: `RecordDeleteByIdErrorResponse` [application/json]
    > Represents the error response returned when the operation fails due to a record delete by ID response error.
    oneOf:
      - `RecordDeleteByIdFlatError` — Represents the error response returned when the operation fails due to a record delete by ID flat error.
        oneOf:
          - `RecordDeleteByIdInvalidDataError` — Represents the error response returned when the operation fails due to a record delete by ID invalid data error.
            - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure.
            - `message` (string) **REQ** — Represents the error message describing why the operation failed.
            - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `details` (object `RecordDeleteByIdResourcePathDetails`) **REQ** — Contains the contextual details for the record delete by ID resource path error.
              schema: `RecordDeleteByIdResourcePathDetails`
              - `resource_path_index` (integer/int32) **REQ** — Represents the zero-based index indicating which resource in the path caused the error.
          - `InvalidModuleError` — Represents the error response returned when the operation fails due to a invalid module error.
            - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code identifying the type of failure.
            - `message` (string) **REQ** — Represents the error message describing why the operation failed.
            - `details` (object) **REQ** — Contains additional context about the error.
              - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
            - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
          - `RecordDeleteByIdInvalidRequestMethodError` — Represents the error response returned when the operation fails due to a record delete by ID invalid request method error.
            - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Represents the error code identifying the type of failure.
            - `message` (string) **REQ** — Represents the error message describing why the operation failed.
            - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `details` (object) **REQ** [maxProperties=0] — Contains the contextual details for the record delete empty error.
          - `RecordDeleteByIdAuthorizationFailedError` — Represents the error response returned when the operation fails due to a record delete by ID authorization failed error.
            - `code` (string) **REQ** [enum=['AUTHORIZATION_FAILED']] — Represents the error code identifying the type of failure.
            - `message` (string) **REQ** — Represents the error message describing why the operation failed.
            - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `details` (object) **REQ** [maxProperties=0] — Contains the contextual details for the record delete empty error.
          - `RecordDeleteByIdRequiredParamMissingError` — Represents the error response returned when the operation fails due to a record delete by ID required parameter missing error.
            - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code identifying the type of failure.
            - `message` (string) **REQ** — Represents the error message describing why the operation failed.
            - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `details` (object `RecordDeleteRequiredParamDetails`) **REQ** — Contains the contextual details for the record delete required parameter error.
              schema: `RecordDeleteRequiredParamDetails`
              - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter that caused the error.
      - `RecordDeleteByIdLockedError` — Represents the error response returned when the operation fails due to a record delete by ID locked error.
        - `data` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the data value.
          - `code` (string) **REQ** [enum=['RECORD_LOCKED']] — Represents the data value.
          - `message` (string) **REQ** — Represents the data value.
          - `status` (string) **REQ** [enum=['error']] — Represents the data value.
          - `details` (object) **REQ** — Represents the data value.
            - `action` (string) **REQ** [maxLen=100] — Represents the data value.
            - `id` (string/int64) **REQ** — Represents the data value.
      - `RecordDeleteByIdNotApprovedError` — Represents the error response returned when the operation fails due to a record delete by ID not approved error.
        - `data` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the data value.
          - `code` (string) **REQ** [enum=['NOT_APPROVED']] — Represents the data value.
          - `message` (string) **REQ** — Represents the data value.
          - `status` (string) **REQ** [enum=['error']] — Represents the data value.
          - `details` (object `RecordDeleteByIdDetails`) **REQ** — Details object returned when a delete-by-ID request fails due to an invalid record ID.
            schema: `RecordDeleteByIdDetails`
            - `id` (string/int64) **REQ** — ID of the record that caused the error.

- **401**: Authentication failed because the OAuth token is missing, expired, or does not include the required scope.
**Resolution:** A new access token must be generated with the required scope for this operation. — Schema: `RecordDeleteByIdUnauthorizedResponse` [application/json]
    > Represents the response schema for the record delete by ID unauthorized operation.
    schema: `RecordDeleteByIdUnauthorizedResponse`
    - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

- **403**: Permission denied to delete record in the specified module.
**Resolution:** The CRM administrator must grant the required deletion permission to the user's profile. — Schema: `RecordDeleteByIdNoPermissionResponse` [application/json]
    > Represents the response schema for the record delete by ID no permission operation.
    schema: `RecordDeleteByIdNoPermissionResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.
      - `permissions` (array of string) [minItems=1, maxItems=100] **REQ** — Contains additional context about the error.
        items: [maxLen=255]

- **404**: The request URL does not match any valid API endpoint pattern.
**Resolution:** The API endpoint URL must be verified for correct format and path parameters. — Schema: `RecordDeleteByIdInvalidUrlPatternResponse` [application/json]
    > Represents the response schema for the record delete by ID invalid URL pattern operation.
    schema: `RecordDeleteByIdInvalidUrlPatternResponse`
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

- **500**: An unexpected server error occurred while processing the request.
**Resolution:** The request can be retried after some time. If the error persists, Zoho CRM support must be contacted. — Schema: `RecordDeleteByIdInternalServerErrorResponse` [application/json]
    > Represents the error response returned when the operation fails due to a record delete by ID internal server response error.
    schema: `RecordDeleteByIdInternalServerErrorResponse`
    - `data` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the data value.
      - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Represents the data value.
      - `message` (string) **REQ** — Represents the data value.
      - `status` (string) **REQ** [enum=['error']] — Represents the data value.
      - `details` (object) **REQ** — Represents the data value.

**Scopes:** ZohoCRM.modules.DELETE

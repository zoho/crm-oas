# POST /{module}/actions/assign_territories
**Operation:** `assignTerritoriesToRecords` — Assign territories to multiple records
> To assign one or more territories to multiple records in your Zoho CRM organization.

**Tags:** Territory Assignments

**Parameters:**
- `module` (path, string, required) [maxLen=100]: The API name of the module that contains the records.

**Schemas:**
`TerritoryAssignSuccessResponse`:
  > Represents the response returned when territories are successfully assigned to records.
  - `data` (array of object) [minItems=1, maxItems=10] **REQ** — Represents the list of territory assignment result objects.
    - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the territory assignment. Possible values: **SUCCESS**.
    - `details` (object) **REQ** — Represents additional details about the territory assignment, including the record identifier.
      - `id` (string/int64) **REQ** — Represents the unique identifier of the record to which territories were assigned.
    - `message` (string) **REQ** [enum=['the territories data updated successfully']] — Represents the success message returned for the territory assignment. Possible values: **the territories data updated successfully**.
    - `status` (string) **REQ** [enum=['success']] — Represents the status of the territory assignment operation. Possible values: **success**.

**Request Body** (required) — application/json
> The request body must contain a **data** array. You can include a maximum of 10 objects per request.
  > Specify the records and territories to assign.
  - `data` (array of object) [minItems=1, maxItems=10] **REQ** — Specify the list of records and their associated territories to assign.
    - `id` (string/int64) **REQ** — Specify the unique ID of the record for which to assign the territories.
    - `Territories` (array of object) [minItems=1, maxItems=100] **REQ** — Specify the list of territories to assign to the record. Each object in the array must contain the unique ID of the territory.
      - `id` (string/int64) **REQ** — Specify the unique ID of the territory to assign to the record.

**Responses:**

- **200**: Returns the list of territory assignment results when territories are assigned immediately to the requested records. — Schema: `TerritoryAssignSuccessResponse` [application/json]
    > Represents the response returned when territories are successfully assigned to records.

- **202**: Returns a multi-status scheduled response indicating that the territory assignment jobs were queued. The **code** field is set to **SCHEDULED**, and the **details** object contains the record ID and job ID for each record. [application/json]
    > Represents the response returned when a territory assignment job has been scheduled.
    oneOf:
      - `TerritoryAssignScheduledResponse` — Represents the response returned when a territory assignment job has been scheduled.
        - `data` (array of object) [minItems=1, maxItems=10] **REQ** — Represents the list of record-territory association objects.
          - `code` (string) **REQ** [enum=['SCHEDULED']] — Represents the code for the scheduled territory assignment. Possible values: **SCHEDULED**.
          - `details` (object) **REQ** — Represents additional details about the scheduled territory assignment, including the record and job identifiers.
            - `id` (string/int64) **REQ** — Represents the unique identifier of the record.
            - `job_id` (string/int64) **REQ** — Represents the unique identifier of the scheduled job.
          - `message` (string) **REQ** [enum=['Territory assignment process scheduled successfully']] — Represents the message returned when the territory assignment is scheduled. Possible values: **Territory assignment process scheduled successfully**.
          - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation. Possible values: **success**.
      - `TerritoryAssignSuccessResponse` — Represents the response returned when territories are successfully assigned to records.

- **400**: The territory assignment request contains invalid or missing data.
**Resolution:** All required fields must be present, and the record and territory IDs must be valid and within the configured assignment limits. [application/json]
    > Represents the error response for an invalid or failed territory assignment request.
    oneOf:
      - `TerritoryAssignInvalidDataTerritoryId` — Represents the error response when an invalid territory ID is provided in a territory assignment request.
        - `data` (array of object) [minItems=1, maxItems=10] **REQ** — Represents the list of assignment objects with error details.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request. Possible values: **INVALID_DATA**.
          - `details` (object) **REQ** — Represents additional details about the error, including the field and path associated with the invalid territory ID.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field that contains the invalid territory ID.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field that contains the invalid territory ID.
          - `message` (string) **REQ** [enum=['the id given seems to be invalid', 'The record Id given seems to be invalid']] — Represents the error message returned when an invalid territory ID is provided. Possible values: **the id given seems to be invalid**, **The record Id given seems to be invalid**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryAssignInvalidDataOnURL` — Represents the error response when an invalid value is found in the URL path of a territory assignment request.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request. Possible values: **INVALID_DATA**.
        - `details` (object) **REQ** — Represents additional details about the error, including the resource path index where the issue occurred.
          - `resource_path_index` (integer/int32) **REQ** [min=0] — Represents the index in the resource path where the invalid data was detected.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid', 'The record Id given seems to be invalid']] — Represents the error message returned when an invalid ID is provided in the URL. Possible values: **the id given seems to be invalid**, **The record Id given seems to be invalid**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryAssignMandatoryNotFound` — Represents the error response when a mandatory field is missing from a territory assignment request.
        - `data` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of assignment objects with error details.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for the request. Possible values: **MANDATORY_NOT_FOUND**.
          - `details` (object) **REQ** — Represents additional details about the error, including the missing mandatory field.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the missing mandatory field.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the missing mandatory field.
          - `message` (string) **REQ** [enum=['One of the expected parameter is missing', 'required field not found']] — Represents the error message returned when a mandatory field is absent. Possible values: **One of the expected parameter is missing**, **required field not found**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryAssignDuplicateData` — Represents the error response when duplicate territory entries are found in the assignment request.
        - `data` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of assignment objects with error details.
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code for the request. Possible values: **DUPLICATE_DATA**.
          - `details` (object) **REQ** — Represents additional details about the error, including the field and path that contains duplicate data.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field that contains duplicate data.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field that contains duplicate data.
          - `message` (string) **REQ** [enum=[2 values]] — Represents the error message returned when a duplicate territory is found. Possible values: **Given Territory id already exists for that record**, **Given Territory already exists for that record**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryAssignNotSupported` — Represents the error response when the territory assignment operation is not supported for the specified module.
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the error code for the request. Possible values: **NOT_SUPPORTED**.
        - `details` (object) **REQ** — Represents additional details about the error, including the resource path index where the issue occurred.
          - `resource_path_index` (integer/int32) **REQ** [min=0] — Represents the index in the resource path where the unsupported operation was detected.
        - `message` (string) **REQ** [enum=['the api is not supported for this module']] — Detailed error message to help fix the validation issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryAssignAlreadyUsed` — Represents the error response when a territory is already assigned to the specified record.
        - `data` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of territory assignment objects with error details.
          - `code` (string) **REQ** [enum=['ALREADY_USED']] — Represents the error code for the request. Possible values: **ALREADY_USED**.
          - `details` (object) **REQ** — Represents additional details about the error, including the field and path that caused it.
            - `exists_in` (object) **REQ** — Represents the location where the duplicate value already exists in the request.
              - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path pointing to the existing duplicate value.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field that caused the error.
          - `message` (string) **REQ** [enum=['duplicate territory id found']] — Represents the error message returned when a duplicate territory ID is found. Possible values: **duplicate territory id found**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryAssignRecordLocked` — Represents the error response when the target record is locked and cannot be assigned a territory.
        - `data` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of assignment objects with error details.
          - `code` (string) **REQ** [enum=['RECORD_LOCKED']] — Represents the error code for the request. Possible values: **RECORD_LOCKED**.
          - `details` (object) **REQ** — Represents additional details about the error, including the locked record identifier.
            - `id` (string/int64) **REQ** — Represents the unique identifier of the locked record.
            - `action` (string) **REQ** [enum=['record_locking']] — Represents the action that triggered the record lock error. Possible values: **record_locking**.
          - `message` (string) **REQ** [enum=['Sorry, you cannot perform this operation as the record is locked.']] — Represents the error message returned when a record is locked. Possible values: **Sorry, you cannot perform this operation as the record is locked.**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryAssignInvalidDataMaxLen` — Represents the error response when a territory assignment field value exceeds the maximum allowed length.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request. Possible values: **INVALID_DATA**.
        - `details` (object) **REQ** — Represents additional details about the error, including the maximum allowed length.
          - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field that exceeds the maximum length.
          - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field that exceeds the maximum length.
          - `maximum_length` (integer/int32) **REQ** [min=1] — Represents the maximum number of characters allowed for the field.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message returned when invalid data is submitted. Possible values: **invalid data**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryFeatureNotEnabledError` — Represents the error response when the territory feature is not enabled for the organization.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for the request. Possible values: **FEATURE_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [maxLen=100, enum=[5 values]] — Represents the error message returned when the territory feature is not enabled for the organization. Possible values: **Territory Management is disabled**, **Territory Management is not enabled**, **Territory Management Disabled**, **the territory feature is not enabled for Leads Module**, **Territory Management is not enabled for Leads Module**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `AssignTerritoryAssignErrorDataObject` — Represents the error details object for a limit exceeded error on a territory assignment operation.
        - `data` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the array of record-territory association objects with assignment or removal error details.
          oneOf:
            - `TerritoryLimitExceededError` — Represents the error response when a territory-related limit is exceeded.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code for the request. Possible values: **LIMIT_EXCEEDED**.
              - `details` (object) **REQ** — Represents additional details about the error, including the limit information.
                - `limit` (integer/int32) **REQ** [min=1] — Represents the maximum allowed limit that was exceeded.
              - `message` (string) **REQ** [maxLen=100, enum=['Maximum limit of territories for that record exceeds']] — Represents the error message returned when the territory limit is exceeded. Possible values: **Maximum limit of territories for that record exceeds**.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
            - `TerritoryLimitExceededErrorWithField` — Represents the error response when a territory-related limit is exceeded, with field-level context.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code for the request. Possible values: **LIMIT_EXCEEDED**.
              - `details` (object) **REQ** — Represents additional details about the error, including the field-level context and limit information.
                - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that caused the limit exceeded error.
                - `json_path` (string) **REQ** [maxLen=100] — Represents the JSON path pointing to the field that caused the limit exceeded error.
                - `limit` (integer/int32) **REQ** [min=1] — Represents the maximum allowed limit that was exceeded.
              - `message` (string) **REQ** [maxLen=100, enum=['Maximum limit of territories for that record exceeds']] — Represents the error message returned when the territory limit is exceeded. Possible values: **Maximum limit of territories for that record exceeds**.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `InvalidModule` — Represents the error response when an invalid module is specified in the URL path.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for the request. Possible values: **INVALID_MODULE**.
        - `details` (object) **REQ** — Represents additional details about the error, including the URL path index of the invalid module.
          - `resource_path_index` (integer/int32) **REQ** [min=0] — Represents the zero-based index of the URL path segment that contains the invalid module name.
        - `message` (string) **REQ** [maxLen=100, enum=['the module name given seems to be invalid']] — Represents the error message returned when the specified module is invalid. Possible values: **the module name given seems to be invalid**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

- **401**: Authentication failure due to missing, expired, or invalid OAuth token.
**Resolution:** A new access token must be generated with the required scope for this API. [application/json]
    oneOf:
      - `TerritoryAssignNoPermission` — Represents the error response when the authenticated user does not have permission to assign territories to the specified record.
        - `data` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of assignment objects with error details.
          - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the request. Possible values: **NO_PERMISSION**.
          - `details` (object) **REQ** — Represents additional details about the error.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field related to the permission error.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field related to the permission error.
          - `message` (string) **REQ** [enum=[3 values]] — Represents the error message returned when a user lacks permission for the territory operation. Possible values: **User has no permission to add / remove the Territories**, **User has no permission to update the record**, **User has no permission to assign/remove this territory**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `UnauthorizedError` — Represents the error response when authentication fails for the request.
        - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code for the request. Possible values: **AUTHENTICATION_FAILURE**.
        - `details` (object) **REQ** — Represents additional details about the authentication error.
        - `message` (string) **REQ** [maxLen=100, enum=['Authentication failed']] — Represents the error message returned when authentication fails. Possible values: **Authentication failed**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

- **403**: The territory feature is not enabled or the user lacks permission to update the record.
**Resolution:** The CRM administrator must enable the territory feature in the organization settings and grant the required permissions to the user's profile. [application/json]
    oneOf:
      - `TerritoryNotEnabledError` — Represents the error response when territory management has never been enabled for the organization.
        - `code` (string) **REQ** [enum=['TERRITORY_NOT_ENABLED']] — Represents the error code for the request. Possible values: **TERRITORY_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [maxLen=100, enum=[2 values]] — Represents the error message returned when territory management has never been enabled. Possible values: **the territory feature is not enabled for Leads Module**, **Territory Management is not enabled**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryRecordUpdateNoPermission` — Represents the error response when the user lacks permission to update the record for a territory assign or remove operation.
        - `data` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of error details for the records that could not be processed.
          - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the request. Possible values: **NO_PERMISSION**.
          - `details` (object) **REQ** — Represents additional details about the permission error, including the field API name and JSON path.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field associated with the permission error.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path pointing to the field that caused the permission error.
          - `message` (string) **REQ** [enum=['User has no permission to update the record']] — Represents the error message returned when the user lacks permission to update the record. Possible values: **User has no permission to update the record**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

**Scopes:** ZohoCRM.modules.UPDATE

# POST /{module}/actions/remove_territories
**Operation:** `removeTerritoriesFromRecords` — Remove territories from multiple records
> To remove one or more territories from multiple records in your Zoho CRM organization. Supported modules are Leads, Accounts, Contacts, and Deals. The removal can be processed synchronously or scheduled as a background job, depending on the number of records.

**Tags:** Territory Assignments

**Parameters:**
- `module` (path, string, required) [maxLen=100]: The API name of the module that contains the records.

**Schemas:**
`TerritoryRemoveSuccessResponse`:
  > Represents the response returned when territories are successfully removed from records.
  - `data` (array of object) [minItems=1, maxItems=10] **REQ** — Represents the list of territory removal results.
    - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the territory removal. Possible values: **SUCCESS**.
    - `details` (object) **REQ** — Represents additional details about the territory removal, including the record identifier.
      - `id` (string/int64) **REQ** — Represents the unique identifier of the record from which territories were removed.
    - `message` (string) **REQ** [enum=['the territories data removed successfully']] — Represents the success message returned for the territory removal. Possible values: **the territories data removed successfully**.
    - `status` (string) **REQ** [enum=['success']] — Represents the status of the territory removal operation. Possible values: **success**.

**Request Body** (required) — application/json
> The request body must contain a **data** array. You can include a maximum of 10 objects per request.
  > Specify the records and their associated territories to remove.
  - `data` (array of object) [minItems=1, maxItems=10] **REQ** — Specify the list of records and their associated territories to remove.
    - `id` (string/int64) **REQ** — Specify the unique record ID of the record from which to remove the territories.
    - `Territories` (array of object) [minItems=1, maxItems=100] **REQ** — Specify the list of territories to remove from the record. Refer to the [Get Territories](territories.yaml#$.paths./settings/territories.get) resource for valid values.
      - `id` (string/int64) **REQ** — Specify the unique ID of the territory to remove from the record. Refer to the [Get Territories](territories.yaml#$.paths./settings/territories.get) resource for valid values.

**Responses:**

- **200**: Returns the territory removal results for all records in the request. — Schema: `TerritoryRemoveSuccessResponse` [application/json]
    > Represents the response returned when territories are successfully removed from records.

- **202**: Returns a scheduled response indicating that territory removal jobs were queued successfully. The **code** field is set to **SCHEDULED**, and the **details** object contains the record ID and job ID for each record. [application/json]
    > Represents the scheduled territory removal response, returned when the removal jobs are queued for processing.
    oneOf:
      - `TerritoryRemoveScheduledResponse` — Represents the response returned when a territory removal job has been scheduled.
        - `data` (array of object) [minItems=1, maxItems=10] **REQ** — Represents the list of scheduled territory removal results.
          - `code` (string) **REQ** [enum=['SCHEDULED']] — Represents the result code for the scheduled territory removal. Possible values: **SCHEDULED**.
          - `details` (object) **REQ** — Represents additional details about the scheduled territory removal, including the record and job identifiers.
            - `id` (string/int64) **REQ** — Represents the unique identifier of the record for which territory removal was scheduled.
            - `job_id` (string/int64) **REQ** — Represents the unique identifier of the scheduled territory removal job.
          - `message` (string) **REQ** [enum=['Territory removal process scheduled successfully']] — Represents the success message returned when the territory removal is scheduled. Possible values: **Territory removal process scheduled successfully**.
          - `status` (string) **REQ** [enum=['success']] — Represents the status of the scheduled territory removal operation. Possible values: **success**.
      - `TerritoryRemoveSuccessResponse` — Represents the response returned when territories are successfully removed from records.

- **400**: One or more records in the request contain invalid data or missing required fields.
**Resolution:** Verify that all required fields are present, the record and territory IDs are valid, and the territories are currently assigned to the records. [application/json]
    > Represents the error response for an invalid or failed territory removal request.
    oneOf:
      - `TerritoryAssignInvalidDataTerritoryId` — Represents the error response when an invalid territory ID is provided in a territory assignment request.
        - `data` (array of object) [minItems=1, maxItems=10] **REQ** — Represents the list of assignment objects with error details.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request. Possible values: **INVALID_DATA**.
          - `details` (object) **REQ** — Represents additional details about the error, including the field and path associated with the invalid territory ID.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field that contains the invalid territory ID.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field that contains the invalid territory ID.
          - `message` (string) **REQ** [enum=['the id given seems to be invalid', 'The record Id given seems to be invalid']] — Represents the error message returned when an invalid territory ID is provided. Possible values: **the id given seems to be invalid**, **The record Id given seems to be invalid**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryAssignMandatoryNotFound` — Represents the error response when a mandatory field is missing from a territory assignment request.
        - `data` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of assignment objects with error details.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for the request. Possible values: **MANDATORY_NOT_FOUND**.
          - `details` (object) **REQ** — Represents additional details about the error, including the missing mandatory field.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the missing mandatory field.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the missing mandatory field.
          - `message` (string) **REQ** [enum=['One of the expected parameter is missing', 'required field not found']] — Represents the error message returned when a mandatory field is absent. Possible values: **One of the expected parameter is missing**, **required field not found**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryFeatureNotEnabledError` — Represents the error response when the territory feature is not enabled for the organization.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for the request. Possible values: **FEATURE_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [maxLen=100, enum=[5 values]] — Represents the error message returned when the territory feature is not enabled for the organization. Possible values: **Territory Management is disabled**, **Territory Management is not enabled**, **Territory Management Disabled**, **the territory feature is not enabled for Leads Module**, **Territory Management is not enabled for Leads Module**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryAssignNotSupported` — Represents the error response when the territory assignment operation is not supported for the specified module.
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the error code for the request. Possible values: **NOT_SUPPORTED**.
        - `details` (object) **REQ** — Represents additional details about the error, including the resource path index where the issue occurred.
          - `resource_path_index` (integer/int32) **REQ** [min=0] — Represents the index in the resource path where the unsupported operation was detected.
        - `message` (string) **REQ** [enum=['the api is not supported for this module']] — Detailed error message to help fix the validation issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryRemoveSystemAssignedNotAllowed` — Represents the error response when attempting to remove a system-assigned territory from a record.
        - `data` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of error details for the territory removal operations that are not allowed.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for the request. Possible values: **NOT_ALLOWED**.
          - `details` (object) **REQ** — Represents additional details about the error, including the field API name and JSON path.
            - `api_name` (string) **REQ** [enum=['id']] — Represents the API name of the field that caused the error. Possible values: **id**.
            - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path pointing to the invalid territory ID in the request.
          - `message` (string) **REQ** [enum=[2 values]] — Represents the error message returned when attempting to remove a system-assigned territory. Possible values: **Territory id which you are trying to remove was system assigned**, **The territory id which you are trying to remove was system assigned**.
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
      - `InvalidModule` — Represents the error response when an invalid module is specified in the URL path.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for the request. Possible values: **INVALID_MODULE**.
        - `details` (object) **REQ** — Represents additional details about the error, including the URL path index of the invalid module.
          - `resource_path_index` (integer/int32) **REQ** [min=0] — Represents the zero-based index of the URL path segment that contains the invalid module name.
        - `message` (string) **REQ** [maxLen=100, enum=['the module name given seems to be invalid']] — Represents the error message returned when the specified module is invalid. Possible values: **the module name given seems to be invalid**.
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

- **403**: Territory management is not enabled for the organization, or the user does not have permission to update the record.
**Resolution:** The CRM administrator must enable territory management in the organization settings and grant the required profile permission to the user. [application/json]
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

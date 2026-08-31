# POST /settings/territories/actions/transfer_and_delete
**Operation:** `transferAndDeleteTerritories` — Transfer and delete territories
> To transfer records from one or more territories to a target territory and then delete those territories in your Zoho CRM organization.

**Tags:** Territories

**Request Body** (required) — application/json
> The request body must contain a **territories** array. You can include a maximum of 100 territory objects per request.
  > Specify the territories to transfer records from and delete.
  - `territories` (array of object) [minItems=1, maxItems=100] **REQ** — Specify the list of territories to transfer records from and delete.
    - `id` (string/int64) **REQ** — Specify the unique ID of the territory to delete.
    - `transfer_to_id` (string/int64) — Specify the unique ID of the territory to which the records are transferred before deletion. If not specified, the records are removed without being transferred to another territory.
    - `delete_previous_forecasts` (boolean) — Specify whether to delete previous forecasts associated with the territory. Set to **true** to delete forecasts, or **false** to retain them.

**Responses:**

- **200**: Returns the result of the territory transfer-and-delete operation for each territory in the **territories** array. The **code** field indicates **SUCCESS** for processed territories and **ERROR** for failed ones. — Schema: `TerritoryTransferAndDeleteSuccessResponse` [application/json]
    > Represents the response returned when a territory is successfully transferred and deleted.
    schema: `TerritoryTransferAndDeleteSuccessResponse`
    - `territories` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the list of territory objects transferred and deleted by the request.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the territory transfer and deletion. Possible values: **SUCCESS**.
      - `details` (object) **REQ** — Represents additional details about the transferred and deleted territory, including its unique identifier.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the transferred and deleted territory.
      - `message` (string) **REQ** [maxLen=100, enum=[2 values]] — Represents the success message returned for the territory transfer and deletion. Possible values: **Territory Transferred And Deleted Successfully**, **Given Territory Removed Successfully and its child Territories moved to the another territory**.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the territory transfer and delete operation. Possible values: **success**.

- **400**: The territory transfer-and-delete operation contains invalid or missing data.
**Resolution:** The territory IDs in the request must be valid, the transfer target territory must exist, and all required fields must be present in each territory object. [application/json]
    > Represents the error response for an invalid or failed territory transfer-and-delete operation.
    oneOf:
      - `InvalidData` — Represents the error response when a territory request contains invalid field data.
        - `territories` (array of object) [minItems=1, maxItems=10] **REQ** — Represents the list of territory objects with their error details.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the territory error.
          - `details` (object) **REQ** — Represents additional details about the error.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field that contains invalid data.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field that contains invalid data.
          - `message` (string) **REQ** [enum=[15 values]] — Represents the error message describing the reason for this failure.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `MandatoryNotFoundError` — Represents the error response when a mandatory field is missing from the territory request.
        - `territories` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the list of territory objects with error details.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for the territory error. Possible values: **MANDATORY_NOT_FOUND**.
          - `details` (object) **REQ** — Represents additional details about the error, including the field name and JSON path of the missing mandatory field.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the mandatory field that is missing from the request.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the mandatory field that is missing from the request body.
          - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message returned when a required field is absent. Possible values: **required field not found**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `DependentFieldMissingError` — Represents the error response when a required dependent field is missing from the territory request.
        - `territories` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of territory objects with their error details.
          - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code indicating the type of error for the territory operation.
          - `details` (object) **REQ** — Represents additional details about the error, including the API name and JSON path of the problematic field.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field that caused the error.
            - `dependee` (object) — Represents the dependent field that is required but missing from the request.
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the dependent field.
              - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the dependent field.
          - `message` (string) **REQ** [enum=['This territory has its child. Please Give the transfer_to_id field value']] — Represents the error message describing the reason for this failure.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `NotAllowedDeleteErrorResponse` — Represents the error response when deleting a territory is not permitted.
        - `territories` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of territory objects with error details.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for the territory error. Possible values: **NOT_ALLOWED**.
          - `details` (object) **REQ** — Represents additional details about the error, including the ID of the territory that cannot be deleted.
            - `id` (string/int64) **REQ** — Represents the unique ID of the territory that cannot be deleted.
          - `message` (string) **REQ** [enum=[4 values]] — Represents the error message returned when a territory cannot be deleted. Possible values: **Territory can't be deleted as it's having child**, **Org Territory cannot be deleted**, **Reporting_to id should not be the child of given territory. Chosse another territory as Reporing_to**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryFeatureNotEnabledError` — Represents the error response when the territory feature is not enabled for the organization.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for the request. Possible values: **FEATURE_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [maxLen=100, enum=[5 values]] — Represents the error message returned when the territory feature is not enabled for the organization. Possible values: **Territory Management is disabled**, **Territory Management is not enabled**, **Territory Management Disabled**, **the territory feature is not enabled for Leads Module**, **Territory Management is not enabled for Leads Module**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryReportingToChildError` — Represents the error response when the reporting_to territory ID is a child of the territory being updated, which would create a circular hierarchy.
        - `territories` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of territory objects with child hierarchy error details.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for the request. Possible values: **NOT_ALLOWED**.
          - `details` (object) **REQ** — Represents additional details about the hierarchy error, including the field API name and JSON path.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field associated with the hierarchy validation error.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path pointing to the field that caused the hierarchy error.
          - `message` (string) **REQ** [enum=[3 values]] — Represents the error message returned when the reporting_to territory is a child of the territory being updated. Possible values: **Reporting_to id should not be the child of given territory. Chosse another territory as Reporing_to**, **Org Territory cannot be deleted.**, **Territory can't be deleted as it's having child**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryOrgNoPermission` — Represents the error response when the user does not have update or delete permission for the specified territory.
        - `territories` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of territory objects with organization permission error details.
          - `code` (string) **REQ** [enum=['PERMISSION_DENIED']] — Represents the error code for the request. Possible values: **PERMISSION_DENIED**.
          - `details` (object) **REQ** — Represents additional details about the permission error.
            - `id` (string/int64) **REQ** — Represents the unique identifier related to the permission error context.
          - `message` (string) **REQ** [enum=[2 values]] — Represents the error message returned when the user lacks permission for the organization territory. Possible values: **User does not have update/delete permission for the territory**, **You do not have the necessary permissions to access this territory.**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryParentNoPermissionDetailed` — Represents the error response when the user does not have permission to use the specified territory as a parent, with detailed field-level context.
        - `territories` (array of object) [minItems=1, maxItems=10] **REQ** — Represents the list of territory objects with detailed permission error information.
          - `code` (string) **REQ** [enum=['PERMISSION_DENIED']] — Represents the error code for the request. Possible values: **PERMISSION_DENIED**.
          - `details` (object) **REQ** — Represents additional details about the permission error, including the field API name and JSON path.
            - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that caused the permission error.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path pointing to the field that caused the permission error.
          - `message` (string) **REQ** [enum=[3 values]] — Represents the error message returned when the user lacks permission for the territory. Possible values: **Doesn't have a permission to choose that territory as a Parent Id**, **User does not have update/delete permission for the territory**, **User does not have permission to view/access the Territory**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

- **401**: Authentication failed due to a missing, expired, or invalid OAuth token.
**Resolution:** A valid OAuth token with the required scope must be included in the request. — Schema: `UnauthorizedError` [application/json]
    > Represents the error response when authentication fails for the request.
    schema: `UnauthorizedError`
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code for the request. Possible values: **AUTHENTICATION_FAILURE**.
    - `details` (object) **REQ** — Represents additional details about the authentication error.
    - `message` (string) **REQ** [maxLen=100, enum=['Authentication failed']] — Represents the error message returned when authentication fails. Possible values: **Authentication failed**.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

**Scopes:** ZohoCRM.settings.territories.DELETE

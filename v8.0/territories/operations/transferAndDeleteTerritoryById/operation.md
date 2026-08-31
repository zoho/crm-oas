# POST /settings/territories/{id}/actions/transfer_and_delete
**Operation:** `transferAndDeleteTerritoryById` — Transfer and delete a specific territory by ID
> To transfer child territories to a target parent territory and then delete a specific territory from your Zoho CRM organization. This operation is required for territories that have child territories, as they cannot be directly deleted using the Delete Territories API.

**Tags:** Territories

**Parameters:**
- `id` (path, string/int64, required): The unique ID of the territory to transfer child territories from and then delete.

**Request Body** (required) — application/json
> The request body must contain a **territories** array with one object.
  > Specify the transfer configuration for the territory to delete.
  - `territories` (array of object) [minItems=1, maxItems=1] **REQ** — Specify the transfer details for the territory to delete.
    - `id` (string/int64) — Specify the unique ID of the territory to delete. If omitted, the operation uses the territory ID from the URL path parameter.
    - `transfer_to_id` (string/int64) **REQ** — Specify the unique ID of the parent territory to which child territories are transferred before deleting the specified territory. The target territory must be higher in the hierarchy than the territory to delete.
    - `delete_previous_forecasts` (boolean) — Specify whether to delete previous forecasts associated with the territory.
Possible values:
**true** - Deletes the previous forecasts for the territory.
**false** - Retains the previous forecasts for the territory.

**Responses:**

- **200**: Returns the result of the territory transfer-and-delete operation for the specified territory. — Schema: `TerritoryTransferAndDeleteSuccessResponse` [application/json]
    > Represents the response returned when a territory is successfully transferred and deleted.
    schema: `TerritoryTransferAndDeleteSuccessResponse`
    - `territories` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the list of territory objects transferred and deleted by the request.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the territory transfer and deletion. Possible values: **SUCCESS**.
      - `details` (object) **REQ** — Represents additional details about the transferred and deleted territory, including its unique identifier.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the transferred and deleted territory.
      - `message` (string) **REQ** [maxLen=100, enum=[2 values]] — Represents the success message returned for the territory transfer and deletion. Possible values: **Territory Transferred And Deleted Successfully**, **Given Territory Removed Successfully and its child Territories moved to the another territory**.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the territory transfer and delete operation. Possible values: **success**.

- **400**: The territory transfer-and-DELETE request contains invalid or missing data.
**Resolution:** The request must specify a valid **transfer_to_id** that references an existing territory higher in the hierarchy than the territory to delete. [application/json]
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
      - `DependentFieldMissingErrorInURL` — Represents the error response when a required dependent field is missing from a URL-parameterized territory request.
        - `territories` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of territory objects with error details.
          - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code for the territory operation. Possible values: **DEPENDENT_FIELD_MISSING**.
          - `details` (object) **REQ** — Represents additional details about the error, including the field name, JSON path, and dependent field information.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field whose dependent field is missing.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field in the request body that triggered the dependent field error.
            - `dependee` (object) — Represents the dependent field that is required but absent from the request.
              - `resource_path_index` (integer/int32) **REQ** [min=0] — Represents the zero-based index of the URL path segment that identifies the resource associated with the dependent field error.
          - `message` (string) **REQ** [enum=['This territory has its child. Please Give the transfer_to_id field value']] — Represents the error message returned when a required dependent field is missing.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryInvalidUrlPathErrorSchema` — Represents the error response when an invalid value is provided in the URL path of a territory request.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request. Possible values: **INVALID_DATA**.
        - `details` (object) **REQ** — Represents additional details about the error, including the index of the invalid URL path segment.
          - `resource_path_index` (integer/int32) **REQ** [min=0] — Represents the index of the URL path segment where the invalid value was found.
        - `message` (string) **REQ** [maxLen=100, enum=[4 values]] — Represents the error message returned when an invalid value is provided in the URL path. Possible values: **The given territory id is invalid**, **the id given seems to be invalid**, **The record Id given seems to be invalid**, **Invalid Territory Id**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryFeatureNotEnabledError` — Represents the error response when the territory feature is not enabled for the organization.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for the request. Possible values: **FEATURE_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [maxLen=100, enum=[5 values]] — Represents the error message returned when the territory feature is not enabled for the organization. Possible values: **Territory Management is disabled**, **Territory Management is not enabled**, **Territory Management Disabled**, **the territory feature is not enabled for Leads Module**, **Territory Management is not enabled for Leads Module**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryByIdNoPermission` — Represents the error response when the user does not have permission to access the specified territory by ID.
        - `code` (string) **REQ** [enum=['PERMISSION_DENIED']] — Represents the error code for the request. Possible values: **PERMISSION_DENIED**.
        - `details` (object) **REQ** — Represents additional details about the permission error, including the resource path index.
          - `resource_path_index` (integer/int32) **REQ** [min=0] — Represents the index in the resource path where the permission error occurred.
        - `message` (string) **REQ** [enum=[2 values]] — Represents the error message returned when the user lacks permission to access the territory. Possible values: **User does not have update/delete permission for the territory**, **User does not have permission to view/access the Territory**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

- **401**: The access token does not include the required scope.
**Resolution:** A new access token must be generated with the required scope for this API. — Schema: `UnauthorizedError` [application/json]
    > Represents the error response when authentication fails for the request.
    schema: `UnauthorizedError`
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code for the request. Possible values: **AUTHENTICATION_FAILURE**.
    - `details` (object) **REQ** — Represents additional details about the authentication error.
    - `message` (string) **REQ** [maxLen=100, enum=['Authentication failed']] — Represents the error message returned when authentication fails. Possible values: **Authentication failed**.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

**Scopes:** ZohoCRM.settings.territories.DELETE

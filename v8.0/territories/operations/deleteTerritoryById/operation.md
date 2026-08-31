# DELETE /settings/territories/{id}
**Operation:** `deleteTerritoryById` — Delete a territory by ID
> To delete a specific territory from your Zoho CRM organization using its unique ID.

**Tags:** Territories

**Parameters:**
- `id` (path, string/int64, required): The unique ID of the territory to delete.
- `delete_previous_forecasts` (query, boolean, optional): Delete Previous Forecasts for these territories

**Responses:**

- **200**: Returns the details of the deleted territory, including the result code and territory ID in the **details** object. — Schema: `TerritoryDeleteSuccessResponse` [application/json]
    > Represents the response returned when one or more territories are successfully deleted.
    schema: `TerritoryDeleteSuccessResponse`
    - `territories` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the list of territory objects deleted by the request.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the territory deletion. Possible values: **SUCCESS**.
      - `details` (object) **REQ** — Represents additional details about the deleted territory, including its unique identifier.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the deleted territory.
      - `message` (string) **REQ** [maxLen=100, enum=['Territory Deleted Successfully', 'Given Territory Removed Successfully']] — Represents the success message returned for the territory deletion. Possible values: **Territory Deleted Successfully**, **Given Territory Removed Successfully**.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the territory deletion operation. Possible values: **success**.

- **400**: The request is invalid or the territory cannot be deleted.
**Resolution:** The territory ID in the request URL must be valid, and the territory must be eligible for deletion. [application/json]
    > Represents the error response for an invalid or failed territory deletion request.
    oneOf:
      - `NotAllowedDeleteErrorResponseInURL` — Represents the error response when a territory cannot be deleted because it has child territories.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for the request. Possible values: **NOT_ALLOWED**.
        - `details` (object) **REQ** — Represents additional details about the error, including the URL path index of the invalid resource.
          - `resource_path_index` (integer/int32) **REQ** [min=0] — Represents the zero-based index of the URL path segment that identifies the resource that cannot be deleted.
        - `message` (string) **REQ** [enum=[2 values]] — Represents the error message returned when the territory cannot be deleted. Possible values: **Territory can't be deleted as it's having child**, **Org Territory cannot be deleted**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryInvalidUrlPathErrorSchema` — Represents the error response when an invalid value is provided in the URL path of a territory request.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request. Possible values: **INVALID_DATA**.
        - `details` (object) **REQ** — Represents additional details about the error, including the index of the invalid URL path segment.
          - `resource_path_index` (integer/int32) **REQ** [min=0] — Represents the index of the URL path segment where the invalid value was found.
        - `message` (string) **REQ** [maxLen=100, enum=[4 values]] — Represents the error message returned when an invalid value is provided in the URL path. Possible values: **The given territory id is invalid**, **the id given seems to be invalid**, **The record Id given seems to be invalid**, **Invalid Territory Id**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryByIdNoPermission` — Represents the error response when the user does not have permission to access the specified territory by ID.
        - `code` (string) **REQ** [enum=['PERMISSION_DENIED']] — Represents the error code for the request. Possible values: **PERMISSION_DENIED**.
        - `details` (object) **REQ** — Represents additional details about the permission error, including the resource path index.
          - `resource_path_index` (integer/int32) **REQ** [min=0] — Represents the index in the resource path where the permission error occurred.
        - `message` (string) **REQ** [enum=[2 values]] — Represents the error message returned when the user lacks permission to access the territory. Possible values: **User does not have update/delete permission for the territory**, **User does not have permission to view/access the Territory**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryFeatureNotEnabledError` — Represents the error response when the territory feature is not enabled for the organization.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for the request. Possible values: **FEATURE_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [maxLen=100, enum=[5 values]] — Represents the error message returned when the territory feature is not enabled for the organization. Possible values: **Territory Management is disabled**, **Territory Management is not enabled**, **Territory Management Disabled**, **the territory feature is not enabled for Leads Module**, **Territory Management is not enabled for Leads Module**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

- **401**: Authentication failure due to missing, expired, or invalid OAuth token.
**Resolution:** A new access token must be generated with the required scope for this API. — Schema: `UnauthorizedError` [application/json]
    > Represents the error response when authentication fails for the request.
    schema: `UnauthorizedError`
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code for the request. Possible values: **AUTHENTICATION_FAILURE**.
    - `details` (object) **REQ** — Represents additional details about the authentication error.
    - `message` (string) **REQ** [maxLen=100, enum=['Authentication failed']] — Represents the error message returned when authentication fails. Possible values: **Authentication failed**.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

**Scopes:** ZohoCRM.settings.territories.DELETE

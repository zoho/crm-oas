# DELETE /settings/territories
**Operation:** `deleteTerritories` — Delete territories
> To delete one or more territories from your Zoho CRM organization. The territories to delete are specified using the **ids** query parameter. Deleting a territory is irreversible; child territories must be transferred before a parent territory can be deleted.

**Tags:** Territories

**Parameters:**
- `ids` (query, array, required) [minItems=1, maxItems=100, uniqueItems] {style=form, explode=False}: Specify the unique IDs of the territories you want to delete. Accepts comma-separated territory IDs.
- `delete_previous_forecasts` (query, boolean, optional): Delete Previous Forecasts for these territories

**Responses:**

- **200**: Returns the deletion result for each territory in the request. Each item in the territories array contains a **code** field indicating **SUCCESS** for deleted territories or the relevant error code for failed ones. — Schema: `TerritoryDeleteSuccessResponse` [application/json]
    > Represents the response returned when one or more territories are successfully deleted.
    schema: `TerritoryDeleteSuccessResponse`
    - `territories` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the list of territory objects deleted by the request.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the territory deletion. Possible values: **SUCCESS**.
      - `details` (object) **REQ** — Represents additional details about the deleted territory, including its unique identifier.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the deleted territory.
      - `message` (string) **REQ** [maxLen=100, enum=['Territory Deleted Successfully', 'Given Territory Removed Successfully']] — Represents the success message returned for the territory deletion. Possible values: **Territory Deleted Successfully**, **Given Territory Removed Successfully**.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the territory deletion operation. Possible values: **success**.

- **400**: The territory deletion request contains an invalid or missing query parameter.
**Resolution:** The **ids** query parameter must be present and must contain valid territory IDs. [application/json]
    > Represents the error response for an invalid or failed territory deletion request.

    oneOf:
      - `NotAllowedDeleteErrorResponse` — Represents the error response when deleting a territory is not permitted.
        - `territories` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of territory objects with error details.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for the territory error. Possible values: **NOT_ALLOWED**.
          - `details` (object) **REQ** — Represents additional details about the error, including the ID of the territory that cannot be deleted.
            - `id` (string/int64) **REQ** — Represents the unique ID of the territory that cannot be deleted.
          - `message` (string) **REQ** [enum=[4 values]] — Represents the error message returned when a territory cannot be deleted. Possible values: **Territory can't be deleted as it's having child**, **Org Territory cannot be deleted**, **Reporting_to id should not be the child of given territory. Chosse another territory as Reporing_to**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `RequiredParamMissing` — Represents the error response when a required query or path parameter is missing from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for the request. Possible values: **REQUIRED_PARAM_MISSING**.
        - `details` (object) **REQ** — Represents additional details about the error, including the name of the missing required parameter.
          - `param_name` (string) **REQ** [enum=['ids']] — Represents the name of the required parameter that is missing from the request. Possible values: **ids**.
        - `message` (string) **REQ** [enum=['mandatory param missing']] — Represents the error message returned when a required parameter is missing. Possible values: **mandatory param missing**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `InvalidDataWithId` — Represents the error response when an invalid territory ID is provided in the request.
        - `territories` (array of object) [minItems=1, maxItems=10] **REQ** — Represents the list of territory objects with error details.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the territory error. Possible values: **INVALID_DATA**.
          - `details` (object) **REQ** — Represents additional details about the error, including the invalid territory ID.
            - `id` (string/int64) **REQ** — Represents the territory ID that was provided but found to be invalid.
          - `message` (string) **REQ** [enum=['the id given seems to be invalid', 'Invalid Territory Id']] — Represents the error message returned when an invalid territory ID is provided. Possible values: **the id given seems to be invalid**, **Invalid Territory Id**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryOrgNoPermission` — Represents the error response when the user does not have update or delete permission for the specified territory.
        - `territories` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of territory objects with organization permission error details.
          - `code` (string) **REQ** [enum=['PERMISSION_DENIED']] — Represents the error code for the request. Possible values: **PERMISSION_DENIED**.
          - `details` (object) **REQ** — Represents additional details about the permission error.
            - `id` (string/int64) **REQ** — Represents the unique identifier related to the permission error context.
          - `message` (string) **REQ** [enum=[2 values]] — Represents the error message returned when the user lacks permission for the organization territory. Possible values: **User does not have update/delete permission for the territory**, **You do not have the necessary permissions to access this territory.**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryFeatureNotEnabledError` — Represents the error response when the territory feature is not enabled for the organization.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for the request. Possible values: **FEATURE_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [maxLen=100, enum=[5 values]] — Represents the error message returned when the territory feature is not enabled for the organization. Possible values: **Territory Management is disabled**, **Territory Management is not enabled**, **Territory Management Disabled**, **the territory feature is not enabled for Leads Module**, **Territory Management is not enabled for Leads Module**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `InvalidRequestError` — Represents the error response when the request is invalid, such as when the ids parameter exceeds the maximum allowed limit.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Represents the error code for the request. Possible values: **INVALID_REQUEST**.
        - `details` (object) **REQ** — Represents additional contextual information about the error.
        - `message` (string) **REQ** [enum=[1 values]] — Represents the error message returned when the request cannot be processed. Possible values: **unable to process your request. please verify whether you have entered proper method name, parameter and parameter values.**
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

- **401**: Authentication failure due to a missing, expired, or invalid OAuth token.
**Resolution:** A valid OAuth access token with the **ZohoCRM.settings.territories.DELETE** scope must be included in the request. — Schema: `UnauthorizedError` [application/json]
    > Represents the error response when authentication fails for the request.
    schema: `UnauthorizedError`
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code for the request. Possible values: **AUTHENTICATION_FAILURE**.
    - `details` (object) **REQ** — Represents additional details about the authentication error.
    - `message` (string) **REQ** [maxLen=100, enum=['Authentication failed']] — Represents the error message returned when authentication fails. Possible values: **Authentication failed**.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

**Scopes:** ZohoCRM.settings.territories.DELETE

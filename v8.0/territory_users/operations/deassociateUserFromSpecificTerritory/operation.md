# DELETE /settings/territories/{territory}/users/{user}
**Operation:** `deassociateUserFromSpecificTerritory` — Territory User
> To disassociate a specific user from a territory in your Zoho CRM organization.

**Parameters:**
- `territory` (path, string, required) [maxLen=100]: Territory Id Param in URL
- `user` (path, string, required) [maxLen=100]: User Id Param in URL

**Responses:**

- **200**: Returns the result of the user-territory disassociation. [application/json]
    > Represents the success response body returned after disassociating the user from the territory.
    oneOf:
        - `users` (array of object) [maxItems=100] **REQ** — Represents the list of user-territory disassociation results.
          oneOf:
              type: array of object [maxItems=100]
                - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the status code of the disassociation operation for the user.
                - `details` (object) **REQ** — Represents additional details about the disassociation operation.
                  - `id` (string) **REQ** [maxLen=100] — Represents the unique ID of the user.
                - `message` (string) **REQ** [maxLen=250] — Represents the status message of the disassociation operation.
                - `status` (string) **REQ** [enum=['success']] — Represents the status of the disassociation operation for the user.

- **400**: Returns an error when the request contains invalid user IDs or missing required parameters. **Resolution:** Verify the user ID and ensure all required parameters are provided. [application/json]
    > Represents the error response body returned when the request contains invalid user IDs.
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the invalid request.
        - `details` (object) **REQ** — Represents additional details about the validation error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the invalid resource path in the request.
        - `message` (string) **REQ** [maxLen=250] — Represents the error message describing the validation error.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the validation error response.

- **403**: Returns an error when the territory feature is not yet enabled, is disabled, or access is denied. **Resolution:** Ensure the Territories feature is active and that your OAuth token includes the required scopes. [application/json]
    > Represents the error response body returned when access is denied or the territory feature is not enabled.
    oneOf:
      - `TerritoryErrorPermissionDenied` — Territory Not yet Enabled.
        - `code` (string) **REQ** [enum=[4 values]] — Represents the error code indicating why territory access was denied. Possible values: **PERMISSION_DENIED**, **FEATURE_NOT_ENABLED**, **TERRITORY_DISABLED**, **TERRITORY_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the permission denied error, returned as an empty object.
        - `message` (string) **REQ** [maxLen=100] — Represents the human-readable description of why the territory access was denied.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error**.

- **500**: An internal server error occurred while processing the request. **Resolution:** Retry the request after some time. If the error persists, contact Zoho CRM support. [application/json]
    > Represents the error response body returned when an internal server error occurs.
    oneOf:
      - `TerritoryInternalServerErrorSchema` — Internal server error.
        - `code` (string) **REQ** [enum=['INTERNAL_SERVER_ERROR']] — Represents the error code for an internal server error. Possible values: **INTERNAL_SERVER_ERROR**.
        - `details` (object) **REQ** — Represents additional details about the internal server error, returned as an empty object.
        - `message` (string) **REQ** [maxLen=100] — Represents the human-readable description of the internal server error.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error**.

**Scopes:** ZohoCRM.users.ALL, ZohoCRM.settings.territories.ALL

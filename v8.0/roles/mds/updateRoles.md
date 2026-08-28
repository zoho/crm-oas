# PUT /settings/roles
**Operation:** `updateRoles` — Update a role
> Updates an existing role in your Zoho CRM organization.

**Request Body** (required) — application/json
> The request body must contain a roles array. You can include exactly one object per request (bulk create/update is not supported).
  > Represents the request body for updating a role.
  - `roles` (array of object) [maxItems=1] **REQ** — Specify the array of role objects to update.
    - `id` (string) **REQ** [maxLen=19] — Specify the unique ID of the role to update. Refer to the [Get Roles](roles.yaml#$.paths./settings/roles.get) resource for valid values.
    - `reporting_to` (object) — Specify the updated parent role for this role in the CRM hierarchy. Refer to the [Get Roles](roles.yaml#$.paths./settings/roles.get) resource for valid values.
      - `id` (string) [maxLen=19] — Specify the unique ID of the updated parent role.
    - `forecast_manager` (object) — Specify the forecast manager to assign to this role.
      - `id` (string) [maxLen=19] — Specify the unique ID of the forecast manager to assign to the role.
      - `name` (string) [maxLen=255, nullable] — Specify the display name of the forecast manager to assign to the role.
    - `share_with_peers` (boolean) — Specify whether users assigned to this role can share records with users in peer roles at the same level.
Possible values:
**true** - Users assigned to this role can share records with peer role users.
**false** - Users assigned to this role cannot share records with peer role users.
    - `description` (string) [maxLen=250, nullable] — Specify the updated description for the role.
    - `name` (string) [maxLen=200] — Specify the updated display name for the role.

**Responses:**

- **200**: Returns the update result for each role submitted in the request. [application/json]
    > Represents the successful response for the role update operation.
    - `roles` (array of object) [maxItems=1] **REQ** — Represents the role update result. 
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code of the role update operation. 
Possible values:
**SUCCESS** - The role update succeeded.
      - `details` (object) **REQ** — Represents additional details about the updated role. 
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the updated role. 
      - `message` (string) **REQ** [maxLen=100] — Represents the status message for the role update result. 
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the role update operation. 
Possible values:
**success** - The role update succeeded.

- **400**: The request contains invalid data or a required parameter is missing. **Resolution**: Verify that all roles include a valid **ID** field and that all updated fields conform to the allowed format and constraints. [application/json]
    > Represents the error response for the role update operation.
    oneOf:
        - `roles` (array of object) [maxItems=1] **REQ** — Represents the list of role update results containing both success and error items. 
          - `status` (string) **REQ** [enum=['success', 'error']] — Represents the status of the role update operation for this item. 
          - `code` (string) **REQ** [enum=['SUCCESS', 'INVALID_DATA', 'NOT_ALLOWED', 'MANDATORY_PARAM_MISSING']] — Represents the result code for the role update operation. 
          - `message` (string) **REQ** [maxLen=500] — Represents the status message for the role update result. 
          - `details` (object) — Represents additional details about the role update result.
            - `id` (string) [maxLen=19] — Represents the unique ID of the role associated with the update result.
            - `maximum_length` (integer/int32) — Represents the maximum allowed length for the field that failed validation.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with the update result.
            - `json_path` (string) [maxLen=200] — Represents the JSON path to the field in the request body associated with the update result.
        - `code` (string) **REQ** [enum=['MANDATORY_PARAM_MISSING']] — Represents the error code indicating a required parameter is missing. 
Possible values:
**MANDATORY_PARAM_MISSING** - A required parameter was not included in the request.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the missing parameter issue. 
        - `status` (string) **REQ** [enum=['error']] — Represents the error status of the request. 
Possible values:
**error** - The request failed.
        - `details` (object) — Represents additional details about the missing parameter.
          - `api_name` (string) [maxLen=100] — Represents the API name of the missing required parameter.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code indicating the operation is not allowed. 
Possible values:
**NOT_ALLOWED** - The operation is not permitted.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing why the operation is not allowed. 
        - `status` (string) **REQ** [enum=['error']] — Represents the error status of the request. 
Possible values:
**error** - The request failed.
        - `details` (object) — Represents additional details about why the operation is not allowed.

**Scopes:** ZohoCRM.settings.roles.UPDATE

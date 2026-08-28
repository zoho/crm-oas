# PUT /settings/roles/{role}
**Operation:** `updateRole` — Update a role
> Updates a single role, specified by its ID in the URL.

**Parameters:**
- `role` (path, integer/int64, required): The unique ID of the role.

**Request Body** (required) — application/json
> The request body must contain a roles array with one object.
  > Represents the request body for updating a specific CRM role.
  - `roles` (array of object) [maxItems=1] **REQ** — Specify the array containing the role object to update.
    - `reporting_to` (object) — Specify the updated parent role for this role in the CRM hierarchy. Refer to the [Get Roles](roles.yaml#$.paths./settings/roles.get) resource for valid values.
      - `id` (string) [maxLen=19] — Specify the unique ID of the updated parent role.
    - `share_with_peers` (boolean) — Specify whether users assigned to this role can share records with users in peer roles at the same level.
Possible values:
**true** - Users assigned to this role can share records with peer role users.
**false** - Users assigned to this role cannot share records with peer role users.
    - `description` (string) [maxLen=250, nullable] — Specify the updated description for the role.
    - `name` (string) **REQ** [maxLen=200] — Specify the updated display name for the role.

**Responses:**

- **200**: Returns the update result for the specified role. [application/json]
    > Represents the successful response for the single role update operation.
    - `roles` (array of object) [maxItems=1] **REQ** — Represents the list containing the role update result. 
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code of the role update operation. 
Possible values:
**SUCCESS** - The role update succeeded.
      - `details` (object) **REQ** — Represents additional details about the updated role. 
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the updated role. 
      - `message` (string) **REQ** [maxLen=100] — Represents the status message for the role update result. 
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the role update operation. 
Possible values:
**success** - The role update succeeded.

- **400**: The request contains invalid data or the role ID is invalid. **Resolution**: Verify that the role ID in the request URL is valid and that all updated fields conform to the allowed format and constraints. [application/json]
    > Represents the error response for the single role update operation.
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Represents the error status of the request. 
Possible values:
**error** - The request failed.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating an invalid URL pattern. 
Possible values:
**INVALID_DATA** - The provided data is invalid.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the invalid URL issue. 
        - `details` (object) **REQ** — Represents additional details about the invalid URL error. 
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment that is invalid. 
        - `roles` (array of object) [maxItems=1] **REQ** — Represents the list of role update failure results for validation errors. 
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the role update operation for this item. 
Possible values:
**error** - The role update failed.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the validation failure. 
Possible values:
**INVALID_DATA** - The provided data failed validation.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the validation issue. 
          - `details` (object) **REQ** — Represents additional details identifying the field that failed validation. 
            - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the field that failed validation. 
            - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that failed validation. 
            - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path to the field in the request body that failed validation. 
        - `roles` (array of object) [maxItems=1] **REQ** — Represents the list of role update failure results for invalid data errors. 
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the role update operation for this item. 
Possible values:
**error** - The role update failed.
          - `code` (string) **REQ** [enum=['INVALID_DATA', 'invalid data']] — Represents the error code for the invalid data failure. 
Possible values:
**INVALID_DATA** - The provided data is invalid.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the invalid data issue. 
          - `details` (object) **REQ** — Represents additional details identifying the field that contains invalid data. 
            - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contains the invalid data. 
            - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path to the field in the request body that contains the invalid data. 
        - `roles` (array of object) [maxItems=1] **REQ** — Represents the list of role update failure results for duplicate data errors. 
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the role update operation for this item. 
Possible values:
**error** - The role update failed.
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code for the duplicate data failure. 
Possible values:
**DUPLICATE_DATA** - The role data conflicts with an existing role.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the duplicate data issue. 
          - `details` (object) **REQ** — Represents additional details identifying the field that caused the duplicate data error. 
            - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contains the duplicate value. 
            - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path to the field in the request body that contains the duplicate value. 

**Scopes:** ZohoCRM.settings.roles.UPDATE

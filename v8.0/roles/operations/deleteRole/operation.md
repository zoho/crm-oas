# DELETE /settings/roles/{role}
**Operation:** `deleteRole` — Delete a role
> Deletes a role in your Zoho CRM organization and moves its users to another role.

**Parameters:**
- `role` (path, integer/int64, required): The unique ID of the role.
- `transfer_to_id` (query, integer/int64, required): The unique ID of the role to which subordinate records are transferred before the deletion. Refer to the [Get Roles](roles.yaml#$.paths./settings/roles.get) resource for valid values.

**Responses:**

- **200**: Returns the deletion result for the specified role. [application/json]
    > Represents the successful response for the single role deletion operation.
    - `roles` (array of object) [maxItems=1] **REQ** — Represents the list containing the role deletion result. 
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code of the role deletion operation. 
Possible values:
**SUCCESS** - The role deletion succeeded.
      - `details` (object) **REQ** — Represents additional details about the deleted role. 
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the deleted role. 
      - `message` (string) **REQ** [maxLen=100] — Represents the status message for the role deletion result. 
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the role deletion operation. 
Possible values:
**success** - The role deletion succeeded.

- **400**: The request failed due to an invalid role ID, missing required parameter, or a role that cannot be deleted. **Resolution**: Verify that the role ID is valid, include the transfer_to parameter, and confirm the role is in a deletable state. [application/json]
    > Represents the error response for the single role deletion operation.
    oneOf:
        - `roles` (array of object) [maxItems=1] **REQ** — Represents the list of role deletion failure results for invalid data errors. 
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the role deletion operation for this item. 
Possible values:
**error** - The role deletion failed.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the invalid data failure. 
Possible values:
**INVALID_DATA** - The provided data failed validation.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the validation failure. 
          - `details` (object) **REQ** — Represents additional details identifying the field that failed validation. 
            - `maximum_length` (integer/int32) — Represents the maximum allowed length for the field that failed validation.
            - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that failed validation. 
            - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path to the field in the request body that failed validation. 
        - `status` (string) **REQ** [enum=['error']] — Represents the error status of the request. 
Possible values:
**error** - The request failed.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating that the role cannot be deleted in its current state. 
Possible values:
**INVALID_DATA** - The role is not in a deletable state.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing why the role cannot be deleted. 
        - `details` (object) **REQ** — Represents additional details about why the role cannot be deleted. 
          - `role_status` (string) **REQ** [enum=['subordinate | invalid | same_role']] — Represents the current status of the role that prevents deletion. 
          - `param_name` (string) **REQ** [maxLen=100] — Represents the name of the parameter related to the deletion error. 
        - `status` (string) **REQ** [enum=['error']] — Represents the error status of the request. 
Possible values:
**error** - The request failed.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating that the role ID in the request URL is invalid. 
Possible values:
**INVALID_DATA** - The provided data is invalid.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the invalid URL issue. 
        - `details` (object) **REQ** — Represents additional details about the invalid URL error. 
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment that is invalid. 
        - `status` (string) **REQ** [enum=['error']] — Represents the error status of the request. 
Possible values:
**error** - The request failed.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code indicating that the required transfer_to parameter is missing. 
Possible values:
**REQUIRED_PARAM_MISSING** - A required query parameter is absent from the request.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message indicating the missing required parameter. 
        - `details` (object) **REQ** — Represents additional details about the missing required parameter. 
          - `param_name` (string) **REQ** [maxLen=100] — Represents the name of the missing required parameter. 

**Scopes:** ZohoCRM.settings.roles.DELETE

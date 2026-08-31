# PUT /settings/user_groups/{group}
**Operation:** `updateGroup` — Update a user group
> To update the name, description, and member sources of an existing user group in your Zoho CRM organization.

**Parameters:**
- `group` (path, string, required) [enum=['1234567890']]: Specify the unique ID of the user group to operate on. From API v9 onwards, UUID format is also accepted. Example: `1234567890`.

**Request Body** (required) — application/json
> Provide the updated user group details including the name, optional description, and member sources.
  > Request body schema for updating a user group.
  - `user_groups` (array of object) [maxItems=1] **REQ** — Specify an array containing one user group object to update.
    - `description` (object) — Specify an updated text description for the user group, or null to remove the description.
      oneOf:
          type: string [maxLen=250] — Specify the updated text description for the user group.
          type: null — Use null to remove the existing description.
    - `name` (string) **REQ** [maxLen=250] — The name to be updated for the user group. Accepts alphanumeric characters. Note that the name must be unique for each group.
    - `sources` (array of object) [maxItems=200] **REQ** — Specify the updated array of member sources for the user group. Replaces all existing sources.
      - `type` (string) **REQ** [enum=['territories', 'roles', 'users']] — Specify the type of the member source being updated for the user group.
Possible values:
**territories** - Add a CRM territory as a member source.
**roles** - Add a CRM role as a member source.
**users** - Add individual CRM users as a member source.
      - `source` (object) **REQ** — Specify the identifier of the source to add to the user group.
        - `id` (string) **REQ** [maxLen=19] — Specify the unique ID of the user, role, or territory to add as a member source.
      - `subordinates` (object) — Specify whether to include users in subordinate roles when the source type is **roles** or **territories**.
Possible values:
**true** - Include users in subordinate roles.
**false** - Do not include users in subordinate roles.
        oneOf:
            type: boolean — Specify **true** to include users in subordinate roles, or false to exclude them.
            type: null — Use null to omit the subordinates flag.
      - `sub_territories` (object) — Specify whether to include members from sub-territories when the source type is **territories**.
Possible values:
**true** - Include members from sub-territories.
**false** - Do not include members from sub-territories.
        oneOf:
            type: boolean — Specify true to include members from sub-territories, or false to exclude them.
            type: null — Use null to omit the sub-territories flag.

**Responses:**

- **200**: User group updated successfully. Returns the group ID and a success status. [application/json]
    > Response schema for a successful user group update.
    - `user_groups` (array of object) [maxItems=1] **REQ** — Represents the array containing the result of the user group update operation. 
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the user group update operation. 
Possible values:
**SUCCESS** - The user group update succeeds.
      - `message` (string) **REQ** [maxLen=500] — Represents the result message for the user group update operation. 
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the user group update operation. 
Possible values:
**success** - The user group update succeeds.
      - `details` (object) **REQ** — Represents additional details about the updated user group. 
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the updated user group. 

- **400**: The user group could not be updated. **Resolution:** Verify the group ID is valid and all field values in the request body are correct. [application/json]
    > Response schema for a failed user group update, covering both invalid field values and invalid group ID errors.
    oneOf:
        - `user_groups` (array of object) [maxItems=1] **REQ** — Represents the array containing the error details for the failed update operation. 
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the update operation. 
Possible values:
**error** - The user group update failed.
          - `code` (string) **REQ** [enum=['INVALID_DATA', 'MANDATORY_NOT_FOUND', 'DUPLICATE_DATA']] — Represents the error code for the update failure. 
Possible values:
**INVALID_DATA** - One or more field values in the request body are invalid.
**MANDATORY_NOT_FOUND** - A required field is missing from the request body.
**DUPLICATE_DATA** - A user group with the same name already exists.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the update failure. 
          - `details` (object) **REQ** — Represents additional details about the update error, including the problematic field information. 
            - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that caused the update error. 
            - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path to the field that caused the update error. 
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the invalid group ID failure. 
Possible values:
**INVALID_DATA** - The group ID in the URL does not reference an existing user group.
        - `details` (object) **REQ** — Represents additional details about the invalid group ID error. 
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the path segment where the invalid resource ID was found. 
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the invalid group ID failure. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the update request. 
Possible values:
**error** - The request failed because the group ID is invalid.

- **404**: The request URL does not match any configured endpoint pattern. **Resolution:** Verify the request URL follows the pattern /settings/user_groups/{group}. [application/json]
    > Response schema for an invalid URL pattern error.
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code for the URL pattern failure. 
Possible values:
**INVALID_URL_PATTERN** - The request URL does not match any configured API endpoint.
    - `details` (object) **REQ** — Represents additional details about the URL pattern error. 
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the URL pattern failure. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the request. 
Possible values:
**error** - The request URL pattern was invalid.

**Scopes:** ZohoCRM.settings.user_groups.UPDATE

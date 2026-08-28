# POST /settings/user_groups
**Operation:** `createGroup` — Create a user group
> To create a new user group in your Zoho CRM organization with a specified name, optional description, and member sources (users, roles, or territories).

**Request Body** (required) — application/json
> Provide the user group details including the name, optional description, and member sources (users, roles, or territories).
  > Request body schema for creating a user group.
  - `user_groups` (array of object) [maxItems=10] **REQ** — Specify an array containing up to 10 user group objects to create.
    - `description` (object) — Specify an optional text description for the user group.
      oneOf:
          type: string [maxLen=250] — Specify the text description for the user group.
          type: null — Use null to indicate no description.
    - `name` (string) **REQ** [maxLen=250] — Specify the name of the user group.
    - `sources` (array of object) [maxItems=200] **REQ** — Specify the array of member sources for the user group.
      - `type` (string) **REQ** [enum=['territories', 'roles', 'users']] — Specify the type of the member source being added to the user group.
Possible values:
**territories** - Add a CRM territory as a member source.
**roles** - Add a CRM role as a member source.
**users** - Add individual CRM users as a member source.
      - `source` (object) **REQ** — Specify the identifier of the source to add to the user group.
        - `id` (string) **REQ** [maxLen=19] — Specify the unique ID of the user, role, or territory to add as a member source.
      - `subordinates` (object) — Specify whether to include users in subordinate roles when the source type is **roles**.
Possible values:
**true** - Include users in subordinate roles.
**false** - Do not include users in subordinate roles.
        oneOf:
            type: boolean — Specify true to include users in subordinate roles, or false to exclude them.
            type: null — Use null to omit the subordinates flag.
      - `sub_territories` (object) — Specify whether to include members from sub-territories when the source type is **territories**.
Possible values:
**true** - Include members from sub-territories.
**false** - Do not include members from sub-territories.
        oneOf:
            type: boolean — Specify true to include members from sub-territories, or false to exclude them.
            type: null — Use null to omit the sub-territories flag.

**Responses:**

- **201**: User group created successfully. Returns the new group ID and a success status. [application/json]
    > Response schema for a successful user group creation.
    - `user_groups` (array of object) [maxItems=10] **REQ** — Represents the array containing the result of the user group creation operation. 
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the user group creation operation. 
Possible values:
**SUCCESS** - The user group creation succeeded.
      - `message` (string) **REQ** [maxLen=500] — Represents the result message for the user group creation operation. 
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the user group creation operation. 
Possible values:
**success** - The user group creation succeeded.
      - `details` (object) **REQ** — Represents additional details about the created user group. 
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the newly created user group. 

- **400**: The user group could not be created. **Resolution:** Check that the **name** field is provided and unique, all required fields are present, and source IDs are valid. [application/json]
    > Response schema for a failed user group creation.
    - `user_groups` (array of object) [maxItems=10] **REQ** — Represents the array containing the error details for the failed user group creation operation. 
      - `status` (string) **REQ** [enum=['error']] — Represents the status of the user group creation operation. 
Possible values:
**error** - The user group creation failed.
      - `code` (string) **REQ** [enum=['DUPLICATE_DATA', 'INVALID_DATA', 'MANDATORY_NOT_FOUND']] — Represents the error code for the user group creation failure. 
Possible values:
**DUPLICATE_DATA** - A user group with the same name already exists.
**INVALID_DATA** - One or more field values are invalid.
**MANDATORY_NOT_FOUND** - A required field is missing from the request.
      - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the user group creation failure. 
      - `details` (object) **REQ** — Represents additional details about the creation error, including the API name and JSON path of the problematic field. 
        - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that caused the creation error. 
        - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path to the field that caused the creation error. 

**Scopes:** ZohoCRM.settings.user_groups.CREATE

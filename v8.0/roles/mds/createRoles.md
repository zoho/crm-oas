# POST /settings/roles
**Operation:** `createRoles` — Create a role
> Creates a new role in your Zoho CRM organization.

**Request Body** (required) — application/json
> The request body must contain a roles array. You can include exactly one object per request (bulk create/update is not supported).
  > Represents the request body for creating one or more CRM roles.
  - `roles` (array of object) [maxItems=1] **REQ** — Specify the array of role objects to create. You can include exactly one object per request (bulk create/update is not supported).
    - `reporting_to` (object) **REQ** — Specify the parent role to which this new role reports in the CRM role hierarchy. Refer to the [Get Roles](roles.yaml#$.paths./settings/roles.get) resource for valid values.
      - `id` (string) [maxLen=19] — Specify the unique ID of the parent role in the role hierarchy.
    - `share_with_peers` (boolean) [nullable] — Specify whether users assigned to this role can share records with users in peer roles at the same level.
Possible values:
**true** - Users assigned to this role can share records with peer role users.
**false** - Users assigned to this role cannot share records with peer role users.
    - `description` (string) [maxLen=250, nullable] — Specify the description of the role to provide additional context about its purpose and responsibilities.
    - `name` (string) **REQ** [maxLen=200] — Specify the display name for the role.

**Responses:**

- **201**: Returns the creation result for each role submitted in the request. [application/json]
    > Represents the successful response for the role creation operation.
    - `roles` (array of object) [maxItems=1] **REQ** — Represents the list of role creation results. 
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code of the role creation operation. 
Possible values:
**SUCCESS** - The role creation succeeded.
      - `details` (object) **REQ** — Represents additional details about the created role. 
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the newly created role. 
      - `message` (string) **REQ** [maxLen=100] — Represents the status message for the role creation result. 
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the role creation operation. 
Possible values:
**success** - The role creation succeeded.

- **400**: The request is invalid. **Resolution**: Verify that all required fields are provided and that all field values conform to the allowed format and constraints. [application/json]
    > Represents the error response for the role creation operation.
    oneOf:
        - `roles` (array of object) [maxItems=1] **REQ** — Represents the list of role creation failure results for duplicate data errors. 
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the role creation operation for this item. 
Possible values:
**error** - The role creation failed.
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code for the role creation failure. 
Possible values:
**DUPLICATE_DATA** - The role data conflicts with an existing role.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the duplicate data issue. 
          - `details` (object) **REQ** — Represents additional details identifying the field that caused the duplicate data error. 
            - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contains the duplicate value. 
            - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path to the field in the request body that contains the duplicate value. 
        - `roles` (array of object) [maxItems=1] **REQ** — Represents the list of role creation failure results for invalid data errors. 
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the role creation operation for this item. 
Possible values:
**error** - The role creation failed.
          - `code` (string) **REQ** [enum=['INVALID_DATA', 'invalid data']] — Represents the error code for the role creation failure. 
Possible values:
**INVALID_DATA** - The provided data is invalid.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the invalid data issue. 
          - `details` (object) **REQ** — Represents additional details identifying the field that caused the invalid data error. 
            - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contains the invalid value. 
            - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path to the field in the request body that contains the invalid value. 
        - `roles` (array of object) [maxItems=1] **REQ** — Represents the list of role creation failure results for validation errors. 
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the role creation operation for this item. 
Possible values:
**error** - The role creation failed.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the validation failure. 
Possible values:
**INVALID_DATA** - The provided data failed validation.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the validation issue. 
          - `details` (object) **REQ** — Represents additional details identifying the field that failed validation. 
            - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the field that failed validation. 
            - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that failed validation. 
            - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path to the field in the request body that failed validation. 
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

**Scopes:** ZohoCRM.settings.roles.CREATE

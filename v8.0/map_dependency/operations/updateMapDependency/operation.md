# PUT /settings/layouts/{layoutId}/map_dependency/{dependencyId}
**Operation:** `updateMapDependency` — Update an existing field dependency
> Updates the picklist value mappings for an existing field dependency. Use \"_delete\": null to remove specific mappings.


**Parameters:**
- `module` (query, string, required) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$]: Specify the API name of the module. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get the valid API names. 
- `layoutId` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique identifier of the layout. Use the [Get Layouts API](layouts.yaml#$./settings/layouts.get) to get the ID of the layout.
- `dependencyId` (path, string/int64, required): Specify the unique identifier of the map dependency to retrieve, update, or delete.

**Schemas:**
`FieldReference`:
  > Parent field details
  - `id` (string/int64) **REQ** — Represents the unique identifier of the field. 
  - `api_name` (string) [maxLen=50] — Represents the API name of the field.

**Request Body** (required) — application/json
> The request body contains the data required to perform the operation.
  > Represents the request body for updating a field dependency between picklist fields in a layout.
  - `map_dependency` (array of object) [maxItems=1] **REQ** — Specify the field dependency configuration to update.
    - `parent` (object `FieldReference`) **REQ** — Parent field details
    - `child` (object `FieldReference`) **REQ** — Child field details
    - `pick_list_values` (array of object `PicklistMappingUpdate`) [maxItems=2000] **REQ** — Specify the updated picklist value mappings. Set **_delete** to **null** on a child option entry to remove that specific mapping.
      schema: `PicklistMappingUpdate`
      - `id` (string/int64) **REQ** — Represents the unique identifier of the parent picklist option.
      - `actual_value` (string) [maxLen=120] — Represents the actual stored value of the parent picklist option.
      - `display_value` (string) [maxLen=120] — Represents the display label of the parent picklist option as shown in the CRM interface.
      - `maps` (array of object) [maxItems=2000] **REQ** — Lists the child picklist options associated with this parent picklist value.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the child picklist option.
        - `actual_value` (string) [maxLen=120] — Represents the actual stored value of the child picklist option.
        - `display_value` (string) [maxLen=120] — Represents the display label of the child picklist option as shown in the CRM interface.
        - `_delete` (null) — Indicates that this child option mapping should be deleted. Set to **null** to remove the mapping.
        additionalProperties: any
    - `internal` (boolean) — Specify whether the dependency is system-defined or user-created. Possible values: **true**, **false**.

    - `active` (boolean) — Specify whether the dependency should be active in the layout. Possible values: **true**, **false**.

    - `id` (string/int64) — Specify the unique identifier of the dependency to update.
    - `source` (integer/int32) [enum=[1]] — Specify the source for the dependency. Possible values: **1**. It represents Zoho CRM.

    - `category` (integer/int32) [enum=[0]] — Specify the category of the dependency. Possible values: **0**.


**Responses:**

- **200**: Returns the result of the update operation, including the unique identifier of the updated field dependency. [application/json]
    > Represents the success response returned after the field dependency is successfully updated.
    - `map_dependency` (array of object `SuccessResponse`) [maxItems=1] **REQ** — Contains the result of the update operation. 
      schema: `SuccessResponse`
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation. Possible values: **success**. 

      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the success code for the operation. Possible values: **SUCCESS**. 

      - `message` (string) **REQ** [maxLen=500] — Describes the result of the operation.
      - `details` (object) **REQ** — Contains the result details for the operation. 
        - `id` (string/int64) **REQ** — Represents the unique identifier of the dependency the operation created, updated, or deleted. 

- **400**: The request contains invalid data or violates an update rule.
**Resolution:** Verify that the dependency ID, parent and child field IDs, and all picklist option IDs are valid. Internal dependencies cannot be modified.
 [application/json]
    > Represents the error response when the update request fails. Returns either a root-level error or a field-level error wrapped in the **map_dependency** array.
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
        - `code` (string) **REQ** [enum=[5 values]] — Represents the error code for the root-level request error. 
Possible values: **REQUIRED_PARAM_MISSING**, **INVALID_MODULE**, **NOT_SUPPORTED**, **INVALID_DATA**, **NOT_ALLOWED**. 

        - `message` (string) **REQ** [maxLen=500] — Describes the root-level error that occurred. 
        - `details` (object) **REQ** — Contains additional details about the root-level error. 
        - `map_dependency` (array of object) [maxItems=1] **REQ** — Contains the field-level error details for each dependency in the request. 
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the field-level response. 
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND', 'INVALID_DATA', 'NOT_ALLOWED']] — Represents the error code for the field-level error. 
Possible values: **MANDATORY_NOT_FOUND**, **INVALID_DATA**, **NOT_ALLOWED**. 

          - `message` (string) **REQ** [maxLen=500] — Describes the field-level error that occurred. 
          - `details` (object) **REQ** — Contains field-specific details about the error. 

- **403**: The user does not have the required permission to perform this operation.
**Resolution:** The CRM administrator must grant the user's profile the required permissions listed in the **details.permissions** array.
 [application/json]
    > Represents the error response returned when the user does not have the required permissions to perform this operation.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error**. 

    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the response. Possible values: **NO_PERMISSION**. 

    - `message` (string) **REQ** [maxLen=500] — Describes the reason for the permission error. 
    - `details` (object) **REQ** — Contains additional details about the missing permissions. 
      - `permissions` (object) **REQ** — Lists the permissions required to perform this operation. 
      additionalProperties: any

- **404**: The request URL does not match a valid endpoint pattern.
**Resolution:** Verify the request URL and ensure all path parameter IDs are valid.
 [application/json]
    > Represents the error response returned when the request URL does not match a valid endpoint pattern.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error**.

    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code for this response. 
    - `message` (string) **REQ** [maxLen=500] — Describes the reason the requested resource could not be found. 
    - `details` (object) **REQ** — Contains additional details about the error. 

- **500**: An unexpected error occurred on the server.
**Resolution:** Retry the request. If the error persists, contact Zoho CRM support.
 [application/json]
    > Represents the error response returned when an unexpected server-side error occurs.
    - `code` (string) **REQ** [maxLen=500] — Represents the error code indicating the type of internal server error. 
    - `message` (string) **REQ** [maxLen=500] — Describes the internal server error that occurred. 
    - `details` (object) **REQ** — Contains additional details about the internal server error. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error**. 


**Scopes:** ZohoCRM.settings.map_dependency.update

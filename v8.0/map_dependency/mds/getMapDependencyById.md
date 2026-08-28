# GET /settings/layouts/{layoutId}/map_dependency/{dependencyId}
**Operation:** `getMapDependencyById` — Get a field dependency by ID
> To retrieve the complete details of a specific field dependency from a layout in your Zoho CRM organization, including all picklist value mappings.

**Parameters:**
- `module` (query, string, required) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$]: Specify the API name of the module. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get the valid API names. 
- `layoutId` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique identifier of the layout. Use the [Get Layouts API](layouts.yaml#$./settings/layouts.get) to get the ID of the layout.
- `dependencyId` (path, string/int64, required): Specify the unique identifier of the map dependency to retrieve, update, or delete.

**Schemas:**
`FieldReference`:
  > Parent field details
  - `id` (string/int64) **REQ** — Represents the unique identifier of the field. 
  - `api_name` (string) [maxLen=50] — Represents the API name of the field.

**Responses:**

- **200**: Returns the complete details of the specified field dependency, including all picklist value mappings. [application/json]
    > Represents the response containing the complete details of the specified field dependency, including all picklist value mappings.
    - `map_dependency` (array of object) [maxItems=1] **REQ** — Contains the field dependency details for the specified dependency ID. 
      - `parent` (object `FieldReference`) **REQ** — Parent field details
      - `child` (object `FieldReference`) **REQ** — Details of the child field
      - `pick_list_values` (array of object `PicklistMappingRead`) [maxItems=2000] **REQ** — Contains the complete mapping of parent picklist options to their corresponding child picklist options. 
        schema: `PicklistMappingRead`
        - `id` (string/int64) **REQ** — Represents the unique identifier of the parent picklist option. 
        - `actual_value` (string) **REQ** [maxLen=120] — Represents the actual stored value of the parent picklist option. 
        - `display_value` (string) **REQ** [maxLen=120] — Represents the display label of the parent picklist option as shown in the CRM interface. 
        - `maps` (array of object `PicklistOption`) [maxItems=2000] **REQ** — Lists the child picklist options associated with this parent picklist value. 
          schema: `PicklistOption`
          - `id` (string/int64) **REQ** — Represents the unique identifier of the picklist option. 
          - `actual_value` (string) **REQ** [maxLen=120] — Represents the actual stored value of the picklist option.
          - `display_value` (string) **REQ** [maxLen=120] — Represents the display label of the picklist option as shown in the CRM interface. 
      - `internal` (boolean) **REQ** [enum=[True, False]] — Indicates whether the dependency was defined by the system or created by the user. Possible values: **true**, **false**. 

      - `active` (boolean) **REQ** [enum=[True, False]] — Indicates whether the dependency is active in the layout. Possible values: **true**, **false**. 

      - `id` (string/int64) **REQ** — Represents the unique identifier of the field dependency. 
      - `source` (integer/int32) **REQ** [enum=[1]] — Represents the source of the dependency. Possible values: **1**. It indicates Zoho CRM as the source. 

      - `category` (integer/int32) **REQ** [enum=[0]] — Represents the category of the dependency. Possible values: **0**. **0** represents the default category. 


- **204**: The specified field dependency was not found in the layout.
**Resolution**: Use the [Get Layouts API](layouts.yaml#$.paths./settings/layouts.get) to provide a valid ID in the request.


- **400**: The request contains invalid parameters or data.
**Resolution:** Verify the module API name and ensure all required parameters are included. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get the details of a module.
 [application/json]
    > Represents the error response returned when the request contains invalid parameters or data.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
    - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING', 'INVALID_MODULE', 'NOT_SUPPORTED']] — Represents the error code for the request error. Possible values: **REQUIRED_PARAM_MISSING**, **INVALID_MODULE**, **NOT_SUPPORTED**. 

    - `message` (string) **REQ** [maxLen=500] — Describes the error that occurred. 
    - `details` (object) **REQ** — Contains additional details about the error. 

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


**Scopes:** ZohoCRM.settings.map_dependency.read

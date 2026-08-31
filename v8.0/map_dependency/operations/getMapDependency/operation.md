# GET /settings/layouts/{layoutId}/map_dependency
**Operation:** `getMapDependency` — Get field dependencies for a layout
> To retrieve the list of field dependencies configured for a specific layout in your Zoho CRM organization.

**Parameters:**
- `layoutId` (path, string/int64, required) [pattern=^[0-9]+$]: Specify the unique identifier of the layout. Use the [Get Layouts API](layouts.yaml#$./settings/layouts.get) to get the ID of the layout.
- `module` (query, string, required) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$]: Specify the API name of the module. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get the valid API names. 
- `page` (query, integer/int32, optional): Specify the page number to retrieve in the paginated response.
- `per_page` (query, integer/int32, optional) [max=200]: Specify the number of records to include on each page of the response.
- `filters` (query, string, optional) [maxLen=100]: Specify the filter criteria for field dependencies in JSON format. Supported filters allow narrowing results by specific field attributes using **comparator** and **field** attributes. Supported comparator values: **equal**, **in**.


**Schemas:**
`FieldReference`:
  > Details of the parent field.
  - `id` (string/int64) **REQ** — Represents the unique identifier of the field. 
  - `api_name` (string) [maxLen=50] — Represents the API name of the field.

**Responses:**

- **200**: Returns the list of field dependencies configured for the specified layout. [application/json]
    > Represents the successful response containing the list of field dependencies and pagination details for the specified layout.
    - `map_dependency` (array of object) [maxItems=200] **REQ** — Contains the list of field dependency objects for the specified layout. 
      - `parent` (object `FieldReference`) **REQ** — Details of the parent field.
      - `child` (object `FieldReference`) **REQ** — Details of the child field.
      - `sub_module` (object) **REQ** — The API name and ID of the field that is mapped as the parent in the subform of the module. For non-subforms, this value is **null**. This key is present only when you fetch all the mapped dependencies in a module.
        oneOf:
            type: null — Indicates that the dependency applies to the main module fields and is not associated with any subform.
            - `id` (string/int64) **REQ** — Represents the unique identifier of the subform module. Make a [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get the details of the subform module. 
            - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the subform module. 
      - `internal` (boolean) **REQ** [enum=[True, False]] — Indicates whether the dependency was defined by the system or created by the user. Possible values: **true**, **false**. 

      - `active` (boolean) **REQ** [enum=[True, False]] — Indicates whether the dependency is active in the layout. Possible values: **true**, **false**. 

      - `id` (string/int64) **REQ** — Represents the unique identifier of the field dependency. 
      - `source` (integer/int32) **REQ** [enum=[1]] — Represents the source of the dependency. Possible values: **1**. It indicates Zoho CRM as the source. 

      - `category` (integer/int32) **REQ** [enum=[0]] — Represents the category of the dependency. Possible values: **0**. **0** represents the default category. 

    - `info` (object) **REQ** — Contains the pagination details for the response. 
      - `page` (integer/int32) **REQ** — Represents the current page number in the paginated response.
      - `per_page` (integer/int32) **REQ** — Represents the maximum number of records included on each page. 
      - `count` (integer/int32) **REQ** — Represents the number of records returned on the current page. 
      - `more_records` (boolean) **REQ** — Indicates whether additional pages of records are available. Possible values: **true**, **false**. 


- **204**: No field dependencies are configured for the specified layout.

- **400**: The request contains invalid parameters or data.
**Resolution:** Verify the module API name and layout ID in the request, and ensure all required parameters are included and all filter criteria are valid JSON.
 [application/json]
    > Represents the error response returned when the request contains invalid parameters or data.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. 
    - `code` (string) **REQ** [enum=[6 values]] — Represents the error code for the request error. Possible values: **REQUIRED_PARAM_MISSING**, **INVALID_MODULE**, **NOT_SUPPORTED**, **INVALID_DATA**, **DEPENDENT_FIELD_MISSING**, **MANDATORY_NOT_FOUND**. 

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

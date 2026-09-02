# GET /settings/global_picklists/{id}/actions/associations
**Operation:** `getGlobalPickListFieldAssociations` — Get Field Associations
> Retrieves associations of picklist values with modules, fields, and layouts for a given global picklist ID.

**Tags:** Global Picklists

**Parameters:**
- `id` (path, string/int64, required): Numeric id of the global picklist. Use the [Get All Global Picklists](global_picklists.yaml#$.paths./settings/global_picklists.get) resource to retrieve global picklist IDs.

- `page` (query, integer/int32, optional) [min=1, default=1]: Page number (positive integer). Default: 1.
- `per_page` (query, integer/int64, optional) [min=1, max=200, default=200]: Number of records per page. Default and maximum: 200.
- `include_inner_details` (query, array, optional) [maxItems=3] {style=form, explode=False}: Comma-separated list of nested details to include (e.g., `module.plural_label,module.module_name,layouts.status`). Allowed values: module.plural_label, module.module_name, layouts.status.

**Responses:**

- **200**: Successful response containing picklist associations. [application/json]
    > Response object containing associations of global picklist fields and modules.
    - `associations` (array of object) [maxItems=1000] **REQ** — List of associations between global picklist and fields/modules/layouts.
      - `field` (object) **REQ** — Field details associated with the global picklist.
        - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
        - `id` (string/int64) **REQ** — Id of the resource.
        - `field_label` (string) [maxLen=100] — Name of the field label.
      - `module` (object) **REQ** — Module details associated with the field.
        - `plural_label` (string) [maxLen=25] — Plural label of the module.
        - `api_name` (string) **REQ** [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
        - `module_name` (string) [maxLen=100] — Name of the module
        - `id` (string/int64) **REQ** — Id of the resource.
      - `layouts` (array of object) [maxItems=100] **REQ** — List of layouts associated with the field.
        - `name` (string) **REQ** [maxLen=50] — Name of the layout
        - `id` (string/int64) **REQ** — Id of the resource.
        - `status` (string) [maxLen=20] — Layout status.
    - `info` (object) **REQ** — Pagination and record info for associations response.
      - `per_page` (integer/int32) **REQ** — Number of records per page.
      - `count` (integer/int32) **REQ** — Number of records returned.
      - `page` (integer/int32) **REQ** — Current page number.
      - `more_records` (boolean) **REQ** — Whether more records are available.

- **204**: if there is no picklist field associated with the global picklist.

- **400**: Bad Request - Invalid data or not allowed action. [application/json]
    > Error response object containing code, message, details, and status.
    - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Error code indicating the failure reason. Possible values: INVALID_DATA, NOT_ALLOWED.
    - `details` (object) — Additional details about the error.
      - `resource_path_index` (integer/int32) **REQ** [const=2] — This value is always 2.
    - `message` (string) **REQ** [maxLen=250] — Describes the reason for the failure. Examples: 'the id given seems to be invalid' or 'global picklist deletion in progress.'
    - `status` (string) **REQ** [maxLen=100] — Status of the error response.

- **403**: Forbidden [application/json]
    > Error response object containing code, message, details, and status.
    - `code` (string) **REQ** [maxLen=50] — Error code indicating the type of error.
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `details` (object) **REQ** — Additional details about the error.
      - `permissions` (array of string) [maxItems=1] — List of permissions required to access the resource.
        items: [enum=['Crm_Implied_Customize_Zoho_CRM']]
    - `status` (string) **REQ** [maxLen=100, enum=['error']] — Status of the error response.

- **500**: Internal Server Error [application/json]
    > Internal server error response object containing code, message, details, and status.
    - `code` (string) **REQ** [maxLen=50] — Error code indicating the type of error.
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `details` (object) **REQ** — Additional details about the error.
    - `status` (string) **REQ** [enum=['error']] — Status of the error response.

**Scopes:** ZohoCRM.settings.global_picklist.READ

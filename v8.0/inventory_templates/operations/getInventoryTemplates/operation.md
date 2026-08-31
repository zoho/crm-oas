# GET /settings/inventory_templates
**Operation:** `getInventoryTemplates` — Inventory templates
> To retrieve a paginated list of inventory templates configured in your Zoho CRM organization, with optional filtering by module, category, and field criteria, and sorting by name or usage and modification timestamps.

**Parameters:**
- `module` (query, string, optional) [maxLen=128]: Specifies the API name of the CRM module used to filter the returned inventory templates.
- `per_page` (query, integer/int32, optional) [max=200, default=200]: Specify the number of inventory templates to return per page.
- `page` (query, integer/int32, optional) [min=1, default=1]: Specify the page number to retrieve in the paginated results.

**Schemas:**
`ErrorItemBase`:
  > Base structure for all error items returned in inventory templates error responses, containing the code, message, status, and details fields.
  - `code` (string) **REQ** [maxLen=128] — Represents the error code for the failed operation. 
  - `message` (string) **REQ** [maxLen=1024] — Represents the error message describing the issue. 
  - `status` (string) **REQ** [enum=['error', 'warning', 'info']] — Represents the severity level of the result. 
Possible values:
**error** - The operation failed due to an error.
**warning** - The operation completed with warnings.
**info** - The operation returned an informational status.
  - `details` (object) **REQ** — Represents the additional details about the error, such as the parameter name or field that caused it. 
`UserRef`:
  > User who created the template
  - `name` (string) **REQ** [maxLen=255] — Represents the display name of the CRM user. 
  - `id` (string) **REQ** [maxLen=50] — Represents the unique ID of the CRM user. 

**Responses:**

- **200**: Returns the paginated list of inventory templates matching the specified criteria, along with pagination metadata. — Schema: `InventoryTemplateListResponse` [application/json]
    > Successful response containing inventory_templates array and pagination info.
    schema: `InventoryTemplateListResponse`
    - `inventory_templates` (array of object `InventoryTemplateListItem`) [maxItems=2000] **REQ** — Represents the list of inventory templates returned for the current page. 
      schema: `InventoryTemplateListItem`
      - `created_time` (string/date-time) **REQ** — Represents the creation timestamp of the inventory template. 
      - `modified_time` (string/date-time) **REQ** — Represents the date and time at which the inventory template was last modified. 
      - `last_usage_time` (object) **REQ** — Represents the date and time at which the inventory template was last used, or null if the template has never been used. 
        oneOf:
            type: string/date-time — Represents the date and time at which the template was last used.
            type: null — Indicates that the template has never been used.
      - `category` (string) **REQ** [enum=['normal', 'draft']] — Represents the category of the inventory template. 
Possible values:
**normal** - A regular, published inventory template.
**draft** - A template that is saved as a draft and not yet published.
      - `folder` (object `FolderRef`) **REQ** — Folder containing this template
        schema: `FolderRef`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the folder. 
        - `id` (string) **REQ** [maxLen=50] — Represents the unique ID of the folder. 
      - `module` (object `ModuleRef`) **REQ** — Module this template belongs to
        schema: `ModuleRef`
        - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the CRM module associated with the inventory template. 
        - `id` (string) **REQ** [maxLen=50] — Represents the unique ID of the CRM module associated with the inventory template. 
      - `created_by` (object `UserRef`) **REQ** — User who created the template
      - `modified_by` (object `UserRef`) **REQ** — User who last modified the template
      - `name` (string) **REQ** [maxLen=75, pattern=^[A-Za-z0-9]{5}$] — Represents the name of the inventory template. 
      - `id` (string) **REQ** [maxLen=50] — Represents the unique ID of the inventory template. 
      - `editor_mode` (string) **REQ** [enum=['plain_text', 'rich_text', 'gallery']] — Represents the editor mode used to create the inventory template. 
Possible values:
**plain_text** - The template was built from scratch using plain text.
**rich_text** - The template is a pre-designed custom template.
**gallery** - The template was chosen from the template gallery and customized.
      - `favorite` (boolean) **REQ** — Indicates whether the inventory template is marked as a favorite. 
Possible values:
**true** - The template is marked as a favorite.
**false** - The template is not marked as a favorite.
    - `info` (object `InfoBlock`) **REQ** — Pagination information
      schema: `InfoBlock`
      - `per_page` (integer/int32) **REQ** — Represents the number of inventory template records returned per page. 
      - `page` (integer/int32) **REQ** — Represents the current page number in the paginated response. 
      - `count` (integer/int32) **REQ** — Represents the number of inventory template records returned in the current page. 
      - `more_records` (boolean) **REQ** — Indicates whether additional pages of inventory template records are available beyond the current page. 
Possible values:
**true** - More records are available on subsequent pages.
**false** - The current page is the last page.

- **204**: No inventory templates match the specified filter criteria. The response body is empty.

- **400**: The request contains invalid parameters or an invalid module name.
**Resolution:** The module API name and all query parameter values must be valid before retrying the request. — Schema: `GetInventoryTemplates400Error` [application/json]
    > Error response schema for inventory templates operations.
    schema: `GetInventoryTemplates400Error`

**Scopes:** ZohoCRM.templates.inventory.READ

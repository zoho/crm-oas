# GET /settings/inventory_templates/{templateId}
**Operation:** `getInventoryTemplateById` — Inventory Template
> Retrieves a single inventory template by its ID with complete details including content and all metadata.

**Parameters:**
- `templateId` (path, string, required) [maxLen=64]: Inventory template ID.

**Schemas:**
`UserRef`:
  > User who created the template
  - `name` (string) **REQ** [maxLen=255] — Represents the display name of the CRM user. 
  - `id` (string) **REQ** [maxLen=50] — Represents the unique ID of the CRM user. 

**Responses:**

- **200**: OK - single inventory template with all details — Schema: `InventoryTemplateDetailResponse` [application/json]
    > Successful response for single inventory template retrieval
    schema: `InventoryTemplateDetailResponse`
    - `inventory_templates` (array of object `InventoryTemplateDetail`) [maxItems=1] **REQ** — Represents an array containing the details of a single inventory template. 
      schema: `InventoryTemplateDetail`
      - `id` (string) **REQ** [maxLen=50] — Unique template identifier
      - `name` (string) **REQ** [maxLen=75] — Represents the name of the inventory template. 
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
      - `editor_mode` (string) **REQ** [enum=['plain_text', 'rich_text', 'gallery']] — Represents the editor mode used to create the inventory template. 
Possible values:
**plain_text** - The template was built from scratch using plain text.
**rich_text** - The template is a pre-designed custom template.
**gallery** - The template was chosen from the template gallery and customized.
      - `favorite` (boolean) **REQ** — Indicates whether the inventory template is marked as a favorite. 
Possible values:
**true** - The template is marked as a favorite.
**false** - The template is not marked as a favorite.
      - `content` (string) **REQ** [maxLen=300000] — Represents the full HTML content of the inventory template. 
    additionalProperties: any

- **204**: No Content - template not found

**Scopes:** ZohoCRM.templates.inventory.READ

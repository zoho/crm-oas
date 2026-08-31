# GET /settings/global_picklists/{id}/actions/replaced_values
**Operation:** `getReplacedValues` — Get Replaced Picklist Values
> Retrieves picklist values that are currently being replaced through a replace scheduler for the given global picklist ID.

**Tags:** Global Picklists

**Parameters:**
- `id` (path, string/int64, required): Numeric id of the global picklist. Use the [Get All Global Picklists](global_picklists.yaml#$.paths./settings/global_picklists.get) resource to retrieve global picklist IDs.


**Responses:**

- **200**: OK - Replace scheduler in progress. Returns values which are currently being replaced. [application/json]
    > Response object containing picklist values that are currently being replaced.
    - `replaced_values` (array of object) [maxItems=500] **REQ** — Array of picklist values that are currently being replaced.
      - `display_value` (string) **REQ** [maxLen=120] — The picklist display value(translated value if translation enabled).
      - `reference_value` (string) **REQ** [maxLen=120] — Reference value of the picklist field.

- **204**: No Content - No replace scheduler is currently in progress for the given picklist.

- **400**: Bad Request - Invalid data or not allowed action. [application/json]
    > Error response object containing code, message, details, and status.
    - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Error code indicating the failure reason. Possible values: INVALID_DATA, NOT_ALLOWED.
    - `details` (object) — Details about the error, including the resource path index.
      - `resource_path_index` (integer/int32) **REQ** [enum=[2]] — This value is always 2.
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

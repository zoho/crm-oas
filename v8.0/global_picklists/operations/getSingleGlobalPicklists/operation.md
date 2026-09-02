# GET /settings/global_picklists/{id}
**Operation:** `getSingleGlobalPicklists` — Get a Single Global Picklist by ID
> Fetches the global picklist for given id along with their pick_list_values. used_in_modules, and associated_fields_count can be included in the response based on the 'include' query parameter. Use the `fields` query parameter to filter the response by key, so that only the requested keys along with `id` are returned. A 204 is returned when no global picklists exist.

**Parameters:**
- `id` (path, string/int64, required): Numeric id of the global picklist. Use the [Get All Global Picklists](global_picklists.yaml#$.paths./settings/global_picklists.get) resource to retrieve global picklist IDs.

- `include` (query, array, optional) [maxItems=3] {style=form, explode=False}: Comma-separated list of related resources to include. Allowed values: "used_in_modules", "pick_list_values", "associated_fields_count". Use CSV encoding (style=form, explode=false) for multiple values, e.g. include=used_in_modules,pick_list_values.
- `include_inner_details` (query, string, optional) [enum=['used_in_modules.plural_label']]: Optional detailed expansion keys. Currently only allowed when `used_in_modules` is present in `include`. Allowed value: used_in_modules.plural_label.
- `fields` (query, array, optional) [minItems=1, maxItems=20] {style=form, explode=False}: Comma-separated list of the api_names of the global picklist keys to be returned in the response, which lets you filter the response by key. Only the requested keys along with `id` are returned. Keys need not be unique — a key repeated in the list is processed once and the duplicates are ignored. Use CSV encoding (style=form, explode=false) for multiple values, e.g. fields=display_label,api_name,customizable.

**Responses:**

- **200**: Fetches the global picklist for given id along with their pick_list_values. used_in_modules, and associated_fields_count can be included in the response based on the 'include' query parameter. When the 'fields' query parameter is given, only the requested keys along with 'id' are returned. A 204 is returned when no global picklists exist. [application/json]
    > Response object containing an array of global picklists.
    - `global_picklists` (array of object) [maxItems=1] **REQ** — Array of global picklists with their properties.
      - `display_label` (string) [maxLen=50] — Display label of the global picklist.
      - `api_name` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
      - `source` (string) [maxLen=50, enum=['crm', 'platform_plugin', 'marketplace_plugin']] — Source of the global picklist.
      - `created_time` (string/date-time) [nullable] — Creation timestamp of the global picklist.
      - `modified_time` (string/date-time) [nullable] — Last modification timestamp of the global picklist.
      - `id` (string/int64) **REQ** — Id of the resource.
      - `actual_label` (string) [maxLen=50] — Actual label of the global picklist.
      - `description` (string) [maxLen=1000, nullable] — Description of the global picklist.
      - `associated_fields_count` (integer/int32) — Number of fields associated with this global picklist.
      - `modified_by` (object) — User who last modified the global picklist.
        oneOf:
            - `name` (string) [maxLen=255] — Name of the user.
            - `id` (string/int64) — Id of the resource.
            type: null — Null if no user information is available.
      - `used_in_modules` (array of object) [maxItems=100] — Array of modules using this global picklist.
        - `plural_label` (string) [maxLen=25] — Plural label of the module.
        - `api_name` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the resource. It will start with alphabets and can contain alphanumeric characters and underscores.
        - `id` (string/int64) — Id of the resource.
      - `created_by` (object) — User who created the global picklist.
        oneOf:
            - `name` (string) [maxLen=255] — Name of the user.
            - `id` (string/int64) — Id of the resource.
            type: null — Null if no user information is available.
      - `presence` (boolean) — Indicates if the global picklist is present. false if global picklist is in delete scheduler.
      - `customizable` (boolean) — Indicates if the global picklist is customizable.
      - `pick_list_values_sorted_lexically` (boolean) — Indicates if picklist values are sorted lexically.
      - `pick_list_values` (array of object) [maxItems=5000] — Array of picklist values.
        - `type` (string) **REQ** [enum=['unused', 'used']] — Type of the picklist value (used or unused).
        - `id` (string/int64) **REQ** — Id of the resource.
        - `sequence_number` (integer/int32) **REQ** — Sequence number of the picklist value.
        - `display_value` (string) **REQ** [maxLen=120] — The picklist display value(translated value if translation enabled).
        - `reference_value` (string) **REQ** [maxLen=120] — Reference value of the picklist field.
        - `actual_value` (string) [maxLen=120] — Actual value of the picklist field.

- **204**: No global picklists available. (No content)

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

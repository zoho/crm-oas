# GET /settings/duplicate_check_preference
**Operation:** `getDuplicateCheckPreference` — Get Duplicate Check Preference
> To retrieve the duplicate check preference configured for the Leads module in your Zoho CRM organization.

**Parameters:**
- `module` (query, string, required) [enum=['Leads']]: Represents the module whose Duplicate Check Preference details you want to retrieve.  Supported module: Leads.

**Responses:**

- **200**: Returns the duplicate check preference configured for the specified module. — Schema: `GetDuplicateCheckPreference` [application/json]
    > Schema for getting duplicate check preference.
    schema: `GetDuplicateCheckPreference`
    - `duplicate_check_preference` (object) **REQ** — Duplicate check preference details.
      - `type` (string) **REQ** [enum=['converted_records', 'mapped_module_records']] — Type of duplicate check preference.
      - `type_configurations` (array of object) [maxItems=1, nullable] **REQ** — Configurations for the duplicate check preference type
        - `field_mappings` (array of object) **REQ** — Field mappings for duplicate check.
          - `current_field` (object) **REQ** — Current field details.
            - `id` (string) **REQ** [maxLen=50] — Represents the unique identifier of the field. Use the [Get Fields Metadata API](fields.json#$.paths./settings/fields.get) to retrieve the unique ID fields.
            - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the unique field in the Leads module. Use the [Get Fields Metadata API](fields.json#$.paths./settings/fields.get) to retrieve the API names of the unique fields.
            - `name` (string) **REQ** [maxLen=50] — Represents the module that the field belongs to, not the field's own display name. The API returns `Leads` for `current_field` and `Contacts` for `mapped_field`.
          - `mapped_field` (object) **REQ** — Mapped field details.
            - `id` (string) **REQ** [maxLen=50] — Represents the unique identifier of the mapped field.
            - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the mapped field.
            - `name` (string) **REQ** [maxLen=50] — Represents the module that the mapped field belongs to, not the field's own display name. The API returns `Contacts`.
        - `mapped_module` (object) **REQ** — Represents the mapped module details.
          - `id` (string) **REQ** [maxLen=50] — Represents the unique identifier of the module.
          - `api_name` (string) **REQ** [enum=['Contacts']] — Represents the API name of the module.
          - `name` (string) **REQ** [enum=['Contacts']] — Represents the display name of the module.

- **204**: Indicates that duplicate check preference is not enabled for the specified module.

- **400**: Bad Request - Invalid or missing parameters [application/json]
    oneOf:
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Error code
        - `details` (object) **REQ** — Additional error context
          - `param_name` (string) [maxLen=50] — Missing parameter name
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code
        - `details` (object) **REQ** — Additional error context
          - `param_name` (string) [maxLen=50] — Invalid parameter name
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Error status indicator
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Error code
        - `details` (object) **REQ** — Additional error context
          - `param_name` (string) [maxLen=50] — Name of the unsupported parameter
        - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Error status indicator

- **403**: No permission to perform this operation [application/json]
    > No permission error response
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code indicating permission denied
    - `details` (object) **REQ** — Additional error details
      - `permissions` (array of string) [maxItems=25] — List of required permissions
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=1000] — Human-readable error message
    - `status` (string) **REQ** [enum=['error']] — Status indicator for error

**Scopes:** ZohoCRM.settings.duplicate_check_preference.READ

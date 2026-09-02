# GET /settings/profiles/{id}
**Operation:** `getProfile` — Profile
> Retrieves the full details of the CRM profile identified by `{id}`, including its complete permission tree organized by sections and categories. See [Get Profiles](https://www.zoho.com/crm/developer/docs/api/v8/get-profiles.html).

**Parameters:**
- `id` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$]: Represents the unique identifier of the profile (64-bit integer represented as a string, 1-19 digits).

**Schemas:**
`UserReference`:
  > Reference to the CRM user who performed an action on a profile.
  - `name` (string) **REQ** [maxLen=100, minLen=1] — Display name of the user as shown in Zoho CRM.
  - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique record identifier - a 64-bit integer encoded as a string of 1 to 19 decimal digits.

**Responses:**

- **200**: Profile retrieved successfully. [application/json]
    > Successful response containing the requested profile's details.
    - `profiles` (array of object) [maxItems=1] **REQ** — Array containing the details of the requested profile (single-item array).
      - `api_name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z][A-Za-z0-9_]*$] — API name of the profile, composed of alphanumeric characters and underscores and starting with a letter.
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique profile identifier.
      - `created_time` (object `CreatedTime`) **REQ** — Creation timestamp of the profile - an ISO 8601 datetime string, or null when creation time is not available.
        oneOf:
            schema: `Timestamp`
            type: string/date-time — ISO 8601 datetime string with timezone offset representing when the profile action was performed (for example, `2024-05-17T09:15:56+05:30`).
            schema: `TypeNull`
            type: null — Represents a null value for optional fields.
      - `modified_time` (object `ModifiedTime`) **REQ** — Last modification timestamp of the profile - an ISO 8601 datetime string, or null when the modification time is not available.
        oneOf:
            schema: `Timestamp`
            type: string/date-time — ISO 8601 datetime string with timezone offset representing when the profile action was performed (for example, `2024-05-17T09:15:56+05:30`).
            schema: `TypeNull`
            type: null — Represents a null value for optional fields.
      - `name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[^~`#%^&*()+|,={};\[\]"]+$] — Display name for the profile, up to 50 characters, excluding the special characters `~`, `` ` ``, `#`, `%`, `^`, `&`, `*`, `(`, `)`, `+`, `|`, `,`, `=`, `{`, `}`, `;`, `[`, `]`, `"`.
      - `display_label` (string) **REQ** [maxLen=255] — Display label shown for the profile in the CRM UI.
      - `modified_by` (object `ModifiedBy`) — Last modifier of the profile - a [UserReference](users.yaml#$.paths./users.get) object, or null when modifier information is not available.
        oneOf:
            schema: `TypeNull`
            type: null — Represents a null value for optional fields.
      - `description` (string) [maxLen=255, nullable] — Optional description of the profile.
      - `created_by` (object `CreatedBy`) — Creator of the profile - a [UserReference](users.yaml#$.paths./users.get) object, or null when creator information is not available.
        oneOf:
            schema: `TypeNull`
            type: null — Represents a null value for optional fields.
      - `custom` (boolean) **REQ** — Indicates whether the profile is a custom profile (`true`) or a system profile (`false`).
      - `type` (string) **REQ** [enum=[5 values]] — Profile type classification. Possible values: `private_profile`, `normal_profile`, `lite_profile`, `system_profile`, `portal_profile`. `private_profile` is used exclusively for team modules; non-private profiles are not allowed for team modules.
      - `permissions_details` (array of object) [maxItems=2000] **REQ** — Flat list of all individual permissions configured for this profile (up to 2000 entries).
        - `display_label` (string) [maxLen=255] — Human-readable label displayed for this permission in the CRM UI.
        - `module` (string) [maxLen=100, nullable] — Module associated with this permission. Null when the permission is not tied to a specific module.
        - `name` (string) [maxLen=255] — Internal API name of the permission.
        - `customizable` (boolean) — Indicates whether this permission can be toggled on or off by an administrator.
        - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — The unique identifier of the permission.
        - `enabled` (boolean) — Indicates whether this permission is currently enabled for the profile.
        - `tooltip_msg` (string) [maxLen=500] — Tooltip text displayed when hovering over this permission in the CRM UI.
        - `api_name` (string) [maxLen=255] — API name of the permission.
        - `active` (boolean) — Whether the permission is active.
        - `description` (string) [maxLen=500, nullable] — Description of the permission.
        - `custom_permission` (boolean) — Whether this is a custom permission.
        - `parent_permissions` (object) — List of parent permission names this permission depends on, or null when there are no parent dependencies.
          oneOf:
              type: array of string/int64 `Id` [maxItems=200]
                schema: `Id`
                type: string/int64 [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique record identifier - a 64-bit integer encoded as a string of 1 to 19 decimal digits.
                items: [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$]
              schema: `TypeNull`
              type: null — Represents a null value for optional fields.
      - `$has_more` (boolean) — Indicates whether the profile has more permission records beyond the included set.
      - `sections` (array of object) [maxItems=100] — Grouped sections that organize permissions into categories for display in the CRM UI (up to 100 sections).
        - `name` (string) **REQ** [maxLen=255] — Internal name of the permission section.
        - `categories` (array of object) [maxItems=100] **REQ** — List of permission categories within this section (up to 100 categories).
          - `display_label` (string) **REQ** [maxLen=255] — Display label shown for this category in the CRM UI.
          - `permissions_details` (array of string) [minItems=0, maxItems=500] **REQ** — Permission identifiers grouped under this category.
            items: [maxLen=255]
          - `name` (string) **REQ** [maxLen=255] — Internal name of the permission category.
          - `module` (string) [maxLen=100, nullable] — Module associated with this category or null when the category is not module-specific.

- **204**: No content - the profile exists but has no body to return.

- **400**: Invalid request. [application/json]
    > Error response body for invalid GET /settings/profiles/{id} requests.
    oneOf:
        schema: `InvalidRequestMethodError`
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Error code indicating an unsupported HTTP method. Possible values: `INVALID_REQUEST_METHOD`.
        - `details` (object) **REQ** — Empty details object included with the invalid method error.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable description of the invalid request method.
        - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `InvalidIdError`
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating an invalid profile ID. Possible values: `INVALID_DATA`.
        - `details` (object) **REQ** — Details object identifying the path segment that contains the invalid ID.
          - `resource_path_index` (integer/int32) **REQ** — Zero-based index of the URL path segment that contains the invalid profile ID.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable description of the invalid ID error.
        - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**

- **401**: Unauthorized - authentication failed or the access token lacks the required OAuth scope. [application/json]
    > Unauthorized error response body.
    oneOf:
        schema: `AuthenticationFailureError`
        - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Error code indicating the authentication failure. Possible values: `AUTHENTICATION_FAILURE`.
        - `details` (object) **REQ** — Empty details object included with the authentication error.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable description of the authentication failure.
        - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `OAuthScopeMismatchError`
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Error code indicating an OAuth scope mismatch. Possible values: `OAUTH_SCOPE_MISMATCH`.
        - `details` (object) **REQ** — Empty details object included with the scope mismatch error.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable description of the scope mismatch.
        - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**

- **403**: Forbidden - the authenticated user lacks the required permission to perform this operation. [application/json]
    > Forbidden error response body.
    schema: `PermissionErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code indicating the permission denial. Possible values: `NO_PERMISSION`.
    - `details` (object) **REQ** — Details object listing the permissions required for the operation.
      - `permissions` (array of string) [maxItems=10] — List of permission identifiers required to perform this operation.
        items: [maxLen=100]
    - `message` (string) **REQ** [maxLen=255] — Human-readable description of the permission error.
    - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**

- **500**: Internal server error - an unexpected error occurred while processing the request. [application/json]
    > Internal server error response body.
    schema: `InternalServerError`
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Error code for the internal server error. Possible values: `INTERNAL_ERROR`.
    - `details` (object) **REQ** — Empty details object included with the internal error.
    - `message` (string) **REQ** [maxLen=1000] — Human-readable description of the internal server error.
    - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**

**Scopes:** ZohoCRM.settings.profiles.READ

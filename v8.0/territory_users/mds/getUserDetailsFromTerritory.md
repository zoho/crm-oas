# GET /settings/territories/{territory}/users/{user}
**Operation:** `getUserDetailsFromTerritory` — Specific Territory User
> To retrieve the details of a specific user associated with a territory in your Zoho CRM organization.

**Parameters:**
- `territory` (path, string, required) [maxLen=100]: Territory Id Param in URL
- `user` (path, string, required) [maxLen=100]: User Id Param in URL

**Responses:**

- **200**: Returns the details of the specified user associated with the territory. [application/json]
    > Represents the success response body containing the details of the specified user associated with the territory.
    - `users` (array of object `User`) [maxItems=100] **REQ** — Represents the list of users associated with the territory.
      schema: `User`
      - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the user.
      - `first_name` (string) **REQ** [maxLen=50] — Represents the user's first name.
      - `last_name` (string) [maxLen=50, nullable] — Represents the user's last name.
      - `full_name` (string) **REQ** [maxLen=200] — Represents the user's full name.
      - `country` (string) [maxLen=100, nullable] — Represents the user's country.
      - `state` (string) [maxLen=100, nullable] — Represents the user's state or province.
      - `city` (string) [maxLen=100, nullable] — Represents the user's city.
      - `zip` (string) [maxLen=30, nullable] — Represents the user's postal or zip code.
      - `fax` (string) [maxLen=30, nullable] — Represents the user's fax number.
      - `street` (string) [maxLen=250, nullable] — Represents the user's street address.
      - `status` (string) **REQ** [enum=['inactive', 'deleted', 'rejected', 'active', 'closed', 'disabled']] — Represents the user's account status.
      - `category` (string) **REQ** [enum=['regular_user', 'sandbox_user', 'light_user']] — Represents the user's category or type.
      - `profile` (object) **REQ** — Represents the user's profile.
        - `id` (string) **REQ** [maxLen=100] — Represents the unique ID of the user's profile.
        - `name` (string) **REQ** [maxLen=100] — Represents the name of the user's profile.
      - `role` (object) **REQ** — Represents the user's role.
        - `id` (string) **REQ** [maxLen=100] — Represents the unique ID of the user's role.
        - `name` (string) **REQ** [maxLen=100] — Represents the name of the user's role.
      - `created_by` (object) **REQ** — Represents the user who created this user record.
        - `id` (string) **REQ** [maxLen=100] — Represents the unique ID of the creator.
        - `name` (string) **REQ** [maxLen=200] — Represents the full name of the creator.
      - `created_time` (string/date-time) **REQ** — Represents the date and time when the user account was created.
      - `Modified_By` (object) **REQ** — Represents the user who last modified this user record.
        - `id` (string) **REQ** [maxLen=100] — Represents the unique ID of the modifier.
        - `name` (string) **REQ** [maxLen=200] — Represents the full name of the modifier.
      - `Modified_Time` (string/date-time) **REQ** — Represents the date and time when the user account was last modified.
      - `language` (string) **REQ** [maxLen=50] — Represents the user's preferred language.
      - `locale` (string) **REQ** [maxLen=50] — Represents the user's locale.
      - `time_zone` (string) [maxLen=50] — Represents the user's time zone.
      - `time_format` (string) [enum=['HH:mm', 'hh:mm a']] — Represents the user's preferred time format.
      - `date_format` (string) [maxLen=50] — Represents the user's preferred date format.
      - `decimal_separator` (string) [enum=['Comma', 'Period']] — Represents the user's preferred decimal separator.
      - `number_separator` (string) [maxLen=10] — Represents the user's preferred number separator.
      - `country_locale` (string) [maxLen=50] — Represents the user's country locale.
      - `microsoft` (boolean) — Indicates whether the user has Microsoft integration enabled.
      - `sandboxDeveloper` (boolean) — Indicates whether the user is a sandbox developer.
      - `personal_account` (boolean) — Indicates whether this is a personal account.
      - `Isonline` (boolean) — Indicates whether the user is currently online.
      - `confirm` (boolean) — Indicates whether the user has confirmed their account.
      - `offset` (integer/int32) — Represents the time zone offset in milliseconds.
      - `zuid` (string) **REQ** [maxLen=100] — Represents the Zoho user ID.
      - `alias` (string) [maxLen=50, nullable] — Represents the user's alias.
      - `dob` (string/date) [nullable] — Represents the user's date of birth.
      - `website` (string) [maxLen=250, pattern=[a-z0-9]{5}[.]com, nullable] — Represents the user's website URL.
      - `signature` (string) [maxLen=200, nullable] — Represents the user's email signature.
      - `name_format__s` (string) [enum=[6 values]] — Represents the user's preferred name format.
      - `sort_order_preference__s` (string) [maxLen=50] — Represents the user's sort order preference.
      - `status_reason__s` (string) [maxLen=100, nullable] — Represents the reason for the user's current status.
      - `default_tab_group` (string) [maxLen=100] — Represents the user's default tab group.
      - `$shift_effective_from` (object) [nullable] — Represents the date from which the user's shift becomes effective.
      - `$current_shift` (object) [nullable] — Represents the user's current shift assignment.
      - `$next_shift` (object) [nullable] — Represents the user's next upcoming shift assignment.
      - `customize_info` (object) — Represents the user's customization preferences.
        - `notes_desc` (object) [nullable] — Indicates whether the notes description is visible.
        - `show_right_panel` (boolean) [nullable] — Indicates whether the right panel is visible.
        - `show_left_panel` (boolean) [nullable] — Indicates whether the left panel is visible.
        - `bc_view` (object) [nullable] — Represents the business card view preference.
        - `show_home` (boolean) — Indicates whether the home page is visible.
        - `show_detail_view` (boolean) — Indicates whether the detail view is visible.
        - `unpin_recent_item` (object) [nullable] — Indicates whether recent items are unpinned.
      - `theme` (object) — Represents the user's UI theme preferences.
        - `normal_tab` (object) **REQ** — Represents the normal tab theme settings.
          - `font_color` (string) **REQ** [maxLen=7, pattern=^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$] — Represents the font color of the normal tab in hexadecimal format.
          - `background` (string) **REQ** [maxLen=7, pattern=^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$] — Represents the background color of the normal tab in hexadecimal format.
        - `selected_tab` (object) **REQ** — Represents the selected tab theme settings.
          - `font_color` (string) **REQ** [maxLen=7, pattern=^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$] — Represents the font color of the selected tab in hexadecimal format.
          - `background` (string) **REQ** [maxLen=7, pattern=^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$] — Represents the background color of the selected tab in hexadecimal format.
        - `new_background` (string) [maxLen=7, pattern=^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$, nullable] — Represents the new background color of the theme.
        - `background` (string) **REQ** [maxLen=7, pattern=^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$] — Represents the overall background color of the theme.
        - `screen` (string) **REQ** [enum=['stretched', 'fixed']] — Represents the screen layout preference.
        - `type` (string) **REQ** [enum=['default', 'custom']] — Represents the type of theme applied.
    - `info` (object) **REQ** — Represents the pagination metadata for the response.
      - `per_page` (integer/int32) **REQ** — Represents the number of records per page.
      - `count` (integer/int32) **REQ** — Represents the total number of records returned.
      - `page` (integer/int32) **REQ** — Represents the current page number.
      - `more_records` (boolean) **REQ** — Indicates whether there are more records available beyond the current page.

- **204**: No content found for the specified user in the territory.

- **400**: Returns an error when the request contains invalid parameters. **Resolution:** Verify the territory ID and user ID and ensure all required parameters are provided. [application/json]
    > Represents the error response body returned when the request contains invalid parameters.
    oneOf:
      - `UserInvalidErrorSchemaInURL` — Represents the invalid-request error schema when the territory or user ID in the URL is invalid.
        - `code` (string) **REQ** [enum=[5 values]] — Represents the error code for the validation failure. Possible values: **INVALID_DATA**, **DUPLICATE_DATA**, **MANDATORY_NOT_FOUND**, **NOT_ALLOWED**, **DEPENDENT_FIELD_MISSING**.
        - `details` (object) **REQ** — Represents additional contextual information about the URL validation error.
          - `api_name` (string/string) [minLen=1] — Represents the API field name associated with the URL validation error.
          - `json_path` (string/string) [minLen=1] — Represents the JSON path to the field that caused the URL validation error.
          - `supported_values` (array of string) [maxItems=100] — Represents the list of supported values for the field associated with the URL validation error.
            items: [maxLen=100]
          - `id` (string/string) — Represents the unique identifier of the resource related to the URL validation error.
          - `resource_path_index` (integer/int32) — Represents the index in the resource path where the URL validation error occurred.
          - `dependee` (object) — Represents the dependent field information related to the URL validation error.
            - `api_name` (string/string) — Represents the API field name of the dependent field that caused the URL validation error.
            - `json_path` (string/string) [minLen=1] — Represents the JSON path to the dependent field that caused the URL validation error.
            - `resource_path_index` (integer/int32) — Represents the index in the resource path where the dependent field is located.
        - `message` (string/string) **REQ** — Represents the detailed error message describing the URL validation failure.
        - `status` (string) **REQ** [enum=['error', 'success', 'failure']] — Represents the outcome status of the response. Possible values: **error**, **success**, **failure**.

- **403**: Returns an error when the territory feature is not yet enabled, is disabled, or access is denied. **Resolution:** Ensure the Territories feature is active and that your OAuth token includes the required scopes. [application/json]
    > Represents the error response body returned when access is denied or the territory feature is not enabled.
    oneOf:
      - `TerritoryErrorPermissionDenied` — Territory Not yet Enabled.
        - `code` (string) **REQ** [enum=[4 values]] — Represents the error code indicating why territory access was denied. Possible values: **PERMISSION_DENIED**, **FEATURE_NOT_ENABLED**, **TERRITORY_DISABLED**, **TERRITORY_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the permission denied error, returned as an empty object.
        - `message` (string) **REQ** [maxLen=100] — Represents the human-readable description of why the territory access was denied.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error**.

- **500**: An internal server error occurred while processing the request. **Resolution:** Retry the request after some time. If the error persists, contact Zoho CRM support. [application/json]
    > Represents the error response body returned when an internal server error occurs.
    oneOf:
      - `TerritoryInternalServerErrorSchema` — Internal server error.
        - `code` (string) **REQ** [enum=['INTERNAL_SERVER_ERROR']] — Represents the error code for an internal server error. Possible values: **INTERNAL_SERVER_ERROR**.
        - `details` (object) **REQ** — Represents additional details about the internal server error, returned as an empty object.
        - `message` (string) **REQ** [maxLen=100] — Represents the human-readable description of the internal server error.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error**.

**Scopes:** ZohoCRM.users.READ, ZohoCRM.settings.territories.READ, ZohoCRM.users.ALL, ZohoCRM.settings.territories.ALL

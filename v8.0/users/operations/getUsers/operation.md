# GET /users
**Operation:** `getUsers` — Get users
> To retrieve all users in your Zoho CRM organization based on the specified filter parameters, including type, role, query criteria, and field selection.

**Parameters:**
- `type` (query, string, optional) [enum=[18 values]]: Specify the type of users to retrieve.
Possible values:
CurrentUser - Retrieves the currently authenticated user.
DeletedUsers - Retrieves only deleted users.
DeactiveUsers - Retrieves only deactivated users.
NotConfirmedUsers - Retrieves only unconfirmed users.
ConfirmedUsers - Retrieves only confirmed users.
ActiveUsers - Retrieves only active users.
AdminUsers - Retrieves only administrator users.
ActiveConfirmedAdmins - Retrieves active, confirmed, and administrator users.
ActiveConfirmedUsers - Retrieves active and confirmed users.
DeveloperUsers - Retrieves only developer users.
AllUsers - Retrieves all users.
AllActiveUsers - Retrieves all active users.
ActiveLiteUser - Retrieves active lite users.
ActiveAndDeactive - Retrieves both active and deactivated users.
ChildRoleUsers - Retrieves users belonging to child roles.
ParentRoleUsers - Retrieves users belonging to the parent role.
SubordinateRoleUsers - Retrieves users in subordinate roles.
ConfirmedReportingUsers - Retrieves confirmed users who have reporting relationships.
- `page` (query, integer/int32, optional): Specify the page number to retrieve in the paginated response.
- `per_page` (query, integer/int32, optional): Specify the number of user records to return per page.
- `include_lite_users` (query, boolean, optional): Specify whether to include lite users in the result set.\n\nPossible values:\ntrue - Lite users are included.\nfalse - Lite users are not included.
- `role_id` (query, string, optional) [maxLen=19]: Specify the role ID to filter users. The API retrieves users with the specified role and higher or lower roles based on the value of the **type** parameter. Applicable only for **ParentRoleUsers**, **ChildRoleUsers**, and **SubordinateRoleUsers** types.
- `query_id` (query, string/int64, optional): Specify the query ID of the user lookup field. Used to retrieve users based on the filter criteria of the lookup field.
- `child_data` (query, object, optional): Specify the child data object containing the record ID of the module with a user lookup field. This is required only if the user lookup field has criteria based on the dynamic value of a record. The **query_id** parameter is required when this parameter is provided.
- `ids` (query, array, optional) [minItems=1, maxItems=100] {style=form, explode=False}: Specify a comma-separated list of user IDs to retrieve. If not provided, the API retrieves all users based on the other parameters.
- `fields` (query, string, optional) [maxLen=3000, pattern=^[A-Za-z][A-Za-z0-9_]*$] {style=form, explode=False}: Specify the comma-separated list of field API names to include in the response.
- `type__s` (query, string, optional) [enum=[6 values]] {style=form, explode=False}: Filter users by their account type.
Possible values:
**Regular User** - Standard CRM user with full access to the organization.
**Sandbox Developer User** - User with access to the sandbox environment for development and testing.
**Team User** - User operating as part of a team account.
**Digital Employee** - Automated or bot-type user representing a digital workforce entity.
**Support User** - User with access granted for support purposes.
**Client Portal User** - User with limited access via the client-facing portal.

**Responses:**

- **200**: Returns user records matching the specified filter parameters. The response body contains a list of user objects and an info object. [application/json]
    > Contains the paginated response for the getUsers operation. Includes a list of user objects and an info object.
    - `users` (array of object `GetUserDetails`) [maxItems=200] — List of user objects, each representing an individual Zoho CRM user returned by the query.
      schema: `GetUserDetails`
      - `$next_shift` (object) — Represents the upcoming shift scheduled for the user, including the shift's ID and name.
        oneOf:
            - `name` (string) **REQ** [maxLen=80] — Represents the display name of the user's upcoming shift.
            - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user's upcoming shift.
            type: null — Indicates that no upcoming shift is assigned to the user.
      - `$current_shift` (object) — Represents the shift currently assigned to the user, including the shift's ID and name.
        oneOf:
            - `name` (string) **REQ** [maxLen=80] — Represents the display name of the user's current shift.
            - `id` (string/int64) **REQ** — Represents the unique ID of the user's current shift.
            type: null — Indicates that no current shift is assigned to the user.
      - `$shift_effective_from` (object) — Represents the date on which the user's upcoming shift becomes effective.
        oneOf:
            type: string/date [pattern=([0-9]{4})-([0-9]{2})-([0-9]{2})] — Represents the date from which the upcoming shift assignment becomes effective.
            type: null — Indicates that no upcoming shift effective date is set.
      - `confirm` (boolean) [readOnly] — Indicates whether the user has accepted the invitation to join the organization.\n\nPossible values:\ntrue - The user has accepted the invitation.\nfalse - The user has not yet accepted the invitation.
      - `date_format` (string) [enum=[49 values]] — Represents the user's preferred date format used for displaying date values throughout the application.
      - `decimal_separator` (string) [enum=['Comma', 'Period']] — Represents the user's preferred decimal separator character used when displaying numerical values.
      - `email` (string) [maxLen=100, pattern=^[\+\-\p{L}\p{M}\p{N}_]([\p{L}\p{M}\p{N}!#$%&'*+\-\/=?^_`{|}~.]*)@(?=.{4,256}$)(([\p{L}\p{N}\p{M}]+)(([\-_]*[\p{L}\p{M}\p{N}])*)[.])+[\p{L}\p{M}]{2,22}$] — Represents the email address associated with the user's account.
      - `first_name` (object) — Represents the user's first name. Returns null if no first name is set.
        oneOf:
            type: string [maxLen=50] — Represents the first name of the user.
            type: null — Indicates that no first name is set for the user.
      - `full_name` (string) [maxLen=100, readOnly] — Represents the user's full name.
      - `id` (string) [maxLen=19, readOnly] — Represents the unique identifier of the user.
      - `last_name` (object) — Represents the user's last name. Returns null if no last name is set.
        oneOf:
            type: string [maxLen=50] — Represents the last name of the user.
            type: null — Indicates that no last name is set for the user.
      - `type__s` (string) [enum=[7 values], readOnly] — Represents the account type of the user.
      - `profile` (object) — Represents the profile associated with the user, including the profile's unique identifier and display name.
        - `name` (string) **REQ** [maxLen=50] — Represents the display name of the profile associated with the user.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the profile associated with the user.
      - `role` (object) — Represents the role assigned to the user, containing the role's unique identifier and display name.
        - `name` (string) **REQ** [maxLen=200] — Represents the display name of the role assigned to the user.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the role assigned to the user.
      - `status` (object) — Represents the current status of the user in the Zoho CRM organization.
Possible values:
active - The user is active and can access the CRM.
inactive - The user is deactivated and cannot access the CRM.
deleted - The user account has been deleted.
disabled - The user account is disabled.
closed - The user account is closed.
disabled dormant - The user account is disabled and dormant.
        oneOf:
            type: string [enum=['deleted', 'disabled', 'closed', 'disabled dormant'], readOnly] — Represents the current status of the user in the Zoho CRM organization.
            type: string [enum=['active', 'inactive']] — Indicates that no status is set for the user.
      - `zuid` (object) — Represents the Zoho User ID (ZUID) associated with the user's Zoho account.
        oneOf:
            type: string [maxLen=19] — Represents the Zoho User ID (ZUID) associated with the user.
            type: null — Indicates that no ZUID is associated with the user.
      - `alias` (object) — Represents the alias or short name associated with the user. Returns null if no alias is configured.
        oneOf:
            type: string [maxLen=50] — Represents the alias or short name associated with the user.
            type: null — Indicates that no alias is configured for the user.
      - `created_by` (object) — Represents the user who created this user record. Returns null if the creator information is not available. Refer to the [Get Users](users.yaml#$.paths./users.get) endpoint for details.
        oneOf:
            - `name` (string) **REQ** [maxLen=100] — Represents the full name of the user who created this record.
            - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user who created this record.
            type: null — Indicates that no creator information is available for this user record.
      - `created_time` (object) — Represents the date and time when this user record was first added to the system, in ISO 8601 format. Returns null if the creation time is not available.
        oneOf:
            type: string/date-time [readOnly] — Represents the date and time when this user record was first created.
            type: null — Indicates that no creation time is available for this user record.
      - `locale` (string) [enum=[29 values]] — Represents the locale of the user.
      - `microsoft` (boolean) — Indicates whether the user is authenticated via a Microsoft account.\nPossible values:\ntrue - The user is a Microsoft account user.\nfalse - The user is not a Microsoft account user.
      - `Modified_By` (object) — Represents the user who last modified this user record. Returns null if no modification has occurred. Refer to the [Get Users](users.yaml#$.paths./users.get) endpoint for details.
        oneOf:
            - `name` (string) **REQ** [maxLen=100] — Represents the full name of the user who last modified this user record.
            - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user who last modified this user record.
            type: null — Indicates that no modification has been recorded for this user record.
      - `Modified_Time` (object) — Represents the date and time at which this user record was last modified, in ISO 8601 format. Returns null if no modification has occurred.
        oneOf:
            type: string/date-time [readOnly] — Represents the date and time at which this user record was last modified.
            type: null — Indicates that no modification time is recorded for this user record.
      - `phone` (string) [maxLen=30, nullable] — Represents the user's phone number. Returns null when no phone number is associated with the account.
      - `mobile` (string) [maxLen=30, nullable] — Represents the user's mobile phone number. Returns null when no mobile number is associated with the account.
      - `city` (object) — Represents the city associated with the user's address. Returns null if no city is configured.
        oneOf:
            type: string [maxLen=100] — Represents the city associated with the user.
            type: null — Indicates that no city is configured for the user.
      - `country` (object) — Represents the country associated with the user's address. Returns null if no country is configured.
        oneOf:
            type: string [maxLen=100] — Represents the country associated with the user.
            type: null — Indicates that no country is configured for the user.
      - `dob` (object) — Represents the user's date of birth. Returns null if no date of birth has been set.
        oneOf:
            type: string/date — Represents the user's date of birth.
            type: null — Indicates that no date of birth is set for the user.
      - `fax` (object) — Represents the user's fax number. Returns null if no fax number is configured.
        oneOf:
            type: string [maxLen=30] — Represents the user's fax number.
            type: null — Indicates that no fax number is configured for the user.
      - `number_separator` (string) [enum=['Comma', 'Period', 'Space', 'comma', 'period', 'space']] — Represents the character used as a separator when formatting numbers for the user. This field is case-insensitive.
      - `state` (object) — Represents the user's state or province. Returns null if no state is set.
        oneOf:
            type: string [maxLen=100] — Represents the state or province associated with the user.
            type: null — Indicates that no state or province is set for the user.
      - `street` (object) — Represents the user's street address. Returns null if no street address is set.
        oneOf:
            type: string [maxLen=250] — Represents the street address associated with the user.
            type: null — Indicates that no street address is set for the user.
      - `time_format` (string) [enum=['HH:mm', 'hh:mm a']] — Represents the time format preferred by the user for displaying time values.
      - `website` (object) — Represents the user's website URL. Returns null if no website is configured.
        oneOf:
            type: string [maxLen=250, pattern=^(http:\/\/www.|https:\/\/www.|ftp:\/\/www.|www.|http:\/\/|https:\/\/|ftp:\/\/|){1}[^\x00-\x19\x22-\x27\x2A-\x2C\x2E-\x2F\x3A-\x3F\x5B-\x5E\x60\x7B\x7D-\x7F]+(\.[^\x00-\x19\x22\x24-\x2C\x2E-\x2F\x3C\x3E\x40\x5B-\x5E\x60\x7B\x7D-\x7F]+)+([\/\?].*)*$] — Represents the website URL associated with the user.
            type: null — Indicates that no website URL is configured for the user.
      - `zip` (object) — Represents the user's postal code or ZIP code. Returns null if no postal code is set.
        oneOf:
            type: string [maxLen=30] — Represents the postal code or ZIP code associated with the user.
            type: null — Indicates that no postal code is set for the user.
      - `sandboxDeveloper` (boolean) — Indicates whether the user is designated as a sandbox developer.\n\nPossible values:\ntrue - The user is a sandbox developer.\nfalse - The user is not a sandbox developer.
      - `name_format__s` (string) [enum=[6 values]] — Represents the format used to display the user's name.
      - `language` (string) [enum=[231 values]] — Represents the preferred language of the user. This value can be updated only by the user themselves.
      - `status_reason__s` (object) — Represents the reason for the user's current status. Returns null if no reason is associated with the current status.
        oneOf:
            type: string [enum=[6 values]] — Represents the reason for the user's current status.
            type: null — Indicates that no status reason is associated with the user's current status.
      - `country_locale` (string) [enum=[247 values]] — Represents the locale associated with the user's country.
      - `ezuid` (string) [maxLen=100, readOnly] — Represents the encrypted Zoho User ID (ZUID), used to securely identify the user without showing their actual ID.
      - `image_link` (string) [maxLen=100] — Represents the URL of the user's profile image as provided by the Identity and Access Management (IAM) system.
      - `sort_order_preference__s` (string) [enum=['First Name,Last Name', 'Last Name,First Name']] — Represents the user's preferred sort order for displaying records.
      - `Reporting_To` (object) — Represents the user to whom this user reports within the organizational hierarchy. Returns null if no reporting manager is assigned. Refer to the [Get Users](users.yaml#$.paths./users.get) endpoint for details.
        oneOf:
            - `name` (string) **REQ** [maxLen=100] — Represents the full name of the user to whom this user reports.
            - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user to whom this user reports.
            type: null — Indicates that no reporting manager is assigned to this user.
      - `share_among_subordinates` (boolean) — Indicates whether the user's records are shared with their subordinates.\n\nPossible values:\ntrue - Records are shared with subordinates.\nfalse - Records are not shared with subordinates.
      - `imap_status` (boolean) — Indicates whether IMAP access is enabled for the user.\nPossible values:\ntrue - IMAP access is enabled.\nfalse - IMAP access is disabled.
      - `time_zone` (string) [maxLen=150] — Represents the time zone of the user. This value can be updated only by the user themselves.
      - `distance_preference__s` (string) [enum=['Kilometers', 'Miles']] — Represents the user's preferred unit of measurement for displaying distance values.
      - `default_tab_group` (string) [maxLen=100] — Represents the default tab group assigned to the user, determining which group of tabs is presented upon login.
      - `signature` (string) [maxLen=200, nullable] — Represents the email signature configured for the user. Returns null if no signature has been set.
      - `personal_account` (boolean) — Indicates whether the user has a personal account associated with their profile.\n\nPossible values:\ntrue - The user has a personal account.\nfalse - The user does not have a personal account.
      - `customize_info` (object) — Represents a collection of user interface customization preferences associated with the user's account.
        - `notes_desc` (boolean) [nullable] — Indicates whether notes are displayed in descending order for the user.\nPossible values:\ntrue - Notes are displayed in descending order.\nfalse - Notes are not displayed in descending order.
        - `show_left_panel` (boolean) [nullable] — Indicates whether the left panel is displayed in the user interface.\n\nPossible values:\ntrue - The left panel is shown.\nfalse - The left panel is hidden.
        - `show_right_panel` (object) — Indicates whether the right panel is displayed in the user interface.\n\nPossible values:\ntrue - The right panel is shown.\nfalse - The right panel is hidden.
          oneOf:
              type: string [maxLen=20] — Indicates that the right panel is displayed in the user interface.
              type: null — Indicates that the right panel is not displayed in the user interface.
        - `show_detail_view` (boolean) — Indicates whether the detail view panel is displayed for the user.\nPossible values:\ntrue - The detail view panel is displayed.\nfalse - The detail view panel is not displayed.
        - `unpin_recent_item` (object) — Indicates whether the recent item is unpinned from its fixed position in the user interface.\n\nPossible values:\ntrue - The recent item is unpinned.\nfalse - The recent item remains pinned.
          oneOf:
              type: boolean — Indicates that the recent item is unpinned from its fixed position.
              type: null — Indicates that the recent item remains pinned in its fixed position.
        - `bc_view` (object) — Indicates whether the breadcrumb view is displayed for the user.\nPossible values:\ntrue - The breadcrumb view is displayed.\nfalse - The breadcrumb view is not displayed.
          oneOf:
              type: boolean — Indicates that the breadcrumb view is displayed for the user.
              type: null — Indicates that the breadcrumb view is not displayed for the user.
        - `show_home` (boolean) — Indicates whether the home screen is displayed for the user.\nPossible values:\ntrue - The home screen is displayed.\nfalse - The home screen is not displayed.
        additionalProperties: any
      - `theme` (object) — Represents the theme configuration applied to the user's CRM interface. Includes color and display settings for the background, screen, header, normal tab, and selected tab elements.
        - `normal_tab` (object) — Represents the theme configuration for the normal (unselected) tab in the user's CRM interface, including background color and font color settings.
          - `background` (string/hex-color) — Represents the background color of the normal tab in the user's theme.
          - `font_color` (string/hex-color) — Represents the font color of the normal tab in the user's theme.
        - `selected_tab` (object) — Represents the theme configuration for the currently selected tab in the user's CRM interface, including background color and font color settings.
          - `background` (string/hex-color) — Represents the background color of the selected tab in the user's theme.
          - `font_color` (string/hex-color) — Represents the font color of the selected tab in the user's theme.
        - `header` (object) — Represents the theme configuration for the header area of the user's CRM interface. Includes the background color and font color settings for the header.
          - `background` (string/hex-color) — Represents the background color of the header area in the user's theme.
          - `font_color` (string/hex-color) — Represents the font color of the header area in the user's theme.
        - `new_background` (string/hex-color) [nullable] — Represents the updated background color applied to the user's theme.
        - `background` (string/hex-color) — Represents the background color of the user's theme.
        - `screen` (string) [enum=['fixed']] — Represents the screen type or layout setting applied to the user's CRM interface.
        - `type` (string) [enum=['default', 'custom']] — Represents the type of theme applied to the user's CRM interface.
      - `offset` (integer/int32) [readOnly] — Represents the user's current UTC offset in milliseconds, adjusted for Daylight Saving Time (DST) where applicable. For example, a timezone of UTC+5:30 yields an offset value of 19800000 (5.5 hours × 3600 seconds × 1000 milliseconds). This value may be added to the current UTC time to derive the user's local time.
      - `Status_Updated_By__s` (object) — Represents the details of the user who last updated the status of this user. Returns null if no status update has been recorded.
        oneOf:
            - `name` (string) **REQ** [maxLen=100] — Represents the full name of the user who last updated the status of this user.
            - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user who last updated the status of this user.
            type: null — Indicates that no status update has been recorded for this user.
      - `Confirmed_Time__s` (object) — Represents the date and time at which the user's status was confirmed. Returns null if confirmation has not occurred.
        oneOf:
            type: string/date-time — Represents the date and time at which the user status was confirmed.
            type: null — Indicates that no confirmation time is recorded for the user.
      - `Status_Updated_Time__s` (string/date-time) [readOnly] — Represents the date and time at which the status of this user was last updated.
      - `Invited_Time__s` (object) — Represents the date and time at which the most recent invitation was sent to this user. Returns null if no invitation has been sent.
        oneOf:
            type: string/date-time [readOnly] — Represents the date and time at which the most recent invitation was sent to this user.
            type: null — Indicates that no invitation has been sent to this user.
      - `Invited_By__s` (object) — Represents the user who extended the invitation to this user. Returns null if no inviting user is associated.
        oneOf:
            - `name` (string) **REQ** [maxLen=100] — Represents the full name of the user who invited this user.
            - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user who invited this user.
            type: null — Indicates that no inviting user is associated with this user.
      - `ntc_notification_type` (array of integer/int64) [maxItems=100] — Represents the list of Notification Template Configuration (NTC) notification type identifiers assigned to the user.
      - `ntc_enabled` (boolean) — Indicates whether Notification Template Configuration (NTC) is enabled for the user.\n\nPossible values:\ntrue - NTC is enabled and notification templates are applied to the user.\nfalse - NTC is disabled and notification templates are not applied to the user.
      - `rtl_enabled` (boolean) — Indicates whether Right-to-Left (RTL) text direction is enabled for the user's interface.\n\nPossible values:\ntrue - RTL text direction is enabled for the user.\nfalse - RTL text direction is not enabled for the user.
      - `telephony_enabled` (boolean) — Indicates whether telephony is enabled for the user.\nPossible values:\ntrue - Telephony is enabled for the user.\nfalse - Telephony is not enabled for the user.
      additionalProperties: any
    - `info` (object `Info`) — Represents the pagination metadata returned with the user list response, including the current page, records per page, total count, and whether additional pages are available.
      schema: `Info`
      - `per_page` (integer/int32) **REQ** — Represents the number of user records returned per page.
      - `count` (integer/int32) **REQ** — Represents the total number of user records returned in the current response.
      - `page` (integer/int32) **REQ** — Represents the current page number in the paginated response.
      - `more_records` (boolean) **REQ** — Indicates whether additional records are available beyond the current page.\n\nPossible values:\ntrue - More records are available on subsequent pages.\nfalse - No more records are available.

- **204**: Returns no content when no users match the specified filter criteria.

- **400**: Invalid query parameter or missing required dependent parameter. **Resolution:** The query_id parameter must contain a valid identifier, and the child_data dependent parameter must be provided alongside it. [application/json]
    > The request contains an invalid or missing parameter. The INVALID_DATA error occurs when the query_id parameter has an invalid value. The DEPENDENT_PARAM_MISSING error occurs when query_id is provided but the required child_data dependent parameter is absent.
    oneOf:
      - `UsersGetInvalidParamResponse` — Represents the error response returned when an invalid parameter value is provided in the request.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when an invalid parameter value is provided in the request.
        - `details` (object) **REQ** — Contains additional details about the invalid parameter, including the name of the parameter.
          - `param_name` (string) [enum=['query_id']] — Represents the name of the invalid parameter in the request.
        - `message` (string) **REQ** [enum=['Invalid queryId']] — Represents the error message describing the invalid parameter.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `UsersGetDependentFieldMissingResponse` — Represents the error response returned when a required dependent parameter is missing from the request.
        - `code` (string) **REQ** [enum=['DEPENDENT_PARAM_MISSING']] — Represents the error code returned when a required dependent parameter is missing from the request.
        - `details` (object) **REQ** — Contains additional details about the missing dependent parameter, including the names of the dependent and dependee parameters.
          - `dependee` (object) **REQ** — Represents the parameter that depends on the missing parameter and requires it to be present in the request.
            - `param_name` (string) **REQ** [enum=['child_data']] — Represents the name of the parameter that depends on the missing parameter.
          - `param_name` (string) **REQ** [enum=['query_id']] — Represents the name of the missing required parameter in the request.
        - `message` (string) **REQ** [enum=['Dependent Param missing']] — Represents the error message describing the missing dependent parameter.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

**Scopes:** ZohoCRM.users.READ

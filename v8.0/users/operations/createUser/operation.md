# POST /users
**Operation:** `createUser` — Create User
> To create a new user record in your Zoho CRM organization. The request body must contain a `users` array with one user object including the required fields such as email, role, profile, and first name.

**Request Body** — application/json
> The request body must contain a `users` array with one object.
  > Represents the request payload schema for creating a user in Zoho CRM. Contains the `users` array with user detail objects.
  - `users` (array of object `UserDetails`) [maxItems=1] **REQ** — The request body must contain a `users` array. You can include a maximum of one object per request.
    schema: `UserDetails`
    - `$next_shift` (object) — Specify the upcoming shift to be assigned to the user. Set to null to clear the upcoming shift.
      oneOf:
          - `name` (string) **REQ** [maxLen=80] — Specify the display name of the shift to assign as the upcoming shift.
          - `id` (string/int64) **REQ** [maxLen=100, pattern=^[0-9]+$] — Specify the unique ID of the shift to assign as the upcoming shift.
          type: null — Indicates that no upcoming shift is assigned to the user.
    - `$current_shift` (object) — Specify the current shift assigned to the user. Set to null to clear the assigned shift.
      oneOf:
          - `name` (string) **REQ** [maxLen=80] — Specify the display name of the shift to assign as the current shift.
          - `id` (string) **REQ** [maxLen=19, pattern=^[0-9]+$] — Specify the unique ID of the shift to assign as the current shift.
          type: null — Indicates that no current shift is assigned to the user.
    - `$shift_effective_from` (object) — Specify the date on which the upcoming shift assignment becomes effective.
      oneOf:
          type: string/date [pattern=([0-9]{4})-([0-9]{2})-([0-9]{2})] — Represents the date on which the upcoming shift assignment becomes effective.
          type: null — Indicates that no upcoming shift effective date is set.
    - `date_format` (string) [enum=[49 values]] — Specify the user's preferred date format for displaying date values.
    - `decimal_separator` (string) [enum=['Comma', 'Period']] — Specify the user's preferred decimal separator character for displaying numerical values.
    - `email` (string) [maxLen=100, pattern=^[\+\-\p{L}\p{M}\p{N}_]([\p{L}\p{M}\p{N}!#$%&'*+\-\/=?^_`{|}~.]*)@(?=.{4,256}$)(([\p{L}\p{N}\p{M}]+)(([\-_]*[\p{L}\p{M}\p{N}])*)[.])+[\p{L}\p{M}]{2,22}$] — Specify the email address for the user's account.
    - `first_name` (string) [maxLen=50] — Specify the user's first name.
    - `full_name` (string) [maxLen=100, readOnly] — Specify the user's full name.
    - `id` (string) [maxLen=19, readOnly] — Represents the unique identifier of the user record.
    - `last_name` (object) — Specify the user's last name. Set to null if no last name is to be stored.
      oneOf:
          type: string [maxLen=50] — Represents the last name to set for the user.
          type: null — Indicates that the last name should be cleared.
    - `profile` (object) — Specify the profile to assign to the user, including the profile's unique identifier and display name.
      - `name` (string) **REQ** [maxLen=50] — Specify the display name of the profile to assign to the user.
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Specify the unique ID of the profile to assign to the user.
    - `role` (object) — Specify the role to assign to the user, including the role's unique identifier and display name.
      - `name` (string) **REQ** [maxLen=200] — Specify the display name of the role to assign to the user.
      - `id` (string) **REQ** [maxLen=19] — Specify the unique ID of the role to assign to the user.
    - `status` (string) [enum=['active', 'inactive']] — Specify the status of the user account.
    - `alias` (object) — Specify an alias or short name for the user. Set to null to remove an existing alias.
      oneOf:
          type: string [maxLen=50] — Represents the alias or short name to assign to the user.
          type: null — Indicates that no alias is set for the user.
    - `locale` (string) [enum=[28 values]] — Specify the locale for the user.
    - `phone` (string) [maxLen=30, nullable] — Specify the user's phone number. Set to null to clear an existing phone number.
    - `mobile` (string) [maxLen=30, nullable] — Specify the user's mobile phone number. Set to null to clear an existing mobile number.
    - `city` (object) — Specify the city for the user's address. Set to null to clear an existing city value.
      oneOf:
          type: string [maxLen=100] — Represents the city value to set for the user.
          type: null — Indicates that the city value should be cleared.
    - `country` (object) — Specify the country for the user's address. Set to null to clear an existing country value.
      oneOf:
          type: string [maxLen=100] — Represents the country value to set for the user.
          type: null — Indicates that the country value should be cleared.
    - `dob` (object) — Specify the user's date of birth in YYYY-MM-DD format. Set to null to clear an existing date of birth.
      oneOf:
          type: string/date — Represents the date of birth value in YYYY-MM-DD format to set for the user.
          type: null — Indicates that the date of birth should be cleared.
    - `fax` (object) — Specify the user's fax number. Set to null to clear an existing fax number.
      oneOf:
          type: string [maxLen=30] — Represents the fax number to set for the user.
          type: null — Indicates that the fax number should be cleared.
    - `number_separator` (string) [enum=['Comma', 'Period', 'Space', 'comma', 'period', 'space']] — Specify the character to use as a separator when formatting numbers for the user. This field is case-insensitive.
    - `state` (object) — Specify the state or province for the user's address. Set to null to clear an existing state value.
      oneOf:
          type: string [maxLen=100] — Represents the state or province to set for the user.
          type: null — Indicates that the state value should be cleared.
    - `street` (object) — Specify the street address for the user. Set to null to clear an existing street address.
      oneOf:
          type: string [maxLen=250] — Represents the street address to set for the user.
          type: null — Indicates that the street address should be cleared.
    - `time_format` (string) [enum=['HH:mm', 'hh:mm a']] — Specify the time format to use for displaying time values for the user.
    - `website` (object) — Specify the user's website URL. Set to null to clear an existing website URL.
      oneOf:
          type: string [maxLen=250, pattern=^(http:\/\/www.|https:\/\/www.|ftp:\/\/www.|www.|http:\/\/|https:\/\/|ftp:\/\/|){1}[^\x00-\x19\x22-\x27\x2A-\x2C\x2E-\x2F\x3A-\x3F\x5B-\x5E\x60\x7B\x7D-\x7F]+(\.[^\x00-\x19\x22\x24-\x2C\x2E-\x2F\x3C\x3E\x40\x5B-\x5E\x60\x7B\x7D-\x7F]+)+([\/\?].*)*$] — Represents the website URL to set for the user.
          type: null — Indicates that the website URL should be cleared.
    - `zip` (object) — Specify the user's postal code or ZIP code. Set to null to clear an existing postal code.
      oneOf:
          type: string [maxLen=30] — Represents the postal code or ZIP code to set for the user.
          type: null — Indicates that the postal code should be cleared.
    - `name_format__s` (string) [enum=[6 values]] — Specify the format to use when displaying the user's name.
    - `language` (string) [enum=[228 values]] — Specify the preferred language for the user. This value can be updated only by the user themselves.
    - `country_locale` (string) [enum=[247 values]] — Specify the locale associated with the user's country.
    - `image_link` (string) [maxLen=100] — Specify the URL of the user's profile image from the Identity and Access Management (IAM) system.
    - `sort_order_preference__s` (string) [enum=['First Name,Last Name', 'Last Name,First Name']] — Specify the user's preferred sort order for displaying records.
    - `Reporting_To` (object) — Specify the user to whom this user reports. Set to null to remove the reporting relationship. Refer to the [Get Users](users.yaml#$.paths./users.get) endpoint for valid user IDs.
      oneOf:
          - `name` (string) **REQ** [maxLen=100] — Specify the full name of the user to assign as the reporting manager.
          - `id` (string) **REQ** [maxLen=19] — Specify the unique ID of the user to assign as the reporting manager.
          type: null — Indicates that no reporting manager is assigned to this user.
    - `share_among_subordinates` (boolean) — Specify whether the user's records should be shared with their subordinates.\n\nPossible values:\ntrue - Records are shared with subordinates.\nfalse - Records are not shared with subordinates.
    - `time_zone` (string) [maxLen=150] — Specify the time zone for the user. This value can be updated only by the user themselves.
    - `distance_preference__s` (string) [enum=['Kilometers', 'Miles']] — Specify the user's preferred unit of measurement for displaying distance values.
    - `default_tab_group` (integer/int32) — Specify the default tab group for the user, determining which group of tabs is shown upon login.
    - `signature` (string) [maxLen=200, nullable] — Specify the email signature for the user. Set to null to remove an existing signature.
    - `customize_info` (object) — Specify user interface customization preferences for the user's account.
      - `notes_desc` (boolean) — Specify whether notes should be displayed in descending order for the user.\n\nPossible values:\ntrue - Notes are displayed in descending order.\nfalse - Notes are not displayed in descending order.
      - `show_left_panel` (boolean) — Specify whether the left panel is displayed in the user interface.\n\nPossible values:\ntrue - The left panel is shown.\nfalse - The left panel is hidden.
      - `show_detail_view` (boolean) — Specify whether the detail view panel is displayed for the user.\n\nPossible values:\ntrue - The detail view panel is displayed.\nfalse - The detail view panel is not displayed.
      additionalProperties: any
    - `theme` (object) — Specify the theme configuration for the user's CRM interface, including color and display settings for the background, screen, header, normal tab, and selected tab elements.
      - `normal_tab` (object) — Specify the theme settings for the normal (unselected) tab in the user's CRM interface, including background color and font color.
        - `background` (string/hex-color) — Specify the background color for the normal tab in the user's theme.
        - `font_color` (string/hex-color) — Specify the font color for the normal tab in the user's theme.
      - `selected_tab` (object) — Specify the theme settings for the selected tab in the user's CRM interface, including background color and font color.
        - `background` (string/hex-color) — Specify the background color for the selected tab in the user's theme.
        - `font_color` (string/hex-color) — Specify the font color for the selected tab in the user's theme.
      - `header` (object) — Specify the theme settings for the header area of the user's CRM interface, including background color and font color.
        - `background` (string/hex-color) — Specify the background color for the header area of the user's theme.
        - `font_color` (string/hex-color) — Specify the font color for the header area of the user's theme.
      - `new_background` (string/hex-color) [nullable] — Specify the updated background color for the user's theme.
      - `background` (string/hex-color) — Specify the background color for the user's theme.
      - `screen` (string) [enum=['fixed']] — Specify the screen type or layout for the user's CRM interface.
      - `type` (string) [enum=['default', 'custom']] — Specify the type of theme to apply to the user's CRM interface.
    additionalProperties: any

**Responses:**

- **201**: Returns the result of the user creation request, including the unique ID of the newly created user. [application/json]
    > Represents the response payload schema returned upon successful user creation. Contains the `users` array with the result objects.
    - `users` (array of object) [maxItems=1] — Contains the result of the user creation request, including the status, response code, confirmation message, and the unique ID of the newly created user.
      - `code` (string) [enum=['SUCCESS']] — Indicates the result code for the user creation request. Possible values: `SUCCESS`.
      - `details` (object) — Contains additional information about the created user, including the unique ID assigned to the user record in Zoho CRM.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user record created in Zoho CRM.
      - `message` (string) [enum=['User added']] — Indicates the confirmation message returned upon successful user creation. Possible values: `User added`.
      - `status` (string) [enum=['success']] — Indicates the overall status of the user creation request. Possible values: `success`.

- **400**: The request contains invalid, missing, or unsupported field values.
**Resolution:** The invalid field details are available in the `users[].details` object. The request must be corrected and resubmitted. [application/json]
    > Represents the response payload schema returned when a user creation request fails. Contains the `users` array with error result objects.
    - `users` (array of object) [maxItems=1] — Contains one or more error objects returned when the user creation request fails validation or cannot be processed.
      oneOf:
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error classification code returned when a user creation request contains invalid data.
Possible values: INVALID_DATA.
          - `details` (object) — Contains additional context about the validation error, including the affected field API name, JSON path, maximum permitted length, expected data type, and applicable date range constraints.
            - `api_name` (string) [maxLen=100] — Represents the API name of the request field that triggered the validation error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the request field that triggered the validation error.
            - `maximum_length` (integer/int32) — Represents the maximum number of characters permitted for the field that triggered the validation error.
            - `expected_data_type` (string) [maxLen=100] — Represents the data type that was expected for the field that triggered the validation error.
            - `range` (object) — Contains the acceptable date range for the field that triggered the validation error, expressed as a start date and an end date.
              - `from` (string/date) — Represents the start date of the acceptable date range for the field that triggered the validation error.
              - `to` (string/date) — Represents the end date of the acceptable date range for the field that triggered the validation error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[14 values]] — Represents the message describing the nature of the validation error encountered during user creation.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the user creation request. Possible values: `error`.
          - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Indicates the error code identifying a dependent field value mismatch condition. Possible values: `DEPENDENT_MISMATCH`.
          - `details` (object) — Contains additional context about the dependent field mismatch error, including the API name and JSON path of the offending field and information about the field it depends on.
            - `dependee` (object) — Contains the API name and JSON path of the field upon which the erroring field depends.
              - `api_name` (string) [maxLen=100] — Represents the API name of the field upon which the erroring field depends.
              - `json_path` (string) [maxLen=200] — Represents the JSON path of the field upon which the erroring field depends.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with the dependent field mismatch error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with the dependent field mismatch error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['Dependent Field value should not be null']] — Indicates the error message returned when a dependent field value is missing. Possible values: `Dependent Field value should not be null`.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the user creation request. Possible values: `error`.
          - `code` (string) **REQ** [enum=['UNAPPROVABLE']] — Indicates the error code returned when the user type cannot be approved for creation. Possible values: `UNAPPROVABLE`.
          - `details` (object) — Contains additional context about the unapprovable user creation error.
          - `message` (string) **REQ** [enum=[2 values]] — Indicates the error message returned when a user cannot be added from the CRM interface for certain account types. Possible values: `Cannot add user for ZohoOne account from CRM. Kindly add user through ZohoOne`, `Cannot add user for CRMPlus account from CRM. Kindly add user through CRMPlus`.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the user creation request. Possible values: `error`.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Indicates the error code identifying an operation that is not permitted. Possible values: `NOT_ALLOWED`.
          - `details` (object) — Contains additional context about the not-allowed error, including the API name and JSON path of the field that triggered the restriction.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field that triggered the not-allowed error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field that triggered the not-allowed error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[5 values]] — Indicates the error message returned when a user creation attempt is not allowed for the specified user type or organization context. Possible values: `You cannot create user in a sandbox org`, `Support user cannot be added`, `System user cannot be added`, `the id given seems to be already deleted`, `current shift and next shift should not be same`.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the user creation request. Possible values: `error`.
          - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Indicates the error code returned when the requested operation is not supported for the user type. Possible values: `NOT_SUPPORTED`.
          - `details` (object) — Contains additional context about the not-supported error, including the API name and JSON path of the field that triggered the restriction.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field that triggered the not-supported error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field that triggered the not-supported error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[2 values]] — Indicates the error message returned when an update to a restricted field is attempted through the API. Possible values: `type__s is cannot be updated by api`, `Created by & Modified by fields cannot be updated by api`.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the user creation request. Possible values: `error`.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Indicates the error code returned when a required field is missing in the request. Possible values: `MANDATORY_NOT_FOUND`.
          - `details` (object) — Contains additional context about the mandatory field missing error.
          - `message` (string) **REQ** [enum=['Company Name is required']] — Indicates the error message returned when a required company detail is missing from the request. Possible values: `Company Name is required`.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the user creation request. Possible values: `error`.
          - `code` (string) **REQ** [enum=['LICENSE_LIMIT_EXCEEDED']] — Indicates the error code returned when the request exceeds the account license limit for users. Possible values: `LICENSE_LIMIT_EXCEEDED`.
          - `details` (object) — Contains additional context about the license limit exceeded error.
          - `message` (string) **REQ** [enum=[2 values]] — Indicates the error message returned when the license limit for users is exceeded. Possible values: `Request exceeds your license limit. Need to upgrade in order to add a user`, `Request exceeds your license limit. Need to upgrade in order to add a team user`.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the user creation request. Possible values: `error`.
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Indicates the error code returned when a duplicate user email address is detected. Possible values: `DUPLICATE_DATA`.
          - `details` (object) — Contains additional context about the duplicate data error.
          - `message` (string) **REQ** [enum=['Failed to add user since same email id is already present']] — Indicates the error message returned when a user with the same email address already exists. Possible values: `Failed to add user since same email id is already present`.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the user creation request. Possible values: `error`.
          - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Indicates the error code returned when the request itself is invalid or cannot be processed. Possible values: `INVALID_REQUEST`.
          - `details` (object) — Contains additional context about the invalid request error, including the API name and JSON path of the offending field.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with the invalid request error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with the invalid request error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[3 values]] — Indicates the error message returned for an invalid user creation request. Possible values: `User cannot be added as the user has already reached the maximum invitation limit`, `Invalid current shift id`, `Invalid next shift id`.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the user creation request. Possible values: `error`.
          - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Indicates the error code returned when a required CRM feature is not enabled for the organization. Possible values: `FEATURE_NOT_ENABLED`.
          - `details` (object) — Contains additional context about the feature not enabled error.
          - `message` (string) **REQ** [enum=['ReportingTo Feature is not enabled']] — Indicates the error message returned when the Reporting To feature is not enabled in the CRM organization. Possible values: `ReportingTo Feature is not enabled`.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the user creation request. Possible values: `error`.
          - `code` (string) **REQ** [enum=['MAPPING_MISMATCH']] — Indicates the error code identifying a mapping mismatch condition. Possible values: `MAPPING_MISMATCH`.
          - `details` (object) — Contains additional context about the mapping mismatch error, including the API name and JSON path of the offending field and the corresponding mapped field information.
            - `mapped_field` (object) — Contains the API name and JSON path of the field that is mapped to the conflicting field in the mapping mismatch error.
              - `api_name` (string) [maxLen=100] — Represents the API name of the mapped field involved in the mapping mismatch error.
              - `json_path` (string) [maxLen=200] — Represents the JSON path of the mapped field involved in the mapping mismatch error.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with the mapping mismatch error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with the mapping mismatch error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['the number separator and decimal separator values should not be same']] — Indicates the error message returned when a mapping mismatch is detected. Possible values: `the number separator and decimal separator values should not be same`.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the user creation request. Possible values: `error`.
          - `code` (string) **REQ** [enum=['ALREADY_USED']] — Indicates the error code identifying a value that has already been used. Possible values: `ALREADY_USED`.
          - `details` (object) — Contains additional context about the already-used value error, including the API name and JSON path of the offending field and the location where the value already exists.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with the already-used value error.
            - `exists_in` (object) — Contains the API name and JSON path identifying the location where the conflicting value already exists.
              - `api_name` (string) [maxLen=100] — Represents the API name of the field where the conflicting value already exists.
              - `json_path` (string) [maxLen=200] — Represents the JSON path of the field where the conflicting value already exists.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with the already-used value error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['current shift and next shift id cannot be the same']] — Indicates the error message returned when a duplicate shift assignment is detected. Possible values: `current shift and next shift id cannot be the same`.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the user creation request. Possible values: `error`.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Indicates the error code identifying an operation that is not permitted. Possible values: `NOT_ALLOWED`.
          - `details` (object) — Contains additional context about the not-allowed error, including the API name and JSON path of the field that triggered the restriction.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field that triggered the not-allowed error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field that triggered the not-allowed error.
          - `message` (string) **REQ** [enum=['The specified user type is not allowed']] — Indicates the error message returned when a disallowed user type is specified. Possible values: `The specified user type is not allowed`.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the user creation request. Possible values: `error`.
    additionalProperties: any

- **403**: Permission denied to create a user.
**Resolution:** The Zoho CRM administrator must grant the Manage Users permission to the requesting user profile. [application/json]
    > Represents the response payload schema returned when the requesting user does not have permission to create a user.
    - `code` (string) [enum=['NO_PERMISSION', 'PERMISSION_DENIED']] — Indicates the error code returned when the requesting user lacks permission to create a user. Possible values: `NO_PERMISSION`, `PERMISSION_DENIED`.
    - `details` (object) — Contains additional context about the permission denied error, including the list of required permissions that are missing.
      - `permissions` (array of string) [maxItems=1] — Contains the list of Zoho CRM permission identifiers required for this operation that are absent from the requesting user profile.
        items: [enum=['Crm_Implied_Manage_Users']]
    - `message` (string) [enum=['permission denied']] — Indicates the error message returned when permission to create a user is denied. Possible values: `permission denied`.
    - `status` (string) [enum=['error']] — Indicates the overall response status when access is denied. Possible values: `error`.

**Scopes:** ZohoCRM.users.CREATE

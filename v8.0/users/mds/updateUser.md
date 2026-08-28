# PUT /users
**Operation:** `updateUser` — Update users
> To update the details of one or more users in your Zoho CRM organization. The request must include a users array with up to 10 user records, each identified by a unique user ID. You can update user profile settings, role assignments, locale preferences, and other account details.

**Request Body** — application/json
> The request body must contain a users array. You can include a maximum of 10 objects per request.
  > Contains the list of user objects to update in this request.
  - `users` (array of object `UserDetails`) [maxItems=10] **REQ** — Specify the list of user records to update. Each object in the array represents a single user whose details you want to modify.
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

- **200**: Returns the update result for the user records processed in the request. [application/json]
    > Contains the list of user update result objects returned in the 200 response.
    - `users` (array of object) [maxItems=10] — Represents the list of user update result objects returned after a successful request.
      - `code` (string) [enum=['SUCCESS']] — Represents the response code indicating a successful update. Possible values: **SUCCESS**.
      - `details` (object) — Contains the details of the updated user record.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the updated user.
      - `message` (string) [enum=['User updated']] — Represents the response message confirming the outcome of the update operation. Possible values: **User updated**.
      - `status` (string) [enum=['success']] — Represents the response status indicating success. Possible values: **success**.

- **400**: Indicates that the request could not be processed due to validation errors or constraint violations in the input data. [application/json]
    > Contains the list of error result objects returned in the 400 response when user update fails.
    - `users` (array of object) [maxItems=1] — Represents the error result object returned when the user update request fails validation or cannot be processed.
      oneOf:
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this error variant. Possible values: **INVALID_DATA**.
          - `details` (object) — Contains additional details about the error, including the field API name and JSON path.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with this error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with this error.
            - `maximum_length` (integer/int32) — Represents the maximum character length allowed for the field.
            - `expected_data_type` (string) [maxLen=100] — Represents the expected data type for the field that caused the error.
            - `resource_path_index` (integer/int32) — Represents the index position of the resource path in the array for the field that caused the error.
            - `range` (object) — Contains the valid date range.
              - `from` (string/date) — Represents the start date of the valid date range.
              - `to` (string/date) — Represents the end date of the valid date range.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[19 values]] — Indicates the error message describing the invalid data condition. Possible values: **invalid data**, **INVALID_DATA**, **the id given seems to be invalid**,
**Special Characters Found**, 
**Pattern not matched**, 
**invalid id in reporting to or roles provided**, 
**the number separator and decimal separator values should not be same**, 
**Invalid data. Valid values are Comma/Period/Space (Not case-sensitive)**, 
**Invalid data. Valid values are Comma/Period (Not case-sensitive)**, 
**Give a proper time zone value**, 
**Reporting manager should be from parent roles or from the same role to which the current user belongs**, 
**Valid name format should be given**, 
**Valid sort order preference should be given**, **Give a proper language code**, 
**the reporting manager must be superior in reporting hierarchy**,
 **Effective from should be greater than current date**, 
**Effective from should be less than 6 months**, **Shift effective from date should be greater than Current Shift date**, 
**User is not confirmed so customization information cannot be updated**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code for this error variant. Possible values: **DEPENDENT_MISMATCH**.
          - `details` (object) — Contains additional details about the error, including the field API name, JSON path, and dependee field information.
            - `dependee` (object) — Contains details about the dependee field that caused the mismatch.
              - `api_name` (string) [maxLen=100] — Represents the API name of the dependee field.
              - `json_path` (string) [maxLen=200] — Represents the JSON path of the dependee field.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with this error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with this error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['Dependent Field value should not be null']] — Represents the error message. Possible values: **Dependent Field value should not be null**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this error variant. Possible values: **NOT_ALLOWED**.
          - `details` (object) — Contains additional details about the error, including the field API name, JSON path, user ID, and resource path index.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with this error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with this error.
            - `id` (string) [maxLen=19] — Represents the unique ID of the user associated with this error.
            - `resource_path_index` (integer/int32) — Represents the index position of the resource path in the array for the field that caused the error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[15 values]] — Indicates the error message when an operation is not allowed. Possible values: **the id given seems to be invalid**, **Support user cannot be activated**, **System user cannot be activated**, **Support user cannot be deactivated**, **System user cannot be deactivated**, **Cannot update the user details of support user**, **System Profile cannot be assigned to other users**, **You are not allowed to perform this operation.**, **Cannot update the name_format__s of another User**, **Non subordinate users cannot be updated**, **You cannot perform this action over a closed/deleted user**, **Support user cannot be added**, **Cannot update the sort_order_preference__s of another User**, **Cannot update the user details of System User**, **current shift and next shift should not be same**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this error variant. Possible values: **MANDATORY_NOT_FOUND**.
          - `details` (object) — Contains additional details about the error, including the field API name and JSON path.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with this error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with this error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['required field not found', 'Company Name is required']] — Represents the error message when a required field is not found. Possible values: **required field not found**, **Company Name is required**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['CANNOT_UPDATE_DELETED_USER']] — Represents the error code for this error variant. Possible values: **CANNOT_UPDATE_DELETED_USER**.
          - `details` (object) — Contains additional details about the error.
          - `message` (string) **REQ** [enum=['Deleted user cannot be updated']] — Represents the error message. Possible values: **Deleted user cannot be updated**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['EMAIL_UPDATE_NOT_ALOWED']] — Represents the error code for this error variant. Possible values: **EMAIL_UPDATE_NOT_ALOWED**.
          - `details` (object) — Contains additional details about the error, including the field API name.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with this error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[2 values]] — Indicates the error message when an email update is not allowed. Possible values: **Crm Plus account is not allowed to edit the email while updating the user info**, **Cannot update email of a confirmed CRM User**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Represents the error code for this error variant. Possible values: **INVALID_REQUEST**.
          - `details` (object) — Contains additional details about the error, including the field API name, user ID, and JSON path.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with this error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with this error.
            - `id` (string) [maxLen=19] — Represents the unique ID of the user associated with this error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[6 values]] — Indicates the error message for an invalid request. Possible values: **You cannot perform this action over logged in user**, **invalid request**, **Reinvite is not allowed for a confirmed user**, **Primary Contact cannot be deactivated**, **Invalid current shift id**, **Invalid next shift id**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code for this error variant. Possible values: **DUPLICATE_DATA**.
          - `details` (object) — Contains additional details about the error, including the field API name, the duplicate user ID, and JSON path.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with this error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with this error.
            - `id` (string) [maxLen=19] — Represents the unique ID of the duplicate user.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['User with same email id is already in CRM Plus', 'Email already exists']] — Represents the error message when duplicate data is found. Possible values: **User with same email id is already in CRM Plus**, **Email already exists**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['ID_ALREADY_DEACTIVATED']] — Represents the error code for this error variant. Possible values: **ID_ALREADY_DEACTIVATED**.
          - `details` (object) — Contains additional details about the error, including the field API name and user ID.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with this error.
            - `id` (string) [maxLen=19] — Represents the unique ID of the user.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['User is already deactivated']] — Represents the error message. Possible values: **User is already deactivated**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the error code for this error variant. Possible values: **NOT_SUPPORTED**.
          - `details` (object) — Contains additional details about the error, including the field API name and JSON path.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with this error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with this error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[2 values]] — Indicates the error message when the operation is not supported. Possible values: **type__s is cannot be updated by api**, **Created by & Modified by fields cannot be updated by api**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['UNAPPROVABLE']] — Represents the error code for this error variant. Possible values: **UNAPPROVABLE**.
          - `details` (object) — Contains additional details about the error.
          - `message` (string) **REQ** [enum=['You cannot update user in a sandbox org']] — Represents the error message. Possible values: **You cannot update user in a sandbox org**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['LICENSE_LIMIT_EXCEEDED']] — Represents the error code for this error variant. Possible values: **LICENSE_LIMIT_EXCEEDED**.
          - `details` (object) — Contains additional details about the error.
          - `message` (string) **REQ** [enum=[2 values]] — Indicates the error message when the license limit is exceeded. Possible values: **You are trying to activate more mail addon which exceeds your license limit. If you want to activate mail addon for additional users, please upgrade your license**, **License Limit is Exceeded**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['AUTHORIZATION_FAILED']] — Represents the error code for this error variant. Possible values: **AUTHORIZATION_FAILED**.
          - `details` (object) — Contains additional details about the error.
          - `message` (string) **REQ** [enum=[2 values]] — Indicates the error message when the user lacks authorization. Possible values: **Either trial is expired or user does not have sufficient privilege to perform this action**, **Either trial is expired or user does not have sufficient privilege to perform this action**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['FEATURE_NOT_AVAILABLE']] — Represents the error code for this error variant. Possible values: **FEATURE_NOT_AVAILABLE**.
          - `details` (object) — Contains additional details about the error.
          - `message` (string) **REQ** [enum=['Share among Subordinates Feature is not available']] — Represents the error message. Possible values: **Share among Subordinates Feature is not available**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['CONFLICTING_DATA_FOUND']] — Represents the error code for this error variant. Possible values: **CONFLICTING_DATA_FOUND**.
          - `details` (object) — Contains additional details about the error, including the field API name and JSON path.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with this error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with this error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[2 values]] — Indicates the error message when conflicting reporting manager data is found. Possible values: **the user must be updated with new eligible reporting manager because of changing user role**, **the user must be updated with new eligible reporting manager and the subordinates who are going to report to a user in a role below them, because of new role change are need to transfer to new eligible reporting manager**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['ID_ALREADY_ACTIVE']] — Represents the error code for this error variant. Possible values: **ID_ALREADY_ACTIVE**.
          - `details` (object) — Contains additional details about the error, including the user ID and JSON path.
            - `id` (string) [maxLen=19] — Represents the unique ID of the user.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with this error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['User is already active']] — Represents the error message. Possible values: **User is already active**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['MAPPING_MISMATCH']] — Represents the error code for this error variant. Possible values: **MAPPING_MISMATCH**.
          - `details` (object) — Contains additional details about the error, including the field API name, JSON path, and mapped field information.
            - `mapped_field` (object) — Contains information about the mapped field associated with this error.
              - `api_name` (string) [maxLen=100] — Represents the API name of the mapped field.
              - `json_path` (string) [maxLen=200] — Represents the JSON path of the mapped field.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with this error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with this error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['the number separator and decimal separator values should not be same']] — Represents the error message. Possible values: **the number separator and decimal separator values should not be same**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for this error variant. Possible values: **FEATURE_NOT_ENABLED**.
          - `details` (object) — Contains additional details about the error.
          - `message` (string) **REQ** [enum=[2 values]] — Indicates the error message when a required feature is not enabled. Possible values: **ReportingTo Feature is not enabled**, **User is not confirmed so customization information cannot be updated**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['ALREADY_USED']] — Represents the error code for this error variant. Possible values: **ALREADY_USED**.
          - `details` (object) — Contains additional details about the error, including field identifiers and information about where the value already exists.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with this error.
            - `exists_in` (object) — Contains information about the location where the value already exists.
              - `api_name` (string) [maxLen=100] — Represents the API name of the field where the value already exists.
              - `json_path` (string) [maxLen=200] — Represents the JSON path of the field where the value already exists.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with this error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['Current shift and next shift id cannot be the same']] — Represents the error message. Possible values: **Current shift and next shift id cannot be the same**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this error variant. Possible values: **NOT_ALLOWED**.
          - `details` (object) — Contains additional details about the error, including the field API name and JSON path.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field associated with this error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path of the field associated with this error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['Digital Employee cannot be Deleted / Deactivated / Activated']] — Represents the error message. Possible values: **Digital Employee cannot be Deleted / Deactivated / Activated**.
          - `status` (string) **REQ** [enum=['error']] — Represents the response status. Possible values: **error**.
    additionalProperties: any

- **403**: Indicates that the requesting user does not have the required Zoho CRM profile permissions to update users. [application/json]
    > Represents the permission denied response schema returned when the user lacks the required CRM permissions to update a user.
    - `code` (string) [enum=['NO_PERMISSION', 'PERMISSION_DENIED']] — Represents the error code for the permission denied response. Possible values: **NO_PERMISSION**, **PERMISSION_DENIED**.
    - `details` (object) — Contains additional details about the permission error, including the list of missing permissions.
      - `permissions` (array of string) [maxItems=1] — Represents the list of permissions that are missing for the requested action.
        items: [enum=['Crm_Implied_Manage_Users']]
    - `message` (string) [enum=['permission denied']] — Represents the error message. Possible values: **permission denied**.
    - `status` (string) [enum=['error']] — Represents the response status. Possible values: **error**.

**Scopes:** ZohoCRM.users.UPDATE

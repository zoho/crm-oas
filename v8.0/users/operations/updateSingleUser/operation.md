# PUT /users/{user}
**Operation:** `updateSingleUser` — Update a single user by user ID
> To update the details of a specific user in your Zoho CRM organization by user ID.

**Parameters:**
- `user` (path, string, required) [maxLen=19]: Specify the unique ID of the user to retrieve, update, or delete.

**Request Body** — application/json
> The request body must contain a users array with one object.
  > Represents the structure of the user update request body. Contains a users array with the details of the user to update.
  - `users` (array of object `UserDetails`) [maxItems=1] **REQ** — Specify the user details to update. Only one user record can be submitted per request.
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

- **200**: Returns the result of the user update operation, including the status and unique ID of the updated user. [application/json]
    > Represents the structure of the user update success response. Contains a users array with the outcome of the update operation.
    - `users` (array of object) [maxItems=10] — Represents the list of outcome objects returned after processing the user update request. Each element reports the result status for the updated user record.
      - `code` (string) [enum=['SUCCESS']] — Indicates the API-level result code for the user update operation.

Possible values:
SUCCESS - The user record updates successfully.
      - `details` (object) — Represents an object containing identifying information about the updated user. Includes the unique ID of the user.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique system-generated identifier of the updated user.
      - `message` (string) [enum=['User updated']] — Indicates the message describing the outcome of the user update operation.

Possible values:
User updated - The user record updates successfully.
      - `status` (string) [enum=['success']] — Indicates the overall processing status of the user update request.

Possible values:
success - The request processes and the user record updates without errors.

- **400**: The request could not be processed due to a validation or business-rule failure.
**Resolution:** Review the error details in the response to identify and correct the invalid field values before resubmitting the request. [application/json]
    > Represents the structure of the user update error response. Contains a users array with details of the validation or processing failure.
    - `users` (array of object) [maxItems=1] — Represents the list of error objects returned when the user update request could not be processed. Each element describes the specific error encountered.
      oneOf:
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Indicates the specific error classification returned when the request payload fails validation.

Possible values:
INVALID_DATA - The submitted field value does not match the expected type or format.
          - `details` (object) — Contains structured diagnostic information about the validation failure, including the affected field API name, JSON path, data type expectations, length constraints, resource path index, and applicable date range.
            - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that triggered the INVALID_DATA error, enabling callers to identify and correct the offending field in the request payload.
            - `json_path` (string) [maxLen=200] — Indicates the path within the request body that locates the field responsible for the validation failure, useful for pinpointing errors in nested or array structures.
            - `maximum_length` (integer/int32) — Indicates the maximum number of characters or digits permitted for the field that failed validation, giving callers the upper bound needed to correct the submitted value.
            - `expected_data_type` (string) [maxLen=100] — Indicates the data type that the API expected to receive for the failing field, allowing callers to supply a correctly typed value in a corrected request.
            - `resource_path_index` (integer/int32) — Indicates the zero-based index position within an array in the request body that identifies which element caused the validation failure.
            - `range` (object) — Contains the permissible date interval for a date-type field that failed validation, expressed as a start date and an end date defining the inclusive bounds that the submitted value must fall within.
              - `from` (string/date) — Represents the earliest permissible date of the valid range for the field that triggered the validation error.
              - `to` (string/date) — Represents the latest permissible date of the valid range for the field that triggered the validation error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[17 values]] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Indicates the error code for this failure type.

Possible values:
[error-specific code] - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
            - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that caused the error, enabling callers to identify the offending field in the request payload.
            - `json_path` (string) [maxLen=200] — Indicates the path within the request body that locates the field responsible for the error.
            - `id` (string) [maxLen=19] — Represents the unique identifier of the user associated with this error condition.
            - `resource_path_index` (integer/int32) — Indicates the zero-based index position within an array in the request body that identifies which element caused the validation failure.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[15 values]] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['CANNOT_UPDATE_DELETED_USER']] — Indicates the error code for this failure type.

Possible values:
[error-specific code] - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
          - `message` (string) **REQ** [enum=['Deleted user cannot be updated']] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['EMAIL_UPDATE_NOT_ALOWED']] — Indicates the error code for this failure type.

Possible values:
[error-specific code] - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
            - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that caused the error, enabling callers to identify the offending field in the request payload.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[2 values]] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Indicates the error code for this failure type.

Possible values:
[error-specific code] - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
            - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that caused the error, enabling callers to identify the offending field in the request payload.
            - `json_path` (string) [maxLen=200] — Indicates the path within the request body that locates the field responsible for the error.
            - `id` (string) [maxLen=19] — Represents the unique identifier of the user associated with this error condition.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[6 values]] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Indicates the error code for this failure type.

Possible values:
[error-specific code] - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
            - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that caused the error, enabling callers to identify the offending field in the request payload.
            - `json_path` (string) [maxLen=200] — Indicates the path within the request body that locates the field responsible for the error.
            - `id` (string) [maxLen=19] — Represents the unique identifier of the user associated with this error condition.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['User with same email id is already in CRM Plus', 'Email already exists']] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['ID_ALREADY_DEACTIVATED']] — Indicates the error code for this failure type.

Possible values:
[error-specific code] - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
            - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that caused the error, enabling callers to identify the offending field in the request payload.
            - `id` (string) [maxLen=19] — Represents the unique identifier of the user associated with this error condition.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['User is already deactivated']] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Indicates the error code for this failure type.

Possible values:
[error-specific code] - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
            - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that caused the error, enabling callers to identify the offending field in the request payload.
            - `json_path` (string) [maxLen=200] — Indicates the path within the request body that locates the field responsible for the error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[2 values]] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['UNAPPROVABLE']] — Indicates the error code for this failure type.

Possible values:
[error-specific code] - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
          - `message` (string) **REQ** [enum=[3 values]] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['LICENSE_LIMIT_EXCEEDED']] — Indicates the error code for this failure type.

Possible values:
[error-specific code] - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
          - `message` (string) **REQ** [enum=[2 values]] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['AUTHORIZATION_FAILED']] — Indicates the error code for this failure type.

Possible values:
AUTHORIZATION_FAILED - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
          - `message` (string) **REQ** [enum=[2 values]] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['FEATURE_NOT_AVAILABLE']] — Indicates the error code for this failure type.

Possible values:
FEATURE_NOT_AVAILABLE - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
          - `message` (string) **REQ** [enum=['Share among Subordinates Feature is not available']] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['CONFLICTING_DATA_FOUND']] — Indicates the error code for this failure type.

Possible values:
CONFLICTING_DATA_FOUND - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
            - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that caused the error, enabling callers to identify the offending field in the request payload.
            - `json_path` (string) [maxLen=200] — Indicates the path within the request body that locates the field responsible for the error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=[2 values]] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['ID_ALREADY_ACTIVE']] — Indicates the error code for this failure type.

Possible values:
ID_ALREADY_ACTIVE - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
            - `id` (string) [maxLen=19] — Represents the unique identifier of the user associated with this error condition.
            - `json_path` (string) [maxLen=200] — Indicates the path within the request body that locates the field responsible for the error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['User is already active']] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['MAPPING_MISMATCH']] — Indicates the error code for this failure type.

Possible values:
MAPPING_MISMATCH - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
            - `mapped_field` (object) — Contains the API name and JSON path of the field whose configuration conflicts with the submitted separator value.
              - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that caused the error, enabling callers to identify the offending field in the request payload.
              - `json_path` (string) [maxLen=200] — Indicates the path within the request body of the conflicting separator field.
            - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that caused the error, enabling callers to identify the offending field in the request payload.
            - `json_path` (string) [maxLen=200] — Indicates the path within the request body that locates the field responsible for the error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['the number separator and decimal separator values should not be same']] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Indicates the error code for this failure type.

Possible values:
FEATURE_NOT_ENABLED - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
          - `message` (string) **REQ** [enum=['ReportingTo Feature is not enabled']] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['ALREADY_USED']] — Indicates the error code for this failure type.

Possible values:
ALREADY_USED - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
            - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that caused the error, enabling callers to identify the offending field in the request payload.
            - `exists_in` (object) — Contains the location of the existing record that already uses the submitted value, identifying the source of the duplicate conflict.
              - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that caused the error, enabling callers to identify the offending field in the request payload.
              - `json_path` (string) [maxLen=200] — Indicates the path within the request body of the field where the conflicting value already exists.
            - `json_path` (string) [maxLen=200] — Indicates the path within the request body that locates the field responsible for the error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['Current shift and next shift id cannot be the same']] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Indicates the error code for this failure type.

Possible values:
DEPENDENT_MISMATCH - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
            - `dependee` (object) — Contains the API name and JSON path of the parent field on which the failing field depends.
              - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that caused the error, enabling callers to identify the offending field in the request payload.
              - `json_path` (string) [maxLen=200] — Indicates the path within the request body of the parent (dependee) field.
            - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that caused the error, enabling callers to identify the offending field in the request payload.
            - `json_path` (string) [maxLen=200] — Indicates the path within the request body that locates the field responsible for the error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['Dependent Field value should not be null']] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Indicates the error code for this failure type.

Possible values:
[error-specific code] - The error code returned when this specific validation failure occurs.
          - `details` (object) — Contains diagnostic information about the error, identifying the specific field or condition that caused the failure.
            - `api_name` (string) [maxLen=100] — Indicates the API name of the user field that caused the error, enabling callers to identify the offending field in the request payload.
            - `json_path` (string) [maxLen=200] — Indicates the path within the request body that locates the field responsible for the error.
            additionalProperties: any
          - `message` (string) **REQ** [enum=['Digital Employee cannot be Deleted / Deactivated / Activated']] — Indicates the error message describing the specific validation or processing failure that occurred.
          - `status` (string) **REQ** [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.
    additionalProperties: any

- **403**: Permission denied to update the user.
**Resolution:** The CRM administrator must grant the Manage Users permission to the requesting user's profile. [application/json]
    > Represents the error response body returned when the user update request is denied due to insufficient permissions.
    - `code` (string) [enum=['NO_PERMISSION', 'PERMISSION_DENIED']] — Indicates the error code for this failure type.

Possible values:
[error-specific code] - The error code returned when this specific validation failure occurs.
    - `details` (object) — Contains additional information about the permission denial, including the list of missing permissions.
      - `permissions` (array of string) [maxItems=1] — Indicates the list of CRM permissions that the requesting user's profile lacks for this operation.
        items: [enum=['Crm_Implied_Manage_Users']]
    - `message` (string) [enum=['permission denied']] — Indicates the error message describing the specific validation or processing failure that occurred.
    - `status` (string) [enum=['error']] — Indicates the processing status when this error occurs.

Possible values:
error - The request could not be processed due to a validation or business-rule failure.

**Scopes:** ZohoCRM.users.UPDATE

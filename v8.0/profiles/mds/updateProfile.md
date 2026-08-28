# PUT /settings/profiles/{id}
**Operation:** `updateProfile` — Specific Profile
> Replaces the name, description, and permission enablement for the profile identified by `{id}`. System profiles (Administrator, Standard) cannot be updated. See [Update Profile Permission](https://www.zoho.com/crm/developer/docs/api/v8/update-profile-permission.html).

**Parameters:**
- `id` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$]: Represents the unique identifier of the profile (64-bit integer represented as a string, 1-19 digits).

**Request Body** (required) — application/json
> Payload containing profile fields and permission enablement entries to update.
  > Request body for the profile update operation.
  - `profiles` (array of object) [maxItems=1] **REQ** — Specify a single-item JSON array containing the profile update payload.
    - `name` (string) [maxLen=50, nullable] — Specify the new name for the profile (up to 50 characters).
    - `description` (string) [maxLen=250, nullable] — Specify the new text description for the profile.
    - `permissions_details` (array of object) [maxItems=2000] — List of permission toggle entries to apply (up to 2000).
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — The unique identifier of the permission.
      - `enabled` (boolean) **REQ** — Desired enabled state for the permission.
**Possible values:**
`true` to enable, `false` to disable.

**Responses:**

- **200**: Profile updated successfully. [application/json]
    > Successful response for the profile update operation.
    - `profiles` (array of object) [maxItems=50] **REQ** — Update results for the profile (up to 50 entries).
      - `code` (string) **REQ** [enum=['SUCCESS']] — Operation result code. Possible values: `SUCCESS`.
      - `details` (object) **REQ** — Details object containing the ID of the updated profile.
        - `id` (string/int64) **REQ** — Unique identifier of the updated profile.
      - `status` (string) **REQ** [enum=['success']] — Operation result status. Possible values: `success`.
      - `message` (string) **REQ** [maxLen=500] — Human-readable message confirming the update result.

- **400**: Invalid update request. [application/json]
    > Error response body for invalid PUT /settings/profiles/{id} requests.
    oneOf:
        schema: `UpdateProfileDuplicateDataErrorResponse`
        - `profiles` (array of object) [minItems=1, maxItems=1] **REQ** — Per-profile DUPLICATE_DATA errors from the update request.
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Error code indicating duplicate profile name data. Possible values: `DUPLICATE_DATA`.
          - `details` (object) **REQ** — Details object identifying the duplicated field and the ID of the conflicting profile.
            - `api_name` (string) **REQ** [maxLen=255, minLen=1] — API name of the field that contains duplicate data.
            - `json_path` (string) **REQ** [maxLen=500, minLen=1] — JSONPath to the duplicate field in the request payload.
          - `message` (string) **REQ** [enum=['duplicate data']] — Human-readable description of the duplicate data error.
          - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `UpdateProfileInvalidProfileNameSpecialCharsErrorResponse`
        - `profiles` (array of object) [minItems=1, maxItems=1] **REQ** — Per-profile INVALID_DATA errors pointing to the invalid `name` value in the update request.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating invalid profile name data. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Details object identifying the invalid `name` field in the update request.
            - `api_name` (string) **REQ** [maxLen=255, minLen=1] — API name of the field that contains an invalid value.
            - `json_path` (string) **REQ** [maxLen=500, minLen=1] — JSONPath to the invalid field in the update request.
          - `message` (string) **REQ** [enum=[1 values]] — Human-readable description of the invalid profile name characters error.
          - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `UpdateProfileInvalidActionErrorResponse`
        - `profiles` (array of object) [minItems=1, maxItems=1] **REQ** — Per-profile INVALID_DATA errors from the update request.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating an invalid action. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** [maxProperties=0] — Empty details object returned for the invalid action error.
          - `message` (string) **REQ** [enum=['The action given is invalid']] — Human-readable description of the invalid action error.
          - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `UpdateProfileInvalidPermissionIdErrorResponse`
        - `profiles` (array of object) [minItems=1, maxItems=1] **REQ** — Per-profile INVALID_DATA errors identifying the invalid permission ID.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating an invalid permission ID. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Details object identifying the permission ID field that failed validation.
            - `api_name` (string) **REQ** [enum=['id']] — API name of the field containing the invalid permission ID. Possible values: `id`.
            - `json_path` (string) **REQ** [enum=['$.profiles[0].permissions_details[0].id']] — JSONPath to the invalid permission ID in the request payload.
          - `message` (string) **REQ** [enum=[2 values]] — Human-readable error message. v8 returns "Invalid permission ID"; v9 returns "the id given seems to be invalid or already deleted".
          - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `UpdateProfilePermissionNotCustomizableErrorResponse`
        - `profiles` (array of object) [minItems=1, maxItems=1] **REQ** — Per-profile INVALID_DATA errors indicating a non-customizable permission.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating invalid data for a non-customizable permission. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Details object identifying the non-customizable permission ID field.
            - `api_name` (string) **REQ** [enum=['id']] — API name of the field containing the non-customizable permission. Possible values: `id`.
            - `json_path` (string) **REQ** [maxLen=500] — JSONPath to the permission id in the request payload.
          - `message` (string) **REQ** [enum=['Permission is not customizable']] — Human-readable description of the non-customizable permission error.
          - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `UpdateProfileInvalidPermissionsDetailsDatatypeErrorResponse`
        - `profiles` (array of object) [minItems=1, maxItems=1] **REQ** — Per-profile errors for the update request.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code.
          - `details` (object) **REQ** — Details about the datatype mismatch.
            - `expected_data_type` (string) **REQ** [enum=['jsonobject', 'jsonarray']] — Expected datatype for the field.
            - `api_name` (string) **REQ** [enum=['permissions_details']] — API name of the field with datatype mismatch.
            - `json_path` (string) [maxLen=500, minLen=1] — JSONPath to the field with datatype mismatch.
          - `message` (string) **REQ** [maxLen=1000] — Human-readable error message.
          - `status` (string) **REQ** [enum=['error']] — Error status indicator.
        schema: `UpdateProfileChildPermissionParentDisabledErrorResponse`
        - `profiles` (array of object) [minItems=1, maxItems=1] **REQ** — Per-profile INVALID_DATA errors indicating a child-parent permission rule violation.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating invalid permission state. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Details object identifying the permission ID that violates the parent-child rule.
            - `api_name` (string) **REQ** [enum=['id']] — API name of the field containing the child permission ID. Possible values: `id`.
            - `json_path` (string) **REQ** [maxLen=500] — JSONPath to the permission id in the request payload.
          - `message` (string) **REQ** [enum=[1 values]] — Human-readable description explaining that the parent permission must be enabled first.
          - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `UpdateProfilePermissionNotAllowedErrorResponse`
        - `profiles` (array of object) [minItems=1, maxItems=1] **REQ** — Per-permission NOT_ALLOWED errors from the update request.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code indicating the permission cannot be updated. Possible values: `NOT_ALLOWED`.
          - `details` (object) **REQ** — Details object identifying the permission ID that cannot be updated.
            - `api_name` (string) **REQ** [enum=['id']] — API name of the field containing the non-updatable permission ID. Possible values: `id`.
            - `json_path` (string) **REQ** [maxLen=500] — JSONPath to the field in the request payload.
          - `message` (string) **REQ** [enum=['This Permissionid cannot be updated']] — Human-readable description of why this permission ID cannot be updated.
          - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `UpdateProfileSystemProfileNotAllowedErrorResponse`
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code indicating the update operation is not allowed. Possible values: `NOT_ALLOWED`.
        - `details` (object) **REQ** — Details object identifying the path segment containing the system profile ID.
          - `resource_path_index` (integer/int32) **REQ** — Zero-based index of the URL path segment that contains the system profile ID.
        - `message` (string) **REQ** [enum=['System profile cannot be updated']] — Human-readable description of why the system profile cannot be updated.
        - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `UpdateProfilePrivateProfileNotAllowedErrorResponse`
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code indicating the update operation is not allowed. Possible values: `NOT_ALLOWED`.
        - `details` (object) **REQ** — Details object identifying the path segment containing the private profile ID.
          - `resource_path_index` (integer/int32) **REQ** — Zero-based index of the URL path segment that contains the private profile ID.
        - `message` (string) **REQ** [enum=['Team Module profile cannot be updated']] — Human-readable description of why the team module profile cannot be updated.
        - `status` (string) **REQ** [enum=['error']] — The status of the response.
**Possible values:**
**error**
        schema: `UpdateProfileInvalidIdErrorResponse`
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating an invalid profile ID. Possible values: `INVALID_DATA`.
        - `details` (object) **REQ** — Details object identifying the path segment containing the invalid ID.
          - `resource_path_index` (integer/int32) **REQ** — Zero-based index of the URL path segment that contains the invalid profile ID.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid or already deleted']] — Human-readable description of the invalid ID error.
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

**Scopes:** ZohoCRM.settings.profiles.UPDATE

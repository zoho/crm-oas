# POST /settings/profiles/{id}/actions/clone
**Operation:** `cloneProfile` — Clone a CRM profile
> Creates a new profile by cloning the existing profile identified by `{id}`. The request body must include the new profile's `name`, which must be unique within the organization and must not exceed 50 characters. See [Create a Profile](https://www.zoho.com/crm/developer/docs/api/v8/create-profile.html).

**Parameters:**
- `id` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$]: Represents the unique identifier of the profile (64-bit integer represented as a string, 1-19 digits).

**Request Body** (required) — application/json
> Profile definition for the new cloned profile.
  > Request body for cloning a profile.
  - `profiles` (array of object) [maxItems=1] **REQ** — Single-item JSON array containing the new profile definition for the clone operation.
    - `name` (string) **REQ** [maxLen=50] — The name of the new profile. Accepts up to 50 characters.
    - `description` (string) [maxLen=250, nullable] — A description of the profile. Accepts up to 250 characters.

**Responses:**

- **201**: Profile cloned successfully. — Schema: `CloneProfileResponse` [application/json]
    > Response body returned after a profile is successfully cloned.
    schema: `CloneProfileResponse`
    - `profiles` (array of object `CloneProfileActionResponse`) [maxItems=1] **REQ** — Array containing the clone action result (contains at most one entry).
      schema: `CloneProfileActionResponse`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Operation result code. Possible values: `SUCCESS`.
      - `details` (object) **REQ** — Represents the additional details returned with the clone operation result.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — ID of the newly created (cloned) profile.
      - `message` (string) **REQ** [maxLen=1000] — Description of the clone operation result.
      - `status` (string) **REQ** [enum=['success']] — Status of the operation result. Possible values: `success`.

- **400**: Invalid clone request. [application/json]
    > Error response body for invalid POST /settings/profiles/{id}/actions/clone requests.
    oneOf:
        schema: `CloneProfileInvalidIdErrorResponse`
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating an invalid profile ID. Possible values: `INVALID_DATA`.
        - `details` (object) **REQ** — Details object identifying the path segment that contains the invalid ID.
          - `resource_path_index` (integer/int32) **REQ** — Zero-based index of the URL path segment that contains the invalid profile ID.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable description of the invalid ID error.
        - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `CloneProfileInvalidCreateRequestErrorResponse`
        - `profiles` (array of object `MandatoryNotFoundProfileError`) [minItems=1, maxItems=1] **REQ** — Per-profile validation errors from the clone request.
          schema: `MandatoryNotFoundProfileError`
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code indicating a missing mandatory field. 
**Possible values:**
 **MANDATORY_NOT_FOUND**.
          - `details` (object) **REQ** — Details object identifying the missing mandatory field.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the missing mandatory field.
            - `json_path` (string) **REQ** [maxLen=500] — A JSONPath expression that indicates the location of the missing field in the request payload.
          - `message` (string) **REQ** [maxLen=1000] — A human-readable message describing the missing mandatory field.
          - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `CloneProfileDuplicateProfileNameErrorResponse`
        - `profiles` (array of object `DuplicateProfileNameError`) [minItems=1, maxItems=1] **REQ** — Per-profile duplicate name errors from the clone request.
          schema: `DuplicateProfileNameError`
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Error code indicating duplicate profile name data. 
**Possible values:**
 **DUPLICATE_DATA**.
          - `details` (object) **REQ** — Details object identifying the duplicated field and the ID of the conflicting profile.
            - `api_name` (string) **REQ** [maxLen=255] — Indicates the API name of the field that contains duplicate data.
            - `json_path` (string) **REQ** [maxLen=500] — A JSONPath expression that indicates the location of the duplicate field in the request payload.
          - `message` (string) **REQ** [maxLen=1000] — A descriptive error message explaining why the data was identified as a duplicate.
          - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `CloneProfileLicenseLimitExceededErrorResponse`
        - `profiles` (array of object `LicenseLimitExceededError`) [minItems=1, maxItems=1] **REQ** — Per-profile license limit exceeded errors from the clone request.
          schema: `LicenseLimitExceededError`
          - `code` (string) **REQ** [enum=['LICENSE_LIMIT_EXCEEDED']] — Error code indicating the license limit has been exceeded. 
**Possible values:**
 **LICENSE_LIMIT_EXCEEDED**.
          - `details` (object) **REQ** — Details object containing the license limit value.
            - `limit` (integer/int32) **REQ** — Maximum number of profiles allowed by the organization's license.
          - `message` (string) **REQ** [maxLen=1000] — A human-readable message describing the license limit exceeded error.
          - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `CloneProfileInvalidProfileNameSpecialCharsErrorResponse`
        - `profiles` (array of object) [minItems=1, maxItems=1] **REQ** — Per-profile INVALID_DATA errors pointing to the invalid `name` value in the clone request.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating invalid profile name data. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** — Details object identifying the invalid `name` field in the clone request.
            - `api_name` (string) **REQ** [maxLen=255, minLen=1] — API name of the field that failed validation.
            - `json_path` (string) **REQ** [maxLen=500, minLen=1] — A JSONPath expression that indicates the location of the invalid field in the request payload.
          - `message` (string) **REQ** [maxLen=1000] — Human-readable description of the invalid profile name error.
          - `status` (string) **REQ** [enum=['error']] — Response status indicator. Possible values: `error`.
        schema: `CloneProfileCannotBeClonedErrorResponse`
        - `profiles` (array of object) [minItems=1, maxItems=1] **REQ** — Per-profile INVALID_DATA errors indicating the clone operation is not permitted.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating invalid data. Possible values: `INVALID_DATA`.
          - `details` (object) **REQ** [maxProperties=0] — Empty details object returned for this error type.
          - `message` (string) **REQ** [maxLen=1000] — Human-readable description of why the clone operation is not permitted.
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

**Scopes:** ZohoCRM.settings.profiles.CREATE

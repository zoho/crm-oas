# DELETE /settings/profiles/{id}
**Operation:** `deleteProfile` — Profile
> Transfers all users of the profile identified by `{id}` to the profile specified by the `transfer_to` query parameter, then permanently deletes the source profile. System profiles (Administrator, Standard) cannot be deleted. See [Transfer Users and Delete a Profile](https://www.zoho.com/crm/developer/docs/api/v8/transfer-delete-profile.html).

**Parameters:**
- `id` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$]: Represents the unique identifier of the profile (64-bit integer represented as a string, 1-19 digits).
- `transfer_to` (query, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$]: Specify the unique identifier of the profile to which users of the deleted profile will be transferred.

**Responses:**

- **200**: Profile deleted and users transferred successfully. [application/json]
    > Successful response for the profile delete operation.
    - `status` (string) **REQ** [enum=['success']] — Status of the operation result. Possible values: `success`.
    - `code` (string) **REQ** [enum=['SUCCESS']] — The status code of the result. 
**Possible values:** 
**SUCCESS**
    - `message` (string) **REQ** [maxLen=500] — Human-readable message confirming the delete result.
    - `details` (object) **REQ** — Additional details returned with the delete operation result.
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Deleted profile ID.

- **400**: Invalid delete request. [application/json]
    > Error response body for invalid DELETE /settings/profiles/{id} requests.
    oneOf:
        schema: `TransferToIdNotFoundError`
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code indicating a missing mandatory parameter. Possible values: `MANDATORY_NOT_FOUND`.
        - `details` (object) **REQ** — Details object identifying the missing parameter.
          - `param` (string) **REQ** [enum=['transfer_to']] — Name of the missing required query parameter. Possible values: `transfer_to`.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable description of the missing parameter error.
        - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `InvalidTransferToIdError`
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating an invalid `transfer_to` value. Possible values: `INVALID_DATA`.
        - `details` (object) **REQ** — Empty details object returned for this error type.
          - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Invalid transfer_to value.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable description of the invalid transfer-to ID error.
        - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `InvalidDeleteRequestError`
        - `code` (string) **REQ** [enum=['CANNOT_DELETE']] — Error code indicating the delete operation is not allowed. Possible values: `CANNOT_DELETE`.
        - `details` (object) **REQ** — Empty details object returned for this error type.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable description of why the deletion is not permitted.
        - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `InvalidRequestMethodError`
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Error code indicating an unsupported HTTP method. Possible values: `INVALID_REQUEST_METHOD`.
        - `details` (object) **REQ** — Empty details object included with the invalid method error.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable description of the invalid request method.
        - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `DeleteProfileInvalidIdErrorResponse`
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating an invalid profile ID. Possible values: `INVALID_DATA`.
        - `details` (object) **REQ** — Details object identifying the path segment that contains the invalid ID.
          - `resource_path_index` (integer/int32) **REQ** — Zero-based index of the URL path segment that contains the invalid profile ID.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable description of the invalid ID error.
        - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `DeleteProfileInvalidActionErrorResponse`
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating an invalid action. Possible values: `INVALID_DATA`.
        - `details` (object) **REQ** [maxProperties=0] — Empty details object returned for this error type.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable description of the invalid action error.
        - `status` (string) **REQ** [enum=['error']] — The status of the response. 
**Possible values:**
**error**
        schema: `DeleteProfileSystemProfileNotAllowedErrorResponse`
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code indicating the operation is not allowed. Possible values: `NOT_ALLOWED`.
        - `details` (object) **REQ** — Details object identifying the path segment containing the system profile ID.
          - `resource_path_index` (integer/int32) **REQ** — Zero-based index of the URL path segment that contains the system profile ID.
        - `message` (string) **REQ** [maxLen=1000] — Human-readable description of why the system profile cannot be deleted.
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

**Scopes:** ZohoCRM.settings.profiles.DELETE

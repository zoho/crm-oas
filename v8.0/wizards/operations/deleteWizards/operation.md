# DELETE /settings/wizards/{id}
**Operation:** `deleteWizards` — Wizard
> Deletes the specified wizard configuration.

**Parameters:**
- `id` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]+$]: Specify the unique ID of the wizard to retrieve or delete.

**Responses:**

- **200**: Wizard deleted successfully. [application/json]
    > Response returned when a wizard is deleted successfully.
    - `wizards` (array of object) [maxItems=1] **REQ** — List of delete operation results, one entry per wizard in the request.
      - `status` (string) **REQ** [maxLen=7, enum=['success']] — Indicates that the delete operation was successful.
      - `code` (string) **REQ** [maxLen=7, enum=['SUCCESS']] — Operation result code.
      - `message` (string) **REQ** [maxLen=255] — Human-readable message describing the result of the delete operation.
      - `details` (object) **REQ** — Additional information about the deleted wizard.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the deleted wizard.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad request. The wizard ID provided in the request is invalid. [application/json]
    > Error response returned when the wizard ID passed to the delete API is invalid.
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating that the provided wizard ID is invalid.
    - `details` (object) **REQ** — Additional information about the invalid wizard ID error.
      - `resource_path_index` (integer/int32) **REQ** — Index of the resource path segment that contains the invalid wizard ID.
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message describing the invalid wizard ID.
    - `status` (string) **REQ** [enum=['error']] — Indicates that the delete operation failed.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **401**: Authentication credentials are missing or invalid. [application/json]
    > Represents the error response returned when authentication credentials are missing or invalid.
    oneOf:
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Error code indicating OAuth scope mismatch.
        - `details` (object) **REQ** — Empty details object.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
        - `status` (string) **REQ** [enum=['error']] — Status indicating failure.
        - `code` (string) **REQ** [enum=['INVALID_TOKEN']] — Error code indicating an invalid token.
        - `details` (object) **REQ** — Empty details object.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
        - `status` (string) **REQ** [enum=['error']] — Status indicating failure.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The authenticated user does not have permission to delete wizards. [application/json]
    > Error returned when the user lacks permission to perform the operation.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code indicating insufficient permissions.
    - `details` (object) **REQ** — Details about the required permissions.
      - `permissions` (array of string) [maxItems=50] **REQ** — List of permissions required.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `status` (string) **REQ** [enum=['error']] — Status indicating failure.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **404**: The requested resource could not be found. Typically returned when the URL pattern is invalid. [application/json]
    > Error response returned when the URL pattern is invalid.
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Indicates that the request failed.
        - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Error code indicating that the URL is invalid.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message explaining why the resource was not found.
        - `details` (object) **REQ** — Additional information about the error, if available.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.wizards.DELETE

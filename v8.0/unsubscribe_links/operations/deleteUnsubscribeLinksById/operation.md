# DELETE /settings/unsubscribe_links/{id}
**Operation:** `deleteUnsubscribeLinksById` — Delete Unsubscribe Link by ID
> To delete a specific unsubscribe link. Note that the default unsubscribe link cannot be deleted.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: The unique ID of the unsubscribe link to retrieve, update, or delete. This ID is returned in the response when creating or fetching unsubscribe links.

**Responses:**

- **200**: Success - Unsubscribe link deleted successfully — Schema: `UnsubscribeLinkRemovalResultList` [application/json]
    > Collection of action status objects produced after deleting unsubscribe links via DELETE requests.
    schema: `UnsubscribeLinkRemovalResultList`
    - `unsubscribe_links` (array of object `UnsubscribeLinkActionStatus`) [maxItems=1] — Array containing the status of the delete operation for each link
      schema: `UnsubscribeLinkActionStatus`
      - `code` (string) [maxLen=255] — The result code (SUCCESS or error code)
      - `details` (object `ActionEntityReference`) — Reference to the entity affected by an operation, containing its unique identifier.
        schema: `ActionEntityReference`
        - `id` (string) [maxLen=19] — The unique identifier of the affected unsubscribe link
      - `message` (string) [maxLen=255] — Represents the message describing the operation result.
      - `status` (string) [maxLen=255] — The status of the operation (success or error)

- **400**: Bad Request - The unsubscribe link ID is invalid or you are trying to delete the default unsubscribe link, which is not allowed. [application/json]
    > Validation error response for the DELETE by ID request, covering invalid or not-allowed unsubscribe link IDs.
    anyOf:
      - `NotAllowedUnsubscribeLinkIdError` — Error returned when attempting to update or delete the default unsubscribe link, which is not allowed.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional validation information about the not-allowed operation on a default link.
          - `resource_path_index` (integer/int32) **REQ** — The index position in the URL path where the default link ID was found
        - `message` (string) **REQ** [enum=['The given Unsubscribe Link id is Default']] — Represents the error message describing the not-allowed operation on a default unsubscribe link.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
      - `InvalidUnsubscribeLinkIdError` — Error returned when an invalid unsubscribe link ID is provided that does not belong to your organization.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Contains additional validation information about the invalid unsubscribe link ID error.
          - `resource_path_index` (integer/int32) **REQ** — The index position in the URL path where the invalid ID was found
        - `message` (string) **REQ** [enum=['The given Unsubscribe Link id is not part of Org']] — Represents the error message describing the invalid ID issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

- **403**: Forbidden - The request requires the ZohoCRM.settings.unsubscribe.DELETE scope. You cannot delete the default unsubscribe link. — Schema: `PermissionDeniedError` [application/json]
    > Error returned when the OAuth token does not have the required scope to perform the operation.
    schema: `PermissionDeniedError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for this response.
    - `details` (object) **REQ** — Contains additional validation information about the permission denied error.
      - `permissions` (array of string) [maxItems=25] **REQ** — The list of required permissions
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message describing the permission denied issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

**Scopes:** ZohoCRM.settings.unsubscribe.DELETE

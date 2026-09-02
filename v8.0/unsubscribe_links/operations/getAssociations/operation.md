# GET /settings/unsubscribe_link/actions/associations
**Operation:** `getAssociations` — Get Unsubscribe Link Associations
> To retrieve information about where unsubscribe links are being used (associated places) in your CRM account, such as in email templates.

**Responses:**

- **200**: Success - Returns a list of associated places for each unsubscribe link — Schema: `FetchAssociatedPlacesResponse` [application/json]
    > Response containing the list of places where unsubscribe links are currently associated in the Zoho CRM organization.
    schema: `FetchAssociatedPlacesResponse`
    - `associations` (array of object `UnsubscribeLinkAssociationRecord`) [maxItems=1] **REQ** — Array of association records showing where unsubscribe links are being used
      schema: `UnsubscribeLinkAssociationRecord`
      - `id` (string) **REQ** [maxLen=19] — The unique identifier of the unsubscribe link
      - `associated_places` (array of object `UnsubscribeLinkAssociatedPlace`) [maxItems=1] **REQ** — List of places where this unsubscribe link is being used
        schema: `UnsubscribeLinkAssociatedPlace`
        - `resource` (object `UnsubscribeLinkAssociationResource`) **REQ** — Represents the resource associated with an unsubscribe link, including its name and unique identifier.
          schema: `UnsubscribeLinkAssociationResource`
          - `name` (string) **REQ** [maxLen=255] — The name of the associated resource
          - `id` (string) **REQ** [maxLen=19] — The unique identifier of the associated resource
        - `details` (object `UnsubscribeLinkAssociationDetails`) **REQ** — Additional details for an unsubscribe link association, including the associated module context.
          schema: `UnsubscribeLinkAssociationDetails`
          - `module` (object `UnsubscribeLinkAssociationResourceModule`) **REQ** — Represents the module information associated with an unsubscribe link, including the module API name and ID.
            schema: `UnsubscribeLinkAssociationResourceModule`
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM module associated with the unsubscribe link.
            - `id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the CRM module associated with the unsubscribe link.
        - `type` (string) **REQ** [maxLen=255] — The type of associated place (e.g., email_templates)

- **204**: No Content - No associated places found for any unsubscribe link

- **403**: Forbidden - The request requires the ZohoCRM.settings.unsubscribe.READ scope — Schema: `PermissionDeniedError` [application/json]
    > Error returned when the OAuth token does not have the required scope to perform the operation.
    schema: `PermissionDeniedError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for this response.
    - `details` (object) **REQ** — Contains additional validation information about the permission denied error.
      - `permissions` (array of string) [maxItems=25] **REQ** — The list of required permissions
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message describing the permission denied issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

**Scopes:** ZohoCRM.settings.unsubscribe.READ

# GET /settings/kiosks/associations
**Operation:** `getAllKiosksAssociations` — Kiosk Associations
> To retrieve association information for all kiosks in your Zoho CRM organization, including detail view page associations with linked layout and module details. Use the [Get All Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve the Kiosk ID.


**Note:**
  - The structure of each resource object is mostly consistent, but _details can vary.
  - The sequence_number plays an important role in determining execution or display order.


**Parameters:**
- `include_inner_details` (query, string, optional) [maxLen=500]: Controls additional inner details to include in the response.
- `module` (query, string, optional) [maxLen=255]: Filters associations by the specified module API name.
- `include` (query, string, optional) [maxLen=255]: Specifies additional properties to include in the response.

**Responses:**

- **200**: Returns a list of all kiosks and their associations, including detail view page entries with linked layout and module details.
 — Schema: `GetAllKioskAssociationsListResponse` [application/json]
    > Response containing association information for all kiosks.
    schema: `GetAllKioskAssociationsListResponse`
    - `kiosks` (array of object `GETKioskAssociationsListEntry`) [maxItems=200] **REQ** — Array of kiosk association data.
      schema: `GETKioskAssociationsListEntry`
      - `_associations` (array of object `GETKioskDetailViewAssociationFull`) [maxItems=50] **REQ** — List of associations for this kiosk.
        schema: `GETKioskDetailViewAssociationFull`
        - `resources` (null) **REQ** — Resources field (null for detail_view_page type).
        - `type` (string) **REQ** [maxLen=255] — Type of association.
        - `detail_view_page` (array of object `GETDetailViewPageWithDetails`) [maxItems=50] **REQ** — Detail view page configurations.
          schema: `GETDetailViewPageWithDetails`
          - `sequence_number` (integer/int32) **REQ** — Display sequence number.
          - `layout` (object `GETAssociationLayout`) **REQ** — Layout associated with this detail view page.
            schema: `GETAssociationLayout`
            - `name` (string) **REQ** [maxLen=255] — Name of the layout.
            - `id` (string) **REQ** [maxLen=19] — Unique identifier of the layout.
            - `status` (string) **REQ** [maxLen=50] — Status of the layout.
          - `module` (object `GETAssociationModule`) **REQ** — Module associated with this detail view page.
            schema: `GETAssociationModule`
            - `display_label` (string) **REQ** [maxLen=255] — Display label of the module.
            - `api_name` (string) **REQ** [maxLen=50] — API name of the module.
            - `name` (string) **REQ** [maxLen=50] — Name of the module.
            - `id` (string) **REQ** [maxLen=19] — Unique identifier of the module.
          - `name` (string) **REQ** [maxLen=255] — Name of the detail view page association.
          - `id` (string) **REQ** [maxLen=255] — Unique identifier.
      - `id` (string) **REQ** [maxLen=255] — Kiosk identifier.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: Indicates that no kiosk associations were found for the account.

  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.READ

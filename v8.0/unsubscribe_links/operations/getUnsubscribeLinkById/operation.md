# GET /settings/unsubscribe_links/{id}
**Operation:** `getUnsubscribeLinkById` — Get Unsubscribe Link by ID
> To retrieve the complete configuration details of a specific unsubscribe link using its ID. This includes page settings, submission behavior, timestamps, and creator information.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: The unique ID of the unsubscribe link to retrieve, update, or delete. This ID is returned in the response when creating or fetching unsubscribe links.

**Responses:**

- **200**: Success - Returns the full configuration of the specified unsubscribe link — Schema: `RetrieveUnsubscribeLinksResponse` [application/json]
    > Response payload containing the unsubscribe link records returned by the GET by ID endpoint.
    schema: `RetrieveUnsubscribeLinksResponse`
    - `unsubscribe_links` (array of object `UnsubscribeLinkDetailRecord`) [maxItems=1] **REQ** — Array containing the requested unsubscribe link details
      schema: `UnsubscribeLinkDetailRecord`
      - `created_time` (string) **REQ** [maxLen=255] — The date and time when the unsubscribe link was created
      - `submission_message` (string) **REQ** [maxLen=2000] — The message displayed when the user clicks the unsubscribe button (for display_message action type)
      - `modified_time` (string) **REQ** [maxLen=255] — The date and time when the unsubscribe link was last modified
      - `submission_redirect_url` (null) **REQ** — The URL to which the user is redirected after unsubscribing (for redirect action type). Null if not configured.
      - `page_type` (string) **REQ** [maxLen=255] — Indicates whether the unsubscribe page is hosted on Zoho's standard page (standard) or a custom webpage (custom)
      - `custom_location_url` (null) **REQ** — The custom webpage URL where the unsubscribe link is hosted. Null if page_type is standard.
      - `modified_by` (object `UnsubscribeLinkModifiedByUser`) **REQ** — User who last modified the unsubscribe link, including the user name and ID. Refer to the [Get Users](users.yaml#$.paths./users.get) endpoint for details.
        schema: `UnsubscribeLinkModifiedByUser`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who last modified the unsubscribe link link
        - `id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the user who last modified the unsubscribe link unsubscribe link
      - `name` (string) **REQ** [maxLen=255] — The unique name of the unsubscribe link
      - `id` (string) **REQ** [maxLen=19] — The unique identifier of the unsubscribe link
      - `created_by` (object `UnsubscribeLinkCreatedByUser`) **REQ** — User who created the unsubscribe link, including the user name and ID. Refer to the [Get Users](users.yaml#$.paths./users.get) endpoint for details.
        schema: `UnsubscribeLinkCreatedByUser`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who created the unsubscribe link
        - `id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the user who created the unsubscribe link unsubscribe link
      - `standard_page_message` (string) **REQ** [maxLen=2000] — The message displayed on the standard unsubscribe page
      - `submission_action_type` (string) **REQ** [maxLen=255] — The action performed after unsubscribe: display_message (show a message) or redirect (redirect to a URL)

- **204**: No Content - No unsubscribe link found with the specified ID

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

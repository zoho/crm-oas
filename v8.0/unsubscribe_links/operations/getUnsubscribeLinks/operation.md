# GET /settings/unsubscribe_links
**Operation:** `getUnsubscribeLinks` — Get Unsubscribe Links
> To retrieve the details of all unsubscribe links configured in your CRM account. This API returns a list of unsubscribe links with their complete configuration, including page type, submission behavior, timestamps, and creator information.

**Responses:**

- **200**: Success - Returns a list of unsubscribe links with their configurations — Schema: `UnsubscribeLinksResponse` [application/json]
    > Response envelope containing a collection of unsubscribe link records returned by the settings listing endpoint.
    schema: `UnsubscribeLinksResponse`
    - `unsubscribe_links` (array of object `UnsubscribeLinkSummaryRecord`) [maxItems=10] **REQ** — Array of unsubscribe link summary records
      schema: `UnsubscribeLinkSummaryRecord`
      - `created_time` (string) **REQ** [maxLen=255] — The date and time when the unsubscribe link was created
      - `submission_message` (string) **REQ** [maxLen=2000, nullable] — The message displayed when the user clicks the unsubscribe button (for display_message action type). Null if not configured.
      - `modified_time` (string) **REQ** [maxLen=255] — The date and time when the unsubscribe link was last modified
      - `submission_redirect_url` (string) **REQ** [maxLen=255, nullable] — The URL to which the user is redirected after unsubscribing (for redirect action type). Null if not configured.
      - `page_type` (string) **REQ** [maxLen=255, nullable] — Indicates whether the unsubscribe page is hosted on Zoho's standard page (standard) or a custom webpage (custom)
      - `custom_location_url` (string) **REQ** [maxLen=255, nullable] — The custom webpage URL where the unsubscribe link is hosted. Null if page_type is standard.
      - `modified_by` (object `UnsubscribeLinkModifiedByUser`) **REQ** — User who last modified the unsubscribe link, including the user name and ID. Refer to the [Get Users](users.yaml#$.paths./users.get) endpoint for details.
        schema: `UnsubscribeLinkModifiedByUser`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who last modified the unsubscribe link link
        - `id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the user who last modified the unsubscribe link unsubscribe link
      - `name` (string) **REQ** [maxLen=255] — Represents the unique name of the unsubscribe link
      - `id` (string) **REQ** [maxLen=19] — The unique identifier of the unsubscribe link
      - `created_by` (object `UnsubscribeLinkCreatedByUser`) **REQ** — User who created the unsubscribe link, including the user name and ID. Refer to the [Get Users](users.yaml#$.paths./users.get) endpoint for details.
        schema: `UnsubscribeLinkCreatedByUser`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who created the unsubscribe link
        - `id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the user who created the unsubscribe link unsubscribe link
      - `standard_page_message` (string) **REQ** [maxLen=2000, nullable] — Represents the message displayed on the standard unsubscribe page. Null if page_type is custom. Null if page_type is custom.
      - `submission_action_type` (string) **REQ** [maxLen=255] — Represents the action performed after unsubscribe display_message (show a message) or redirect (redirect to a URL) a message) or redirect (redirect to a URL) a message) or redirect (redirect to a URL)"

- **204**: No content - No unsubscribe links found in the account

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

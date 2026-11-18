# GET /settings/webforms/{id}/actions/associated
**Operation:** `getAssociated` — Get webform associations

> To retrieve association details for a specific webform in Zoho CRM, including linked records, orchestration entries, and transition rules tied to the webform.


**Parameters:**
- `id` (path, string, required) [maxLen=255]: Specify the unique [Webform ID](webforms.yaml#$.paths./settings/webforms.get).

**Responses:**

- **200**: Returns the association details for the specified webform, including linked records, associated orchestration entries, and transition rules. — Schema: `GetassociatedResponse200` [application/json]
    > Represents the response for webform associations, listing the records linked to the requested webform.
    schema: `GetassociatedResponse200`
    - `webform_associations` (array of object `WebformAssociationsNested`) [maxItems=1] **REQ** — Contains the list of webform associations indicating which records are linked to the webform.
      schema: `WebformAssociationsNested`
      - `records_associated` (boolean) **REQ** — Indicates whether records are associated with the webform. Possible values: true - Records are associated. false - No records are associated.
      - `associated` (array of object `AssociatedNested`) [maxItems=1] **REQ** — Contains the list of record association objects linked to the webform.
        schema: `AssociatedNested`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the entity associated with the webform.
        - `details` (object `DetailsNested`) **REQ** — Represents the details of a Blueprint transition associated with the webform.
          schema: `DetailsNested`
          - `Transition` (object `TransitionNested`) **REQ** — Represents a Blueprint transition associated with the webform, including its identifier and name.
            schema: `TransitionNested`
            - `name` (string) **REQ** [maxLen=255] — Represents the name of the Blueprint transition associated with the webform.
            - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the Blueprint transition associated with the webform.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the entity associated with the webform.
        - `type` (string) **REQ** [maxLen=255] — Represents the type classification of the entity associated with the webform.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the webform for which the associations appear in the response.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The webform ID given seems to be invalid.
**Resolution:** The webform ID provided in the URL path must be a valid webform ID. — Schema: `ErrorResponse` [application/json]
    > Represents a generic API error response containing an error code, status, message, and details.
    schema: `ErrorResponse`
    - `code` (string) **REQ** [enum=[18 values]] — Represents the error code that identifies the type of error returned by the API.
    - `details` (object) **REQ** — Represents additional details providing context about the error, such as the invalid field name or parameter.
    - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the reason for the failure.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: error - The request was not successful.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.webforms.READ

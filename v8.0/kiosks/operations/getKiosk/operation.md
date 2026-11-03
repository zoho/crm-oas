# GET /settings/kiosks/{kioskId}
**Operation:** `getKiosk` — Get a Specific Kiosk
> To retrieve the details of a specific kiosk in your Zoho CRM organization, identified by its unique kiosk ID.

Use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve Kiosk ID.


**Parameters:**
- `kioskId` (path, string, required) [maxLen=19]: Specify the unique identifier of the kiosk. Use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get) to retrieve Kiosk ID.
- `include_inner_details` (query, string, optional) [maxLen=500]: Controls additional inner details to include in the response.

**Responses:**

- **200**: Returns a kiosks array containing the full details of the requested kiosk, including its version details, associated module, current status, creator and modifier information, and configuration data. — Schema: `KioskGetByIdResponse` [application/json]
    > Represents the response payload for retrieving a specific kiosk by its identifier, including full workflow and configuration details.
    schema: `KioskGetByIdResponse`
    - `kiosks` (array of object `KioskSummary`) [maxItems=1] **REQ** — Contains the kiosk object retrieved by the specified identifier.
      schema: `KioskSummary`
      - `created_time` (string) **REQ** [maxLen=255] — Represents the creation timestamp of the kiosk.
      - `version_details` (object `KioskVersionDetails`) **REQ** — Represents the versioning metadata for a kiosk, including the parent version identifier and the version number.
        schema: `KioskVersionDetails`
        - `parent_id` (null) **REQ** — Represents the identifier of the parent kiosk version. This value is null for the initial version.
        - `version_number` (integer/int32) **REQ** — Represents the version number of the kiosk.
      - `module` (object `KioskModuleRef`) **REQ** — Represents the reference to the CRM module configured for the kiosk, including the API name and identifier.
        schema: `KioskModuleRef`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module configured for the kiosk.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the module configured for the kiosk.
      - `description` (string) **REQ** [maxLen=255, nullable] — Represents the description of the kiosk. This value may be null if no description is provided.
      - `created_by` (object `KioskCreatedBySummary`) **REQ** — Represents the summary of the user who created the kiosk, including the user ID and display name.
        schema: `KioskCreatedBySummary`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who created the kiosk.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the user who created the kiosk.
      - `sequence_number` (integer/int32) **REQ** — Represents the display order of the kiosk within its group.
      - `modified_time` (string) **REQ** [maxLen=255] — Represents the date and time when the kiosk was last modified.
      - `group_id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the group to which the kiosk belongs.
      - `current_record_module` (object) **REQ** — Represents the module configured as the current record for the kiosk.
        anyOf:
          - `KioskCurrentRecordModuleSummary` — Represents a summary of the module assigned as the current record for the kiosk, including the plural label, API name, and identifier.
            - `plural_label` (string) **REQ** [maxLen=255] — Represents the plural display label of the current record module.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the current record module configured for the kiosk.
            - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the current record module configured for the kiosk.
            type: null — Represents the null state when no current record module is configured for the kiosk.
      - `associated` (boolean) **REQ** — Indicates whether the kiosk is associated with other CRM components. Possible values:
true - The kiosk is associated with other components.
false - The kiosk is not associated with other components.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the kiosk.
      - `modified_by` (object `KioskModifiedBySummary`) **REQ** — Represents the summary of the user who last modified the kiosk, including the user ID and display name.
        schema: `KioskModifiedBySummary`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who last modified the kiosk.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the user who last modified the kiosk.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the kiosk.
      - `status` (string) **REQ** [maxLen=255] — Represents the current status of the kiosk.
      - `group_api_name` (string) **REQ** [maxLen=255] — Represents the unique group API name for the kiosk.
      - `chart_data` (object) — Contains the workflow visualization data for the kiosk, including chart-specific configuration.
      - `transitions` (array of object) [maxItems=100] — Contains the list of workflow transitions defined for the kiosk.
      - `states` (array of object) [maxItems=100] — Contains the list of workflow states defined for the kiosk.
      additionalProperties: any
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: API version is not supported.
**Resolution:** A supported API version must be used when calling this endpoint. The caller should verify the API version in the request and upgrade to a version that supports the kiosks API. — Schema: `KioskErrorApiNotSupported` [application/json]
    > Represents the error response returned when the API version used does not support kiosks.
    schema: `KioskErrorApiNotSupported`
    - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Represents the error code. Possible values:
API_NOT_SUPPORTED - The requested API version is not supported.
    - `details` (object) **REQ** — Contains additional details about the error.
      - `supported_version` (integer/int32) **REQ** — Indicates the minimum supported API version for this operation.
    - `message` (string) **REQ** [enum=['api version is not supported']] — Represents the error message indicating that the requested API version is not supported.
    - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.READ

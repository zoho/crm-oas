# GET /settings/kiosks
**Operation:** `getAllKiosks` — Get All Kiosks

> To retrieve all the available Kiosks in your Zoho CRM organization. The response includes metadata for each Kiosk, such as version information, associated module, current status, creator and modifier details, and record context, if configured.


**Parameters:**
- `include_inner_details` (query, string, optional) [maxLen=500]: Controls additional inner details to include in the response.

**Responses:**

- **200**: Returns the list of kiosks with metadata, including version information, associated module, current status, creator and modifier details, and record context.
 — Schema: `KioskDetailResponse` [application/json]
    > Represents the response payload delivering detailed information for a specific kiosk, including workflow and configuration data.
    schema: `KioskDetailResponse`
    - `kiosks` (array of object `KioskSummary`) [maxItems=50] **REQ** — Contains the list of kiosk objects with detailed information.
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

- **400**: The configuration module name is invalid (INVALID_MODULE), or the API version used does not support kiosks (API_NOT_SUPPORTED).
**Resolution:** Pass the correct module name, or use a supported API version. [application/json]
    > Represents one of two possible error responses returned for a bad request: an invalid configuration module name (INVALID_MODULE) or an unsupported API version (API_NOT_SUPPORTED).

    oneOf:
      - `KioskErrorInvalidModule` — Represents the error response returned when the configuration module name in the request is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code. 
Possible values:
INVALID_MODULE - The module specified for the kiosk configuration is invalid.
        - `details` (object) **REQ** — Contains additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Indicates the index position within the resource path where the invalid module error was encountered.
        - `message` (string) **REQ** [enum=['the config module name seems to be invalid']] — Represents the error message describing the issue. Possible values:
The config module name seems to be invalid
        - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
      - `KioskErrorApiNotSupported` — Represents the error response returned when the API version used does not support kiosks.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Represents the error code. Possible values:
API_NOT_SUPPORTED - The requested API version is not supported.
        - `details` (object) **REQ** — Contains additional details about the error.
          - `supported_version` (integer/int32) **REQ** — Indicates the minimum supported API version for this operation.
        - `message` (string) **REQ** [enum=['api version is not supported']] — Represents the error message indicating that the requested API version is not supported.
        - `status` (string) **REQ** [enum=['error']] — Represents the HTTP response status for this error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.kiosks.READ

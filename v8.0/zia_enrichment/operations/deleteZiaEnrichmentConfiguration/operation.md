# DELETE /settings/zia/data_enrichment/{id}
**Operation:** `deleteZiaEnrichmentConfiguration` — Delete Zia Enrichment Configuration for a specific module
> Deletes a Zia Enrichment Configuration for a specific module by ID. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID.

**Parameters:**
- `id` (path, string, required) [maxLen=19]: Data Enrichment configuration ID

**Responses:**

- **200**: Enrichment configuration deleted successfully. [application/json]
    > Data enrichment deleted successfully.
    - `data_enrichment` (array of object) [maxItems=50] **REQ** — Array of deletion results for each configuration.
      - `code` (string) **REQ** [maxLen=255] — Result code — 'SUCCESS' for successful deletion.
      - `details` (object) **REQ** — Details of the deleted configuration.
        - `id` (string) **REQ** [maxLen=19] — Unique identifier of the deleted enrichment configuration.
      - `message` (string) **REQ** [maxLen=255] — Human-readable message describing the operation result.
      - `status` (string) **REQ** [maxLen=255] — Overall status of the operation — 'success' or 'error'.

- **400**: Bad Request. Returned when the enrichment ID is invalid or the feature is not enabled. [application/json]
    > 400 responses
    oneOf:
        - `code` (string) **REQ** [maxLen=255] — Error code — 'INVALID_DATA'.
        - `details` (object) **REQ** — Details about the invalid path parameter.
          - `resource_path_index` (integer/int32) **REQ** — Index of the invalid resource path segment.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
        - `status` (string) **REQ** [maxLen=255] — Error status — always 'error'.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED', 'FEATURE_NOT_SUPPORTED']] — Error code indicating the feature is not enabled or not supported.
        - `details` (object) **REQ** — Additional details — empty for this error type.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
        - `status` (string) **REQ** [maxLen=255] — Error status — always 'error'.

- **403**: Permission error. Returned when the user lacks the necessary permissions to delete enrichment configurations. [application/json]
    > Error response when the user lacks permission to access this feature.
    - `code` (string) **REQ** [maxLen=255] — Error code — 'NO_PERMISSION'.
    - `details` (object) **REQ** — Details about the missing permissions.
      - `permissions` (array of string) [maxItems=50] **REQ** — List of required permissions.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `status` (string) **REQ** [maxLen=255] — Error status — always 'error'.

**Scopes:** ZohoCRM.zia.enrichment.DELETE

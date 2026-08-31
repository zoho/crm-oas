# GET /__zia_org_enrichment/{id}
**Operation:** `getOrgEnrichmentById` — Org Enrichment Details
> Fetches the enrichment status and enriched organization data for a specific enrichment job using its unique ID. Returns completed, scheduled, or failed enrichment information along with enriched fields such as name, website, email, address, CEO, revenue, employees, social media, and industries.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: Specify the unique identifier of the Zia organization enrichment job to retrieve. Obtain this value from the response of POST `/__zia_org_enrichment` or from the listing returned by GET `/__zia_org_enrichment`.

**Responses:**

- **200**: Returns the details and enriched data of the requested organization enrichment job. [application/json]
    > Defines the response body returned when the requested organization enrichment job is retrieved successfully.
    - `__zia_org_enrichment` (array of object) [maxItems=1] **REQ** — Contains the details of the requested organization enrichment job.
      - `id` (string) **REQ** [maxLen=19] — Shows the unique identifier of the organization enrichment job.
      - `status` (string) **REQ** [enum=['COMPLETED', 'SCHEDULED', 'FAILED', 'DATA_NOT_FOUND', 'RUNNING']] — Indicates the current execution status of the enrichment job.

Possible values:
**COMPLETED** - The job has finished and enriched data is available.
**SCHEDULED** - The job is queued and yet to run.
**FAILED** - The job ended in a failure.
**DATA_NOT_FOUND** - The job completed but Zia could not locate public data to enrich.
      - `enrich_based_on` (object) **REQ** — Shows the trigger values that were supplied when the enrichment job was scheduled.
        - `name` (string) [maxLen=255] — Shows the organization name that was used as a trigger value.
        - `email` (string/email) [maxLen=255] — Shows the email address that was used as a trigger value.
        - `website` (string) [maxLen=255] — Shows the website domain that was used as a trigger value.
      - `enriched_data` (object) **REQ** [nullable] — Contains the data retrieved by Zia for the organization. The keys present in this object depend on the fields configured in the enrichment configuration of the organization. Returns `null` when the job has not yet completed or when no public data could be retrieved.

- **204**: Returned when no enrichment job exists for the supplied identifier or when the identifier is invalid.

- **400**: Returned when the data enrichment feature is not enabled or supported for the organization. Resolution: enable the data enrichment feature or upgrade to a CRM edition that supports it. [application/json]
    > Defines the response body returned when the data enrichment feature is not enabled or not supported.
    - `__zia_org_enrichment` (array of object `FeatureNotEnableOrNotSupported`) [maxItems=1] — Contains the list of error envelopes returned by the endpoint.
      schema: `FeatureNotEnableOrNotSupported`
      - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED', 'FEATURE_NOT_SUPPORTED']] — Identifies the feature-availability failure that was raised.

Possible values:
**FEATURE_NOT_ENABLED** - The data enrichment feature has not been enabled for the organization.
**FEATURE_NOT_SUPPORTED** - The current CRM edition does not support the data enrichment feature.
      - `details` (object) **REQ** — Contains additional context about the feature-availability failure. This object remains empty for this error.
      - `message` (string) **REQ** [maxLen=255] — Data enrichment is not available for your edition of CRM.
      - `status` (string) **REQ** [enum=['error']] — Indicates that the request ended in failure.

Possible values:
**error** - The request could not be processed because the data enrichment feature is unavailable.

- **403**: Returned when the authenticated user does not have the required permission to access the data enrichment feature. Resolution: contact the system administrator to be granted the Manage or View Data Enrichment profile permission. — Schema: `NoPermission` [application/json]
    > Error envelope returned when the authenticated user does not have permission to access the data enrichment feature.
    schema: `NoPermission`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Identifies the permission failure that was raised.

Possible values:
**NO_PERMISSION** - The authenticated user lacks the profile permission required to access the data enrichment feature.
    - `details` (object) **REQ** — Contains additional context about the permission failure. This object remains empty for this error.
    - `message` (string) **REQ** [maxLen=255] — You do not have the Manage or View Data Enrichment permission to access this feature.
    - `status` (string) **REQ** [enum=['error']] — Indicates that the request ended in failure.

Possible values:
**error** - The request could not be processed because the user lacks the required permission.

**Scopes:** ZohoCRM.settings.intelligence.READ

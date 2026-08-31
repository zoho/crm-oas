# GET /__zia_org_enrichment
**Operation:** `getZiaOrgEnrichment` — Get Zia Org Enrichment
> To retrieve the paginated list of Zia organization enrichment jobs that have been scheduled in your Zoho CRM organization. Each entry includes the job identifier, current status, creation timestamp, and the user who triggered the job.

**Parameters:**
- `page` (query, integer/int32, optional) [enum=[1, 2]]: Specify the page number to retrieve the list of records from the paginated results. Default value is 1. Accepts only positive integer values.
- `per_page` (query, integer/int32, optional) [enum=[100]]: Specify the number of records to retrieve per page. Default and maximum value is 100.
- `sort_by` (query, string, optional) [enum=['created_time']]: Specify the field to use for sorting the response based on created time. Accepts the literal value `created_time`.
- `sort_order` (query, string, optional) [enum=['asc', 'desc']]: Specify the direction(ascending or descending) in which to sort the response.

Possible values:
**asc** - Sort results in ascending order.
**desc** - Sort results in descending order.
- `status` (query, string, optional) [enum=['COMPLETED', 'FAILED', 'DATA_NOT_FOUND', 'SCHEDULED']]: Filter the response by the status of the scheduled enrichment job, using the create org enrichment API.

Possible values:
**COMPLETED** - Returns jobs that finished and produced enriched data.
**FAILED** - Returns jobs that ended with a failure.
**DATA_NOT_FOUND** - Returns jobs that completed but could not locate any public data to enrich.
**SCHEDULED** - Returns jobs that are queued and yet to run.

**Responses:**

- **200**: Returns the paginated list of organization enrichment jobs along with pagination metadata. [application/json]
    > Defines the response body returned when the list of organization enrichment jobs is retrieved successfully.
    - `__zia_org_enrichment` (array of object) [maxItems=200] **REQ** — Contains the list of organization enrichment jobs for the current page.
      - `id` (string) **REQ** [maxLen=19] — Shows the unique identifier of the organization enrichment job. Use this identifier with GET `/__zia_org_enrichment/{id}` to retrieve the enriched data of the job.
      - `status` (string) **REQ** [enum=['SCHEDULED', 'COMPLETED', 'DATA_NOT_FOUND', 'FAILED', 'RUNNING']] — Indicates the current execution status of the enrichment job.

Possible values:
**SCHEDULED** - The job is queued and yet to run.
**COMPLETED** - The job has finished and enriched data is available.
**FAILED** - The job ended in a failure.
**DATA_NOT_FOUND** - The job completed but Zia could not locate public data to enrich.
      - `created_time` (string/date-time) **REQ** — Shows the timestamp at which the enrichment job was scheduled, in ISO 8601 format.
      - `created_by` (object) **REQ** — Identifies the CRM user who triggered the enrichment job.
        - `id` (string) **REQ** [maxLen=19] — Shows the unique identifier of the CRM user who triggered the enrichment job.
        - `name` (string) **REQ** [maxLen=255] — Shows the display name of the CRM user who triggered the enrichment job.
    - `info` (object) **REQ** — Contains pagination metadata for the current page of enrichment jobs.
      - `per_page` (integer/int32) **REQ** [max=200] — Shows the configured number of enrichment jobs per page.
      - `count` (integer/int32) **REQ** [max=200] — Shows the number of enrichment jobs returned in the current page.
      - `page` (integer/int32) **REQ** — Shows the page number that this response corresponds to.
      - `more_records` (boolean) **REQ** — Indicates whether additional enrichment jobs exist beyond the current page. When the value is `true`, fetch the next page using the `page` parameter.

- **204**: Returned when no organization enrichment jobs exist for the authenticated CRM organization.

- **400**: Returned when the data enrichment feature is not enabled or supported for the organization, or when a supplied query parameter such as `status`, `sort_by`, or `sort_order` is invalid. Resolution: review the returned `code` and `details` to identify the offending input and resend the request after correcting it. [application/json]
    > Defines the set of bad-request error envelopes that the GET `/__zia_org_enrichment` endpoint can return. Exactly one variant matches the failure condition.
    oneOf:
      - `FeatureNotEnableOrNotSupported` — Error envelope returned when the data enrichment feature is either disabled for the organization or not available under the current CRM edition.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED', 'FEATURE_NOT_SUPPORTED']] — Identifies the feature-availability failure that was raised.

Possible values:
**FEATURE_NOT_ENABLED** - The data enrichment feature has not been enabled for the organization.
**FEATURE_NOT_SUPPORTED** - The current CRM edition does not support the data enrichment feature.
        - `details` (object) **REQ** — Contains additional context about the feature-availability failure. This object remains empty for this error.
        - `message` (string) **REQ** [maxLen=255] — Data enrichment is not available for your edition of CRM.
        - `status` (string) **REQ** [enum=['error']] — Indicates that the request ended in failure.

Possible values:
**error** - The request could not be processed because the data enrichment feature is unavailable.
      - `ZiaOrgEnrichmentInvalidParam` — Error envelope returned when a supplied query parameter such as `status`, `sort_by`, or `sort_order` does not match the allowed set of values.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Identifies the parameter-validation failure that was raised.

Possible values:
**INVALID_DATA** - The supplied query parameter value is not among the allowed values.
        - `details` (object) **REQ** — Contains additional context that identifies the offending query parameter and lists the values that the parameter accepts.
          - `param` (string) **REQ** [enum=['status', 'sort_order', 'sort_by']] — Shows the name of the query parameter whose value failed validation.
          - `supported_values` (object) **REQ** — Lists the values that the offending query parameter accepts. The exact list depends on which parameter raised the failure.
            oneOf:
                type: array of string [maxItems=5]
                  type: string [enum=['COMPLETED', 'SCHEDULED', 'FAILED', 'RUNNING', 'DATA_NOT_FOUND', 'UPDATED']] — Represents a single value accepted by the `status` query parameter.

Possible values:
**COMPLETED** - The job has finished and enriched data is available.
**SCHEDULED** - The job is queued and yet to run.
**FAILED** - The job ended in a failure.
**RUNNING** - The job is currently running.
**DATA_NOT_FOUND** - The job completed but Zia could not locate public data to enrich.
                  items: [enum=['COMPLETED', 'SCHEDULED', 'FAILED', 'RUNNING', 'DATA_NOT_FOUND', 'UPDATED']]
                type: array of string [maxItems=2]
                  type: string [enum=['asc', 'desc']] — Represents a single value accepted by the `sort_order` query parameter.

Possible values:
**asc** - Sort results in ascending order.
**desc** - Sort results in descending order.
                  items: [enum=['asc', 'desc']]
                type: array of string [maxItems=1]
                  type: string [enum=['created_time']] — Represents a single value accepted by the `sort_by` query parameter.

Possible values:
**created_time** - Sort results by the timestamp at which each enrichment job was scheduled.
                  items: [enum=['created_time']]
        - `message` (string) **REQ** [maxLen=255] — Provides a message that explains the parameter-validation failure.
        - `status` (string) **REQ** [enum=['error']] — Indicates that the request ended in failure.

Possible values:
**error** - The request could not be processed because of a parameter-validation failure.

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

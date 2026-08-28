# POST /__zia_org_enrichment
**Operation:** `submitOrgEnrichmentRequest` — Trigger organization-level enrichment for a CRM record
> To submit a request that schedules a Zia organization enrichment job in your Zoho CRM organization. The job runs asynchronously and uses the supplied name, email, or website to retrieve publicly available details such as address, primary contact, industries, and social media handles, and to populate the configured fields of the target module or record.

**Parameters:**
- `module` (query, string, required) [maxLen=255]: Specify the API name of the CRM module for which enrichment is to be triggered. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the list of valid module API names.
- `record_id` (query, string, optional) [maxLen=19]: Specify the unique identifier of the record for which enrichment is to be triggered. When omitted, the job runs at the module level. Use the records API of the target module to retrieve record identifiers.

**Request Body** (required) — application/json
> Specify the payload that contains the list of enrichment requests. Each request supplies trigger values that Zia uses to look up public information about the organization.
  > Defines the body of a Zia organization enrichment request. Wraps the list of enrichment inputs under the `__zia_org_enrichment` key.
  - `__zia_org_enrichment` (array of object) [maxItems=50] **REQ** — Specify the list of enrichment requests to schedule. You can supply up to 50 entries in a single call.
    - `enrich_based_on` (object) **REQ** — Specify the details of the fields on whose values you want to trigger enrichment.  Note that you must provide at least one of the following values in the input. Based on these values, Zia will look for information on the web and enrich fields as per [Enrichment Configuration.](zia_enrichment.yaml#$.paths./settings/zia/data_enrichment.get)) Note that the values of these keys must be at least three characters long and only in English.
      - `name` (string) **REQ** [maxLen=255] — Specify the name of the organization  that Zia uses as a trigger value to look up enrichment data.
      - `email` (string/email) — Specify the email address of the organization that Zia uses as a trigger value to look up enrichment data.
      - `website` (string/website) — Specify the website domain of the organization that Zia uses as a trigger value to look up enrichment data.

**Responses:**

- **202**: Returns a confirmation that the enrichment job has been accepted and queued for asynchronous execution. [application/json]
    > Defines the response body returned when a Zia organization enrichment job is successfully scheduled.
    - `__zia_org_enrichment` (array of object) [maxItems=50] **REQ** — Contains the list of scheduling results, one entry per submitted enrichment request.
      - `code` (string) **REQ** [enum=['SCHEDULED']] — Indicates the scheduling outcome of the enrichment request.

Possible values:
**SCHEDULED** - The enrichment job has been queued for asynchronous execution.
      - `details` (object) **REQ** — Contains identifying information about the scheduled enrichment job.
        - `id` (string) **REQ** [maxLen=255] — Shows the unique identifier assigned to the scheduled enrichment job. Use this identifier with GET `/__zia_org_enrichment/{id}` to retrieve job status and enriched data.
      - `message` (string) **REQ** [maxLen=255] — Provides a message that describes the outcome of the scheduling request.
      - `status` (string) **REQ** [enum=['success']] — Indicates whether the scheduling request succeeded.

Possible values:
**success** - The enrichment job was successfully accepted and queued.

- **400**: Returned when the request cannot be processed because of validation failures, missing inputs, exceeded enrichment limits, an unsupported module, or because the data enrichment feature is not enabled or not supported. Resolution: review the returned `code` and `details` to identify the offending input and resend the request after correcting it. [application/json]
    > Defines the set of bad-request error envelopes that the POST `/__zia_org_enrichment` endpoint can return. Exactly one variant matches the failure condition.
    oneOf:
        - `__zia_org_enrichment` (array of object) [maxItems=50] **REQ** — Contains the list of validation errors detected in the submitted enrichment requests.
          - `code` (string) **REQ** [enum=['INVALID_DATA', 'MANDATORY_NOT_FOUND']] — Identifies the validation failure that was raised.

Possible values:
**INVALID_DATA** - A value supplied in `enrich_based_on` is incorrect, shorter than three characters, in a non-English language, or has the wrong data type.
**MANDATORY_NOT_FOUND** - The mandatory key `enrich_based_on` was not supplied in the input.
          - `details` (object) **REQ** — Contains additional context that identifies the invalid or missing input field.
            - `expected_data_type` (string) [maxLen=255] — Indicates the data type that the field expects when the supplied value uses an incorrect type.
            - `api_name` (string) **REQ** [enum=['name', 'email', 'website', 'enrich_based_on']] — Identifies the field whose value failed validation.

Possible values:
**name** - The organization name in `enrich_based_on`.
**email** - The organization email in `enrich_based_on`.
**website** - The organization website in `enrich_based_on`.
**enrich_based_on** - The `enrich_based_on` object itself.
            - `json_path` (string) **REQ** [enum=[4 values]] — Shows the JSON path that points to the exact field in the request payload that failed validation.
          - `message` (string) **REQ** [maxLen=255] — Provides a message that explains the validation failure like "You have not specified the key "enrich_based_on" in the input".
          - `status` (string) **REQ** [enum=['error']] — Indicates that the request ended in failure.

Possible values:
**error** - The request could not be processed because of a validation error.
        - `__zia_org_enrichment` (array of object) [maxItems=1] **REQ** — Contains the list of enrichment requests that breached the configured limit.
          - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Identifies the limit violation that was raised.

Possible values:
**LIMIT_EXCEEDED** - The organization has used up its enrichment quota for the current edition.
          - `details` (object) **REQ** — Contains additional context about the enrichment limit that was breached.
            - `limit` (integer/int32) **REQ** — Shows the maximum number of enrichments allowed for the organization based on its CRM edition and user count.
            - `limit_due_to` (array of object) [maxItems=1] **REQ** — Lists the input fields that contributed to the limit breach.
              - `api_name` (string) **REQ** [enum=['enrich_based_on']] — Identifies the API name of the field that contributed to the limit breach.
              - `json_path` (string) **REQ** [enum=['$.__zia_org_enrichment[0].enrich_based_on']] — Shows the JSON path that points to the field in the request payload that contributed to the limit breach.
          - `message` (string) **REQ** [maxLen=255] — Provides a message that explains the limit violation like, "You have created more than the allowed enrichments for your org."
          - `status` (string) **REQ** [enum=['error']] — Indicates that the request ended in failure.

Possible values:
**error** - The request could not be processed because the enrichment limit was breached.
        - `__zia_org_enrichment` (array of object) [maxItems=50] **REQ** — Contains the list of errors identifying the missing expected fields.
          - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Identifies the missing-input failure that was raised.

Possible values:
**EXPECTED_FIELD_MISSING** - None of the trigger fields expected inside `enrich_based_on` were supplied.
          - `details` (object) **REQ** — Contains the list of trigger fields that the request was expected to include.
            - `expected_fields` (array of object) [maxItems=50] **REQ** — Lists the trigger fields that the request must include inside `enrich_based_on`.
              - `api_name` (string) **REQ** [enum=['name', 'email', 'website']] — Shows the API name of the expected trigger field.
              - `json_path` (string) **REQ** [enum=[3 values]] — Shows the JSON path at which the expected trigger field should appear in the request payload.
          - `message` (string) **REQ** [maxLen=255] — Provides a message that explains which trigger fields are expected like, "You have not specified any key in the "enrich_based_on" JSON object."
          - `status` (string) **REQ** [enum=['error']] — Indicates that the request ended in failure.

Possible values:
**error** - The request could not be processed because no expected trigger field was supplied.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING', 'INVALID_DATA', 'NOT_SUPPORTED']] — Identifies the parameter-level failure that was raised.

Possible values:
**REQUIRED_PARAM_MISSING** - The required `module` query parameter was not supplied.
**INVALID_DATA** - The supplied `module` value is not supported for organization enrichment.
        - `details` (object) **REQ** — Contains additional context that identifies the offending query parameter.
          - `param_name` (string) **REQ** [enum=['module', 'record_id']] — Shows the name of the query parameter that triggered the failure.
        - `message` (string) **REQ** [maxLen=255] — Provides a message that explains the parameter-level failure.
        - `status` (string) **REQ** [enum=['error']] — Indicates that the request ended in failure.

Possible values:
**error** - The request could not be processed because of a parameter-level failure.
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
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Identifies the array-level validation failure that was raised.

Possible values:
**INVALID_DATA** - The submitted `__zia_org_enrichment` array contains more entries than the allowed maximum.
        - `details` (object) **REQ** — Contains additional context about the array-level validation failure.
          - `maximum_length` (integer/int32) **REQ** — Shows the maximum number of entries allowed in the array.
          - `api_name` (string) **REQ** [enum=['__zia_org_enrichment']] — Identifies the array field whose cardinality was exceeded.
          - `json_path` (string) **REQ** [enum=['$.__zia_org_enrichment']] — Shows the JSON path that points to the array field whose cardinality was exceeded.
        - `message` (string) **REQ** [maxLen=255] — Provides a message that explains the array cardinality violation.
        - `status` (string) **REQ** [maxLen=255] — Indicates that the request ended in failure.

Possible values:
**error** - The request could not be processed because the array exceeded its allowed cardinality.

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

**Scopes:** ZohoCRM.settings.intelligence.CREATE

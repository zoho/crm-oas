# GET /settings/territories/actions/scheduled_run_rule_jobs
**Operation:** `getTerritoryScheduledRunRuleJobs` — Get scheduled territory run rule job status
> To retrieve the status of a scheduled territory rule execution job in your Zoho CRM organization by specifying the **job_id** parameter.

**Tags:** Territories

**Parameters:**
- `job_id` (query, string/int64, required): The unique identifier of the scheduled run rule job.

**Responses:**

- **200**: Returns the status and details of the specified scheduled territory run rule job.
 — Schema: `TerritoryScheduledRunRuleJobsResponse` [application/json]
    > Represents the response containing the status and details of scheduled territory run rule jobs.
    schema: `TerritoryScheduledRunRuleJobsResponse`
    - `scheduled_run_rule_jobs` (object) **REQ** — Represents the status and details of the scheduled territory rule execution job.
      - `status` (string) **REQ** [enum=['COMPLETED', 'IN_PROGRESS', 'FAILED', 'SCHEDULED']] — Represents the current status of the scheduled run rule job. Possible values: **COMPLETED**, **IN_PROGRESS**, **FAILED**, **SCHEDULED**.
      - `job_id` (string/int64) **REQ** — Represents the unique identifier of the scheduled run rule job.
      - `scheduled_by` (object) **REQ** — Represents the user who scheduled the run rule job.
        - `name` (string) **REQ** [maxLen=100] — Represents the name of the user who scheduled the run rule job.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the user who scheduled the run rule job.
      - `scheduled_time` (string/date-time) **REQ** — Represents the date and time when the run rule job was scheduled, in ISO 8601 format.

- **204**: Indicates that no scheduled territory run rule job was found for the specified **job_id**.


- **400**: The request could not be processed due to a missing required parameter or a disabled territory feature.
**Resolution:** The **job_id** query parameter must be included in the request, and territory management must be enabled in the Zoho CRM organization. [application/json]
    > Represents the error response for a 400 Bad Request, which occurs when the territory feature is not enabled or the required **job_id** parameter is missing.

    oneOf:
      - `TerritoryFeatureNotEnabledError` — Represents the error response when the territory feature is not enabled for the organization.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for the request. Possible values: **FEATURE_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [maxLen=100, enum=[5 values]] — Represents the error message returned when the territory feature is not enabled for the organization. Possible values: **Territory Management is disabled**, **Territory Management is not enabled**, **Territory Management Disabled**, **the territory feature is not enabled for Leads Module**, **Territory Management is not enabled for Leads Module**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `ScheduledRunRuleJobsRequiredParamMissing` — Represents the error response when the required job_id query parameter is missing or null in the Get Scheduled Run Rule Jobs request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for the request. Possible values: **REQUIRED_PARAM_MISSING**.
        - `details` (object) **REQ** — Represents additional details about the error, including the name of the missing required parameter.
          - `param_name` (string) **REQ** [enum=['job_id']] — Represents the name of the required parameter that is missing from the request. Possible values: **job_id**.
        - `message` (string) **REQ** [enum=['mandatory param missing', 'One of the expected parameter is missing']] — Represents the error message returned when a required parameter is missing. Possible values: **mandatory param missing**, **One of the expected parameter is missing**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

- **401**: Authentication failed for the request.
**Resolution:** A new access token must be generated with the required scope for this API. — Schema: `UnauthorizedError` [application/json]
    > Represents the error response when authentication fails for the request.
    schema: `UnauthorizedError`
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code for the request. Possible values: **AUTHENTICATION_FAILURE**.
    - `details` (object) **REQ** — Represents additional details about the authentication error.
    - `message` (string) **REQ** [maxLen=100, enum=['Authentication failed']] — Represents the error message returned when authentication fails. Possible values: **Authentication failed**.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

**Scopes:** ZohoCRM.settings.territories.READ, ZohoCRM.settings.territories.ALL

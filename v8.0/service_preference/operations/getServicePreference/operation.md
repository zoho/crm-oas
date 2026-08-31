# GET /settings/service_preferences
**Operation:** `getServicePreference` — Get service preferences
> Retrieves the service preference settings of the organization, including whether the job sheet is enabled for service appointments. Use this API to check whether a job sheet can be generated once a service appointment is marked complete.

**Responses:**

- **200**: The service preference settings of the organization were retrieved successfully. [application/json]
    > Represents the response wrapper that contains the service preference settings of the organization.
    - `service_preferences` (object) **REQ** — Represents the service preference settings configured for the organization.
      - `job_sheet_enabled` (boolean) **REQ** — Denotes whether the job sheet is enabled for the
organization. When the job sheet is enabled, a job
sheet can be generated for a service appointment once
the appointment is marked complete.


Possible values:


- **true**: The job sheet is enabled for the
organization. This is the default value.

- **false**: The job sheet is disabled for the
organization.


**Scopes:** ZohoCRM.settings.modules.READ

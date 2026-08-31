# GET /settings/audit_log_export
**Operation:** `getAuditLogExports` — Get audit log export jobs
> To retrieve the list of all audit log export jobs in your Zoho CRM organization, along with their status, filter criteria, and download links.

**Schemas:**
`AuditLogActionEqualCriterion`:
  > Match audit log entries whose action equals a single value.
  - `field` (object) **REQ** — Field to apply the filter on.
    - `api_name` (string) **REQ** [enum=['action']] — API name of the field.
  - `comparator` (string) **REQ** [enum=['equal']] — Comparison operator.
  - `value` (string) **REQ** [enum=['added', 'updated', 'deleted']] — Action to match.
`AuditLogActionInCriterion`:
  > Match audit log entries whose action is one of several values.
  - `field` (object) **REQ** — Field to apply the filter on.
    - `api_name` (string) **REQ** [enum=['action']] — API name of the field.
  - `comparator` (string) **REQ** [enum=['in']] — Comparison operator.
  - `value` (array of string) [minItems=1, maxItems=3] **REQ** — Actions to match.
    items: [enum=['added', 'updated', 'deleted']]
`AuditLogAuditedTimeBetweenCriterion`:
  > Match audit log entries audited within a time range. The range must not exceed 180 days.
  - `field` (object) **REQ** — Field to apply the filter on.
    - `api_name` (string) **REQ** [enum=['audited_time']] — API name of the field.
  - `comparator` (string) **REQ** [enum=['between']] — Comparison operator.
  - `value` (array of string/date-time) [minItems=2, maxItems=2] **REQ** — Start and end of the range, as exactly two ISO 8601 timestamps.
`AuditLogDoneByEqualCriterion`:
  > Match audit log entries performed by a single user.
  - `field` (object) **REQ** — Field to apply the filter on.
    - `api_name` (string) **REQ** [enum=['done_by']] — API name of the field.
  - `comparator` (string) **REQ** [enum=['equal']] — Comparison operator.
  - `value` (array of object `AuditLogDoneByValue`) [minItems=1, maxItems=1] **REQ** — Exactly one user reference.
`AuditLogDoneByInCriterion`:
  > Match audit log entries performed by any of several users.
  - `field` (object) **REQ** — Field to apply the filter on.
    - `api_name` (string) **REQ** [enum=['done_by']] — API name of the field.
  - `comparator` (string) **REQ** [enum=['in']] — Comparison operator.
  - `value` (array of object `AuditLogDoneByValue`) [minItems=1, maxItems=500] **REQ** — User references to match.
`AuditLogDoneByValue`:
  > User reference for the done_by filter.
  - `id` (string) **REQ** [maxLen=64] — Unique identifier of the user.
  - `name` (string) [maxLen=256] — Display name of the user.
`AuditLogGroupedCriterion`:
  > A group of filter conditions combined with a logical operator.
  - `group_operator` (string) **REQ** [enum=['and']] — Logical operator applied between the grouped conditions.
  - `group` (array of object) [minItems=1, maxItems=2] **REQ** — Conditions to combine.
    oneOf:
      - `AuditLogSimpleCriterion` — A single field-level filter condition.
      - `AuditLogGroupedCriterion` — A group of filter conditions combined with a logical operator.
`AuditLogModuleEqualCriterion`:
  > Match audit log entries belonging to a single module.
  - `field` (object) **REQ** — Field to apply the filter on.
    - `api_name` (string) **REQ** [enum=['module']] — API name of the field.
  - `comparator` (string) **REQ** [enum=['equal']] — Comparison operator.
  - `value` (array of object `AuditLogModuleValue`) [minItems=1, maxItems=1] **REQ** — Exactly one module reference.
`AuditLogModuleInCriterion`:
  > Match audit log entries belonging to any of several modules.
  - `field` (object) **REQ** — Field to apply the filter on.
    - `api_name` (string) **REQ** [enum=['module']] — API name of the field.
  - `comparator` (string) **REQ** [enum=['in']] — Comparison operator.
  - `value` (array of object `AuditLogModuleValue`) [minItems=1, maxItems=500] **REQ** — Module references to match.
`AuditLogModuleValue`:
  - `api_name` (string) [maxLen=128] — API name of the module.
  - `id` (string) [maxLen=64] — Unique identifier of the module.
  anyOf:
`AuditLogSimpleCriterion`:
  oneOf:
    - `AuditLogActionEqualCriterion` — Match audit log entries whose action equals a single value.
    - `AuditLogActionInCriterion` — Match audit log entries whose action is one of several values.
    - `AuditLogModuleEqualCriterion` — Match audit log entries belonging to a single module.
    - `AuditLogModuleInCriterion` — Match audit log entries belonging to any of several modules.
    - `AuditLogDoneByEqualCriterion` — Match audit log entries performed by a single user.
    - `AuditLogDoneByInCriterion` — Match audit log entries performed by any of several users.
    - `AuditLogAuditedTimeBetweenCriterion` — Match audit log entries audited within a time range. The range must not exceed 180 days.

**Responses:**

- **200**: Returns the list of audit log export jobs along with their status, filter criteria, and download links. [application/json]
    > Represents the success response for retrieving audit log export jobs.
    - `audit_log_export` (array of object) [maxItems=100] — Represents the list of audit log export jobs.
      - `criteria` (object `AuditLogCriterionNullable`) **REQ** — Filter criteria stored for this export job. Null when the job was created without criteria.
        oneOf:
          - `AuditLogCriterion` — Filter criteria for an audit log export job.
            oneOf:
              - `AuditLogSimpleCriterion` — A single field-level filter condition.
              - `AuditLogGroupedCriterion` — A group of filter conditions combined with a logical operator.
            type: null — No criteria were stored for this export job.
      - `id` (string) [maxLen=64] — Represents the unique ID of the audit log export job.
      - `status` (string) [enum=[7 values]] — Status of the export job.
      - `created_by` (object) — Represents the Zoho CRM user who created the export job.
        - `name` (string) [maxLen=256] — Represents the name of the user who created the export job.
        - `id` (string) **REQ** [maxLen=64] — Represents the unique ID of the user who created the export job.
      - `download_links` (array of string) [maxItems=1000, nullable] **REQ** — Download links for exported audit logs. Null until the job completes and produces at least one file.
        items: [maxLen=2048]
      - `job_start_time` (string/date-time) — Represents the date and time when the export job started.
      - `job_end_time` (string/date-time) — Represents the date and time when the export job was completed.
      - `expiry_date` (string/date-time) [nullable] — Expiry date for download links. Null until download links are generated.

- **204**: Returns an empty response when no audit log export jobs are available.

- **403**: Forbidden - the current user does not have an administrator profile, or the Audit Logs feature is not available for this organization. — Schema: `AuditLogExportForbiddenResponse` [application/json]
    > Error returned when the user lacks an administrator profile or the Audit Logs feature is unavailable.
    schema: `AuditLogExportForbiddenResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code.
    - `message` (string) **REQ** [maxLen=256] — Error message.
    - `status` (string) **REQ** [enum=['error']] — Error status.
    - `details` (object) **REQ** — Permissions the current user is missing.
      - `permissions` (array of string) [maxItems=25] **REQ** — Permissions required to perform this operation.
        items: [maxLen=128]

**Scopes:** ZohoCRM.settings.audit_logs.READ

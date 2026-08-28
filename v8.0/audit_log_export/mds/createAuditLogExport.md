# POST /settings/audit_log_export
**Operation:** `createAuditLogExport` — Create an audit log export job
> To create an asynchronous audit log export job in your Zoho CRM organization. The system schedules the job and returns a unique job ID with a SCHEDULED status code. Use the[Get Audit Log Export API](audit_log_export.yaml#.$./paths./settings/audit_log_export.get) to poll for completion and retrieve the download links.

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
`AuditLogExportErrorFieldPointer`:
  > Pointer to the request field that caused the error.
  - `api_name` (string) **REQ** [maxLen=64] — API name of the field that caused the error.
  - `json_path` (string) **REQ** [maxLen=256] — JSON path of the field within the request body.
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

**Request Body** — application/json
> The request body must contain an audit_log_export array. You can include a maximum of 100 objects per request.
  > Represents the request body for creating an audit log export job.
  - `audit_log_export` (array of object) [maxItems=100] **REQ** — Specify the list of audit log export job configurations.
    - `criteria` (object `AuditLogCriterion`) **REQ** — Filter criteria for an audit log export job.
      oneOf:
        - `AuditLogSimpleCriterion` — A single field-level filter condition.
        - `AuditLogGroupedCriterion` — A group of filter conditions combined with a logical operator.

**Responses:**

- **200**: Returns the scheduled status and unique job ID for each submitted audit log export request. [application/json]
    > Represents the success response for creating an audit log export job.
    - `audit_log_export` (array of object) [maxItems=1] — Represents the list of audit log export job responses.
      - `code` (string) [enum=['SCHEDULED']] — Specifies the status code of the export job creation.
Possible values:
SCHEDULED - The audit log export job has been successfully scheduled.
      - `details` (object) — Represents additional details for the scheduled audit log export job.
        - `id` (string) [maxLen=64] — Represents the unique ID of the scheduled audit log export job.
      - `message` (string) [maxLen=256] — Represents the message describing the audit log export job status.
      - `status` (string) [enum=['success']] — Represents the status of the export job creation request.
Possible values:
success - The audit log export job creation completed successfully.

- **400**: The audit log export request is invalid. Resolution: Verify the request body structure, filter criteria, and field values are correctly formatted. [application/json]
    > Bad request response for Create Audit Log Export.
    oneOf:
      - `CreateAuditLogExportDirectError` — Error raised before the criteria are validated, returned without the audit_log_export wrapper.
        oneOf:
          - `CreateAuditLogExportDirectErrorMandatoryNotFound` — The request body is missing the audit_log_export key.
            - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code.
            - `message` (string) **REQ** [maxLen=256] — Error message.
            - `status` (string) **REQ** [enum=['error']] — Error status.
            - `details` (object `AuditLogExportErrorFieldPointer`) **REQ** — Pointer to the request field that caused the error.
          - `CreateAuditLogExportDirectErrorInvalidData` — The request body has the wrong data type at the top level.
            - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code.
            - `message` (string) **REQ** [maxLen=256] — Error message.
            - `status` (string) **REQ** [enum=['error']] — Error status.
            - `details` (object) **REQ** — Details of the invalid value.
              - `api_name` (string) **REQ** [maxLen=64] — API name of the field that caused the error.
              - `json_path` (string) **REQ** [maxLen=256] — JSON path of the field within the request body.
              - `expected_data_type` (string) **REQ** [maxLen=32] — Data type expected for this field.
          - `CreateAuditLogExportDirectErrorInvalidRequest` — The organization is in read-only mode, so no export can be scheduled.
            - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Error code.
            - `message` (string) **REQ** [maxLen=256] — Error message.
            - `status` (string) **REQ** [enum=['error']] — Error status.
            - `details` (object) **REQ** — Always an empty object for this error.
      - `CreateAuditLogExportWrappedError` — Error raised while validating the export criteria, wrapped in the audit_log_export array.
        - `audit_log_export` (array of object) [minItems=1, maxItems=1] **REQ** — Array containing a single error object.
          oneOf:
            - `CreateAuditLogExportErrorMandatoryNotFound` — A mandatory key inside criteria is missing.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code.
              - `message` (string) **REQ** [maxLen=256] — Error message.
              - `status` (string) **REQ** [enum=['error']] — Error status.
              - `details` (object `AuditLogExportErrorFieldPointer`) **REQ** — Pointer to the request field that caused the error.
            - `CreateAuditLogExportErrorNotSupported` — The supplied field or value is not supported by this API.
              - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Error code.
              - `message` (string) **REQ** [maxLen=256] — Error message.
              - `status` (string) **REQ** [enum=['error']] — Error status.
              - `details` (object `AuditLogExportErrorFieldPointer`) **REQ** — Pointer to the request field that caused the error.
            - `CreateAuditLogExportErrorNotAllowed` — The audited_time range spans more than 180 days.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code.
              - `message` (string) **REQ** [maxLen=256] — Error message.
              - `status` (string) **REQ** [enum=['error']] — Error status.
              - `details` (object `AuditLogExportErrorFieldPointer`) **REQ** — Pointer to the request field that caused the error.
            - `CreateAuditLogExportErrorInvalidData` — The supplied value is invalid for the given field or comparator.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code.
              - `message` (string) **REQ** [maxLen=256] — Error message.
              - `status` (string) **REQ** [enum=['error']] — Error status.
              - `details` (object) **REQ** — Details of the invalid value.
                - `api_name` (string) **REQ** [maxLen=64] — API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=256] — JSON path of the field within the request body.
                - `supported_values` (array of string) [maxItems=25] — Values accepted for this field. Present when the value is outside the allowed set.
                  items: [maxLen=64]
                - `expected_data_type` (string) [maxLen=32] — Data type expected for this field. Present when the value has the wrong type.
            - `CreateAuditLogExportErrorLimitExceeded` — An array in the request exceeds its permitted size.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Error code.
              - `message` (string) **REQ** [maxLen=256] — Error message.
              - `status` (string) **REQ** [enum=['error']] — Error status.
              - `details` (object) **REQ** — Details of the exceeded limit.
                - `api_name` (string) **REQ** [maxLen=64] — API name of the array that exceeded its limit.
                - `json_path` (string) **REQ** [maxLen=256] — JSON path of the array within the request body.
                - `limit` (string) **REQ** [maxLen=32] — Maximum number of items permitted.
            - `CreateAuditLogExportErrorExpectedFieldMissing` — Neither group nor field was supplied inside criteria.
              - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Error code.
              - `message` (string) **REQ** [maxLen=256] — Error message.
              - `status` (string) **REQ** [enum=['error']] — Error status.
              - `details` (object) **REQ** — Fields of which at least one must be supplied.
                - `expected_fields` (array of object `AuditLogExportErrorFieldPointer`) [maxItems=25] **REQ** — Candidate fields, at least one of which is required.
            - `CreateAuditLogExportErrorAmbiguityDuringProcessing` — Both id and api_name were supplied for a module value but they identify different modules.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Error code.
              - `message` (string) **REQ** [maxLen=256] — Error message.
              - `status` (string) **REQ** [enum=['error']] — Error status.
              - `details` (object) **REQ** — Fields that conflict with one another.
                - `ambiguity_due_to` (array of object `AuditLogExportErrorFieldPointer`) [maxItems=25] **REQ** — The conflicting fields.
            - `CreateAuditLogExportErrorDependentFieldMissing` — A field was supplied without its dependent field.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Error code.
              - `message` (string) **REQ** [maxLen=256] — Error message.
              - `status` (string) **REQ** [enum=['error']] — Error status.
              - `details` (object) **REQ** — The missing field and the field it depends on.
                - `dependee` (object `AuditLogExportErrorFieldPointer`) **REQ** — Pointer to the request field that caused the error.
                - `api_name` (string) **REQ** [maxLen=64] — API name of the missing field.
                - `json_path` (string) **REQ** [maxLen=256] — JSON path of the missing field within the request body.
                - `expected_data_type` (string) [maxLen=32] — Data type expected for the missing field.
            - `CreateAuditLogExportErrorDependentMismatch` — The supplied value is incompatible with the comparator it depends on.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code.
              - `message` (string) **REQ** [maxLen=256] — Error message.
              - `status` (string) **REQ** [enum=['error']] — Error status.
              - `details` (object) **REQ** — The mismatched field and the field it depends on.
                - `dependee` (object `AuditLogExportErrorFieldPointer`) **REQ** — Pointer to the request field that caused the error.
                - `api_name` (string) **REQ** [maxLen=64] — API name of the mismatched field.
                - `json_path` (string) **REQ** [maxLen=256] — JSON path of the mismatched field within the request body.
                - `expected_data_type` (string) [maxLen=32] — Data type expected for the mismatched field.
            - `CreateAuditLogExportErrorAlreadyScheduled` — An audit log export job is already scheduled for this organization.
              - `code` (string) **REQ** [enum=['ALREADY_SCHEDULED']] — Error code.
              - `message` (string) **REQ** [maxLen=256] — Error message.
              - `status` (string) **REQ** [enum=['error']] — Error status.
              - `details` (object) **REQ** — Identifier of the export job that is already scheduled.
                - `id` (string) **REQ** [maxLen=64] — Unique identifier of the already scheduled export job.

- **403**: Forbidden - the current user does not have an administrator profile, or the Audit Logs feature is not available for this organization. — Schema: `AuditLogExportForbiddenResponse` [application/json]
    > Error returned when the user lacks an administrator profile or the Audit Logs feature is unavailable.
    schema: `AuditLogExportForbiddenResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code.
    - `message` (string) **REQ** [maxLen=256] — Error message.
    - `status` (string) **REQ** [enum=['error']] — Error status.
    - `details` (object) **REQ** — Permissions the current user is missing.
      - `permissions` (array of string) [maxItems=25] **REQ** — Permissions required to perform this operation.
        items: [maxLen=128]

**Scopes:** ZohoCRM.settings.audit_logs.CREATE

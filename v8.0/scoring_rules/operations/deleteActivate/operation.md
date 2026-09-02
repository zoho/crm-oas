# DELETE /settings/automation/scoring_rules/{ruleId}/actions/activate
**Operation:** `deleteActivate` — Deactivate a scoring rule
> Deactivates an active scoring rule identified by `ruleId`, suspending its scoring evaluation without deleting it.

**Parameters:**
- `ruleId` (path, string, required) [maxLen=20]: Specifies the unique ID of the Scoring Rule to retrieve, update, activate, deactivate, delete, or clone.

**Responses:**

- **200**: Returns the operation status after the Scoring Rule is deactivated. — Schema: `ScoringRulesDeactivateSuccessResponse` [application/json]
    > Successful deactivation of a rule
    schema: `ScoringRulesDeactivateSuccessResponse`
    - `scoring_rules` (array of object `ScoringRuleResponseDetails`) [maxItems=1] — Deactivation result for the scoring rule, containing the status and details of the deactivated rule.
      schema: `ScoringRuleResponseDetails`
      - `code` (string) [maxLen=255] — Represents the result code for this per-item Scoring Rule operation.
      - `details` (object `SuccessResponseDetails`) — Represents the details returned in a successful Scoring Rule operation, including the affected rule ID and any unsaved custom fields.
        schema: `SuccessResponseDetails`
        - `unsaved_custom_fields` (array of object `UnsavedCustomFieldDetails`) [maxItems=6] — Represents an array of custom fields that could not be saved during the operation.
          schema: `UnsavedCustomFieldDetails`
          - `field_label` (string) [maxLen=100] — Represents the display name of the custom field that could not be saved.
        - `id` (string) [maxLen=25] — Represents the unique ID of the Scoring Rule affected by the operation.
        additionalProperties: any
      - `message` (string) [maxLen=255] — Response message for the scoring rule operation
      - `status` (string) [maxLen=255] — Response status for the scoring rule operation

- **400**: Returns an error response when the provided Scoring Rule ID is invalid.
**Resolution:** Verify that the ID is a valid Scoring Rule ID before retrying. — Schema: `InvalidRuleIdErrorResponse` [application/json]
    > Represents an error response returned when the provided Scoring Rule ID in the request path is invalid.
    schema: `InvalidRuleIdErrorResponse`
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this error response.
    - `details` (object) **REQ** — Represents additional details about the validation error.
      - `resource_path_index` (integer/int32) — Represents the index of the resource path element that contains the invalid identifier.
    - `message` (string) **REQ** [enum=['The id given seems to be invalid']] — Represents the error message describing the validation issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

**Scopes:** ZohoCRM.settings.scoring_rules.DELETE

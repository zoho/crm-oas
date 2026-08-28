# DELETE /settings/automation/scoring_rules
**Operation:** `deleteScoringRules` — Scoring Rules
> Permanently deletes multiple scoring rules

**Parameters:**
- `ids` (query, string, required) [maxLen=255]: Specifies the IDs of the Scoring Rules to delete, provided as a comma-separated list.

**Schemas:**
`ScoringRuleResponseDetails`:
  > Represents the per-item operation result for a Scoring Rule action, including status, code, and message.
  - `code` (string) [maxLen=255] — Represents the result code for this per-item Scoring Rule operation.
  - `details` (object `SuccessResponseDetails`) — Represents the details returned in a successful Scoring Rule operation, including the affected rule ID and any unsaved custom fields.
  - `message` (string) [maxLen=255] — Response message for the scoring rule operation
  - `status` (string) [maxLen=255] — Response status for the scoring rule operation
`SuccessResponseDetails`:
  > Represents the details returned in a successful Scoring Rule operation, including the affected rule ID and any unsaved custom fields.
  - `unsaved_custom_fields` (array of object `UnsavedCustomFieldDetails`) [maxItems=6] — Represents an array of custom fields that could not be saved during the operation.
  - `id` (string) [maxLen=25] — Represents the unique ID of the Scoring Rule affected by the operation.
  additionalProperties: any
`UnsavedCustomFieldDetails`:
  > Represents the details of a custom field that could not be saved during the operation.
  - `field_label` (string) [maxLen=100] — Represents the display name of the custom field that could not be saved.

**Responses:**

- **200**: All rules are deleted successfully — Schema: `ScoringRulesDeleteAllResponse` [application/json]
    schema: `ScoringRulesDeleteAllResponse`
    - `scoring_rules` (array of object `ScoringRuleResponseDetails`) [maxItems=20] — Deletion results for all requested scoring rules.

- **207**: Returns per-item operation statuses when some Scoring Rule IDs are invalid while others are successfully deleted. — Schema: `ScoringRulesDelete207Response` [application/json]
    > few ids are invalid and others rules are deleted.
    schema: `ScoringRulesDelete207Response`
    - `scoring_rules` (array of object `ScoringRuleResponseDetails`) [maxItems=20] — Mixed deletion results - includes success entries for deleted rules and error entries for invalid IDs.

**Scopes:** ZohoCRM.settings.scoring_rules.DELETE

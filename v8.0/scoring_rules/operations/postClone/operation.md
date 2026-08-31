# POST /settings/automation/scoring_rules/{ruleId}/actions/clone
**Operation:** `postClone` — Clone a scoring rule
> To clone a Scoring Rule in your Zoho CRM organization.

**Parameters:**
- `ruleId` (path, string, required) [maxLen=20]: Specifies the unique ID of the Scoring Rule to retrieve, update, activate, deactivate, delete, or clone.

**Request Body** — application/json `EmptyRequestBody`
> Accepts an empty JSON request body to clone the specified Scoring Rule.
  > Empty request body

**Responses:**

- **200**: Returns the operation status after the Scoring Rule is cloned. — Schema: `ScoringRuleCloneSuccessResponse` [application/json]
    > successful cloning of a rule
    schema: `ScoringRuleCloneSuccessResponse`
    - `scoring_rules` (array of object `ScoringRuleResponseDetails`) [maxItems=1] — Clone result for the scoring rule, containing the status and ID of the newly cloned rule.
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

- **400**: Returns an error response when the maximum number of active or total Scoring Rules for the layout has been reached.
**Resolution:** Deactivate or delete existing Scoring Rules before cloning. [application/json]
    oneOf:
      - `InvalidRuleIdErrorResponse` — Represents an error response returned when the provided Scoring Rule ID in the request path is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this error response.
        - `details` (object) **REQ** — Represents additional details about the validation error.
          - `resource_path_index` (integer/int32) — Represents the index of the resource path element that contains the invalid identifier.
        - `message` (string) **REQ** [enum=['The id given seems to be invalid']] — Represents the error message describing the validation issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
        - `scoring_rules` (array of object) [maxItems=25] **REQ** — Represents an array of per-item error objects in the clone Scoring Rule error response.
          oneOf:
            - `GlobalScoringRuleLimitExceededErrorResponse` — Error message indicating that the maximum number of scoring rules for a layout has been exceeded, which is capped at 10.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code **LIMIT_EXCEEDED**.
              - `details` (object) **REQ** — Represents additional validation details about the Scoring Rule limit error.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that triggered the limit exceeded error.
                - `limit` (integer/int32) — Represents the maximum number of Scoring Rules allowed per layout.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field that triggered the limit exceeded error.
              - `message` (string) **REQ** [enum=['More than 10 scoring rules cannot be created for a layout']] — Represents the error message indicating that the Scoring Rule limit per layout has been reached.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.
            - `ActiveStateLimitErrorResponse` — Represents an error response returned when the number of active Scoring Rules for a layout has reached the maximum limit of 5.
              - `code` (string) **REQ** [enum=['ACTIVE_STATE_LIMIT_EXCEEDED']] — Represents the error code **ACTIVE_STATE_LIMIT_EXCEEDED**.
              - `details` (object) **REQ** — Represents additional validation details about the active state limit error.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that triggered the active state limit error.
                - `limit` (integer/int32) — Represents the maximum number of active Scoring Rules allowed per layout.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field that triggered the active state limit error.
              - `message` (string) **REQ** [enum=['More than 5 active scoring rules cannot be created for a layout']] — Represents the error message indicating that the active Scoring Rule limit has been reached.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

**Scopes:** ZohoCRM.settings.scoring_rules.CREATE

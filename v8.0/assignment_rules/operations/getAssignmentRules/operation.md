# GET /settings/automation/assignment_rules
**Operation:** `getAssignmentRules` — Assignment Rules
> To retrieve all Assignment Rules configured in your Zoho CRM organization.

**Parameters:**
- `module` (query, string, optional) [maxLen=100]: Specify the param query module schema value for the request. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID and API name.
- `include_inner_details` (query, string, optional) [enum=['created_by.zuid', 'modified_by.zuid']]: Specify the param query include inner details value for the request.
Possible values:
**created_by.zuid** - Represents created by.zuid.
**modified_by.zuid** - Represents modified by.zuid.

**Schemas:**
`ResourceResponseObject`:
  > Resource details.
  - `name` (string) **REQ** [maxLen=255] — Represents the display name of the resource. 
  - `id` (string) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — Id of the resource
  - `_details` (object) [nullable] — _Details Schema.
  - `api_name` (string) [maxLen=255] — Represents the API name of the resource.
  - `zuid` (string/int32) [maxLen=19] — Zuid of the user resource
  additionalProperties: any

**Responses:**

- **200**: Returns the Assignment Rule response details for the completed operation. — Schema: `GetAllAssignmentRulesSuccessResponse` [application/json]
    > Get all Assignment Rules success response.
    schema: `GetAllAssignmentRulesSuccessResponse`
    - `assignment_rules` (array of object `AssignmentRuleResponseObject`) [minItems=1, maxItems=200] — Represents the list of all Assignment Rules.
      schema: `AssignmentRuleResponseObject`
      - `id` (string) **REQ** [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — ID of the resource.
      - `name` (string) **REQ** [maxLen=100, minLen=1] — Represents the name to be displayed for the Assignment Rule. 
      - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the rule. 
      - `module` (object `ResourceResponseObject`) — Resource details.
      - `description` (string) **REQ** [maxLen=250, nullable] — Purpose of the Assignment Rule.
      - `created_by` (object `ResourceResponseObject`) **REQ** — Resource details.
      - `created_time` (string/date-time) **REQ** [maxLen=255] — Represents the date and time of Assignment Rule creation. 
      - `modified_by` (object `ResourceResponseObject`) **REQ** — Resource details.
      - `modified_time` (string/date-time) **REQ** [maxLen=255] — Represents the date and time of Assignment Rule recent modification. 
      - `default_assignee` (object `DefaultAssigneeResponseObject`) **REQ** — Defines the details of the fall back user to whom the records will be assigned when owner couldn't be assigned by any of the rule entries defined. (Required)
        schema: `DefaultAssigneeResponseObject`
        - `name` (string) [maxLen=255] — Represents the display name of the default assignee. 
        - `id` (object) — Represents the iD of the default assignee. is deprecated.
          oneOf:
            - `IdSchema` (string) [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — ID of the resource.
              type: string [enum=['${CURRENTUSER}']] — To define "logged in user" as fallback user for the given Assignment Rule, set ${CURRENTUSER} as value for this field.
        - `type` (string) [enum=['user']] — Defines the type of the default assignee.
Possible values:
**user** - Represents user.
        - `resource` (object) — Represents the resource returned for the Assignment Rule operation.
          oneOf:
            - `ResourceResponseObject` — Defines the details of the default assignee
              - `name` (string) [maxLen=255] — Logged in user reference display name.
              - `api_name` (string) [enum=['${CURRENTUSER}']] — To define "logged in user" as fallback user for the given Assignment Rule, set ${CURRENTUSER} as value for this field.
Possible values:
**${CURRENTUSER}** - Represents ${currentuser}.

- **204**: Indicates that no Assignment Rule records are available for the request.

- **400**: The request contains invalid, missing, or unsupported data.
**Resolution:** The request must include valid Assignment Rule data and valid parameter values for this operation. [application/json]
    > Get All AR Possible 400 Error Response Schema.
    oneOf:
      - `ErrorResponseInvalidModule` — Error response when module given is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**INVALID_MODULE** - Represents invalid module.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
          - `param_name` (string) **REQ** [enum=['module']] — Represents the param name returned for the Assignment Rule operation.
Possible values:
**module** - Represents module. 
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**the module name given seems to be invalid** - Represents the module name given seems to be invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
      - `ErrorResponseFeatureNotSupported` — Feature not supported.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_SUPPORTED']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**FEATURE_NOT_SUPPORTED** - Represents feature not supported.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
        - `message` (string) **REQ** [enum=['Assignment rules not supported for current edition']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**Assignment rules not supported for current edition** - Represents Assignment Rules not supported for current edition.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.
      - `ErrorResponseModuleNotSupported` — Error response for a module that is valid but unsupported in Assignment Rule processes.
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**NOT_SUPPORTED** - Represents not supported.
        - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
          - `param_name` (string) **REQ** [enum=['module']] — Represents the param name returned for the Assignment Rule operation.
Possible values:
**module** - Represents module. 
        - `message` (string) **REQ** [enum=['Module not supported in assignment rules']] — Represents the error message returned when the specified module does not support Assignment Rules.
Possible values:
**Module not supported in assignment rules** - Indicates that Assignment Rules are not supported for the specified module.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.

- **403**: Permission denied for the Assignment Rule operation.
**Resolution:** The CRM administrator must grant the required Assignment Rule permission for the specified module, and the OAuth token must include the required scope. — Schema: `ErrorResponseNoPermissionToAccessAPI` [application/json]
    > If current user does not have permission to access API.
    schema: `ErrorResponseNoPermissionToAccessAPI`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the status code that identifies the result of the Assignment Rule operation.
Possible values:
**NO_PERMISSION** - Represents no permission.
    - `details` (object) **REQ** — Represents additional details about the Assignment Rule operation result.
      - `permissions` (array of string) [minItems=1, maxItems=1] **REQ** — Represents the list of required permissions. 
        items: [enum=['Crm_Implied_Api_Access']]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the message that describes the result of the Assignment Rule operation.
Possible values:
**permission denied** - Represents permission denied.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the Assignment Rule operation.
Possible values:
**error** - Represents error.

**Scopes:** ZohoCRM.settings.assignment_rules.READ

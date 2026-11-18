# GET /settings/AB_testing/actions/visitors
**Operation:** `getVisitors` — Get A/B testing visitor counts

> To retrieve the visitor count of Webform A/B Testing configurations in your Zoho CRM organization, including all tests that are currently running as well as completed ones.


**Parameters:**
- `module` (query, string, optional) [enum=['Leads']]: Specify the module API name to filter AB test configurations. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID and API name. 
Possible values:
**Leads** - Filter by the Leads module.

**Responses:**

- **200**: Returns the visitor count for all active Webform A/B Testing configurations in the specified module.
 — Schema: `GetvisitorsResponse200` [application/json]
    > Successful response returned when retrieving aggregated visitor statistics for all AB tests in a module.
    schema: `GetvisitorsResponse200`
    - `AB_testing` (array of object `GetvisitorsResponseNested`) [maxItems=1] — Represents the list of visitor statistics for each AB test in the specified module.
      schema: `GetvisitorsResponseNested`
      - `started_time` (string) [maxLen=100] — Represents the date and time when the AB test started.
      - `visitors` (integer/int32) — Represents the total number of visitors who have been exposed to the AB test.
      - `days` (integer/int32) — Represents the number of days the AB test has been running.
      - `id` (string) [maxLen=19] — Represents the unique identifier of the AB test.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: No Webform A/B Testing configurations match the specified filter criteria.

  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The module name provided in the request is invalid, or a required parameter is missing from the request.
**Resolution:** Specify a valid module API name and ensure all required parameters are included in the request. [application/json]
    > Represents the error response body for a 400 Bad Request. Returned when the module parameter is invalid (INVALID_MODULE) or when a required parameter is missing from the request (REQUIRED_PARAM_MISSING).

    anyOf:
      - `ErrorResponseCore1335454202` — Error response returned when the module name in the request is not a valid Zoho CRM module.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned when the module name in the request is not valid.
Possible values:
**INVALID_MODULE** - The module name specified in the request is not a valid Zoho CRM module.
        - `details` (object) **REQ** — Represents the details of the invalid module error.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message indicating that the module name is not valid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to an invalid module name.
      - `ErrorResponseCore216006943` — Error response returned when a required query parameter is missing from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code returned when a required query parameter is missing from the request.
Possible values:
**REQUIRED_PARAM_MISSING** - A required parameter is absent from the request.
        - `details` (object) **REQ** — Represents the details of the missing parameter error, including the name of the required parameter.
          - `param_name` (string) [maxLen=255] — Represents the name of the required query parameter that is missing from the request.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message indicating that a required parameter is missing from the request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to a missing required parameter.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to access Webform A/B Testing visitor details.
**Resolution:** The CRM administrator must grant the required Webform A/B Testing permission to the user's profile. — Schema: `PermissionDeniedErrorResponse` [application/json]
    > Error response returned when the requesting user lacks the required CRM permission to perform the action.
    schema: `PermissionDeniedErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned when the requesting user lacks the required CRM permission.
Possible values:
**NO_PERMISSION** - The user's CRM profile does not include the required permission for this action.
    - `details` (object) **REQ** — Represents the details of the permission denied error, including the list of required CRM permissions.
      - `permissions` (array of string) [maxItems=25] — Represents the list of CRM permissions required to perform this action.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message indicating that the user does not have permission to perform this action.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to insufficient CRM permissions.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.abtest.READ

# GET /settings/AB_testing/{id}/actions/check_launch_suggestions
**Operation:** `getCheckLaunchSuggestions` — Retrieve launch suggestions for an AB Testing configuration

> To retrieve Zia AI launch suggestions for a Webform A/B Testing configuration in your Zoho CRM organization, indicating whether the test is ready to launch based on conversion rate analysis.


**Parameters:**
- `id` (path, string, required) [maxLen=18]: Specify the unique [Webform ID](webforms.yaml#$.paths./settings/webforms.get).

**Responses:**

- **200**: Returns the Zia launch suggestion check result for the specified AB Testing configuration, including whether a launch suggestion is available and the conversion rates inside and outside the AB test.
 — Schema: `GetchecklaunchsuggestionsResponse200` [application/json]
    > Successful response returned when checking for Zia launch suggestions for an AB test.
    schema: `GetchecklaunchsuggestionsResponse200`
    - `AB_testing_launch_suggestions` (array of object `GETAbTestingLaunchSuggestionsNested`) [maxItems=1] **REQ** — Represents the list of Zia launch suggestions for the specified AB test.
      schema: `GETAbTestingLaunchSuggestionsNested`
      - `has_launch_suggestion` (boolean) **REQ** — Indicates whether Zia has a launch suggestion for the AB test based on conversion rate comparison.
Possible values:
**true** - A launch suggestion is available.
**false** - No launch suggestion is available.
      - `conversion_rate_in_abtest` (integer/int32) **REQ** — Represents the conversion rate of the webform during the AB test period, as a percentage.
      - `conversion_rate_outside_abtest` (integer/int32) **REQ** — Represents the conversion rate of the webform outside the AB test period, as a percentage.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request was not processed because the AB Testing ID in the request path is invalid.
**Resolution:** The caller must verify that the AB Testing ID specified in the request path is a valid numeric identifier of up to 18 characters.
 — Schema: `ErrorResponseCore1388195357` [application/json]
    > Error response returned when a path segment in the request URL contains invalid data.
    schema: `ErrorResponseCore1388195357`
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a resource path in the request URL contains invalid data.
Possible values:
**INVALID_DATA** - The value at the specified resource path index is not valid.
    - `details` (object) **REQ** — Represents the details of the invalid resource path error, including the index of the invalid path segment.
      - `resource_path_index` (integer/int32) — Represents the index of the path segment in the request URL that contains the invalid value.
    - `message` (string) **REQ** [enum=[3 values]] — Represents the error message indicating that the resource path data is invalid.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to an invalid resource path.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The request was rejected because the user does not have permission to access AB Testing data.
**Resolution:** A Zoho CRM administrator must grant the user's profile access to the Webform AB Testing permission to perform this operation.
 — Schema: `ErrorResponseCore949217572` [application/json]
    > Error response returned when the requesting user lacks the required CRM permission to perform the action.
    schema: `ErrorResponseCore949217572`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned when the requesting user lacks the required permission.
Possible values:
**NO_PERMISSION** - The user's CRM profile does not include the required permission for this action.
    - `details` (object) **REQ** — Represents the details of the permission denied error, including the list of required permissions.
      - `permissions` (array of string) [maxItems=25] **REQ** — Represents the list of CRM permissions required to perform this action.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message indicating that access is denied.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to insufficient permissions.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.abtest.READ

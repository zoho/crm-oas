# GET /settings/AB_testing/{id}/actions/suggestions
**Operation:** `getAbTestingSuggestions` — Get AB testing optimization suggestions
> To retrieve optimization suggestions for a specific AB test configuration in your Zoho CRM organization, based on the current performance of the base form and variant forms.

Two types of suggestions are provided:
- **split_suggestion**: Recommends adjusting traffic allocation when a variant form is underperforming relative to other forms.
- **extend_test**: Recommends extending the test duration when results are inconclusive after the test completes.

**Parameters:**
- `id` (path, string, required) [maxLen=18]: Specify the unique [Webform ID](webforms.yaml#$.paths./settings/webforms.get).

**Responses:**

- **200**: Returns the suggestions for the specified AB test, including split suggestions and extend-test recommendations based on current performance. — Schema: `GetsuggestionsResponse200` [application/json]
    > Successful response returned when retrieving AI-generated optimization suggestions for an AB test.
    schema: `GetsuggestionsResponse200`
    - `AB_testing_suggestions` (array of object `GETAbTestingSuggestionsNested`) [maxItems=1] **REQ** — Represents the list of AI-generated optimization suggestions for the AB test.
      schema: `GETAbTestingSuggestionsNested`
      - `suggestion_details` (object `GETSuggestionDetailsNested`) **REQ** — Represents the detailed performance data for an AB test suggestion, including metrics for the base form and all variant forms.
        schema: `GETSuggestionDetailsNested`
        - `variant_form` (array of object `GETVariantFormNested`) [maxItems=2] **REQ** — Represents the list of variant webforms included in the AB test suggestion details, each with their performance metrics.
          schema: `GETVariantFormNested`
          - `underperforming_variant` (boolean) **REQ** — Indicates whether the variant form is identified as underperforming in the AB test.
Possible values:
**true** - The variant form is underperforming.
**false** - The variant form is not underperforming.
          - `name` (string) **REQ** [maxLen=255] — Represents the name of the variant webform.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the variant webform in the suggestion details.
          - `no_of_submission` (integer/int32) **REQ** — Represents the total number of form submissions received by the variant webform during the AB test.
          - `conversion_rate` (integer/int32) **REQ** — Represents the conversion rate of the variant webform during the AB test, as a percentage.
          - `no_of_visits` (integer/int32) **REQ** — Represents the total number of visitor sessions on the variant webform during the AB test.
          - `traffic` (integer/int32) **REQ** — Represents the percentage of visitor traffic currently allocated to the variant webform.
        - `base_form` (object `GETBaseFormNested`) **REQ** — Represents the base webform performance data in an AB test suggestion, including submission counts, visits, and traffic allocation.
          schema: `GETBaseFormNested`
          - `underperforming_variant` (boolean) **REQ** — Indicates whether the base form is identified as the underperforming variant in the AB test.
Possible values:
**true** - The base form is underperforming.
**false** - The base form is not underperforming.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the base webform in the suggestion details.
          - `no_of_submission` (integer/int32) **REQ** — Represents the total number of form submissions received by the base webform during the AB test.
          - `no_of_visits` (integer/int32) **REQ** — Represents the total number of visitor sessions on the base webform during the AB test.
          - `traffic` (integer/int32) **REQ** — Represents the percentage of visitor traffic currently allocated to the base webform.
      - `type` (string) **REQ** [maxLen=255] — Represents the type of AI-generated suggestion for the AB test.
Possible values:
**split_suggestion** - A recommendation to adjust traffic allocation between forms.
**extend_test** - A recommendation to continue the test for a longer period.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: Returns no content when no suggestions are available for the specified AB test.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The AB test ID in the request path is invalid.
**Resolution:** The AB test ID in the request URL must be a valid numeric identifier. — Schema: `ErrorResponseCore1388195357` [application/json]
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

- **403**: Permission denied to retrieve suggestions for this AB test.
**Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `ErrorResponseCore949217572` [application/json]
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

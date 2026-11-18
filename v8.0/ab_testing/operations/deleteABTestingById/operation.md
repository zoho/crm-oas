# DELETE /settings/AB_testing/{id}
**Operation:** `deleteABTestingById` — Delete an A/B Testing configuration by ID

> To delete a Webform A/B Testing configuration by its unique ID
 from your Zoho CRM organization. 

**Notes:**   
 - Deleting an A/B test is permanent. The test configuration and all metrics
 collected for it are removed and cannot be recovered.
 - The variant webforms that were created as part of this A/B test are deleted
 along with the test. Variants are configured and owned by the A/B test;
 they are not stand-alone webforms.
 - The base (original) webform referenced by base_form.id is not deleted.
 Only the A/B test and its variants are removed.
 - An A/B test can be deleted from any lifecycle state: drafted, scheduled,
   running, paused, completed, or launched. If the test is currently running
   or paused, the deletion stops serving variants immediately, and all visitors
   are directed to the base webform.


**Parameters:**
- `id` (path, string, required) [maxLen=19]: Specify the unique [AB Testing ID](ab_testing.yaml#$.paths./settings/AB_testing.get).
- `module` (query, string, required) [enum=['Leads']]: Specify the module API name for the AB test operation. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID and API name. 
Possible values:
**Leads** - Target the Leads module.

**Responses:**

- **200**: Returns the result of the A/B test deletion. The response contains an **AB_testing** array with one object indicating the outcome of the delete operation.
 — Schema: `Delete111111000000122003Response200` [application/json]
    > Successful response returned after deleting an AB test configuration.
    schema: `Delete111111000000122003Response200`
    - `AB_testing` (array of object `AbTestingNested201`) [maxItems=1] — Represents the list of results for the AB test delete operation.
      schema: `AbTestingNested201`
      - `code` (string) [maxLen=255] — Represents the status code of the AB test operation result.
Possible values:
**SUCCESS** - The operation completed successfully.
      - `details` (object `DetailsNested`) — Represents the details returned in a successful AB test operation response, including the ID of the affected record.
        schema: `DetailsNested`
        - `id` (string) [maxLen=19] — Represents the unique identifier of the AB test record affected by the operation.
      - `message` (string) [maxLen=255] — Represents the message describing the result of the AB test operation.
      - `status` (string) [maxLen=255] — Represents the status of the AB test operation.
Possible values:
**success** - The AB test operation completed successfully.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request could not be processed due to an invalid A/B test ID, an invalid module name, or a missing required module parameter.
**Resolution:** Verify the A/B test ID using the Get A/B Testing API and ensure the **module** query parameter is included with a valid module API name.
 [application/json]
    > Error response body for HTTP 400 on the deleteABTestingById operation. Represents one of the following error conditions: invalid A/B test ID, invalid module name, or missing required module parameter.

    anyOf:
      - `ErrorResponseCore1388195357` — Error response returned when a path segment in the request URL contains invalid data.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a resource path in the request URL contains invalid data.
Possible values:
**INVALID_DATA** - The value at the specified resource path index is not valid.
        - `details` (object) **REQ** — Represents the details of the invalid resource path error, including the index of the invalid path segment.
          - `resource_path_index` (integer/int32) — Represents the index of the path segment in the request URL that contains the invalid value.
        - `message` (string) **REQ** [enum=[3 values]] — Represents the error message indicating that the resource path data is invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to an invalid resource path.
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
      - `ErrorResponseCore94581445` — Error response returned when a required query parameter is missing from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code returned when a required query parameter is missing from the request.
Possible values:
**REQUIRED_PARAM_MISSING** - A required parameter is absent from the request.
        - `details` (object) **REQ** — Represents the details of the missing parameter error, including the name of the required parameter.
          - `param_name` (string) [maxLen=255] — Represents the name of the required query parameter that is missing from the request.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message indicating that a required parameter is missing from the request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to a missing required parameter.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to perform the delete operation on this A/B Testing configuration.
**Resolution:** The CRM administrator must grant the required permission to the user's profile, and the OAuth token must include the **ZohoCRM.settings.abtest.DELETE** or **ZohoCRM.settings.abtest.ALL** scope.
 — Schema: `PermissionDeniedErrorResponse` [application/json]
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

**Scopes:** ZohoCRM.settings.abtest.DELETE

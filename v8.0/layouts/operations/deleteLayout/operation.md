# DELETE /settings/layouts/{id}
**Operation:** `deleteLayout` — Delete a custom layout
> To delete a custom layout from a module in your Zoho CRM organization. When the layout being deleted has associated records, a target layout must be specified to receive the transferred records and profile associations. If the layout has an associated pipeline, the target pipeline and stage must also be provided. Specifying a transfer target is optional only when the layout is deactivated and has no associated records. Only one custom layout can be deleted per API call, and the standard layout cannot be deleted.

**Parameters:**
- `id` (path, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$]: Specify the unique identifier of the layout. Refer to the [Get Layouts](layouts.yaml#$.paths./settings/layouts.get) resource for valid values.
- `module` (query, string, required) [maxLen=50]: Specify the API name of the required module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
- `transfer_to` (query, string/int64, optional) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$]: Specify the ID of the layout to which records associated with the current layout move upon layout deletion or deactivation. Refer to the [Get Layouts](layouts.yaml#$.paths./settings/layouts.get) resource for valid values.
- `pipeline` (query, string/int64, optional) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$]: Specify the ID of the pipeline to transfer records to when deleting or deactivating a layout. Refer to the [Get Pipelines](pipeline.yaml#$.paths./settings/pipeline.get) resource for valid values.
- `stage` (query, string/int64, optional) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$]: Specify the ID of the stage within the pipeline to assign transferred records when deleting or deactivating a layout. Refer to the [Get Pipelines](pipeline.yaml#$.paths./settings/pipeline.get) resource for valid values.

**Schemas:**
`ErrorDetails`:
  > Contains additional context-specific details accompanying an API error response, providing structured diagnostics such as the offending parameter name, expected data type, supported values, or dependency information.
  - `param_name` (string) [maxLen=100] — Identifies the specific request parameter whose value or absence triggered the error, enabling targeted correction of the offending input.
  - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Resource ID related to the error, if applicable.
  - `expected_data_type` (string) [maxLen=50] — Indicates the data type that the API expects for the parameter that failed validation, enabling callers to correct the value format before retrying the request.
  - `supported_values` (array of string) [maxItems=10] — Contains the discrete values accepted for the parameter identified in the error, providing a reference set to correct the offending request.
    items: [maxLen=100]
  - `dependee` (object) — Contains structured information about the controlling parameter whose presence or value is required before the missing dependent parameter becomes valid or applicable.
    - `param_name` (string) [maxLen=100] — Identifies the API parameter name of the dependee — the controlling parameter that must be supplied or satisfied to make the associated dependent parameter applicable in the request.
  - `resource_path_index` (integer/int32) — Indicates the zero-based position within a multi-segment URL path at which the invalid or unrecognised segment was detected, helping to locate the exact portion of the resource path that caused the error.
  - `permissions` (array of string) [maxItems=20] — Contains the set of OAuth permission scopes that must be granted to the authenticating user or application before the requested action can be completed. Returned when the request is denied due to insufficient permissions.
    items: [maxLen=100]
  additionalProperties: any
`ErrorResponse`:
  > Represents the standard error response structure returned by the API when a request fails, containing a structured error code, a descriptive message, and a status indicator.
  - `code` (string) **REQ** [enum=[11 values]] — Identifies the category of error returned by the API. Possible values: `REQUIRED_PARAM_MISSING` — a mandatory parameter was absent from the request; `DEPENDENT_PARAM_MISSING` — a parameter required by another supplied parameter was not provided; `INVALID_MODULE` — the specified module does not exist or is not accessible; `INVALID_DATA` — one or more field values failed validation; `NOT_SUPPORTED` — the requested operation is not supported for the target resource; `NOT_ALLOWED` — the operation is not permitted in the current context; `AUTHENTICATION_FAILURE` — the supplied credentials could not be verified; `OAUTH_SCOPE_MISMATCH` — the OAuth token does not carry the scope required for the operation; `INVALID_REQUEST_METHOD` — the HTTP method used is not accepted by the endpoint; `INTERNAL_ERROR` — an unexpected server-side failure occurred; `NO_PERMISSION` — the authenticated user lacks the CRM profile permission needed to perform the action.
  - `details` (object `ErrorDetails`) **REQ** — Contains additional context-specific details accompanying an API error response, providing structured diagnostics such as the offending parameter name, expected data type, supported values, or dependency information.
  - `message` (string) **REQ** [maxLen=1000] — Contains a short, descriptive explanation of the error condition, providing context that supplements the structured error code.
  - `status` (string) **REQ** [enum=['error']] — Indicates the outcome of the request. Possible values: `error` — the request did not complete successfully and the response body contains error details.

**Responses:**

- **200**: Successful response returned when one or more layouts complete the deletion operation. Contains the per-layout deletion outcome. — Schema: `DeleteLayoutSuccessResponseBody` [application/json]
    > Represents the response body returned when one or more layouts are successfully deleted, containing per-layout deletion results.
    schema: `DeleteLayoutSuccessResponseBody`
    - `layouts` (array of object `DeleteLayoutResult`) [minItems=1, maxItems=1] **REQ** — Contains one entry per layout included in the deletion request, each reporting the individual outcome — such as success or failure — for that specific layout.
      schema: `DeleteLayoutResult`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Indicates the outcome code returned for the layout deletion attempt. Possible values: `SUCCESS` — the layout deletion completes successfully.
      - `details` (object `DeleteLayoutDetails`) **REQ** — Represents the identifying details of a layout that has been successfully deleted, returned in the deletion response to confirm which layout was removed.
        schema: `DeleteLayoutDetails`
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Unique identifier of the deleted layout.
      - `message` (string) **REQ** [maxLen=500] — Contains a descriptive message summarising the outcome of the layout deletion operation, providing context for both successful completions and failure conditions.
      - `status` (string) **REQ** [enum=['success']] — Represents the overall processing state of the layout deletion request. Possible values: `success` — the layout was removed as requested.

- **400**: Bad request response returned when a layout deletion request contains invalid or missing parameters, or when the requested deletion action is not permitted due to existing associations. [application/json]
    oneOf:
      - `ErrorResponse` — Represents the standard error response structure returned by the API when a request fails, containing a structured error code, a descriptive message, and a status indicator.
      - `LayoutErrorResponse` — Represents the layout-specific error response structure returned when one or more layouts in a batch operation fail, containing per-layout error entries.
        - `layouts` (array of object) [maxItems=100] **REQ** — Contains the array of layout-specific error entries, each describing a failure encountered for an individual layout within a batch operation.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED', 'INVALID_DATA']] — Represents the error classification code for the individual layout operation failure, identifying the category of problem encountered.
          - `details` (object `LayoutErrorDetails`) **REQ** — Represents error details specific to layout operations, providing structured diagnostics such as the offending parameter name, JSON path, and any dependency or limit information relevant to the failure.
            schema: `LayoutErrorDetails`
            - `action` (string) [maxLen=255] — Represents the operation that was being executed when the error occurred, providing context for diagnosing which layout action — such as update, delete, or deactivate — triggered the failure.
            - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Resource ID related to the error, if applicable.
            - `resource_path_index` (integer/int32) — Indicates the zero-based position within the request resource path at which the invalid or unrecognised segment was detected, helping to locate the exact path segment that caused the layout operation error.
            - `param_name` (string) [maxLen=100] — Identifies the specific request parameter whose value or absence caused the layout operation to fail, enabling targeted correction of the offending input.
            additionalProperties: any
          - `message` (string) **REQ** [maxLen=1000] — Contains a descriptive explanation of the error encountered for this individual layout operation, providing context for diagnosing the failure.
          - `status` (string) **REQ** [enum=['error']] — Indicates the outcome of the layout operation. Possible values: `error` — the layout operation did not complete successfully.

- **401**: Unauthorized response returned when authentication fails or the provided credentials are invalid or missing. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API when a request fails, containing a structured error code, a descriptive message, and a status indicator.

- **403**: Permission denied to delete the layout. **Resolution:** The Zoho CRM administrator grants the user's profile the CRM customization permission required to delete layouts. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API when a request fails, containing a structured error code, a descriptive message, and a status indicator.

- **500**: Internal server error response returned when an unexpected failure occurs on the server side while processing the request. — Schema: `ErrorResponse` [application/json]
    > Represents the standard error response structure returned by the API when a request fails, containing a structured error code, a descriptive message, and a status indicator.

**Scopes:** ZohoCRM.settings.layouts.DELETE

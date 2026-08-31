# GET /settings/pipeline
**Operation:** `getPipelines` — Pipelines
> Retrieve all pipelines available for the specified Deals layout. Use the required layout_id query parameter to identify the layout.

**Parameters:**
- `layout_id` (query, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$]: Specify the Layout ID of the Deals module. Use the [Get Layouts Metadata API](layouts.yaml#$.paths./settings/layouts.get) to retrieve the Layout ID.

**Responses:**

- **200**: Successfully retrieved all pipelines configured for the given layout. — Schema: `PipelineGetResponse` [application/json]
    > Root response object containing all pipeline configurations configured for a given Deals layout in Zoho CRM.
    schema: `PipelineGetResponse`
    - `pipeline` (array of object) [minItems=1, maxItems=90] **REQ** — Array of pipeline configuration items.
      - `display_value` (string/string) **REQ** — Display name of the picklist value as shown to users.
      - `default` (boolean) — Indicates if this is the default picklist value.
      - `maps` (array of object) [minItems=1, maxItems=200] **REQ** — Array of stage mappings for this picklist value.
        - `display_value` (string/string) **REQ** — User-facing display name of the pipeline stage.
        - `sequence_number` (integer/int32) **REQ** — Position of this stage in the pipeline sequence (1-based indexing).
        - `colour_code` (string/string) — Hexadecimal color code associated with the stage for UI representation.
        - `forecast_category` (object) **REQ** — Represents a forecast category used in sales pipeline stages for revenue forecasting and reporting.
          - `name` (string/string) **REQ** — Represents the name of the forecast category (e.g., 'Pipeline', 'Closed', 'Omitted').
          - `id` (string/int64) **REQ** — Unique system identifier for the forecast category.
        - `actual_value` (string/string) **REQ** — Internal system value/API name for the stage.
        - `id` (string/int64) **REQ** — Unique identifier for this stage mapping.
        - `forecast_type` (string/string) **REQ** — Forecast type indicating stage status (e.g., 'Open', 'Closed Won', 'Closed Lost').
      - `actual_value` (string/string) **REQ** — Internal API value for the picklist option.
      - `id` (string/int64) **REQ** — Unique identifier for this picklist value.

- **204**: No pipeline records were found for the given layout.

- **400**: The request is invalid, for example when the layout_id is invalid. — Schema: `PipelineGetErrorResponse` [application/json]
    > Standard error response format used across API endpoints for validation and business logic errors.
    schema: `PipelineGetErrorResponse`
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating the type of error (e.g., 'INVALID_DATA', 'RESOURCE_NOT_FOUND').
    - `details` (object) **REQ** — Additional context about the specific error, typically identifying the problematic parameter.
      - `param_name` (string/string) **REQ** [enum=['layout_id']] — Name of the parameter that caused the validation error.
    - `message` (string/string) **REQ** — Represents the error messsage.
    - `status` (string) **REQ** [enum=['error']] — Overall status indicator ('error' or 'success').

**Scopes:** ZohoCRM.settings.pipeline.READ

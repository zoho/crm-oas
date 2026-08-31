# POST /settings/pipeline
**Operation:** `createPipeline` — Pipeline
> Create a new pipeline for the specified Deals layout by providing a pipeline display label and one or more mapped stages.

**Parameters:**
- `layout_id` (query, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$]: Specify the Layout ID of the Deals module. Use the [Get Layouts Metadata API](layouts.yaml#$.paths./settings/layouts.get) to retrieve the Layout ID.

**Request Body** (required) — application/json `PipelineCreateRequest`
  > Request body for creating a pipeline configuration with a custom pipeline label and mapped stage values for a specific Deals layout.
  - `pipeline` (array of object) [minItems=1, maxItems=1] **REQ** — Array of pipeline picklist configurations to create or update.
    - `display_value` (string/string) **REQ** — User-facing display name for the picklist value.
    - `default` (boolean) — Indicates if this picklist value should be set as the default option.
    - `maps` (array of object) [minItems=1, maxItems=200] **REQ** — Array of stage mappings defining which stages this picklist value connects to and their sequence.
      - `id` (string/int64) **REQ** — Unique identifier of the target pipeline stage to map.
      - `display_value` (string/string) — User-facing display name for the pipeline stage.
      - `sequence_number` (integer/int32) — Optional position of this stage mapping in the pipeline sequence (overrides default positioning).

**Responses:**

- **201**: Success Response — Schema: `PipelineSuccessResponse` [application/json]
    > Batch success response for pipeline creation/update operations, maintaining 1:1 correspondence with request items.
    schema: `PipelineSuccessResponse`
    - `pipeline` (array of object) [minItems=1, maxItems=1] **REQ** — Array of individual success responses matching the request pipeline items.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the success code indicating the type of successful operation.
      - `details` (object) **REQ** — Operation-specific success details including resource identifiers.
        - `id` (string/int64) **REQ** — Unique identifier of the newly created pipeline configuration.
      - `message` (string/string) **REQ** — Represents the confirmation of the successful operation.
      - `status` (string) **REQ** [enum=['success']] — Overall status indicator.

- **400**: The request body or layout_id is invalid, or mandatory fields required to create the pipeline are missing. [application/json]
    oneOf:
      - `PipelineCreateErrorResponse` — Batch error response for pipeline operations maintaining 1:1 correspondence with request items when validation fails.
        - `pipeline` (array of object) [minItems=1, maxItems=1] **REQ** — Array of individual error responses matching the request pipeline items.
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA', 'INVALID_DATA', 'MANDATORY_NOT_FOUND']] — Represents the error code indicating the specific validation failure.
          - `details` (object) **REQ** — Error-specific context including field name and JSON path location.
            - `api_name` (string/string) **REQ** — API field name that caused the error.
            - `json_path` (string/string) **REQ** — JSON path pointing to the exact location of the error in the request.
          - `message` (string/string) **REQ** — Represents the explanation of the specific error.
          - `status` (string) **REQ** [enum=['error']] — Overall status indicator for this item.
      - `PipelineGetErrorResponse` — Standard error response format used across API endpoints for validation and business logic errors.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating the type of error (e.g., 'INVALID_DATA', 'RESOURCE_NOT_FOUND').
        - `details` (object) **REQ** — Additional context about the specific error, typically identifying the problematic parameter.
          - `param_name` (string/string) **REQ** [enum=['layout_id']] — Name of the parameter that caused the validation error.
        - `message` (string/string) **REQ** — Represents the error messsage.
        - `status` (string) **REQ** [enum=['error']] — Overall status indicator ('error' or 'success').

- **403**: The user does not have permission to create or customize pipelines in Zoho CRM. — Schema: `NoPermissionErrorResponse` [application/json]
    > Error response when the user lacks required permissions to perform the operation.
    schema: `NoPermissionErrorResponse`
    - `code` (string) [enum=['NO_PERMISSION']] — Represents the error code indicating the type of error (e.g., 'NO_PERMISSION').
    - `details` (object) — Additional context about the specific error.
      - `permissions` (string/string) — The required permission that is missing.
    - `message` (string/string) — Represents the explanation of the error suitable for display to end users.
    - `status` (string/string) — Overall status indicator ('error' or 'success').

**Scopes:** ZohoCRM.settings.pipeline.CREATE

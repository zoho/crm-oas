# POST /settings/pipeline/actions/transfer
**Operation:** `transferAndDeletePipelines` — Transfer Pipeline
> Transfer records and stage mappings from one pipeline to another in the specified layout, and delete the source pipeline after the transfer is scheduled.

**Parameters:**
- `layout_id` (query, string/int64, required) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$]: Specify the Layout ID of the Deals module. Use the [Get Layouts Metadata API](layouts.yaml#$.paths./settings/layouts.get) to retrieve the Layout ID.

**Request Body** (required) — application/json `PipelineTransferResponse`
  > Response confirming pipeline transfer operation with source-to-target mappings for pipeline and stages.
  - `transfer_pipeline` (array of object) [minItems=1, maxItems=1] **REQ** — Array of pipeline transfer mappings showing source and target configurations.
    - `pipeline` (object) **REQ** — Pipeline-level transfer mapping from source to target pipeline.
      - `from` (string/int64) **REQ** — Source pipeline ID.
      - `to` (string/int64) **REQ** — Target pipeline ID.
    - `stages` (array of object) [minItems=1, maxItems=200] **REQ** — Array of stage mappings showing which stages transferred to which target stages.
      - `from` (string/int64) **REQ** — Source stage ID.
      - `to` (string/int64) **REQ** — Target stage ID.

**Responses:**

- **200**: The pipeline transfer and delete operation was scheduled successfully. — Schema: `PipelineTransferSuccessResponse` [application/json]
    > Success response for pipeline transfer scheduling operation with job tracking information.
    schema: `PipelineTransferSuccessResponse`
    - `transfer_pipeline` (array of object) [minItems=1, maxItems=1] **REQ** — Array of pipeline transfer scheduling results maintaining 1:1 correspondence with request.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the success code indicating the type of successful operation.
      - `details` (object) **REQ** — Success details including the scheduled job identifier.
        - `job_id` (string/int64) **REQ** — Unique identifier of the scheduled pipeline transfer job for tracking.
      - `message` (string/string) **REQ** — Represents the confirmation of the pipeline transfer scheduling.
      - `status` (string) **REQ** [enum=['success']] — Overall status indicator.

- **400**: The request is invalid due to invalid source or target pipeline or stage IDs, duplicate stage mappings, invalid layout_id, missing required fields, or a transfer that is already scheduled. [application/json]
    oneOf:
      - `PipelineTransferErrorResponse` — Batch error response for pipeline transfer operations with detailed validation failure information.
        - `transfer_pipeline` (array of object) [minItems=1, maxItems=1] **REQ** — Array of individual pipeline transfer error responses matching request items.
          - `code` (string) **REQ** [enum=['INVALID_DATA', 'MANDATORY_NOT_FOUND', 'ALREADY_SCHEDULED', 'ALREADY_USED']] — Represents the error code for the validation failure.
          - `details` (object) **REQ** — Represents the error context identifying the problematic field and its location.
            - `api_name` (string/string) — Represents the API field name that failed validation.
            - `value` (string/string) — Represents the invalid value that caused the error.
            - `exists_in` (object) — Represents where the value already exists.
              - `json_path` (string/string) — JSON path where the value already exists.
            - `json_path` (string/string) — JSON path to the exact location of the validation error.
          - `message` (string/string) **REQ** — error explanation.
          - `status` (string) **REQ** [enum=['error']] — Error status indicator.
      - `PipelineGetErrorResponse` — Standard error response format used across API endpoints for validation and business logic errors.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code indicating the type of error (e.g., 'INVALID_DATA', 'RESOURCE_NOT_FOUND').
        - `details` (object) **REQ** — Additional context about the specific error, typically identifying the problematic parameter.
          - `param_name` (string/string) **REQ** [enum=['layout_id']] — Name of the parameter that caused the validation error.
        - `message` (string/string) **REQ** — Represents the error messsage.
        - `status` (string) **REQ** [enum=['error']] — Overall status indicator ('error' or 'success').

- **403**: The user does not have permission to transfer or delete pipelines in Zoho CRM. — Schema: `NoPermissionErrorResponse` [application/json]
    > Error response when the user lacks required permissions to perform the operation.
    schema: `NoPermissionErrorResponse`
    - `code` (string) [enum=['NO_PERMISSION']] — Represents the error code indicating the type of error (e.g., 'NO_PERMISSION').
    - `details` (object) — Additional context about the specific error.
      - `permissions` (string/string) — The required permission that is missing.
    - `message` (string/string) — Represents the explanation of the error suitable for display to end users.
    - `status` (string/string) — Overall status indicator ('error' or 'success').

**Scopes:** ZohoCRM.settings.pipeline.CREATE

# Examples: deleteLayout

**DELETE /settings/layouts/{id}**

## Parameter examples

### `id` (path) — ValidId

Valid layout ID

```json
"111111000000098320"
```

### `module` (query) — StandardModule

Standard module

```json
"Leads"
```

### `module` (query) — CustomModule

Custom module

```json
"Custom_Projects"
```

### `transfer_to` (query) — TransferLayoutId

Transfer to layout ID

```json
"111111000000337001"
```

### `pipeline` (query) — PipelineId

Pipeline ID

```json
"111111000000098500"
```

### `stage` (query) — StageId

Stage ID

```json
"111111000000098510"
```

## Response examples

### Status `200` — `application/json` — LayoutDeleted

Layout successfully deleted

```json
{
  "layouts": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111112000000337004"
      },
      "message": "layout deleted",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MissingTransferTo

Required transfer_to parameter missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "transfer_to"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — MissingModule

Required module parameter missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "module"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — MissingPipeline

Required pipeline parameter missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "pipeline"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — MissingStage

Required stage parameter missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "stage"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — LayoutNotFound

Layout not found with given ID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "No layout found with given id",
  "status": "error"
}
```

### Status `400` — `application/json` — LayoutNotFoundWrapped

Layout not found (wrapped in layouts array)

```json
{
  "layouts": [
    {
      "code": "INVALID_DATA",
      "details": {
        "resource_path_index": 2
      },
      "message": "No layout found with given id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidTransferToLayout

Invalid transfer_to layout ID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "transfer_to"
  },
  "message": "Transfer To Layout Id is Invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — TransferToDeactivatedLayout

Cannot transfer to deactivated layout

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "param_name": "transfer_to"
  },
  "message": "Cannot transfer to the deactivated layout",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module name provided

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidLayoutId

Invalid layout ID format

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "id",
    "expected_data_type": "int64"
  },
  "message": "The id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidRequestMethod

Invalid HTTP method used

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The http request method type is not a valid one",
  "status": "error"
}
```

### Status `400` — `application/json` — DependentPipelineParamMissing

Dependent pipeline parameter missing

```json
{
  "code": "DEPENDENT_PARAM_MISSING",
  "details": {
    "dependee": {
      "param_name": "transfer_to"
    },
    "param_name": "pipeline"
  },
  "message": "Cannot delete layout as pipeline is not specified for trasfer_to layout",
  "status": "error"
}
```

### Status `400` — `application/json` — DependentStageParamMissing

Dependent stage parameter missing

```json
{
  "code": "DEPENDENT_PARAM_MISSING",
  "details": {
    "dependee": {
      "param_name": "transfer_to"
    },
    "param_name": "stage"
  },
  "message": "Cannot delete layout as stage is not specified for trasfer_to layout",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailure

Authentication failure

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```

### Status `401` — `application/json` — OAuthScopeMismatch

OAuth scope mismatch

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "Invalid oauth scope to access this URL",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermission

User lacks permission to delete the layout

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Customize_Zoho_CRM"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```

### Status `500` — `application/json` — InternalError

Server error

```json
{
  "code": "INTERNAL_ERROR",
  "details": {},
  "message": "Internal Server Error",
  "status": "error"
}
```

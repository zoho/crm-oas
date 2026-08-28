# Examples: replacePipelineById

**PUT /settings/pipeline/{pipelineIdentifier}**

## Request examples

### `application/json` — PipelineUpdateRequest

```json
{
  "pipeline": [
    {
      "display_value": "adfadf12adf",
      "default": false,
      "maps": [
        {
          "id": "2766660000000007106",
          "sequence_number": 2
        },
        {
          "id": "2766660000000007104",
          "sequence_number": 1
        }
      ]
    }
  ]
}
```

### `application/json` — PipelineDeleteRequest

```json
{
  "pipeline": [
    {
      "_delete": {
        "permanent": null
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — PipelineUpdateResponse

```json
{
  "pipeline": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "2766660000055809093"
      },
      "message": "Pipeline updated",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — NoMappingFoundErrorRespones

```json
{
  "pipeline": [
    {
      "code": "INVALID_DATA",
      "details": {},
      "message": "No mapping found ",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — CannotRemoveTheLastStageErrorResponse

```json
{
  "pipeline": [
    {
      "code": "CANNOT_DELETE",
      "details": {
        "api_name": "id",
        "json_path": "$.pipeline[0].maps[0].id"
      },
      "message": "Cannot delete the last stage associated with the pipeline",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidPipelineIdInUrlErrorResponse

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "invalid pick_list_values id",
  "status": "error"
}
```

### Status `400` — `application/json` — AlreadyScheduledError

```json
{
  "pipeline": [
    {
      "code": "ALREADY_SCHEDULED",
      "details": {
        "api_name": "pipeline",
        "json_path": "$.pipeline[0].pipeline",
        "value": "2766660000056063000"
      },
      "message": "Scheduler already running for this pipeline",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicatePipelineNameError

```json
{
  "pipeline": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "display_value",
        "json_path": "$.pipeline[0].display_value"
      },
      "message": "Duplicate pipeline label found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidMapStageIDError

```json
{
  "pipeline": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.pipeline[0].maps[0].id"
      },
      "message": "Invalid child option id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DisplayValueIsNotFountError

```json
{
  "pipeline": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "display_value",
        "json_path": "$.pipeline[0].display_value"
      },
      "message": "required  field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MapIDNotFoundError

```json
{
  "pipeline": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.pipeline[0].maps[0].id"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidLayoutID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "layout_id"
  },
  "message": "Invalid layoutid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidPipelineID

```json
{
  "pipeline": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "12345678901234567890"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionErrorResponse

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": "Crm_Implied_Customize_Zoho_CRM"
  },
  "message": "permission denied to customize Zoho CRM",
  "status": "error"
}
```

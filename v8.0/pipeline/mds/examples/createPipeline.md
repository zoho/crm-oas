# Examples: createPipeline

**POST /settings/pipeline**

## Request examples

### `application/json` — PipelineCreateRequest

```json
{
  "pipeline": [
    {
      "display_value": "adfadf12adf",
      "default": true,
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

## Response examples

### Status `201` — `application/json` — PipelineCreateResponse

```json
{
  "pipeline": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "2766660000055809093"
      },
      "message": "Pipeline created successfully",
      "status": "success"
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

# Examples: updateFieldUpdateById

**PUT /settings/automation/field_updates/{id}**

## Request examples

### `application/json` — SamplePutRequest

Sample request body

```json
{
  "field_updates": [
    {
      "name": "FieldUpdatePUT",
      "module": {
        "id": "3361265000000000131",
        "api_name": "Deals"
      },
      "field": {
        "id": "3361265000000236001",
        "api_name": "Pipeline"
      },
      "value": "Test",
      "dependent_fields": [
        {
          "field": {
            "api_name": "Stage",
            "id": "3361265000000000525"
          },
          "value": "Qualification"
        }
      ],
      "related_records": [
        {
          "api_name": "Events",
          "id": "3361265000000000145"
        },
        {
          "api_name": "Calls",
          "id": "3361265000000017015"
        }
      ],
      "notify": true,
      "feature_type": "workflow",
      "type": "static",
      "apply_assignment_threshold": true,
      "update_type": "append"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "field_updates": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "3361265000006103518"
      },
      "message": "fieldupdate updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — FieldUpdatesInvalidData

Error response with code INVALID_DATA: invalid data (Field: field_updates)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "field_updates",
    "json_path": "$.field_updates"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — NameInvalidDataType1

Error response with code INVALID_DATA: the id given seems to be invalid

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

Error response with code REQUIRED_PARAM_MISSING: the id given seems to be invalid

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "id"
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — RequiredPathIdMissingPostman

Error response with code REQUIRED_PARAM_MISSING: One of the expected parameter is missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "resource_path_index": 3
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — RelatedRecordsNotAllowed1

Error response with code NOT_ALLOWED: This key is not supported for this particular action (Field: notify)

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "api_name": "notify",
    "json_path": "$.field_updates.notify"
  },
  "message": "This key is not supported for this particular action",
  "status": "error"
}
```

### Status `400` — `application/json` — ReadOnlyActionNotAllowedPostman

Error response with code NOT_ALLOWED: Insufficient privileges to edit action

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 3
  },
  "message": "Insufficient privileges to edit action",
  "status": "error"
}
```

### Status `400` — `application/json` — DependentFieldMissing1

Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: related_records)

```json
{
  "field_updates": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "field",
          "json_path": "$.field_updates[0].field"
        },
        "api_name": "related_records",
        "json_path": "$.field_updates[0].related_records"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissing2

Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: notify)

```json
{
  "field_updates": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "field",
          "json_path": "$.field_updates[0].field"
        },
        "api_name": "notify",
        "json_path": "$.field_updates.notify"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchPostman

Error response with code DEPENDENT_MISMATCH: Dependent Field is not matching

```json
{
  "field_updates": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "field",
          "json_path": "$.field_updates[0].field"
        },
        "api_name": "value",
        "json_path": "$.field_updates[0].value"
      },
      "message": "Dependent Field is not matching",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse3

Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: apply_assignment_threshold)

```json
{
  "field_updates": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "field",
          "json_path": "$.field_updates[0].field"
        },
        "api_name": "apply_assignment_threshold",
        "json_path": "$.field_updates[0].apply_assignment_threshold"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse4

Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: dependent_fields)

```json
{
  "field_updates": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "field",
          "json_path": "$.field_updates[0].field"
        },
        "api_name": "dependent_fields",
        "json_path": "$.field_updates[0].dependent_fields"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NameExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: name)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ModuleInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: module)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "module",
        "expected_data_type": "jsonobject",
        "json_path": "$.field_updates[*].module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ModuleExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.field_updates[*].module.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ModuleIdInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].module.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NameMandatoryNotFound1

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: field)

```json
{
  "field_updates": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "field",
        "json_path": "$.field_updates[*].field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ModuleIdExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: field)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.field_updates[*].field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ModuleApiNameInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.field_updates[*].field.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ModuleApiNameExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].field.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FieldInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: value)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FieldExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: dependent_fields)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "dependent_fields",
        "expected_data_type": "jsonarray",
        "json_path": "$.field_updates[*].dependent_fields"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ModuleMandatoryNotFound1

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: field)

```json
{
  "field_updates": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "field",
        "json_path": "$.field_updates[*].dependent_fields[*].field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FieldIdInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: field)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.field_updates[*].dependent_fields[*].field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FieldIdExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].dependent_fields[*].field.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FieldApiNameInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.field_updates[*].dependent_fields[*].field.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FieldMandatoryNotFound1

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: value)

```json
{
  "field_updates": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "value",
        "json_path": "$.field_updates[*].dependent_fields[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FieldApiNameExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: value)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].dependent_fields[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ValueInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: related_records)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "related_records",
        "expected_data_type": "jsonarray",
        "json_path": "$.field_updates[*].related_records"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ValueExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].related_records[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldsInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.field_updates[*].related_records[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldsExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: notify)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "notify",
        "expected_data_type": "boolean",
        "json_path": "$.field_updates[*].notify"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldFieldInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: feature_type)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "feature_type",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldFieldExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data (Field: feature_type)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "feature_type",
        "supported_values": [
          "workflow"
        ],
        "json_path": "$.field_updates[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldApiNameInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: type)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldApiNameExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "static"
        ],
        "json_path": "$.field_updates[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldIdInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: apply_assignment_threshold)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "apply_assignment_threshold",
        "expected_data_type": "boolean",
        "json_path": "$.field_updates[*].apply_assignment_threshold"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldIdExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: update_type)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "update_type",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].update_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldValueInvalidDataType1

Error response with code INVALID_DATA: Invalid data (Field: update_type)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "update_type",
        "supported_values": [
          "overwrite",
          "append"
        ],
        "json_path": "$.field_updates[*].update_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse5

Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: related_records)

```json
{
  "field_updates": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "field",
          "json_path": "$.field_updates[0].field"
        },
        "api_name": "related_records",
        "json_path": "$.field_updates[0].related_records"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse6

Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: notify)

```json
{
  "field_updates": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "field",
          "json_path": "$.field_updates[0].field"
        },
        "api_name": "notify",
        "json_path": "$.field_updates.notify"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse7

Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: apply_assignment_threshold)

```json
{
  "field_updates": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "field",
          "json_path": "$.field_updates[0].field"
        },
        "api_name": "apply_assignment_threshold",
        "json_path": "$.field_updates[0].apply_assignment_threshold"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse8

Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: dependent_fields)

```json
{
  "field_updates": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "field",
          "json_path": "$.field_updates[0].field"
        },
        "api_name": "dependent_fields",
        "json_path": "$.field_updates[0].dependent_fields"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldValueExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: name)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RelatedRecordsInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: module)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "module",
        "expected_data_type": "jsonobject",
        "json_path": "$.field_updates[*].module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RelatedRecordsExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.field_updates[*].module.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RelatedRecordApiNameInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].module.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ValueMandatoryNotFound1

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: field)

```json
{
  "field_updates": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "field",
        "json_path": "$.field_updates[*].field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RelatedRecordApiNameExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: field)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.field_updates[*].field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RelatedRecordIdInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.field_updates[*].field.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RelatedRecordIdExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].field.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotifyInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: value)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FeatureTypeInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: dependent_fields)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "dependent_fields",
        "expected_data_type": "jsonarray",
        "json_path": "$.field_updates[*].dependent_fields"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldFieldMandatoryNotFound1

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: field)

```json
{
  "field_updates": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "field",
        "json_path": "$.field_updates[*].dependent_fields[*].field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FeatureTypeUnsupportedValue1

Error response with code INVALID_DATA: Invalid data type (Field: field)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.field_updates[*].dependent_fields[*].field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FeatureTypeUnsupportedValue2

Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].dependent_fields[*].field.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — TypeInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.field_updates[*].dependent_fields[*].field.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldValueMandatoryNotFound1

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: value)

```json
{
  "field_updates": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "value",
        "json_path": "$.field_updates[*].dependent_fields[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — TypeExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: value)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].dependent_fields[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — TypeUnsupportedValue1

Error response with code INVALID_DATA: Invalid data type (Field: related_records)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "related_records",
        "expected_data_type": "jsonarray",
        "json_path": "$.field_updates[*].related_records"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ApplyAssignmentThresholdInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].related_records[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdateTypeInvalidDataType1

Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.field_updates[*].related_records[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdateTypeExceedsMaxLength1

Error response with code INVALID_DATA: Invalid data type (Field: notify)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "notify",
        "expected_data_type": "boolean",
        "json_path": "$.field_updates[*].notify"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdateTypeUnsupportedValue1

Error response with code INVALID_DATA: Invalid data type (Field: feature_type)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "feature_type",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NameInvalidDataType2

Error response with code INVALID_DATA: Invalid data (Field: feature_type)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "feature_type",
        "supported_values": [
          "workflow"
        ],
        "json_path": "$.field_updates[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NameExceedsMaxLength2

Error response with code INVALID_DATA: Invalid data type (Field: type)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ModuleInvalidDataType2

Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "static"
        ],
        "json_path": "$.field_updates[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ModuleExceedsMaxLength2

Error response with code INVALID_DATA: Invalid data type (Field: apply_assignment_threshold)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "apply_assignment_threshold",
        "expected_data_type": "boolean",
        "json_path": "$.field_updates[*].apply_assignment_threshold"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ModuleIdInvalidDataType2

Error response with code INVALID_DATA: Invalid data type (Field: update_type)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "update_type",
        "expected_data_type": "text",
        "json_path": "$.field_updates[*].update_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ModuleIdExceedsMaxLength2

Error response with code INVALID_DATA: Invalid data (Field: update_type)

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "update_type",
        "supported_values": [
          "overwrite",
          "append"
        ],
        "json_path": "$.field_updates[*].update_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse1

Error response with code NO_PERMISSION: feature not available in this edition

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow",
      "Crm_Implied_Customize_Zoho_CRM",
      "Crm_Implied_Manage_ConnectedWorkflow"
    ]
  },
  "message": "feature not available in this edition",
  "status": "error"
}
```

### Status `403` — `application/json` — LockedActionNoPermissionPostman

Error response with code NO_PERMISSION: Insufficient privileges to edit locked action

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "Insufficient privileges to edit locked action",
  "status": "error"
}
```

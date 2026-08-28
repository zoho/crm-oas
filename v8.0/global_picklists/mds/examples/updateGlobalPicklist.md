# Examples: updateGlobalPicklist

**PATCH /settings/global_picklists**

## Request examples

### `application/json` — UpdateDisplayLabel

Update display label

```json
{
  "global_picklists": [
    {
      "id": "111111000000055935",
      "display_label": "Updated Priority Level"
    }
  ]
}
```

### `application/json` — AddPicklistValue

Add new picklist value

```json
{
  "global_picklists": [
    {
      "id": "111111000000055935",
      "pick_list_values": [
        {
          "display_value": "Critical",
          "type": "used"
        }
      ]
    }
  ]
}
```

### `application/json` — UpdatePicklistValue

Update existing picklist value

```json
{
  "global_picklists": [
    {
      "id": "111111000000055935",
      "pick_list_values": [
        {
          "id": "111111000000055938",
          "display_value": "High Priority"
        }
      ]
    }
  ]
}
```

### `application/json` — MoveToUnused

Move one value to unused

```json
{
  "global_picklists": [
    {
      "id": "111111000000055935",
      "pick_list_values": [
        {
          "id": "111111000000055938",
          "type": "unused"
        }
      ]
    }
  ]
}
```

### `application/json` — DeletePicklistValue

Delete one picklist value

```json
{
  "global_picklists": [
    {
      "id": "111111000000055935",
      "pick_list_values": [
        {
          "id": "111111000000055938",
          "_delete": true
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessExample

Successful update response

```json
{
  "global_picklists": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000055935"
      },
      "message": "global picklist updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryIdNotFound

Missing id field

```json
{
  "global_picklists": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.global_picklists[0].id"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidId

Invalid global picklist id

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.global_picklists[0].id",
        "id": "11111100000005593"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — EmptyApiName

Empty api_name

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.global_picklists[0].api_name"
      },
      "message": "Api Name cannot be empty",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidApiNameFormat

Invalid api_name format

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.global_picklists[0].api_name"
      },
      "message": "Api Name should start with English alphabets followed by numbers or alphabets or underscore and should not end with underscore",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateApiName

Duplicate api_name

```json
{
  "global_picklists": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.global_picklists[0].api_name"
      },
      "message": "Duplicate Api name found, enter a unique Api name.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDisplayLabel

Duplicate display_label

```json
{
  "global_picklists": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "display_label",
        "json_path": "$.global_picklists[0].display_label"
      },
      "message": "Duplicate name found, enter a unique name.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryPickListValues

Missing pick_list_values

```json
{
  "global_picklists": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "pick_list_values",
        "json_path": "$.global_picklists[0].pick_list_values"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SpecialCharactersDisplayLabel

Special characters in display_label

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "display_label",
        "json_path": "$.global_picklists[0].display_label"
      },
      "message": "Special characters in name",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DisplayLabelMaxLength

display_label exceeds 50 characters

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 50,
        "api_name": "display_label",
        "json_path": "$.global_picklists[0].display_label"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DescriptionMaxLength

description exceeds 1000 characters

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 1000,
        "api_name": "description",
        "json_path": "$.global_picklists[0].description"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DisplayValueMaxLength

display_value exceeds 120 characters

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 120,
        "api_name": "display_value",
        "json_path": "$.global_picklists[0].pick_list_values[0].display_value"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ReferenceValueMaxLength

reference_value exceeds 120 characters

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 120,
        "api_name": "reference_value",
        "json_path": "$.global_picklists[0].pick_list_values[0].reference_value"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SpecialCharactersDisplayValue

Special characters in display_value

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "display_value",
        "json_path": "$.global_picklists[0].pick_list_values[0].display_value"
      },
      "message": "Special characters are not allowed in Options",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SpecialCharactersReferenceValue

Special characters in reference_value

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "reference_value",
        "json_path": "$.global_picklists[0].pick_list_values[0].reference_value"
      },
      "message": "Special characters are not allowed in Options",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NoUsedOption

No used option in picklist values

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "pick_list_values",
        "json_path": "$.global_picklists[0].pick_list_values"
      },
      "message": "Values in the pick list field cannot be empty.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDisplayValue

Duplicate display_value in pick_list_values

```json
{
  "global_picklists": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "pick_list_values",
        "json_path": "$.global_picklists[0].pick_list_values"
      },
      "message": "Duplicate option found. Enter a unique option.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateReferenceValue

Duplicate reference_value in pick_list_values

```json
{
  "global_picklists": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "pick_list_values",
        "json_path": "$.global_picklists[0].pick_list_values"
      },
      "message": "Duplicate reference option found. Enter a unique reference option.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ReferenceValueEmpty

reference_value is empty or null

```json
{
  "global_picklists": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "reference_value",
        "json_path": "$.global_picklists[0].pick_list_values[0].reference_value"
      },
      "message": "Actual value in pick list values cannot be empty or null",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DisplayValueEmpty

display_value is empty or null

```json
{
  "global_picklists": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "display_value",
        "json_path": "$.global_picklists[0].pick_list_values[0].display_value"
      },
      "message": "Display value in pick list values cannot be empty or null",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — EmptyDisplayLabel

display_label is empty

```json
{
  "global_picklists": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "display_label",
        "json_path": "$.global_picklists[0].display_label"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DeletionInProgress

Deletion in progress

```json
{
  "global_picklists": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "global_picklists",
        "json_path": "$.global_picklists[0]"
      },
      "message": "global picklist deletion in progress.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidOptionId

Invalid picklist value id

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.global_picklists[0].pick_list_values[503].id"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryDisplayValueForUpdate

Missing display_value for update

```json
{
  "global_picklists": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "display_value",
        "json_path": "$.global_picklists[0].pick_list_values[0].display_value"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — BulkUnusedMovement

Bulk unused movement not allowed

```json
{
  "global_picklists": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit_due_to": [
          {
            "api_name": "type",
            "json_path": "$.global_picklists[0].pick_list_values[1].type"
          }
        ],
        "limit": 1
      },
      "message": "More than one picklist value cannot be moved to unused type",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — BulkDeletion

Bulk deletion not allowed

```json
{
  "global_picklists": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit_due_to": {
          "api_name": "_delete",
          "json_path": "$.global_picklists[0].pick_list_values[1]._delete"
        },
        "limit": 1
      },
      "message": "More than one picklist value cannot be deleted",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — OptionDeleteNotAllowed

Option delete not allowed

```json
{
  "global_picklists": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "pick_list_values",
        "json_path": "$.global_picklists[0].pick_list_values[1]"
      },
      "message": "Option delete not allowed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ReplaceInProgress

Replace process in progress

```json
{
  "global_picklists": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "pick_list_values",
        "json_path": "$.global_picklists[0].pick_list_values"
      },
      "message": "Some values can not be modified since they are being deleted from the system through replacing process.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DeleteMoreThan15Fields

Cannot delete when associated with >15 fields

```json
{
  "global_picklists": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "type",
        "json_path": "$.global_picklists[0].pick_list_values[0]._delete"
      },
      "message": "option can't be deleted as global set is associated to more than 15 fields",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MoveMoreThan50ToUsed

Moving >50 values to used when >15 fields

```json
{
  "global_picklists": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit_due_to": [
          {
            "api_name": "type",
            "json_path": "$.global_picklists[0].pick_list_values[50].type"
          }
        ],
        "limit": 50
      },
      "message": "Moving more than 50 values to the used section in a single save is not allowed when they are associated with more than 15 fields.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AddMoreThan50Values

Adding >50 values when >15 fields

```json
{
  "global_picklists": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit_due_to": {
          "api_name": "type",
          "json_path": "$.global_picklists[0].pick_list_values[50]"
        },
        "limit": 50
      },
      "message": "Adding more than 50 values in a single save is not allowed when they are associated with more than 15 fields.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SystemDefinedUpdate

System defined global set update not allowed

```json
{
  "global_picklists": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.global_picklists[0].id",
        "id": "11111100000005593"
      },
      "message": "Updation of system defined global set is not allowed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — EmojiInDisplayLabel

Emoji in display_label

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "display_label",
        "json_path": "$.global_picklists[0].display_label"
      },
      "message": "INVALID_FIELD_LABEL",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UsedOptionsLimitExceeded

Used options limit exceeded (1000)

```json
{
  "global_picklists": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit_due_to": [
          {
            "api_name": "pick_list_values",
            "json_path": "$.global_picklists[0].pick_list_values"
          }
        ],
        "limit": 1000
      },
      "message": "Sorry, you have reached the limit of 1000 values added for this pick list field.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UnusedOptionsLimitExceeded

Unused options limit exceeded (500)

```json
{
  "global_picklists": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit_due_to": {
          "api_name": "pick_list_values",
          "json_path": "$.global_picklists[0].pick_list_values"
        },
        "limit": 500
      },
      "message": "Sorry, you have reached the limit of 500 unused values added for this pick list field.",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — ErrorExample

```json
{
  "code": "NO_PERMISSION",
  "message": "permission denied",
  "details": {
    "permissions": [
      "Crm_Implied_Customize_Zoho_CRM"
    ]
  },
  "status": "error"
}
```

### Status `500` — `application/json` — ErrorExample

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {},
  "status": "error"
}
```

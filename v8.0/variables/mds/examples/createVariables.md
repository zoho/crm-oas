# Examples: createVariables

**POST /settings/variables**

## Request examples

### `application/json` — SamplePostRequest

Sample request body

```json
{
  "variables": [
    {
      "name": "Variable33",
      "api_name": "Variable33",
      "variable_group": {
        "id": "400000000470050090988"
      },
      "type": "integer",
      "value": 33,
      "description": "This denotes variable 3 description"
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — Success201

Success response for status 201

```json
{
  "variables": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "40000000047009"
      },
      "message": "variable added",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — Success207

Success response for status 207

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "variables",
        "json_path": "$.variables[0].variables"
      },
      "message": "Mandatory field variables not found",
      "status": "error"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "1234567890123456"
      },
      "message": "Proper success message",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: body

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "jsonobject"
      },
      "message": "body",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Error response with code MANDATORY_NOT_FOUND: required field not found (Field: variables)

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "variables"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse1

Error response with code DUPLICATE_DATA: duplicate data (Field: api_name)

```json
{
  "variables": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.variables[0].api_name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Error response with code INVALID_DATA: invalid data (Field: variables)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 2,
    "api_name": "variables",
    "json_path": "$.variables"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: name)

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.variables[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error response with code INVALID_DATA: Invalid data type (Field: name)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.variables[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Error response with code INVALID_DATA: Invalid data (Field: name)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 50,
        "json_path": "$.variables[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse3

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: api_name)

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "api_name",
        "json_path": "$.variables[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.variables[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

Error response with code INVALID_DATA: Invalid data (Field: api_name)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "json_path": "$.variables[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse7

Error response with code INVALID_DATA: Invalid data (Field: api_name)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "regex": "^[a-zA-Z]+\\\\w*[a-zA-Z0-9]*$",
        "json_path": "$.variables[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse4

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: variable_group)

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "variable_group",
        "json_path": "$.variables[*].variable_group"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

Error response with code INVALID_DATA: Invalid data type (Field: variable_group)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "variable_group",
        "expected_data_type": "jsonobject",
        "json_path": "$.variables[*].variable_group"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse9

Error response with code INVALID_DATA: Invalid data (Field: variable_group)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "variable_group",
        "maximum_length": 2,
        "json_path": "$.variables[*].variable_group"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse5

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: id)

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.variables[*].variable_group.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse10

Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.variables[*].variable_group.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse11

Error response with code INVALID_DATA: Invalid data (Field: id)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 21,
        "json_path": "$.variables[*].variable_group.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse6

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: type)

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "type",
        "json_path": "$.variables[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse12

Error response with code INVALID_DATA: Invalid data type (Field: type)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.variables[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse13

Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 7,
        "json_path": "$.variables[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse14

Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "text",
          "integer",
          "boolean",
          "date",
          "float"
        ],
        "json_path": "$.variables[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse15

Error response with code INVALID_DATA: Invalid data type (Field: value)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "integer",
        "json_path": "$.variables[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse16

Error response with code INVALID_DATA: Invalid data type (Field: description)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "description",
        "expected_data_type": "text",
        "json_path": "$.variables[*].description"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse17

Error response with code INVALID_DATA: Invalid data (Field: description)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "description",
        "maximum_length": 250,
        "json_path": "$.variables[*].description"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse18

Error response with code INVALID_DATA: body

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "jsonobject"
      },
      "message": "body",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse7

Error response with code MANDATORY_NOT_FOUND: required field not found (Field: variables)

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "variables"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessingResponse1

Error response with code AMBIGUITY_DURING_PROCESSING: Ambiguity while processing the request

```json
{
  "variables": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.variables[0].variable_group.id"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessingResponse2

Error response with code AMBIGUITY_DURING_PROCESSING: Ambiguity while processing the request

```json
{
  "variables": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.variables[0].variable_group.id"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse8

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: name)

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.variables[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse21

Error response with code INVALID_DATA: Invalid data type (Field: name)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.variables[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse22

Error response with code INVALID_DATA: Invalid data (Field: name)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 50,
        "json_path": "$.variables[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse9

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: api_name)

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "api_name",
        "json_path": "$.variables[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse23

Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.variables[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse24

Error response with code INVALID_DATA: Invalid data (Field: api_name)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "json_path": "$.variables[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse25

Error response with code INVALID_DATA: Invalid data (Field: api_name)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "regex": "^[a-zA-Z]+\\\\w*[a-zA-Z0-9]*$",
        "json_path": "$.variables[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse10

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: variable_group)

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "variable_group",
        "json_path": "$.variables[*].variable_group"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse26

Error response with code INVALID_DATA: Invalid data type (Field: variable_group)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "variable_group",
        "expected_data_type": "jsonobject",
        "json_path": "$.variables[*].variable_group"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse27

Error response with code INVALID_DATA: Invalid data (Field: variable_group)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "variable_group",
        "maximum_length": 2,
        "json_path": "$.variables[*].variable_group"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse11

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: id)

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.variables[*].variable_group.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse28

Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.variables[*].variable_group.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse29

Error response with code INVALID_DATA: Invalid data (Field: id)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 21,
        "json_path": "$.variables[*].variable_group.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse12

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: type)

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "type",
        "json_path": "$.variables[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse32

Error response with code INVALID_DATA: Invalid data type (Field: type)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.variables[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse33

Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 7,
        "json_path": "$.variables[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse34

Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "text",
          "integer",
          "boolean",
          "date",
          "float"
        ],
        "json_path": "$.variables[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse35

Error response with code INVALID_DATA: Invalid data type (Field: value)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "integer",
        "json_path": "$.variables[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse36

Error response with code INVALID_DATA: Invalid data type (Field: description)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "description",
        "expected_data_type": "text",
        "json_path": "$.variables[*].description"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse37

Error response with code INVALID_DATA: Invalid data (Field: description)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "description",
        "maximum_length": 250,
        "json_path": "$.variables[*].description"
      },
      "status": "error"
    }
  ]
}
```

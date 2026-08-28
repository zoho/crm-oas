# Examples: createMapDependency

**POST /settings/layouts/{layoutId}/map_dependency**

## Request examples

### `application/json` — CreateDependency

Example of creating a field dependency.

```json
{
  "map_dependency": [
    {
      "parent": {
        "api_name": "Lead_Source",
        "id": "111111000000004107"
      },
      "pick_list_values": [
        {
          "display_value": "-None-",
          "maps": [
            {
              "display_value": "Contacted",
              "actual_value": "Contacted",
              "id": "111111000000016330"
            },
            {
              "display_value": "Contact in Future",
              "actual_value": "Contact in Future",
              "id": "111111000000016333"
            }
          ],
          "actual_value": "-None-",
          "id": "111111000000016273"
        },
        {
          "display_value": "Advertisement",
          "maps": [
            {
              "display_value": "Pre-Qualified",
              "actual_value": "Pre-Qualified",
              "id": "111111000000016327"
            },
            {
              "display_value": "Not Qualified",
              "actual_value": "Not Qualified",
              "id": "111111000000016351"
            }
          ],
          "actual_value": "Advertisement",
          "id": "111111000000016276"
        }
      ],
      "child": {
        "api_name": "Lead_Status",
        "id": "111111000000004109"
      }
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — SuccessResponse

Example of field dependency created successfully.

```json
{
  "map_dependency": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000064003"
      },
      "message": "map dependency created",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — RequiredParamMissing

Example of a required parameter missing.

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

### Status `400` — `application/json` — InvalidModule

Example of an invalid module name.

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "param_name": "module"
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidLayoutId

Example of an invalid layout ID.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "Invalid Layout Id",
  "status": "error"
}
```

### Status `400` — `application/json` — LayoutDeactivated

Example of deactivated layout.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "The given layout is deactivated",
  "status": "error"
}
```

### Status `400` — `application/json` — MaxLengthExceeded

Example of map_dependency array with exceeding length. 

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "map_dependency",
    "json_path": "$.map_dependency"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — MappingAlreadyExists

Example of already existing dependency mapping error. 

```json
{
  "map_dependency": [
    {
      "code": "MAPPING_ALREADY_EXISTS",
      "details": {
        "id": "1234687624378284",
        "dependency": [
          {
            "id": "123467634333580",
            "json_path": "$.map_dependency[0].parent.id"
          },
          {
            "id": "123467634333590",
            "json_path": "$.map_dependency[0].child.id"
          }
        ]
      },
      "message": "The given parent and child fields are already associated in another map dependency in this layout",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependencyLoop

Example error of dependency creating a loop.

```json
{
  "map_dependency": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.map_dependency[0].child.id"
      },
      "message": "The given child field when associated with this parent field will result in loop",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ParentChildSame

Example error for providing the same parent and child field.

```json
{
  "map_dependency": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.map_dependency[0].child.id"
      },
      "message": "The parent and child fieldid cannot be same",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFound

Example of required field not found.

```json
{
  "map_dependency": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.map_dependency[0].pick_list_values[0].maps[1].id"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidParentFieldId

Example of invalid parent field ID.

```json
{
  "map_dependency": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.map_dependency[0].parent.id"
      },
      "message": "invalid parent fieldid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidChildFieldId

Example of invalid child field ID.

```json
{
  "map_dependency": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.map_dependency[0].child.id"
      },
      "message": "invalid child fieldid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidChildOptionId

Example of invalid child picklist option ID.

```json
{
  "map_dependency": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.map_dependency[0].pick_list_values[0].maps[1].id"
      },
      "message": "Invalid child option id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidParentOptionId

Example of invalid parent picklist option ID.

```json
{
  "map_dependency": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.map_dependency[0].pick_list_values[0].id"
      },
      "message": "Invalid parent option id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — PickListValuesNotFound

Example of pick_list_values array missing.

```json
{
  "map_dependency": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "pick_list_values",
        "json_path": "$.map_dependency[0].pick_list_values"
      },
      "message": "required  field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MapsNotFound

Example of maps field missing.

```json
{
  "map_dependency": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "maps",
        "json_path": "$.map_dependency[0].pick_list_values[0].maps"
      },
      "message": "required  field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ChildFieldUnused

Example of child field in unused fields list.

```json
{
  "map_dependency": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.map_dependency[0].child.id"
      },
      "message": "Child fieldid is in unused fields list of the layout",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ParentFieldUnused

Example of parent field in unused fields list.

```json
{
  "map_dependency": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.map_dependency[0].parent.id"
      },
      "message": "Parent fieldid is in unused fields list of the layout",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AssociatedWithLayoutRule

Example of fields associated with a Layout Rule.

```json
{
  "map_dependency": [
    {
      "code": "NOT_ALLOWED",
      "details": {},
      "message": "The given parent and child field are Associated with Layout Rule",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidApiName

Example of invalid field API name.

```json
{
  "map_dependency": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.map_dependency[0].parent.api_name"
      },
      "message": "The given api name is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessing

Example of ambiguity in request field data.

```json
{
  "map_dependency": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.map_dependency[0].parent.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.map_dependency[0].parent.api_name"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

### Status `500` — `application/json` — ErrorExample

Example of an internal server error.

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {},
  "status": "error"
}
```

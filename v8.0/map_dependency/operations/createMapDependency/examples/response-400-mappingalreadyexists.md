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

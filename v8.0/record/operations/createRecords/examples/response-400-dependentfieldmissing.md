Required dependent field missing from the request

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Product_Category",
          "json_path": "$.data[0].Product_Category"
        },
        "api_name": "Product_Subcategory",
        "json_path": "$.data[0].Product_Subcategory"
      },
      "message": "The field 'Product_Subcategory' is required when 'Product_Category' is provided",
      "status": "error"
    }
  ]
}
```

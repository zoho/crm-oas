### `application/json` — BasicMerge

Example of a basic merge operation with field selection. 

```json
{
  "merge": [
    {
      "data": [
        {
          "_fields": [
            {
              "api_name": "Last_Name"
            }
          ],
          "id": "111111000000116110"
        }
      ],
      "master_record_fields": [
        {
          "api_name": "Company"
        }
      ]
    }
  ]
}
```

### `application/json` — FileUploadMerge

Example of a merge with file upload field configuration. 

```json
{
  "merge": [
    {
      "data": [
        {
          "_fields": [
            {
              "api_name": "Image_Upload_1",
              "_data": [
                {
                  "id": "5364788765222"
                }
              ]
            }
          ],
          "id": "111111000000116110"
        }
      ],
      "master_record_fields": [
        {
          "api_name": "Image_Upload_1",
          "_data": [
            {
              "id": "5364788765222"
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — FileDeleteMerge

Example of merge operation with file deletion. 

```json
{
  "merge": [
    {
      "data": [
        {
          "_fields": [
            {
              "api_name": "Company"
            }
          ],
          "id": "111111000000116110"
        }
      ],
      "master_record_fields": [
        {
          "api_name": "Image_Upload_1",
          "_data": null
        }
      ]
    }
  ]
}
```

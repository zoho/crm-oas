# GET /__features/user_licenses
**Operation:** `getUserLicenseFeatureDetails` — User Licenses Feature
> To get the user licenses feature details for the current edition

**Responses:**

- **200**: Response of user licenses feature details for the current edition [application/json]
    > User licenses feature details for the current edition
    - `__features` (array of object) [maxItems=1] **REQ** — User licenses feature details for the current edition
      - `api_name` (string) **REQ** [maxLen=255] — API name of the feature
      - `parent_feature` (object) **REQ** [nullable] — Parent feature details
      - `details` (object) **REQ** — This object will have limits and usage details
        - `available_count` (object) — Available count details for the feature
          - `total` (integer/int32) **REQ** — Total available count
        - `used_count` (object) — used count of the feature
          oneOf:
              - `total` (integer/int32) **REQ** — total count
              additionalProperties: any
              type: integer/int32 — used count of the feature
        - `limits` (object) **REQ** — Limit details for the feature
          - `total` (integer/int32) **REQ** — Total limit
      - `components` (null) **REQ** — Components of the feature
      - `module_supported` (boolean) **REQ** — Module wise feature supported or not
      - `feature_label` (string) **REQ** [maxLen=255] — Label of the feature
      additionalProperties: any
    additionalProperties: any

- **204**: User licenses feature not available for the current edition

- **400**: Invalid request error response [application/json]
    > Invalid request error response schema
    - `status` (string) **REQ** [enum=['error']] — Status of request
    - `code` (string) **REQ** [enum=['INVALID_MODULE', 'INVALID_DATA']] — Error code
    - `message` (string) **REQ** [maxLen=255] — Error message
    - `details` (object) **REQ** — Extra details
    additionalProperties: any

**Scopes:** ZohoCRM.features.READ

# Examples: updatePortal

**PUT /settings/portals/{portal}**

## Request examples

### `application/json` — Default

Sample portal update request

```json
{
  "portals": [
    {
      "name": "updateportal",
      "saml_configuration": {
        "login_url": "https://www.example.com",
        "logout_url": "https://www.example.com",
        "public_key": "-----BEGIN CERTIFICATE-----nMIICkTCCAXkCBgGFNDYS5DANBgkqhkiG9w0BAQsFADAMMQowCAYDVQQDEwFBMB4XDTIyMTIyMDEwMjM1N1oXDTI1MTIyMDEwMjM1N1owDDEKMAgGA1UEAxMBQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJ9JHZa/KoI1v4bl9HyDB2EB684y1P8hykirP0BoGpf2o4hj2ITjkhncbBJt9PFR8Cp8PmxL7UnGIZl/4g0VQMIxtq82UuvaC8uTZUQJeUDbrPEVMoN12YOF2sJ2AZ4gf3Pr6rf+kXYDp5T9gyFMFUzqNS/WL5xOpyzVJkROv69YbPkcLWms+orpcs+ADXXNfwhIfwF6ZLcNqgi1itX9T/vuvW5KEcU5QtOLLQdqNQ0Oi/0oiyIXhcsjGD1e+QSAtxdTpM44WkxOYW3TUj0+8EZOdU+Vj0lhgr61+bJHgnYiyA83LHqKcIKXEYVs70Lb3Ors4dU7XU6gBzxLnsf9nCECAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAUiTh+to8d/QKYh9yOLqE25PraBEVselNgNx8Dly//JXfXz42lzwG5WOY94bmUur2qYe8sVUqY07O/1XSW7QBrGMhGA9Hhvgz6zrRPzGPUVVQT3caTG/b+1pNLriga7OSam6rp1uL5emutkyyn6ZUZ7px4K1vGEx6/GBFsepGH5E2N0PRuekTp0eiV+5m+6z4VL7tVtYGQbWUfVgBqBUEhkdu450ry0jJT6SPs1W8TPBQEZQ/Pjis4MubIRKrUtkb+SkLDpBSWmXdoKlsIJt8VqhdqN04bmt91sB+XdgSC4X7ideK7WPcEj2DYna4v/YB13MitxQrKKU9uT/HNm1JHg==n-----END CERTIFICATE-----",
        "active": true
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Default

Successful portal update

```json
{
  "portals": [
    {
      "code": "SUCCESS",
      "message": "Portal updated successfully",
      "details": {
        "name": "examplePortal"
      },
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — Example1

INVALID_DATA - portal field validation error

```json
{
  "portals": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.portals[0].name",
        "minimum_length": 6
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example2

ALREADY_USED - portal name already in use

```json
{
  "portals": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "name"
      },
      "message": "The entered portal name is already in use",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example3

MANDATORY_NOT_FOUND - required field missing

```json
{
  "portals": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.portals[0].name"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example4

MANDATORY_NOT_FOUND - SAML login URL missing

```json
{
  "portals": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "login_url",
        "json_path": "$.portals[0].saml_configuration.login_url"
      },
      "message": "login url is mandatory to configure saml",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example5

MANDATORY_NOT_FOUND - SAML public key missing

```json
{
  "portals": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "public_key",
        "json_path": "$.portals[0].saml_configuration.public_key"
      },
      "message": "public key is mandatory to configure saml",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example6

NOT_ALLOWED - null value not permitted

```json
{
  "portals": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "login_url",
        "json_path": "$.portals[0].saml_configuration.login_url"
      },
      "message": "not allowed to set value as null",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ApiNotSupportedResponse1

API_NOT_SUPPORTED - sandbox environment

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "unsupported_environment": "sandbox"
  },
  "message": "api not supported in sandbox",
  "status": "error"
}
```

### Status `403` — `application/json` — Example1

NO_PERMISSION - required permission missing

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_ClientPortal"
    ]
  },
  "message": "Permission is invalid.",
  "status": "error"
}
```

### Status `403` — `application/json` — Example2

NO_PERMISSION - insufficient portal permission

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "Permission is invalid.",
  "status": "error"
}
```

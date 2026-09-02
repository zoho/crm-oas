### `application/json` — SingleLayoutMixedProfiles

Activate layout with profile additions and removals

```json
{
  "layouts": [
    {
      "id": "4831139000000673152",
      "profiles": [
        {
          "id": "4831139000000650385"
        },
        {
          "id": "4831139000000653716"
        },
        {
          "id": "4831139000000015972",
          "_delete": true
        }
      ]
    }
  ]
}
```

### `application/json` — SingleLayoutAddProfilesOnly

Activate layout with profile additions only

```json
{
  "layouts": [
    {
      "id": "4831139000000673152",
      "profiles": [
        {
          "id": "4831139000000650385"
        },
        {
          "id": "4831139000000653716"
        },
        {
          "id": "4831139000001234567"
        }
      ]
    }
  ]
}
```

### `application/json` — SingleLayoutRemoveProfilesOnly

Activate layout with profile removals only

```json
{
  "layouts": [
    {
      "id": "4831139000000673152",
      "profiles": [
        {
          "id": "4831139000000015972",
          "_delete": true
        },
        {
          "id": "4831139000000015973",
          "_delete": true
        }
      ]
    }
  ]
}
```

### `application/json` — SingleLayoutNoProfiles

Activate layout without profile modifications

```json
{
  "layouts": [
    {
      "id": "4831139000000673152",
      "profiles": []
    }
  ]
}
```

### `application/json` — SingleLayoutWithoutProfilesKey

Activate layout omitting the profiles key

```json
{
  "layouts": [
    {
      "id": "4831139000000673152"
    }
  ]
}
```

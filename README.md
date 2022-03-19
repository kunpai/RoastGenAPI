# Roast Generator
## Usage

All responses will have the form

```json
{
    "roast": "Roast"
}
```

### List all roasts

**Definition**

`GET /roast`

**Roast**

- `200 OK`

```json
[
    {
        "identifier": "1",
        "roast": "Mirrors can't talk, and lucky for you they can't laugh either"
    },
    {
        "identifier": "2",
        "roast": "I was hoping for a battle of wits but you appear to be unarmed."
    }
]
```

## Lookup roasts

`GET /roast/<identifier>`

**Response**

- `404: Not Found` if roast does not exist
- `200 OK` on success

```json
{
    "identifier": "1",
    "roast": "Mirrors can't talk, and lucky for you they can't laugh either"
}
```


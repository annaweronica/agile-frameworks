# DATABASE SCHEMA 

## Packages

#### Package

```
'name': '...',
'description': '...',
'price': '...',
'rating': '...',
'image': '...',
```

## Profiles

#### User profile

```
'user': '...',
'default_town_or_city': '..',
'default_street_address1': '...',
'default_street_address2': '...',
'default_country': '...',
```
## Checkout App models

#### Order

```
'order_number': '...',
'user_profile': '...',
'name': '...',
'group_size': '...',
'full_name': '...',
'email': '...',
'town_or_city': '...',
'street_address1': '...,
'street_address2': '...',
'date': '...',
'total': '...',
```

#### Order Line item

```
'order': '...',
'package': '...',
'lineitem_total': '...',
```
# DATABASE SCHEMA 

## Packages App Model

#### Package

```
'name': '...',
'description': '...',
'price': '...',
'rating': '...',
'image': '...',
```

## Profiles App Model

#### UserProfile

```
'user': '...',
'default_town_or_city': '..',
'default_street_address1': '...',
'default_street_address2': '...',
'default_country': '...',
```
## Checkout App Models

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

#### OrderLineItem

```
'order': '...',
'package': '...',
'lineitem_total': '...',
```

# Permissions & Postgresql

## Features - Django REST Framework

Make your site a DRF powered API as you did in previous lab.
Adjust project’s permissions so that only authenticated user’s have access to API.
Add a custom permission so that only author of blog post can update or delete it.
Add ability to switch user’s directly from browsable API.

## Permissions in drf

In DRF, permissions, along with authentication and throttling, are used to grant or deny access for different classes of users to different parts of an API.

Authentication and authorization work hand in hand. Authentication is always executed before authorization.


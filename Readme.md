<!--
 * @Description: Project Description
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-02-04 09:35:52
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-02-07 14:10:53
-->

# Reasonable Productivity

This is a `Django` backend and `Vue` frontend test project.

It's a task management system.

## Quick Start

### Start Backend Application

You should install `Django`, `Django REST Framwork`, `drf-nested-routers` and `django-cors-headers` yourself.

```
$ cd backend
$ manage.py migrate
$ manage.py runserver
```

Go to `127.0.0.1:8000` to check.

### Start Frontend Application

```
$ cd frontend
$ yarn install
$ yarn dev
```

Go to `127.0.0.1:3000` to check.

## Backend

- Django
- Django REST Framework

### Database Schema

**Task**

- title
- description
- created_at
- updated_at

**User**

- email
- password

**UserProfile**

- user (Primary Key)
- first_name
- last_name
- image
- fb_profile
- twitter_profile
- linkedin_profile
- website

**List**

- user (Foreign Key to User)
- name
- description
- created_at
- updated_at

**ListItem**

- list
- text
- created_at
- updated_at

## Frontend

### Technologies

- Vue.js
- Nuxt.js
- Vuex
- Vue Router
- Vuetify
- Axios

### Routers

**Tasks**

- `tasks`
- `tasks/:id`

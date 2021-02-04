<!--
 * @Description: Project Description
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-02-04 09:35:52
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-02-04 20:32:51
-->

# Reasonable Productivity

This is a `Django` backend and `Vue` frontend test project.

It's a task management system.

## Quick Start

You should install `Django` and `Django REST Framwork` yourself.

```
$ cd backend
$ manage.py migrate
$ manage.py runserver
```

Go to `127.0.0.1:8000` to check.

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

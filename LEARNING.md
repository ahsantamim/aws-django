# Learning Progress

**Topic:** Django → Django REST Framework (Product CRUD API)
**Goal:** Understand Django's mechanics by building CRUD by hand first, then learn each abstraction and what it replaces, ending with a production-style API.
**Comparison stack:** Express.js

## Current step

**Track: Class-Based Views with a new `orders` feature** (Product FBVs stay as the hand-built reference).
Step 4: how `as_view()` + `dispatch()` route `request.method` to `get/post/...`.

### Orders CBV track

- [x] 1. Create `orders` app + register in `INSTALLED_APPS`
- [x] 2. `Order` model with a `ForeignKey` to `Products` (+ quantity, status) and migrate
- [x] 3. First CBV: `View` subclass with `get()` (list orders) + `.as_view()` in URLs
- [ ] 4. How `dispatch()` routes `request.method` to `get/post/...` (compare with `products_api`)
- [ ] 5. `post()` — create an order (validate product exists, quantity > 0)
- [ ] 6. Detail view: `get()` single order with `pk` URL kwarg
- [ ] 7. `put()` (full replace) vs `patch()` (partial) on the detail view
- [ ] 8. `delete()`
- [ ] 9. Automatic 405 via `http_method_names`; CSRF with `method_decorator`
- [ ] 10. Refactor shared code (serialize helper / mixin) — the idea DRF generalizes

## Syllabus

- [x] Virtual environment, install Django, create project + `products` app
- [x] Configure the app, `Products` model, migrations, SQLite
- [x] Register model in Django Admin (Model → Database flow)
- [x] GET all products (`views.py`, `urls.py`, ORM, `JsonResponse`)
- [x] POST / create a product (`request.body`, JSON parsing, CSRF)
- [x] GET single product by ID (dynamic URL params, `get_object_or_404`)
- [x] DELETE a product
- [x] Group operations per resource endpoint (`/api/products/`, `/api/products/<id>/`)
- [ ] Finish PUT and PATCH (correct semantics)
- [ ] Complete and test full CRUD
- [ ] Refactor function-based CRUD into Class-Based Views
- [ ] Understand CBV `get()`, `post()`, `put()`, `patch()`, `delete()`
- [ ] How Django CBVs dispatch to HTTP methods
- [ ] Introduce Django REST Framework
- [ ] Serializers
- [ ] APIView
- [ ] Generic Views
- [ ] ViewSets
- [ ] Routers
- [ ] Automatic CRUD
- [ ] Validation and error handling
- [ ] Authentication and permissions
- [ ] Pagination and filtering
- [ ] OpenAPI / Swagger documentation
- [ ] Build a production-style CRUD API

## Concepts learned

URL routing, dynamic URL parameters, `request.body`, JSON parsing, CSRF (`@csrf_exempt`), `get_object_or_404()`, HTTP status codes, REST-style resource endpoints, method dispatch by `request.method`, Django apps + `INSTALLED_APPS`, adjacent string literal concatenation, `ForeignKey` (many-to-one), `on_delete` (`PROTECT` vs `CASCADE`), `choices`, `related_name`, `makemigrations` vs `migrate`, `View` subclass + `get()`, `.as_view()`, `select_related` / N+1, multiple `include()` under one prefix, `ModelAdmin` (`list_display`, `list_filter`, `search_fields` with `__` lookups).

## Notable errors hit

_(add as they come up)_

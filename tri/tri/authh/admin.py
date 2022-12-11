from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model


UserModel = get_user_model()
@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    list_filter = ["is_staff", "is_superuser", "is_active", "groups", "first_name", "last_name", "gender", "age"]
    list_display = ["username", "email", "first_name", "last_name", "age", "gender", "is_staff"]
    search_fields = ["username", "first_name", "last_name", "email", "age", "gender"]
    ordering = ["first_name"]
#     form = UserEditForm
#     add_form = UserCreateForm
#
#     fieldsets = (
#         (
#             None,
#             {
#                 'fields': (
#                     'username',
#                     'password',
#                 ),
#             }),
#         (
#             'Personal info',
#             {
#                 'fields': (
#                     'first_name',
#                     'last_name',
#                     'email',
#                     'gender',
#                     'age',
#                 ),
#             },
#         ),
#         )
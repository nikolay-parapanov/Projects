from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model


UserModel = get_user_model()
@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    pass
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
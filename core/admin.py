from django.contrib import admin

from .models import Position, Employee, Service


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'modifiedOn')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'active', 'modifiedOn')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'active', 'modifiedOn')

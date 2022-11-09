from django.contrib import admin

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Relationship

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') == True:
                count += 1
        if count == 0:
            raise ValidationError('Выберите основной раздел')
        elif count == 1:
            pass
        else:
            raise ValidationError('Основной раздел должен быть один')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset

class ScopeInline(admin.TabularInline):
    model = Scope

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
    #inlines = [RelationshipInline]






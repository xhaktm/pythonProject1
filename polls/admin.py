from django.contrib import admin

# Register your models here.
from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuesionAdmin(admin.ModelAdmin):
    fieldsets = [('Question Statement', {'fields' : ['question_text']}),
                 ('Date Information', {'fields' : ['pub_date'], 'classes':['collapse']})]

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuesionAdmin)
admin.site.register(Choice)


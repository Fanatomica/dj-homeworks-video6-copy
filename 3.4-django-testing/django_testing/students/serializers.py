from rest_framework import serializers

from students.models import Course

from django_testing.settings import MAX_STUDENTS_PER_COURSE


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate_students(self, attr):
        if students.count() <= settings.MAX_STUDENTS_PER_COURSE:
            return attr
        else:
            raise serializers.ValidationError(f'Количество студентов на курсе больше {settings.MAX_STUDENTS_PER_COURSE}')


    # def validate(self, data):
    #     print(settings.MAX_STUDENTS_PER_COURSE)
    #     if Course.objects.filter(id=self.contex["request"].id).students.count() <= settings.MAX_STUDENTS_PER_COURSE:
    #         return data
    #     else:
    #         raise serializers.ValidationError(f'Количество студентов на курсе больше {settings.MAX_STUDENTS_PER_COURSE}')



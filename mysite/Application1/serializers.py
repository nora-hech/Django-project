from rest_framework import serializers
from Application1.models import Schools
from Application1.models import Students


class SchoolsSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True)

    class Meta:
        model = Schools
        fields = ('name', 'maxstudents', 'students')

    def create(self, validated_data):
        """
        Create and return a new `Schools` instance, given the validated data.
        """
        return Schools.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Schools` instance,
        given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.maxstudents = validated_data.get(
            'maxstudents', instance.maxstudents)
        instance.students = validated_data.get('students', instance.students)
        instance.save()
        return instance


class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ('firstname', 'lastname', 'school', 'identification')

    def create(self, validated_data):
        """
        Create and return a new `Students` instance, given the validated data.
        """
        return Students.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Students` instance,
        given the validated data.
        """
        instance.firstname = validated_data.get(
            'firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.school = validated_data.get('school', instance.school)
        instance.save()
        return instance

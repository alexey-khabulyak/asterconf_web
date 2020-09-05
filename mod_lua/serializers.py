from rest_framework import serializers
from .models import Call


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ('uuid', 'src', 'dst', 'direction', 'time', 'status', 'duration')

    def update(self, instance, validated_data):
        print(instance)
        print(validated_data)
        instance.duration = validated_data.get('duration')
        instance.status = validated_data.get('status')
        instance.save()
        return instance
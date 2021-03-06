from rest_framework import serializers

from columns.models import Column


class ColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Column
        fields = "__all__"
from django.shortcuts import render
from rest_framework import generics

from columns.api.serializers import ColumnSerializer


class CreateKanban(generics.CreateAPIView):
    serializer_class = ColumnSerializer

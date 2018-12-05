from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework import serializers
from collector.models import ServerInfo


class ShowInfoMixin(object):
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class InfoViewSet(ShowInfoMixin, CreateModelMixin, GenericViewSet):

    # def perform_create(self, serializer):
    #     pk = self.kwargs['performance_pk']
    #     server = ServerInfo.objects.get(pk=pk)
    #     serializer.save(server=server)

    pass

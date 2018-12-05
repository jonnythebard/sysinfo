from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import get_object_or_404
from rest_framework import serializers
from rest_framework import status
from collector.models import ServerInfo


class InfoViewSet(GenericViewSet):

    @property
    def server_id(self):
        return self.kwargs['performance_pk']

    def get_queryset(self):
        queryset = self.queryset.filter(server_id=self.server_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # TODO
        # 평균사용정보
        # 최대사용시간

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        server_id = self.kwargs['performance_pk']

        try:
            server = ServerInfo.objects.get(pk=self.server_id)
        except ServerInfo.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.save(server=server)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

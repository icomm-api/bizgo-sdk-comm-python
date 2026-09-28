"""Image uploads: ``POST /api/comm/v1/file/*``."""

from __future__ import annotations

from typing import Any, Literal

from .._transport import Retry, validate
from ..models._generated_response import (
    BrandMessageFileUploadResponse,
    BrandMessageFileUploadResult,
    FileUploadResponse,
    FileUploadResult,
    RcsFileUploadResponse,
    RcsFileUploadResult,
)
from ._common import FileInput, compact, read_file
from ._generated import AsyncFilesBase, FilesBase

MMS_MAX_BYTES = 300 * 1024

BrandImageKind = Literal["default", "wide", "wideItemList", "wideItemList/first", "carouselFeed", "carouselCommerce"]
"""Brand message image type. Each has its own size/ratio rules (see the API reference)."""


def _form(file: FileInput, filename: str | None, file_key: str | None, image_name: str | None) -> dict[str, Any]:
    name, content, content_type = read_file(file, filename)
    return {
        "files": {"file": (name, content, content_type)},
        "data": compact({"fileKey": file_key, "imageName": image_name}) or None,
        "size": len(content),
    }


def _mms_form(file: FileInput, filename: str | None, file_key: str | None, image_name: str | None) -> dict[str, Any]:
    form = _form(file, filename, file_key, image_name)
    if form.pop("size") > MMS_MAX_BYTES:
        raise ValueError("MMS 이미지는 최대 300KB입니다(jpg, 권장 1,500×1,440px 이하).")
    return form


def _other_form(file: FileInput, filename: str | None, file_key: str | None, image_name: str | None) -> dict[str, Any]:
    form = _form(file, filename, file_key, image_name)
    form.pop("size")
    return form


def _brand_path(kind: BrandImageKind) -> str:
    if kind not in ("default", "wide", "wideItemList", "wideItemList/first", "carouselFeed", "carouselCommerce"):
        raise ValueError(f"지원하지 않는 브랜드메시지 이미지 종류입니다: {kind!r}")
    return f"/api/comm/v1/file/brandmessage/{kind}"


_BRAND_OPERATIONS = {
    "default": "uploadBrandMessageDefaultImage",
    "wide": "uploadBrandMessageWideImage",
    "wideItemList": "uploadBrandMessageWideItemListImage",
    "wideItemList/first": "uploadBrandMessageWideItemListFirstImage",
    "carouselFeed": "uploadBrandMessageCarouselFeedImage",
    "carouselCommerce": "uploadBrandMessageCarouselCommerceImage",
}


def _mms(body: dict[str, Any]) -> FileUploadResult:
    data = validate(FileUploadResponse, body, "uploadMmsFile").data
    return data.data if data and data.data else FileUploadResult()


def _rcs(body: dict[str, Any]) -> RcsFileUploadResult:
    data = validate(RcsFileUploadResponse, body, "uploadRcsFile").data
    return data.data if data and data.data else RcsFileUploadResult()


def _brand(body: dict[str, Any]) -> BrandMessageFileUploadResult:
    data = validate(BrandMessageFileUploadResponse, body, "uploadBrandMessageDefaultImage").data
    return data.data if data and data.data else BrandMessageFileUploadResult()


class Files(FilesBase):
    """Upload images. Access as ``client.files``. Uploads are retried only on HTTP 429."""

    def upload_mms(
        self,
        file: FileInput,
        *,
        filename: str | None = None,
        file_key: str | None = None,
        image_name: str | None = None,
    ) -> FileUploadResult:
        """Upload an MMS image (jpg, max 300KB). Use ``result.file_key`` in ``MmsMessage.file_key``."""
        form = _mms_form(file, filename, file_key, image_name)
        return _mms(
            self._transport.request(
                "POST", "/api/comm/v1/file/mms", retry=Retry.RATE_LIMIT_ONLY, operation="uploadMmsFile", **form
            )
        )

    def upload_rcs(
        self,
        file: FileInput,
        *,
        filename: str | None = None,
        file_key: str | None = None,
        image_name: str | None = None,
    ) -> RcsFileUploadResult:
        """Upload an RCS image. Use ``result.media`` in the RCS message body."""
        form = _other_form(file, filename, file_key, image_name)
        return _rcs(
            self._transport.request(
                "POST", "/api/comm/v1/file/rcs", retry=Retry.RATE_LIMIT_ONLY, operation="uploadRcsFile", **form
            )
        )

    def upload_brand_message(
        self,
        file: FileInput,
        *,
        kind: BrandImageKind = "default",
        filename: str | None = None,
        file_key: str | None = None,
        image_name: str | None = None,
    ) -> BrandMessageFileUploadResult:
        """Upload a Kakao brand message image. Use ``result.img_url`` in the message."""
        form = _other_form(file, filename, file_key, image_name)
        return _brand(
            self._transport.request(
                "POST", _brand_path(kind), retry=Retry.RATE_LIMIT_ONLY, operation=_BRAND_OPERATIONS[kind], **form
            )
        )


class AsyncFiles(AsyncFilesBase):
    """Async version of :class:`Files`."""

    async def upload_mms(
        self,
        file: FileInput,
        *,
        filename: str | None = None,
        file_key: str | None = None,
        image_name: str | None = None,
    ) -> FileUploadResult:
        """See :meth:`Files.upload_mms`. Reading a file path is blocking; pass bytes in async code if that matters."""
        form = _mms_form(file, filename, file_key, image_name)
        return _mms(
            await self._transport.request(
                "POST", "/api/comm/v1/file/mms", retry=Retry.RATE_LIMIT_ONLY, operation="uploadMmsFile", **form
            )
        )

    async def upload_rcs(
        self,
        file: FileInput,
        *,
        filename: str | None = None,
        file_key: str | None = None,
        image_name: str | None = None,
    ) -> RcsFileUploadResult:
        """See :meth:`Files.upload_rcs`."""
        form = _other_form(file, filename, file_key, image_name)
        return _rcs(
            await self._transport.request(
                "POST", "/api/comm/v1/file/rcs", retry=Retry.RATE_LIMIT_ONLY, operation="uploadRcsFile", **form
            )
        )

    async def upload_brand_message(
        self,
        file: FileInput,
        *,
        kind: BrandImageKind = "default",
        filename: str | None = None,
        file_key: str | None = None,
        image_name: str | None = None,
    ) -> BrandMessageFileUploadResult:
        """See :meth:`Files.upload_brand_message`."""
        form = _other_form(file, filename, file_key, image_name)
        return _brand(
            await self._transport.request(
                "POST", _brand_path(kind), retry=Retry.RATE_LIMIT_ONLY, operation=_BRAND_OPERATIONS[kind], **form
            )
        )

"""Generated from spec/openapi.yaml by scripts/generate_models.py. Do not edit.

Resource classes for every operation in the spec (``client.<resource>.<method>``). Hand-written
convenience methods in send/files/reports/messages take precedence (those classes subclass the
``<Name>Base`` classes below).
"""

from __future__ import annotations

import builtins
import datetime as dt
from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from typing import Any, Literal

from .._operation import Pagination
from .._transport import AsyncTransport, Call, Retry, SyncTransport, validate
from ..models import _generated_request as _q
from ..models import _generated_response as _r
from ._common import FileInput
from ._runtime import (
    Form,
    aiterate,
    array,
    check_int,
    check_str,
    date_param,
    datetime_param,
    header,
    iterate,
    json_body,
    need,
    pick,
    pick_list,
    query,
    segment,
)

__all__ = [
    "Alimtalk",
    "AlimtalkPublicTemplates",
    "AlimtalkTemplateCategories",
    "AlimtalkTemplates",
    "AsyncAlimtalk",
    "AsyncAlimtalkPublicTemplates",
    "AsyncAlimtalkTemplateCategories",
    "AsyncAlimtalkTemplates",
    "AsyncBrandMessage",
    "AsyncBrandMessageAudience",
    "AsyncBrandMessageFriendGroups",
    "AsyncBrandMessageGroupSends",
    "AsyncBrandMessageGroupTags",
    "AsyncBrandMessageMarketingAgreements",
    "AsyncBrandMessagePermissions",
    "AsyncBrandMessageTemplates",
    "AsyncBrandMessageUnsubscribeContents",
    "AsyncBrandMessageVideos",
    "AsyncCounsel",
    "AsyncCounselCerts",
    "AsyncCounselChannels",
    "AsyncCounselConsultTime",
    "AsyncCounselFiles",
    "AsyncCounselMessages",
    "AsyncCounselSessions",
    "AsyncCounselSystemMessages",
    "AsyncCounselUsers",
    "AsyncFilesBase",
    "AsyncInsights",
    "AsyncInsightsAlimtalk",
    "AsyncInsightsBrandMessage",
    "AsyncInsightsRcs",
    "AsyncKakao",
    "AsyncKakaoCategories",
    "AsyncKakaoGroups",
    "AsyncKakaoSanctions",
    "AsyncKakaoSenders",
    "AsyncMessagesBase",
    "AsyncRcs",
    "AsyncRcsBrands",
    "AsyncRcsChatbots",
    "AsyncRcsCommonFormats",
    "AsyncRcsTemplateForms",
    "AsyncRcsTemplateImages",
    "AsyncRcsTemplates",
    "AsyncReportsBase",
    "AsyncReservations",
    "AsyncReservationsRecipients",
    "AsyncSendBase",
    "BrandMessage",
    "BrandMessageAudience",
    "BrandMessageFriendGroups",
    "BrandMessageGroupSends",
    "BrandMessageGroupTags",
    "BrandMessageMarketingAgreements",
    "BrandMessagePermissions",
    "BrandMessageTemplates",
    "BrandMessageUnsubscribeContents",
    "BrandMessageVideos",
    "Counsel",
    "CounselCerts",
    "CounselChannels",
    "CounselConsultTime",
    "CounselFiles",
    "CounselMessages",
    "CounselSessions",
    "CounselSystemMessages",
    "CounselUsers",
    "FilesBase",
    "Insights",
    "InsightsAlimtalk",
    "InsightsBrandMessage",
    "InsightsRcs",
    "Kakao",
    "KakaoCategories",
    "KakaoGroups",
    "KakaoSanctions",
    "KakaoSenders",
    "MessagesBase",
    "Rcs",
    "RcsBrands",
    "RcsChatbots",
    "RcsCommonFormats",
    "RcsTemplateForms",
    "RcsTemplateImages",
    "RcsTemplates",
    "ReportsBase",
    "Reservations",
    "ReservationsRecipients",
    "SendBase",
]


def _call_upload_brand_message_default_image(
    *, file: FileInput, filename: str | None, file_key: str | None, image_name: str | None
) -> Call:
    form = Form()
    need("file", file)
    form.file("file", file, filename, "image.jpg", max_bytes=None)
    form.text("fileKey", check_str("fileKey", file_key, max_length=None, enum=()))
    form.text("imageName", check_str("imageName", image_name, max_length=None, enum=()))
    return Call(
        operation="uploadBrandMessageDefaultImage",
        method="POST",
        path="/api/comm/v1/file/brandmessage/default",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_brand_message_default_image(body: dict[str, Any]) -> _r.BrandMessageFileUploadResult:
    found = pick(validate(_r.BrandMessageFileUploadResponse, body, "uploadBrandMessageDefaultImage"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageFileUploadResult) else _r.BrandMessageFileUploadResult()


def _call_upload_brand_message_wide_image(
    *, file: FileInput, filename: str | None, file_key: str | None, image_name: str | None
) -> Call:
    form = Form()
    need("file", file)
    form.file("file", file, filename, "image.jpg", max_bytes=None)
    form.text("fileKey", check_str("fileKey", file_key, max_length=None, enum=()))
    form.text("imageName", check_str("imageName", image_name, max_length=None, enum=()))
    return Call(
        operation="uploadBrandMessageWideImage",
        method="POST",
        path="/api/comm/v1/file/brandmessage/wide",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_brand_message_wide_image(body: dict[str, Any]) -> _r.BrandMessageFileUploadResult:
    found = pick(validate(_r.BrandMessageFileUploadResponse, body, "uploadBrandMessageWideImage"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageFileUploadResult) else _r.BrandMessageFileUploadResult()


def _call_upload_brand_message_wide_item_list_first_image(
    *, file: FileInput, filename: str | None, file_key: str | None, image_name: str | None
) -> Call:
    form = Form()
    need("file", file)
    form.file("file", file, filename, "image.jpg", max_bytes=None)
    form.text("fileKey", check_str("fileKey", file_key, max_length=None, enum=()))
    form.text("imageName", check_str("imageName", image_name, max_length=None, enum=()))
    return Call(
        operation="uploadBrandMessageWideItemListFirstImage",
        method="POST",
        path="/api/comm/v1/file/brandmessage/wideItemList/first",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_brand_message_wide_item_list_first_image(body: dict[str, Any]) -> _r.BrandMessageFileUploadResult:
    found = pick(
        validate(_r.BrandMessageFileUploadResponse, body, "uploadBrandMessageWideItemListFirstImage"), ("data", "data")
    )
    return found if isinstance(found, _r.BrandMessageFileUploadResult) else _r.BrandMessageFileUploadResult()


def _call_upload_brand_message_wide_item_list_image(
    *, file: FileInput, filename: str | None, file_key: str | None, image_name: str | None
) -> Call:
    form = Form()
    need("file", file)
    form.file("file", file, filename, "image.jpg", max_bytes=None)
    form.text("fileKey", check_str("fileKey", file_key, max_length=None, enum=()))
    form.text("imageName", check_str("imageName", image_name, max_length=None, enum=()))
    return Call(
        operation="uploadBrandMessageWideItemListImage",
        method="POST",
        path="/api/comm/v1/file/brandmessage/wideItemList",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_brand_message_wide_item_list_image(body: dict[str, Any]) -> _r.BrandMessageFileUploadResult:
    found = pick(
        validate(_r.BrandMessageFileUploadResponse, body, "uploadBrandMessageWideItemListImage"), ("data", "data")
    )
    return found if isinstance(found, _r.BrandMessageFileUploadResult) else _r.BrandMessageFileUploadResult()


def _call_upload_brand_message_carousel_feed_image(
    *, file: FileInput, filename: str | None, file_key: str | None, image_name: str | None
) -> Call:
    form = Form()
    need("file", file)
    form.file("file", file, filename, "image.jpg", max_bytes=None)
    form.text("fileKey", check_str("fileKey", file_key, max_length=None, enum=()))
    form.text("imageName", check_str("imageName", image_name, max_length=None, enum=()))
    return Call(
        operation="uploadBrandMessageCarouselFeedImage",
        method="POST",
        path="/api/comm/v1/file/brandmessage/carouselFeed",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_brand_message_carousel_feed_image(body: dict[str, Any]) -> _r.BrandMessageFileUploadResult:
    found = pick(
        validate(_r.BrandMessageFileUploadResponse, body, "uploadBrandMessageCarouselFeedImage"), ("data", "data")
    )
    return found if isinstance(found, _r.BrandMessageFileUploadResult) else _r.BrandMessageFileUploadResult()


def _call_upload_brand_message_carousel_commerce_image(
    *, file: FileInput, filename: str | None, file_key: str | None, image_name: str | None
) -> Call:
    form = Form()
    need("file", file)
    form.file("file", file, filename, "image.jpg", max_bytes=None)
    form.text("fileKey", check_str("fileKey", file_key, max_length=None, enum=()))
    form.text("imageName", check_str("imageName", image_name, max_length=None, enum=()))
    return Call(
        operation="uploadBrandMessageCarouselCommerceImage",
        method="POST",
        path="/api/comm/v1/file/brandmessage/carouselCommerce",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_brand_message_carousel_commerce_image(body: dict[str, Any]) -> _r.BrandMessageFileUploadResult:
    found = pick(
        validate(_r.BrandMessageFileUploadResponse, body, "uploadBrandMessageCarouselCommerceImage"), ("data", "data")
    )
    return found if isinstance(found, _r.BrandMessageFileUploadResult) else _r.BrandMessageFileUploadResult()


def _call_create_reservation(*, body: _q.ReservationCreateRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="createReservation",
        method="POST",
        path="/api/comm/v1/reservation",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.ReservationCreateRequest, body),
    )


def _parse_create_reservation(body: dict[str, Any]) -> _r.ReservationCreateServiceResult:
    found = pick(validate(_r.ReservationCreateResponse, body, "createReservation"), ("data",))
    return found if isinstance(found, _r.ReservationCreateServiceResult) else _r.ReservationCreateServiceResult()


def _call_list_reservations(
    *, resv_send_time: dt.datetime | str, payment_code: str | None, last_seq: int | None, limit: int | None
) -> Call:
    return Call(
        operation="listReservations",
        method="GET",
        path="/api/comm/v1/reservation/list",
        retry=Retry.SAFE,
        params=query(
            {
                "resvSendTime": need(
                    "resvSendTime", datetime_param("resvSendTime", resv_send_time, "yyyy-MM-dd HH:mm:ss")
                ),
                "paymentCode": check_str("paymentCode", payment_code, max_length=None, enum=()),
                "lastSeq": check_int("lastSeq", last_seq, None, None),
                "limit": check_int("limit", limit, 1, None),
            }
        ),
    )


def _parse_list_reservations(body: dict[str, Any]) -> _r.ReservationListResult:
    found = pick(validate(_r.ReservationListResponse, body, "listReservations"), ("data", "data"))
    return found if isinstance(found, _r.ReservationListResult) else _r.ReservationListResult()


_PAGE_LIST_RESERVATIONS = Pagination(
    style="cursor",
    request="lastSeq",
    items=("data", "data", "reservations"),
    cursor=("data", "data", "lastSeq"),
    has_next=("data", "data", "hasNext"),
)


def _call_get_reservation(*, resv_key: str) -> Call:
    return Call(
        operation="getReservation",
        method="GET",
        path=f"/api/comm/v1/reservation/resvKey/{segment(resv_key, 'resvKey')}",
        retry=Retry.SAFE,
    )


def _parse_get_reservation(body: dict[str, Any]) -> _r.Reservation:
    found = pick(validate(_r.ReservationResponse, body, "getReservation"), ("data", "data"))
    return found if isinstance(found, _r.Reservation) else _r.Reservation()


def _call_update_reservation(*, resv_key: str, body: _q.ReservationUpdateRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="updateReservation",
        method="PUT",
        path=f"/api/comm/v1/reservation/resvKey/{segment(resv_key, 'resvKey')}",
        retry=Retry.SAFE,
        json=json_body(_q.ReservationUpdateRequest, body),
    )


def _parse_update_reservation(body: dict[str, Any]) -> _r.Reservation:
    found = pick(validate(_r.ReservationResponse, body, "updateReservation"), ("data", "data"))
    return found if isinstance(found, _r.Reservation) else _r.Reservation()


def _call_cancel_reservation(*, resv_key: str) -> Call:
    return Call(
        operation="cancelReservation",
        method="POST",
        path=f"/api/comm/v1/reservation/resvKey/{segment(resv_key, 'resvKey')}/cancel",
        retry=Retry.RATE_LIMIT_ONLY,
    )


def _parse_cancel_reservation(body: dict[str, Any]) -> _r.Reservation:
    found = pick(validate(_r.ReservationResponse, body, "cancelReservation"), ("data", "data"))
    return found if isinstance(found, _r.Reservation) else _r.Reservation()


def _call_stop_reservation(*, resv_key: str) -> Call:
    return Call(
        operation="stopReservation",
        method="POST",
        path=f"/api/comm/v1/reservation/resvKey/{segment(resv_key, 'resvKey')}/stop",
        retry=Retry.RATE_LIMIT_ONLY,
    )


def _parse_stop_reservation(body: dict[str, Any]) -> _r.Reservation:
    found = pick(validate(_r.ReservationResponse, body, "stopReservation"), ("data", "data"))
    return found if isinstance(found, _r.Reservation) else _r.Reservation()


def _call_resume_reservation(*, resv_key: str) -> Call:
    return Call(
        operation="resumeReservation",
        method="POST",
        path=f"/api/comm/v1/reservation/resvKey/{segment(resv_key, 'resvKey')}/resume",
        retry=Retry.RATE_LIMIT_ONLY,
    )


def _parse_resume_reservation(body: dict[str, Any]) -> _r.Reservation:
    found = pick(validate(_r.ReservationResponse, body, "resumeReservation"), ("data", "data"))
    return found if isinstance(found, _r.Reservation) else _r.Reservation()


def _call_add_reservation_recipients(
    *, resv_key: str, body: _q.ReservationRecipientCreateRequest | Mapping[str, Any]
) -> Call:
    return Call(
        operation="addReservationRecipients",
        method="POST",
        path=f"/api/comm/v1/reservation/resvKey/{segment(resv_key, 'resvKey')}/destinations",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.ReservationRecipientCreateRequest, body),
    )


def _parse_add_reservation_recipients(body: dict[str, Any]) -> _r.SendOmniResult:
    found = pick(validate(_r.ReservationRecipientCreateResponse, body, "addReservationRecipients"), ("data", "data"))
    return found if isinstance(found, _r.SendOmniResult) else _r.SendOmniResult()


def _call_list_reservation_recipients(*, resv_key: str, last_seq: int | None, limit: int | None) -> Call:
    return Call(
        operation="listReservationRecipients",
        method="GET",
        path=f"/api/comm/v1/reservation/resvKey/{segment(resv_key, 'resvKey')}/destinations",
        retry=Retry.SAFE,
        params=query(
            {"lastSeq": check_int("lastSeq", last_seq, None, None), "limit": check_int("limit", limit, 1, None)}
        ),
    )


def _parse_list_reservation_recipients(body: dict[str, Any]) -> _r.ReservationRecipientListResult:
    found = pick(validate(_r.ReservationRecipientListResponse, body, "listReservationRecipients"), ("data", "data"))
    return found if isinstance(found, _r.ReservationRecipientListResult) else _r.ReservationRecipientListResult()


_PAGE_LIST_RESERVATION_RECIPIENTS = Pagination(
    style="cursor",
    request="lastSeq",
    items=("data", "data", "destinations"),
    cursor=("data", "data", "lastSeq"),
    has_next=("data", "data", "hasNext"),
)


def _call_delete_reservation_recipient(*, resv_key: str, msg_key: str) -> Call:
    return Call(
        operation="deleteReservationRecipient",
        method="DELETE",
        path=f"/api/comm/v1/reservation/resvKey/{segment(resv_key, 'resvKey')}/destinations/msgKey/{segment(msg_key, 'msgKey')}",
        retry=Retry.SAFE,
    )


def _call_get_alimtalk_insight(
    *,
    start_date: dt.date | str,
    end_date: dt.date | str,
    sender_key: str | Sequence[str],
    template_code: str | Sequence[str] | None,
) -> Call:
    return Call(
        operation="getAlimtalkInsight",
        method="GET",
        path="/api/comm/v1/center/statistics/alimtalk",
        retry=Retry.SAFE,
        params=query(
            {
                "startDate": need("startDate", date_param("startDate", start_date)),
                "endDate": need("endDate", date_param("endDate", end_date)),
                "senderKey": need("senderKey", array("senderKey", sender_key, explode=False, min_items=1)),
                "templateCode": array("templateCode", template_code, explode=False, min_items=0),
            }
        ),
    )


def _parse_get_alimtalk_insight(body: dict[str, Any]) -> _r.InsightKakaoStatisticsResult:
    found = pick(validate(_r.InsightKakaoStatisticsResponse, body, "getAlimtalkInsight"), ("data", "data"))
    return found if isinstance(found, _r.InsightKakaoStatisticsResult) else _r.InsightKakaoStatisticsResult()


def _call_get_alimtalk_hourly_insight(
    *,
    start_date: dt.date | str,
    end_date: dt.date | str,
    sender_key: str | Sequence[str],
    template_code: str | Sequence[str] | None,
) -> Call:
    return Call(
        operation="getAlimtalkHourlyInsight",
        method="GET",
        path="/api/comm/v1/center/statistics/alimtalk/reaction/hourly",
        retry=Retry.SAFE,
        params=query(
            {
                "startDate": need("startDate", date_param("startDate", start_date)),
                "endDate": need("endDate", date_param("endDate", end_date)),
                "senderKey": need("senderKey", array("senderKey", sender_key, explode=False, min_items=1)),
                "templateCode": array("templateCode", template_code, explode=False, min_items=0),
            }
        ),
    )


def _parse_get_alimtalk_hourly_insight(body: dict[str, Any]) -> _r.InsightKakaoHourlyStatisticsResult:
    found = pick(validate(_r.InsightKakaoHourlyStatisticsResponse, body, "getAlimtalkHourlyInsight"), ("data", "data"))
    return (
        found if isinstance(found, _r.InsightKakaoHourlyStatisticsResult) else _r.InsightKakaoHourlyStatisticsResult()
    )


def _call_get_alimtalk_template_insight(
    *,
    start_date: dt.date | str,
    end_date: dt.date | str,
    sender_key: str | Sequence[str],
    template_code: str | Sequence[str] | None,
) -> Call:
    return Call(
        operation="getAlimtalkTemplateInsight",
        method="GET",
        path="/api/comm/v1/center/statistics/alimtalk/template",
        retry=Retry.SAFE,
        params=query(
            {
                "startDate": need("startDate", date_param("startDate", start_date)),
                "endDate": need("endDate", date_param("endDate", end_date)),
                "senderKey": need("senderKey", array("senderKey", sender_key, explode=False, min_items=1)),
                "templateCode": array("templateCode", template_code, explode=False, min_items=0),
            }
        ),
    )


def _parse_get_alimtalk_template_insight(body: dict[str, Any]) -> _r.InsightKakaoTemplateStatisticsResult:
    found = pick(
        validate(_r.InsightKakaoTemplateStatisticsResponse, body, "getAlimtalkTemplateInsight"), ("data", "data")
    )
    return (
        found
        if isinstance(found, _r.InsightKakaoTemplateStatisticsResult)
        else _r.InsightKakaoTemplateStatisticsResult()
    )


def _call_get_brand_message_insight(
    *,
    start_date: dt.date | str,
    end_date: dt.date | str,
    sender_key: str | Sequence[str],
    template_code: str | Sequence[str] | None,
) -> Call:
    return Call(
        operation="getBrandMessageInsight",
        method="GET",
        path="/api/comm/v1/center/statistics/brandmessage",
        retry=Retry.SAFE,
        params=query(
            {
                "startDate": need("startDate", date_param("startDate", start_date)),
                "endDate": need("endDate", date_param("endDate", end_date)),
                "senderKey": need("senderKey", array("senderKey", sender_key, explode=False, min_items=1)),
                "templateCode": array("templateCode", template_code, explode=False, min_items=0),
            }
        ),
    )


def _parse_get_brand_message_insight(body: dict[str, Any]) -> _r.InsightKakaoStatisticsResult:
    found = pick(validate(_r.InsightKakaoStatisticsResponse, body, "getBrandMessageInsight"), ("data", "data"))
    return found if isinstance(found, _r.InsightKakaoStatisticsResult) else _r.InsightKakaoStatisticsResult()


def _call_get_brand_message_hourly_insight(
    *,
    start_date: dt.date | str,
    end_date: dt.date | str,
    sender_key: str | Sequence[str],
    template_code: str | Sequence[str] | None,
) -> Call:
    return Call(
        operation="getBrandMessageHourlyInsight",
        method="GET",
        path="/api/comm/v1/center/statistics/brandmessage/reaction/hourly",
        retry=Retry.SAFE,
        params=query(
            {
                "startDate": need("startDate", date_param("startDate", start_date)),
                "endDate": need("endDate", date_param("endDate", end_date)),
                "senderKey": need("senderKey", array("senderKey", sender_key, explode=False, min_items=1)),
                "templateCode": array("templateCode", template_code, explode=False, min_items=0),
            }
        ),
    )


def _parse_get_brand_message_hourly_insight(body: dict[str, Any]) -> _r.InsightKakaoHourlyStatisticsResult:
    found = pick(
        validate(_r.InsightKakaoHourlyStatisticsResponse, body, "getBrandMessageHourlyInsight"), ("data", "data")
    )
    return (
        found if isinstance(found, _r.InsightKakaoHourlyStatisticsResult) else _r.InsightKakaoHourlyStatisticsResult()
    )


def _call_get_brand_message_template_insight(
    *,
    start_date: dt.date | str,
    end_date: dt.date | str,
    sender_key: str | Sequence[str],
    template_code: str | Sequence[str] | None,
) -> Call:
    return Call(
        operation="getBrandMessageTemplateInsight",
        method="GET",
        path="/api/comm/v1/center/statistics/brandmessage/template",
        retry=Retry.SAFE,
        params=query(
            {
                "startDate": need("startDate", date_param("startDate", start_date)),
                "endDate": need("endDate", date_param("endDate", end_date)),
                "senderKey": need("senderKey", array("senderKey", sender_key, explode=False, min_items=1)),
                "templateCode": array("templateCode", template_code, explode=False, min_items=0),
            }
        ),
    )


def _parse_get_brand_message_template_insight(body: dict[str, Any]) -> _r.InsightKakaoTemplateStatisticsResult:
    found = pick(
        validate(_r.InsightKakaoTemplateStatisticsResponse, body, "getBrandMessageTemplateInsight"), ("data", "data")
    )
    return (
        found
        if isinstance(found, _r.InsightKakaoTemplateStatisticsResult)
        else _r.InsightKakaoTemplateStatisticsResult()
    )


def _call_get_rcs_message_insight(
    *, brand_id: str, start_date: dt.date | str, end_date: dt.date | str, group_id: str, chatbot_id: str | None
) -> Call:
    return Call(
        operation="getRcsMessageInsight",
        method="GET",
        path=f"/api/comm/v1/center/rcs/brandId/{segment(brand_id, 'brandId')}/stat/message",
        retry=Retry.SAFE,
        params=query(
            {
                "startDate": need("startDate", date_param("startDate", start_date)),
                "endDate": need("endDate", date_param("endDate", end_date)),
                "groupId": need("groupId", check_str("groupId", group_id, max_length=None, enum=())),
                "chatbotId": check_str("chatbotId", chatbot_id, max_length=None, enum=()),
            }
        ),
    )


def _parse_get_rcs_message_insight(body: dict[str, Any]) -> _r.InsightRcsMessageStatResult:
    found = pick(validate(_r.InsightRcsMessageStatResponse, body, "getRcsMessageInsight"), ("data", "rcs"))
    return found if isinstance(found, _r.InsightRcsMessageStatResult) else _r.InsightRcsMessageStatResult()


def _call_get_rcs_message_button_insight(
    *, brand_id: str, start_date: dt.date | str, end_date: dt.date | str, group_id: str, chatbot_id: str | None
) -> Call:
    return Call(
        operation="getRcsMessageButtonInsight",
        method="GET",
        path=f"/api/comm/v1/center/rcs/brandId/{segment(brand_id, 'brandId')}/stat/messageButton",
        retry=Retry.SAFE,
        params=query(
            {
                "startDate": need("startDate", date_param("startDate", start_date)),
                "endDate": need("endDate", date_param("endDate", end_date)),
                "groupId": need("groupId", check_str("groupId", group_id, max_length=None, enum=())),
                "chatbotId": check_str("chatbotId", chatbot_id, max_length=None, enum=()),
            }
        ),
    )


def _parse_get_rcs_message_button_insight(body: dict[str, Any]) -> _r.InsightRcsMessageButtonStatResult:
    found = pick(validate(_r.InsightRcsMessageButtonStatResponse, body, "getRcsMessageButtonInsight"), ("data", "rcs"))
    return found if isinstance(found, _r.InsightRcsMessageButtonStatResult) else _r.InsightRcsMessageButtonStatResult()


def _call_get_rcs_persistent_menu_insight(
    *, brand_id: str, start_date: dt.date | str, end_date: dt.date | str, chatbot_id: str
) -> Call:
    return Call(
        operation="getRcsPersistentMenuInsight",
        method="GET",
        path=f"/api/comm/v1/center/rcs/brandId/{segment(brand_id, 'brandId')}/stat/persistentMenu",
        retry=Retry.SAFE,
        params=query(
            {
                "startDate": need("startDate", date_param("startDate", start_date)),
                "endDate": need("endDate", date_param("endDate", end_date)),
                "chatbotId": need("chatbotId", check_str("chatbotId", chatbot_id, max_length=None, enum=())),
            }
        ),
    )


def _parse_get_rcs_persistent_menu_insight(body: dict[str, Any]) -> _r.InsightRcsPersistentMenuStatResult:
    found = pick(
        validate(_r.InsightRcsPersistentMenuStatResponse, body, "getRcsPersistentMenuInsight"), ("data", "rcs")
    )
    return (
        found if isinstance(found, _r.InsightRcsPersistentMenuStatResult) else _r.InsightRcsPersistentMenuStatResult()
    )


def _call_get_rcs_brand_profile_insight(*, brand_id: str, start_date: dt.date | str, end_date: dt.date | str) -> Call:
    return Call(
        operation="getRcsBrandProfileInsight",
        method="GET",
        path=f"/api/comm/v1/center/rcs/brandId/{segment(brand_id, 'brandId')}/stat/brandProfile",
        retry=Retry.SAFE,
        params=query(
            {
                "startDate": need("startDate", date_param("startDate", start_date)),
                "endDate": need("endDate", date_param("endDate", end_date)),
            }
        ),
    )


def _parse_get_rcs_brand_profile_insight(body: dict[str, Any]) -> _r.InsightRcsBrandProfileStatResult:
    found = pick(validate(_r.InsightRcsBrandProfileStatResponse, body, "getRcsBrandProfileInsight"), ("data", "rcs"))
    return found if isinstance(found, _r.InsightRcsBrandProfileStatResult) else _r.InsightRcsBrandProfileStatResult()


def _call_request_kakao_sender_token(*, body: _q.KakaoSenderTokenRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="requestKakaoSenderToken",
        method="POST",
        path="/api/comm/v1/account/kakao/sender/token",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.KakaoSenderTokenRequest, body),
    )


def _parse_request_kakao_sender_token(body: dict[str, Any]) -> _r.KakaoSenderAccountServiceResult:
    found = pick(validate(_r.KakaoSenderAccountResponse, body, "requestKakaoSenderToken"), ("data",))
    return found if isinstance(found, _r.KakaoSenderAccountServiceResult) else _r.KakaoSenderAccountServiceResult()


def _call_create_kakao_sender(
    *, token: str, phone_number: str, body: _q.KakaoSenderCreateRequest | Mapping[str, Any]
) -> Call:
    return Call(
        operation="createKakaoSender",
        method="POST",
        path="/api/comm/v1/account/kakao/sender",
        retry=Retry.RATE_LIMIT_ONLY,
        headers={"token": header("token", token), "phoneNumber": header("phoneNumber", phone_number)},
        json=json_body(_q.KakaoSenderCreateRequest, body),
    )


def _parse_create_kakao_sender(body: dict[str, Any]) -> _r.KakaoSenderProfile:
    found = pick(validate(_r.KakaoSenderAccountResponse, body, "createKakaoSender"), ("data", "kakao", "senderProfile"))
    return found if isinstance(found, _r.KakaoSenderProfile) else _r.KakaoSenderProfile()


def _call_find_kakao_sender(*, uuid: str | None, sender_key: str | None) -> Call:
    return Call(
        operation="findKakaoSender",
        method="GET",
        path="/api/comm/v1/account/kakao/sender",
        retry=Retry.SAFE,
        params=query(
            {
                "uuid": check_str("uuid", uuid, max_length=None, enum=()),
                "senderKey": check_str("senderKey", sender_key, max_length=None, enum=()),
            }
        ),
    )


def _parse_find_kakao_sender(body: dict[str, Any]) -> _r.KakaoSenderProfile:
    found = pick(validate(_r.KakaoSenderAccountResponse, body, "findKakaoSender"), ("data", "kakao", "senderProfile"))
    return found if isinstance(found, _r.KakaoSenderProfile) else _r.KakaoSenderProfile()


def _call_list_kakao_sender_profiles(
    *, start_date: str | None, end_date: str | None, sender_key: str | None, page: int | None, rows: int | None
) -> Call:
    return Call(
        operation="listKakaoSenderProfiles",
        method="GET",
        path="/api/comm/v1/account/kakao/sender/profiles",
        retry=Retry.SAFE,
        params=query(
            {
                "startDate": check_str("startDate", start_date, max_length=None, enum=()),
                "endDate": check_str("endDate", end_date, max_length=None, enum=()),
                "senderKey": check_str("senderKey", sender_key, max_length=None, enum=()),
                "page": check_int("page", page, None, None),
                "rows": check_int("rows", rows, None, None),
            }
        ),
    )


def _parse_list_kakao_sender_profiles(body: dict[str, Any]) -> _r.KakaoSenderListServiceResult:
    found = pick(validate(_r.KakaoSenderListResponse, body, "listKakaoSenderProfiles"), ("data",))
    return found if isinstance(found, _r.KakaoSenderListServiceResult) else _r.KakaoSenderListServiceResult()


_PAGE_LIST_KAKAO_SENDER_PROFILES = Pagination(
    style="page",
    request="page",
    items=("data", "channels"),
    size="rows",
    has_next=("data", "hasNext"),
    total=("data", "totalCount"),
)


def _call_get_kakao_sender(*, sender_key: str) -> Call:
    return Call(
        operation="getKakaoSender",
        method="GET",
        path="/api/comm/v1/center/kakao/sender",
        retry=Retry.SAFE,
        params=query({"senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=()))}),
    )


def _parse_get_kakao_sender(body: dict[str, Any]) -> _r.KakaoSenderProfile:
    found = pick(validate(_r.KakaoSenderResponse, body, "getKakaoSender"), ("data", "data", "kakao", "senderProfile"))
    return found if isinstance(found, _r.KakaoSenderProfile) else _r.KakaoSenderProfile()


def _call_recover_kakao_sender(*, body: _q.KakaoSenderRecoverRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="recoverKakaoSender",
        method="POST",
        path="/api/comm/v1/center/kakao/sender/recover",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.KakaoSenderRecoverRequest, body),
    )


def _call_list_kakao_sender_categories() -> Call:
    return Call(
        operation="listKakaoSenderCategories",
        method="GET",
        path="/api/comm/v1/center/kakao/sender/category/list",
        retry=Retry.SAFE,
    )


def _parse_list_kakao_sender_categories(body: dict[str, Any]) -> builtins.list[_r.KakaoCategory]:
    return pick_list(
        validate(_r.KakaoCategoryListResponse, body, "listKakaoSenderCategories"),
        ("data", "data", "kakao", "categories"),
    )


def _call_get_kakao_sender_category(*, code: str) -> Call:
    return Call(
        operation="getKakaoSenderCategory",
        method="GET",
        path="/api/comm/v1/center/kakao/sender/category",
        retry=Retry.SAFE,
        params=query({"code": need("code", check_str("code", code, max_length=None, enum=()))}),
    )


def _parse_get_kakao_sender_category(body: dict[str, Any]) -> _r.KakaoCategory:
    found = pick(
        validate(_r.KakaoCategoryResponse, body, "getKakaoSenderCategory"), ("data", "data", "kakao", "category")
    )
    return found if isinstance(found, _r.KakaoCategory) else _r.KakaoCategory()


def _call_list_kakao_groups(*, sender_key: str | None) -> Call:
    return Call(
        operation="listKakaoGroups",
        method="GET",
        path="/api/comm/v1/center/kakao/group",
        retry=Retry.SAFE,
        params=query({"senderKey": check_str("senderKey", sender_key, max_length=None, enum=())}),
    )


def _parse_list_kakao_groups(body: dict[str, Any]) -> builtins.list[_r.KakaoGroup]:
    return pick_list(validate(_r.KakaoGroupListResponse, body, "listKakaoGroups"), ("data", "data", "kakao", "groups"))


def _call_add_kakao_group_sender(*, body: _q.KakaoGroupSenderAddRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="addKakaoGroupSender",
        method="POST",
        path="/api/comm/v1/center/kakao/group",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.KakaoGroupSenderAddRequest, body),
    )


def _call_remove_kakao_group_sender(*, group_key: str, sender_key: str) -> Call:
    return Call(
        operation="removeKakaoGroupSender",
        method="DELETE",
        path=f"/api/comm/v1/center/kakao/group/groupKey/{segment(group_key, 'groupKey')}/senderKey/{segment(sender_key, 'senderKey')}",
        retry=Retry.SAFE,
    )


def _call_get_kakao_sender_sanction(*, date: dt.date | str, sender_key: str) -> Call:
    return Call(
        operation="getKakaoSenderSanction",
        method="GET",
        path="/api/comm/v1/center/kakao/abusing/block/sender",
        retry=Retry.SAFE,
        params=query(
            {
                "date": need("date", date_param("date", date)),
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
            }
        ),
    )


def _parse_get_kakao_sender_sanction(body: dict[str, Any]) -> _r.KakaoSanction:
    found = pick(
        validate(_r.KakaoSanctionResponse, body, "getKakaoSenderSanction"), ("data", "data", "kakao", "abusing")
    )
    return found if isinstance(found, _r.KakaoSanction) else _r.KakaoSanction()


def _call_get_kakao_group_template_sender_exclusion(
    *, date: dt.date | str, sender_key: str, group_key: str, template_code: str
) -> Call:
    return Call(
        operation="getKakaoGroupTemplateSenderExclusion",
        method="GET",
        path="/api/comm/v1/center/kakao/abusing/block/senderGroup",
        retry=Retry.SAFE,
        params=query(
            {
                "date": need("date", date_param("date", date)),
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
                "groupKey": need("groupKey", check_str("groupKey", group_key, max_length=None, enum=())),
                "templateCode": need(
                    "templateCode", check_str("templateCode", template_code, max_length=None, enum=())
                ),
            }
        ),
    )


def _parse_get_kakao_group_template_sender_exclusion(body: dict[str, Any]) -> _r.KakaoSanction:
    found = pick(
        validate(_r.KakaoSanctionResponse, body, "getKakaoGroupTemplateSenderExclusion"),
        ("data", "data", "kakao", "abusing"),
    )
    return found if isinstance(found, _r.KakaoSanction) else _r.KakaoSanction()


def _call_get_kakao_template_sanction(*, date: dt.date | str, sender_key: str, template_code: str) -> Call:
    return Call(
        operation="getKakaoTemplateSanction",
        method="GET",
        path="/api/comm/v1/center/kakao/abusing/block/template",
        retry=Retry.SAFE,
        params=query(
            {
                "date": need("date", date_param("date", date)),
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
                "templateCode": need(
                    "templateCode", check_str("templateCode", template_code, max_length=None, enum=())
                ),
            }
        ),
    )


def _parse_get_kakao_template_sanction(body: dict[str, Any]) -> _r.KakaoSanction:
    found = pick(
        validate(_r.KakaoSanctionResponse, body, "getKakaoTemplateSanction"), ("data", "data", "kakao", "abusing")
    )
    return found if isinstance(found, _r.KakaoSanction) else _r.KakaoSanction()


def _call_get_alimtalk_template(*, sender_key: str, template_code: str) -> Call:
    return Call(
        operation="getAlimtalkTemplate",
        method="GET",
        path="/api/comm/v1/center/alimtalk/template",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
                "templateCode": need(
                    "templateCode", check_str("templateCode", template_code, max_length=None, enum=())
                ),
            }
        ),
    )


def _parse_get_alimtalk_template(body: dict[str, Any]) -> _r.AlimtalkTemplate:
    found = pick(validate(_r.AlimtalkTemplateResponse, body, "getAlimtalkTemplate"), ("data", "data", "alimtalk"))
    return found if isinstance(found, _r.AlimtalkTemplate) else _r.AlimtalkTemplate()


def _call_create_alimtalk_template(*, body: _q.AlimtalkTemplateSaveRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="createAlimtalkTemplate",
        method="POST",
        path="/api/comm/v1/center/alimtalk/template",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.AlimtalkTemplateSaveRequest, body),
    )


def _parse_create_alimtalk_template(body: dict[str, Any]) -> _r.AlimtalkTemplate:
    found = pick(validate(_r.AlimtalkTemplateResponse, body, "createAlimtalkTemplate"), ("data", "data", "alimtalk"))
    return found if isinstance(found, _r.AlimtalkTemplate) else _r.AlimtalkTemplate()


def _call_update_alimtalk_template(*, body: _q.AlimtalkTemplateSaveRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="updateAlimtalkTemplate",
        method="PUT",
        path="/api/comm/v1/center/alimtalk/template",
        retry=Retry.SAFE,
        json=json_body(_q.AlimtalkTemplateSaveRequest, body),
    )


def _parse_update_alimtalk_template(body: dict[str, Any]) -> _r.AlimtalkTemplate:
    found = pick(validate(_r.AlimtalkTemplateResponse, body, "updateAlimtalkTemplate"), ("data", "data", "alimtalk"))
    return found if isinstance(found, _r.AlimtalkTemplate) else _r.AlimtalkTemplate()


def _call_list_alimtalk_templates(
    *,
    sender_key: str,
    sender_key_type: Literal["G", "S"] | None,
    status: str | None,
    inspection_status: Literal["REG", "REQ", "APR", "REJ"] | None,
    template_type: str | None,
    offset: int | None,
    limit: int | None,
) -> Call:
    return Call(
        operation="listAlimtalkTemplates",
        method="GET",
        path="/api/comm/v1/center/alimtalk/template/list",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
                "senderKeyType": check_str("senderKeyType", sender_key_type, max_length=None, enum=("G", "S")),
                "status": check_str("status", status, max_length=None, enum=()),
                "inspectionStatus": check_str(
                    "inspectionStatus", inspection_status, max_length=None, enum=("REG", "REQ", "APR", "REJ")
                ),
                "templateType": check_str("templateType", template_type, max_length=None, enum=()),
                "offset": check_int("offset", offset, 0, None),
                "limit": check_int("limit", limit, 1, None),
            }
        ),
    )


def _parse_list_alimtalk_templates(body: dict[str, Any]) -> builtins.list[_r.AlimtalkTemplate]:
    return pick_list(
        validate(_r.AlimtalkTemplateListResponse, body, "listAlimtalkTemplates"),
        ("data", "data", "alimtalk", "templates"),
    )


_PAGE_LIST_ALIMTALK_TEMPLATES = Pagination(
    style="offset", request="offset", items=("data", "data", "alimtalk", "templates"), size="limit"
)


def _call_list_modified_alimtalk_templates(
    *,
    sender_key: str,
    sender_key_type: Literal["G", "S"] | None,
    since: dt.datetime | str | None,
    page: int | None,
    count: int | None,
) -> Call:
    return Call(
        operation="listModifiedAlimtalkTemplates",
        method="GET",
        path="/api/comm/v1/center/alimtalk/template/lastModified",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=40, enum=())),
                "senderKeyType": check_str("senderKeyType", sender_key_type, max_length=None, enum=("G", "S")),
                "since": datetime_param("since", since, "yyyy-MM-dd'T'HH:mm:ss"),
                "page": check_int("page", page, 1, None),
                "count": check_int("count", count, 1, None),
            }
        ),
    )


def _parse_list_modified_alimtalk_templates(body: dict[str, Any]) -> builtins.list[_r.AlimtalkTemplate]:
    return pick_list(
        validate(_r.AlimtalkTemplateListResponse, body, "listModifiedAlimtalkTemplates"),
        ("data", "data", "alimtalk", "templates"),
    )


_PAGE_LIST_MODIFIED_ALIMTALK_TEMPLATES = Pagination(
    style="page", request="page", items=("data", "data", "alimtalk", "templates"), size="count"
)


def _call_delete_alimtalk_template(*, sender_key: str, template_code: str) -> Call:
    return Call(
        operation="deleteAlimtalkTemplate",
        method="DELETE",
        path=f"/api/comm/v1/center/alimtalk/template/senderKey/{segment(sender_key, 'senderKey')}/templateCode/{segment(template_code, 'templateCode')}",
        retry=Retry.SAFE,
    )


def _call_upload_alimtalk_template_image(
    *, file: FileInput, filename: str | None, file_key: str | None, image_name: str | None
) -> Call:
    form = Form()
    need("file", file)
    form.file("file", file, filename, "image.jpg", max_bytes=None)
    form.text("fileKey", check_str("fileKey", file_key, max_length=None, enum=()))
    form.text("imageName", check_str("imageName", image_name, max_length=None, enum=()))
    return Call(
        operation="uploadAlimtalkTemplateImage",
        method="POST",
        path="/api/comm/v1/file/alimtalk/template",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_alimtalk_template_image(body: dict[str, Any]) -> _r.AlimtalkTemplateImageUploadResult:
    found = pick(
        validate(_r.AlimtalkTemplateImageUploadResponse, body, "uploadAlimtalkTemplateImage"), ("data", "data")
    )
    return found if isinstance(found, _r.AlimtalkTemplateImageUploadResult) else _r.AlimtalkTemplateImageUploadResult()


def _call_upload_alimtalk_item_highlight_image(
    *, file: FileInput, filename: str | None, file_key: str | None, image_name: str | None
) -> Call:
    form = Form()
    need("file", file)
    form.file("file", file, filename, "image.jpg", max_bytes=None)
    form.text("fileKey", check_str("fileKey", file_key, max_length=None, enum=()))
    form.text("imageName", check_str("imageName", image_name, max_length=None, enum=()))
    return Call(
        operation="uploadAlimtalkItemHighlightImage",
        method="POST",
        path="/api/comm/v1/file/alimtalk/itemHighlight",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_alimtalk_item_highlight_image(body: dict[str, Any]) -> _r.AlimtalkTemplateImageUploadResult:
    found = pick(
        validate(_r.AlimtalkTemplateImageUploadResponse, body, "uploadAlimtalkItemHighlightImage"), ("data", "data")
    )
    return found if isinstance(found, _r.AlimtalkTemplateImageUploadResult) else _r.AlimtalkTemplateImageUploadResult()


def _call_list_alimtalk_template_categories(*, category_code: str | None) -> Call:
    return Call(
        operation="listAlimtalkTemplateCategories",
        method="GET",
        path="/api/comm/v1/center/alimtalk/category",
        retry=Retry.SAFE,
        params=query({"categoryCode": check_str("categoryCode", category_code, max_length=None, enum=())}),
    )


def _parse_list_alimtalk_template_categories(body: dict[str, Any]) -> _r.AlimtalkTemplateCategoryResult:
    found = pick(
        validate(_r.AlimtalkTemplateCategoryResponse, body, "listAlimtalkTemplateCategories"), ("data", "data")
    )
    return found if isinstance(found, _r.AlimtalkTemplateCategoryResult) else _r.AlimtalkTemplateCategoryResult()


def _call_request_alimtalk_template_inspection(
    *, body: _q.AlimtalkTemplateInspectionRequest | Mapping[str, Any]
) -> Call:
    return Call(
        operation="requestAlimtalkTemplateInspection",
        method="POST",
        path="/api/comm/v1/center/alimtalk/template/request",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.AlimtalkTemplateInspectionRequest, body),
    )


def _call_request_alimtalk_template_inspection_form(
    *,
    sender_key: str,
    sender_key_type: Literal["G", "S"] | None,
    template_code: str,
    comment: str,
    attachment: Sequence[FileInput] | None,
) -> Call:
    form = Form()
    need("senderKey", sender_key)
    form.text("senderKey", check_str("senderKey", sender_key, max_length=None, enum=()))
    form.text("senderKeyType", check_str("senderKeyType", sender_key_type, max_length=None, enum=("G", "S")))
    need("templateCode", template_code)
    form.text("templateCode", check_str("templateCode", template_code, max_length=None, enum=()))
    need("comment", comment)
    form.text("comment", check_str("comment", comment, max_length=None, enum=()))
    form.files_of("attachment", attachment, "file.bin", 10)
    return Call(
        operation="requestAlimtalkTemplateInspection",
        method="POST",
        path="/api/comm/v1/center/alimtalk/template/request",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _call_cancel_alimtalk_template_inspection(
    *, body: _q.AlimtalkTemplateInspectionCancelRequest | Mapping[str, Any]
) -> Call:
    return Call(
        operation="cancelAlimtalkTemplateInspection",
        method="POST",
        path="/api/comm/v1/center/alimtalk/template/request/cancel",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.AlimtalkTemplateInspectionCancelRequest, body),
    )


def _call_list_alimtalk_public_templates(
    *, since: dt.datetime | str | None, page: int | None, count: int | None
) -> Call:
    return Call(
        operation="listAlimtalkPublicTemplates",
        method="GET",
        path="/api/comm/v1/center/alimtalk/public/template",
        retry=Retry.SAFE,
        params=query(
            {
                "since": datetime_param("since", since, "yyyyMMddHHmmss"),
                "page": check_int("page", page, 1, None),
                "count": check_int("count", count, 1, 1000),
            }
        ),
    )


def _parse_list_alimtalk_public_templates(body: dict[str, Any]) -> builtins.list[_r.AlimtalkTemplatePublic]:
    return pick_list(
        validate(_r.AlimtalkTemplatePublicListResponse, body, "listAlimtalkPublicTemplates"),
        ("data", "data", "templates"),
    )


_PAGE_LIST_ALIMTALK_PUBLIC_TEMPLATES = Pagination(
    style="page", request="page", items=("data", "data", "templates"), size="count"
)


def _call_create_brand_message_group_send(*, body: _q.BrandMessageGroupSendCreateRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="createBrandMessageGroupSend",
        method="POST",
        path="/api/comm/v1/center/brandmessage/groupMessage",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.BrandMessageGroupSendCreateRequest, body),
    )


def _parse_create_brand_message_group_send(body: dict[str, Any]) -> _r.BrandMessageGroupSendResult:
    found = pick(validate(_r.BrandMessageGroupSendResponse, body, "createBrandMessageGroupSend"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageGroupSendResult) else _r.BrandMessageGroupSendResult()


def _call_get_brand_message_group_send(*, sender_key: str, request_id: int) -> Call:
    return Call(
        operation="getBrandMessageGroupSend",
        method="GET",
        path="/api/comm/v1/center/brandmessage/groupMessage",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
                "requestId": need("requestId", check_int("requestId", request_id, None, None)),
            }
        ),
    )


def _parse_get_brand_message_group_send(body: dict[str, Any]) -> _r.BrandMessageGroupSendResult:
    found = pick(validate(_r.BrandMessageGroupSendResponse, body, "getBrandMessageGroupSend"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageGroupSendResult) else _r.BrandMessageGroupSendResult()


def _call_resume_brand_message_group_send(*, body: _q.BrandMessageGroupSendControlRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="resumeBrandMessageGroupSend",
        method="POST",
        path="/api/comm/v1/center/brandmessage/groupMessage/resume",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.BrandMessageGroupSendControlRequest, body),
    )


def _parse_resume_brand_message_group_send(body: dict[str, Any]) -> _r.BrandMessageGroupSendResult:
    found = pick(validate(_r.BrandMessageGroupSendResponse, body, "resumeBrandMessageGroupSend"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageGroupSendResult) else _r.BrandMessageGroupSendResult()


def _call_pause_brand_message_group_send(*, body: _q.BrandMessageGroupSendControlRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="pauseBrandMessageGroupSend",
        method="POST",
        path="/api/comm/v1/center/brandmessage/groupMessage/pause",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.BrandMessageGroupSendControlRequest, body),
    )


def _parse_pause_brand_message_group_send(body: dict[str, Any]) -> _r.BrandMessageGroupSendResult:
    found = pick(validate(_r.BrandMessageGroupSendResponse, body, "pauseBrandMessageGroupSend"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageGroupSendResult) else _r.BrandMessageGroupSendResult()


def _call_terminate_brand_message_group_send(
    *, body: _q.BrandMessageGroupSendControlRequest | Mapping[str, Any]
) -> Call:
    return Call(
        operation="terminateBrandMessageGroupSend",
        method="POST",
        path="/api/comm/v1/center/brandmessage/groupMessage/terminate",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.BrandMessageGroupSendControlRequest, body),
    )


def _parse_terminate_brand_message_group_send(body: dict[str, Any]) -> _r.BrandMessageGroupSendResult:
    found = pick(validate(_r.BrandMessageGroupSendResponse, body, "terminateBrandMessageGroupSend"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageGroupSendResult) else _r.BrandMessageGroupSendResult()


def _call_check_brand_message_audience_possible(
    *, sender_key: str, msg_type: str, friend_group_key: str | None
) -> Call:
    return Call(
        operation="checkBrandMessageAudiencePossible",
        method="GET",
        path="/api/comm/v1/center/brandmessage/groupMessage/possible",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
                "msgType": need("msgType", check_str("msgType", msg_type, max_length=None, enum=())),
                "friendGroupKey": check_str("friendGroupKey", friend_group_key, max_length=None, enum=()),
            }
        ),
    )


def _parse_check_brand_message_audience_possible(body: dict[str, Any]) -> _r.BrandMessageAudiencePossibleResult:
    found = pick(
        validate(_r.BrandMessageAudiencePossibleResponse, body, "checkBrandMessageAudiencePossible"), ("data", "data")
    )
    return (
        found if isinstance(found, _r.BrandMessageAudiencePossibleResult) else _r.BrandMessageAudiencePossibleResult()
    )


def _call_check_brand_message_audience_possible_by_phone_numbers(
    *, body: _q.BrandMessageAudiencePossibleByPhoneNumbersRequest | Mapping[str, Any]
) -> Call:
    return Call(
        operation="checkBrandMessageAudiencePossibleByPhoneNumbers",
        method="POST",
        path="/api/comm/v1/center/brandmessage/groupMessage/friend/possible",
        retry=Retry.SAFE,
        json=json_body(_q.BrandMessageAudiencePossibleByPhoneNumbersRequest, body),
    )


def _parse_check_brand_message_audience_possible_by_phone_numbers(
    body: dict[str, Any],
) -> _r.BrandMessageAudiencePossibleResult:
    found = pick(
        validate(_r.BrandMessageAudiencePossibleResponse, body, "checkBrandMessageAudiencePossibleByPhoneNumbers"),
        ("data", "data"),
    )
    return (
        found if isinstance(found, _r.BrandMessageAudiencePossibleResult) else _r.BrandMessageAudiencePossibleResult()
    )


def _call_get_brand_message_friend_count(*, sender_key: str) -> Call:
    return Call(
        operation="getBrandMessageFriendCount",
        method="GET",
        path="/api/comm/v1/center/brandmessage/groupMessage/friendCount",
        retry=Retry.SAFE,
        params=query({"senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=()))}),
    )


def _parse_get_brand_message_friend_count(body: dict[str, Any]) -> _r.BrandMessageAudienceFriendCountResult:
    found = pick(
        validate(_r.BrandMessageAudienceFriendCountResponse, body, "getBrandMessageFriendCount"), ("data", "data")
    )
    return (
        found
        if isinstance(found, _r.BrandMessageAudienceFriendCountResult)
        else _r.BrandMessageAudienceFriendCountResult()
    )


def _call_estimate_brand_message_group_send_duration(
    *, sender_key: str, start_time: dt.datetime | str, count: int, target: Literal["NONE", "FRIEND_GROUP"] | None
) -> Call:
    return Call(
        operation="estimateBrandMessageGroupSendDuration",
        method="GET",
        path="/api/comm/v1/center/brandmessage/groupMessage/estimate",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
                "startTime": need("startTime", datetime_param("startTime", start_time, "yyyy-MM-dd'T'HH:mm:ss")),
                "count": need("count", check_int("count", count, None, None)),
                "target": check_str("target", target, max_length=None, enum=("NONE", "FRIEND_GROUP")),
            }
        ),
    )


def _parse_estimate_brand_message_group_send_duration(body: dict[str, Any]) -> _r.BrandMessageAudienceEstimateResult:
    found = pick(
        validate(_r.BrandMessageAudienceEstimateResponse, body, "estimateBrandMessageGroupSendDuration"),
        ("data", "data"),
    )
    return (
        found if isinstance(found, _r.BrandMessageAudienceEstimateResult) else _r.BrandMessageAudienceEstimateResult()
    )


def _call_check_brand_message_send_permission(*, sender_key: str) -> Call:
    return Call(
        operation="checkBrandMessageSendPermission",
        method="GET",
        path="/api/comm/v1/center/brandmessage/sendPermission",
        retry=Retry.SAFE,
        params=query({"senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=40, enum=()))}),
    )


def _call_apply_brand_message_send_permission(
    *, body: _q.BrandMessagePermissionApplyRequest | Mapping[str, Any]
) -> Call:
    return Call(
        operation="applyBrandMessageSendPermission",
        method="POST",
        path="/api/comm/v1/center/brandmessage/sendPermission",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.BrandMessagePermissionApplyRequest, body),
    )


def _call_upload_brand_message_catalog_image(
    *, file: FileInput, filename: str | None, file_key: str | None, image_name: str | None
) -> Call:
    form = Form()
    need("file", file)
    form.file("file", file, filename, "image.jpg", max_bytes=None)
    form.text("fileKey", check_str("fileKey", file_key, max_length=None, enum=()))
    form.text("imageName", check_str("imageName", image_name, max_length=None, enum=()))
    return Call(
        operation="uploadBrandMessageCatalogImage",
        method="POST",
        path="/api/comm/v1/file/brandmessage/catalog",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_brand_message_catalog_image(body: dict[str, Any]) -> _r.BrandMessageFileUploadResult:
    found = pick(validate(_r.BrandMessageFileUploadResponse, body, "uploadBrandMessageCatalogImage"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageFileUploadResult) else _r.BrandMessageFileUploadResult()


def _call_upload_brand_message_catalog_odd_first_image(
    *, file: FileInput, filename: str | None, file_key: str | None, image_name: str | None
) -> Call:
    form = Form()
    need("file", file)
    form.file("file", file, filename, "image.jpg", max_bytes=None)
    form.text("fileKey", check_str("fileKey", file_key, max_length=None, enum=()))
    form.text("imageName", check_str("imageName", image_name, max_length=None, enum=()))
    return Call(
        operation="uploadBrandMessageCatalogOddFirstImage",
        method="POST",
        path="/api/comm/v1/file/brandmessage/catalog/oddFirst",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_brand_message_catalog_odd_first_image(body: dict[str, Any]) -> _r.BrandMessageFileUploadResult:
    found = pick(
        validate(_r.BrandMessageFileUploadResponse, body, "uploadBrandMessageCatalogOddFirstImage"), ("data", "data")
    )
    return found if isinstance(found, _r.BrandMessageFileUploadResult) else _r.BrandMessageFileUploadResult()


def _call_register_brand_message_video_upload(
    *, body: _q.BrandMessageVideoUploadRegisterRequest | Mapping[str, Any]
) -> Call:
    return Call(
        operation="registerBrandMessageVideoUpload",
        method="POST",
        path="/api/comm/v1/center/brandmessage/video/upload/register",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.BrandMessageVideoUploadRegisterRequest, body),
    )


def _parse_register_brand_message_video_upload(body: dict[str, Any]) -> _r.BrandMessageVideoUploadRegisterResult:
    found = pick(
        validate(_r.BrandMessageVideoUploadRegisterResponse, body, "registerBrandMessageVideoUpload"), ("data", "data")
    )
    return (
        found
        if isinstance(found, _r.BrandMessageVideoUploadRegisterResult)
        else _r.BrandMessageVideoUploadRegisterResult()
    )


def _call_register_brand_message_existing_video(
    *, body: _q.BrandMessageVideoRegisterRequest | Mapping[str, Any]
) -> Call:
    return Call(
        operation="registerBrandMessageExistingVideo",
        method="POST",
        path="/api/comm/v1/center/brandmessage/video/register",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.BrandMessageVideoRegisterRequest, body),
    )


def _parse_register_brand_message_existing_video(body: dict[str, Any]) -> _r.BrandMessageVideoInfoResult:
    found = pick(
        validate(_r.BrandMessageVideoInfoResponse, body, "registerBrandMessageExistingVideo"), ("data", "data")
    )
    return found if isinstance(found, _r.BrandMessageVideoInfoResult) else _r.BrandMessageVideoInfoResult()


def _call_get_brand_message_video(*, vid: str, sender_key: str) -> Call:
    return Call(
        operation="getBrandMessageVideo",
        method="GET",
        path="/api/comm/v1/center/brandmessage/video",
        retry=Retry.SAFE,
        params=query(
            {
                "vid": need("vid", check_str("vid", vid, max_length=None, enum=())),
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=40, enum=())),
            }
        ),
    )


def _parse_get_brand_message_video(body: dict[str, Any]) -> _r.BrandMessageVideoInfoResult:
    found = pick(validate(_r.BrandMessageVideoInfoResponse, body, "getBrandMessageVideo"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageVideoInfoResult) else _r.BrandMessageVideoInfoResult()


def _call_list_brand_message_videos(
    *, sender_key: str, date: dt.date | str | None, offset: int | None, limit: int | None
) -> Call:
    return Call(
        operation="listBrandMessageVideos",
        method="GET",
        path="/api/comm/v1/center/brandmessage/video/list",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=40, enum=())),
                "date": date_param("date", date),
                "offset": check_int("offset", offset, 0, None),
                "limit": check_int("limit", limit, 1, 1000),
            }
        ),
    )


def _parse_list_brand_message_videos(body: dict[str, Any]) -> _r.BrandMessageVideoListResult:
    found = pick(validate(_r.BrandMessageVideoListResponse, body, "listBrandMessageVideos"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageVideoListResult) else _r.BrandMessageVideoListResult()


_PAGE_LIST_BRAND_MESSAGE_VIDEOS = Pagination(
    style="offset",
    request="offset",
    items=("data", "data", "videos"),
    size="limit",
    total=("data", "data", "totalCount"),
)


def _call_get_brand_message_template(
    *, sender_key: str, template_code: str, send_type: Literal["basic", "free"] | None
) -> Call:
    return Call(
        operation="getBrandMessageTemplate",
        method="GET",
        path="/api/comm/v1/center/brandmessage/template",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
                "templateCode": need(
                    "templateCode", check_str("templateCode", template_code, max_length=None, enum=())
                ),
                "sendType": check_str("sendType", send_type, max_length=None, enum=("basic", "free")),
            }
        ),
    )


def _parse_get_brand_message_template(body: dict[str, Any]) -> _r.BrandMessageTemplateResult:
    found = pick(validate(_r.BrandMessageTemplateResponse, body, "getBrandMessageTemplate"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageTemplateResult) else _r.BrandMessageTemplateResult()


def _call_create_brand_message_template(*, body: _q.BrandMessageTemplateRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="createBrandMessageTemplate",
        method="POST",
        path="/api/comm/v1/center/brandmessage/template",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.BrandMessageTemplateRequest, body),
    )


def _parse_create_brand_message_template(body: dict[str, Any]) -> _r.BrandMessageTemplateResult:
    found = pick(validate(_r.BrandMessageTemplateResponse, body, "createBrandMessageTemplate"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageTemplateResult) else _r.BrandMessageTemplateResult()


def _call_update_brand_message_template(*, body: _q.BrandMessageTemplateRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="updateBrandMessageTemplate",
        method="PUT",
        path="/api/comm/v1/center/brandmessage/template",
        retry=Retry.SAFE,
        json=json_body(_q.BrandMessageTemplateRequest, body),
    )


def _parse_update_brand_message_template(body: dict[str, Any]) -> _r.BrandMessageTemplateResult:
    found = pick(validate(_r.BrandMessageTemplateResponse, body, "updateBrandMessageTemplate"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageTemplateResult) else _r.BrandMessageTemplateResult()


def _call_list_brand_message_templates(
    *,
    sender_key: str,
    sender_key_type: str | None,
    status: str | None,
    template_type: str | None,
    offset: int | None,
    limit: int | None,
) -> Call:
    return Call(
        operation="listBrandMessageTemplates",
        method="GET",
        path="/api/comm/v1/center/brandmessage/template/list",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
                "senderKeyType": check_str("senderKeyType", sender_key_type, max_length=None, enum=()),
                "status": check_str("status", status, max_length=None, enum=()),
                "templateType": check_str("templateType", template_type, max_length=None, enum=()),
                "offset": check_int("offset", offset, 0, None),
                "limit": check_int("limit", limit, 1, None),
            }
        ),
    )


def _parse_list_brand_message_templates(body: dict[str, Any]) -> _r.BrandMessageTemplateListResult:
    found = pick(validate(_r.BrandMessageTemplateListResponse, body, "listBrandMessageTemplates"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageTemplateListResult) else _r.BrandMessageTemplateListResult()


_PAGE_LIST_BRAND_MESSAGE_TEMPLATES = Pagination(
    style="offset", request="offset", items=("data", "data", "brandmessage", "templates"), size="limit"
)


def _call_list_brand_message_templates_last_modified(
    *,
    sender_key: str,
    sender_key_type: str | None,
    since: dt.datetime | str | None,
    page: int | None,
    count: int | None,
) -> Call:
    return Call(
        operation="listBrandMessageTemplatesLastModified",
        method="GET",
        path="/api/comm/v1/center/brandmessage/template/lastModified",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=40, enum=())),
                "senderKeyType": check_str("senderKeyType", sender_key_type, max_length=None, enum=()),
                "since": datetime_param("since", since, "yyyy-MM-dd'T'HH:mm:ss"),
                "page": check_int("page", page, 1, None),
                "count": check_int("count", count, 1, None),
            }
        ),
    )


def _parse_list_brand_message_templates_last_modified(body: dict[str, Any]) -> _r.BrandMessageTemplateListResult:
    found = pick(
        validate(_r.BrandMessageTemplateListResponse, body, "listBrandMessageTemplatesLastModified"), ("data", "data")
    )
    return found if isinstance(found, _r.BrandMessageTemplateListResult) else _r.BrandMessageTemplateListResult()


_PAGE_LIST_BRAND_MESSAGE_TEMPLATES_LAST_MODIFIED = Pagination(
    style="page", request="page", items=("data", "data", "brandmessage", "templates"), size="count"
)


def _call_delete_brand_message_template(*, sender_key: str, template_code: str) -> Call:
    return Call(
        operation="deleteBrandMessageTemplate",
        method="DELETE",
        path=f"/api/comm/v1/center/brandmessage/template/senderKey/{segment(sender_key, 'senderKey')}/templateCode/{segment(template_code, 'templateCode')}",
        retry=Retry.SAFE,
    )


def _call_list_brand_message_group_tags(*, sender_key: str) -> Call:
    return Call(
        operation="listBrandMessageGroupTags",
        method="GET",
        path="/api/comm/v1/center/brandmessage/groupTag/list",
        retry=Retry.SAFE,
        params=query({"senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=()))}),
    )


def _parse_list_brand_message_group_tags(body: dict[str, Any]) -> _r.BrandMessageGroupTagListResult:
    found = pick(validate(_r.BrandMessageGroupTagListResponse, body, "listBrandMessageGroupTags"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageGroupTagListResult) else _r.BrandMessageGroupTagListResult()


def _call_get_brand_message_group_tag(*, sender_key: str, group_tag_key: str) -> Call:
    return Call(
        operation="getBrandMessageGroupTag",
        method="GET",
        path="/api/comm/v1/center/brandmessage/groupTag",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
                "groupTagKey": need("groupTagKey", check_str("groupTagKey", group_tag_key, max_length=None, enum=())),
            }
        ),
    )


def _parse_get_brand_message_group_tag(body: dict[str, Any]) -> _r.BrandMessageGroupTagListResult:
    found = pick(validate(_r.BrandMessageGroupTagListResponse, body, "getBrandMessageGroupTag"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageGroupTagListResult) else _r.BrandMessageGroupTagListResult()


def _call_create_brand_message_group_tag(*, body: _q.BrandMessageGroupTagRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="createBrandMessageGroupTag",
        method="POST",
        path="/api/comm/v1/center/brandmessage/groupTag",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.BrandMessageGroupTagRequest, body),
    )


def _parse_create_brand_message_group_tag(body: dict[str, Any]) -> _r.BrandMessageGroupTagListResult:
    found = pick(validate(_r.BrandMessageGroupTagListResponse, body, "createBrandMessageGroupTag"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageGroupTagListResult) else _r.BrandMessageGroupTagListResult()


def _call_update_brand_message_group_tag(*, body: _q.BrandMessageGroupTagRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="updateBrandMessageGroupTag",
        method="PUT",
        path="/api/comm/v1/center/brandmessage/groupTag",
        retry=Retry.SAFE,
        json=json_body(_q.BrandMessageGroupTagRequest, body),
    )


def _parse_update_brand_message_group_tag(body: dict[str, Any]) -> _r.BrandMessageGroupTagListResult:
    found = pick(validate(_r.BrandMessageGroupTagListResponse, body, "updateBrandMessageGroupTag"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageGroupTagListResult) else _r.BrandMessageGroupTagListResult()


def _call_delete_brand_message_group_tag(*, sender_key: str, group_tag_key: str) -> Call:
    return Call(
        operation="deleteBrandMessageGroupTag",
        method="DELETE",
        path=f"/api/comm/v1/center/brandmessage/groupTag/senderKey/{segment(sender_key, 'senderKey')}/groupTagKey/{segment(group_tag_key, 'groupTagKey')}",
        retry=Retry.SAFE,
    )


def _call_upload_brand_message_friend_group_file(*, sender_key: str, file: FileInput, filename: str | None) -> Call:
    form = Form()
    need("senderKey", sender_key)
    form.text("senderKey", check_str("senderKey", sender_key, max_length=None, enum=()))
    need("file", file)
    form.file("file", file, filename, "file.bin", max_bytes=None)
    return Call(
        operation="uploadBrandMessageFriendGroupFile",
        method="POST",
        path="/api/comm/v1/center/brandmessage/friendGroup/file",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_brand_message_friend_group_file(body: dict[str, Any]) -> _r.BrandMessageFriendGroupFileUploadResult:
    found = pick(
        validate(_r.BrandMessageFriendGroupFileUploadResponse, body, "uploadBrandMessageFriendGroupFile"),
        ("data", "data"),
    )
    return (
        found
        if isinstance(found, _r.BrandMessageFriendGroupFileUploadResult)
        else _r.BrandMessageFriendGroupFileUploadResult()
    )


def _call_create_brand_message_friend_group(*, body: _q.BrandMessageFriendGroupRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="createBrandMessageFriendGroup",
        method="POST",
        path="/api/comm/v1/center/brandmessage/friendGroup",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.BrandMessageFriendGroupRequest, body),
    )


def _parse_create_brand_message_friend_group(body: dict[str, Any]) -> _r.BrandMessageFriendGroupProcessingResult:
    found = pick(
        validate(_r.BrandMessageFriendGroupProcessingResponse, body, "createBrandMessageFriendGroup"), ("data", "data")
    )
    return (
        found
        if isinstance(found, _r.BrandMessageFriendGroupProcessingResult)
        else _r.BrandMessageFriendGroupProcessingResult()
    )


def _call_get_brand_message_friend_group(*, sender_key: str, friend_group_key: str) -> Call:
    return Call(
        operation="getBrandMessageFriendGroup",
        method="GET",
        path="/api/comm/v1/center/brandmessage/friendGroup",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
                "friendGroupKey": need(
                    "friendGroupKey", check_str("friendGroupKey", friend_group_key, max_length=None, enum=())
                ),
            }
        ),
    )


def _parse_get_brand_message_friend_group(body: dict[str, Any]) -> _r.BrandMessageFriendGroupResult:
    found = pick(validate(_r.BrandMessageFriendGroupResponse, body, "getBrandMessageFriendGroup"), ("data", "data"))
    return found if isinstance(found, _r.BrandMessageFriendGroupResult) else _r.BrandMessageFriendGroupResult()


def _call_list_brand_message_friend_groups(*, sender_key: str) -> Call:
    return Call(
        operation="listBrandMessageFriendGroups",
        method="GET",
        path="/api/comm/v1/center/brandmessage/friendGroup/list",
        retry=Retry.SAFE,
        params=query({"senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=()))}),
    )


def _parse_list_brand_message_friend_groups(body: dict[str, Any]) -> _r.BrandMessageFriendGroupListResult:
    found = pick(
        validate(_r.BrandMessageFriendGroupListResponse, body, "listBrandMessageFriendGroups"), ("data", "data")
    )
    return found if isinstance(found, _r.BrandMessageFriendGroupListResult) else _r.BrandMessageFriendGroupListResult()


def _call_delete_brand_message_friend_group(*, sender_key: str, friend_group_key: str) -> Call:
    return Call(
        operation="deleteBrandMessageFriendGroup",
        method="DELETE",
        path=f"/api/comm/v1/center/brandmessage/friendGroup/senderKey/{segment(sender_key, 'senderKey')}/friendGroupKey/{segment(friend_group_key, 'friendGroupKey')}",
        retry=Retry.SAFE,
    )


def _call_add_brand_message_friend_group_phone_numbers(
    *, body: _q.BrandMessageFriendGroupRequest | Mapping[str, Any]
) -> Call:
    return Call(
        operation="addBrandMessageFriendGroupPhoneNumbers",
        method="POST",
        path="/api/comm/v1/center/brandmessage/friendGroup/phoneNumber/update",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.BrandMessageFriendGroupRequest, body),
    )


def _parse_add_brand_message_friend_group_phone_numbers(
    body: dict[str, Any],
) -> _r.BrandMessageFriendGroupProcessingResult:
    found = pick(
        validate(_r.BrandMessageFriendGroupProcessingResponse, body, "addBrandMessageFriendGroupPhoneNumbers"),
        ("data", "data"),
    )
    return (
        found
        if isinstance(found, _r.BrandMessageFriendGroupProcessingResult)
        else _r.BrandMessageFriendGroupProcessingResult()
    )


def _call_delete_brand_message_friend_group_phone_numbers(
    *, body: _q.BrandMessageFriendGroupRequest | Mapping[str, Any]
) -> Call:
    return Call(
        operation="deleteBrandMessageFriendGroupPhoneNumbers",
        method="POST",
        path="/api/comm/v1/center/brandmessage/friendGroup/phoneNumber/delete",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.BrandMessageFriendGroupRequest, body),
    )


def _parse_delete_brand_message_friend_group_phone_numbers(
    body: dict[str, Any],
) -> _r.BrandMessageFriendGroupProcessingResult:
    found = pick(
        validate(_r.BrandMessageFriendGroupProcessingResponse, body, "deleteBrandMessageFriendGroupPhoneNumbers"),
        ("data", "data"),
    )
    return (
        found
        if isinstance(found, _r.BrandMessageFriendGroupProcessingResult)
        else _r.BrandMessageFriendGroupProcessingResult()
    )


def _call_list_brand_message_friend_group_phone_number_requests(
    *, sender_key: str, friend_group_key: str, last_request_id: str | None, count: int | None
) -> Call:
    return Call(
        operation="listBrandMessageFriendGroupPhoneNumberRequests",
        method="GET",
        path="/api/comm/v1/center/brandmessage/friendGroup/phoneNumber/requests",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
                "friendGroupKey": need(
                    "friendGroupKey", check_str("friendGroupKey", friend_group_key, max_length=None, enum=())
                ),
                "lastRequestId": check_str("lastRequestId", last_request_id, max_length=None, enum=()),
                "count": check_int("count", count, 1, None),
            }
        ),
    )


def _parse_list_brand_message_friend_group_phone_number_requests(
    body: dict[str, Any],
) -> _r.BrandMessageFriendGroupPhoneNumberRequestListResult:
    found = pick(
        validate(
            _r.BrandMessageFriendGroupPhoneNumberRequestListResponse,
            body,
            "listBrandMessageFriendGroupPhoneNumberRequests",
        ),
        ("data", "data"),
    )
    return (
        found
        if isinstance(found, _r.BrandMessageFriendGroupPhoneNumberRequestListResult)
        else _r.BrandMessageFriendGroupPhoneNumberRequestListResult()
    )


_PAGE_LIST_BRAND_MESSAGE_FRIEND_GROUP_PHONE_NUMBER_REQUESTS = Pagination(
    style="cursor",
    request="lastRequestId",
    items=("data", "data", "friendGroups"),
    cursor=("data", "data", "friendGroups", -1, "requestId"),
    has_next=("data", "data", "hasNext"),
)


def _call_get_brand_message_friend_group_phone_number_request(
    *, sender_key: str, friend_group_key: str, request_id: str
) -> Call:
    return Call(
        operation="getBrandMessageFriendGroupPhoneNumberRequest",
        method="GET",
        path="/api/comm/v1/center/brandmessage/friendGroup/phoneNumber/request",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
                "friendGroupKey": need(
                    "friendGroupKey", check_str("friendGroupKey", friend_group_key, max_length=None, enum=())
                ),
                "requestId": need("requestId", check_str("requestId", request_id, max_length=None, enum=())),
            }
        ),
    )


def _parse_get_brand_message_friend_group_phone_number_request(
    body: dict[str, Any],
) -> _r.BrandMessageFriendGroupPhoneNumberRequestResult:
    found = pick(
        validate(
            _r.BrandMessageFriendGroupPhoneNumberRequestResponse, body, "getBrandMessageFriendGroupPhoneNumberRequest"
        ),
        ("data", "data"),
    )
    return (
        found
        if isinstance(found, _r.BrandMessageFriendGroupPhoneNumberRequestResult)
        else _r.BrandMessageFriendGroupPhoneNumberRequestResult()
    )


def _call_upload_brand_message_marketing_agree_evidence(
    *, sender_key: str, file: FileInput, filename: str | None
) -> Call:
    form = Form()
    need("senderKey", sender_key)
    form.text("senderKey", check_str("senderKey", sender_key, max_length=40, enum=()))
    need("file", file)
    form.file("file", file, filename, "image.jpg", max_bytes=None)
    return Call(
        operation="uploadBrandMessageMarketingAgreeEvidence",
        method="POST",
        path="/api/comm/v1/center/brandmessage/marketingAgree",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_brand_message_marketing_agree_evidence(body: dict[str, Any]) -> _r.BrandMessageMarketingAgreeResult:
    found = pick(
        validate(_r.BrandMessageMarketingAgreeResponse, body, "uploadBrandMessageMarketingAgreeEvidence"),
        ("data", "data"),
    )
    return found if isinstance(found, _r.BrandMessageMarketingAgreeResult) else _r.BrandMessageMarketingAgreeResult()


def _call_register_brand_message_unsubscribe_content(
    *, body: _q.BrandMessageUnsubscribeContentRequest | Mapping[str, Any]
) -> Call:
    return Call(
        operation="registerBrandMessageUnsubscribeContent",
        method="POST",
        path="/api/comm/v1/center/brandmessage/unSubscribeContent",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.BrandMessageUnsubscribeContentRequest, body),
    )


def _call_get_rcs_brand(*, brand_id: str) -> Call:
    return Call(
        operation="getRcsBrand",
        method="GET",
        path="/api/comm/v1/center/rcs/brand",
        retry=Retry.SAFE,
        params=query({"brandId": need("brandId", check_str("brandId", brand_id, max_length=None, enum=()))}),
    )


def _parse_get_rcs_brand(body: dict[str, Any]) -> _r.RcsBrandResult:
    found = pick(validate(_r.RcsBrandResponse, body, "getRcsBrand"), ("data", "data"))
    return found if isinstance(found, _r.RcsBrandResult) else _r.RcsBrandResult()


def _call_update_rcs_brand(
    *,
    brand_id: str,
    reg_brand: _q.RcsBrand | Mapping[str, Any],
    brand_profile: FileInput | None,
    brand_profile_filename: str | None,
    brand_background: FileInput | None,
    brand_background_filename: str | None,
    season_doc_file: FileInput | None,
    season_doc_file_filename: str | None,
) -> Call:
    form = Form()
    need("brandId", brand_id)
    form.text("brandId", check_str("brandId", brand_id, max_length=None, enum=()))
    need("regBrand", reg_brand)
    form.json("regBrand", _q.RcsBrand, reg_brand)
    form.file("brandProfile", brand_profile, brand_profile_filename, "file.bin", max_bytes=None)
    form.file("brandBackground", brand_background, brand_background_filename, "file.bin", max_bytes=None)
    form.file("seasonDocFile", season_doc_file, season_doc_file_filename, "file.bin", max_bytes=None)
    return Call(
        operation="updateRcsBrand",
        method="PUT",
        path="/api/comm/v1/center/rcs/brand",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_update_rcs_brand(body: dict[str, Any]) -> _r.RcsBrandResult:
    found = pick(validate(_r.RcsBrandResponse, body, "updateRcsBrand"), ("data", "data"))
    return found if isinstance(found, _r.RcsBrandResult) else _r.RcsBrandResult()


def _call_list_rcs_chatbots(*, brand_id: str, offset: int | None, limit: int | None) -> Call:
    return Call(
        operation="listRcsChatbots",
        method="GET",
        path="/api/comm/v1/center/rcs/chatbot/list",
        retry=Retry.SAFE,
        params=query(
            {
                "brandId": need("brandId", check_str("brandId", brand_id, max_length=None, enum=())),
                "offset": check_int("offset", offset, None, None),
                "limit": check_int("limit", limit, None, None),
            }
        ),
    )


def _parse_list_rcs_chatbots(body: dict[str, Any]) -> _r.RcsChatbotResult:
    found = pick(validate(_r.RcsChatbotResponse, body, "listRcsChatbots"), ("data", "data"))
    return found if isinstance(found, _r.RcsChatbotResult) else _r.RcsChatbotResult()


_PAGE_LIST_RCS_CHATBOTS = Pagination(
    style="offset", request="offset", items=("data", "data", "rcs", "chatbot"), size="limit"
)


def _call_get_rcs_chatbot(*, brand_id: str, chatbot_id: str) -> Call:
    return Call(
        operation="getRcsChatbot",
        method="GET",
        path="/api/comm/v1/center/rcs/chatbot",
        retry=Retry.SAFE,
        params=query(
            {
                "brandId": need("brandId", check_str("brandId", brand_id, max_length=None, enum=())),
                "chatbotId": need("chatbotId", check_str("chatbotId", chatbot_id, max_length=None, enum=())),
            }
        ),
    )


def _parse_get_rcs_chatbot(body: dict[str, Any]) -> _r.RcsChatbotResult:
    found = pick(validate(_r.RcsChatbotResponse, body, "getRcsChatbot"), ("data", "data"))
    return found if isinstance(found, _r.RcsChatbotResult) else _r.RcsChatbotResult()


def _call_update_rcs_chatbot(
    *,
    brand_id: str,
    chatbot: _q.RcsChatbot | Mapping[str, Any],
    sub_num_certificate: FileInput,
    sub_num_certificate_filename: str | None,
) -> Call:
    form = Form()
    need("brandId", brand_id)
    form.text("brandId", check_str("brandId", brand_id, max_length=None, enum=()))
    need("chatbot", chatbot)
    form.json("chatbot", _q.RcsChatbot, chatbot)
    need("subNumCertificate", sub_num_certificate)
    form.file("subNumCertificate", sub_num_certificate, sub_num_certificate_filename, "file.bin", max_bytes=None)
    return Call(
        operation="updateRcsChatbot",
        method="PUT",
        path="/api/comm/v1/center/rcs/chatbot",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_update_rcs_chatbot(body: dict[str, Any]) -> _r.RcsChatbotResult:
    found = pick(validate(_r.RcsChatbotResponse, body, "updateRcsChatbot"), ("data", "data"))
    return found if isinstance(found, _r.RcsChatbotResult) else _r.RcsChatbotResult()


def _call_cancel_rcs_chatbot_approval(*, brand_id: str, chatbot_id: str) -> Call:
    return Call(
        operation="cancelRcsChatbotApproval",
        method="PUT",
        path=f"/api/comm/v1/center/rcs/brandId/{segment(brand_id, 'brandId')}/chatbotId/{segment(chatbot_id, 'chatbotId')}/cancel",
        retry=Retry.SAFE,
    )


def _parse_cancel_rcs_chatbot_approval(body: dict[str, Any]) -> _r.RcsChatbotResult:
    found = pick(validate(_r.RcsChatbotResponse, body, "cancelRcsChatbotApproval"), ("data", "data"))
    return found if isinstance(found, _r.RcsChatbotResult) else _r.RcsChatbotResult()


def _call_delete_rcs_chatbot(*, brand_id: str, chatbot_id: str) -> Call:
    return Call(
        operation="deleteRcsChatbot",
        method="DELETE",
        path=f"/api/comm/v1/center/rcs/brandId/{segment(brand_id, 'brandId')}/chatbotId/{segment(chatbot_id, 'chatbotId')}",
        retry=Retry.SAFE,
    )


def _parse_delete_rcs_chatbot(body: dict[str, Any]) -> _r.RcsChatbotResult:
    found = pick(validate(_r.RcsChatbotResponse, body, "deleteRcsChatbot"), ("data", "data"))
    return found if isinstance(found, _r.RcsChatbotResult) else _r.RcsChatbotResult()


def _call_get_rcs_chatbot_usable_queries(*, chatbot_id: str) -> Call:
    return Call(
        operation="getRcsChatbotUsableQueries",
        method="GET",
        path=f"/api/comm/v1/center/rcs/usableQuery/chatbotId/{segment(chatbot_id, 'chatbotId')}",
        retry=Retry.SAFE,
    )


def _parse_get_rcs_chatbot_usable_queries(body: dict[str, Any]) -> _r.RcsChatbotResult:
    found = pick(validate(_r.RcsChatbotResponse, body, "getRcsChatbotUsableQueries"), ("data", "data"))
    return found if isinstance(found, _r.RcsChatbotResult) else _r.RcsChatbotResult()


def _call_list_rcs_common_formats() -> Call:
    return Call(
        operation="listRcsCommonFormats",
        method="GET",
        path="/api/comm/v1/center/rcs/messagebase/common/list",
        retry=Retry.SAFE,
    )


def _parse_list_rcs_common_formats(body: dict[str, Any]) -> _r.RcsMessagebaseCommonListResult:
    found = pick(validate(_r.RcsMessagebaseCommonListResponse, body, "listRcsCommonFormats"), ("data", "data"))
    return found if isinstance(found, _r.RcsMessagebaseCommonListResult) else _r.RcsMessagebaseCommonListResult()


def _call_get_rcs_common_format(*, messagebase_id: str) -> Call:
    return Call(
        operation="getRcsCommonFormat",
        method="GET",
        path="/api/comm/v1/center/rcs/messagebase/common",
        retry=Retry.SAFE,
        params=query(
            {
                "messagebaseId": need(
                    "messagebaseId", check_str("messagebaseId", messagebase_id, max_length=None, enum=())
                )
            }
        ),
    )


def _parse_get_rcs_common_format(body: dict[str, Any]) -> _r.RcsMessagebaseFormDetailResult:
    found = pick(validate(_r.RcsMessagebaseFormDetailResponse, body, "getRcsCommonFormat"), ("data", "data"))
    return found if isinstance(found, _r.RcsMessagebaseFormDetailResult) else _r.RcsMessagebaseFormDetailResult()


def _call_list_rcs_template_forms(*, offset: int | None, limit: int | None) -> Call:
    return Call(
        operation="listRcsTemplateForms",
        method="GET",
        path="/api/comm/v1/center/rcs/messagebase/messagebaseform/list",
        retry=Retry.SAFE,
        params=query(
            {"offset": check_int("offset", offset, None, None), "limit": check_int("limit", limit, 100, 1000)}
        ),
    )


def _parse_list_rcs_template_forms(body: dict[str, Any]) -> _r.RcsMessagebaseFormListResult:
    found = pick(validate(_r.RcsMessagebaseFormListResponse, body, "listRcsTemplateForms"), ("data", "data"))
    return found if isinstance(found, _r.RcsMessagebaseFormListResult) else _r.RcsMessagebaseFormListResult()


_PAGE_LIST_RCS_TEMPLATE_FORMS = Pagination(
    style="offset",
    request="offset",
    items=("data", "data", "rcs", "messageForms"),
    size="limit",
    total=("data", "data", "rcs", "pagination", "total"),
)


def _call_get_rcs_template_form(*, messagebaseform_id: str) -> Call:
    return Call(
        operation="getRcsTemplateForm",
        method="GET",
        path="/api/comm/v1/center/rcs/messagebase/messagebaseform",
        retry=Retry.SAFE,
        params=query(
            {
                "messagebaseformId": need(
                    "messagebaseformId", check_str("messagebaseformId", messagebaseform_id, max_length=None, enum=())
                )
            }
        ),
    )


def _parse_get_rcs_template_form(body: dict[str, Any]) -> _r.RcsMessagebaseFormDetailResult:
    found = pick(validate(_r.RcsMessagebaseFormDetailResponse, body, "getRcsTemplateForm"), ("data", "data"))
    return found if isinstance(found, _r.RcsMessagebaseFormDetailResult) else _r.RcsMessagebaseFormDetailResult()


def _call_list_rcs_templates() -> Call:
    return Call(
        operation="listRcsTemplates", method="GET", path="/api/comm/v1/center/rcs/messagebase/list", retry=Retry.SAFE
    )


def _parse_list_rcs_templates(body: dict[str, Any]) -> _r.RcsTemplateListResult:
    found = pick(validate(_r.RcsTemplateListResponse, body, "listRcsTemplates"), ("data", "data"))
    return found if isinstance(found, _r.RcsTemplateListResult) else _r.RcsTemplateListResult()


def _call_get_rcs_template(*, messagebase_id: str) -> Call:
    return Call(
        operation="getRcsTemplate",
        method="GET",
        path="/api/comm/v1/center/rcs/messagebase",
        retry=Retry.SAFE,
        params=query(
            {
                "messagebaseId": need(
                    "messagebaseId", check_str("messagebaseId", messagebase_id, max_length=None, enum=())
                )
            }
        ),
    )


def _parse_get_rcs_template(body: dict[str, Any]) -> _r.RcsTemplateResult:
    found = pick(validate(_r.RcsTemplateResponse, body, "getRcsTemplate"), ("data", "data"))
    return found if isinstance(found, _r.RcsTemplateResult) else _r.RcsTemplateResult()


def _call_create_rcs_template(*, body: _q.RcsTemplateRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="createRcsTemplate",
        method="POST",
        path="/api/comm/v1/center/rcs/messagebase",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.RcsTemplateRequest, body),
    )


def _parse_create_rcs_template(body: dict[str, Any]) -> _r.RcsTemplateIdResult:
    found = pick(validate(_r.RcsTemplateIdResponse, body, "createRcsTemplate"), ("data", "data"))
    return found if isinstance(found, _r.RcsTemplateIdResult) else _r.RcsTemplateIdResult()


def _call_update_rcs_template(*, body: _q.RcsTemplateRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="updateRcsTemplate",
        method="PUT",
        path="/api/comm/v1/center/rcs/messagebase",
        retry=Retry.SAFE,
        json=json_body(_q.RcsTemplateRequest, body),
    )


def _parse_update_rcs_template(body: dict[str, Any]) -> _r.RcsTemplateIdResult:
    found = pick(validate(_r.RcsTemplateIdResponse, body, "updateRcsTemplate"), ("data", "data"))
    return found if isinstance(found, _r.RcsTemplateIdResult) else _r.RcsTemplateIdResult()


def _call_cancel_rcs_template_approval(*, brand_id: str, messagebase_id: str) -> Call:
    return Call(
        operation="cancelRcsTemplateApproval",
        method="PUT",
        path=f"/api/comm/v1/center/rcs/brandId/{segment(brand_id, 'brandId')}/messagebaseId/{segment(messagebase_id, 'messagebaseId')}/cancel",
        retry=Retry.SAFE,
    )


def _parse_cancel_rcs_template_approval(body: dict[str, Any]) -> _r.RcsTemplateIdResult:
    found = pick(validate(_r.RcsTemplateIdResponse, body, "cancelRcsTemplateApproval"), ("data", "data"))
    return found if isinstance(found, _r.RcsTemplateIdResult) else _r.RcsTemplateIdResult()


def _call_delete_rcs_template(*, brand_id: str, messagebase_id: str) -> Call:
    return Call(
        operation="deleteRcsTemplate",
        method="DELETE",
        path=f"/api/comm/v1/center/rcs/brandId/{segment(brand_id, 'brandId')}/messagebaseId/{segment(messagebase_id, 'messagebaseId')}",
        retry=Retry.SAFE,
    )


def _parse_delete_rcs_template(body: dict[str, Any]) -> _r.RcsTemplateIdResult:
    found = pick(validate(_r.RcsTemplateIdResponse, body, "deleteRcsTemplate"), ("data", "data"))
    return found if isinstance(found, _r.RcsTemplateIdResult) else _r.RcsTemplateIdResult()


def _call_get_rcs_template_image(*, brand_id: str, file_id: str) -> Call:
    return Call(
        operation="getRcsTemplateImage",
        method="GET",
        path="/api/comm/v1/center/rcs/messagebase/file",
        retry=Retry.SAFE,
        params=query(
            {
                "brandId": need("brandId", check_str("brandId", brand_id, max_length=None, enum=())),
                "fileId": need("fileId", check_str("fileId", file_id, max_length=None, enum=())),
            }
        ),
    )


def _parse_get_rcs_template_image(body: dict[str, Any]) -> _r.RcsTemplateImageResult:
    found = pick(validate(_r.RcsTemplateImageResponse, body, "getRcsTemplateImage"), ("data", "data"))
    return found if isinstance(found, _r.RcsTemplateImageResult) else _r.RcsTemplateImageResult()


def _call_upload_rcs_template_image(*, brand_id: str, file: FileInput, filename: str | None) -> Call:
    form = Form()
    need("brandId", brand_id)
    form.text("brandId", check_str("brandId", brand_id, max_length=None, enum=()))
    need("file", file)
    form.file("file", file, filename, "image.jpg", max_bytes=None)
    return Call(
        operation="uploadRcsTemplateImage",
        method="POST",
        path="/api/comm/v1/center/rcs/messagebase/file",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_rcs_template_image(body: dict[str, Any]) -> _r.RcsTemplateImageResult:
    found = pick(validate(_r.RcsTemplateImageResponse, body, "uploadRcsTemplateImage"), ("data", "data"))
    return found if isinstance(found, _r.RcsTemplateImageResult) else _r.RcsTemplateImageResult()


def _call_list_rcs_template_form_logos(*, messagebaseform_id: str) -> Call:
    return Call(
        operation="listRcsTemplateFormLogos",
        method="GET",
        path="/api/comm/v1/center/rcs/messagebase/messagebaseform/logo",
        retry=Retry.SAFE,
        params=query(
            {
                "messagebaseformId": need(
                    "messagebaseformId", check_str("messagebaseformId", messagebaseform_id, max_length=None, enum=())
                )
            }
        ),
    )


def _parse_list_rcs_template_form_logos(body: dict[str, Any]) -> _r.RcsTemplateFormLogoListResult:
    found = pick(validate(_r.RcsTemplateFormLogoListResponse, body, "listRcsTemplateFormLogos"), ("data", "data"))
    return found if isinstance(found, _r.RcsTemplateFormLogoListResult) else _r.RcsTemplateFormLogoListResult()


def _call_send_counsel_plain(*, body: _q.CounselPlainMessageRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="sendCounselPlain",
        method="POST",
        path="/api/comm/v1/cstalk/plain",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselPlainMessageRequest, body),
    )


def _parse_send_counsel_plain(body: dict[str, Any]) -> _r.CounselSendServiceResult:
    found = pick(validate(_r.CounselSendResponse, body, "sendCounselPlain"), ("data",))
    return found if isinstance(found, _r.CounselSendServiceResult) else _r.CounselSendServiceResult()


def _call_send_counsel_rich(*, body: _q.CounselRichMessageRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="sendCounselRich",
        method="POST",
        path="/api/comm/v1/cstalk/rich",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselRichMessageRequest, body),
    )


def _parse_send_counsel_rich(body: dict[str, Any]) -> _r.CounselSendServiceResult:
    found = pick(validate(_r.CounselSendResponse, body, "sendCounselRich"), ("data",))
    return found if isinstance(found, _r.CounselSendServiceResult) else _r.CounselSendServiceResult()


def _call_end_counsel_session(*, body: _q.CounselEndRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="endCounselSession",
        method="POST",
        path="/api/comm/v1/cstalk/end",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselEndRequest, body),
    )


def _parse_end_counsel_session(body: dict[str, Any]) -> _r.CounselEndResult:
    found = pick(validate(_r.CounselEndResponse, body, "endCounselSession"), ("data", "data"))
    return found if isinstance(found, _r.CounselEndResult) else _r.CounselEndResult()


def _call_end_counsel_session_with_bot(*, body: _q.CounselEndWithBotRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="endCounselSessionWithBot",
        method="POST",
        path="/api/comm/v1/cstalk/endWithBot",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselEndWithBotRequest, body),
    )


def _parse_end_counsel_session_with_bot(body: dict[str, Any]) -> _r.CounselEndResult:
    found = pick(validate(_r.CounselEndResponse, body, "endCounselSessionWithBot"), ("data", "data"))
    return found if isinstance(found, _r.CounselEndResult) else _r.CounselEndResult()


def _call_block_counsel_user(*, body: _q.CounselUserBlockRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="blockCounselUser",
        method="POST",
        path="/api/comm/v1/center/cstalk/profile/user/block",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselUserBlockRequest, body),
    )


def _call_unblock_counsel_user(*, body: _q.CounselUserBlockRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="unblockCounselUser",
        method="POST",
        path="/api/comm/v1/center/cstalk/profile/user/unblock",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselUserBlockRequest, body),
    )


def _call_get_counsel_session(*, user_key: str) -> Call:
    return Call(
        operation="getCounselSession",
        method="GET",
        path="/api/comm/v1/center/cstalk/session",
        retry=Retry.SAFE,
        params=query({"userKey": need("userKey", check_str("userKey", user_key, max_length=20, enum=()))}),
    )


def _parse_get_counsel_session(body: dict[str, Any]) -> _r.CounselSessionResult:
    found = pick(validate(_r.CounselSessionResponse, body, "getCounselSession"), ("data", "data"))
    return found if isinstance(found, _r.CounselSessionResult) else _r.CounselSessionResult()


def _call_get_counsel_cert_status(*, cert_tx_id: str) -> Call:
    return Call(
        operation="getCounselCertStatus",
        method="GET",
        path="/api/comm/v1/center/cstalk/cert/status",
        retry=Retry.SAFE,
        params=query({"certTxId": need("certTxId", check_str("certTxId", cert_tx_id, max_length=None, enum=()))}),
    )


def _parse_get_counsel_cert_status(body: dict[str, Any]) -> _r.CounselCertStatusResult:
    found = pick(validate(_r.CounselCertStatusResponse, body, "getCounselCertStatus"), ("data", "data"))
    return found if isinstance(found, _r.CounselCertStatusResult) else _r.CounselCertStatusResult()


def _call_upload_counsel_image(
    *,
    file: FileInput,
    filename: str | None,
    file_key: str | None,
    image_name: str | None,
    sender_key: str,
    image_type: str | None,
) -> Call:
    form = Form()
    need("file", file)
    form.file("file", file, filename, "image.jpg", max_bytes=None)
    form.text("fileKey", check_str("fileKey", file_key, max_length=None, enum=()))
    form.text("imageName", check_str("imageName", image_name, max_length=None, enum=()))
    need("senderKey", sender_key)
    form.text("senderKey", check_str("senderKey", sender_key, max_length=None, enum=()))
    form.text("imageType", check_str("imageType", image_type, max_length=None, enum=()))
    return Call(
        operation="uploadCounselImage",
        method="POST",
        path="/api/comm/v1/file/cstalk/image",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_counsel_image(body: dict[str, Any]) -> _r.CounselImageUploadResult:
    found = pick(validate(_r.CounselImageUploadResponse, body, "uploadCounselImage"), ("data", "data"))
    return found if isinstance(found, _r.CounselImageUploadResult) else _r.CounselImageUploadResult()


def _call_upload_counsel_file(
    *,
    file: FileInput,
    filename: str | None,
    file_key: str | None,
    image_name: str | None,
    sender_key: str,
    file_type: Literal["file", "audio", "video"] | None,
) -> Call:
    form = Form()
    need("file", file)
    form.file("file", file, filename, "file.bin", max_bytes=None)
    form.text("fileKey", check_str("fileKey", file_key, max_length=None, enum=()))
    form.text("imageName", check_str("imageName", image_name, max_length=None, enum=()))
    need("senderKey", sender_key)
    form.text("senderKey", check_str("senderKey", sender_key, max_length=None, enum=()))
    form.text("fileType", check_str("fileType", file_type, max_length=None, enum=("file", "audio", "video")))
    return Call(
        operation="uploadCounselFile",
        method="POST",
        path="/api/comm/v1/file/cstalk",
        retry=Retry.RATE_LIMIT_ONLY,
        **form.call_kwargs(),
    )


def _parse_upload_counsel_file(body: dict[str, Any]) -> _r.CounselFileUploadResult:
    found = pick(validate(_r.CounselFileUploadResponse, body, "uploadCounselFile"), ("data", "data"))
    return found if isinstance(found, _r.CounselFileUploadResult) else _r.CounselFileUploadResult()


def _call_activate_counsel(*, body: _q.CounselSenderActivationRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="activateCounsel",
        method="POST",
        path="/api/comm/v1/center/cstalk/sender/activate",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselSenderActivationRequest, body),
    )


def _call_deactivate_counsel(*, body: _q.CounselSenderActivationRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="deactivateCounsel",
        method="POST",
        path="/api/comm/v1/center/cstalk/sender/deactivate",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselSenderActivationRequest, body),
    )


def _call_activate_counsel_chat(*, body: _q.CounselSenderRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="activateCounselChat",
        method="POST",
        path="/api/comm/v1/center/cstalk/sender/chat/activate",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselSenderRequest, body),
    )


def _call_deactivate_counsel_chat(*, body: _q.CounselSenderRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="deactivateCounselChat",
        method="POST",
        path="/api/comm/v1/center/cstalk/sender/chat/deactivate",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselSenderRequest, body),
    )


def _call_get_counsel_consult_time(*, sender_key: str) -> Call:
    return Call(
        operation="getCounselConsultTime",
        method="GET",
        path="/api/comm/v1/center/cstalk/consult/time",
        retry=Retry.SAFE,
        params=query({"senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=()))}),
    )


def _parse_get_counsel_consult_time(body: dict[str, Any]) -> _r.CounselConsultTimeResult:
    found = pick(validate(_r.CounselConsultTimeResponse, body, "getCounselConsultTime"), ("data", "data"))
    return found if isinstance(found, _r.CounselConsultTimeResult) else _r.CounselConsultTimeResult()


def _call_save_counsel_consult_time(*, body: _q.CounselConsultTimeSaveRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="saveCounselConsultTime",
        method="POST",
        path="/api/comm/v1/center/cstalk/consult/time",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselConsultTimeSaveRequest, body),
    )


def _call_list_counsel_system_messages(*, sender_key: str, id: str | None) -> Call:
    return Call(
        operation="listCounselSystemMessages",
        method="GET",
        path="/api/comm/v1/center/cstalk/system/message",
        retry=Retry.SAFE,
        params=query(
            {
                "senderKey": need("senderKey", check_str("senderKey", sender_key, max_length=None, enum=())),
                "id": check_str("id", id, max_length=None, enum=()),
            }
        ),
    )


def _parse_list_counsel_system_messages(body: dict[str, Any]) -> _r.CounselSystemMessageListResult:
    found = pick(validate(_r.CounselSystemMessageListResponse, body, "listCounselSystemMessages"), ("data", "data"))
    return found if isinstance(found, _r.CounselSystemMessageListResult) else _r.CounselSystemMessageListResult()


def _call_create_counsel_system_message(*, body: _q.CounselSystemMessageCreateRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="createCounselSystemMessage",
        method="POST",
        path="/api/comm/v1/center/cstalk/system/message",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselSystemMessageCreateRequest, body),
    )


def _parse_create_counsel_system_message(body: dict[str, Any]) -> _r.CounselSystemMessageCreateResult:
    found = pick(validate(_r.CounselSystemMessageCreateResponse, body, "createCounselSystemMessage"), ("data", "data"))
    return found if isinstance(found, _r.CounselSystemMessageCreateResult) else _r.CounselSystemMessageCreateResult()


def _call_delete_counsel_system_message(*, sender_key: str, id: str) -> Call:
    return Call(
        operation="deleteCounselSystemMessage",
        method="DELETE",
        path=f"/api/comm/v1/center/cstalk/system/message/senderKey/{segment(sender_key, 'senderKey')}/id/{segment(id, 'id')}",
        retry=Retry.SAFE,
    )


def _call_request_counsel_system_message_approval(*, body: _q.CounselSenderRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="requestCounselSystemMessageApproval",
        method="POST",
        path="/api/comm/v1/center/cstalk/system/message/approval/request",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselSenderRequest, body),
    )


def _call_cancel_counsel_system_message_approval(*, body: _q.CounselSenderRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="cancelCounselSystemMessageApproval",
        method="POST",
        path="/api/comm/v1/center/cstalk/system/message/approval/cancel",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselSenderRequest, body),
    )


def _call_delete_counsel_message(*, body: _q.CounselMessageDeleteRequest | Mapping[str, Any]) -> Call:
    return Call(
        operation="deleteCounselMessage",
        method="POST",
        path="/api/comm/v1/center/cstalk/chat/delete",
        retry=Retry.RATE_LIMIT_ONLY,
        json=json_body(_q.CounselMessageDeleteRequest, body),
    )


class SendBase:
    """``client.send``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport


class AsyncSendBase:
    """``client.send`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport


class FilesBase:
    """``client.files``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def upload_brand_message_default(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 이미지 업로드.

        기본형 브랜드메시지에서 사용하는 이미지를 업로드합니다. 발송 본문에 파일을 직접 첨부하는 API가 아니라 브랜드메시지 템플릿 등록과 구성에 사용할 이미지 URL(`imgUrl`)을 발급받는 API입니다.

        ``POST /api/comm/v1/file/brandmessage/default`` (``uploadBrandMessageDefaultImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 브랜드메시지 이미지 파일입니다. 권장 크기 800×400px, 가로 500px 이상, 비율(세로÷가로) 0.5, 형식 jpg·png, 최대 500KB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_default_image(
            self._transport.call(
                _call_upload_brand_message_default_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    def upload_brand_message_wide(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 와이드 이미지 업로드.

        와이드 이미지형 브랜드메시지에서 사용하는 이미지를 업로드합니다. 발급된 `imgUrl`은 브랜드메시지 템플릿 또는 발송 구성에 사용합니다.

        ``POST /api/comm/v1/file/brandmessage/wide`` (``uploadBrandMessageWideImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 브랜드메시지 이미지 파일입니다. 권장 크기 800×600px 또는 800×400px, 가로 500px 이상, 비율 0.5~1, 형식 jpg·png, 최대 5MB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_wide_image(
            self._transport.call(
                _call_upload_brand_message_wide_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    def upload_brand_message_wide_item_list_first(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 와이드 리스트 첫번째 이미지 업로드.

        와이드 리스트형 브랜드메시지의 첫 번째 리스트 이미지에 사용할 이미지를 업로드합니다.

        ``POST /api/comm/v1/file/brandmessage/wideItemList/first`` (``uploadBrandMessageWideItemListFirstImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 브랜드메시지 이미지 파일입니다. 가로 500px 이상, 비율(세로÷가로) 0.5, 형식 jpg·png, 최대 5MB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_wide_item_list_first_image(
            self._transport.call(
                _call_upload_brand_message_wide_item_list_first_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    def upload_brand_message_wide_item_list(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 와이드 리스트 이미지 업로드.

        와이드 리스트형 브랜드메시지의 2~4번째 리스트 이미지에 사용할 이미지를 업로드합니다.

        ``POST /api/comm/v1/file/brandmessage/wideItemList`` (``uploadBrandMessageWideItemListImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 브랜드메시지 이미지 파일입니다. 가로 500px 이상, 비율(세로÷가로) 1, 형식 jpg·png, 최대 5MB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_wide_item_list_image(
            self._transport.call(
                _call_upload_brand_message_wide_item_list_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    def upload_brand_message_carousel_feed(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 캐러셀 피드 이미지 업로드.

        캐러셀 피드형 브랜드메시지에서 사용하는 이미지를 업로드합니다.

        ``POST /api/comm/v1/file/brandmessage/carouselFeed`` (``uploadBrandMessageCarouselFeedImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 브랜드메시지 이미지 파일입니다. 권장 크기 800×600px 또는 800×400px, 가로 500px 이상, 비율 0.5~1.333, 형식 jpg·png, 최대 5MB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_carousel_feed_image(
            self._transport.call(
                _call_upload_brand_message_carousel_feed_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    def upload_brand_message_carousel_commerce(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 캐러셀 커머스 이미지 업로드.

        캐러셀 커머스형 브랜드메시지에서 사용하는 이미지를 업로드합니다. 전체 캐러셀 이미지 비율은 동일하게 맞춰야 합니다.

        ``POST /api/comm/v1/file/brandmessage/carouselCommerce`` (``uploadBrandMessageCarouselCommerceImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 브랜드메시지 이미지 파일입니다. 권장 크기 800×600px 또는 800×400px, 가로 500px 이상, 비율 0.5~1.333, 형식 jpg·png, 최대 5MB입니다. 전체 캐러셀 이미지 비율은 동일해야 합니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_carousel_commerce_image(
            self._transport.call(
                _call_upload_brand_message_carousel_commerce_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    def upload_alimtalk_template_image(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.AlimtalkTemplateImageUploadResult:
        """알림톡 템플릿 이미지 업로드.

        알림톡 이미지형, 와이드 이미지형, 아이템리스트형 템플릿 등록에 사용할 이미지를 업로드합니다. 메시지 발송용 업로드가 아니라 템플릿 등록을 위한 사전 이미지 등록 API입니다. 응답의 `imgUrl`을 템플릿 등록의 `imgUrl`에 넣습니다.

        ``POST /api/comm/v1/file/alimtalk/template`` (``uploadAlimtalkTemplateImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 이미지 파일입니다. 권장 크기 800×400px, 가로 500px 이상, 비율(세로÷가로) 0.5, 형식 jpg·png, 최대 500KB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``AlimtalkTemplateImageUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_alimtalk_template_image(
            self._transport.call(
                _call_upload_alimtalk_template_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    def upload_alimtalk_item_highlight_image(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.AlimtalkTemplateImageUploadResult:
        """알림톡 템플릿 하이라이트 이미지 업로드.

        아이템리스트형 알림톡 템플릿의 아이템 하이라이트 영역에 사용할 이미지를 업로드합니다. 템플릿 이미지 업로드와 같은 템플릿 등록용 사전 이미지 등록 API입니다.

        ``POST /api/comm/v1/file/alimtalk/itemHighlight`` (``uploadAlimtalkItemHighlightImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 아이템 하이라이트 이미지 파일입니다. 108×108px 이상, 비율(세로÷가로) 1, 형식 jpg·png, 최대 500KB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``AlimtalkTemplateImageUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_alimtalk_item_highlight_image(
            self._transport.call(
                _call_upload_alimtalk_item_highlight_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    def upload_brand_message_catalog(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 카탈로그 이미지 업로드.

        카탈로그형(FG) 브랜드메시지에서 쓰는 1:1 비율 이미지를 업로드하고 템플릿에 쓸 `imgUrl`을 발급받습니다. 홀수형(아이템 3·5·7개)의 첫 번째 아이템은 카탈로그 홀수형 첫번째 이미지 업로드를 씁니다.

        ``POST /api/comm/v1/file/brandmessage/catalog`` (``uploadBrandMessageCatalogImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 카탈로그(FG) 아이템 이미지 파일입니다. 1:1 비율 이미지를 씁니다. 홀수형의 첫 번째 아이템(2:1)은 카탈로그 홀수형 첫번째 이미지 업로드를 씁니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_catalog_image(
            self._transport.call(
                _call_upload_brand_message_catalog_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    def upload_brand_message_catalog_odd_first(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 카탈로그 홀수형 첫번째 이미지 업로드.

        카탈로그형(FG) 홀수형의 첫 번째 아이템에 쓰는 2:1 비율 이미지를 업로드합니다. 나머지 아이템과 짝수형(4·6개)은 카탈로그 이미지 업로드를 씁니다.

        ``POST /api/comm/v1/file/brandmessage/catalog/oddFirst`` (``uploadBrandMessageCatalogOddFirstImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 카탈로그 홀수형(아이템 3·5·7개) 첫 번째 아이템 이미지 파일입니다. 2:1 가로형 비율 이미지를 씁니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_catalog_odd_first_image(
            self._transport.call(
                _call_upload_brand_message_catalog_odd_first_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )


class AsyncFilesBase:
    """``client.files`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def upload_brand_message_default(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 이미지 업로드.

        기본형 브랜드메시지에서 사용하는 이미지를 업로드합니다. 발송 본문에 파일을 직접 첨부하는 API가 아니라 브랜드메시지 템플릿 등록과 구성에 사용할 이미지 URL(`imgUrl`)을 발급받는 API입니다.

        ``POST /api/comm/v1/file/brandmessage/default`` (``uploadBrandMessageDefaultImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 브랜드메시지 이미지 파일입니다. 권장 크기 800×400px, 가로 500px 이상, 비율(세로÷가로) 0.5, 형식 jpg·png, 최대 500KB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_default_image(
            await self._transport.call(
                _call_upload_brand_message_default_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    async def upload_brand_message_wide(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 와이드 이미지 업로드.

        와이드 이미지형 브랜드메시지에서 사용하는 이미지를 업로드합니다. 발급된 `imgUrl`은 브랜드메시지 템플릿 또는 발송 구성에 사용합니다.

        ``POST /api/comm/v1/file/brandmessage/wide`` (``uploadBrandMessageWideImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 브랜드메시지 이미지 파일입니다. 권장 크기 800×600px 또는 800×400px, 가로 500px 이상, 비율 0.5~1, 형식 jpg·png, 최대 5MB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_wide_image(
            await self._transport.call(
                _call_upload_brand_message_wide_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    async def upload_brand_message_wide_item_list_first(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 와이드 리스트 첫번째 이미지 업로드.

        와이드 리스트형 브랜드메시지의 첫 번째 리스트 이미지에 사용할 이미지를 업로드합니다.

        ``POST /api/comm/v1/file/brandmessage/wideItemList/first`` (``uploadBrandMessageWideItemListFirstImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 브랜드메시지 이미지 파일입니다. 가로 500px 이상, 비율(세로÷가로) 0.5, 형식 jpg·png, 최대 5MB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_wide_item_list_first_image(
            await self._transport.call(
                _call_upload_brand_message_wide_item_list_first_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    async def upload_brand_message_wide_item_list(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 와이드 리스트 이미지 업로드.

        와이드 리스트형 브랜드메시지의 2~4번째 리스트 이미지에 사용할 이미지를 업로드합니다.

        ``POST /api/comm/v1/file/brandmessage/wideItemList`` (``uploadBrandMessageWideItemListImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 브랜드메시지 이미지 파일입니다. 가로 500px 이상, 비율(세로÷가로) 1, 형식 jpg·png, 최대 5MB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_wide_item_list_image(
            await self._transport.call(
                _call_upload_brand_message_wide_item_list_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    async def upload_brand_message_carousel_feed(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 캐러셀 피드 이미지 업로드.

        캐러셀 피드형 브랜드메시지에서 사용하는 이미지를 업로드합니다.

        ``POST /api/comm/v1/file/brandmessage/carouselFeed`` (``uploadBrandMessageCarouselFeedImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 브랜드메시지 이미지 파일입니다. 권장 크기 800×600px 또는 800×400px, 가로 500px 이상, 비율 0.5~1.333, 형식 jpg·png, 최대 5MB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_carousel_feed_image(
            await self._transport.call(
                _call_upload_brand_message_carousel_feed_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    async def upload_brand_message_carousel_commerce(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 캐러셀 커머스 이미지 업로드.

        캐러셀 커머스형 브랜드메시지에서 사용하는 이미지를 업로드합니다. 전체 캐러셀 이미지 비율은 동일하게 맞춰야 합니다.

        ``POST /api/comm/v1/file/brandmessage/carouselCommerce`` (``uploadBrandMessageCarouselCommerceImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 브랜드메시지 이미지 파일입니다. 권장 크기 800×600px 또는 800×400px, 가로 500px 이상, 비율 0.5~1.333, 형식 jpg·png, 최대 5MB입니다. 전체 캐러셀 이미지 비율은 동일해야 합니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_carousel_commerce_image(
            await self._transport.call(
                _call_upload_brand_message_carousel_commerce_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    async def upload_alimtalk_template_image(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.AlimtalkTemplateImageUploadResult:
        """알림톡 템플릿 이미지 업로드.

        알림톡 이미지형, 와이드 이미지형, 아이템리스트형 템플릿 등록에 사용할 이미지를 업로드합니다. 메시지 발송용 업로드가 아니라 템플릿 등록을 위한 사전 이미지 등록 API입니다. 응답의 `imgUrl`을 템플릿 등록의 `imgUrl`에 넣습니다.

        ``POST /api/comm/v1/file/alimtalk/template`` (``uploadAlimtalkTemplateImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 이미지 파일입니다. 권장 크기 800×400px, 가로 500px 이상, 비율(세로÷가로) 0.5, 형식 jpg·png, 최대 500KB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``AlimtalkTemplateImageUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_alimtalk_template_image(
            await self._transport.call(
                _call_upload_alimtalk_template_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    async def upload_alimtalk_item_highlight_image(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.AlimtalkTemplateImageUploadResult:
        """알림톡 템플릿 하이라이트 이미지 업로드.

        아이템리스트형 알림톡 템플릿의 아이템 하이라이트 영역에 사용할 이미지를 업로드합니다. 템플릿 이미지 업로드와 같은 템플릿 등록용 사전 이미지 등록 API입니다.

        ``POST /api/comm/v1/file/alimtalk/itemHighlight`` (``uploadAlimtalkItemHighlightImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 아이템 하이라이트 이미지 파일입니다. 108×108px 이상, 비율(세로÷가로) 1, 형식 jpg·png, 최대 500KB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``AlimtalkTemplateImageUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_alimtalk_item_highlight_image(
            await self._transport.call(
                _call_upload_alimtalk_item_highlight_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    async def upload_brand_message_catalog(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 카탈로그 이미지 업로드.

        카탈로그형(FG) 브랜드메시지에서 쓰는 1:1 비율 이미지를 업로드하고 템플릿에 쓸 `imgUrl`을 발급받습니다. 홀수형(아이템 3·5·7개)의 첫 번째 아이템은 카탈로그 홀수형 첫번째 이미지 업로드를 씁니다.

        ``POST /api/comm/v1/file/brandmessage/catalog`` (``uploadBrandMessageCatalogImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 카탈로그(FG) 아이템 이미지 파일입니다. 1:1 비율 이미지를 씁니다. 홀수형의 첫 번째 아이템(2:1)은 카탈로그 홀수형 첫번째 이미지 업로드를 씁니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_catalog_image(
            await self._transport.call(
                _call_upload_brand_message_catalog_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )

    async def upload_brand_message_catalog_odd_first(
        self,
        file: FileInput,
        *,
        file_key: str | None = None,
        image_name: str | None = None,
        filename: str | None = None,
    ) -> _r.BrandMessageFileUploadResult:
        """브랜드메시지 카탈로그 홀수형 첫번째 이미지 업로드.

        카탈로그형(FG) 홀수형의 첫 번째 아이템에 쓰는 2:1 비율 이미지를 업로드합니다. 나머지 아이템과 짝수형(4·6개)은 카탈로그 이미지 업로드를 씁니다.

        ``POST /api/comm/v1/file/brandmessage/catalog/oddFirst`` (``uploadBrandMessageCatalogOddFirstImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 카탈로그 홀수형(아이템 3·5·7개) 첫 번째 아이템 이미지 파일입니다. 2:1 가로형 비율 이미지를 씁니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.

        Returns:
            ``BrandMessageFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_catalog_odd_first_image(
            await self._transport.call(
                _call_upload_brand_message_catalog_odd_first_image(
                    file=file, file_key=file_key, image_name=image_name, filename=filename
                )
            )
        )


class ReportsBase:
    """``client.reports``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport


class AsyncReportsBase:
    """``client.reports`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport


class MessagesBase:
    """``client.messages``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport


class AsyncMessagesBase:
    """``client.messages`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport


class ReservationsRecipients:
    """``client.reservations.recipients``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(
        self, resv_key: str, body: _q.ReservationRecipientCreateRequest | Mapping[str, Any]
    ) -> _r.SendOmniResult:
        """예약 수신자 추가.

        기존 예약 건에 수신자를 추가합니다. 한 번에 최대 1,000건까지 추가할 수 있습니다. 수신자별 `code`를 함께 확인합니다.

        ``POST /api/comm/v1/reservation/resvKey/{resvKey}/destinations`` (``addReservationRecipients``). 429만 재시도, 속도 제한 버킷: ``send``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.
            body: :class:`~bizgo.models.ReservationRecipientCreateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``SendOmniResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_add_reservation_recipients(
            self._transport.call(_call_add_reservation_recipients(resv_key=resv_key, body=body))
        )

    def list(
        self, resv_key: str, *, last_seq: int | None = None, limit: int | None = None
    ) -> _r.ReservationRecipientListResult:
        """예약 수신자 목록 조회.

        예약 건에 등록된 수신자 목록을 조회합니다.

        ``GET /api/comm/v1/reservation/resvKey/{resvKey}/destinations`` (``listReservationRecipients``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.
            last_seq: 다음 페이지를 조회할 때 쓰는 마지막 순번입니다. 이전 응답의 `data.data.lastSeq`를 넣습니다.
            limit: 조회 건수입니다.

        Returns:
            ``ReservationRecipientListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_reservation_recipients(
            self._transport.call(_call_list_reservation_recipients(resv_key=resv_key, last_seq=last_seq, limit=limit))
        )

    def iter_list(self, resv_key: str, *, limit: int | None = None) -> Iterator[_r.ReservationRecipient]:
        """Iterate over every page of :meth:`list` (``listReservationRecipients``, cursor pagination)."""

        def fetch(position: Any) -> Any:
            body = self._transport.call(
                _call_list_reservation_recipients(resv_key=resv_key, limit=limit, last_seq=position)
            )
            return validate(_r.ReservationRecipientListResponse, body, "listReservationRecipients")

        return iterate(fetch, _PAGE_LIST_RESERVATION_RECIPIENTS, size=None, start=None)

    def delete(self, resv_key: str, msg_key: str) -> None:
        """예약 수신자 삭제.

        예약 건에 등록된 수신자를 메시지 키(msgKey) 기준으로 삭제합니다.

        ``DELETE /api/comm/v1/reservation/resvKey/{resvKey}/destinations/msgKey/{msgKey}`` (``deleteReservationRecipient``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.
            msg_key: 조회할 메시지 키입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_delete_reservation_recipient(resv_key=resv_key, msg_key=msg_key))


class AsyncReservationsRecipients:
    """``client.reservations.recipients`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(
        self, resv_key: str, body: _q.ReservationRecipientCreateRequest | Mapping[str, Any]
    ) -> _r.SendOmniResult:
        """예약 수신자 추가.

        기존 예약 건에 수신자를 추가합니다. 한 번에 최대 1,000건까지 추가할 수 있습니다. 수신자별 `code`를 함께 확인합니다.

        ``POST /api/comm/v1/reservation/resvKey/{resvKey}/destinations`` (``addReservationRecipients``). 429만 재시도, 속도 제한 버킷: ``send``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.
            body: :class:`~bizgo.models.ReservationRecipientCreateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``SendOmniResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_add_reservation_recipients(
            await self._transport.call(_call_add_reservation_recipients(resv_key=resv_key, body=body))
        )

    async def list(
        self, resv_key: str, *, last_seq: int | None = None, limit: int | None = None
    ) -> _r.ReservationRecipientListResult:
        """예약 수신자 목록 조회.

        예약 건에 등록된 수신자 목록을 조회합니다.

        ``GET /api/comm/v1/reservation/resvKey/{resvKey}/destinations`` (``listReservationRecipients``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.
            last_seq: 다음 페이지를 조회할 때 쓰는 마지막 순번입니다. 이전 응답의 `data.data.lastSeq`를 넣습니다.
            limit: 조회 건수입니다.

        Returns:
            ``ReservationRecipientListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_reservation_recipients(
            await self._transport.call(
                _call_list_reservation_recipients(resv_key=resv_key, last_seq=last_seq, limit=limit)
            )
        )

    def iter_list(self, resv_key: str, *, limit: int | None = None) -> AsyncIterator[_r.ReservationRecipient]:
        """Iterate over every page of :meth:`list` (``listReservationRecipients``, cursor pagination)."""

        async def fetch(position: Any) -> Any:
            body = await self._transport.call(
                _call_list_reservation_recipients(resv_key=resv_key, limit=limit, last_seq=position)
            )
            return validate(_r.ReservationRecipientListResponse, body, "listReservationRecipients")

        return aiterate(fetch, _PAGE_LIST_RESERVATION_RECIPIENTS, size=None, start=None)

    async def delete(self, resv_key: str, msg_key: str) -> None:
        """예약 수신자 삭제.

        예약 건에 등록된 수신자를 메시지 키(msgKey) 기준으로 삭제합니다.

        ``DELETE /api/comm/v1/reservation/resvKey/{resvKey}/destinations/msgKey/{msgKey}`` (``deleteReservationRecipient``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.
            msg_key: 조회할 메시지 키입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_delete_reservation_recipient(resv_key=resv_key, msg_key=msg_key))


class Reservations:
    """``client.reservations``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport
        self.recipients = ReservationsRecipients(transport)

    def create(self, body: _q.ReservationCreateRequest | Mapping[str, Any]) -> _r.ReservationCreateServiceResult:
        """예약 발송 등록.

        메시지를 지정한 시각에 발송하도록 예약 등록합니다. SMS/LMS/MMS, 국제, 통합 RCS, 알림톡, 브랜드메시지(기본형·자유형)를 예약할 수 있으며,
        채널별 메시지 필드는 통합 발송 규격과 같습니다. 채널별 안내는 문자·국제·RCS·알림톡·브랜드메시지 API 레퍼런스의 "예약 발송" 섹션에 있습니다.

        ``POST /api/comm/v1/reservation`` (``createReservation``). 429만 재시도, 속도 제한 버킷: ``send``.

        Args:
            body: :class:`~bizgo.models.ReservationCreateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``ReservationCreateServiceResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_reservation(self._transport.call(_call_create_reservation(body=body)))

    def list(
        self,
        *,
        resv_send_time: dt.datetime | str,
        payment_code: str | None = None,
        last_seq: int | None = None,
        limit: int | None = None,
    ) -> _r.ReservationListResult:
        """예약 목록 조회.

        예약 발송 건 목록을 조회합니다. `resvSendTime`에 지정한 시각을 포함해 그 이후의 예약 건이 조회됩니다.

        ``GET /api/comm/v1/reservation/list`` (``listReservations``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_send_time: 조회 기준 예약 발송 시각입니다. `yyyy-MM-dd HH:mm:ss` 형식만 쓸 수 있습니다.
            payment_code: 정산 코드로 조회 대상을 거릅니다.
            last_seq: 다음 페이지를 조회할 때 쓰는 마지막 순번입니다. 이전 응답의 `data.data.lastSeq`를 넣습니다.
            limit: 조회 건수입니다.

        Returns:
            ``ReservationListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_reservations(
            self._transport.call(
                _call_list_reservations(
                    resv_send_time=resv_send_time, payment_code=payment_code, last_seq=last_seq, limit=limit
                )
            )
        )

    def iter_list(
        self, *, resv_send_time: dt.datetime | str, payment_code: str | None = None, limit: int | None = None
    ) -> Iterator[_r.Reservation]:
        """Iterate over every page of :meth:`list` (``listReservations``, cursor pagination)."""

        def fetch(position: Any) -> Any:
            body = self._transport.call(
                _call_list_reservations(
                    resv_send_time=resv_send_time, payment_code=payment_code, limit=limit, last_seq=position
                )
            )
            return validate(_r.ReservationListResponse, body, "listReservations")

        return iterate(fetch, _PAGE_LIST_RESERVATIONS, size=None, start=None)

    def get(self, resv_key: str) -> _r.Reservation:
        """예약 상세 조회.

        예약 발송 키(resvKey)로 예약 건을 단건 조회합니다.

        ``GET /api/comm/v1/reservation/resvKey/{resvKey}`` (``getReservation``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.

        Returns:
            ``Reservation`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_reservation(self._transport.call(_call_get_reservation(resv_key=resv_key)))

    def update(self, resv_key: str, body: _q.ReservationUpdateRequest | Mapping[str, Any]) -> _r.Reservation:
        """예약 수정.

        예약 대기(PENDING) 상태인 예약 건의 발송 시각과 예약명을 수정합니다. 다른 상태이면 거절됩니다(A824).
        수정 응답에는 `resvData`가 빠질 수 있습니다.

        ``PUT /api/comm/v1/reservation/resvKey/{resvKey}`` (``updateReservation``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.
            body: :class:`~bizgo.models.ReservationUpdateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``Reservation`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_update_reservation(self._transport.call(_call_update_reservation(resv_key=resv_key, body=body)))

    def cancel(self, resv_key: str) -> _r.Reservation:
        """예약 취소.

        예약 대기(PENDING) 또는 예약 중지(STOPPED) 상태인 예약 건을 취소합니다. 성공하면 `status`가 `CANCELLED`가 됩니다.

        ``POST /api/comm/v1/reservation/resvKey/{resvKey}/cancel`` (``cancelReservation``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.

        Returns:
            ``Reservation`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_cancel_reservation(self._transport.call(_call_cancel_reservation(resv_key=resv_key)))

    def pause(self, resv_key: str) -> _r.Reservation:
        """예약 중지.

        발송 처리 중(PROCESSING)인 예약 건을 중지합니다. 성공하면 `status`가 `STOPPED`가 되며, 재개(`resume`)로 다시 발송할 수 있습니다.

        ``POST /api/comm/v1/reservation/resvKey/{resvKey}/stop`` (``stopReservation``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.

        Returns:
            ``Reservation`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_stop_reservation(self._transport.call(_call_stop_reservation(resv_key=resv_key)))

    def resume(self, resv_key: str) -> _r.Reservation:
        """예약 재개.

        예약 중지(STOPPED) 상태인 예약 건을 다시 발송 처리합니다.

        ``POST /api/comm/v1/reservation/resvKey/{resvKey}/resume`` (``resumeReservation``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.

        Returns:
            ``Reservation`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_resume_reservation(self._transport.call(_call_resume_reservation(resv_key=resv_key)))


class AsyncReservations:
    """``client.reservations`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport
        self.recipients = AsyncReservationsRecipients(transport)

    async def create(self, body: _q.ReservationCreateRequest | Mapping[str, Any]) -> _r.ReservationCreateServiceResult:
        """예약 발송 등록.

        메시지를 지정한 시각에 발송하도록 예약 등록합니다. SMS/LMS/MMS, 국제, 통합 RCS, 알림톡, 브랜드메시지(기본형·자유형)를 예약할 수 있으며,
        채널별 메시지 필드는 통합 발송 규격과 같습니다. 채널별 안내는 문자·국제·RCS·알림톡·브랜드메시지 API 레퍼런스의 "예약 발송" 섹션에 있습니다.

        ``POST /api/comm/v1/reservation`` (``createReservation``). 429만 재시도, 속도 제한 버킷: ``send``.

        Args:
            body: :class:`~bizgo.models.ReservationCreateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``ReservationCreateServiceResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_reservation(await self._transport.call(_call_create_reservation(body=body)))

    async def list(
        self,
        *,
        resv_send_time: dt.datetime | str,
        payment_code: str | None = None,
        last_seq: int | None = None,
        limit: int | None = None,
    ) -> _r.ReservationListResult:
        """예약 목록 조회.

        예약 발송 건 목록을 조회합니다. `resvSendTime`에 지정한 시각을 포함해 그 이후의 예약 건이 조회됩니다.

        ``GET /api/comm/v1/reservation/list`` (``listReservations``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_send_time: 조회 기준 예약 발송 시각입니다. `yyyy-MM-dd HH:mm:ss` 형식만 쓸 수 있습니다.
            payment_code: 정산 코드로 조회 대상을 거릅니다.
            last_seq: 다음 페이지를 조회할 때 쓰는 마지막 순번입니다. 이전 응답의 `data.data.lastSeq`를 넣습니다.
            limit: 조회 건수입니다.

        Returns:
            ``ReservationListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_reservations(
            await self._transport.call(
                _call_list_reservations(
                    resv_send_time=resv_send_time, payment_code=payment_code, last_seq=last_seq, limit=limit
                )
            )
        )

    def iter_list(
        self, *, resv_send_time: dt.datetime | str, payment_code: str | None = None, limit: int | None = None
    ) -> AsyncIterator[_r.Reservation]:
        """Iterate over every page of :meth:`list` (``listReservations``, cursor pagination)."""

        async def fetch(position: Any) -> Any:
            body = await self._transport.call(
                _call_list_reservations(
                    resv_send_time=resv_send_time, payment_code=payment_code, limit=limit, last_seq=position
                )
            )
            return validate(_r.ReservationListResponse, body, "listReservations")

        return aiterate(fetch, _PAGE_LIST_RESERVATIONS, size=None, start=None)

    async def get(self, resv_key: str) -> _r.Reservation:
        """예약 상세 조회.

        예약 발송 키(resvKey)로 예약 건을 단건 조회합니다.

        ``GET /api/comm/v1/reservation/resvKey/{resvKey}`` (``getReservation``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.

        Returns:
            ``Reservation`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_reservation(await self._transport.call(_call_get_reservation(resv_key=resv_key)))

    async def update(self, resv_key: str, body: _q.ReservationUpdateRequest | Mapping[str, Any]) -> _r.Reservation:
        """예약 수정.

        예약 대기(PENDING) 상태인 예약 건의 발송 시각과 예약명을 수정합니다. 다른 상태이면 거절됩니다(A824).
        수정 응답에는 `resvData`가 빠질 수 있습니다.

        ``PUT /api/comm/v1/reservation/resvKey/{resvKey}`` (``updateReservation``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.
            body: :class:`~bizgo.models.ReservationUpdateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``Reservation`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_update_reservation(
            await self._transport.call(_call_update_reservation(resv_key=resv_key, body=body))
        )

    async def cancel(self, resv_key: str) -> _r.Reservation:
        """예약 취소.

        예약 대기(PENDING) 또는 예약 중지(STOPPED) 상태인 예약 건을 취소합니다. 성공하면 `status`가 `CANCELLED`가 됩니다.

        ``POST /api/comm/v1/reservation/resvKey/{resvKey}/cancel`` (``cancelReservation``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.

        Returns:
            ``Reservation`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_cancel_reservation(await self._transport.call(_call_cancel_reservation(resv_key=resv_key)))

    async def pause(self, resv_key: str) -> _r.Reservation:
        """예약 중지.

        발송 처리 중(PROCESSING)인 예약 건을 중지합니다. 성공하면 `status`가 `STOPPED`가 되며, 재개(`resume`)로 다시 발송할 수 있습니다.

        ``POST /api/comm/v1/reservation/resvKey/{resvKey}/stop`` (``stopReservation``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.

        Returns:
            ``Reservation`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_stop_reservation(await self._transport.call(_call_stop_reservation(resv_key=resv_key)))

    async def resume(self, resv_key: str) -> _r.Reservation:
        """예약 재개.

        예약 중지(STOPPED) 상태인 예약 건을 다시 발송 처리합니다.

        ``POST /api/comm/v1/reservation/resvKey/{resvKey}/resume`` (``resumeReservation``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            resv_key: 예약 발송 키입니다. 예약 발송 등록 응답의 `data.resvKey` 값입니다.

        Returns:
            ``Reservation`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_resume_reservation(await self._transport.call(_call_resume_reservation(resv_key=resv_key)))


class InsightsAlimtalk:
    """``client.insights.alimtalk``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get(
        self,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        sender_key: str | Sequence[str],
        template_code: str | Sequence[str] | None = None,
    ) -> _r.InsightKakaoStatisticsResult:
        """알림톡 주요 인사이트 조회.

        기간·발신프로필 기준으로 알림톡 발송 성공/실패·읽음·클릭 등 주요 통계를 조회합니다. 카카오가 직접 제공하는 통계입니다.

        ``GET /api/comm/v1/center/statistics/alimtalk`` (``getAlimtalkInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            sender_key: 발신프로필 키입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다.
            template_code: 템플릿 코드입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다. 넣지 않으면 전체를 조회합니다.

        Returns:
            ``InsightKakaoStatisticsResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_alimtalk_insight(
            self._transport.call(
                _call_get_alimtalk_insight(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, template_code=template_code
                )
            )
        )

    def get_hourly(
        self,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        sender_key: str | Sequence[str],
        template_code: str | Sequence[str] | None = None,
    ) -> _r.InsightKakaoHourlyStatisticsResult:
        """알림톡 시간별 반응 지표.

        기간·발신프로필 기준으로 알림톡 시간대별(0~23시) 반응 통계를 조회합니다.

        ``GET /api/comm/v1/center/statistics/alimtalk/reaction/hourly`` (``getAlimtalkHourlyInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            sender_key: 발신프로필 키입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다.
            template_code: 템플릿 코드입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다. 넣지 않으면 전체를 조회합니다.

        Returns:
            ``InsightKakaoHourlyStatisticsResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_alimtalk_hourly_insight(
            self._transport.call(
                _call_get_alimtalk_hourly_insight(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, template_code=template_code
                )
            )
        )

    def get_by_template(
        self,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        sender_key: str | Sequence[str],
        template_code: str | Sequence[str] | None = None,
    ) -> _r.InsightKakaoTemplateStatisticsResult:
        """알림톡 템플릿 상세 조회.

        기간·발신프로필 기준으로 알림톡 템플릿별 통계를 조회합니다.

        ``GET /api/comm/v1/center/statistics/alimtalk/template`` (``getAlimtalkTemplateInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            sender_key: 발신프로필 키입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다.
            template_code: 템플릿 코드입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다. 넣지 않으면 전체를 조회합니다.

        Returns:
            ``InsightKakaoTemplateStatisticsResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_alimtalk_template_insight(
            self._transport.call(
                _call_get_alimtalk_template_insight(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, template_code=template_code
                )
            )
        )


class AsyncInsightsAlimtalk:
    """``client.insights.alimtalk`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get(
        self,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        sender_key: str | Sequence[str],
        template_code: str | Sequence[str] | None = None,
    ) -> _r.InsightKakaoStatisticsResult:
        """알림톡 주요 인사이트 조회.

        기간·발신프로필 기준으로 알림톡 발송 성공/실패·읽음·클릭 등 주요 통계를 조회합니다. 카카오가 직접 제공하는 통계입니다.

        ``GET /api/comm/v1/center/statistics/alimtalk`` (``getAlimtalkInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            sender_key: 발신프로필 키입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다.
            template_code: 템플릿 코드입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다. 넣지 않으면 전체를 조회합니다.

        Returns:
            ``InsightKakaoStatisticsResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_alimtalk_insight(
            await self._transport.call(
                _call_get_alimtalk_insight(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, template_code=template_code
                )
            )
        )

    async def get_hourly(
        self,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        sender_key: str | Sequence[str],
        template_code: str | Sequence[str] | None = None,
    ) -> _r.InsightKakaoHourlyStatisticsResult:
        """알림톡 시간별 반응 지표.

        기간·발신프로필 기준으로 알림톡 시간대별(0~23시) 반응 통계를 조회합니다.

        ``GET /api/comm/v1/center/statistics/alimtalk/reaction/hourly`` (``getAlimtalkHourlyInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            sender_key: 발신프로필 키입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다.
            template_code: 템플릿 코드입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다. 넣지 않으면 전체를 조회합니다.

        Returns:
            ``InsightKakaoHourlyStatisticsResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_alimtalk_hourly_insight(
            await self._transport.call(
                _call_get_alimtalk_hourly_insight(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, template_code=template_code
                )
            )
        )

    async def get_by_template(
        self,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        sender_key: str | Sequence[str],
        template_code: str | Sequence[str] | None = None,
    ) -> _r.InsightKakaoTemplateStatisticsResult:
        """알림톡 템플릿 상세 조회.

        기간·발신프로필 기준으로 알림톡 템플릿별 통계를 조회합니다.

        ``GET /api/comm/v1/center/statistics/alimtalk/template`` (``getAlimtalkTemplateInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            sender_key: 발신프로필 키입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다.
            template_code: 템플릿 코드입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다. 넣지 않으면 전체를 조회합니다.

        Returns:
            ``InsightKakaoTemplateStatisticsResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_alimtalk_template_insight(
            await self._transport.call(
                _call_get_alimtalk_template_insight(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, template_code=template_code
                )
            )
        )


class InsightsBrandMessage:
    """``client.insights.brand_message``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get(
        self,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        sender_key: str | Sequence[str],
        template_code: str | Sequence[str] | None = None,
    ) -> _r.InsightKakaoStatisticsResult:
        """브랜드메시지 주요 인사이트 조회.

        기간·발신프로필 기준으로 브랜드메시지 발송 성공/실패·읽음·클릭 등 주요 통계를 조회합니다. 카카오가 직접 제공하는 통계입니다.

        ``GET /api/comm/v1/center/statistics/brandmessage`` (``getBrandMessageInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            sender_key: 발신프로필 키입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다.
            template_code: 템플릿 코드입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다. 넣지 않으면 전체를 조회합니다.

        Returns:
            ``InsightKakaoStatisticsResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_insight(
            self._transport.call(
                _call_get_brand_message_insight(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, template_code=template_code
                )
            )
        )

    def get_hourly(
        self,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        sender_key: str | Sequence[str],
        template_code: str | Sequence[str] | None = None,
    ) -> _r.InsightKakaoHourlyStatisticsResult:
        """브랜드메시지 시간별 반응 지표.

        기간·발신프로필 기준으로 브랜드메시지 시간대별(0~23시) 반응 통계를 조회합니다.

        ``GET /api/comm/v1/center/statistics/brandmessage/reaction/hourly`` (``getBrandMessageHourlyInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            sender_key: 발신프로필 키입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다.
            template_code: 템플릿 코드입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다. 넣지 않으면 전체를 조회합니다.

        Returns:
            ``InsightKakaoHourlyStatisticsResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_hourly_insight(
            self._transport.call(
                _call_get_brand_message_hourly_insight(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, template_code=template_code
                )
            )
        )

    def get_by_template(
        self,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        sender_key: str | Sequence[str],
        template_code: str | Sequence[str] | None = None,
    ) -> _r.InsightKakaoTemplateStatisticsResult:
        """브랜드메시지 템플릿 상세 조회.

        기간·발신프로필 기준으로 브랜드메시지 템플릿별 통계를 조회합니다.

        ``GET /api/comm/v1/center/statistics/brandmessage/template`` (``getBrandMessageTemplateInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            sender_key: 발신프로필 키입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다.
            template_code: 템플릿 코드입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다. 넣지 않으면 전체를 조회합니다.

        Returns:
            ``InsightKakaoTemplateStatisticsResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_template_insight(
            self._transport.call(
                _call_get_brand_message_template_insight(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, template_code=template_code
                )
            )
        )


class AsyncInsightsBrandMessage:
    """``client.insights.brand_message`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get(
        self,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        sender_key: str | Sequence[str],
        template_code: str | Sequence[str] | None = None,
    ) -> _r.InsightKakaoStatisticsResult:
        """브랜드메시지 주요 인사이트 조회.

        기간·발신프로필 기준으로 브랜드메시지 발송 성공/실패·읽음·클릭 등 주요 통계를 조회합니다. 카카오가 직접 제공하는 통계입니다.

        ``GET /api/comm/v1/center/statistics/brandmessage`` (``getBrandMessageInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            sender_key: 발신프로필 키입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다.
            template_code: 템플릿 코드입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다. 넣지 않으면 전체를 조회합니다.

        Returns:
            ``InsightKakaoStatisticsResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_insight(
            await self._transport.call(
                _call_get_brand_message_insight(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, template_code=template_code
                )
            )
        )

    async def get_hourly(
        self,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        sender_key: str | Sequence[str],
        template_code: str | Sequence[str] | None = None,
    ) -> _r.InsightKakaoHourlyStatisticsResult:
        """브랜드메시지 시간별 반응 지표.

        기간·발신프로필 기준으로 브랜드메시지 시간대별(0~23시) 반응 통계를 조회합니다.

        ``GET /api/comm/v1/center/statistics/brandmessage/reaction/hourly`` (``getBrandMessageHourlyInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            sender_key: 발신프로필 키입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다.
            template_code: 템플릿 코드입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다. 넣지 않으면 전체를 조회합니다.

        Returns:
            ``InsightKakaoHourlyStatisticsResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_hourly_insight(
            await self._transport.call(
                _call_get_brand_message_hourly_insight(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, template_code=template_code
                )
            )
        )

    async def get_by_template(
        self,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        sender_key: str | Sequence[str],
        template_code: str | Sequence[str] | None = None,
    ) -> _r.InsightKakaoTemplateStatisticsResult:
        """브랜드메시지 템플릿 상세 조회.

        기간·발신프로필 기준으로 브랜드메시지 템플릿별 통계를 조회합니다.

        ``GET /api/comm/v1/center/statistics/brandmessage/template`` (``getBrandMessageTemplateInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            sender_key: 발신프로필 키입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다.
            template_code: 템플릿 코드입니다. 여러 개를 조회하려면 콤마(,)로 구분해 전달합니다. 넣지 않으면 전체를 조회합니다.

        Returns:
            ``InsightKakaoTemplateStatisticsResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_template_insight(
            await self._transport.call(
                _call_get_brand_message_template_insight(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, template_code=template_code
                )
            )
        )


class InsightsRcs:
    """``client.insights.rcs``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get_message(
        self,
        brand_id: str,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        group_id: str,
        chatbot_id: str | None = None,
    ) -> _r.InsightRcsMessageStatResult:
        """RCS 메시지 발송·노출 통계.

        브랜드·그룹 기준으로 RCS 메시지의 발송 건수와 노출(읽음) 건수를 일자별로 조회합니다.
        통계는 발송 요청의 `groupId` 단위로 집계되며, `groupId` 없이 보낸 건은 포함되지 않습니다.
        응답 데이터는 `data.data`가 아니라 `data.rcs`에 있습니다.

        ``GET /api/comm/v1/center/rcs/brandId/{brandId}/stat/message`` (``getRcsMessageInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: RCS 브랜드 ID입니다.
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            group_id: 그룹 ID입니다. RCS 발송 요청에 넣은 `messageFlow[].rcs.groupId` 값이어야 합니다.
            chatbot_id: 챗봇 ID입니다. 지정하면 해당 챗봇으로 범위를 좁힙니다.

        Returns:
            ``InsightRcsMessageStatResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_message_insight(
            self._transport.call(
                _call_get_rcs_message_insight(
                    brand_id=brand_id,
                    start_date=start_date,
                    end_date=end_date,
                    group_id=group_id,
                    chatbot_id=chatbot_id,
                )
            )
        )

    def get_message_button(
        self,
        brand_id: str,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        group_id: str,
        chatbot_id: str | None = None,
    ) -> _r.InsightRcsMessageButtonStatResult:
        """RCS 메시지 버튼 클릭 통계.

        RCS 메시지에 포함된 버튼의 클릭 수를 카드·버튼 단위로 조회합니다.
        응답 데이터는 `data.data`가 아니라 `data.rcs`에 있습니다.

        ``GET /api/comm/v1/center/rcs/brandId/{brandId}/stat/messageButton`` (``getRcsMessageButtonInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: RCS 브랜드 ID입니다.
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            group_id: 그룹 ID입니다. RCS 발송 요청에 넣은 `messageFlow[].rcs.groupId` 값이어야 합니다.
            chatbot_id: 챗봇 ID입니다. 지정하면 해당 챗봇으로 범위를 좁힙니다.

        Returns:
            ``InsightRcsMessageButtonStatResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_message_button_insight(
            self._transport.call(
                _call_get_rcs_message_button_insight(
                    brand_id=brand_id,
                    start_date=start_date,
                    end_date=end_date,
                    group_id=group_id,
                    chatbot_id=chatbot_id,
                )
            )
        )

    def get_persistent_menu(
        self, brand_id: str, *, start_date: dt.date | str, end_date: dt.date | str, chatbot_id: str
    ) -> _r.InsightRcsPersistentMenuStatResult:
        """RCS 대화방 메뉴 클릭 통계.

        대화방 하단 고정 메뉴의 클릭 수를 메뉴 단위로 조회합니다. RCS 인사이트 중 이 API만 `chatbotId`가 필수입니다.
        응답 데이터는 `data.data`가 아니라 `data.rcs`에 있습니다.

        ``GET /api/comm/v1/center/rcs/brandId/{brandId}/stat/persistentMenu`` (``getRcsPersistentMenuInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: RCS 브랜드 ID입니다.
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            chatbot_id: 챗봇 ID입니다. 넣지 않으면 요청이 거절됩니다.

        Returns:
            ``InsightRcsPersistentMenuStatResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_persistent_menu_insight(
            self._transport.call(
                _call_get_rcs_persistent_menu_insight(
                    brand_id=brand_id, start_date=start_date, end_date=end_date, chatbot_id=chatbot_id
                )
            )
        )

    def get_brand_profile(
        self, brand_id: str, *, start_date: dt.date | str, end_date: dt.date | str
    ) -> _r.InsightRcsBrandProfileStatResult:
        """RCS 브랜드 프로필 노출 통계.

        브랜드 프로필이 노출된 건수를 일자별로 조회합니다. 그룹·챗봇 조건 없이 기간만으로 조회합니다.
        응답 데이터는 `data.data`가 아니라 `data.rcs`에 있습니다.

        ``GET /api/comm/v1/center/rcs/brandId/{brandId}/stat/brandProfile`` (``getRcsBrandProfileInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: RCS 브랜드 ID입니다.
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.

        Returns:
            ``InsightRcsBrandProfileStatResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_brand_profile_insight(
            self._transport.call(
                _call_get_rcs_brand_profile_insight(brand_id=brand_id, start_date=start_date, end_date=end_date)
            )
        )


class AsyncInsightsRcs:
    """``client.insights.rcs`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_message(
        self,
        brand_id: str,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        group_id: str,
        chatbot_id: str | None = None,
    ) -> _r.InsightRcsMessageStatResult:
        """RCS 메시지 발송·노출 통계.

        브랜드·그룹 기준으로 RCS 메시지의 발송 건수와 노출(읽음) 건수를 일자별로 조회합니다.
        통계는 발송 요청의 `groupId` 단위로 집계되며, `groupId` 없이 보낸 건은 포함되지 않습니다.
        응답 데이터는 `data.data`가 아니라 `data.rcs`에 있습니다.

        ``GET /api/comm/v1/center/rcs/brandId/{brandId}/stat/message`` (``getRcsMessageInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: RCS 브랜드 ID입니다.
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            group_id: 그룹 ID입니다. RCS 발송 요청에 넣은 `messageFlow[].rcs.groupId` 값이어야 합니다.
            chatbot_id: 챗봇 ID입니다. 지정하면 해당 챗봇으로 범위를 좁힙니다.

        Returns:
            ``InsightRcsMessageStatResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_message_insight(
            await self._transport.call(
                _call_get_rcs_message_insight(
                    brand_id=brand_id,
                    start_date=start_date,
                    end_date=end_date,
                    group_id=group_id,
                    chatbot_id=chatbot_id,
                )
            )
        )

    async def get_message_button(
        self,
        brand_id: str,
        *,
        start_date: dt.date | str,
        end_date: dt.date | str,
        group_id: str,
        chatbot_id: str | None = None,
    ) -> _r.InsightRcsMessageButtonStatResult:
        """RCS 메시지 버튼 클릭 통계.

        RCS 메시지에 포함된 버튼의 클릭 수를 카드·버튼 단위로 조회합니다.
        응답 데이터는 `data.data`가 아니라 `data.rcs`에 있습니다.

        ``GET /api/comm/v1/center/rcs/brandId/{brandId}/stat/messageButton`` (``getRcsMessageButtonInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: RCS 브랜드 ID입니다.
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            group_id: 그룹 ID입니다. RCS 발송 요청에 넣은 `messageFlow[].rcs.groupId` 값이어야 합니다.
            chatbot_id: 챗봇 ID입니다. 지정하면 해당 챗봇으로 범위를 좁힙니다.

        Returns:
            ``InsightRcsMessageButtonStatResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_message_button_insight(
            await self._transport.call(
                _call_get_rcs_message_button_insight(
                    brand_id=brand_id,
                    start_date=start_date,
                    end_date=end_date,
                    group_id=group_id,
                    chatbot_id=chatbot_id,
                )
            )
        )

    async def get_persistent_menu(
        self, brand_id: str, *, start_date: dt.date | str, end_date: dt.date | str, chatbot_id: str
    ) -> _r.InsightRcsPersistentMenuStatResult:
        """RCS 대화방 메뉴 클릭 통계.

        대화방 하단 고정 메뉴의 클릭 수를 메뉴 단위로 조회합니다. RCS 인사이트 중 이 API만 `chatbotId`가 필수입니다.
        응답 데이터는 `data.data`가 아니라 `data.rcs`에 있습니다.

        ``GET /api/comm/v1/center/rcs/brandId/{brandId}/stat/persistentMenu`` (``getRcsPersistentMenuInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: RCS 브랜드 ID입니다.
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.
            chatbot_id: 챗봇 ID입니다. 넣지 않으면 요청이 거절됩니다.

        Returns:
            ``InsightRcsPersistentMenuStatResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_persistent_menu_insight(
            await self._transport.call(
                _call_get_rcs_persistent_menu_insight(
                    brand_id=brand_id, start_date=start_date, end_date=end_date, chatbot_id=chatbot_id
                )
            )
        )

    async def get_brand_profile(
        self, brand_id: str, *, start_date: dt.date | str, end_date: dt.date | str
    ) -> _r.InsightRcsBrandProfileStatResult:
        """RCS 브랜드 프로필 노출 통계.

        브랜드 프로필이 노출된 건수를 일자별로 조회합니다. 그룹·챗봇 조건 없이 기간만으로 조회합니다.
        응답 데이터는 `data.data`가 아니라 `data.rcs`에 있습니다.

        ``GET /api/comm/v1/center/rcs/brandId/{brandId}/stat/brandProfile`` (``getRcsBrandProfileInsight``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: RCS 브랜드 ID입니다.
            start_date: 조회 시작일(YYYYMMDD)입니다.
            end_date: 조회 종료일(YYYYMMDD)입니다.

        Returns:
            ``InsightRcsBrandProfileStatResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_brand_profile_insight(
            await self._transport.call(
                _call_get_rcs_brand_profile_insight(brand_id=brand_id, start_date=start_date, end_date=end_date)
            )
        )


class Insights:
    """``client.insights``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport
        self.alimtalk = InsightsAlimtalk(transport)
        self.brand_message = InsightsBrandMessage(transport)
        self.rcs = InsightsRcs(transport)


class AsyncInsights:
    """``client.insights`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport
        self.alimtalk = AsyncInsightsAlimtalk(transport)
        self.brand_message = AsyncInsightsBrandMessage(transport)
        self.rcs = AsyncInsightsRcs(transport)


class KakaoSenders:
    """``client.kakao.senders``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def request_token(self, body: _q.KakaoSenderTokenRequest | Mapping[str, Any]) -> _r.KakaoSenderAccountServiceResult:
        """카카오 채널 인증 토큰 요청.

        발신프로필 등록에 필요한 카카오톡 채널 인증 토큰을 요청합니다.

        ``POST /api/comm/v1/account/kakao/sender/token`` (``requestKakaoSenderToken``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.KakaoSenderTokenRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``KakaoSenderAccountServiceResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_request_kakao_sender_token(self._transport.call(_call_request_kakao_sender_token(body=body)))

    def create(
        self, body: _q.KakaoSenderCreateRequest | Mapping[str, Any], *, token: str, phone_number: str
    ) -> _r.KakaoSenderProfile:
        """인증 토큰으로 발신프로필 등록.

        카카오톡 채널을 발신프로필로 신규 등록합니다.
        카카오비즈니스 파트너센터에서 비즈니스 인증을 받았고, 프로필이 activated 상태이며 운영자에 의해 차단되지 않은 채널이어야 합니다.
        카카오 채널 인증 토큰 요청(`POST /api/comm/v1/account/kakao/sender/token`)으로 받은 토큰과 그때 쓴 전화번호를 헤더로 보냅니다.

        ``POST /api/comm/v1/account/kakao/sender`` (``createKakaoSender``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            token: 카카오 채널 인증 토큰 요청 후 카카오톡으로 받은 채널 인증 토큰 값입니다.
            phone_number: 관리자 전화번호입니다. 카카오 채널 인증 토큰 요청 시 입력한 번호와 같아야 합니다.
            body: :class:`~bizgo.models.KakaoSenderCreateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``KakaoSenderProfile`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_kakao_sender(
            self._transport.call(_call_create_kakao_sender(body=body, token=token, phone_number=phone_number))
        )

    def find(self, *, uuid: str | None = None, sender_key: str | None = None) -> _r.KakaoSenderProfile:
        """발신프로필 키 또는 uuid로 조회.

        발신프로필 키(`senderKey`) 또는 카카오톡 채널 uuid에 해당하는 발신프로필을 조회합니다. `senderKey`와 `uuid` 중 하나는 반드시 입력해야 합니다.

        ``GET /api/comm/v1/account/kakao/sender`` (``findKakaoSender``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            uuid: 조회할 카카오톡 채널의 uuid(`@`로 시작하는 채널 아이디)입니다. `senderKey`가 없으면 필수입니다.
            sender_key: 조회할 발신프로필 키입니다. `uuid`가 없으면 필수입니다.

        Returns:
            ``KakaoSenderProfile`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_find_kakao_sender(self._transport.call(_call_find_kakao_sender(uuid=uuid, sender_key=sender_key)))

    def list(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        sender_key: str | None = None,
        page: int | None = None,
        rows: int | None = None,
    ) -> _r.KakaoSenderListServiceResult:
        """발신프로필 목록 조회.

        API 키에 등록된 발신프로필 목록을 조회합니다. 검색 기간과 발신프로필 키로 범위를 좁힐 수 있고, 결과는 페이지 단위로 반환합니다.

        ``GET /api/comm/v1/account/kakao/sender/profiles`` (``listKakaoSenderProfiles``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            start_date: 검색 시작일입니다.
            end_date: 검색 종료일입니다.
            sender_key: 발신프로필 키 또는 발신프로필 그룹키입니다.
            page: 페이지 번호입니다.
            rows: 페이지당 조회 건수입니다.

        Returns:
            ``KakaoSenderListServiceResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_kakao_sender_profiles(
            self._transport.call(
                _call_list_kakao_sender_profiles(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, page=page, rows=rows
                )
            )
        )

    def iter_list(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        sender_key: str | None = None,
        rows: int | None = None,
    ) -> Iterator[_r.KakaoSenderChannel]:
        """Iterate over every page of :meth:`list` (``listKakaoSenderProfiles``, page pagination)."""

        def fetch(position: Any) -> Any:
            body = self._transport.call(
                _call_list_kakao_sender_profiles(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, rows=rows, page=position
                )
            )
            return validate(_r.KakaoSenderListResponse, body, "listKakaoSenderProfiles")

        return iterate(fetch, _PAGE_LIST_KAKAO_SENDER_PROFILES, size=rows, start=None)

    def get(self, *, sender_key: str) -> _r.KakaoSenderProfile:
        """발신프로필 키로 조회.

        발신프로필 키를 기준으로 카카오 발신프로필 정보를 조회합니다. 알림톡, 브랜드메시지, 상담톡에서 사용하는 senderKey의 상태(차단·휴면·스팸 등)를 확인할 때 사용합니다.

        ``GET /api/comm/v1/center/kakao/sender`` (``getKakaoSender``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.

        Returns:
            ``KakaoSenderProfile`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_kakao_sender(self._transport.call(_call_get_kakao_sender(sender_key=sender_key)))

    def recover(self, body: _q.KakaoSenderRecoverRequest | Mapping[str, Any]) -> None:
        """발신프로필 휴면 해제.

        휴면 상태의 발신프로필을 해제합니다. 카카오 비즈메시지 발송 전 발신프로필 상태 복구가 필요한 경우 사용합니다.

        ``POST /api/comm/v1/center/kakao/sender/recover`` (``recoverKakaoSender``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.KakaoSenderRecoverRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_recover_kakao_sender(body=body))


class AsyncKakaoSenders:
    """``client.kakao.senders`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def request_token(
        self, body: _q.KakaoSenderTokenRequest | Mapping[str, Any]
    ) -> _r.KakaoSenderAccountServiceResult:
        """카카오 채널 인증 토큰 요청.

        발신프로필 등록에 필요한 카카오톡 채널 인증 토큰을 요청합니다.

        ``POST /api/comm/v1/account/kakao/sender/token`` (``requestKakaoSenderToken``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.KakaoSenderTokenRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``KakaoSenderAccountServiceResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_request_kakao_sender_token(
            await self._transport.call(_call_request_kakao_sender_token(body=body))
        )

    async def create(
        self, body: _q.KakaoSenderCreateRequest | Mapping[str, Any], *, token: str, phone_number: str
    ) -> _r.KakaoSenderProfile:
        """인증 토큰으로 발신프로필 등록.

        카카오톡 채널을 발신프로필로 신규 등록합니다.
        카카오비즈니스 파트너센터에서 비즈니스 인증을 받았고, 프로필이 activated 상태이며 운영자에 의해 차단되지 않은 채널이어야 합니다.
        카카오 채널 인증 토큰 요청(`POST /api/comm/v1/account/kakao/sender/token`)으로 받은 토큰과 그때 쓴 전화번호를 헤더로 보냅니다.

        ``POST /api/comm/v1/account/kakao/sender`` (``createKakaoSender``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            token: 카카오 채널 인증 토큰 요청 후 카카오톡으로 받은 채널 인증 토큰 값입니다.
            phone_number: 관리자 전화번호입니다. 카카오 채널 인증 토큰 요청 시 입력한 번호와 같아야 합니다.
            body: :class:`~bizgo.models.KakaoSenderCreateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``KakaoSenderProfile`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_kakao_sender(
            await self._transport.call(_call_create_kakao_sender(body=body, token=token, phone_number=phone_number))
        )

    async def find(self, *, uuid: str | None = None, sender_key: str | None = None) -> _r.KakaoSenderProfile:
        """발신프로필 키 또는 uuid로 조회.

        발신프로필 키(`senderKey`) 또는 카카오톡 채널 uuid에 해당하는 발신프로필을 조회합니다. `senderKey`와 `uuid` 중 하나는 반드시 입력해야 합니다.

        ``GET /api/comm/v1/account/kakao/sender`` (``findKakaoSender``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            uuid: 조회할 카카오톡 채널의 uuid(`@`로 시작하는 채널 아이디)입니다. `senderKey`가 없으면 필수입니다.
            sender_key: 조회할 발신프로필 키입니다. `uuid`가 없으면 필수입니다.

        Returns:
            ``KakaoSenderProfile`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_find_kakao_sender(
            await self._transport.call(_call_find_kakao_sender(uuid=uuid, sender_key=sender_key))
        )

    async def list(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        sender_key: str | None = None,
        page: int | None = None,
        rows: int | None = None,
    ) -> _r.KakaoSenderListServiceResult:
        """발신프로필 목록 조회.

        API 키에 등록된 발신프로필 목록을 조회합니다. 검색 기간과 발신프로필 키로 범위를 좁힐 수 있고, 결과는 페이지 단위로 반환합니다.

        ``GET /api/comm/v1/account/kakao/sender/profiles`` (``listKakaoSenderProfiles``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            start_date: 검색 시작일입니다.
            end_date: 검색 종료일입니다.
            sender_key: 발신프로필 키 또는 발신프로필 그룹키입니다.
            page: 페이지 번호입니다.
            rows: 페이지당 조회 건수입니다.

        Returns:
            ``KakaoSenderListServiceResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_kakao_sender_profiles(
            await self._transport.call(
                _call_list_kakao_sender_profiles(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, page=page, rows=rows
                )
            )
        )

    def iter_list(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        sender_key: str | None = None,
        rows: int | None = None,
    ) -> AsyncIterator[_r.KakaoSenderChannel]:
        """Iterate over every page of :meth:`list` (``listKakaoSenderProfiles``, page pagination)."""

        async def fetch(position: Any) -> Any:
            body = await self._transport.call(
                _call_list_kakao_sender_profiles(
                    start_date=start_date, end_date=end_date, sender_key=sender_key, rows=rows, page=position
                )
            )
            return validate(_r.KakaoSenderListResponse, body, "listKakaoSenderProfiles")

        return aiterate(fetch, _PAGE_LIST_KAKAO_SENDER_PROFILES, size=rows, start=None)

    async def get(self, *, sender_key: str) -> _r.KakaoSenderProfile:
        """발신프로필 키로 조회.

        발신프로필 키를 기준으로 카카오 발신프로필 정보를 조회합니다. 알림톡, 브랜드메시지, 상담톡에서 사용하는 senderKey의 상태(차단·휴면·스팸 등)를 확인할 때 사용합니다.

        ``GET /api/comm/v1/center/kakao/sender`` (``getKakaoSender``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.

        Returns:
            ``KakaoSenderProfile`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_kakao_sender(await self._transport.call(_call_get_kakao_sender(sender_key=sender_key)))

    async def recover(self, body: _q.KakaoSenderRecoverRequest | Mapping[str, Any]) -> None:
        """발신프로필 휴면 해제.

        휴면 상태의 발신프로필을 해제합니다. 카카오 비즈메시지 발송 전 발신프로필 상태 복구가 필요한 경우 사용합니다.

        ``POST /api/comm/v1/center/kakao/sender/recover`` (``recoverKakaoSender``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.KakaoSenderRecoverRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_recover_kakao_sender(body=body))


class KakaoCategories:
    """``client.kakao.categories``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(self) -> builtins.list[_r.KakaoCategory]:
        """발신프로필 카테고리 전체조회.

        발신프로필 등록 시 사용할 수 있는 카카오 비즈메시지 카테고리 목록을 조회합니다.

        ``GET /api/comm/v1/center/kakao/sender/category/list`` (``listKakaoSenderCategories``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Returns:
            ``list[KakaoCategory]`` (없으면 빈 목록).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_kakao_sender_categories(self._transport.call(_call_list_kakao_sender_categories()))

    def get(self, *, code: str) -> _r.KakaoCategory:
        """발신프로필 카테고리 상세조회.

        카테고리 코드를 기준으로 카카오 비즈메시지 카테고리 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/kakao/sender/category`` (``getKakaoSenderCategory``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            code: 조회할 카테고리 코드입니다.

        Returns:
            ``KakaoCategory`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_kakao_sender_category(self._transport.call(_call_get_kakao_sender_category(code=code)))


class AsyncKakaoCategories:
    """``client.kakao.categories`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(self) -> builtins.list[_r.KakaoCategory]:
        """발신프로필 카테고리 전체조회.

        발신프로필 등록 시 사용할 수 있는 카카오 비즈메시지 카테고리 목록을 조회합니다.

        ``GET /api/comm/v1/center/kakao/sender/category/list`` (``listKakaoSenderCategories``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Returns:
            ``list[KakaoCategory]`` (없으면 빈 목록).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_kakao_sender_categories(await self._transport.call(_call_list_kakao_sender_categories()))

    async def get(self, *, code: str) -> _r.KakaoCategory:
        """발신프로필 카테고리 상세조회.

        카테고리 코드를 기준으로 카카오 비즈메시지 카테고리 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/kakao/sender/category`` (``getKakaoSenderCategory``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            code: 조회할 카테고리 코드입니다.

        Returns:
            ``KakaoCategory`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_kakao_sender_category(await self._transport.call(_call_get_kakao_sender_category(code=code)))


class KakaoGroups:
    """``client.kakao.groups``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(self, *, sender_key: str | None = None) -> builtins.list[_r.KakaoGroup]:
        """발신프로필키로 그룹 조회.

        발신프로필 키를 기준으로 연결된 발신프로필 그룹 정보를 조회합니다. `senderKey`를 생략하면 조회 가능한 그룹 정보를 기준으로 응답합니다.

        ``GET /api/comm/v1/center/kakao/group`` (``listKakaoGroups``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 조회 기준 발신프로필 키입니다.

        Returns:
            ``list[KakaoGroup]`` (없으면 빈 목록).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_kakao_groups(self._transport.call(_call_list_kakao_groups(sender_key=sender_key)))

    def add_sender(self, body: _q.KakaoGroupSenderAddRequest | Mapping[str, Any]) -> None:
        """그룹에 발신프로필 등록.

        발신프로필 그룹에 발신프로필을 등록합니다. 그룹 키와 등록할 발신프로필 키를 함께 전달합니다.

        ``POST /api/comm/v1/center/kakao/group`` (``addKakaoGroupSender``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.KakaoGroupSenderAddRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_add_kakao_group_sender(body=body))

    def remove_sender(self, group_key: str, sender_key: str) -> None:
        """그룹에서 발신프로필 삭제.

        발신프로필 그룹에서 특정 발신프로필을 삭제합니다.

        ``DELETE /api/comm/v1/center/kakao/group/groupKey/{groupKey}/senderKey/{senderKey}`` (``removeKakaoGroupSender``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            group_key: 그룹 키입니다.
            sender_key: 삭제할 발신프로필 키입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_remove_kakao_group_sender(group_key=group_key, sender_key=sender_key))


class AsyncKakaoGroups:
    """``client.kakao.groups`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(self, *, sender_key: str | None = None) -> builtins.list[_r.KakaoGroup]:
        """발신프로필키로 그룹 조회.

        발신프로필 키를 기준으로 연결된 발신프로필 그룹 정보를 조회합니다. `senderKey`를 생략하면 조회 가능한 그룹 정보를 기준으로 응답합니다.

        ``GET /api/comm/v1/center/kakao/group`` (``listKakaoGroups``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 조회 기준 발신프로필 키입니다.

        Returns:
            ``list[KakaoGroup]`` (없으면 빈 목록).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_kakao_groups(await self._transport.call(_call_list_kakao_groups(sender_key=sender_key)))

    async def add_sender(self, body: _q.KakaoGroupSenderAddRequest | Mapping[str, Any]) -> None:
        """그룹에 발신프로필 등록.

        발신프로필 그룹에 발신프로필을 등록합니다. 그룹 키와 등록할 발신프로필 키를 함께 전달합니다.

        ``POST /api/comm/v1/center/kakao/group`` (``addKakaoGroupSender``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.KakaoGroupSenderAddRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_add_kakao_group_sender(body=body))

    async def remove_sender(self, group_key: str, sender_key: str) -> None:
        """그룹에서 발신프로필 삭제.

        발신프로필 그룹에서 특정 발신프로필을 삭제합니다.

        ``DELETE /api/comm/v1/center/kakao/group/groupKey/{groupKey}/senderKey/{senderKey}`` (``removeKakaoGroupSender``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            group_key: 그룹 키입니다.
            sender_key: 삭제할 발신프로필 키입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_remove_kakao_group_sender(group_key=group_key, sender_key=sender_key))


class KakaoSanctions:
    """``client.kakao.sanctions``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get_sender(self, *, date: dt.date | str, sender_key: str) -> _r.KakaoSanction:
        """발신프로필 제재 조회.

        특정 일자에 발신프로필에 적용된 제재 정보를 조회합니다. 발송 전 운영 상태를 확인할 때 사용합니다.

        ``GET /api/comm/v1/center/kakao/abusing/block/sender`` (``getKakaoSenderSanction``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            date: 조회 기준 날짜(YYYYMMDD)입니다. 예 `20260305`.
            sender_key: 발신프로필 키입니다.

        Returns:
            ``KakaoSanction`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_kakao_sender_sanction(
            self._transport.call(_call_get_kakao_sender_sanction(date=date, sender_key=sender_key))
        )

    def get_group_template_exclusion(
        self, *, date: dt.date | str, sender_key: str, group_key: str, template_code: str
    ) -> _r.KakaoSanction:
        """그룹템플릿 발신프로필 제외 조회.

        그룹템플릿에서 특정 발신프로필이 제외(제한)된 제재 정보를 조회합니다.

        ``GET /api/comm/v1/center/kakao/abusing/block/senderGroup`` (``getKakaoGroupTemplateSenderExclusion``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            date: 조회 기준 날짜(YYYYMMDD)입니다. 예 `20260305`.
            sender_key: 발신프로필 키입니다.
            group_key: 그룹 발신프로필 키입니다.
            template_code: 템플릿 코드입니다.

        Returns:
            ``KakaoSanction`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_kakao_group_template_sender_exclusion(
            self._transport.call(
                _call_get_kakao_group_template_sender_exclusion(
                    date=date, sender_key=sender_key, group_key=group_key, template_code=template_code
                )
            )
        )

    def get_template(self, *, date: dt.date | str, sender_key: str, template_code: str) -> _r.KakaoSanction:
        """템플릿 제재 조회.

        특정 일자에 템플릿에 적용된 제재 정보를 조회합니다.

        ``GET /api/comm/v1/center/kakao/abusing/block/template`` (``getKakaoTemplateSanction``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            date: 조회 기준 날짜(YYYYMMDD)입니다. 예 `20260305`.
            sender_key: 발신프로필 키입니다.
            template_code: 템플릿 코드입니다.

        Returns:
            ``KakaoSanction`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_kakao_template_sanction(
            self._transport.call(
                _call_get_kakao_template_sanction(date=date, sender_key=sender_key, template_code=template_code)
            )
        )


class AsyncKakaoSanctions:
    """``client.kakao.sanctions`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_sender(self, *, date: dt.date | str, sender_key: str) -> _r.KakaoSanction:
        """발신프로필 제재 조회.

        특정 일자에 발신프로필에 적용된 제재 정보를 조회합니다. 발송 전 운영 상태를 확인할 때 사용합니다.

        ``GET /api/comm/v1/center/kakao/abusing/block/sender`` (``getKakaoSenderSanction``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            date: 조회 기준 날짜(YYYYMMDD)입니다. 예 `20260305`.
            sender_key: 발신프로필 키입니다.

        Returns:
            ``KakaoSanction`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_kakao_sender_sanction(
            await self._transport.call(_call_get_kakao_sender_sanction(date=date, sender_key=sender_key))
        )

    async def get_group_template_exclusion(
        self, *, date: dt.date | str, sender_key: str, group_key: str, template_code: str
    ) -> _r.KakaoSanction:
        """그룹템플릿 발신프로필 제외 조회.

        그룹템플릿에서 특정 발신프로필이 제외(제한)된 제재 정보를 조회합니다.

        ``GET /api/comm/v1/center/kakao/abusing/block/senderGroup`` (``getKakaoGroupTemplateSenderExclusion``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            date: 조회 기준 날짜(YYYYMMDD)입니다. 예 `20260305`.
            sender_key: 발신프로필 키입니다.
            group_key: 그룹 발신프로필 키입니다.
            template_code: 템플릿 코드입니다.

        Returns:
            ``KakaoSanction`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_kakao_group_template_sender_exclusion(
            await self._transport.call(
                _call_get_kakao_group_template_sender_exclusion(
                    date=date, sender_key=sender_key, group_key=group_key, template_code=template_code
                )
            )
        )

    async def get_template(self, *, date: dt.date | str, sender_key: str, template_code: str) -> _r.KakaoSanction:
        """템플릿 제재 조회.

        특정 일자에 템플릿에 적용된 제재 정보를 조회합니다.

        ``GET /api/comm/v1/center/kakao/abusing/block/template`` (``getKakaoTemplateSanction``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            date: 조회 기준 날짜(YYYYMMDD)입니다. 예 `20260305`.
            sender_key: 발신프로필 키입니다.
            template_code: 템플릿 코드입니다.

        Returns:
            ``KakaoSanction`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_kakao_template_sanction(
            await self._transport.call(
                _call_get_kakao_template_sanction(date=date, sender_key=sender_key, template_code=template_code)
            )
        )


class Kakao:
    """``client.kakao``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport
        self.senders = KakaoSenders(transport)
        self.categories = KakaoCategories(transport)
        self.groups = KakaoGroups(transport)
        self.sanctions = KakaoSanctions(transport)


class AsyncKakao:
    """``client.kakao`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport
        self.senders = AsyncKakaoSenders(transport)
        self.categories = AsyncKakaoCategories(transport)
        self.groups = AsyncKakaoGroups(transport)
        self.sanctions = AsyncKakaoSanctions(transport)


class AlimtalkTemplates:
    """``client.alimtalk.templates``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get(self, *, sender_key: str, template_code: str) -> _r.AlimtalkTemplate:
        """알림톡 템플릿 조회.

        발신프로필 키와 템플릿 코드를 기준으로 알림톡 템플릿 상세 정보(검수 상태, 심사 의견 포함)를 조회합니다.

        ``GET /api/comm/v1/center/alimtalk/template`` (``getAlimtalkTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            template_code: 템플릿 코드입니다.

        Returns:
            ``AlimtalkTemplate`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_alimtalk_template(
            self._transport.call(_call_get_alimtalk_template(sender_key=sender_key, template_code=template_code))
        )

    def create(self, body: _q.AlimtalkTemplateSaveRequest | Mapping[str, Any]) -> _r.AlimtalkTemplate:
        """알림톡 템플릿 등록.

        알림톡 템플릿을 등록합니다. 등록한 템플릿은 검수 요청(`POST /api/comm/v1/center/alimtalk/template/request`) 후 카카오 승인을 받아야 발송할 수 있습니다.
        이미지형·아이템리스트형 템플릿은 템플릿 이미지 업로드 API로 받은 `imgUrl`을 함께 넣습니다.

        ``POST /api/comm/v1/center/alimtalk/template`` (``createAlimtalkTemplate``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.AlimtalkTemplateSaveRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``AlimtalkTemplate`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_alimtalk_template(self._transport.call(_call_create_alimtalk_template(body=body)))

    def update(self, body: _q.AlimtalkTemplateSaveRequest | Mapping[str, Any]) -> _r.AlimtalkTemplate:
        """알림톡 템플릿 수정.

        등록된 알림톡 템플릿 정보를 수정합니다. 검수 상태와 카카오 정책에 따라 수정 가능한 범위가 달라질 수 있습니다. 대상 템플릿은 본문의 `senderKey`와 `templateCode`로 지정합니다.

        ``PUT /api/comm/v1/center/alimtalk/template`` (``updateAlimtalkTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.AlimtalkTemplateSaveRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``AlimtalkTemplate`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_update_alimtalk_template(self._transport.call(_call_update_alimtalk_template(body=body)))

    def list(
        self,
        *,
        sender_key: str,
        sender_key_type: Literal["G", "S"] | None = None,
        status: str | None = None,
        inspection_status: Literal["REG", "REQ", "APR", "REJ"] | None = None,
        template_type: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> builtins.list[_r.AlimtalkTemplate]:
        """알림톡 템플릿 목록 조회.

        발신프로필에 등록된 알림톡 템플릿 목록을 페이징 조회합니다. 카카오를 호출하지 않고 비즈고에 적재된 템플릿을 읽으므로 목록 화면이나 주기적인 동기화에 사용할 수 있습니다.

        ``GET /api/comm/v1/center/alimtalk/template/list`` (``listAlimtalkTemplates``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키 또는 그룹키입니다.
            sender_key_type: 발신키 유형입니다(`S` 발신프로필, `G` 그룹).
            status: 템플릿 상태입니다.
            inspection_status: 검수 상태입니다(`REG` 등록, `REQ` 검수 요청, `APR` 승인, `REJ` 반려).
            template_type: 템플릿 유형입니다.
            offset: 조회 시작 위치입니다. 문서 예시는 `0`입니다.
            limit: 조회 건수입니다. 문서 예시는 `100`입니다.

        Returns:
            ``list[AlimtalkTemplate]`` (없으면 빈 목록).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_alimtalk_templates(
            self._transport.call(
                _call_list_alimtalk_templates(
                    sender_key=sender_key,
                    sender_key_type=sender_key_type,
                    status=status,
                    inspection_status=inspection_status,
                    template_type=template_type,
                    offset=offset,
                    limit=limit,
                )
            )
        )

    def iter_list(
        self,
        *,
        sender_key: str,
        sender_key_type: Literal["G", "S"] | None = None,
        status: str | None = None,
        inspection_status: Literal["REG", "REQ", "APR", "REJ"] | None = None,
        template_type: str | None = None,
        limit: int | None = None,
    ) -> Iterator[_r.AlimtalkTemplate]:
        """Iterate over every page of :meth:`list` (``listAlimtalkTemplates``, offset pagination)."""

        def fetch(position: Any) -> Any:
            body = self._transport.call(
                _call_list_alimtalk_templates(
                    sender_key=sender_key,
                    sender_key_type=sender_key_type,
                    status=status,
                    inspection_status=inspection_status,
                    template_type=template_type,
                    limit=limit,
                    offset=position,
                )
            )
            return validate(_r.AlimtalkTemplateListResponse, body, "listAlimtalkTemplates")

        return iterate(fetch, _PAGE_LIST_ALIMTALK_TEMPLATES, size=limit, start=None)

    def list_modified(
        self,
        *,
        sender_key: str,
        sender_key_type: Literal["G", "S"] | None = None,
        since: dt.datetime | str | None = None,
        page: int | None = None,
        count: int | None = None,
    ) -> builtins.list[_r.AlimtalkTemplate]:
        """최근 변경 알림톡 템플릿 조회.

        지정한 시각 이후 변경된 알림톡 템플릿 목록을 조회합니다. 템플릿 최신화나 내부 동기화 배치 기준으로 사용할 수 있습니다.

        ``GET /api/comm/v1/center/alimtalk/template/lastModified`` (``listModifiedAlimtalkTemplates``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다. 최대 40자입니다.
            sender_key_type: 발신키 유형입니다(`S` 발신프로필, `G` 그룹). 기본값은 `S`입니다.
            since: 조회 시작 시각(yyyy-MM-dd'T'HH:mm:ss)입니다. 예 `2026-04-23T09:00:00`.
            page: 페이지 번호입니다. 기본값 1, 최소 1입니다.
            count: 페이지당 조회 건수입니다. 기본값 100, 최소 1입니다.

        Returns:
            ``list[AlimtalkTemplate]`` (없으면 빈 목록).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_modified_alimtalk_templates(
            self._transport.call(
                _call_list_modified_alimtalk_templates(
                    sender_key=sender_key, sender_key_type=sender_key_type, since=since, page=page, count=count
                )
            )
        )

    def iter_list_modified(
        self,
        *,
        sender_key: str,
        sender_key_type: Literal["G", "S"] | None = None,
        since: dt.datetime | str | None = None,
        count: int | None = None,
    ) -> Iterator[_r.AlimtalkTemplate]:
        """Iterate over every page of :meth:`list_modified` (``listModifiedAlimtalkTemplates``, page pagination)."""

        def fetch(position: Any) -> Any:
            body = self._transport.call(
                _call_list_modified_alimtalk_templates(
                    sender_key=sender_key, sender_key_type=sender_key_type, since=since, count=count, page=position
                )
            )
            return validate(_r.AlimtalkTemplateListResponse, body, "listModifiedAlimtalkTemplates")

        return iterate(fetch, _PAGE_LIST_MODIFIED_ALIMTALK_TEMPLATES, size=count, start=1)

    def delete(self, sender_key: str, template_code: str) -> None:
        """알림톡 템플릿 삭제.

        발신프로필 키와 템플릿 코드를 기준으로 알림톡 템플릿을 삭제합니다.

        ``DELETE /api/comm/v1/center/alimtalk/template/senderKey/{senderKey}/templateCode/{templateCode}`` (``deleteAlimtalkTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            template_code: 삭제할 템플릿 코드입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_delete_alimtalk_template(sender_key=sender_key, template_code=template_code))

    def request_inspection(self, body: _q.AlimtalkTemplateInspectionRequest | Mapping[str, Any]) -> None:
        """알림톡 템플릿 검수 요청.

        등록된 알림톡 템플릿을 카카오 검수로 요청합니다. 템플릿 상태가 대기이고 검수 상태가 등록(`REG`)인 경우 요청할 수 있습니다.
        - `application/json`: 첨부 없이 요청합니다. 템플릿 정보는 `alimtalk` 객체에 넣습니다.
        - `multipart/form-data`: 파일을 첨부해 요청합니다. 필드를 최상위에 두며 `comment`가 필수입니다. 파일 형식은 png, jpg, jpeg, gif, pdf, hwp, doc, docx입니다.

        ``POST /api/comm/v1/center/alimtalk/template/request`` (``requestAlimtalkTemplateInspection``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            sender_key_type: 발신프로필 키 타입입니다. 기본값은 `S`입니다.
            template_code: 템플릿 코드입니다.
            comment: 검수 의견 또는 문의 사항입니다. 파일첨부 요청에서는 필수입니다.
            attachment: 검수 요청에 첨부할 파일입니다. `attachment` 필드를 반복해 최대 10개까지 보낼 수 있으며, 파일당 최대 50MB, 합계 최대 100MB입니다.
            body: :class:`~bizgo.models.AlimtalkTemplateInspectionRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_request_alimtalk_template_inspection(body=body))

    def request_inspection_with_files(
        self,
        *,
        sender_key: str,
        template_code: str,
        comment: str,
        sender_key_type: Literal["G", "S"] | None = None,
        attachment: Sequence[FileInput] | None = None,
    ) -> None:
        """알림톡 템플릿 검수 요청.

        등록된 알림톡 템플릿을 카카오 검수로 요청합니다. 템플릿 상태가 대기이고 검수 상태가 등록(`REG`)인 경우 요청할 수 있습니다.
        - `application/json`: 첨부 없이 요청합니다. 템플릿 정보는 `alimtalk` 객체에 넣습니다.
        - `multipart/form-data`: 파일을 첨부해 요청합니다. 필드를 최상위에 두며 `comment`가 필수입니다. 파일 형식은 png, jpg, jpeg, gif, pdf, hwp, doc, docx입니다.

        ``POST /api/comm/v1/center/alimtalk/template/request`` (``requestAlimtalkTemplateInspection``). 429만 재시도, 속도 제한 버킷: ``other``.

        multipart/form-data로 파일과 함께 보냅니다.

        Args:
            sender_key: 발신프로필 키입니다.
            sender_key_type: 발신프로필 키 타입입니다. 기본값은 `S`입니다.
            template_code: 템플릿 코드입니다.
            comment: 검수 의견 또는 문의 사항입니다. 파일첨부 요청에서는 필수입니다.
            attachment: 검수 요청에 첨부할 파일입니다. `attachment` 필드를 반복해 최대 10개까지 보낼 수 있으며, 파일당 최대 50MB, 합계 최대 100MB입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(
            _call_request_alimtalk_template_inspection_form(
                sender_key=sender_key,
                template_code=template_code,
                comment=comment,
                sender_key_type=sender_key_type,
                attachment=attachment,
            )
        )

    def cancel_inspection(self, body: _q.AlimtalkTemplateInspectionCancelRequest | Mapping[str, Any]) -> None:
        """알림톡 템플릿 검수 요청 취소.

        검수 요청된 알림톡 템플릿의 검수 요청을 취소합니다.

        ``POST /api/comm/v1/center/alimtalk/template/request/cancel`` (``cancelAlimtalkTemplateInspection``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.AlimtalkTemplateInspectionCancelRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_cancel_alimtalk_template_inspection(body=body))


class AsyncAlimtalkTemplates:
    """``client.alimtalk.templates`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get(self, *, sender_key: str, template_code: str) -> _r.AlimtalkTemplate:
        """알림톡 템플릿 조회.

        발신프로필 키와 템플릿 코드를 기준으로 알림톡 템플릿 상세 정보(검수 상태, 심사 의견 포함)를 조회합니다.

        ``GET /api/comm/v1/center/alimtalk/template`` (``getAlimtalkTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            template_code: 템플릿 코드입니다.

        Returns:
            ``AlimtalkTemplate`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_alimtalk_template(
            await self._transport.call(_call_get_alimtalk_template(sender_key=sender_key, template_code=template_code))
        )

    async def create(self, body: _q.AlimtalkTemplateSaveRequest | Mapping[str, Any]) -> _r.AlimtalkTemplate:
        """알림톡 템플릿 등록.

        알림톡 템플릿을 등록합니다. 등록한 템플릿은 검수 요청(`POST /api/comm/v1/center/alimtalk/template/request`) 후 카카오 승인을 받아야 발송할 수 있습니다.
        이미지형·아이템리스트형 템플릿은 템플릿 이미지 업로드 API로 받은 `imgUrl`을 함께 넣습니다.

        ``POST /api/comm/v1/center/alimtalk/template`` (``createAlimtalkTemplate``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.AlimtalkTemplateSaveRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``AlimtalkTemplate`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_alimtalk_template(await self._transport.call(_call_create_alimtalk_template(body=body)))

    async def update(self, body: _q.AlimtalkTemplateSaveRequest | Mapping[str, Any]) -> _r.AlimtalkTemplate:
        """알림톡 템플릿 수정.

        등록된 알림톡 템플릿 정보를 수정합니다. 검수 상태와 카카오 정책에 따라 수정 가능한 범위가 달라질 수 있습니다. 대상 템플릿은 본문의 `senderKey`와 `templateCode`로 지정합니다.

        ``PUT /api/comm/v1/center/alimtalk/template`` (``updateAlimtalkTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.AlimtalkTemplateSaveRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``AlimtalkTemplate`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_update_alimtalk_template(await self._transport.call(_call_update_alimtalk_template(body=body)))

    async def list(
        self,
        *,
        sender_key: str,
        sender_key_type: Literal["G", "S"] | None = None,
        status: str | None = None,
        inspection_status: Literal["REG", "REQ", "APR", "REJ"] | None = None,
        template_type: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> builtins.list[_r.AlimtalkTemplate]:
        """알림톡 템플릿 목록 조회.

        발신프로필에 등록된 알림톡 템플릿 목록을 페이징 조회합니다. 카카오를 호출하지 않고 비즈고에 적재된 템플릿을 읽으므로 목록 화면이나 주기적인 동기화에 사용할 수 있습니다.

        ``GET /api/comm/v1/center/alimtalk/template/list`` (``listAlimtalkTemplates``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키 또는 그룹키입니다.
            sender_key_type: 발신키 유형입니다(`S` 발신프로필, `G` 그룹).
            status: 템플릿 상태입니다.
            inspection_status: 검수 상태입니다(`REG` 등록, `REQ` 검수 요청, `APR` 승인, `REJ` 반려).
            template_type: 템플릿 유형입니다.
            offset: 조회 시작 위치입니다. 문서 예시는 `0`입니다.
            limit: 조회 건수입니다. 문서 예시는 `100`입니다.

        Returns:
            ``list[AlimtalkTemplate]`` (없으면 빈 목록).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_alimtalk_templates(
            await self._transport.call(
                _call_list_alimtalk_templates(
                    sender_key=sender_key,
                    sender_key_type=sender_key_type,
                    status=status,
                    inspection_status=inspection_status,
                    template_type=template_type,
                    offset=offset,
                    limit=limit,
                )
            )
        )

    def iter_list(
        self,
        *,
        sender_key: str,
        sender_key_type: Literal["G", "S"] | None = None,
        status: str | None = None,
        inspection_status: Literal["REG", "REQ", "APR", "REJ"] | None = None,
        template_type: str | None = None,
        limit: int | None = None,
    ) -> AsyncIterator[_r.AlimtalkTemplate]:
        """Iterate over every page of :meth:`list` (``listAlimtalkTemplates``, offset pagination)."""

        async def fetch(position: Any) -> Any:
            body = await self._transport.call(
                _call_list_alimtalk_templates(
                    sender_key=sender_key,
                    sender_key_type=sender_key_type,
                    status=status,
                    inspection_status=inspection_status,
                    template_type=template_type,
                    limit=limit,
                    offset=position,
                )
            )
            return validate(_r.AlimtalkTemplateListResponse, body, "listAlimtalkTemplates")

        return aiterate(fetch, _PAGE_LIST_ALIMTALK_TEMPLATES, size=limit, start=None)

    async def list_modified(
        self,
        *,
        sender_key: str,
        sender_key_type: Literal["G", "S"] | None = None,
        since: dt.datetime | str | None = None,
        page: int | None = None,
        count: int | None = None,
    ) -> builtins.list[_r.AlimtalkTemplate]:
        """최근 변경 알림톡 템플릿 조회.

        지정한 시각 이후 변경된 알림톡 템플릿 목록을 조회합니다. 템플릿 최신화나 내부 동기화 배치 기준으로 사용할 수 있습니다.

        ``GET /api/comm/v1/center/alimtalk/template/lastModified`` (``listModifiedAlimtalkTemplates``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다. 최대 40자입니다.
            sender_key_type: 발신키 유형입니다(`S` 발신프로필, `G` 그룹). 기본값은 `S`입니다.
            since: 조회 시작 시각(yyyy-MM-dd'T'HH:mm:ss)입니다. 예 `2026-04-23T09:00:00`.
            page: 페이지 번호입니다. 기본값 1, 최소 1입니다.
            count: 페이지당 조회 건수입니다. 기본값 100, 최소 1입니다.

        Returns:
            ``list[AlimtalkTemplate]`` (없으면 빈 목록).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_modified_alimtalk_templates(
            await self._transport.call(
                _call_list_modified_alimtalk_templates(
                    sender_key=sender_key, sender_key_type=sender_key_type, since=since, page=page, count=count
                )
            )
        )

    def iter_list_modified(
        self,
        *,
        sender_key: str,
        sender_key_type: Literal["G", "S"] | None = None,
        since: dt.datetime | str | None = None,
        count: int | None = None,
    ) -> AsyncIterator[_r.AlimtalkTemplate]:
        """Iterate over every page of :meth:`list_modified` (``listModifiedAlimtalkTemplates``, page pagination)."""

        async def fetch(position: Any) -> Any:
            body = await self._transport.call(
                _call_list_modified_alimtalk_templates(
                    sender_key=sender_key, sender_key_type=sender_key_type, since=since, count=count, page=position
                )
            )
            return validate(_r.AlimtalkTemplateListResponse, body, "listModifiedAlimtalkTemplates")

        return aiterate(fetch, _PAGE_LIST_MODIFIED_ALIMTALK_TEMPLATES, size=count, start=1)

    async def delete(self, sender_key: str, template_code: str) -> None:
        """알림톡 템플릿 삭제.

        발신프로필 키와 템플릿 코드를 기준으로 알림톡 템플릿을 삭제합니다.

        ``DELETE /api/comm/v1/center/alimtalk/template/senderKey/{senderKey}/templateCode/{templateCode}`` (``deleteAlimtalkTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            template_code: 삭제할 템플릿 코드입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_delete_alimtalk_template(sender_key=sender_key, template_code=template_code))

    async def request_inspection(self, body: _q.AlimtalkTemplateInspectionRequest | Mapping[str, Any]) -> None:
        """알림톡 템플릿 검수 요청.

        등록된 알림톡 템플릿을 카카오 검수로 요청합니다. 템플릿 상태가 대기이고 검수 상태가 등록(`REG`)인 경우 요청할 수 있습니다.
        - `application/json`: 첨부 없이 요청합니다. 템플릿 정보는 `alimtalk` 객체에 넣습니다.
        - `multipart/form-data`: 파일을 첨부해 요청합니다. 필드를 최상위에 두며 `comment`가 필수입니다. 파일 형식은 png, jpg, jpeg, gif, pdf, hwp, doc, docx입니다.

        ``POST /api/comm/v1/center/alimtalk/template/request`` (``requestAlimtalkTemplateInspection``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            sender_key_type: 발신프로필 키 타입입니다. 기본값은 `S`입니다.
            template_code: 템플릿 코드입니다.
            comment: 검수 의견 또는 문의 사항입니다. 파일첨부 요청에서는 필수입니다.
            attachment: 검수 요청에 첨부할 파일입니다. `attachment` 필드를 반복해 최대 10개까지 보낼 수 있으며, 파일당 최대 50MB, 합계 최대 100MB입니다.
            body: :class:`~bizgo.models.AlimtalkTemplateInspectionRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_request_alimtalk_template_inspection(body=body))

    async def request_inspection_with_files(
        self,
        *,
        sender_key: str,
        template_code: str,
        comment: str,
        sender_key_type: Literal["G", "S"] | None = None,
        attachment: Sequence[FileInput] | None = None,
    ) -> None:
        """알림톡 템플릿 검수 요청.

        등록된 알림톡 템플릿을 카카오 검수로 요청합니다. 템플릿 상태가 대기이고 검수 상태가 등록(`REG`)인 경우 요청할 수 있습니다.
        - `application/json`: 첨부 없이 요청합니다. 템플릿 정보는 `alimtalk` 객체에 넣습니다.
        - `multipart/form-data`: 파일을 첨부해 요청합니다. 필드를 최상위에 두며 `comment`가 필수입니다. 파일 형식은 png, jpg, jpeg, gif, pdf, hwp, doc, docx입니다.

        ``POST /api/comm/v1/center/alimtalk/template/request`` (``requestAlimtalkTemplateInspection``). 429만 재시도, 속도 제한 버킷: ``other``.

        multipart/form-data로 파일과 함께 보냅니다.

        Args:
            sender_key: 발신프로필 키입니다.
            sender_key_type: 발신프로필 키 타입입니다. 기본값은 `S`입니다.
            template_code: 템플릿 코드입니다.
            comment: 검수 의견 또는 문의 사항입니다. 파일첨부 요청에서는 필수입니다.
            attachment: 검수 요청에 첨부할 파일입니다. `attachment` 필드를 반복해 최대 10개까지 보낼 수 있으며, 파일당 최대 50MB, 합계 최대 100MB입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(
            _call_request_alimtalk_template_inspection_form(
                sender_key=sender_key,
                template_code=template_code,
                comment=comment,
                sender_key_type=sender_key_type,
                attachment=attachment,
            )
        )

    async def cancel_inspection(self, body: _q.AlimtalkTemplateInspectionCancelRequest | Mapping[str, Any]) -> None:
        """알림톡 템플릿 검수 요청 취소.

        검수 요청된 알림톡 템플릿의 검수 요청을 취소합니다.

        ``POST /api/comm/v1/center/alimtalk/template/request/cancel`` (``cancelAlimtalkTemplateInspection``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.AlimtalkTemplateInspectionCancelRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_cancel_alimtalk_template_inspection(body=body))


class AlimtalkTemplateCategories:
    """``client.alimtalk.template_categories``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(self, *, category_code: str | None = None) -> _r.AlimtalkTemplateCategoryResult:
        """알림톡 템플릿 카테고리 조회.

        알림톡 템플릿 카테고리를 조회합니다. 문서는 같은 경로에 두 기능을 둡니다.
        - `categoryCode` 없이 호출: 템플릿 카테고리 전체 목록(`data.data.categories`)
        - `categoryCode`를 넣어 호출: 해당 카테고리 상세(`data.data.category`)

        ``GET /api/comm/v1/center/alimtalk/category`` (``listAlimtalkTemplateCategories``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            category_code: 조회할 템플릿 카테고리 코드입니다. 넣으면 상세 조회, 생략하면 전체 조회입니다(상세 조회 문서에서는 필수).

        Returns:
            ``AlimtalkTemplateCategoryResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_alimtalk_template_categories(
            self._transport.call(_call_list_alimtalk_template_categories(category_code=category_code))
        )


class AsyncAlimtalkTemplateCategories:
    """``client.alimtalk.template_categories`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(self, *, category_code: str | None = None) -> _r.AlimtalkTemplateCategoryResult:
        """알림톡 템플릿 카테고리 조회.

        알림톡 템플릿 카테고리를 조회합니다. 문서는 같은 경로에 두 기능을 둡니다.
        - `categoryCode` 없이 호출: 템플릿 카테고리 전체 목록(`data.data.categories`)
        - `categoryCode`를 넣어 호출: 해당 카테고리 상세(`data.data.category`)

        ``GET /api/comm/v1/center/alimtalk/category`` (``listAlimtalkTemplateCategories``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            category_code: 조회할 템플릿 카테고리 코드입니다. 넣으면 상세 조회, 생략하면 전체 조회입니다(상세 조회 문서에서는 필수).

        Returns:
            ``AlimtalkTemplateCategoryResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_alimtalk_template_categories(
            await self._transport.call(_call_list_alimtalk_template_categories(category_code=category_code))
        )


class AlimtalkPublicTemplates:
    """``client.alimtalk.public_templates``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(
        self, *, since: dt.datetime | str | None = None, page: int | None = None, count: int | None = None
    ) -> builtins.list[_r.AlimtalkTemplatePublic]:
        """알림톡 공용템플릿 조회.

        카카오가 제공하는 공용템플릿 목록을 조회합니다.

        ``GET /api/comm/v1/center/alimtalk/public/template`` (``listAlimtalkPublicTemplates``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            since: 조회 기준 시각(yyyyMMddHHmmss)입니다. 기본값은 `20250708000000`입니다.
            page: 조회 페이지 번호입니다. 기본값은 1입니다.
            count: 페이지당 조회 건수입니다. 기본값 100, 최대 1,000입니다.

        Returns:
            ``list[AlimtalkTemplatePublic]`` (없으면 빈 목록).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_alimtalk_public_templates(
            self._transport.call(_call_list_alimtalk_public_templates(since=since, page=page, count=count))
        )

    def iter_list(
        self, *, since: dt.datetime | str | None = None, count: int | None = None
    ) -> Iterator[_r.AlimtalkTemplatePublic]:
        """Iterate over every page of :meth:`list` (``listAlimtalkPublicTemplates``, page pagination)."""

        def fetch(position: Any) -> Any:
            body = self._transport.call(_call_list_alimtalk_public_templates(since=since, count=count, page=position))
            return validate(_r.AlimtalkTemplatePublicListResponse, body, "listAlimtalkPublicTemplates")

        return iterate(fetch, _PAGE_LIST_ALIMTALK_PUBLIC_TEMPLATES, size=count, start=1)


class AsyncAlimtalkPublicTemplates:
    """``client.alimtalk.public_templates`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(
        self, *, since: dt.datetime | str | None = None, page: int | None = None, count: int | None = None
    ) -> builtins.list[_r.AlimtalkTemplatePublic]:
        """알림톡 공용템플릿 조회.

        카카오가 제공하는 공용템플릿 목록을 조회합니다.

        ``GET /api/comm/v1/center/alimtalk/public/template`` (``listAlimtalkPublicTemplates``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            since: 조회 기준 시각(yyyyMMddHHmmss)입니다. 기본값은 `20250708000000`입니다.
            page: 조회 페이지 번호입니다. 기본값은 1입니다.
            count: 페이지당 조회 건수입니다. 기본값 100, 최대 1,000입니다.

        Returns:
            ``list[AlimtalkTemplatePublic]`` (없으면 빈 목록).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_alimtalk_public_templates(
            await self._transport.call(_call_list_alimtalk_public_templates(since=since, page=page, count=count))
        )

    def iter_list(
        self, *, since: dt.datetime | str | None = None, count: int | None = None
    ) -> AsyncIterator[_r.AlimtalkTemplatePublic]:
        """Iterate over every page of :meth:`list` (``listAlimtalkPublicTemplates``, page pagination)."""

        async def fetch(position: Any) -> Any:
            body = await self._transport.call(
                _call_list_alimtalk_public_templates(since=since, count=count, page=position)
            )
            return validate(_r.AlimtalkTemplatePublicListResponse, body, "listAlimtalkPublicTemplates")

        return aiterate(fetch, _PAGE_LIST_ALIMTALK_PUBLIC_TEMPLATES, size=count, start=1)


class Alimtalk:
    """``client.alimtalk``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport
        self.templates = AlimtalkTemplates(transport)
        self.template_categories = AlimtalkTemplateCategories(transport)
        self.public_templates = AlimtalkPublicTemplates(transport)


class AsyncAlimtalk:
    """``client.alimtalk`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport
        self.templates = AsyncAlimtalkTemplates(transport)
        self.template_categories = AsyncAlimtalkTemplateCategories(transport)
        self.public_templates = AsyncAlimtalkPublicTemplates(transport)


class BrandMessageGroupSends:
    """``client.brand_message.group_sends``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(self, body: _q.BrandMessageGroupSendCreateRequest | Mapping[str, Any]) -> _r.BrandMessageGroupSendResult:
        """브랜드메시지 동보 발송.

        기본형 템플릿을 기준으로 친구 그룹 또는 전체 친구에게 동보 발송을 예약합니다. 템플릿은 변수가 없고 상태가 등록(`A`)이어야 합니다. 발송 수는 요청 시점의 친구 관계로 정해지고, 실제 발송 시점의 친구 관계에 따라 그 수 안에서 순차 발송됩니다.

        ``POST /api/comm/v1/center/brandmessage/groupMessage`` (``createBrandMessageGroupSend``). 429만 재시도, 속도 제한 버킷: ``send``.

        Args:
            body: :class:`~bizgo.models.BrandMessageGroupSendCreateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageGroupSendResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_brand_message_group_send(
            self._transport.call(_call_create_brand_message_group_send(body=body))
        )

    def get(self, *, sender_key: str, request_id: int) -> _r.BrandMessageGroupSendResult:
        """브랜드메시지 동보 발송 조회.

        발신프로필 키와 요청 아이디로 특정 동보 발송 요청의 상태를 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/groupMessage`` (``getBrandMessageGroupSend``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            request_id: 동보 발송 요청 아이디입니다.

        Returns:
            ``BrandMessageGroupSendResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_group_send(
            self._transport.call(_call_get_brand_message_group_send(sender_key=sender_key, request_id=request_id))
        )

    def resume(
        self, body: _q.BrandMessageGroupSendControlRequest | Mapping[str, Any]
    ) -> _r.BrandMessageGroupSendResult:
        """브랜드메시지 동보 발송 재개.

        중지된 기본형 템플릿 동보 발송 요청을 다시 시작합니다.

        ``POST /api/comm/v1/center/brandmessage/groupMessage/resume`` (``resumeBrandMessageGroupSend``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageGroupSendControlRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageGroupSendResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_resume_brand_message_group_send(
            self._transport.call(_call_resume_brand_message_group_send(body=body))
        )

    def pause(self, body: _q.BrandMessageGroupSendControlRequest | Mapping[str, Any]) -> _r.BrandMessageGroupSendResult:
        """브랜드메시지 동보 발송 중지.

        진행 중인 기본형 템플릿 동보 발송 요청을 일시 중지합니다.

        ``POST /api/comm/v1/center/brandmessage/groupMessage/pause`` (``pauseBrandMessageGroupSend``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageGroupSendControlRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageGroupSendResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_pause_brand_message_group_send(
            self._transport.call(_call_pause_brand_message_group_send(body=body))
        )

    def terminate(
        self, body: _q.BrandMessageGroupSendControlRequest | Mapping[str, Any]
    ) -> _r.BrandMessageGroupSendResult:
        """브랜드메시지 동보 발송 종료.

        예약 또는 진행 중인 기본형 템플릿 동보 발송 요청을 종료합니다.

        ``POST /api/comm/v1/center/brandmessage/groupMessage/terminate`` (``terminateBrandMessageGroupSend``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageGroupSendControlRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageGroupSendResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_terminate_brand_message_group_send(
            self._transport.call(_call_terminate_brand_message_group_send(body=body))
        )


class AsyncBrandMessageGroupSends:
    """``client.brand_message.group_sends`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(
        self, body: _q.BrandMessageGroupSendCreateRequest | Mapping[str, Any]
    ) -> _r.BrandMessageGroupSendResult:
        """브랜드메시지 동보 발송.

        기본형 템플릿을 기준으로 친구 그룹 또는 전체 친구에게 동보 발송을 예약합니다. 템플릿은 변수가 없고 상태가 등록(`A`)이어야 합니다. 발송 수는 요청 시점의 친구 관계로 정해지고, 실제 발송 시점의 친구 관계에 따라 그 수 안에서 순차 발송됩니다.

        ``POST /api/comm/v1/center/brandmessage/groupMessage`` (``createBrandMessageGroupSend``). 429만 재시도, 속도 제한 버킷: ``send``.

        Args:
            body: :class:`~bizgo.models.BrandMessageGroupSendCreateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageGroupSendResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_brand_message_group_send(
            await self._transport.call(_call_create_brand_message_group_send(body=body))
        )

    async def get(self, *, sender_key: str, request_id: int) -> _r.BrandMessageGroupSendResult:
        """브랜드메시지 동보 발송 조회.

        발신프로필 키와 요청 아이디로 특정 동보 발송 요청의 상태를 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/groupMessage`` (``getBrandMessageGroupSend``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            request_id: 동보 발송 요청 아이디입니다.

        Returns:
            ``BrandMessageGroupSendResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_group_send(
            await self._transport.call(_call_get_brand_message_group_send(sender_key=sender_key, request_id=request_id))
        )

    async def resume(
        self, body: _q.BrandMessageGroupSendControlRequest | Mapping[str, Any]
    ) -> _r.BrandMessageGroupSendResult:
        """브랜드메시지 동보 발송 재개.

        중지된 기본형 템플릿 동보 발송 요청을 다시 시작합니다.

        ``POST /api/comm/v1/center/brandmessage/groupMessage/resume`` (``resumeBrandMessageGroupSend``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageGroupSendControlRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageGroupSendResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_resume_brand_message_group_send(
            await self._transport.call(_call_resume_brand_message_group_send(body=body))
        )

    async def pause(
        self, body: _q.BrandMessageGroupSendControlRequest | Mapping[str, Any]
    ) -> _r.BrandMessageGroupSendResult:
        """브랜드메시지 동보 발송 중지.

        진행 중인 기본형 템플릿 동보 발송 요청을 일시 중지합니다.

        ``POST /api/comm/v1/center/brandmessage/groupMessage/pause`` (``pauseBrandMessageGroupSend``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageGroupSendControlRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageGroupSendResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_pause_brand_message_group_send(
            await self._transport.call(_call_pause_brand_message_group_send(body=body))
        )

    async def terminate(
        self, body: _q.BrandMessageGroupSendControlRequest | Mapping[str, Any]
    ) -> _r.BrandMessageGroupSendResult:
        """브랜드메시지 동보 발송 종료.

        예약 또는 진행 중인 기본형 템플릿 동보 발송 요청을 종료합니다.

        ``POST /api/comm/v1/center/brandmessage/groupMessage/terminate`` (``terminateBrandMessageGroupSend``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageGroupSendControlRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageGroupSendResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_terminate_brand_message_group_send(
            await self._transport.call(_call_terminate_brand_message_group_send(body=body))
        )


class BrandMessageAudience:
    """``client.brand_message.audience``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def check_possible(
        self, *, sender_key: str, msg_type: str, friend_group_key: str | None = None
    ) -> _r.BrandMessageAudiencePossibleResult:
        """발송 예상 모수 확인 (친구 그룹 기반).

        메시지 타입과 친구 그룹 조건으로 동보 발송 예상 발송 수를 조회합니다. 친구 그룹을 쓰면 그룹 상태가 완료이고 등록 유저 수가 10 이상이어야 발송 예약이 가능하며, 친구 관계는 실시간으로 동기화됩니다.

        ``GET /api/comm/v1/center/brandmessage/groupMessage/possible`` (``checkBrandMessageAudiencePossible``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            msg_type: 브랜드메시지 타입입니다(카카오 원본 chatBubbleType으로 변환됩니다). 알려진 값: `FT`, `FI`, `FW`, `FL`, `FC`, `FM`, `FA`, `FP`, `FG`.
            friend_group_key: 대상 친구 그룹 키입니다. 생략하면 전체 친구를 기준으로 조회합니다.

        Returns:
            ``BrandMessageAudiencePossibleResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_check_brand_message_audience_possible(
            self._transport.call(
                _call_check_brand_message_audience_possible(
                    sender_key=sender_key, msg_type=msg_type, friend_group_key=friend_group_key
                )
            )
        )

    def check_possible_by_phone_numbers(
        self, body: _q.BrandMessageAudiencePossibleByPhoneNumbersRequest | Mapping[str, Any]
    ) -> _r.BrandMessageAudiencePossibleResult:
        """발송 예상 모수 확인 (전화번호 명단 기반).

        전화번호 명단으로 동보 발송 가능 예상 수를 조회합니다. 국가코드는 자동 정규화되고 유효한 번호로 모수를 계산합니다. 최소 10건이며, 하나라도 형식이 잘못되면 요청 전체가 거부됩니다. 상태를 바꾸지 않는 조회이므로 재시도해도 안전합니다.

        ``POST /api/comm/v1/center/brandmessage/groupMessage/friend/possible`` (``checkBrandMessageAudiencePossibleByPhoneNumbers``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageAudiencePossibleByPhoneNumbersRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageAudiencePossibleResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_check_brand_message_audience_possible_by_phone_numbers(
            self._transport.call(_call_check_brand_message_audience_possible_by_phone_numbers(body=body))
        )

    def get_friend_count(self, *, sender_key: str) -> _r.BrandMessageAudienceFriendCountResult:
        """채널 전체 친구 수 조회.

        발신프로필 기준 친구 수를 조회합니다. 동보 발송 가능 대상 수를 미리 확인할 때 씁니다.

        ``GET /api/comm/v1/center/brandmessage/groupMessage/friendCount`` (``getBrandMessageFriendCount``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.

        Returns:
            ``BrandMessageAudienceFriendCountResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_friend_count(
            self._transport.call(_call_get_brand_message_friend_count(sender_key=sender_key))
        )

    def estimate(
        self,
        *,
        sender_key: str,
        start_time: dt.datetime | str,
        count: int,
        target: Literal["NONE", "FRIEND_GROUP"] | None = None,
    ) -> _r.BrandMessageAudienceEstimateResult:
        """동보 발송 예상 소요시간 조회.

        동보 발송 시작 시각과 대상 수로 예상 종료 시각과 소요 시간을 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/groupMessage/estimate`` (``estimateBrandMessageGroupSendDuration``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            start_time: 동보 발송 시작 일시(`yyyy-MM-dd'T'HH:mm:ss`, KST)입니다. 동보 발송 요청의 `sendStartAt`(`yyyy-MM-dd HH:mm:ss`)과 형식이 다릅니다.
            count: 발송 모수입니다.
            target: 대상 유형입니다. 기본값은 `NONE`입니다.

        Returns:
            ``BrandMessageAudienceEstimateResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_estimate_brand_message_group_send_duration(
            self._transport.call(
                _call_estimate_brand_message_group_send_duration(
                    sender_key=sender_key, start_time=start_time, count=count, target=target
                )
            )
        )


class AsyncBrandMessageAudience:
    """``client.brand_message.audience`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def check_possible(
        self, *, sender_key: str, msg_type: str, friend_group_key: str | None = None
    ) -> _r.BrandMessageAudiencePossibleResult:
        """발송 예상 모수 확인 (친구 그룹 기반).

        메시지 타입과 친구 그룹 조건으로 동보 발송 예상 발송 수를 조회합니다. 친구 그룹을 쓰면 그룹 상태가 완료이고 등록 유저 수가 10 이상이어야 발송 예약이 가능하며, 친구 관계는 실시간으로 동기화됩니다.

        ``GET /api/comm/v1/center/brandmessage/groupMessage/possible`` (``checkBrandMessageAudiencePossible``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            msg_type: 브랜드메시지 타입입니다(카카오 원본 chatBubbleType으로 변환됩니다). 알려진 값: `FT`, `FI`, `FW`, `FL`, `FC`, `FM`, `FA`, `FP`, `FG`.
            friend_group_key: 대상 친구 그룹 키입니다. 생략하면 전체 친구를 기준으로 조회합니다.

        Returns:
            ``BrandMessageAudiencePossibleResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_check_brand_message_audience_possible(
            await self._transport.call(
                _call_check_brand_message_audience_possible(
                    sender_key=sender_key, msg_type=msg_type, friend_group_key=friend_group_key
                )
            )
        )

    async def check_possible_by_phone_numbers(
        self, body: _q.BrandMessageAudiencePossibleByPhoneNumbersRequest | Mapping[str, Any]
    ) -> _r.BrandMessageAudiencePossibleResult:
        """발송 예상 모수 확인 (전화번호 명단 기반).

        전화번호 명단으로 동보 발송 가능 예상 수를 조회합니다. 국가코드는 자동 정규화되고 유효한 번호로 모수를 계산합니다. 최소 10건이며, 하나라도 형식이 잘못되면 요청 전체가 거부됩니다. 상태를 바꾸지 않는 조회이므로 재시도해도 안전합니다.

        ``POST /api/comm/v1/center/brandmessage/groupMessage/friend/possible`` (``checkBrandMessageAudiencePossibleByPhoneNumbers``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageAudiencePossibleByPhoneNumbersRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageAudiencePossibleResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_check_brand_message_audience_possible_by_phone_numbers(
            await self._transport.call(_call_check_brand_message_audience_possible_by_phone_numbers(body=body))
        )

    async def get_friend_count(self, *, sender_key: str) -> _r.BrandMessageAudienceFriendCountResult:
        """채널 전체 친구 수 조회.

        발신프로필 기준 친구 수를 조회합니다. 동보 발송 가능 대상 수를 미리 확인할 때 씁니다.

        ``GET /api/comm/v1/center/brandmessage/groupMessage/friendCount`` (``getBrandMessageFriendCount``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.

        Returns:
            ``BrandMessageAudienceFriendCountResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_friend_count(
            await self._transport.call(_call_get_brand_message_friend_count(sender_key=sender_key))
        )

    async def estimate(
        self,
        *,
        sender_key: str,
        start_time: dt.datetime | str,
        count: int,
        target: Literal["NONE", "FRIEND_GROUP"] | None = None,
    ) -> _r.BrandMessageAudienceEstimateResult:
        """동보 발송 예상 소요시간 조회.

        동보 발송 시작 시각과 대상 수로 예상 종료 시각과 소요 시간을 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/groupMessage/estimate`` (``estimateBrandMessageGroupSendDuration``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            start_time: 동보 발송 시작 일시(`yyyy-MM-dd'T'HH:mm:ss`, KST)입니다. 동보 발송 요청의 `sendStartAt`(`yyyy-MM-dd HH:mm:ss`)과 형식이 다릅니다.
            count: 발송 모수입니다.
            target: 대상 유형입니다. 기본값은 `NONE`입니다.

        Returns:
            ``BrandMessageAudienceEstimateResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_estimate_brand_message_group_send_duration(
            await self._transport.call(
                _call_estimate_brand_message_group_send_duration(
                    sender_key=sender_key, start_time=start_time, count=count, target=target
                )
            )
        )


class BrandMessagePermissions:
    """``client.brand_message.permissions``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def check(self, *, sender_key: str) -> None:
        """브랜드메시지 발송권한 신청 가능 여부 확인.

        발신프로필이 고객사 회원 대상 발송 권한을 신청할 수 있는 상태인지 확인합니다. `data.code`가 `A000`이면 신청 가능합니다. 고객사 회원 대상 발송(targeting M·N·O)에는 카카오 발송 권한이 필요합니다. 조건: 비즈니스 인증 채널, 등록된 채널 전화번호, 채널 친구 수 5만 이상, 업로드된 광고성 정보 수신동의 증적파일, 3개월 이내 알림톡 발송 이력. 어떤 조건이 미달인지는 응답으로 구분되지 않습니다.

        ``GET /api/comm/v1/center/brandmessage/sendPermission`` (``checkBrandMessageSendPermission``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다. 최대 40자입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_check_brand_message_send_permission(sender_key=sender_key))

    def apply(self, body: _q.BrandMessagePermissionApplyRequest | Mapping[str, Any]) -> None:
        """브랜드메시지 발송권한 신청.

        고객사 회원 대상 발송(targeting M·N·O) 권한을 신청합니다. 권한은 톡채널 단위로 부여되므로 같은 톡채널을 쓰는 다른 딜러사의 발신프로필에도 함께 적용됩니다. 고객사 회원 대상 발송(targeting M·N·O)에는 카카오 발송 권한이 필요합니다. 조건: 비즈니스 인증 채널, 등록된 채널 전화번호, 채널 친구 수 5만 이상, 업로드된 광고성 정보 수신동의 증적파일, 3개월 이내 알림톡 발송 이력. 어떤 조건이 미달인지는 응답으로 구분되지 않습니다.

        ``POST /api/comm/v1/center/brandmessage/sendPermission`` (``applyBrandMessageSendPermission``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessagePermissionApplyRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_apply_brand_message_send_permission(body=body))


class AsyncBrandMessagePermissions:
    """``client.brand_message.permissions`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def check(self, *, sender_key: str) -> None:
        """브랜드메시지 발송권한 신청 가능 여부 확인.

        발신프로필이 고객사 회원 대상 발송 권한을 신청할 수 있는 상태인지 확인합니다. `data.code`가 `A000`이면 신청 가능합니다. 고객사 회원 대상 발송(targeting M·N·O)에는 카카오 발송 권한이 필요합니다. 조건: 비즈니스 인증 채널, 등록된 채널 전화번호, 채널 친구 수 5만 이상, 업로드된 광고성 정보 수신동의 증적파일, 3개월 이내 알림톡 발송 이력. 어떤 조건이 미달인지는 응답으로 구분되지 않습니다.

        ``GET /api/comm/v1/center/brandmessage/sendPermission`` (``checkBrandMessageSendPermission``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다. 최대 40자입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_check_brand_message_send_permission(sender_key=sender_key))

    async def apply(self, body: _q.BrandMessagePermissionApplyRequest | Mapping[str, Any]) -> None:
        """브랜드메시지 발송권한 신청.

        고객사 회원 대상 발송(targeting M·N·O) 권한을 신청합니다. 권한은 톡채널 단위로 부여되므로 같은 톡채널을 쓰는 다른 딜러사의 발신프로필에도 함께 적용됩니다. 고객사 회원 대상 발송(targeting M·N·O)에는 카카오 발송 권한이 필요합니다. 조건: 비즈니스 인증 채널, 등록된 채널 전화번호, 채널 친구 수 5만 이상, 업로드된 광고성 정보 수신동의 증적파일, 3개월 이내 알림톡 발송 이력. 어떤 조건이 미달인지는 응답으로 구분되지 않습니다.

        ``POST /api/comm/v1/center/brandmessage/sendPermission`` (``applyBrandMessageSendPermission``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessagePermissionApplyRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_apply_brand_message_send_permission(body=body))


class BrandMessageVideos:
    """``client.brand_message.videos``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def register_upload(
        self, body: _q.BrandMessageVideoUploadRegisterRequest | Mapping[str, Any]
    ) -> _r.BrandMessageVideoUploadRegisterResult:
        """브랜드메시지 동영상 업로드 등록.

        브랜드메시지에 쓸 동영상의 업로드를 등록하고 카카오 업로드 채널(`vid`, `uploadUrl`, `token`)을 발급받습니다. 파일은 이 API로 보내지 않고 `uploadUrl`로 직접 전송합니다(5분 안에). 전송 후 동영상 조회로 `status`가 `PUBLIC`인지 확인합니다.

        ``POST /api/comm/v1/center/brandmessage/video/upload/register`` (``registerBrandMessageVideoUpload``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageVideoUploadRegisterRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageVideoUploadRegisterResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_register_brand_message_video_upload(
            self._transport.call(_call_register_brand_message_video_upload(body=body))
        )

    def register_existing(
        self, body: _q.BrandMessageVideoRegisterRequest | Mapping[str, Any]
    ) -> _r.BrandMessageVideoInfoResult:
        """브랜드메시지 기존 동영상 등록.

        카카오톡 채널에 이미 올라가 있는 동영상을 재업로드 없이 브랜드메시지 발송용으로 등록합니다. `vid` 또는 `videoUrl` 중 하나만 지정합니다.

        ``POST /api/comm/v1/center/brandmessage/video/register`` (``registerBrandMessageExistingVideo``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageVideoRegisterRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageVideoInfoResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_register_brand_message_existing_video(
            self._transport.call(_call_register_brand_message_existing_video(body=body))
        )

    def get(self, *, vid: str, sender_key: str) -> _r.BrandMessageVideoInfoResult:
        """브랜드메시지 동영상 조회.

        동영상 식별자로 업로드된 동영상 한 건의 처리 상태와 메타 정보를 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/video`` (``getBrandMessageVideo``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            vid: 조회할 동영상 식별자입니다.
            sender_key: 발신프로필 키입니다. 최대 40자입니다.

        Returns:
            ``BrandMessageVideoInfoResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_video(
            self._transport.call(_call_get_brand_message_video(vid=vid, sender_key=sender_key))
        )

    def list(
        self, *, sender_key: str, date: dt.date | str | None = None, offset: int | None = None, limit: int | None = None
    ) -> _r.BrandMessageVideoListResult:
        """브랜드메시지 동영상 목록 조회.

        발신프로필 기준으로 업로드한 동영상 이력을 조회합니다. 등록일자로 거르고 `offset`·`limit`으로 페이징합니다.

        ``GET /api/comm/v1/center/brandmessage/video/list`` (``listBrandMessageVideos``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다. 최대 40자입니다.
            date: 조회할 등록일자(`yyyyMMdd`)입니다. 생략하면 전체를 조회합니다.
            offset: 조회 시작 위치입니다. 음수는 쓸 수 없습니다. 기본값은 0입니다.
            limit: 조회 건수입니다. 기본값 100, 최대 1,000입니다.

        Returns:
            ``BrandMessageVideoListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_brand_message_videos(
            self._transport.call(
                _call_list_brand_message_videos(sender_key=sender_key, date=date, offset=offset, limit=limit)
            )
        )

    def iter_list(
        self, *, sender_key: str, date: dt.date | str | None = None, limit: int | None = None
    ) -> Iterator[_r.BrandMessageVideoListEntry]:
        """Iterate over every page of :meth:`list` (``listBrandMessageVideos``, offset pagination)."""

        def fetch(position: Any) -> Any:
            body = self._transport.call(
                _call_list_brand_message_videos(sender_key=sender_key, date=date, limit=limit, offset=position)
            )
            return validate(_r.BrandMessageVideoListResponse, body, "listBrandMessageVideos")

        return iterate(fetch, _PAGE_LIST_BRAND_MESSAGE_VIDEOS, size=limit, start=0)


class AsyncBrandMessageVideos:
    """``client.brand_message.videos`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def register_upload(
        self, body: _q.BrandMessageVideoUploadRegisterRequest | Mapping[str, Any]
    ) -> _r.BrandMessageVideoUploadRegisterResult:
        """브랜드메시지 동영상 업로드 등록.

        브랜드메시지에 쓸 동영상의 업로드를 등록하고 카카오 업로드 채널(`vid`, `uploadUrl`, `token`)을 발급받습니다. 파일은 이 API로 보내지 않고 `uploadUrl`로 직접 전송합니다(5분 안에). 전송 후 동영상 조회로 `status`가 `PUBLIC`인지 확인합니다.

        ``POST /api/comm/v1/center/brandmessage/video/upload/register`` (``registerBrandMessageVideoUpload``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageVideoUploadRegisterRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageVideoUploadRegisterResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_register_brand_message_video_upload(
            await self._transport.call(_call_register_brand_message_video_upload(body=body))
        )

    async def register_existing(
        self, body: _q.BrandMessageVideoRegisterRequest | Mapping[str, Any]
    ) -> _r.BrandMessageVideoInfoResult:
        """브랜드메시지 기존 동영상 등록.

        카카오톡 채널에 이미 올라가 있는 동영상을 재업로드 없이 브랜드메시지 발송용으로 등록합니다. `vid` 또는 `videoUrl` 중 하나만 지정합니다.

        ``POST /api/comm/v1/center/brandmessage/video/register`` (``registerBrandMessageExistingVideo``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageVideoRegisterRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageVideoInfoResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_register_brand_message_existing_video(
            await self._transport.call(_call_register_brand_message_existing_video(body=body))
        )

    async def get(self, *, vid: str, sender_key: str) -> _r.BrandMessageVideoInfoResult:
        """브랜드메시지 동영상 조회.

        동영상 식별자로 업로드된 동영상 한 건의 처리 상태와 메타 정보를 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/video`` (``getBrandMessageVideo``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            vid: 조회할 동영상 식별자입니다.
            sender_key: 발신프로필 키입니다. 최대 40자입니다.

        Returns:
            ``BrandMessageVideoInfoResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_video(
            await self._transport.call(_call_get_brand_message_video(vid=vid, sender_key=sender_key))
        )

    async def list(
        self, *, sender_key: str, date: dt.date | str | None = None, offset: int | None = None, limit: int | None = None
    ) -> _r.BrandMessageVideoListResult:
        """브랜드메시지 동영상 목록 조회.

        발신프로필 기준으로 업로드한 동영상 이력을 조회합니다. 등록일자로 거르고 `offset`·`limit`으로 페이징합니다.

        ``GET /api/comm/v1/center/brandmessage/video/list`` (``listBrandMessageVideos``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다. 최대 40자입니다.
            date: 조회할 등록일자(`yyyyMMdd`)입니다. 생략하면 전체를 조회합니다.
            offset: 조회 시작 위치입니다. 음수는 쓸 수 없습니다. 기본값은 0입니다.
            limit: 조회 건수입니다. 기본값 100, 최대 1,000입니다.

        Returns:
            ``BrandMessageVideoListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_brand_message_videos(
            await self._transport.call(
                _call_list_brand_message_videos(sender_key=sender_key, date=date, offset=offset, limit=limit)
            )
        )

    def iter_list(
        self, *, sender_key: str, date: dt.date | str | None = None, limit: int | None = None
    ) -> AsyncIterator[_r.BrandMessageVideoListEntry]:
        """Iterate over every page of :meth:`list` (``listBrandMessageVideos``, offset pagination)."""

        async def fetch(position: Any) -> Any:
            body = await self._transport.call(
                _call_list_brand_message_videos(sender_key=sender_key, date=date, limit=limit, offset=position)
            )
            return validate(_r.BrandMessageVideoListResponse, body, "listBrandMessageVideos")

        return aiterate(fetch, _PAGE_LIST_BRAND_MESSAGE_VIDEOS, size=limit, start=0)


class BrandMessageTemplates:
    """``client.brand_message.templates``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get(
        self, *, sender_key: str, template_code: str, send_type: Literal["basic", "free"] | None = None
    ) -> _r.BrandMessageTemplateResult:
        """브랜드메시지 템플릿 조회.

        발신프로필 키와 템플릿 코드로 브랜드메시지 템플릿 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/template`` (``getBrandMessageTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            template_code: 템플릿 코드입니다.
            send_type: 브랜드메시지 발송 타입입니다. `basic`(기본형) 또는 `free`(자유형)입니다.

        Returns:
            ``BrandMessageTemplateResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_template(
            self._transport.call(
                _call_get_brand_message_template(
                    sender_key=sender_key, template_code=template_code, send_type=send_type
                )
            )
        )

    def create(self, body: _q.BrandMessageTemplateRequest | Mapping[str, Any]) -> _r.BrandMessageTemplateResult:
        """브랜드메시지 템플릿 등록.

        브랜드메시지 템플릿을 등록합니다. 이미지가 필요한 유형은 이미지 업로드 API로 발급받은 `imgUrl`을 함께 씁니다.

        ``POST /api/comm/v1/center/brandmessage/template`` (``createBrandMessageTemplate``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageTemplateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageTemplateResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_brand_message_template(
            self._transport.call(_call_create_brand_message_template(body=body))
        )

    def update(self, body: _q.BrandMessageTemplateRequest | Mapping[str, Any]) -> _r.BrandMessageTemplateResult:
        """브랜드메시지 템플릿 수정.

        등록된 브랜드메시지 템플릿을 수정합니다. 검수 상태와 카카오 정책에 따라 수정 가능한 범위가 달라질 수 있습니다.

        ``PUT /api/comm/v1/center/brandmessage/template`` (``updateBrandMessageTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageTemplateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageTemplateResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_update_brand_message_template(
            self._transport.call(_call_update_brand_message_template(body=body))
        )

    def list(
        self,
        *,
        sender_key: str,
        sender_key_type: str | None = None,
        status: str | None = None,
        template_type: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> _r.BrandMessageTemplateListResult:
        """브랜드메시지 템플릿 목록 조회.

        발신프로필(또는 그룹키)에 등록된 브랜드메시지 템플릿 목록을 페이징 조회합니다. 카카오를 호출하지 않고 비즈고에 적재된 템플릿을 읽으므로 목록 화면이나 주기적인 동기화에 쓸 수 있습니다.

        ``GET /api/comm/v1/center/brandmessage/template/list`` (``listBrandMessageTemplates``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키 또는 그룹키입니다.
            sender_key_type: 발신키 유형입니다. 문서 예시 값은 `S`(발신프로필)입니다. 기본값은 `S`입니다.
            status: 템플릿 상태입니다. 알려진 값: `A`(등록), `S`(차단).
            template_type: 템플릿 유형입니다.
            offset: 조회 시작 위치입니다.
            limit: 조회 건수입니다.

        Returns:
            ``BrandMessageTemplateListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_brand_message_templates(
            self._transport.call(
                _call_list_brand_message_templates(
                    sender_key=sender_key,
                    sender_key_type=sender_key_type,
                    status=status,
                    template_type=template_type,
                    offset=offset,
                    limit=limit,
                )
            )
        )

    def iter_list(
        self,
        *,
        sender_key: str,
        sender_key_type: str | None = None,
        status: str | None = None,
        template_type: str | None = None,
        limit: int | None = None,
    ) -> Iterator[_r.BrandMessageTemplateSummary]:
        """Iterate over every page of :meth:`list` (``listBrandMessageTemplates``, offset pagination)."""

        def fetch(position: Any) -> Any:
            body = self._transport.call(
                _call_list_brand_message_templates(
                    sender_key=sender_key,
                    sender_key_type=sender_key_type,
                    status=status,
                    template_type=template_type,
                    limit=limit,
                    offset=position,
                )
            )
            return validate(_r.BrandMessageTemplateListResponse, body, "listBrandMessageTemplates")

        return iterate(fetch, _PAGE_LIST_BRAND_MESSAGE_TEMPLATES, size=limit, start=None)

    def list_last_modified(
        self,
        *,
        sender_key: str,
        sender_key_type: str | None = None,
        since: dt.datetime | str | None = None,
        page: int | None = None,
        count: int | None = None,
    ) -> _r.BrandMessageTemplateListResult:
        """최근 변경 브랜드메시지 템플릿 조회.

        지정한 시각 이후 변경된 브랜드메시지 템플릿 목록을 조회합니다. 템플릿 최신화나 내부 동기화 배치에 씁니다.

        ``GET /api/comm/v1/center/brandmessage/template/lastModified`` (``listBrandMessageTemplatesLastModified``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다. 최대 40자입니다.
            sender_key_type: 발신키 유형입니다. 문서 예시 값은 `S`(발신프로필)입니다. 기본값은 `S`입니다.
            since: 조회 시작 시각(`yyyy-MM-dd'T'HH:mm:ss`)입니다.
            page: 페이지 번호입니다. 기본값 1, 최소 1입니다.
            count: 페이지당 조회 건수입니다. 기본값 100, 최소 1입니다.

        Returns:
            ``BrandMessageTemplateListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_brand_message_templates_last_modified(
            self._transport.call(
                _call_list_brand_message_templates_last_modified(
                    sender_key=sender_key, sender_key_type=sender_key_type, since=since, page=page, count=count
                )
            )
        )

    def iter_list_last_modified(
        self,
        *,
        sender_key: str,
        sender_key_type: str | None = None,
        since: dt.datetime | str | None = None,
        count: int | None = None,
    ) -> Iterator[_r.BrandMessageTemplateSummary]:
        """Iterate over every page of :meth:`list_last_modified` (``listBrandMessageTemplatesLastModified``, page pagination)."""

        def fetch(position: Any) -> Any:
            body = self._transport.call(
                _call_list_brand_message_templates_last_modified(
                    sender_key=sender_key, sender_key_type=sender_key_type, since=since, count=count, page=position
                )
            )
            return validate(_r.BrandMessageTemplateListResponse, body, "listBrandMessageTemplatesLastModified")

        return iterate(fetch, _PAGE_LIST_BRAND_MESSAGE_TEMPLATES_LAST_MODIFIED, size=count, start=1)

    def delete(self, sender_key: str, template_code: str) -> None:
        """브랜드메시지 템플릿 삭제.

        발신프로필 키와 템플릿 코드로 브랜드메시지 템플릿을 삭제합니다.

        ``DELETE /api/comm/v1/center/brandmessage/template/senderKey/{senderKey}/templateCode/{templateCode}`` (``deleteBrandMessageTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            template_code: 삭제할 템플릿 코드입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_delete_brand_message_template(sender_key=sender_key, template_code=template_code))


class AsyncBrandMessageTemplates:
    """``client.brand_message.templates`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get(
        self, *, sender_key: str, template_code: str, send_type: Literal["basic", "free"] | None = None
    ) -> _r.BrandMessageTemplateResult:
        """브랜드메시지 템플릿 조회.

        발신프로필 키와 템플릿 코드로 브랜드메시지 템플릿 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/template`` (``getBrandMessageTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            template_code: 템플릿 코드입니다.
            send_type: 브랜드메시지 발송 타입입니다. `basic`(기본형) 또는 `free`(자유형)입니다.

        Returns:
            ``BrandMessageTemplateResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_template(
            await self._transport.call(
                _call_get_brand_message_template(
                    sender_key=sender_key, template_code=template_code, send_type=send_type
                )
            )
        )

    async def create(self, body: _q.BrandMessageTemplateRequest | Mapping[str, Any]) -> _r.BrandMessageTemplateResult:
        """브랜드메시지 템플릿 등록.

        브랜드메시지 템플릿을 등록합니다. 이미지가 필요한 유형은 이미지 업로드 API로 발급받은 `imgUrl`을 함께 씁니다.

        ``POST /api/comm/v1/center/brandmessage/template`` (``createBrandMessageTemplate``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageTemplateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageTemplateResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_brand_message_template(
            await self._transport.call(_call_create_brand_message_template(body=body))
        )

    async def update(self, body: _q.BrandMessageTemplateRequest | Mapping[str, Any]) -> _r.BrandMessageTemplateResult:
        """브랜드메시지 템플릿 수정.

        등록된 브랜드메시지 템플릿을 수정합니다. 검수 상태와 카카오 정책에 따라 수정 가능한 범위가 달라질 수 있습니다.

        ``PUT /api/comm/v1/center/brandmessage/template`` (``updateBrandMessageTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageTemplateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageTemplateResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_update_brand_message_template(
            await self._transport.call(_call_update_brand_message_template(body=body))
        )

    async def list(
        self,
        *,
        sender_key: str,
        sender_key_type: str | None = None,
        status: str | None = None,
        template_type: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> _r.BrandMessageTemplateListResult:
        """브랜드메시지 템플릿 목록 조회.

        발신프로필(또는 그룹키)에 등록된 브랜드메시지 템플릿 목록을 페이징 조회합니다. 카카오를 호출하지 않고 비즈고에 적재된 템플릿을 읽으므로 목록 화면이나 주기적인 동기화에 쓸 수 있습니다.

        ``GET /api/comm/v1/center/brandmessage/template/list`` (``listBrandMessageTemplates``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키 또는 그룹키입니다.
            sender_key_type: 발신키 유형입니다. 문서 예시 값은 `S`(발신프로필)입니다. 기본값은 `S`입니다.
            status: 템플릿 상태입니다. 알려진 값: `A`(등록), `S`(차단).
            template_type: 템플릿 유형입니다.
            offset: 조회 시작 위치입니다.
            limit: 조회 건수입니다.

        Returns:
            ``BrandMessageTemplateListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_brand_message_templates(
            await self._transport.call(
                _call_list_brand_message_templates(
                    sender_key=sender_key,
                    sender_key_type=sender_key_type,
                    status=status,
                    template_type=template_type,
                    offset=offset,
                    limit=limit,
                )
            )
        )

    def iter_list(
        self,
        *,
        sender_key: str,
        sender_key_type: str | None = None,
        status: str | None = None,
        template_type: str | None = None,
        limit: int | None = None,
    ) -> AsyncIterator[_r.BrandMessageTemplateSummary]:
        """Iterate over every page of :meth:`list` (``listBrandMessageTemplates``, offset pagination)."""

        async def fetch(position: Any) -> Any:
            body = await self._transport.call(
                _call_list_brand_message_templates(
                    sender_key=sender_key,
                    sender_key_type=sender_key_type,
                    status=status,
                    template_type=template_type,
                    limit=limit,
                    offset=position,
                )
            )
            return validate(_r.BrandMessageTemplateListResponse, body, "listBrandMessageTemplates")

        return aiterate(fetch, _PAGE_LIST_BRAND_MESSAGE_TEMPLATES, size=limit, start=None)

    async def list_last_modified(
        self,
        *,
        sender_key: str,
        sender_key_type: str | None = None,
        since: dt.datetime | str | None = None,
        page: int | None = None,
        count: int | None = None,
    ) -> _r.BrandMessageTemplateListResult:
        """최근 변경 브랜드메시지 템플릿 조회.

        지정한 시각 이후 변경된 브랜드메시지 템플릿 목록을 조회합니다. 템플릿 최신화나 내부 동기화 배치에 씁니다.

        ``GET /api/comm/v1/center/brandmessage/template/lastModified`` (``listBrandMessageTemplatesLastModified``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다. 최대 40자입니다.
            sender_key_type: 발신키 유형입니다. 문서 예시 값은 `S`(발신프로필)입니다. 기본값은 `S`입니다.
            since: 조회 시작 시각(`yyyy-MM-dd'T'HH:mm:ss`)입니다.
            page: 페이지 번호입니다. 기본값 1, 최소 1입니다.
            count: 페이지당 조회 건수입니다. 기본값 100, 최소 1입니다.

        Returns:
            ``BrandMessageTemplateListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_brand_message_templates_last_modified(
            await self._transport.call(
                _call_list_brand_message_templates_last_modified(
                    sender_key=sender_key, sender_key_type=sender_key_type, since=since, page=page, count=count
                )
            )
        )

    def iter_list_last_modified(
        self,
        *,
        sender_key: str,
        sender_key_type: str | None = None,
        since: dt.datetime | str | None = None,
        count: int | None = None,
    ) -> AsyncIterator[_r.BrandMessageTemplateSummary]:
        """Iterate over every page of :meth:`list_last_modified` (``listBrandMessageTemplatesLastModified``, page pagination)."""

        async def fetch(position: Any) -> Any:
            body = await self._transport.call(
                _call_list_brand_message_templates_last_modified(
                    sender_key=sender_key, sender_key_type=sender_key_type, since=since, count=count, page=position
                )
            )
            return validate(_r.BrandMessageTemplateListResponse, body, "listBrandMessageTemplatesLastModified")

        return aiterate(fetch, _PAGE_LIST_BRAND_MESSAGE_TEMPLATES_LAST_MODIFIED, size=count, start=1)

    async def delete(self, sender_key: str, template_code: str) -> None:
        """브랜드메시지 템플릿 삭제.

        발신프로필 키와 템플릿 코드로 브랜드메시지 템플릿을 삭제합니다.

        ``DELETE /api/comm/v1/center/brandmessage/template/senderKey/{senderKey}/templateCode/{templateCode}`` (``deleteBrandMessageTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            template_code: 삭제할 템플릿 코드입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(
            _call_delete_brand_message_template(sender_key=sender_key, template_code=template_code)
        )


class BrandMessageGroupTags:
    """``client.brand_message.group_tags``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(self, *, sender_key: str) -> _r.BrandMessageGroupTagListResult:
        """브랜드메시지 전체 그룹태그 조회.

        발신프로필 키로 브랜드메시지 전체 그룹태그 목록을 조회합니다. 그룹태그 키는 자유형 발송의 `groupTagKey`에 씁니다.

        ``GET /api/comm/v1/center/brandmessage/groupTag/list`` (``listBrandMessageGroupTags``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.

        Returns:
            ``BrandMessageGroupTagListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_brand_message_group_tags(
            self._transport.call(_call_list_brand_message_group_tags(sender_key=sender_key))
        )

    def get(self, *, sender_key: str, group_tag_key: str) -> _r.BrandMessageGroupTagListResult:
        """브랜드메시지 그룹태그 조회.

        발신프로필 키와 그룹태그 키로 그룹태그 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/groupTag`` (``getBrandMessageGroupTag``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            group_tag_key: 그룹태그 키입니다.

        Returns:
            ``BrandMessageGroupTagListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_group_tag(
            self._transport.call(_call_get_brand_message_group_tag(sender_key=sender_key, group_tag_key=group_tag_key))
        )

    def create(self, body: _q.BrandMessageGroupTagRequest | Mapping[str, Any]) -> _r.BrandMessageGroupTagListResult:
        """브랜드메시지 그룹태그 등록.

        브랜드메시지 그룹태그를 등록합니다.

        ``POST /api/comm/v1/center/brandmessage/groupTag`` (``createBrandMessageGroupTag``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageGroupTagRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageGroupTagListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_brand_message_group_tag(
            self._transport.call(_call_create_brand_message_group_tag(body=body))
        )

    def update(self, body: _q.BrandMessageGroupTagRequest | Mapping[str, Any]) -> _r.BrandMessageGroupTagListResult:
        """브랜드메시지 그룹태그 수정.

        등록된 브랜드메시지 그룹태그 정보를 수정합니다.

        ``PUT /api/comm/v1/center/brandmessage/groupTag`` (``updateBrandMessageGroupTag``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageGroupTagRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageGroupTagListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_update_brand_message_group_tag(
            self._transport.call(_call_update_brand_message_group_tag(body=body))
        )

    def delete(self, sender_key: str, group_tag_key: str) -> None:
        """브랜드메시지 그룹태그 삭제.

        발신프로필 키와 그룹태그 키로 그룹태그를 삭제합니다.

        ``DELETE /api/comm/v1/center/brandmessage/groupTag/senderKey/{senderKey}/groupTagKey/{groupTagKey}`` (``deleteBrandMessageGroupTag``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            group_tag_key: 삭제할 그룹태그 키입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_delete_brand_message_group_tag(sender_key=sender_key, group_tag_key=group_tag_key))


class AsyncBrandMessageGroupTags:
    """``client.brand_message.group_tags`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(self, *, sender_key: str) -> _r.BrandMessageGroupTagListResult:
        """브랜드메시지 전체 그룹태그 조회.

        발신프로필 키로 브랜드메시지 전체 그룹태그 목록을 조회합니다. 그룹태그 키는 자유형 발송의 `groupTagKey`에 씁니다.

        ``GET /api/comm/v1/center/brandmessage/groupTag/list`` (``listBrandMessageGroupTags``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.

        Returns:
            ``BrandMessageGroupTagListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_brand_message_group_tags(
            await self._transport.call(_call_list_brand_message_group_tags(sender_key=sender_key))
        )

    async def get(self, *, sender_key: str, group_tag_key: str) -> _r.BrandMessageGroupTagListResult:
        """브랜드메시지 그룹태그 조회.

        발신프로필 키와 그룹태그 키로 그룹태그 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/groupTag`` (``getBrandMessageGroupTag``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            group_tag_key: 그룹태그 키입니다.

        Returns:
            ``BrandMessageGroupTagListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_group_tag(
            await self._transport.call(
                _call_get_brand_message_group_tag(sender_key=sender_key, group_tag_key=group_tag_key)
            )
        )

    async def create(
        self, body: _q.BrandMessageGroupTagRequest | Mapping[str, Any]
    ) -> _r.BrandMessageGroupTagListResult:
        """브랜드메시지 그룹태그 등록.

        브랜드메시지 그룹태그를 등록합니다.

        ``POST /api/comm/v1/center/brandmessage/groupTag`` (``createBrandMessageGroupTag``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageGroupTagRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageGroupTagListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_brand_message_group_tag(
            await self._transport.call(_call_create_brand_message_group_tag(body=body))
        )

    async def update(
        self, body: _q.BrandMessageGroupTagRequest | Mapping[str, Any]
    ) -> _r.BrandMessageGroupTagListResult:
        """브랜드메시지 그룹태그 수정.

        등록된 브랜드메시지 그룹태그 정보를 수정합니다.

        ``PUT /api/comm/v1/center/brandmessage/groupTag`` (``updateBrandMessageGroupTag``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageGroupTagRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageGroupTagListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_update_brand_message_group_tag(
            await self._transport.call(_call_update_brand_message_group_tag(body=body))
        )

    async def delete(self, sender_key: str, group_tag_key: str) -> None:
        """브랜드메시지 그룹태그 삭제.

        발신프로필 키와 그룹태그 키로 그룹태그를 삭제합니다.

        ``DELETE /api/comm/v1/center/brandmessage/groupTag/senderKey/{senderKey}/groupTagKey/{groupTagKey}`` (``deleteBrandMessageGroupTag``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            group_tag_key: 삭제할 그룹태그 키입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(
            _call_delete_brand_message_group_tag(sender_key=sender_key, group_tag_key=group_tag_key)
        )


class BrandMessageFriendGroups:
    """``client.brand_message.friend_groups``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def upload_file(
        self, file: FileInput, *, sender_key: str, filename: str | None = None
    ) -> _r.BrandMessageFriendGroupFileUploadResult:
        """친구 그룹 파일 업로드.

        전화번호 목록 파일(txt, csv)을 업로드해 친구 그룹 등록 또는 전화번호 추가·삭제에 쓸 임시 파일 키를 발급받습니다.

        ``POST /api/comm/v1/center/brandmessage/friendGroup/file`` (``uploadBrandMessageFriendGroupFile``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            file: 업로드할 전화번호 목록 파일입니다. 줄바꿈으로 구분한 전화번호 파일이며 txt, csv만 허용됩니다.

        Returns:
            ``BrandMessageFriendGroupFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_friend_group_file(
            self._transport.call(
                _call_upload_brand_message_friend_group_file(file=file, sender_key=sender_key, filename=filename)
            )
        )

    def create(
        self, body: _q.BrandMessageFriendGroupRequest | Mapping[str, Any]
    ) -> _r.BrandMessageFriendGroupProcessingResult:
        """친구 그룹 등록.

        친구 그룹을 생성합니다. `fileKey` 또는 `phoneNumbers`로 그룹에 넣을 전화번호를 함께 등록할 수 있습니다. 처리는 비동기이며 응답의 `status`는 `IN_PROGRESS`일 수 있습니다.

        ``POST /api/comm/v1/center/brandmessage/friendGroup`` (``createBrandMessageFriendGroup``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageFriendGroupRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageFriendGroupProcessingResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_brand_message_friend_group(
            self._transport.call(_call_create_brand_message_friend_group(body=body))
        )

    def get(self, *, sender_key: str, friend_group_key: str) -> _r.BrandMessageFriendGroupResult:
        """친구 그룹 조회.

        발신프로필 키와 친구 그룹 키로 친구 그룹 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/friendGroup`` (``getBrandMessageFriendGroup``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            friend_group_key: 친구 그룹 키입니다.

        Returns:
            ``BrandMessageFriendGroupResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_friend_group(
            self._transport.call(
                _call_get_brand_message_friend_group(sender_key=sender_key, friend_group_key=friend_group_key)
            )
        )

    def list(self, *, sender_key: str) -> _r.BrandMessageFriendGroupListResult:
        """친구 그룹 목록 조회.

        발신프로필 기준으로 등록된 친구 그룹 목록을 조회합니다. 문서에 페이징 파라미터가 없습니다.

        ``GET /api/comm/v1/center/brandmessage/friendGroup/list`` (``listBrandMessageFriendGroups``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.

        Returns:
            ``BrandMessageFriendGroupListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_brand_message_friend_groups(
            self._transport.call(_call_list_brand_message_friend_groups(sender_key=sender_key))
        )

    def delete(self, sender_key: str, friend_group_key: str) -> None:
        """친구 그룹 삭제.

        발신프로필 키와 친구 그룹 키로 친구 그룹을 삭제합니다.

        ``DELETE /api/comm/v1/center/brandmessage/friendGroup/senderKey/{senderKey}/friendGroupKey/{friendGroupKey}`` (``deleteBrandMessageFriendGroup``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            friend_group_key: 삭제할 친구 그룹 키입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(
            _call_delete_brand_message_friend_group(sender_key=sender_key, friend_group_key=friend_group_key)
        )

    def add_phone_numbers(
        self, body: _q.BrandMessageFriendGroupRequest | Mapping[str, Any]
    ) -> _r.BrandMessageFriendGroupProcessingResult:
        """친구 그룹 내 전화번호 추가.

        기존 친구 그룹에 전화번호를 추가합니다. `fileKey` 또는 `phoneNumbers`로 입력합니다. 처리는 비동기이며 진행 상황은 전화번호 요청 조회로 확인합니다.

        ``POST /api/comm/v1/center/brandmessage/friendGroup/phoneNumber/update`` (``addBrandMessageFriendGroupPhoneNumbers``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageFriendGroupRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageFriendGroupProcessingResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_add_brand_message_friend_group_phone_numbers(
            self._transport.call(_call_add_brand_message_friend_group_phone_numbers(body=body))
        )

    def delete_phone_numbers(
        self, body: _q.BrandMessageFriendGroupRequest | Mapping[str, Any]
    ) -> _r.BrandMessageFriendGroupProcessingResult:
        """친구 그룹 내 전화번호 삭제.

        기존 친구 그룹에서 전화번호를 삭제합니다. `fileKey` 또는 `phoneNumbers`로 입력합니다. 처리는 비동기이며 진행 상황은 전화번호 요청 조회로 확인합니다.

        ``POST /api/comm/v1/center/brandmessage/friendGroup/phoneNumber/delete`` (``deleteBrandMessageFriendGroupPhoneNumbers``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageFriendGroupRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageFriendGroupProcessingResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_delete_brand_message_friend_group_phone_numbers(
            self._transport.call(_call_delete_brand_message_friend_group_phone_numbers(body=body))
        )

    def list_phone_number_requests(
        self, *, sender_key: str, friend_group_key: str, last_request_id: str | None = None, count: int | None = None
    ) -> _r.BrandMessageFriendGroupPhoneNumberRequestListResult:
        """친구 그룹 전화번호 요청 목록 조회.

        친구 그룹 전화번호 추가·삭제 요청의 처리 상태를 목록으로 조회합니다. 다음 페이지는 이전 응답의 마지막 항목 `requestId`를 `lastRequestId`로 넘겨 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/friendGroup/phoneNumber/requests`` (``listBrandMessageFriendGroupPhoneNumberRequests``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            friend_group_key: 친구 그룹 키입니다.
            last_request_id: 이전 페이지의 마지막 요청 아이디입니다.
            count: 조회 건수입니다.

        Returns:
            ``BrandMessageFriendGroupPhoneNumberRequestListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_brand_message_friend_group_phone_number_requests(
            self._transport.call(
                _call_list_brand_message_friend_group_phone_number_requests(
                    sender_key=sender_key,
                    friend_group_key=friend_group_key,
                    last_request_id=last_request_id,
                    count=count,
                )
            )
        )

    def iter_list_phone_number_requests(
        self, *, sender_key: str, friend_group_key: str, count: int | None = None
    ) -> Iterator[_r.BrandMessageFriendGroupPhoneNumberRequest]:
        """Iterate over every page of :meth:`list_phone_number_requests` (``listBrandMessageFriendGroupPhoneNumberRequests``, cursor pagination)."""

        def fetch(position: Any) -> Any:
            body = self._transport.call(
                _call_list_brand_message_friend_group_phone_number_requests(
                    sender_key=sender_key, friend_group_key=friend_group_key, count=count, last_request_id=position
                )
            )
            return validate(
                _r.BrandMessageFriendGroupPhoneNumberRequestListResponse,
                body,
                "listBrandMessageFriendGroupPhoneNumberRequests",
            )

        return iterate(fetch, _PAGE_LIST_BRAND_MESSAGE_FRIEND_GROUP_PHONE_NUMBER_REQUESTS, size=None, start=None)

    def get_phone_number_request(
        self, *, sender_key: str, friend_group_key: str, request_id: str
    ) -> _r.BrandMessageFriendGroupPhoneNumberRequestResult:
        """친구 그룹 전화번호 요청 단건 조회.

        전화번호 추가·삭제 응답으로 받은 `requestId`로 해당 요청의 처리 상태를 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/friendGroup/phoneNumber/request`` (``getBrandMessageFriendGroupPhoneNumberRequest``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            friend_group_key: 친구 그룹 키입니다.
            request_id: 조회할 요청 아이디입니다.

        Returns:
            ``BrandMessageFriendGroupPhoneNumberRequestResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_friend_group_phone_number_request(
            self._transport.call(
                _call_get_brand_message_friend_group_phone_number_request(
                    sender_key=sender_key, friend_group_key=friend_group_key, request_id=request_id
                )
            )
        )


class AsyncBrandMessageFriendGroups:
    """``client.brand_message.friend_groups`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def upload_file(
        self, file: FileInput, *, sender_key: str, filename: str | None = None
    ) -> _r.BrandMessageFriendGroupFileUploadResult:
        """친구 그룹 파일 업로드.

        전화번호 목록 파일(txt, csv)을 업로드해 친구 그룹 등록 또는 전화번호 추가·삭제에 쓸 임시 파일 키를 발급받습니다.

        ``POST /api/comm/v1/center/brandmessage/friendGroup/file`` (``uploadBrandMessageFriendGroupFile``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            file: 업로드할 전화번호 목록 파일입니다. 줄바꿈으로 구분한 전화번호 파일이며 txt, csv만 허용됩니다.

        Returns:
            ``BrandMessageFriendGroupFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_friend_group_file(
            await self._transport.call(
                _call_upload_brand_message_friend_group_file(file=file, sender_key=sender_key, filename=filename)
            )
        )

    async def create(
        self, body: _q.BrandMessageFriendGroupRequest | Mapping[str, Any]
    ) -> _r.BrandMessageFriendGroupProcessingResult:
        """친구 그룹 등록.

        친구 그룹을 생성합니다. `fileKey` 또는 `phoneNumbers`로 그룹에 넣을 전화번호를 함께 등록할 수 있습니다. 처리는 비동기이며 응답의 `status`는 `IN_PROGRESS`일 수 있습니다.

        ``POST /api/comm/v1/center/brandmessage/friendGroup`` (``createBrandMessageFriendGroup``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageFriendGroupRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageFriendGroupProcessingResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_brand_message_friend_group(
            await self._transport.call(_call_create_brand_message_friend_group(body=body))
        )

    async def get(self, *, sender_key: str, friend_group_key: str) -> _r.BrandMessageFriendGroupResult:
        """친구 그룹 조회.

        발신프로필 키와 친구 그룹 키로 친구 그룹 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/friendGroup`` (``getBrandMessageFriendGroup``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            friend_group_key: 친구 그룹 키입니다.

        Returns:
            ``BrandMessageFriendGroupResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_friend_group(
            await self._transport.call(
                _call_get_brand_message_friend_group(sender_key=sender_key, friend_group_key=friend_group_key)
            )
        )

    async def list(self, *, sender_key: str) -> _r.BrandMessageFriendGroupListResult:
        """친구 그룹 목록 조회.

        발신프로필 기준으로 등록된 친구 그룹 목록을 조회합니다. 문서에 페이징 파라미터가 없습니다.

        ``GET /api/comm/v1/center/brandmessage/friendGroup/list`` (``listBrandMessageFriendGroups``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.

        Returns:
            ``BrandMessageFriendGroupListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_brand_message_friend_groups(
            await self._transport.call(_call_list_brand_message_friend_groups(sender_key=sender_key))
        )

    async def delete(self, sender_key: str, friend_group_key: str) -> None:
        """친구 그룹 삭제.

        발신프로필 키와 친구 그룹 키로 친구 그룹을 삭제합니다.

        ``DELETE /api/comm/v1/center/brandmessage/friendGroup/senderKey/{senderKey}/friendGroupKey/{friendGroupKey}`` (``deleteBrandMessageFriendGroup``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            friend_group_key: 삭제할 친구 그룹 키입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(
            _call_delete_brand_message_friend_group(sender_key=sender_key, friend_group_key=friend_group_key)
        )

    async def add_phone_numbers(
        self, body: _q.BrandMessageFriendGroupRequest | Mapping[str, Any]
    ) -> _r.BrandMessageFriendGroupProcessingResult:
        """친구 그룹 내 전화번호 추가.

        기존 친구 그룹에 전화번호를 추가합니다. `fileKey` 또는 `phoneNumbers`로 입력합니다. 처리는 비동기이며 진행 상황은 전화번호 요청 조회로 확인합니다.

        ``POST /api/comm/v1/center/brandmessage/friendGroup/phoneNumber/update`` (``addBrandMessageFriendGroupPhoneNumbers``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageFriendGroupRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageFriendGroupProcessingResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_add_brand_message_friend_group_phone_numbers(
            await self._transport.call(_call_add_brand_message_friend_group_phone_numbers(body=body))
        )

    async def delete_phone_numbers(
        self, body: _q.BrandMessageFriendGroupRequest | Mapping[str, Any]
    ) -> _r.BrandMessageFriendGroupProcessingResult:
        """친구 그룹 내 전화번호 삭제.

        기존 친구 그룹에서 전화번호를 삭제합니다. `fileKey` 또는 `phoneNumbers`로 입력합니다. 처리는 비동기이며 진행 상황은 전화번호 요청 조회로 확인합니다.

        ``POST /api/comm/v1/center/brandmessage/friendGroup/phoneNumber/delete`` (``deleteBrandMessageFriendGroupPhoneNumbers``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageFriendGroupRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``BrandMessageFriendGroupProcessingResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_delete_brand_message_friend_group_phone_numbers(
            await self._transport.call(_call_delete_brand_message_friend_group_phone_numbers(body=body))
        )

    async def list_phone_number_requests(
        self, *, sender_key: str, friend_group_key: str, last_request_id: str | None = None, count: int | None = None
    ) -> _r.BrandMessageFriendGroupPhoneNumberRequestListResult:
        """친구 그룹 전화번호 요청 목록 조회.

        친구 그룹 전화번호 추가·삭제 요청의 처리 상태를 목록으로 조회합니다. 다음 페이지는 이전 응답의 마지막 항목 `requestId`를 `lastRequestId`로 넘겨 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/friendGroup/phoneNumber/requests`` (``listBrandMessageFriendGroupPhoneNumberRequests``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            friend_group_key: 친구 그룹 키입니다.
            last_request_id: 이전 페이지의 마지막 요청 아이디입니다.
            count: 조회 건수입니다.

        Returns:
            ``BrandMessageFriendGroupPhoneNumberRequestListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_brand_message_friend_group_phone_number_requests(
            await self._transport.call(
                _call_list_brand_message_friend_group_phone_number_requests(
                    sender_key=sender_key,
                    friend_group_key=friend_group_key,
                    last_request_id=last_request_id,
                    count=count,
                )
            )
        )

    def iter_list_phone_number_requests(
        self, *, sender_key: str, friend_group_key: str, count: int | None = None
    ) -> AsyncIterator[_r.BrandMessageFriendGroupPhoneNumberRequest]:
        """Iterate over every page of :meth:`list_phone_number_requests` (``listBrandMessageFriendGroupPhoneNumberRequests``, cursor pagination)."""

        async def fetch(position: Any) -> Any:
            body = await self._transport.call(
                _call_list_brand_message_friend_group_phone_number_requests(
                    sender_key=sender_key, friend_group_key=friend_group_key, count=count, last_request_id=position
                )
            )
            return validate(
                _r.BrandMessageFriendGroupPhoneNumberRequestListResponse,
                body,
                "listBrandMessageFriendGroupPhoneNumberRequests",
            )

        return aiterate(fetch, _PAGE_LIST_BRAND_MESSAGE_FRIEND_GROUP_PHONE_NUMBER_REQUESTS, size=None, start=None)

    async def get_phone_number_request(
        self, *, sender_key: str, friend_group_key: str, request_id: str
    ) -> _r.BrandMessageFriendGroupPhoneNumberRequestResult:
        """친구 그룹 전화번호 요청 단건 조회.

        전화번호 추가·삭제 응답으로 받은 `requestId`로 해당 요청의 처리 상태를 조회합니다.

        ``GET /api/comm/v1/center/brandmessage/friendGroup/phoneNumber/request`` (``getBrandMessageFriendGroupPhoneNumberRequest``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다.
            friend_group_key: 친구 그룹 키입니다.
            request_id: 조회할 요청 아이디입니다.

        Returns:
            ``BrandMessageFriendGroupPhoneNumberRequestResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_brand_message_friend_group_phone_number_request(
            await self._transport.call(
                _call_get_brand_message_friend_group_phone_number_request(
                    sender_key=sender_key, friend_group_key=friend_group_key, request_id=request_id
                )
            )
        )


class BrandMessageMarketingAgreements:
    """``client.brand_message.marketing_agreements``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def upload_evidence(
        self, file: FileInput, *, sender_key: str, filename: str | None = None
    ) -> _r.BrandMessageMarketingAgreeResult:
        """광고성 정보 수신동의 증적자료 파일 업로드.

        광고성 정보 수신동의를 입증하는 증적자료 파일을 업로드합니다. 파일은 발신프로필 기준으로 관리되며, 발송권한 신청 조건 중 하나입니다.

        ``POST /api/comm/v1/center/brandmessage/marketingAgree`` (``uploadBrandMessageMarketingAgreeEvidence``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다. 최대 40자입니다.
            file: 업로드할 광고성 정보 수신동의 증적자료 파일입니다.

        Returns:
            ``BrandMessageMarketingAgreeResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_marketing_agree_evidence(
            self._transport.call(
                _call_upload_brand_message_marketing_agree_evidence(file=file, sender_key=sender_key, filename=filename)
            )
        )


class AsyncBrandMessageMarketingAgreements:
    """``client.brand_message.marketing_agreements`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def upload_evidence(
        self, file: FileInput, *, sender_key: str, filename: str | None = None
    ) -> _r.BrandMessageMarketingAgreeResult:
        """광고성 정보 수신동의 증적자료 파일 업로드.

        광고성 정보 수신동의를 입증하는 증적자료 파일을 업로드합니다. 파일은 발신프로필 기준으로 관리되며, 발송권한 신청 조건 중 하나입니다.

        ``POST /api/comm/v1/center/brandmessage/marketingAgree`` (``uploadBrandMessageMarketingAgreeEvidence``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다. 최대 40자입니다.
            file: 업로드할 광고성 정보 수신동의 증적자료 파일입니다.

        Returns:
            ``BrandMessageMarketingAgreeResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_brand_message_marketing_agree_evidence(
            await self._transport.call(
                _call_upload_brand_message_marketing_agree_evidence(file=file, sender_key=sender_key, filename=filename)
            )
        )


class BrandMessageUnsubscribeContents:
    """``client.brand_message.unsubscribe_contents``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def register(self, body: _q.BrandMessageUnsubscribeContentRequest | Mapping[str, Any]) -> None:
        """발신프로필 무료수신거부 정보 입력.

        발신프로필의 무료수신거부 전화번호와 인증번호를 등록합니다. 광고성 메시지 하단의 무료수신거부 안내에 씁니다.

        ``POST /api/comm/v1/center/brandmessage/unSubscribeContent`` (``registerBrandMessageUnsubscribeContent``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageUnsubscribeContentRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_register_brand_message_unsubscribe_content(body=body))


class AsyncBrandMessageUnsubscribeContents:
    """``client.brand_message.unsubscribe_contents`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def register(self, body: _q.BrandMessageUnsubscribeContentRequest | Mapping[str, Any]) -> None:
        """발신프로필 무료수신거부 정보 입력.

        발신프로필의 무료수신거부 전화번호와 인증번호를 등록합니다. 광고성 메시지 하단의 무료수신거부 안내에 씁니다.

        ``POST /api/comm/v1/center/brandmessage/unSubscribeContent`` (``registerBrandMessageUnsubscribeContent``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.BrandMessageUnsubscribeContentRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_register_brand_message_unsubscribe_content(body=body))


class BrandMessage:
    """``client.brand_message``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport
        self.group_sends = BrandMessageGroupSends(transport)
        self.audience = BrandMessageAudience(transport)
        self.permissions = BrandMessagePermissions(transport)
        self.videos = BrandMessageVideos(transport)
        self.templates = BrandMessageTemplates(transport)
        self.group_tags = BrandMessageGroupTags(transport)
        self.friend_groups = BrandMessageFriendGroups(transport)
        self.marketing_agreements = BrandMessageMarketingAgreements(transport)
        self.unsubscribe_contents = BrandMessageUnsubscribeContents(transport)


class AsyncBrandMessage:
    """``client.brand_message`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport
        self.group_sends = AsyncBrandMessageGroupSends(transport)
        self.audience = AsyncBrandMessageAudience(transport)
        self.permissions = AsyncBrandMessagePermissions(transport)
        self.videos = AsyncBrandMessageVideos(transport)
        self.templates = AsyncBrandMessageTemplates(transport)
        self.group_tags = AsyncBrandMessageGroupTags(transport)
        self.friend_groups = AsyncBrandMessageFriendGroups(transport)
        self.marketing_agreements = AsyncBrandMessageMarketingAgreements(transport)
        self.unsubscribe_contents = AsyncBrandMessageUnsubscribeContents(transport)


class RcsBrands:
    """``client.rcs.brands``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get(self, *, brand_id: str) -> _r.RcsBrandResult:
        """RCS 브랜드 상세 조회.

        brandId 기준으로 RCS 브랜드 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/rcs/brand`` (``getRcsBrand``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 조회할 브랜드 ID입니다.

        Returns:
            ``RcsBrandResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_brand(self._transport.call(_call_get_rcs_brand(brand_id=brand_id)))

    def update(
        self,
        *,
        brand_id: str,
        reg_brand: _q.RcsBrand | Mapping[str, Any],
        brand_profile: FileInput | None = None,
        brand_background: FileInput | None = None,
        season_doc_file: FileInput | None = None,
        brand_profile_filename: str | None = None,
        brand_background_filename: str | None = None,
        season_doc_file_filename: str | None = None,
    ) -> _r.RcsBrandResult:
        """RCS 브랜드 수정.

        브랜드 기본 정보와 브랜드 이미지를 수정합니다. `multipart/form-data`로 보내며,
        `regBrand`는 JSON 문자열 파트, 이미지·증빙 파일은 바이너리 파트입니다.
        파일 스트림을 다시 보내야 하고 검수 요청이 다시 걸릴 수 있으므로 SDK는 429만 재시도합니다.

        ``PUT /api/comm/v1/center/rcs/brand`` (``updateRcsBrand``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 수정할 브랜드 ID입니다.
            reg_brand: 브랜드 수정 정보입니다. JSON으로 직렬화해 한 파트로 보냅니다.
            brand_profile: 브랜드 프로필 이미지 파일입니다.
            brand_background: 브랜드 배경 이미지 파일입니다.
            season_doc_file: 시즌성 증빙 파일입니다.

        Returns:
            ``RcsBrandResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_update_rcs_brand(
            self._transport.call(
                _call_update_rcs_brand(
                    brand_id=brand_id,
                    reg_brand=reg_brand,
                    brand_profile=brand_profile,
                    brand_background=brand_background,
                    season_doc_file=season_doc_file,
                    brand_profile_filename=brand_profile_filename,
                    brand_background_filename=brand_background_filename,
                    season_doc_file_filename=season_doc_file_filename,
                )
            )
        )


class AsyncRcsBrands:
    """``client.rcs.brands`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get(self, *, brand_id: str) -> _r.RcsBrandResult:
        """RCS 브랜드 상세 조회.

        brandId 기준으로 RCS 브랜드 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/rcs/brand`` (``getRcsBrand``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 조회할 브랜드 ID입니다.

        Returns:
            ``RcsBrandResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_brand(await self._transport.call(_call_get_rcs_brand(brand_id=brand_id)))

    async def update(
        self,
        *,
        brand_id: str,
        reg_brand: _q.RcsBrand | Mapping[str, Any],
        brand_profile: FileInput | None = None,
        brand_background: FileInput | None = None,
        season_doc_file: FileInput | None = None,
        brand_profile_filename: str | None = None,
        brand_background_filename: str | None = None,
        season_doc_file_filename: str | None = None,
    ) -> _r.RcsBrandResult:
        """RCS 브랜드 수정.

        브랜드 기본 정보와 브랜드 이미지를 수정합니다. `multipart/form-data`로 보내며,
        `regBrand`는 JSON 문자열 파트, 이미지·증빙 파일은 바이너리 파트입니다.
        파일 스트림을 다시 보내야 하고 검수 요청이 다시 걸릴 수 있으므로 SDK는 429만 재시도합니다.

        ``PUT /api/comm/v1/center/rcs/brand`` (``updateRcsBrand``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 수정할 브랜드 ID입니다.
            reg_brand: 브랜드 수정 정보입니다. JSON으로 직렬화해 한 파트로 보냅니다.
            brand_profile: 브랜드 프로필 이미지 파일입니다.
            brand_background: 브랜드 배경 이미지 파일입니다.
            season_doc_file: 시즌성 증빙 파일입니다.

        Returns:
            ``RcsBrandResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_update_rcs_brand(
            await self._transport.call(
                _call_update_rcs_brand(
                    brand_id=brand_id,
                    reg_brand=reg_brand,
                    brand_profile=brand_profile,
                    brand_background=brand_background,
                    season_doc_file=season_doc_file,
                    brand_profile_filename=brand_profile_filename,
                    brand_background_filename=brand_background_filename,
                    season_doc_file_filename=season_doc_file_filename,
                )
            )
        )


class RcsChatbots:
    """``client.rcs.chatbots``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(self, *, brand_id: str, offset: int | None = None, limit: int | None = None) -> _r.RcsChatbotResult:
        """RCS 대화방 목록 조회.

        브랜드 ID를 기준으로 등록된 RCS 대화방 목록을 조회합니다. 대화방(챗봇)은 브랜드에 속해 실제로 메시지를 주고받는 단위입니다.

        ``GET /api/comm/v1/center/rcs/chatbot/list`` (``listRcsChatbots``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 조회할 브랜드 ID입니다.
            offset: 조회 시작 위치입니다. 기본값 0(영문 문서 기준).
            limit: 조회 최대 건수입니다. 기본값 1000(영문 문서 기준).

        Returns:
            ``RcsChatbotResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_rcs_chatbots(
            self._transport.call(_call_list_rcs_chatbots(brand_id=brand_id, offset=offset, limit=limit))
        )

    def iter_list(self, *, brand_id: str, limit: int | None = None) -> Iterator[_r.RcsChatbot]:
        """Iterate over every page of :meth:`list` (``listRcsChatbots``, offset pagination)."""

        def fetch(position: Any) -> Any:
            body = self._transport.call(_call_list_rcs_chatbots(brand_id=brand_id, limit=limit, offset=position))
            return validate(_r.RcsChatbotResponse, body, "listRcsChatbots")

        return iterate(fetch, _PAGE_LIST_RCS_CHATBOTS, size=limit, start=0)

    def get(self, *, brand_id: str, chatbot_id: str) -> _r.RcsChatbotResult:
        """RCS 대화방 상세 조회.

        브랜드 ID와 대화방 ID를 기준으로 RCS 대화방 상세 정보를 조회합니다. 결과는 `data.data.rcs.chatbot` 배열로 돌아옵니다.

        ``GET /api/comm/v1/center/rcs/chatbot`` (``getRcsChatbot``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 조회할 브랜드 ID입니다.
            chatbot_id: 조회할 대화방 ID입니다.

        Returns:
            ``RcsChatbotResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_chatbot(
            self._transport.call(_call_get_rcs_chatbot(brand_id=brand_id, chatbot_id=chatbot_id))
        )

    def update(
        self,
        *,
        brand_id: str,
        chatbot: _q.RcsChatbot | Mapping[str, Any],
        sub_num_certificate: FileInput,
        sub_num_certificate_filename: str | None = None,
    ) -> _r.RcsChatbotResult:
        """RCS 대화방 수정.

        등록된 RCS 대화방 정보를 수정합니다. `multipart/form-data`로 보내며, 대화방 정보(`chatbot`)는 JSON 문자열,
        부가번호 증명 서류(`subNumCertificate`)는 파일로 함께 보냅니다.
        파일 스트림을 다시 보내야 하고 검수 요청이 다시 걸릴 수 있으므로 SDK는 429만 재시도합니다.

        ``PUT /api/comm/v1/center/rcs/chatbot`` (``updateRcsChatbot``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 수정할 대화방이 속한 브랜드 ID입니다.
            chatbot: 수정할 대화방 정보입니다. 문서상 타입은 String(JSON 문자열)이며, JSON으로 직렬화해 한 파트로 보냅니다.
            sub_num_certificate: 부가번호 사용을 증명하는 서류 파일입니다.

        Returns:
            ``RcsChatbotResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_update_rcs_chatbot(
            self._transport.call(
                _call_update_rcs_chatbot(
                    brand_id=brand_id,
                    chatbot=chatbot,
                    sub_num_certificate=sub_num_certificate,
                    sub_num_certificate_filename=sub_num_certificate_filename,
                )
            )
        )

    def cancel(self, brand_id: str, chatbot_id: str) -> _r.RcsChatbotResult:
        """RCS 대화방 승인 취소.

        승인 진행 중인 RCS 대화방의 승인 요청을 취소합니다.

        ``PUT /api/comm/v1/center/rcs/brandId/{brandId}/chatbotId/{chatbotId}/cancel`` (``cancelRcsChatbotApproval``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 브랜드 ID입니다.
            chatbot_id: 대화방 ID입니다.

        Returns:
            ``RcsChatbotResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_cancel_rcs_chatbot_approval(
            self._transport.call(_call_cancel_rcs_chatbot_approval(brand_id=brand_id, chatbot_id=chatbot_id))
        )

    def delete(self, brand_id: str, chatbot_id: str) -> _r.RcsChatbotResult:
        """RCS 대화방 삭제.

        등록된 RCS 대화방을 삭제합니다.

        ``DELETE /api/comm/v1/center/rcs/brandId/{brandId}/chatbotId/{chatbotId}`` (``deleteRcsChatbot``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 브랜드 ID입니다.
            chatbot_id: 대화방 ID입니다.

        Returns:
            ``RcsChatbotResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_delete_rcs_chatbot(
            self._transport.call(_call_delete_rcs_chatbot(brand_id=brand_id, chatbot_id=chatbot_id))
        )

    def get_usable_queries(self, chatbot_id: str) -> _r.RcsChatbotResult:
        """RCS 대화방 사용 가능 쿼리 조회.

        대화방 ID를 기준으로 해당 대화방에서 사용할 수 있는 쿼리 정보를 조회합니다.

        ``GET /api/comm/v1/center/rcs/usableQuery/chatbotId/{chatbotId}`` (``getRcsChatbotUsableQueries``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            chatbot_id: 대화방 ID입니다.

        Returns:
            ``RcsChatbotResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_chatbot_usable_queries(
            self._transport.call(_call_get_rcs_chatbot_usable_queries(chatbot_id=chatbot_id))
        )


class AsyncRcsChatbots:
    """``client.rcs.chatbots`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(self, *, brand_id: str, offset: int | None = None, limit: int | None = None) -> _r.RcsChatbotResult:
        """RCS 대화방 목록 조회.

        브랜드 ID를 기준으로 등록된 RCS 대화방 목록을 조회합니다. 대화방(챗봇)은 브랜드에 속해 실제로 메시지를 주고받는 단위입니다.

        ``GET /api/comm/v1/center/rcs/chatbot/list`` (``listRcsChatbots``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 조회할 브랜드 ID입니다.
            offset: 조회 시작 위치입니다. 기본값 0(영문 문서 기준).
            limit: 조회 최대 건수입니다. 기본값 1000(영문 문서 기준).

        Returns:
            ``RcsChatbotResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_rcs_chatbots(
            await self._transport.call(_call_list_rcs_chatbots(brand_id=brand_id, offset=offset, limit=limit))
        )

    def iter_list(self, *, brand_id: str, limit: int | None = None) -> AsyncIterator[_r.RcsChatbot]:
        """Iterate over every page of :meth:`list` (``listRcsChatbots``, offset pagination)."""

        async def fetch(position: Any) -> Any:
            body = await self._transport.call(_call_list_rcs_chatbots(brand_id=brand_id, limit=limit, offset=position))
            return validate(_r.RcsChatbotResponse, body, "listRcsChatbots")

        return aiterate(fetch, _PAGE_LIST_RCS_CHATBOTS, size=limit, start=0)

    async def get(self, *, brand_id: str, chatbot_id: str) -> _r.RcsChatbotResult:
        """RCS 대화방 상세 조회.

        브랜드 ID와 대화방 ID를 기준으로 RCS 대화방 상세 정보를 조회합니다. 결과는 `data.data.rcs.chatbot` 배열로 돌아옵니다.

        ``GET /api/comm/v1/center/rcs/chatbot`` (``getRcsChatbot``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 조회할 브랜드 ID입니다.
            chatbot_id: 조회할 대화방 ID입니다.

        Returns:
            ``RcsChatbotResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_chatbot(
            await self._transport.call(_call_get_rcs_chatbot(brand_id=brand_id, chatbot_id=chatbot_id))
        )

    async def update(
        self,
        *,
        brand_id: str,
        chatbot: _q.RcsChatbot | Mapping[str, Any],
        sub_num_certificate: FileInput,
        sub_num_certificate_filename: str | None = None,
    ) -> _r.RcsChatbotResult:
        """RCS 대화방 수정.

        등록된 RCS 대화방 정보를 수정합니다. `multipart/form-data`로 보내며, 대화방 정보(`chatbot`)는 JSON 문자열,
        부가번호 증명 서류(`subNumCertificate`)는 파일로 함께 보냅니다.
        파일 스트림을 다시 보내야 하고 검수 요청이 다시 걸릴 수 있으므로 SDK는 429만 재시도합니다.

        ``PUT /api/comm/v1/center/rcs/chatbot`` (``updateRcsChatbot``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 수정할 대화방이 속한 브랜드 ID입니다.
            chatbot: 수정할 대화방 정보입니다. 문서상 타입은 String(JSON 문자열)이며, JSON으로 직렬화해 한 파트로 보냅니다.
            sub_num_certificate: 부가번호 사용을 증명하는 서류 파일입니다.

        Returns:
            ``RcsChatbotResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_update_rcs_chatbot(
            await self._transport.call(
                _call_update_rcs_chatbot(
                    brand_id=brand_id,
                    chatbot=chatbot,
                    sub_num_certificate=sub_num_certificate,
                    sub_num_certificate_filename=sub_num_certificate_filename,
                )
            )
        )

    async def cancel(self, brand_id: str, chatbot_id: str) -> _r.RcsChatbotResult:
        """RCS 대화방 승인 취소.

        승인 진행 중인 RCS 대화방의 승인 요청을 취소합니다.

        ``PUT /api/comm/v1/center/rcs/brandId/{brandId}/chatbotId/{chatbotId}/cancel`` (``cancelRcsChatbotApproval``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 브랜드 ID입니다.
            chatbot_id: 대화방 ID입니다.

        Returns:
            ``RcsChatbotResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_cancel_rcs_chatbot_approval(
            await self._transport.call(_call_cancel_rcs_chatbot_approval(brand_id=brand_id, chatbot_id=chatbot_id))
        )

    async def delete(self, brand_id: str, chatbot_id: str) -> _r.RcsChatbotResult:
        """RCS 대화방 삭제.

        등록된 RCS 대화방을 삭제합니다.

        ``DELETE /api/comm/v1/center/rcs/brandId/{brandId}/chatbotId/{chatbotId}`` (``deleteRcsChatbot``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 브랜드 ID입니다.
            chatbot_id: 대화방 ID입니다.

        Returns:
            ``RcsChatbotResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_delete_rcs_chatbot(
            await self._transport.call(_call_delete_rcs_chatbot(brand_id=brand_id, chatbot_id=chatbot_id))
        )

    async def get_usable_queries(self, chatbot_id: str) -> _r.RcsChatbotResult:
        """RCS 대화방 사용 가능 쿼리 조회.

        대화방 ID를 기준으로 해당 대화방에서 사용할 수 있는 쿼리 정보를 조회합니다.

        ``GET /api/comm/v1/center/rcs/usableQuery/chatbotId/{chatbotId}`` (``getRcsChatbotUsableQueries``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            chatbot_id: 대화방 ID입니다.

        Returns:
            ``RcsChatbotResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_chatbot_usable_queries(
            await self._transport.call(_call_get_rcs_chatbot_usable_queries(chatbot_id=chatbot_id))
        )


class RcsCommonFormats:
    """``client.rcs.common_formats``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(self) -> _r.RcsMessagebaseCommonListResult:
        """RCS 공통 포맷 목록 조회.

        RCS에서 사용할 수 있는 공통 포맷 목록을 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase/common/list`` (``listRcsCommonFormats``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Returns:
            ``RcsMessagebaseCommonListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_rcs_common_formats(self._transport.call(_call_list_rcs_common_formats()))

    def get(self, *, messagebase_id: str) -> _r.RcsMessagebaseFormDetailResult:
        """RCS 공통 포맷 상세 조회.

        메시지베이스 ID를 기준으로 RCS 공통 포맷 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase/common`` (``getRcsCommonFormat``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            messagebase_id: 조회할 메시지베이스 ID입니다.

        Returns:
            ``RcsMessagebaseFormDetailResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_common_format(
            self._transport.call(_call_get_rcs_common_format(messagebase_id=messagebase_id))
        )


class AsyncRcsCommonFormats:
    """``client.rcs.common_formats`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(self) -> _r.RcsMessagebaseCommonListResult:
        """RCS 공통 포맷 목록 조회.

        RCS에서 사용할 수 있는 공통 포맷 목록을 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase/common/list`` (``listRcsCommonFormats``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Returns:
            ``RcsMessagebaseCommonListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_rcs_common_formats(await self._transport.call(_call_list_rcs_common_formats()))

    async def get(self, *, messagebase_id: str) -> _r.RcsMessagebaseFormDetailResult:
        """RCS 공통 포맷 상세 조회.

        메시지베이스 ID를 기준으로 RCS 공통 포맷 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase/common`` (``getRcsCommonFormat``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            messagebase_id: 조회할 메시지베이스 ID입니다.

        Returns:
            ``RcsMessagebaseFormDetailResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_common_format(
            await self._transport.call(_call_get_rcs_common_format(messagebase_id=messagebase_id))
        )


class RcsTemplateForms:
    """``client.rcs.template_forms``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(self, *, offset: int | None = None, limit: int | None = None) -> _r.RcsMessagebaseFormListResult:
        """RCS 템플릿 양식 목록 조회.

        RCS 템플릿 등록에 사용할 수 있는 템플릿 양식 목록을 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase/messagebaseform/list`` (``listRcsTemplateForms``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            offset: 조회 시작 위치입니다. 기본값 0(영문 문서 기준).
            limit: 조회 최대 건수입니다. 최소 100, 최대 1000, 기본값 100(영문 문서 기준).

        Returns:
            ``RcsMessagebaseFormListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_rcs_template_forms(
            self._transport.call(_call_list_rcs_template_forms(offset=offset, limit=limit))
        )

    def iter_list(self, *, limit: int | None = None) -> Iterator[_r.RcsMessagebaseFormSummary]:
        """Iterate over every page of :meth:`list` (``listRcsTemplateForms``, offset pagination)."""

        def fetch(position: Any) -> Any:
            body = self._transport.call(_call_list_rcs_template_forms(limit=limit, offset=position))
            return validate(_r.RcsMessagebaseFormListResponse, body, "listRcsTemplateForms")

        return iterate(fetch, _PAGE_LIST_RCS_TEMPLATE_FORMS, size=limit, start=0)

    def get(self, *, messagebaseform_id: str) -> _r.RcsMessagebaseFormDetailResult:
        """RCS 템플릿 양식 상세 조회.

        템플릿 양식 ID를 기준으로 템플릿 양식 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase/messagebaseform`` (``getRcsTemplateForm``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            messagebaseform_id: 메시지 양식 ID입니다.

        Returns:
            ``RcsMessagebaseFormDetailResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_template_form(
            self._transport.call(_call_get_rcs_template_form(messagebaseform_id=messagebaseform_id))
        )


class AsyncRcsTemplateForms:
    """``client.rcs.template_forms`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(self, *, offset: int | None = None, limit: int | None = None) -> _r.RcsMessagebaseFormListResult:
        """RCS 템플릿 양식 목록 조회.

        RCS 템플릿 등록에 사용할 수 있는 템플릿 양식 목록을 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase/messagebaseform/list`` (``listRcsTemplateForms``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            offset: 조회 시작 위치입니다. 기본값 0(영문 문서 기준).
            limit: 조회 최대 건수입니다. 최소 100, 최대 1000, 기본값 100(영문 문서 기준).

        Returns:
            ``RcsMessagebaseFormListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_rcs_template_forms(
            await self._transport.call(_call_list_rcs_template_forms(offset=offset, limit=limit))
        )

    def iter_list(self, *, limit: int | None = None) -> AsyncIterator[_r.RcsMessagebaseFormSummary]:
        """Iterate over every page of :meth:`list` (``listRcsTemplateForms``, offset pagination)."""

        async def fetch(position: Any) -> Any:
            body = await self._transport.call(_call_list_rcs_template_forms(limit=limit, offset=position))
            return validate(_r.RcsMessagebaseFormListResponse, body, "listRcsTemplateForms")

        return aiterate(fetch, _PAGE_LIST_RCS_TEMPLATE_FORMS, size=limit, start=0)

    async def get(self, *, messagebaseform_id: str) -> _r.RcsMessagebaseFormDetailResult:
        """RCS 템플릿 양식 상세 조회.

        템플릿 양식 ID를 기준으로 템플릿 양식 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase/messagebaseform`` (``getRcsTemplateForm``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            messagebaseform_id: 메시지 양식 ID입니다.

        Returns:
            ``RcsMessagebaseFormDetailResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_template_form(
            await self._transport.call(_call_get_rcs_template_form(messagebaseform_id=messagebaseform_id))
        )


class RcsTemplates:
    """``client.rcs.templates``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(self) -> _r.RcsTemplateListResult:
        """RCS 템플릿 목록 조회.

        브랜드 ID를 기준으로 등록된 RCS 템플릿 목록을 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase/list`` (``listRcsTemplates``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Returns:
            ``RcsTemplateListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_rcs_templates(self._transport.call(_call_list_rcs_templates()))

    def get(self, *, messagebase_id: str) -> _r.RcsTemplateResult:
        """RCS 템플릿 상세 조회.

        메시지베이스 ID를 기준으로 등록된 RCS 템플릿 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase`` (``getRcsTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            messagebase_id: 메시지베이스 ID입니다.

        Returns:
            ``RcsTemplateResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_template(self._transport.call(_call_get_rcs_template(messagebase_id=messagebase_id)))

    def create(self, body: _q.RcsTemplateRequest | Mapping[str, Any]) -> _r.RcsTemplateIdResult:
        """RCS 템플릿 등록.

        브랜드에 RCS 템플릿을 등록합니다. 응답의 `messagebaseId`를 발송 시 `formatId` 필드에 넣습니다(영문 문서 기준).

        ``POST /api/comm/v1/center/rcs/messagebase`` (``createRcsTemplate``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.RcsTemplateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``RcsTemplateIdResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_rcs_template(self._transport.call(_call_create_rcs_template(body=body)))

    def update(self, body: _q.RcsTemplateRequest | Mapping[str, Any]) -> _r.RcsTemplateIdResult:
        """RCS 템플릿 수정.

        등록된 RCS 템플릿 정보를 수정합니다.

        ``PUT /api/comm/v1/center/rcs/messagebase`` (``updateRcsTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.RcsTemplateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``RcsTemplateIdResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_update_rcs_template(self._transport.call(_call_update_rcs_template(body=body)))

    def cancel(self, brand_id: str, messagebase_id: str) -> _r.RcsTemplateIdResult:
        """RCS 템플릿 승인 취소.

        승인 진행 중인 RCS 템플릿의 승인 요청을 취소합니다.

        ``PUT /api/comm/v1/center/rcs/brandId/{brandId}/messagebaseId/{messagebaseId}/cancel`` (``cancelRcsTemplateApproval``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 브랜드 ID입니다.
            messagebase_id: 메시지베이스 ID입니다. 발송 시에는 `formatId` 필드 이름으로 쓰이므로 혼동하지 않도록 주의합니다.

        Returns:
            ``RcsTemplateIdResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_cancel_rcs_template_approval(
            self._transport.call(_call_cancel_rcs_template_approval(brand_id=brand_id, messagebase_id=messagebase_id))
        )

    def delete(self, brand_id: str, messagebase_id: str) -> _r.RcsTemplateIdResult:
        """RCS 템플릿 삭제.

        등록된 RCS 템플릿을 삭제합니다.

        ``DELETE /api/comm/v1/center/rcs/brandId/{brandId}/messagebaseId/{messagebaseId}`` (``deleteRcsTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 브랜드 ID입니다.
            messagebase_id: 메시지베이스 ID입니다. 발송 시에는 `formatId` 필드 이름으로 쓰이므로 혼동하지 않도록 주의합니다.

        Returns:
            ``RcsTemplateIdResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_delete_rcs_template(
            self._transport.call(_call_delete_rcs_template(brand_id=brand_id, messagebase_id=messagebase_id))
        )


class AsyncRcsTemplates:
    """``client.rcs.templates`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(self) -> _r.RcsTemplateListResult:
        """RCS 템플릿 목록 조회.

        브랜드 ID를 기준으로 등록된 RCS 템플릿 목록을 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase/list`` (``listRcsTemplates``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Returns:
            ``RcsTemplateListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_rcs_templates(await self._transport.call(_call_list_rcs_templates()))

    async def get(self, *, messagebase_id: str) -> _r.RcsTemplateResult:
        """RCS 템플릿 상세 조회.

        메시지베이스 ID를 기준으로 등록된 RCS 템플릿 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase`` (``getRcsTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            messagebase_id: 메시지베이스 ID입니다.

        Returns:
            ``RcsTemplateResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_template(
            await self._transport.call(_call_get_rcs_template(messagebase_id=messagebase_id))
        )

    async def create(self, body: _q.RcsTemplateRequest | Mapping[str, Any]) -> _r.RcsTemplateIdResult:
        """RCS 템플릿 등록.

        브랜드에 RCS 템플릿을 등록합니다. 응답의 `messagebaseId`를 발송 시 `formatId` 필드에 넣습니다(영문 문서 기준).

        ``POST /api/comm/v1/center/rcs/messagebase`` (``createRcsTemplate``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.RcsTemplateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``RcsTemplateIdResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_rcs_template(await self._transport.call(_call_create_rcs_template(body=body)))

    async def update(self, body: _q.RcsTemplateRequest | Mapping[str, Any]) -> _r.RcsTemplateIdResult:
        """RCS 템플릿 수정.

        등록된 RCS 템플릿 정보를 수정합니다.

        ``PUT /api/comm/v1/center/rcs/messagebase`` (``updateRcsTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.RcsTemplateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``RcsTemplateIdResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_update_rcs_template(await self._transport.call(_call_update_rcs_template(body=body)))

    async def cancel(self, brand_id: str, messagebase_id: str) -> _r.RcsTemplateIdResult:
        """RCS 템플릿 승인 취소.

        승인 진행 중인 RCS 템플릿의 승인 요청을 취소합니다.

        ``PUT /api/comm/v1/center/rcs/brandId/{brandId}/messagebaseId/{messagebaseId}/cancel`` (``cancelRcsTemplateApproval``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 브랜드 ID입니다.
            messagebase_id: 메시지베이스 ID입니다. 발송 시에는 `formatId` 필드 이름으로 쓰이므로 혼동하지 않도록 주의합니다.

        Returns:
            ``RcsTemplateIdResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_cancel_rcs_template_approval(
            await self._transport.call(
                _call_cancel_rcs_template_approval(brand_id=brand_id, messagebase_id=messagebase_id)
            )
        )

    async def delete(self, brand_id: str, messagebase_id: str) -> _r.RcsTemplateIdResult:
        """RCS 템플릿 삭제.

        등록된 RCS 템플릿을 삭제합니다.

        ``DELETE /api/comm/v1/center/rcs/brandId/{brandId}/messagebaseId/{messagebaseId}`` (``deleteRcsTemplate``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 브랜드 ID입니다.
            messagebase_id: 메시지베이스 ID입니다. 발송 시에는 `formatId` 필드 이름으로 쓰이므로 혼동하지 않도록 주의합니다.

        Returns:
            ``RcsTemplateIdResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_delete_rcs_template(
            await self._transport.call(_call_delete_rcs_template(brand_id=brand_id, messagebase_id=messagebase_id))
        )


class RcsTemplateImages:
    """``client.rcs.template_images``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get(self, *, brand_id: str, file_id: str) -> _r.RcsTemplateImageResult:
        """RCS 템플릿 이미지 상세 조회.

        브랜드 ID와 템플릿 파일 ID를 기준으로 템플릿 이미지 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase/file`` (``getRcsTemplateImage``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 브랜드 ID입니다.
            file_id: 템플릿 파일 ID입니다.

        Returns:
            ``RcsTemplateImageResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_template_image(
            self._transport.call(_call_get_rcs_template_image(brand_id=brand_id, file_id=file_id))
        )

    def upload(self, file: FileInput, *, brand_id: str, filename: str | None = None) -> _r.RcsTemplateImageResult:
        """RCS 템플릿 이미지 등록.

        RCS 템플릿 등록에 사용할 이미지를 업로드하고 템플릿 파일 ID를 발급받습니다.
        발송용 이미지 업로드(`/api/comm/v1/file/rcs`)와는 다른 API입니다.

        ``POST /api/comm/v1/center/rcs/messagebase/file`` (``uploadRcsTemplateImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 브랜드 ID입니다.
            file: 템플릿 등록에 사용할 이미지 파일입니다.

        Returns:
            ``RcsTemplateImageResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_rcs_template_image(
            self._transport.call(_call_upload_rcs_template_image(file=file, brand_id=brand_id, filename=filename))
        )

    def list_form_logos(self, *, messagebaseform_id: str) -> _r.RcsTemplateFormLogoListResult:
        """RCS 템플릿 양식 로고 이미지 조회.

        템플릿 양식 ID를 기준으로 템플릿 양식에서 사용할 수 있는 로고 이미지 목록을 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase/messagebaseform/logo`` (``listRcsTemplateFormLogos``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            messagebaseform_id: 메시지 양식 ID입니다.

        Returns:
            ``RcsTemplateFormLogoListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_rcs_template_form_logos(
            self._transport.call(_call_list_rcs_template_form_logos(messagebaseform_id=messagebaseform_id))
        )


class AsyncRcsTemplateImages:
    """``client.rcs.template_images`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get(self, *, brand_id: str, file_id: str) -> _r.RcsTemplateImageResult:
        """RCS 템플릿 이미지 상세 조회.

        브랜드 ID와 템플릿 파일 ID를 기준으로 템플릿 이미지 상세 정보를 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase/file`` (``getRcsTemplateImage``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 브랜드 ID입니다.
            file_id: 템플릿 파일 ID입니다.

        Returns:
            ``RcsTemplateImageResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_rcs_template_image(
            await self._transport.call(_call_get_rcs_template_image(brand_id=brand_id, file_id=file_id))
        )

    async def upload(self, file: FileInput, *, brand_id: str, filename: str | None = None) -> _r.RcsTemplateImageResult:
        """RCS 템플릿 이미지 등록.

        RCS 템플릿 등록에 사용할 이미지를 업로드하고 템플릿 파일 ID를 발급받습니다.
        발송용 이미지 업로드(`/api/comm/v1/file/rcs`)와는 다른 API입니다.

        ``POST /api/comm/v1/center/rcs/messagebase/file`` (``uploadRcsTemplateImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            brand_id: 브랜드 ID입니다.
            file: 템플릿 등록에 사용할 이미지 파일입니다.

        Returns:
            ``RcsTemplateImageResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_rcs_template_image(
            await self._transport.call(_call_upload_rcs_template_image(file=file, brand_id=brand_id, filename=filename))
        )

    async def list_form_logos(self, *, messagebaseform_id: str) -> _r.RcsTemplateFormLogoListResult:
        """RCS 템플릿 양식 로고 이미지 조회.

        템플릿 양식 ID를 기준으로 템플릿 양식에서 사용할 수 있는 로고 이미지 목록을 조회합니다.

        ``GET /api/comm/v1/center/rcs/messagebase/messagebaseform/logo`` (``listRcsTemplateFormLogos``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            messagebaseform_id: 메시지 양식 ID입니다.

        Returns:
            ``RcsTemplateFormLogoListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_rcs_template_form_logos(
            await self._transport.call(_call_list_rcs_template_form_logos(messagebaseform_id=messagebaseform_id))
        )


class Rcs:
    """``client.rcs``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport
        self.brands = RcsBrands(transport)
        self.chatbots = RcsChatbots(transport)
        self.common_formats = RcsCommonFormats(transport)
        self.template_forms = RcsTemplateForms(transport)
        self.templates = RcsTemplates(transport)
        self.template_images = RcsTemplateImages(transport)


class AsyncRcs:
    """``client.rcs`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport
        self.brands = AsyncRcsBrands(transport)
        self.chatbots = AsyncRcsChatbots(transport)
        self.common_formats = AsyncRcsCommonFormats(transport)
        self.template_forms = AsyncRcsTemplateForms(transport)
        self.templates = AsyncRcsTemplates(transport)
        self.template_images = AsyncRcsTemplateImages(transport)


class CounselMessages:
    """``client.counsel.messages``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def send_plain(self, body: _q.CounselPlainMessageRequest | Mapping[str, Any]) -> _r.CounselSendServiceResult:
        """상담톡 Plain 메시지 발송.

        상담톡 Plain 메시지(TEXT, IMAGE, VIDEO, AUDIO, FILE)를 발송합니다.

        ``POST /api/comm/v1/cstalk/plain`` (``sendCounselPlain``). 429만 재시도, 속도 제한 버킷: ``send``.

        Args:
            body: :class:`~bizgo.models.CounselPlainMessageRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``CounselSendServiceResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_send_counsel_plain(self._transport.call(_call_send_counsel_plain(body=body)))

    def send_rich(self, body: _q.CounselRichMessageRequest | Mapping[str, Any]) -> _r.CounselSendServiceResult:
        """상담톡 Rich 메시지 발송.

        상담톡 Rich 메시지(TEXT, IMAGE, WIDE, ITEM_LIST, WIDE_ITEM_LIST, CAROUSEL_FEED, PERSONAL)를 발송합니다.
        `KAKAO_CERT`(본인인증) 발송은 채널이 본인인증 화이트리스트에 사전 등록되어 있어야 하며, 결과는 `counselCertResult` 웹훅으로 옵니다.

        ``POST /api/comm/v1/cstalk/rich`` (``sendCounselRich``). 429만 재시도, 속도 제한 버킷: ``send``.

        Args:
            body: :class:`~bizgo.models.CounselRichMessageRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``CounselSendServiceResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_send_counsel_rich(self._transport.call(_call_send_counsel_rich(body=body)))

    def delete(self, body: _q.CounselMessageDeleteRequest | Mapping[str, Any]) -> None:
        """상담 메시지 삭제.

        이미 발송된 상담톡 메시지를 삭제합니다. 삭제한 메시지는 복구할 수 없습니다.
        응답 코드: `A000` 삭제 성공, `A502` 발신프로필 미등록·`senderKey`/`msgKey` 오류·소유자 불일치, `A507` `userKey` 오류, `A822` 삭제 불가 상태, `A213` 그 외 처리 실패.

        ``POST /api/comm/v1/center/cstalk/chat/delete`` (``deleteCounselMessage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselMessageDeleteRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_delete_counsel_message(body=body))


class AsyncCounselMessages:
    """``client.counsel.messages`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def send_plain(self, body: _q.CounselPlainMessageRequest | Mapping[str, Any]) -> _r.CounselSendServiceResult:
        """상담톡 Plain 메시지 발송.

        상담톡 Plain 메시지(TEXT, IMAGE, VIDEO, AUDIO, FILE)를 발송합니다.

        ``POST /api/comm/v1/cstalk/plain`` (``sendCounselPlain``). 429만 재시도, 속도 제한 버킷: ``send``.

        Args:
            body: :class:`~bizgo.models.CounselPlainMessageRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``CounselSendServiceResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_send_counsel_plain(await self._transport.call(_call_send_counsel_plain(body=body)))

    async def send_rich(self, body: _q.CounselRichMessageRequest | Mapping[str, Any]) -> _r.CounselSendServiceResult:
        """상담톡 Rich 메시지 발송.

        상담톡 Rich 메시지(TEXT, IMAGE, WIDE, ITEM_LIST, WIDE_ITEM_LIST, CAROUSEL_FEED, PERSONAL)를 발송합니다.
        `KAKAO_CERT`(본인인증) 발송은 채널이 본인인증 화이트리스트에 사전 등록되어 있어야 하며, 결과는 `counselCertResult` 웹훅으로 옵니다.

        ``POST /api/comm/v1/cstalk/rich`` (``sendCounselRich``). 429만 재시도, 속도 제한 버킷: ``send``.

        Args:
            body: :class:`~bizgo.models.CounselRichMessageRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``CounselSendServiceResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_send_counsel_rich(await self._transport.call(_call_send_counsel_rich(body=body)))

    async def delete(self, body: _q.CounselMessageDeleteRequest | Mapping[str, Any]) -> None:
        """상담 메시지 삭제.

        이미 발송된 상담톡 메시지를 삭제합니다. 삭제한 메시지는 복구할 수 없습니다.
        응답 코드: `A000` 삭제 성공, `A502` 발신프로필 미등록·`senderKey`/`msgKey` 오류·소유자 불일치, `A507` `userKey` 오류, `A822` 삭제 불가 상태, `A213` 그 외 처리 실패.

        ``POST /api/comm/v1/center/cstalk/chat/delete`` (``deleteCounselMessage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselMessageDeleteRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_delete_counsel_message(body=body))


class CounselSessions:
    """``client.counsel.sessions``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def end(self, body: _q.CounselEndRequest | Mapping[str, Any]) -> _r.CounselEndResult:
        """상담 종료.

        현재 열려 있는 상담 세션을 종료합니다. 처리 결과는 발송 결과 웹훅(`counselResult`, requestType `end`)으로도 전달됩니다.

        ``POST /api/comm/v1/cstalk/end`` (``endCounselSession``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselEndRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``CounselEndResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_end_counsel_session(self._transport.call(_call_end_counsel_session(body=body)))

    def end_with_bot(self, body: _q.CounselEndWithBotRequest | Mapping[str, Any]) -> _r.CounselEndResult:
        """상담 종료 및 봇 전환.

        상담 세션을 종료한 뒤 봇 이벤트 말블록을 실행합니다. 처리 결과는 발송 결과 웹훅(`counselResult`, requestType `endwithbot`)으로도 전달됩니다.

        ``POST /api/comm/v1/cstalk/endWithBot`` (``endCounselSessionWithBot``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselEndWithBotRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``CounselEndResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_end_counsel_session_with_bot(self._transport.call(_call_end_counsel_session_with_bot(body=body)))

    def get(self, *, user_key: str) -> _r.CounselSessionResult:
        """세션 조회.

        사용자 키 기준으로 현재 상담 세션 정보를 조회합니다.

        ``GET /api/comm/v1/center/cstalk/session`` (``getCounselSession``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            user_key: 상담톡 사용자 키입니다. 1~20자입니다.

        Returns:
            ``CounselSessionResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_counsel_session(self._transport.call(_call_get_counsel_session(user_key=user_key)))


class AsyncCounselSessions:
    """``client.counsel.sessions`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def end(self, body: _q.CounselEndRequest | Mapping[str, Any]) -> _r.CounselEndResult:
        """상담 종료.

        현재 열려 있는 상담 세션을 종료합니다. 처리 결과는 발송 결과 웹훅(`counselResult`, requestType `end`)으로도 전달됩니다.

        ``POST /api/comm/v1/cstalk/end`` (``endCounselSession``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselEndRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``CounselEndResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_end_counsel_session(await self._transport.call(_call_end_counsel_session(body=body)))

    async def end_with_bot(self, body: _q.CounselEndWithBotRequest | Mapping[str, Any]) -> _r.CounselEndResult:
        """상담 종료 및 봇 전환.

        상담 세션을 종료한 뒤 봇 이벤트 말블록을 실행합니다. 처리 결과는 발송 결과 웹훅(`counselResult`, requestType `endwithbot`)으로도 전달됩니다.

        ``POST /api/comm/v1/cstalk/endWithBot`` (``endCounselSessionWithBot``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselEndWithBotRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``CounselEndResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_end_counsel_session_with_bot(
            await self._transport.call(_call_end_counsel_session_with_bot(body=body))
        )

    async def get(self, *, user_key: str) -> _r.CounselSessionResult:
        """세션 조회.

        사용자 키 기준으로 현재 상담 세션 정보를 조회합니다.

        ``GET /api/comm/v1/center/cstalk/session`` (``getCounselSession``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            user_key: 상담톡 사용자 키입니다. 1~20자입니다.

        Returns:
            ``CounselSessionResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_counsel_session(await self._transport.call(_call_get_counsel_session(user_key=user_key)))


class CounselUsers:
    """``client.counsel.users``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def block(self, body: _q.CounselUserBlockRequest | Mapping[str, Any]) -> None:
        """사용자 수신 차단.

        특정 사용자의 상담톡 수신을 차단합니다. 차단하면 해당 사용자의 상담 세션도 종료됩니다.

        ``POST /api/comm/v1/center/cstalk/profile/user/block`` (``blockCounselUser``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselUserBlockRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_block_counsel_user(body=body))

    def unblock(self, body: _q.CounselUserBlockRequest | Mapping[str, Any]) -> None:
        """사용자 수신 차단 해제.

        차단된 사용자의 상담톡 수신 차단을 해제합니다.

        ``POST /api/comm/v1/center/cstalk/profile/user/unblock`` (``unblockCounselUser``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselUserBlockRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_unblock_counsel_user(body=body))


class AsyncCounselUsers:
    """``client.counsel.users`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def block(self, body: _q.CounselUserBlockRequest | Mapping[str, Any]) -> None:
        """사용자 수신 차단.

        특정 사용자의 상담톡 수신을 차단합니다. 차단하면 해당 사용자의 상담 세션도 종료됩니다.

        ``POST /api/comm/v1/center/cstalk/profile/user/block`` (``blockCounselUser``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselUserBlockRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_block_counsel_user(body=body))

    async def unblock(self, body: _q.CounselUserBlockRequest | Mapping[str, Any]) -> None:
        """사용자 수신 차단 해제.

        차단된 사용자의 상담톡 수신 차단을 해제합니다.

        ``POST /api/comm/v1/center/cstalk/profile/user/unblock`` (``unblockCounselUser``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselUserBlockRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_unblock_counsel_user(body=body))


class CounselCerts:
    """``client.counsel.certs``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get(self, *, cert_tx_id: str) -> _r.CounselCertStatusResult:
        """카카오톡 인증 상태 조회.

        인증 트랜잭션 ID로 사용자의 카카오톡 인증(전자서명) 진행 상태를 조회합니다. 최종 결과(암호화된 인증정보)는 `counselCertResult` 웹훅으로 받습니다.

        ``GET /api/comm/v1/center/cstalk/cert/status`` (``getCounselCertStatus``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            cert_tx_id: 인증 트랜잭션 ID입니다. 카카오가 인증 요청 시 발급하며 `counselCertResult` 웹훅의 `certTxId`와 같습니다.

        Returns:
            ``CounselCertStatusResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_counsel_cert_status(
            self._transport.call(_call_get_counsel_cert_status(cert_tx_id=cert_tx_id))
        )


class AsyncCounselCerts:
    """``client.counsel.certs`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get(self, *, cert_tx_id: str) -> _r.CounselCertStatusResult:
        """카카오톡 인증 상태 조회.

        인증 트랜잭션 ID로 사용자의 카카오톡 인증(전자서명) 진행 상태를 조회합니다. 최종 결과(암호화된 인증정보)는 `counselCertResult` 웹훅으로 받습니다.

        ``GET /api/comm/v1/center/cstalk/cert/status`` (``getCounselCertStatus``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            cert_tx_id: 인증 트랜잭션 ID입니다. 카카오가 인증 요청 시 발급하며 `counselCertResult` 웹훅의 `certTxId`와 같습니다.

        Returns:
            ``CounselCertStatusResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_counsel_cert_status(
            await self._transport.call(_call_get_counsel_cert_status(cert_tx_id=cert_tx_id))
        )


class CounselFiles:
    """``client.counsel.files``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def upload_image(
        self,
        file: FileInput,
        *,
        sender_key: str,
        file_key: str | None = None,
        image_name: str | None = None,
        image_type: str | None = None,
        filename: str | None = None,
    ) -> _r.CounselImageUploadResult:
        """상담톡 이미지 업로드.

        상담톡 이미지(jpg, png, gif, 최대 5MB)를 올리고 `imgUrl`을 받습니다. Rich 메시지용은 `imageType=rich`로 올립니다.

        ``POST /api/comm/v1/file/cstalk/image`` (``uploadCounselImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 상담톡 이미지 파일입니다. jpg, png, gif 형식, 최대 5MB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.
            sender_key: 카카오 비즈메시지 발신프로필 키입니다.
            image_type: 이미지 타입입니다. Rich 메시지 이미지 업로드 시 `rich`를 입력합니다.

        Returns:
            ``CounselImageUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_counsel_image(
            self._transport.call(
                _call_upload_counsel_image(
                    file=file,
                    sender_key=sender_key,
                    file_key=file_key,
                    image_name=image_name,
                    image_type=image_type,
                    filename=filename,
                )
            )
        )

    def upload(
        self,
        file: FileInput,
        *,
        sender_key: str,
        file_key: str | None = None,
        image_name: str | None = None,
        file_type: Literal["file", "audio", "video"] | None = None,
        filename: str | None = None,
    ) -> _r.CounselFileUploadResult:
        """상담톡 파일 업로드.

        상담톡 FILE·AUDIO·VIDEO 타입 첨부 파일을 올리고 `fileUrl`을 받습니다. 운영은 최대 300MB, 샌드박스는 최대 10MB입니다.

        ``POST /api/comm/v1/file/cstalk`` (``uploadCounselFile``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 파일 바이너리입니다. 운영 환경은 최대 300MB, 샌드박스는 최대 10MB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.
            sender_key: 카카오 비즈메시지 발신프로필 키입니다.
            file_type: 파일 타입입니다. `file`은 일반 파일, `audio`는 오디오 파일, `video`는 비디오 파일입니다.

        Returns:
            ``CounselFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_counsel_file(
            self._transport.call(
                _call_upload_counsel_file(
                    file=file,
                    sender_key=sender_key,
                    file_key=file_key,
                    image_name=image_name,
                    file_type=file_type,
                    filename=filename,
                )
            )
        )


class AsyncCounselFiles:
    """``client.counsel.files`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def upload_image(
        self,
        file: FileInput,
        *,
        sender_key: str,
        file_key: str | None = None,
        image_name: str | None = None,
        image_type: str | None = None,
        filename: str | None = None,
    ) -> _r.CounselImageUploadResult:
        """상담톡 이미지 업로드.

        상담톡 이미지(jpg, png, gif, 최대 5MB)를 올리고 `imgUrl`을 받습니다. Rich 메시지용은 `imageType=rich`로 올립니다.

        ``POST /api/comm/v1/file/cstalk/image`` (``uploadCounselImage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 상담톡 이미지 파일입니다. jpg, png, gif 형식, 최대 5MB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.
            sender_key: 카카오 비즈메시지 발신프로필 키입니다.
            image_type: 이미지 타입입니다. Rich 메시지 이미지 업로드 시 `rich`를 입력합니다.

        Returns:
            ``CounselImageUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_counsel_image(
            await self._transport.call(
                _call_upload_counsel_image(
                    file=file,
                    sender_key=sender_key,
                    file_key=file_key,
                    image_name=image_name,
                    image_type=image_type,
                    filename=filename,
                )
            )
        )

    async def upload(
        self,
        file: FileInput,
        *,
        sender_key: str,
        file_key: str | None = None,
        image_name: str | None = None,
        file_type: Literal["file", "audio", "video"] | None = None,
        filename: str | None = None,
    ) -> _r.CounselFileUploadResult:
        """상담톡 파일 업로드.

        상담톡 FILE·AUDIO·VIDEO 타입 첨부 파일을 올리고 `fileUrl`을 받습니다. 운영은 최대 300MB, 샌드박스는 최대 10MB입니다.

        ``POST /api/comm/v1/file/cstalk`` (``uploadCounselFile``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            file: 업로드할 파일 바이너리입니다. 운영 환경은 최대 300MB, 샌드박스는 최대 10MB입니다.
            file_key: 업로드 파일을 식별하는 키입니다. 생략하면 서버가 자동으로 생성합니다.
            image_name: 업로드 파일의 이름입니다. 생략하면 확장자를 제외한 파일명을 사용합니다.
            sender_key: 카카오 비즈메시지 발신프로필 키입니다.
            file_type: 파일 타입입니다. `file`은 일반 파일, `audio`는 오디오 파일, `video`는 비디오 파일입니다.

        Returns:
            ``CounselFileUploadResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_upload_counsel_file(
            await self._transport.call(
                _call_upload_counsel_file(
                    file=file,
                    sender_key=sender_key,
                    file_key=file_key,
                    image_name=image_name,
                    file_type=file_type,
                    filename=filename,
                )
            )
        )


class CounselChannels:
    """``client.counsel.channels``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def activate(self, body: _q.CounselSenderActivationRequest | Mapping[str, Any]) -> None:
        """상담톡 이용 활성화.

        발신프로필의 상담톡 이용을 활성화합니다.

        ``POST /api/comm/v1/center/cstalk/sender/activate`` (``activateCounsel``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselSenderActivationRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_activate_counsel(body=body))

    def deactivate(self, body: _q.CounselSenderActivationRequest | Mapping[str, Any]) -> None:
        """상담톡 이용 비활성화.

        발신프로필의 상담톡 이용을 비활성화합니다. 해지하면 저장된 상담시간이 삭제됩니다.

        ``POST /api/comm/v1/center/cstalk/sender/deactivate`` (``deactivateCounsel``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselSenderActivationRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_deactivate_counsel(body=body))

    def activate_chat(self, body: _q.CounselSenderRequest | Mapping[str, Any]) -> None:
        """채팅 기능 활성화.

        카카오톡 채널의 채팅 기능을 활성화합니다.

        ``POST /api/comm/v1/center/cstalk/sender/chat/activate`` (``activateCounselChat``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselSenderRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_activate_counsel_chat(body=body))

    def deactivate_chat(self, body: _q.CounselSenderRequest | Mapping[str, Any]) -> None:
        """채팅 기능 비활성화.

        카카오톡 채널의 채팅 기능을 비활성화합니다.

        ``POST /api/comm/v1/center/cstalk/sender/chat/deactivate`` (``deactivateCounselChat``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselSenderRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_deactivate_counsel_chat(body=body))


class AsyncCounselChannels:
    """``client.counsel.channels`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def activate(self, body: _q.CounselSenderActivationRequest | Mapping[str, Any]) -> None:
        """상담톡 이용 활성화.

        발신프로필의 상담톡 이용을 활성화합니다.

        ``POST /api/comm/v1/center/cstalk/sender/activate`` (``activateCounsel``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselSenderActivationRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_activate_counsel(body=body))

    async def deactivate(self, body: _q.CounselSenderActivationRequest | Mapping[str, Any]) -> None:
        """상담톡 이용 비활성화.

        발신프로필의 상담톡 이용을 비활성화합니다. 해지하면 저장된 상담시간이 삭제됩니다.

        ``POST /api/comm/v1/center/cstalk/sender/deactivate`` (``deactivateCounsel``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselSenderActivationRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_deactivate_counsel(body=body))

    async def activate_chat(self, body: _q.CounselSenderRequest | Mapping[str, Any]) -> None:
        """채팅 기능 활성화.

        카카오톡 채널의 채팅 기능을 활성화합니다.

        ``POST /api/comm/v1/center/cstalk/sender/chat/activate`` (``activateCounselChat``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselSenderRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_activate_counsel_chat(body=body))

    async def deactivate_chat(self, body: _q.CounselSenderRequest | Mapping[str, Any]) -> None:
        """채팅 기능 비활성화.

        카카오톡 채널의 채팅 기능을 비활성화합니다.

        ``POST /api/comm/v1/center/cstalk/sender/chat/deactivate`` (``deactivateCounselChat``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselSenderRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_deactivate_counsel_chat(body=body))


class CounselConsultTime:
    """``client.counsel.consult_time``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get(self, *, sender_key: str) -> _r.CounselConsultTimeResult:
        """상담시간 조회.

        상담 운영 시간(요일별)을 조회합니다.

        ``GET /api/comm/v1/center/cstalk/consult/time`` (``getCounselConsultTime``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 카카오 비즈메시지 발신프로필 키입니다.

        Returns:
            ``CounselConsultTimeResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_counsel_consult_time(
            self._transport.call(_call_get_counsel_consult_time(sender_key=sender_key))
        )

    def save(self, body: _q.CounselConsultTimeSaveRequest | Mapping[str, Any]) -> None:
        """상담시간 저장.

        카카오톡 채널의 상담시간을 저장합니다. 한 번 등록하면 수정만 가능하며, 상담톡 이용을 해지하면 삭제됩니다.
        상담시간은 카카오톡 채널 홈에 노출되며, 확인하려면 채팅 기능이 활성화되어 있어야 합니다.

        ``POST /api/comm/v1/center/cstalk/consult/time`` (``saveCounselConsultTime``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselConsultTimeSaveRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_save_counsel_consult_time(body=body))


class AsyncCounselConsultTime:
    """``client.counsel.consult_time`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get(self, *, sender_key: str) -> _r.CounselConsultTimeResult:
        """상담시간 조회.

        상담 운영 시간(요일별)을 조회합니다.

        ``GET /api/comm/v1/center/cstalk/consult/time`` (``getCounselConsultTime``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 카카오 비즈메시지 발신프로필 키입니다.

        Returns:
            ``CounselConsultTimeResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_get_counsel_consult_time(
            await self._transport.call(_call_get_counsel_consult_time(sender_key=sender_key))
        )

    async def save(self, body: _q.CounselConsultTimeSaveRequest | Mapping[str, Any]) -> None:
        """상담시간 저장.

        카카오톡 채널의 상담시간을 저장합니다. 한 번 등록하면 수정만 가능하며, 상담톡 이용을 해지하면 삭제됩니다.
        상담시간은 카카오톡 채널 홈에 노출되며, 확인하려면 채팅 기능이 활성화되어 있어야 합니다.

        ``POST /api/comm/v1/center/cstalk/consult/time`` (``saveCounselConsultTime``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselConsultTimeSaveRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_save_counsel_consult_time(body=body))


class CounselSystemMessages:
    """``client.counsel.system_messages``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(self, *, sender_key: str, id: str | None = None) -> _r.CounselSystemMessageListResult:
        """시스템 메시지 조회.

        시스템 메시지 목록을 조회합니다. `id`를 주면 해당 메시지만 조회합니다. 페이지네이션은 문서에 없습니다.

        ``GET /api/comm/v1/center/cstalk/system/message`` (``listCounselSystemMessages``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 카카오 비즈메시지 발신프로필 키입니다.
            id: 시스템 메시지 ID입니다. 특정 메시지만 조회할 때 입력합니다.

        Returns:
            ``CounselSystemMessageListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_counsel_system_messages(
            self._transport.call(_call_list_counsel_system_messages(sender_key=sender_key, id=id))
        )

    def create(
        self, body: _q.CounselSystemMessageCreateRequest | Mapping[str, Any]
    ) -> _r.CounselSystemMessageCreateResult:
        """시스템 메시지 등록.

        시스템 메시지를 등록합니다.

        ``POST /api/comm/v1/center/cstalk/system/message`` (``createCounselSystemMessage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselSystemMessageCreateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``CounselSystemMessageCreateResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_counsel_system_message(
            self._transport.call(_call_create_counsel_system_message(body=body))
        )

    def delete(self, sender_key: str, id: str) -> None:
        """시스템 메시지 삭제.

        시스템 메시지를 삭제합니다.

        ``DELETE /api/comm/v1/center/cstalk/system/message/senderKey/{senderKey}/id/{id}`` (``deleteCounselSystemMessage``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다. URL 인코딩해서 넣습니다.
            id: 삭제할 시스템 메시지 ID입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_delete_counsel_system_message(sender_key=sender_key, id=id))

    def request_approval(self, body: _q.CounselSenderRequest | Mapping[str, Any]) -> None:
        """시스템 메시지 검수 요청.

        시스템 메시지 검수를 요청합니다.

        ``POST /api/comm/v1/center/cstalk/system/message/approval/request`` (``requestCounselSystemMessageApproval``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselSenderRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_request_counsel_system_message_approval(body=body))

    def cancel_approval(self, body: _q.CounselSenderRequest | Mapping[str, Any]) -> None:
        """시스템 메시지 검수 취소.

        시스템 메시지 검수 요청을 취소합니다.

        ``POST /api/comm/v1/center/cstalk/system/message/approval/cancel`` (``cancelCounselSystemMessageApproval``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselSenderRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        self._transport.call(_call_cancel_counsel_system_message_approval(body=body))


class AsyncCounselSystemMessages:
    """``client.counsel.system_messages`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(self, *, sender_key: str, id: str | None = None) -> _r.CounselSystemMessageListResult:
        """시스템 메시지 조회.

        시스템 메시지 목록을 조회합니다. `id`를 주면 해당 메시지만 조회합니다. 페이지네이션은 문서에 없습니다.

        ``GET /api/comm/v1/center/cstalk/system/message`` (``listCounselSystemMessages``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 카카오 비즈메시지 발신프로필 키입니다.
            id: 시스템 메시지 ID입니다. 특정 메시지만 조회할 때 입력합니다.

        Returns:
            ``CounselSystemMessageListResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_list_counsel_system_messages(
            await self._transport.call(_call_list_counsel_system_messages(sender_key=sender_key, id=id))
        )

    async def create(
        self, body: _q.CounselSystemMessageCreateRequest | Mapping[str, Any]
    ) -> _r.CounselSystemMessageCreateResult:
        """시스템 메시지 등록.

        시스템 메시지를 등록합니다.

        ``POST /api/comm/v1/center/cstalk/system/message`` (``createCounselSystemMessage``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselSystemMessageCreateRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            ``CounselSystemMessageCreateResult`` (응답에 데이터가 없으면 빈 객체, None을 돌려주지 않음). 모델은 ``bizgo.models._generated_response``에 있습니다.

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        return _parse_create_counsel_system_message(
            await self._transport.call(_call_create_counsel_system_message(body=body))
        )

    async def delete(self, sender_key: str, id: str) -> None:
        """시스템 메시지 삭제.

        시스템 메시지를 삭제합니다.

        ``DELETE /api/comm/v1/center/cstalk/system/message/senderKey/{senderKey}/id/{id}`` (``deleteCounselSystemMessage``). 429·5xx·네트워크 오류 재시도, 속도 제한 버킷: ``other``.

        Args:
            sender_key: 발신프로필 키입니다. URL 인코딩해서 넣습니다.
            id: 삭제할 시스템 메시지 ID입니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_delete_counsel_system_message(sender_key=sender_key, id=id))

    async def request_approval(self, body: _q.CounselSenderRequest | Mapping[str, Any]) -> None:
        """시스템 메시지 검수 요청.

        시스템 메시지 검수를 요청합니다.

        ``POST /api/comm/v1/center/cstalk/system/message/approval/request`` (``requestCounselSystemMessageApproval``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselSenderRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_request_counsel_system_message_approval(body=body))

    async def cancel_approval(self, body: _q.CounselSenderRequest | Mapping[str, Any]) -> None:
        """시스템 메시지 검수 취소.

        시스템 메시지 검수 요청을 취소합니다.

        ``POST /api/comm/v1/center/cstalk/system/message/approval/cancel`` (``cancelCounselSystemMessageApproval``). 429만 재시도, 속도 제한 버킷: ``other``.

        Args:
            body: :class:`~bizgo.models.CounselSenderRequest` 또는 API 필드 이름의 dict. 보내기 전에 검증합니다.

        Returns:
            None (응답에 데이터가 없습니다).

        Raises:
            ValueError: 요청 값이 스펙 규칙에 맞지 않습니다(보내기 전).
            bizgo.APIError: 비즈고가 요청을 거절했습니다.
        """
        await self._transport.call(_call_cancel_counsel_system_message_approval(body=body))


class Counsel:
    """``client.counsel``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport
        self.messages = CounselMessages(transport)
        self.sessions = CounselSessions(transport)
        self.users = CounselUsers(transport)
        self.certs = CounselCerts(transport)
        self.files = CounselFiles(transport)
        self.channels = CounselChannels(transport)
        self.consult_time = CounselConsultTime(transport)
        self.system_messages = CounselSystemMessages(transport)


class AsyncCounsel:
    """``client.counsel`` (async)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport
        self.messages = AsyncCounselMessages(transport)
        self.sessions = AsyncCounselSessions(transport)
        self.users = AsyncCounselUsers(transport)
        self.certs = AsyncCounselCerts(transport)
        self.files = AsyncCounselFiles(transport)
        self.channels = AsyncCounselChannels(transport)
        self.consult_time = AsyncCounselConsultTime(transport)
        self.system_messages = AsyncCounselSystemMessages(transport)


class Resources:
    """Top-level resources generated from the spec (mixed into :class:`bizgo.Bizgo`)."""

    reservations: Reservations
    insights: Insights
    kakao: Kakao
    alimtalk: Alimtalk
    brand_message: BrandMessage
    rcs: Rcs
    counsel: Counsel

    def _init_resources(self, transport: SyncTransport) -> None:
        self.reservations = Reservations(transport)
        self.insights = Insights(transport)
        self.kakao = Kakao(transport)
        self.alimtalk = Alimtalk(transport)
        self.brand_message = BrandMessage(transport)
        self.rcs = Rcs(transport)
        self.counsel = Counsel(transport)


class AsyncResources:
    """Async version of :class:`Resources`."""

    reservations: AsyncReservations
    insights: AsyncInsights
    kakao: AsyncKakao
    alimtalk: AsyncAlimtalk
    brand_message: AsyncBrandMessage
    rcs: AsyncRcs
    counsel: AsyncCounsel

    def _init_resources(self, transport: AsyncTransport) -> None:
        self.reservations = AsyncReservations(transport)
        self.insights = AsyncInsights(transport)
        self.kakao = AsyncKakao(transport)
        self.alimtalk = AsyncAlimtalk(transport)
        self.brand_message = AsyncBrandMessage(transport)
        self.rcs = AsyncRcs(transport)
        self.counsel = AsyncCounsel(transport)

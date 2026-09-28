"""Generated from spec/openapi.yaml by scripts/generate_models.py. Do not edit."""

from __future__ import annotations

from typing import Any, Literal

from bizgo._base import ResponseModel
from pydantic import ConfigDict, Field


class AlimtalkButton(ResponseModel):
    """
    알림톡 버튼입니다. 버튼 타입에 따라 필요한 필드가 다릅니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    type: str = Field(..., examples=['WL'])
    """
    카카오 버튼 타입 코드입니다. 문서 예시에 나온 값은 `WL`(웹 링크)입니다.
    """
    name: str
    """
    카카오 버튼명입니다.
    """
    url_pc: str | None = Field(default=None, validation_alias='urlPc', serialization_alias='urlPc')
    """
    PC 환경에서 버튼 클릭 시 이동할 URL입니다.
    """
    url_mobile: str | None = Field(default=None, validation_alias='urlMobile', serialization_alias='urlMobile')
    """
    모바일 환경에서 버튼 클릭 시 이동할 URL입니다.
    """
    scheme_ios: str | None = Field(default=None, validation_alias='schemeIos', serialization_alias='schemeIos')
    """
    iOS 환경에서 버튼 클릭 시 실행할 커스텀 스킴입니다.
    """
    scheme_android: str | None = Field(default=None, validation_alias='schemeAndroid', serialization_alias='schemeAndroid')
    """
    Android 환경에서 버튼 클릭 시 실행할 커스텀 스킴입니다.
    """
    target: str | None = None
    """
    웹 링크 버튼의 target 값입니다. `type`이 `WL`이고 `target`이 `out`이면 아웃링크로 동작합니다.
    """
    chat_extra: str | None = Field(default=None, validation_alias='chatExtra', serialization_alias='chatExtra')
    """
    봇/상담톡 전환 시 전달할 메타 정보입니다.
    """
    chat_event: str | None = Field(default=None, validation_alias='chatEvent', serialization_alias='chatEvent')
    """
    봇/상담톡 전환 시 연결할 이벤트명입니다.
    """
    plugin_id: str | None = Field(default=None, validation_alias='pluginId', serialization_alias='pluginId')
    """
    비즈플러그인 ID입니다.
    """
    relay_id: str | None = Field(default=None, validation_alias='relayId', serialization_alias='relayId')
    """
    비즈플러그인 relay ID입니다. 비즈플러그인 실행 시 `X-Kakao-Plugin-Relay-Id` 헤더로 전달됩니다.
    """
    oneclick_id: str | None = Field(default=None, validation_alias='oneclickId', serialization_alias='oneclickId')
    """
    원클릭 결제 정보 ID입니다.
    """
    product_id: str | None = Field(default=None, validation_alias='productId', serialization_alias='productId')
    """
    원클릭 결제 상품 ID입니다.
    """
    biz_form_key: str | None = Field(default=None, validation_alias='bizFormKey', serialization_alias='bizFormKey')
    """
    비즈폼 키입니다.
    """
    biz_form_id: str | None = Field(default=None, validation_alias='bizFormId', serialization_alias='bizFormId')
    """
    비즈폼 ID입니다.
    """
    tel_number: str | None = Field(default=None, validation_alias='telNumber', serialization_alias='telNumber')
    """
    전화번호입니다.
    """


class AlimtalkItemHighlight(ResponseModel):
    """
    알림톡 아이템 하이라이트 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    title: str = Field(..., max_length=30)
    """
    아이템 하이라이트 타이틀입니다. 최대 30자이며, 이미지가 있으면 최대 21자입니다.
    """
    description: str = Field(..., max_length=19)
    """
    아이템 하이라이트 부가정보입니다. 최대 19자이며, 이미지가 있으면 최대 13자입니다.
    """


class AlimtalkItemListEntry(ResponseModel):
    """
    알림톡 아이템 리스트의 항목 1개입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    title: str = Field(..., max_length=6)
    """
    아이템 타이틀입니다. 최대 6자입니다.
    """
    description: str = Field(..., max_length=23)
    """
    아이템 부가정보입니다. 최대 23자입니다.
    """


class AlimtalkItemSummary(ResponseModel):
    """
    알림톡 아이템 요약 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    title: str = Field(..., max_length=6)
    """
    요약 타이틀입니다. 최대 6자입니다.
    """
    description: str = Field(..., max_length=14)
    """
    요약 가격정보입니다. 최대 14자입니다.
    허용 문자: 통화 기호(유니코드 통화 기호, 元, 円, 원), 통화 코드(ISO 4217), 숫자, 쉼표, 소수점, 공백. 소수점 이하는 2자리까지 허용합니다.

    """


class AlimtalkLink(ResponseModel):
    """
    알림톡 대표 링크 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    url_pc: str = Field(..., validation_alias='urlPc', serialization_alias='urlPc')
    """
    PC 환경에서 클릭 시 이동할 URL입니다.
    """
    url_mobile: str = Field(..., validation_alias='urlMobile', serialization_alias='urlMobile')
    """
    모바일 환경에서 클릭 시 이동할 URL입니다.
    """
    scheme_android: str | None = Field(default=None, validation_alias='schemeAndroid', serialization_alias='schemeAndroid')
    """
    Android 커스텀 스킴입니다.
    """
    scheme_ios: str | None = Field(default=None, validation_alias='schemeIos', serialization_alias='schemeIos')
    """
    iOS 커스텀 스킴입니다.
    """


class AlimtalkQuickReply(ResponseModel):
    """
    알림톡 바로연결 1개입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    type: str
    """
    바로연결 타입 코드입니다.
    """
    name: str
    """
    바로연결 제목입니다. 템플릿 등록 규격상 최대 14자입니다.
    """
    url_pc: str | None = Field(default=None, validation_alias='urlPc', serialization_alias='urlPc')
    """
    PC 환경에서 클릭 시 이동할 URL입니다.
    """
    url_mobile: str | None = Field(default=None, validation_alias='urlMobile', serialization_alias='urlMobile')
    """
    모바일 환경에서 클릭 시 이동할 URL입니다.
    """
    scheme_ios: str | None = Field(default=None, validation_alias='schemeIos', serialization_alias='schemeIos')
    """
    iOS 커스텀 스킴입니다.
    """
    scheme_android: str | None = Field(default=None, validation_alias='schemeAndroid', serialization_alias='schemeAndroid')
    """
    Android 커스텀 스킴입니다.
    """
    chat_extra: str | None = Field(default=None, validation_alias='chatExtra', serialization_alias='chatExtra')
    """
    봇/상담톡 전환 시 전달할 메타 정보입니다.
    """
    chat_event: str | None = Field(default=None, validation_alias='chatEvent', serialization_alias='chatEvent')
    """
    봇/상담톡 전환 시 연결할 이벤트명입니다.
    """
    biz_form_id: str | None = Field(default=None, validation_alias='bizFormId', serialization_alias='bizFormId')
    """
    비즈폼 ID입니다.
    """


class AlimtalkSupplement(ResponseModel):
    """
    메시지에 첨부할 바로연결 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    quick_reply: list[AlimtalkQuickReply] | None = Field(default=None, validation_alias='quickReply', serialization_alias='quickReply')
    """
    바로연결 정보입니다.
    """


class AlimtalkTemplateCategory(ResponseModel):
    """
    알림톡 템플릿 카테고리입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    code: str | None = None
    """
    카테고리 코드입니다.
    """
    name: str | None = None
    """
    카테고리 이름입니다.
    """
    group_name: str | None = Field(default=None, validation_alias='groupName', serialization_alias='groupName')
    """
    카테고리 그룹 이름입니다.
    """
    inclusion: str | None = None
    """
    포함 기준 설명입니다.
    """
    exclusion: str | None = None
    """
    제외 기준 설명입니다.
    """


class AlimtalkTemplateCategoryResult(ResponseModel):
    """
    템플릿 카테고리 조회 응답 데이터입니다.
    `categoryCode` 없이 호출하면 `categories`(전체 목록), `categoryCode`를 주면 `category`(상세 1건)가 옵니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    categories: list[AlimtalkTemplateCategory] | None = None
    """
    템플릿 카테고리 목록입니다(전체 조회).
    """
    category: AlimtalkTemplateCategory | None = None


class AlimtalkTemplateComment(ResponseModel):
    """
    템플릿 심사 의견 1건입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: int | None = None
    """
    심사 의견 ID입니다.
    """
    user_name: str | None = Field(default=None, validation_alias='userName', serialization_alias='userName')
    """
    심사 의견을 남긴 담당자명입니다.
    """
    created_at: str | None = Field(default=None, validation_alias='createdAt', serialization_alias='createdAt')
    """
    심사 의견 등록일입니다.
    """
    status: str | None = None
    """
    해당 의견 시점의 심사 상태입니다.
    """
    attachment: list[dict[str, Any]] | None = None
    """
    심사 의견에 첨부된 파일 목록입니다.
    """


class AlimtalkTemplateImageUploadResult(ResponseModel):
    """
    알림톡 템플릿 이미지·아이템 하이라이트 이미지 업로드 결과입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    img_url: str | None = Field(
        default=None,
        validation_alias='imgUrl', serialization_alias='imgUrl',
        examples=['https://example.kakao.image/template-image.jpg'],
    )
    """
    업로드된 이미지 URL입니다. 템플릿 등록의 `imgUrl`에 씁니다.
    """
    file_name: str | None = Field(
        default=None, validation_alias='fileName', serialization_alias='fileName', examples=['template-image.jpg']
    )
    """
    업로드된 이미지 파일 이름입니다.
    """


class AlimtalkTemplatePublic(ResponseModel):
    """
    카카오가 제공하는 공용템플릿 1건입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    template_name: str | None = Field(default=None, validation_alias='templateName', serialization_alias='templateName')
    """
    공용 템플릿 이름입니다.
    """
    template_code: str | None = Field(
        default=None, validation_alias='templateCode', serialization_alias='templateCode', examples=['TEMPLATE_CODE_EXAMPLE']
    )
    """
    공용 템플릿 코드입니다.
    """
    status: str | None = None
    """
    공용 템플릿 상태입니다. 문서 예시 값은 `APR`입니다.
    """
    category_code: str | None = Field(default=None, validation_alias='categoryCode', serialization_alias='categoryCode')
    """
    카테고리 코드입니다.
    """
    release_date: str | None = Field(
        default=None, validation_alias='releaseDate', serialization_alias='releaseDate', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    공용 템플릿 배포 일시(yyyy-MM-dd HH:mm:ss)입니다.
    """
    preview_image_url: str | None = Field(default=None, validation_alias='previewImageUrl', serialization_alias='previewImageUrl')
    """
    미리보기 이미지 URL입니다.
    """


class AlimtalkTemplatePublicListResult(ResponseModel):
    """
    공용템플릿 조회 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    templates: list[AlimtalkTemplatePublic] | None = None
    """
    공용 템플릿 목록입니다.
    """


class Brandmessage(ResponseModel):
    """
    동보 발송 예상 시간 결과입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    estimated_finished_at: str | None = Field(
        default=None,
        validation_alias='estimatedFinishedAt', serialization_alias='estimatedFinishedAt',
        examples=['2026-04-08T16:58:00'],
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss"},
    )
    """
    예상 종료 시각(`yyyy-MM-dd'T'HH:mm:ss`, KST)입니다.
    """
    duration: int | None = Field(default=None, examples=[18])
    """
    예상 소요 시간(분)입니다.
    """


class BrandMessageAudienceEstimateResult(ResponseModel):
    """
    예상 시간 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brandmessage: Brandmessage | None = None
    """
    동보 발송 예상 시간 결과입니다.
    """


class Brandmessage1(ResponseModel):
    """
    친구 수 조회 결과입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    count: int | None = Field(default=None, examples=[1250])
    """
    보유 친구 수입니다.
    """


class BrandMessageAudienceFriendCountResult(ResponseModel):
    """
    친구 수 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brandmessage: Brandmessage1 | None = None
    """
    친구 수 조회 결과입니다.
    """


class Brandmessage2(ResponseModel):
    """
    동보 발송 가능 수 결과입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    possible: int | None = Field(default=None, examples=[320])
    """
    예상 발송 수입니다.
    """


class BrandMessageAudiencePossibleResult(ResponseModel):
    """
    발송 가능 수 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brandmessage: Brandmessage2 | None = None
    """
    동보 발송 가능 수 결과입니다.
    """


class BrandMessageButton(ResponseModel):
    """
    브랜드메시지 버튼입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    type: str = Field(..., examples=['WL'])
    """
    버튼 타입입니다. 문서에 언급된 값은 `WL`, `AL`입니다.
    """
    name: str | None = Field(default=None, max_length=28)
    """
    버튼명입니다. 최대 28자입니다.
    """
    url_pc: str | None = Field(default=None, validation_alias='urlPc', serialization_alias='urlPc')
    """
    PC 클릭 URL입니다. `WL` 타입에서 필수입니다.
    """
    url_mobile: str | None = Field(default=None, validation_alias='urlMobile', serialization_alias='urlMobile')
    """
    모바일 클릭 URL입니다. `WL`, `AL` 타입에서 필수입니다.
    """
    scheme_ios: str | None = Field(default=None, validation_alias='schemeIos', serialization_alias='schemeIos')
    """
    iOS 커스텀 스킴입니다.
    """
    scheme_android: str | None = Field(default=None, validation_alias='schemeAndroid', serialization_alias='schemeAndroid')
    """
    Android 커스텀 스킴입니다.
    """
    chat_extra: str | None = Field(default=None, validation_alias='chatExtra', serialization_alias='chatExtra')
    """
    봇/상담톡 메타데이터입니다.
    """
    chat_event: str | None = Field(default=None, validation_alias='chatEvent', serialization_alias='chatEvent')
    """
    봇/상담톡 이벤트명입니다.
    """
    biz_form_key: str | None = Field(default=None, validation_alias='bizFormKey', serialization_alias='bizFormKey')
    """
    비즈폼 키입니다.
    """


class BrandMessageCarouselHead(ResponseModel):
    """
    캐러셀 인트로 정보입니다. FC 타입에서는 사용할 수 없습니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    header: str | None = Field(default=None, max_length=20)
    """
    캐러셀 인트로 헤더입니다. 줄바꿈 불가, 최대 20자입니다.
    """
    content: str | None = Field(default=None, max_length=50)
    """
    캐러셀 인트로 내용입니다. 줄바꿈 최대 2회, 최대 50자입니다.
    """
    image_url: str | None = Field(default=None, validation_alias='imageUrl', serialization_alias='imageUrl')
    """
    캐러셀 인트로 이미지 URL입니다.
    """
    url_mobile: str | None = Field(default=None, validation_alias='urlMobile', serialization_alias='urlMobile', max_length=1000)
    """
    모바일 클릭 URL입니다. URL 또는 스킴 중 하나라도 입력하면 필수입니다. 최대 1,000자입니다.
    """
    url_pc: str | None = Field(default=None, validation_alias='urlPc', serialization_alias='urlPc', max_length=1000)
    """
    PC 클릭 URL입니다. 최대 1,000자입니다.
    """
    scheme_android: str | None = Field(default=None, validation_alias='schemeAndroid', serialization_alias='schemeAndroid', max_length=1000)
    """
    Android 커스텀 스킴입니다. 최대 1,000자입니다.
    """
    scheme_ios: str | None = Field(default=None, validation_alias='schemeIos', serialization_alias='schemeIos', max_length=1000)
    """
    iOS 커스텀 스킴입니다. 최대 1,000자입니다.
    """


class BrandMessageCarouselTail(ResponseModel):
    """
    캐러셀 더보기 버튼 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    url_mobile: str = Field(..., validation_alias='urlMobile', serialization_alias='urlMobile', max_length=1000)
    """
    모바일 클릭 URL입니다. 최대 1,000자입니다.
    """
    url_pc: str | None = Field(default=None, validation_alias='urlPc', serialization_alias='urlPc', max_length=1000)
    """
    PC 클릭 URL입니다. 최대 1,000자입니다.
    """
    scheme_ios: str | None = Field(default=None, validation_alias='schemeIos', serialization_alias='schemeIos', max_length=1000)
    """
    iOS 커스텀 스킴입니다. 최대 1,000자입니다.
    """
    scheme_android: str | None = Field(default=None, validation_alias='schemeAndroid', serialization_alias='schemeAndroid', max_length=1000)
    """
    Android 커스텀 스킴입니다. 최대 1,000자입니다.
    """


class BrandMessageCarouselVariable(ResponseModel):
    """
    기본형 변수 분리 방식에서 캐러셀 아이템 1개에 대한 변수입니다(FC, FA).
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    message_variable: dict[str, Any] | None = Field(default=None, validation_alias='messageVariable', serialization_alias='messageVariable')
    """
    캐러셀 메시지 영역 변수입니다. FC, FA 캐러셀 리스트에서 사용합니다.
    """
    button_variable: dict[str, Any] | None = Field(default=None, validation_alias='buttonVariable', serialization_alias='buttonVariable')
    """
    캐러셀 버튼 영역 변수입니다. FC, FA 타입에서 사용합니다.
    """
    coupon_variable: dict[str, Any] | None = Field(default=None, validation_alias='couponVariable', serialization_alias='couponVariable')
    """
    캐러셀 쿠폰 영역 변수입니다. FC, FA 캐러셀 리스트에서 사용합니다.
    """
    image_variable: dict[str, Any] | None = Field(default=None, validation_alias='imageVariable', serialization_alias='imageVariable')
    """
    캐러셀 이미지 영역 변수입니다. FC, FA 캐러셀 리스트에서 사용합니다.
    """
    commerce_variable: dict[str, Any] | None = Field(default=None, validation_alias='commerceVariable', serialization_alias='commerceVariable')
    """
    캐러셀 커머스 영역 변수입니다. FA 캐러셀 리스트에서 사용합니다.
    """


class BrandMessageCatalogItem(ResponseModel):
    """
    브랜드메시지 카탈로그 아이템 1개입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    type: str
    """
    카탈로그 아이템 타입입니다.
    """
    img_url: str | None = Field(default=None, validation_alias='imgUrl', serialization_alias='imgUrl')
    """
    아이템 이미지 URL입니다.
    """
    img_link: str | None = Field(default=None, validation_alias='imgLink', serialization_alias='imgLink')
    """
    이미지 클릭 시 이동할 URL입니다.
    """
    title: str | None = None
    """
    상품명입니다.
    """
    description: str | None = None
    """
    상품 설명입니다.
    """
    regular_price: int | None = Field(default=None, validation_alias='regularPrice', serialization_alias='regularPrice')
    """
    정상 가격입니다.
    """
    discount_price: int | None = Field(default=None, validation_alias='discountPrice', serialization_alias='discountPrice')
    """
    할인 후 가격입니다.
    """
    discount_rate: int | None = Field(default=None, validation_alias='discountRate', serialization_alias='discountRate')
    """
    할인율입니다.
    """
    discount_fixed: int | None = Field(default=None, validation_alias='discountFixed', serialization_alias='discountFixed')
    """
    정액 할인금액입니다.
    """
    regular_price_name: str | None = Field(default=None, validation_alias='regularPriceName', serialization_alias='regularPriceName')
    """
    정상 가격명입니다.
    """
    discount_price_name: str | None = Field(default=None, validation_alias='discountPriceName', serialization_alias='discountPriceName')
    """
    할인 후 가격명입니다.
    """
    regular_price_variable_name: str | None = Field(
        default=None, validation_alias='regularPriceVariableName', serialization_alias='regularPriceVariableName'
    )
    """
    정상 가격 고정변수명입니다.
    """
    discount_price_variable_name: str | None = Field(
        default=None, validation_alias='discountPriceVariableName', serialization_alias='discountPriceVariableName'
    )
    """
    할인 후 가격 고정변수명입니다.
    """
    discount_rate_variable_name: str | None = Field(
        default=None, validation_alias='discountRateVariableName', serialization_alias='discountRateVariableName'
    )
    """
    할인율 고정변수명입니다.
    """
    discount_fixed_variable_name: str | None = Field(
        default=None, validation_alias='discountFixedVariableName', serialization_alias='discountFixedVariableName'
    )
    """
    정액 할인금액 고정변수명입니다.
    """


class BrandMessageCommerce(ResponseModel):
    """
    브랜드메시지 커머스 요소입니다(FM, 캐러셀 커머스 FA).
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    title: str = Field(..., max_length=30)
    """
    상품명입니다. 최대 30자입니다.
    """
    regular_price: int = Field(..., validation_alias='regularPrice', serialization_alias='regularPrice', ge=0, le=99999999)
    """
    정가입니다. 0~99,999,999입니다.
    """
    discount_price: int | None = Field(default=None, validation_alias='discountPrice', serialization_alias='discountPrice', ge=0, le=99999999)
    """
    할인가입니다. 0~99,999,999입니다.
    """
    discount_rate: int | None = Field(default=None, validation_alias='discountRate', serialization_alias='discountRate', ge=1, le=100)
    """
    할인율(%)입니다. `discountPrice`와 함께 씁니다. 허용 범위는 1~100입니다.
    2026년 8월 4일부터 `0`이면 템플릿 등록·발송 요청이 실패하므로, 할인율을 쓰지 않을 때는 `0` 대신 `null`로 보냅니다.

    """
    discount_fixed: int | None = Field(default=None, validation_alias='discountFixed', serialization_alias='discountFixed', ge=0, le=999999)
    """
    정액 할인금액입니다. `discountPrice`와 함께 씁니다. 0~999,999입니다.
    """
    regular_price_name: str | None = Field(default=None, validation_alias='regularPriceName', serialization_alias='regularPriceName')
    """
    정상 가격명입니다.
    """
    discount_price_name: str | None = Field(default=None, validation_alias='discountPriceName', serialization_alias='discountPriceName')
    """
    할인 후 가격명입니다.
    """
    discount_rate_name: str | None = Field(default=None, validation_alias='discountRateName', serialization_alias='discountRateName')
    """
    할인율명입니다.
    """
    discount_fixed_name: str | None = Field(default=None, validation_alias='discountFixedName', serialization_alias='discountFixedName')
    """
    정액 할인금액명입니다.
    """


class BrandMessageCoupon(ResponseModel):
    """
    브랜드메시지 쿠폰 요소입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    title: str
    """
    쿠폰명입니다. `${n}원 할인`, `${n}% 할인`, `배송비 할인`, `${7자 이내} 무료`, `${7자 이내} UP` 형식을 지원합니다.
    """
    description: str = Field(..., max_length=18)
    """
    쿠폰 상세 정보입니다. 와이드(FW)·와이드 리스트(FL)·프리미엄 동영상(FP)은 최대 18자, 그 외(캐러셀 아이템 포함)는 최대 12자입니다.
    """
    url_pc: str | None = Field(default=None, validation_alias='urlPc', serialization_alias='urlPc')
    """
    PC 클릭 URL입니다.
    """
    url_mobile: str | None = Field(default=None, validation_alias='urlMobile', serialization_alias='urlMobile')
    """
    모바일 클릭 URL입니다.
    """
    scheme_android: str | None = Field(default=None, validation_alias='schemeAndroid', serialization_alias='schemeAndroid')
    """
    Android 커스텀 스킴입니다.
    """
    scheme_ios: str | None = Field(default=None, validation_alias='schemeIos', serialization_alias='schemeIos')
    """
    iOS 커스텀 스킴입니다.
    """


class BrandMessageFileUploadResult(ResponseModel):
    """
    브랜드메시지 이미지 업로드 결과입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    img_url: str | None = Field(
        default=None, validation_alias='imgUrl', serialization_alias='imgUrl', examples=['https://example.kakao.image/brand-image.jpg']
    )
    """
    브랜드메시지 템플릿·발송 구성(`attachment.image.imgUrl` 등)에 사용할 이미지 URL입니다.
    """


class BrandMessageFriendGroup(ResponseModel):
    """
    친구 그룹 상세 정보입니다. 동보 발송에 쓰려면 상태가 완료이고 `userCount`가 10 이상이어야 합니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    friend_group_key: str | None = Field(default=None, validation_alias='friendGroupKey', serialization_alias='friendGroupKey')
    """
    친구 그룹 키입니다.
    """
    user_count: int | None = Field(default=None, validation_alias='userCount', serialization_alias='userCount')
    """
    등록 유저 수입니다.
    """
    friend_count: int | None = Field(default=None, validation_alias='friendCount', serialization_alias='friendCount')
    """
    친구 수입니다. `status`가 `IN_PROGRESS`이면 없을 수 있습니다.
    """
    status: str | None = Field(default=None, examples=['COMPLETED'])
    """
    친구 그룹 처리 상태입니다. 알려진 값: `IN_PROGRESS`, `COMPLETED`.
    """
    created_at: str | None = Field(
        default=None, validation_alias='createdAt', serialization_alias='createdAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    생성 일시(`yyyy-MM-dd HH:mm:ss`)입니다.
    """
    modified_at: str | None = Field(
        default=None, validation_alias='modifiedAt', serialization_alias='modifiedAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    수정 일시(`yyyy-MM-dd HH:mm:ss`)입니다.
    """


class FriendGroup(ResponseModel):
    """
    임시 업로드 파일 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    file_key: str | None = Field(default=None, validation_alias='fileKey', serialization_alias='fileKey', examples=['FILE_KEY_001'])
    """
    친구 그룹 등록·전화번호 추가·삭제에 쓸 임시 파일 키입니다.
    """
    expired_at: str | None = Field(
        default=None, validation_alias='expiredAt', serialization_alias='expiredAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    파일 키 만료 일시(`yyyy-MM-dd HH:mm:ss`)입니다.
    """


class BrandMessageFriendGroupFileUploadResult(ResponseModel):
    """
    친구 그룹 파일 업로드 결과입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    friend_group: FriendGroup | None = Field(default=None, validation_alias='friendGroup', serialization_alias='friendGroup')
    """
    임시 업로드 파일 정보입니다.
    """


class BrandMessageFriendGroupListResult(ResponseModel):
    """
    친구 그룹 목록 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    friend_groups: list[BrandMessageFriendGroup] | None = Field(
        default=None, validation_alias='friendGroups', serialization_alias='friendGroups'
    )
    """
    친구 그룹 목록입니다.
    """


class BrandMessageFriendGroupPhoneNumberRequest(ResponseModel):
    """
    친구 그룹 전화번호 추가·삭제 요청 1건의 처리 상태입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    friend_group_key: str | None = Field(default=None, validation_alias='friendGroupKey', serialization_alias='friendGroupKey')
    """
    친구 그룹 키입니다.
    """
    request_id: str | None = Field(
        default=None, validation_alias='requestId', serialization_alias='requestId', examples=['3930171852209730143']
    )
    """
    요청 아이디입니다.
    """
    type: str | None = None
    """
    요청 유형입니다. 문서 예시 값은 `ADD`입니다.
    """
    status: str | None = None
    """
    요청 처리 상태입니다. 문서 예시 값은 `COMPLETED`입니다.
    """
    processed_count: int | None = Field(default=None, validation_alias='processedCount', serialization_alias='processedCount')
    """
    처리된 전화번호 건수입니다.
    """
    created_at: str | None = Field(
        default=None, validation_alias='createdAt', serialization_alias='createdAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    요청 일시(`yyyy-MM-dd HH:mm:ss`)입니다.
    """
    modified_at: str | None = Field(
        default=None, validation_alias='modifiedAt', serialization_alias='modifiedAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    상태 변경 일시(`yyyy-MM-dd HH:mm:ss`)입니다.
    """


class BrandMessageFriendGroupPhoneNumberRequestListResult(ResponseModel):
    """
    전화번호 요청 목록 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    friend_groups: list[BrandMessageFriendGroupPhoneNumberRequest] | None = Field(
        default=None, validation_alias='friendGroups', serialization_alias='friendGroups'
    )
    """
    전화번호 추가·삭제 요청 목록입니다.
    """
    has_next: bool | None = Field(default=None, validation_alias='hasNext', serialization_alias='hasNext')
    """
    다음 페이지 존재 여부입니다.
    """


class BrandMessageFriendGroupPhoneNumberRequestResult(ResponseModel):
    """
    전화번호 요청 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    friend_group: BrandMessageFriendGroupPhoneNumberRequest | None = Field(
        default=None, validation_alias='friendGroup', serialization_alias='friendGroup'
    )
    """
    전화번호 추가·삭제 요청 정보입니다.
    """


class BrandMessageFriendGroupProcessing(ResponseModel):
    """
    친구 그룹 등록·전화번호 추가·삭제 요청의 처리 정보입니다. 처리는 비동기이며 진행 상황은 전화번호 요청 조회 API로 확인합니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    friend_group_key: str | None = Field(default=None, validation_alias='friendGroupKey', serialization_alias='friendGroupKey')
    """
    친구 그룹 키입니다.
    """
    request_id: str | None = Field(
        default=None, validation_alias='requestId', serialization_alias='requestId', examples=['3930171852209730143']
    )
    """
    요청 아이디입니다.
    """
    status: str | None = Field(default=None, examples=['COMPLETED'])
    """
    친구 그룹 처리 상태입니다. 알려진 값: `IN_PROGRESS`, `COMPLETED`.
    """
    created_at: str | None = Field(
        default=None, validation_alias='createdAt', serialization_alias='createdAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    생성 일시(`yyyy-MM-dd HH:mm:ss`)입니다.
    """
    modified_at: str | None = Field(
        default=None, validation_alias='modifiedAt', serialization_alias='modifiedAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    수정 일시(`yyyy-MM-dd HH:mm:ss`)입니다.
    """


class BrandMessageFriendGroupProcessingResult(ResponseModel):
    """
    친구 그룹 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    friend_group: BrandMessageFriendGroupProcessing | None = Field(
        default=None, validation_alias='friendGroup', serialization_alias='friendGroup'
    )
    """
    친구 그룹 정보입니다.
    """


class BrandMessageFriendGroupResult(ResponseModel):
    """
    친구 그룹 상세 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    friend_group: BrandMessageFriendGroup | None = Field(default=None, validation_alias='friendGroup', serialization_alias='friendGroup')
    """
    친구 그룹 상세 정보입니다.
    """


class BrandMessageGroupSend(ResponseModel):
    """
    동보 발송 요청 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    request_id: str | None = Field(default=None, validation_alias='requestId', serialization_alias='requestId', examples=['1203981'])
    """
    동보 발송 요청 아이디입니다.
    """
    status: str | None = Field(default=None, examples=['READY'])
    """
    동보 발송 상태입니다. 알려진 값: `READY`(발송 대기), `SENDING`(발송 중), `PAUSED`(발송 중지), `DONE`(발송 완료), `TERMINATED`(발송 종료), `BLOCKED`(발송 차단).
    """
    send_start_at: str | None = Field(
        default=None, validation_alias='sendStartAt', serialization_alias='sendStartAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    동보 발송 시작 일시(`yyyy-MM-dd HH:mm:ss`, KST)입니다.
    """
    campaign_id: str | None = Field(default=None, validation_alias='campaignId', serialization_alias='campaignId')
    """
    고객 캠페인 식별자입니다.
    """
    tps_limit: int | None = Field(default=None, validation_alias='tpsLimit', serialization_alias='tpsLimit')
    """
    초당 발송 건수 상한입니다.
    """
    push_alarm: Literal['Y', 'N'] | None = Field(default=None, validation_alias='pushAlarm', serialization_alias='pushAlarm')
    """
    메시지 푸시 알림 발송 여부입니다.
    """
    expected_count: int | None = Field(default=None, validation_alias='expectedCount', serialization_alias='expectedCount')
    """
    예상 발송 수입니다.
    """
    send_count: int | None = Field(default=None, validation_alias='sendCount', serialization_alias='sendCount')
    """
    실제 발송 처리 수입니다.
    """
    sender_key: str | None = Field(default=None, validation_alias='senderKey', serialization_alias='senderKey')
    """
    발신프로필 키입니다.
    """
    msg_type: str | None = Field(default=None, validation_alias='msgType', serialization_alias='msgType', examples=['FI'])
    """
    브랜드메시지 메시지 타입입니다.
    """
    template_code: str | None = Field(default=None, validation_alias='templateCode', serialization_alias='templateCode')
    """
    기본형 템플릿 코드입니다.
    """
    friend_group_key: str | None = Field(default=None, validation_alias='friendGroupKey', serialization_alias='friendGroupKey')
    """
    친구 그룹 키입니다. 전체 친구 대상이면 없을 수 있습니다.
    """


class BrandMessageGroupSendResult(ResponseModel):
    """
    동보 발송 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brandmessage: BrandMessageGroupSend | None = None
    """
    동보 발송 기본 정보입니다.
    """


class BrandMessageGroupTag(ResponseModel):
    """
    브랜드메시지 그룹태그입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    group_tag_key: str | None = Field(
        default=None, validation_alias='groupTagKey', serialization_alias='groupTagKey', examples=['GROUP_TAG_KEY_EXAMPLE']
    )
    """
    그룹태그 키입니다.
    """
    group_tag_name: str | None = Field(
        default=None, validation_alias='groupTagName', serialization_alias='groupTagName', examples=['VIP 고객']
    )
    """
    그룹태그 이름입니다.
    """


class BrandMessageGroupTagListResult(ResponseModel):
    """
    그룹태그 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    group_tags: list[BrandMessageGroupTag] | None = Field(default=None, validation_alias='groupTags', serialization_alias='groupTags')
    """
    그룹태그 목록입니다.
    """


class BrandMessageImage(ResponseModel):
    """
    브랜드메시지 이미지 요소입니다. 최상위 `attachment.image`는 FI, FW, FM 타입에서, 캐러셀 아이템의 `attachment.image`는 FC, FA 타입에서 필수입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    img_url: str = Field(..., validation_alias='imgUrl', serialization_alias='imgUrl')
    """
    등록된 이미지 URL입니다. 브랜드메시지 이미지 업로드 API(`/api/comm/v1/file/brandmessage/...`)로 발급받은 `imgUrl`을 씁니다.
    """
    img_link: str | None = Field(default=None, validation_alias='imgLink', serialization_alias='imgLink', max_length=1000)
    """
    이미지 클릭 시 이동할 URL입니다. 생략하면 카카오 뷰어로 열립니다. 최대 1,000자입니다.
    """


class BrandMessageItemListEntry(ResponseModel):
    """
    브랜드메시지 와이드 아이템 목록의 항목 1개입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    title: str | None = Field(default=None, max_length=30)
    """
    아이템 제목입니다. 첫 번째 아이템은 최대 25자(줄바꿈 1회), 2~4번째 아이템은 최대 30자(줄바꿈 1회)입니다.
    """
    img_url: str | None = Field(default=None, validation_alias='imgUrl', serialization_alias='imgUrl')
    """
    아이템 이미지 URL입니다. 첫 번째 아이템은 와이드 리스트 첫번째 이미지 업로드, 2~4번째는 와이드 리스트 이미지 업로드로 발급받은 URL을 씁니다.
    """
    url_mobile: str | None = Field(default=None, validation_alias='urlMobile', serialization_alias='urlMobile', max_length=1000)
    """
    모바일 클릭 URL입니다. 최대 1,000자입니다.
    """
    url_pc: str | None = Field(default=None, validation_alias='urlPc', serialization_alias='urlPc', max_length=1000)
    """
    PC 클릭 URL입니다. 최대 1,000자입니다.
    """
    scheme_ios: str | None = Field(default=None, validation_alias='schemeIos', serialization_alias='schemeIos', max_length=1000)
    """
    iOS 커스텀 스킴입니다. 최대 1,000자입니다.
    """
    scheme_android: str | None = Field(default=None, validation_alias='schemeAndroid', serialization_alias='schemeAndroid', max_length=1000)
    """
    Android 커스텀 스킴입니다. 최대 1,000자입니다.
    """


class MarketingAgree(ResponseModel):
    """
    업로드된 증적자료 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    file_key: str | None = Field(default=None, validation_alias='fileKey', serialization_alias='fileKey', examples=['FILE_KEY_001'])
    """
    업로드된 파일의 식별 키입니다.
    """
    file_url: str | None = Field(default=None, validation_alias='fileUrl', serialization_alias='fileUrl')
    """
    업로드된 파일의 URL입니다.
    """


class BrandMessageMarketingAgreeResult(ResponseModel):
    """
    업로드 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    marketing_agree: MarketingAgree | None = Field(default=None, validation_alias='marketingAgree', serialization_alias='marketingAgree')
    """
    업로드된 증적자료 정보입니다.
    """


class BrandMessageTemplateSummary(ResponseModel):
    """
    템플릿 목록의 항목 1개입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str | None = Field(default=None, validation_alias='senderKey', serialization_alias='senderKey')
    """
    발신프로필 키입니다.
    """
    sender_key_type: str | None = Field(default=None, validation_alias='senderKeyType', serialization_alias='senderKeyType')
    """
    발신키 유형입니다. 문서 예시 값은 `S`(발신프로필)입니다. 기본값은 `S`입니다.
    """
    template_code: str | None = Field(default=None, validation_alias='templateCode', serialization_alias='templateCode')
    """
    템플릿 코드입니다.
    """
    status: str | None = Field(default=None, examples=['A'])
    """
    템플릿 상태입니다. 알려진 값: `A`(등록), `S`(차단). 최근 변경 템플릿 조회 응답에는 없습니다.
    """


class BrandMessageVideo(ResponseModel):
    """
    브랜드메시지 동영상 요소입니다(FP).
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    video_url: str = Field(..., validation_alias='videoUrl', serialization_alias='videoUrl', max_length=500)
    """
    카카오TV 동영상 URL입니다. 최대 500자입니다.
    """
    thumbnail_url: str | None = Field(default=None, validation_alias='thumbnailUrl', serialization_alias='thumbnailUrl', max_length=500)
    """
    동영상 썸네일 URL입니다. 비공개 동영상이면 필수입니다. 최대 500자입니다.
    """


class BrandMessageVideoInfo(ResponseModel):
    """
    브랜드메시지 동영상 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    vid: str | None = None
    """
    동영상 식별자입니다.
    """
    status: str | None = Field(default=None, examples=['PUBLIC'])
    """
    동영상 처리 상태입니다. 알려진 값: `REGISTERED`(업로드 등록됨), `ENCODING`(인코딩 중), `PUBLIC`(공개, 발송·템플릿 등록 가능), `PRIVATE`(비공개, 템플릿 등록만 가능), `VIOLATED`(정책 위반), `ILLEGAL`(불법촬영물), `DELETED`(삭제됨), `ERROR`(업로드·인코딩 오류).
    """
    title: str | None = None
    """
    동영상 제목입니다.
    """
    thumbnail_url: str | None = Field(default=None, validation_alias='thumbnailUrl', serialization_alias='thumbnailUrl')
    """
    동영상 썸네일 URL입니다.
    """
    video_url: str | None = Field(default=None, validation_alias='videoUrl', serialization_alias='videoUrl')
    """
    동영상 재생 URL입니다.
    """


class Brandmessage4(ResponseModel):
    """
    브랜드메시지 응답 영역입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    video: BrandMessageVideoInfo | None = None
    """
    동영상 정보입니다.
    """


class BrandMessageVideoInfoResult(ResponseModel):
    """
    동영상 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brandmessage: Brandmessage4 | None = None
    """
    브랜드메시지 응답 영역입니다.
    """


class BrandMessageVideoListEntry(ResponseModel):
    """
    동영상 업로드 이력 1건입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    vid: str | None = None
    """
    동영상 식별자입니다.
    """
    sender_key: str | None = Field(default=None, validation_alias='senderKey', serialization_alias='senderKey')
    """
    발신프로필 키입니다.
    """
    file_name: str | None = Field(default=None, validation_alias='fileName', serialization_alias='fileName')
    """
    업로드한 파일 이름입니다.
    """
    file_size: int | None = Field(default=None, validation_alias='fileSize', serialization_alias='fileSize')
    """
    업로드한 파일 크기(byte)입니다.
    """
    status: str | None = None
    """
    동영상 처리 상태입니다. 알려진 값: `REGISTERED`(업로드 등록됨), `ENCODING`(인코딩 중), `PUBLIC`(공개, 발송·템플릿 등록 가능), `PRIVATE`(비공개, 템플릿 등록만 가능), `VIOLATED`(정책 위반), `ILLEGAL`(불법촬영물), `DELETED`(삭제됨), `ERROR`(업로드·인코딩 오류).
    """
    title: str | None = None
    """
    동영상 제목입니다.
    """
    thumbnail_url: str | None = Field(default=None, validation_alias='thumbnailUrl', serialization_alias='thumbnailUrl')
    """
    동영상 썸네일 URL입니다. 처리 실패 시 빈 값입니다.
    """
    video_url: str | None = Field(default=None, validation_alias='videoUrl', serialization_alias='videoUrl')
    """
    동영상 재생 URL입니다. 처리 실패 시 빈 값입니다.
    """
    modified_at: str | None = Field(
        default=None, validation_alias='modifiedAt', serialization_alias='modifiedAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    카카오 기준 최종 변경 일시(`yyyy-MM-dd HH:mm:ss`)입니다. 처리 실패 시 반환되지 않습니다.
    """
    reg_date: str | None = Field(
        default=None, validation_alias='regDate', serialization_alias='regDate', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    업로드 등록 일시(`yyyy-MM-dd HH:mm:ss`)입니다.
    """
    update_date: str | None = Field(
        default=None, validation_alias='updateDate', serialization_alias='updateDate', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    최종 갱신 일시(`yyyy-MM-dd HH:mm:ss`)입니다.
    """


class BrandMessageVideoListResult(ResponseModel):
    """
    동영상 목록 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    offset: int | None = None
    """
    조회 시작 위치입니다.
    """
    limit: int | None = None
    """
    조회 건수입니다.
    """
    total_count: int | None = Field(default=None, validation_alias='totalCount', serialization_alias='totalCount')
    """
    전체 동영상 건수입니다.
    """
    videos: list[BrandMessageVideoListEntry] | None = None
    """
    동영상 이력 배열입니다.
    """


class BrandMessageVideoUploadChannel(ResponseModel):
    """
    발급된 카카오 업로드 채널 정보입니다. `uploadUrl`과 `token`은 발급 후 5분간만 유효합니다. 파일은 `POST {uploadUrl}`에 `x-kamp-upload-token: {token}` 헤더와 multipart `file` 필드로 직접 전송합니다(비즈고 API를 거치지 않음).
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    vid: str | None = Field(default=None, examples=['VID_EXAMPLE'])
    """
    동영상 식별자입니다. 이후 조회 API에서 사용합니다.
    """
    upload_url: str | None = Field(
        default=None,
        validation_alias='uploadUrl', serialization_alias='uploadUrl',
        examples=['https://example.kakao.upload/v4/upload/VID_EXAMPLE/open'],
    )
    """
    동영상 파일을 전송할 카카오 업로드 URL입니다.
    """
    token: str | None = Field(default=None, examples=['UPLOAD_TOKEN_EXAMPLE'])
    """
    업로드 요청 시 `x-kamp-upload-token` 헤더로 보낼 인증 토큰(JWT)입니다.
    """


class Brandmessage5(ResponseModel):
    """
    브랜드메시지 응답 영역입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    video: BrandMessageVideoUploadChannel | None = None
    """
    발급된 업로드 채널 정보입니다.
    """


class BrandMessageVideoUploadRegisterResult(ResponseModel):
    """
    업로드 등록 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brandmessage: Brandmessage5 | None = None
    """
    브랜드메시지 응답 영역입니다.
    """


class CommonResult(ResponseModel):
    """
    API Gateway 공통 결과(인증·권한·요청 형식 검증)입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    auth_code: str | None = Field(default=None, validation_alias='authCode', serialization_alias='authCode', examples=['A000'])
    """
    인증 결과 코드입니다. `A000`이면 성공입니다.
    """
    auth_result: str | None = Field(default=None, validation_alias='authResult', serialization_alias='authResult', examples=['Success'])
    """
    인증 결과 메시지입니다.
    """
    infobank_tr_id: str | None = Field(
        default=None, validation_alias='infobankTrId', serialization_alias='infobankTrId', examples=['Infobank-Tracking-Id']
    )
    """
    인포뱅크 트랜잭션 추적 ID입니다. 문의 시 이 값을 전달합니다.
    """


class CounselCert(ResponseModel):
    """
    카카오톡 인증(전자서명) 진행 상태입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    tx_id: str | None = Field(default=None, validation_alias='txId', serialization_alias='txId')
    """
    인증 트랜잭션 ID입니다.
    """
    session_id: int | None = Field(default=None, validation_alias='sessionId', serialization_alias='sessionId')
    """
    세션 아이디입니다.
    """
    sign_status: str | None = Field(default=None, validation_alias='signStatus', serialization_alias='signStatus')
    """
    서명 상태입니다. 문서 예시 값은 `COMPLETED`입니다.
    """
    created_at: str | None = Field(
        default=None, validation_alias='createdAt', serialization_alias='createdAt', json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss"}
    )
    """
    서명 요청 시각입니다.
    """
    viewed_at: str | None = Field(
        default=None, validation_alias='viewedAt', serialization_alias='viewedAt', json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss"}
    )
    """
    사용자가 서명 내용을 확인한 시각입니다.
    """
    completed_at: str | None = Field(
        default=None,
        validation_alias='completedAt', serialization_alias='completedAt',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss"},
    )
    """
    서명 완료 시각입니다.
    """
    expired_at: str | None = Field(
        default=None, validation_alias='expiredAt', serialization_alias='expiredAt', json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss"}
    )
    """
    서명 만료 시각입니다.
    """


class CounselCertStatusResult(ResponseModel):
    """
    카카오톡 인증 상태 조회 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    cert: CounselCert | None = None


class CounselEndResult(ResponseModel):
    """
    상담 종료 처리 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_key: str | None = Field(default=None, validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다. 발송 결과 웹훅(`cstalk/result`, requestType `end`/`endwithbot`)의 `msgKey`와 대조합니다.
    """


class CounselFileUploadResult(ResponseModel):
    """
    상담톡 파일 업로드 결과입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    file_url: str | None = Field(
        default=None, validation_alias='fileUrl', serialization_alias='fileUrl', examples=['https://example.kakao.file/cstalk_file.pdf']
    )
    """
    업로드된 파일 URL입니다. 발송 요청의 `attachment.file.fileUrl`에 넣습니다.
    """
    file_name: str | None = Field(default=None, validation_alias='fileName', serialization_alias='fileName')
    """
    업로드된 파일 이름입니다.
    """
    size: str | None = None
    """
    업로드된 파일 용량입니다. 문서 예시는 byte 단위 문자열(`102400`)입니다.
    """


class CounselImageUploadResult(ResponseModel):
    """
    상담톡 이미지 업로드 결과입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    img_url: str | None = Field(
        default=None, validation_alias='imgUrl', serialization_alias='imgUrl', examples=['https://example.kakao.image/cstalk_image.jpg']
    )
    """
    업로드된 이미지 URL입니다. 발송 요청의 `attachment.image.imgUrl`에 넣습니다.
    """


class CounselLastReference(ResponseModel):
    """
    현재 메타 정보가 없을 때 전달되는 가장 마지막 메타 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    extra: str | None = None
    """
    이전 상담 연결 버튼으로 전달된 메타 정보입니다.
    """
    bot: str | None = None
    """
    상담을 어떻게 시작했는지 나타내는 값입니다. 문서 예시 값은 문자열 `false`입니다.
    """
    bot_event: str | None = None
    """
    봇으로 상담을 시작했을 때 전달되는 봇 블록 이벤트 값입니다.
    """
    created_at: str | None = Field(
        default=None, json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"}
    )
    """
    마지막 메타 정보 생성 시각입니다.
    """


class CounselMessageAttachment(ResponseModel):
    """
    사용자 메시지가 4,000자를 넘으면 전체 메시지를 txt 파일 URL로 추가 전달하는 영역입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    url: str | None = None
    """
    전체 메시지를 확인할 수 있는 txt 파일 URL입니다.
    """


class CounselMessageContent(ResponseModel):
    """
    사용자가 전송한 메시지 데이터 1건입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    url: str | None = None
    """
    이미지, 파일 등 데이터 경로입니다.
    """
    comment: str | None = None
    """
    사용자가 입력한 문구입니다.
    """


class CounselPersonalInfo(ResponseModel):
    """
    사용자가 수집에 동의한 개인정보입니다. 저장·로그 출력에 주의하고 목적 외로 쓰지 않습니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    phone_number: str | None = Field(default=None, examples=['01000000000'])
    """
    카카오 계정 전화번호입니다.
    """
    nickname: str | None = None
    """
    카카오 프로필 닉네임입니다.
    """


class CounselReference(ResponseModel):
    """
    고객사에서 설정한 현재 메타 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    extra: str | None = None
    """
    상담 연결 버튼(`https://bizmessage.kakao.com/chat/open`)의 `extra`로 전달된 메타 정보입니다.
    """


class CounselSession(ResponseModel):
    """
    상담 세션 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    session_id: int | None = Field(default=None, validation_alias='sessionId', serialization_alias='sessionId')
    """
    세션 아이디입니다.
    """
    sender_key: str | None = Field(default=None, validation_alias='senderKey', serialization_alias='senderKey')
    """
    발신프로필 키입니다.
    """
    started_type: str | None = Field(default=None, validation_alias='startedType', serialization_alias='startedType')
    """
    세션 시작 타입입니다. 문서 예시 값은 `UM`입니다.
    """
    started_at: str | None = Field(
        default=None,
        validation_alias='startedAt', serialization_alias='startedAt',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSS"},
    )
    """
    세션 시작 시각입니다. 문서 예시는 오프셋 없는 ISO 8601 형식(`2025-09-24T11:22:08.557`)입니다.
    """
    expired_type: str | None = Field(default=None, validation_alias='expiredType', serialization_alias='expiredType')
    """
    세션 종료 타입입니다. 문서 예시 값은 `AE`입니다.
    """
    expired_at: str | None = Field(
        default=None, validation_alias='expiredAt', serialization_alias='expiredAt', json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss"}
    )
    """
    세션 종료 시각입니다. 현재 시각보다 크면 종료 예정 시각입니다(마지막 메시지 수신 시각 기준 다음 정각으로부터 30일 후).
    """


class CounselSessionResult(ResponseModel):
    """
    세션 조회 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    session: CounselSession | None = None


class CounselSystemMessageButton(ResponseModel):
    """
    시스템 메시지 하단 버튼입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    ordering: int
    """
    버튼 노출 순서입니다.
    """
    type: str
    """
    시스템 메시지 버튼 링크 타입입니다. 문서 예시 값은 `WL`입니다.
    """
    name: str
    """
    버튼 이름입니다.
    """
    url_mobile: str | None = Field(default=None, validation_alias='urlMobile', serialization_alias='urlMobile')
    """
    모바일 웹링크 주소입니다.
    """
    url_pc: str | None = Field(default=None, validation_alias='urlPc', serialization_alias='urlPc')
    """
    PC 웹링크 주소입니다.
    """
    scheme_ios: str | None = Field(default=None, validation_alias='schemeIos', serialization_alias='schemeIos')
    """
    iOS 앱링크 주소입니다.
    """
    scheme_android: str | None = Field(default=None, validation_alias='schemeAndroid', serialization_alias='schemeAndroid')
    """
    Android 앱링크 주소입니다.
    """


class CounselSystemMessageComment(ResponseModel):
    """
    시스템 메시지 검수 결과 또는 문의입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: str | None = None
    """
    댓글 아이디입니다.
    """
    content: str | None = None
    """
    댓글 내용입니다.
    """
    user_name: str | None = Field(default=None, validation_alias='userName', serialization_alias='userName')
    """
    작성자입니다.
    """
    created_at: str | None = Field(
        default=None, validation_alias='createdAt', serialization_alias='createdAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    등록일입니다.
    """
    status: Literal['APR', 'REJ', 'INQ'] | None = None
    """
    상태입니다. `APR` 승인, `REJ` 반려, `INQ` 문의입니다.
    """


class CounselSystemMessageContent(ResponseModel):
    """
    시스템 메시지 1건의 내용입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    message_type: str = Field(..., validation_alias='messageType', serialization_alias='messageType')
    """
    시스템 메시지 타입입니다. 문서 예시 값은 `ST`입니다.
    """
    content: str
    """
    메시지 내용입니다.
    """
    buttons: list[CounselSystemMessageButton]
    """
    메시지 하단 버튼 목록입니다. 등록 요청에서는 필수로 표시되어 있습니다.
    """


class CounselSystemMessageRef(ResponseModel):
    """
    생성된 시스템 메시지 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: str | None = None
    """
    생성된 시스템 메시지 ID입니다.
    """


class CounselWebhookAck(ResponseModel):
    """
    상담톡 웹훅 수신 응답입니다. 리포트·MO 웹훅(`{"msgKey": ...}`)과 달리 `code`/`result`를 돌려줍니다.
    HTTP 200과 이 규격의 응답을 받아야 정상 처리되며, 응답이 없거나 규격이 다르면 최대 3회 재시도합니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    code: str | None = Field(default=None, examples=['A000'])
    """
    웹훅 처리 결과 코드입니다. 문서 예시 값은 `A000`입니다.
    """
    result: str | None = Field(default=None, examples=['Success'])
    """
    웹훅 처리 결과 메시지입니다. 문서 예시 값은 `Success`입니다.
    """


class CounselWebhookCommon(ResponseModel):
    """
    상담톡 웹훅 7종의 공통 필드입니다. 값이 없는 필드는 본문에서 빠지므로 이벤트마다 전달되는 키 집합이 다릅니다.
    시각 필드는 `yyyy-MM-dd'T'HH:mm:ss.SSS+09:00`(KST) 형식이며 원본 값이 없으면 빈 문자열입니다.
    상담톡 웹훅 본문은 최종 사용자의 상담 내용·식별자이므로 개인정보로 취급하고 로그·APM·에러 리포트에 남기지 않습니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_key: str | None = Field(default=None, validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다. 발송 결과(`result`)에서는 발송 API 응답의 msgKey와 같고, 수신 6종에서는 이벤트마다 새로 발급된 값이라 발송 건과 대응하지 않습니다.
    재시도로 같은 이벤트가 다시 올 수 있으므로 msgKey 기준으로 멱등 처리합니다.

    """
    user_key: str | None = Field(default=None, validation_alias='userKey', serialization_alias='userKey')
    """
    상담톡 사용자 키입니다. 카카오톡 채널별로 다르며 대소문자를 구분하고, 사용자가 탈퇴 후 재가입하면 바뀝니다.
    """
    sender_key: str | None = Field(default=None, validation_alias='senderKey', serialization_alias='senderKey')
    """
    메시지를 수신한 발신프로필 키입니다.
    """
    service_type: str | None = Field(default=None, validation_alias='serviceType', serialization_alias='serviceType')
    """
    서비스 타입입니다. 문서 예시 값은 `CSTALK`입니다.
    """
    msg_type: str | None = Field(default=None, validation_alias='msgType', serialization_alias='msgType')
    """
    메시지 타입입니다.
    """
    request_type: str | None = Field(default=None, validation_alias='requestType', serialization_alias='requestType')
    """
    요청(이벤트) 타입입니다.
    """
    send_time: str | None = Field(
        default=None,
        validation_alias='sendTime', serialization_alias='sendTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 이벤트를 수신한 시각입니다.
    """
    report_time: str | None = Field(
        default=None,
        validation_alias='reportTime', serialization_alias='reportTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 웹훅을 전송한 시각입니다.
    """
    kakao_time: str | None = Field(
        default=None,
        validation_alias='kakaoTime', serialization_alias='kakaoTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    카카오(상담톡 서버)가 전달한 시각입니다. 사용자가 메시지를 입력한 시각이 아닙니다.
    """


class CounselWeekTime(ResponseModel):
    """
    요일별 상담 시간입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    day: Literal['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    """
    요일입니다.
    """
    start_at: str = Field(..., validation_alias='startAt', serialization_alias='startAt', json_schema_extra={'x-format': 'HHmm'})
    """
    상담 시작 시간입니다. 문서 예시는 `0900`입니다.
    """
    end_at: str = Field(..., validation_alias='endAt', serialization_alias='endAt', json_schema_extra={'x-format': 'HHmm'})
    """
    상담 종료 시간입니다. 문서 예시는 `1800`입니다.
    """


class FileUploadResult(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    file_key: str | None = Field(default=None, validation_alias='fileKey', serialization_alias='fileKey', examples=['FILE_KEY_001'])
    """
    업로드 후 발급된 파일 키입니다. 메시지 본문의 `fileKey`에 씁니다.
    """
    expired: str | None = Field(default=None, examples=['2027-04-24T10:45:24+09:00'])
    """
    파일 키 만료 일시(ISO 8601)입니다.
    """


class InsightKakaoStatistics(ResponseModel):
    """
    카카오(알림톡·브랜드메시지) 발송·읽음·클릭 통계 1건입니다. 카카오가 직접 제공하는 채널 기반 통계입니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    success_count: int | None = Field(default=None, validation_alias='successCount', serialization_alias='successCount')
    """
    발송 성공 건수입니다.
    """
    fail_count: int | None = Field(default=None, validation_alias='failCount', serialization_alias='failCount')
    """
    발송 실패 건수입니다.
    """
    read_count: int | None = Field(default=None, validation_alias='readCount', serialization_alias='readCount')
    """
    읽음 건수입니다.
    """
    button_click_count: int | None = Field(default=None, validation_alias='buttonClickCount', serialization_alias='buttonClickCount')
    """
    버튼 클릭 건수입니다.
    """
    list_click_count: int | None = Field(default=None, validation_alias='listClickCount', serialization_alias='listClickCount')
    """
    목록 클릭 건수입니다.
    """
    thumbnail_click_count: int | None = Field(default=None, validation_alias='thumbnailClickCount', serialization_alias='thumbnailClickCount')
    """
    썸네일 클릭 건수입니다.
    """
    etc_click_count: int | None = Field(default=None, validation_alias='etcClickCount', serialization_alias='etcClickCount')
    """
    기타 클릭 건수입니다.
    """
    send_rate: float | None = Field(default=None, validation_alias='sendRate', serialization_alias='sendRate')
    """
    발송 성공률입니다.
    """
    read_rate: float | None = Field(default=None, validation_alias='readRate', serialization_alias='readRate')
    """
    읽음률입니다.
    """
    click_rate: float | None = Field(default=None, validation_alias='clickRate', serialization_alias='clickRate')
    """
    클릭률입니다.
    """
    ctr: float | None = None
    """
    CTR(클릭률/읽음률)입니다.
    """


class InsightKakaoStatisticsResult(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    statistics: list[InsightKakaoStatistics] | None = None
    """
    발송 통계 목록입니다.
    """


class InsightKakaoTemplateStatistics(InsightKakaoStatistics):
    """
    카카오(알림톡·브랜드메시지) 템플릿별 통계 1건입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    template_code: str | None = Field(
        default=None, validation_alias='templateCode', serialization_alias='templateCode', examples=['TEMPLATE_CODE_EXAMPLE']
    )
    """
    템플릿 코드입니다.
    """
    template_name: str | None = Field(default=None, validation_alias='templateName', serialization_alias='templateName')
    """
    템플릿 이름입니다.
    """


class InsightKakaoTemplateStatisticsResult(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    statistics: list[InsightKakaoTemplateStatistics] | None = None
    """
    템플릿별 통계 목록입니다.
    """


class InsightRcsBrandProfileStat(ResponseModel):
    """
    브랜드 프로필 노출 일자별 통계 1건입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    stat_date: str | None = Field(
        default=None,
        validation_alias='statDate', serialization_alias='statDate',
        examples=['20260801'],
        json_schema_extra={'x-format': 'yyyyMMdd'},
    )
    """
    통계 일자(yyyyMMdd)입니다.
    """
    chatbot_id: str | None = Field(default=None, validation_alias='chatbotId', serialization_alias='chatbotId')
    """
    챗봇 ID입니다.
    """
    displayed_count: int | None = Field(default=None, validation_alias='displayedCount', serialization_alias='displayedCount')
    """
    노출 건수입니다.
    """


class InsightRcsBrandProfileStatResult(ResponseModel):
    """
    RCS 응답 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    stat: list[InsightRcsBrandProfileStat] | None = None
    """
    일자별 노출 통계 목록입니다.
    """


class InsightRcsButtonClick(ResponseModel):
    """
    RCS 메시지 버튼 1개의 클릭 통계입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    button_num: int | None = Field(default=None, validation_alias='buttonNum', serialization_alias='buttonNum')
    """
    버튼 번호입니다.
    """
    action_type: str | None = Field(default=None, validation_alias='actionType', serialization_alias='actionType')
    """
    버튼 액션 유형입니다. 알려진 값은 `urlAction`입니다(발송 규격의 action 키 이름으로 보입니다).
    """
    title: str | None = None
    """
    버튼 제목입니다.
    """
    click_count: int | None = Field(default=None, validation_alias='clickCount', serialization_alias='clickCount')
    """
    클릭 수입니다.
    """


class InsightRcsMenuClick(ResponseModel):
    """
    대화방 메뉴 1개의 클릭 통계입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    postback_id: str | None = Field(default=None, validation_alias='postbackId', serialization_alias='postbackId')
    """
    포스트백 ID입니다.
    """
    menu_type: str | None = Field(default=None, validation_alias='menuType', serialization_alias='menuType')
    """
    메뉴 유형입니다. 알려진 값은 `text`입니다.
    """
    action_type: str | None = Field(default=None, validation_alias='actionType', serialization_alias='actionType')
    """
    메뉴 액션 유형입니다. 알려진 값은 `postbackAction`입니다.
    """
    title: str | None = None
    """
    메뉴 제목입니다.
    """
    click_count: int | None = Field(default=None, validation_alias='clickCount', serialization_alias='clickCount')
    """
    클릭 수입니다.
    """
    sub_list: list[InsightRcsMenuClick] | None = Field(default=None, validation_alias='subList', serialization_alias='subList')
    """
    하위 메뉴 목록입니다. 상위 메뉴와 같은 항목으로 구성됩니다.
    """


class InsightRcsMessageButtonStat(ResponseModel):
    """
    RCS 메시지 버튼 클릭 일자별 통계 1건(카드 단위)입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    stat_date: str | None = Field(
        default=None,
        validation_alias='statDate', serialization_alias='statDate',
        examples=['20260801'],
        json_schema_extra={'x-format': 'yyyyMMdd'},
    )
    """
    통계 일자(yyyyMMdd)입니다.
    """
    corp_id: str | None = Field(default=None, validation_alias='corpId', serialization_alias='corpId')
    """
    기업 ID입니다.
    """
    corp_reg_num: str | None = Field(default=None, validation_alias='corpRegNum', serialization_alias='corpRegNum')
    """
    사업자등록번호입니다.
    """
    brand_id: str | None = Field(default=None, validation_alias='brandId', serialization_alias='brandId', examples=['BRAND_ID_EXAMPLE'])
    """
    RCS 브랜드 ID입니다.
    """
    chatbot_id: str | None = Field(default=None, validation_alias='chatbotId', serialization_alias='chatbotId')
    """
    챗봇 ID입니다.
    """
    group_id: str | None = Field(default=None, validation_alias='groupId', serialization_alias='groupId')
    """
    그룹 ID입니다.
    """
    messagebase_id: str | None = Field(default=None, validation_alias='messagebaseId', serialization_alias='messagebaseId')
    """
    메시지베이스 ID입니다.
    """
    reaction_type: str | None = Field(default=None, validation_alias='reactionType', serialization_alias='reactionType')
    """
    반응 유형입니다. 알려진 값은 `button`입니다.
    """
    card_num: int | None = Field(default=None, validation_alias='cardNum', serialization_alias='cardNum')
    """
    카드 번호입니다.
    """
    button_list: list[InsightRcsButtonClick] | None = Field(default=None, validation_alias='buttonList', serialization_alias='buttonList')
    """
    버튼별 클릭 상세입니다.
    """


class InsightRcsMessageButtonStatResult(ResponseModel):
    """
    RCS 응답 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    stat: list[InsightRcsMessageButtonStat] | None = None
    """
    일자별 버튼 클릭 통계 목록입니다.
    """


class InsightRcsMessageStat(ResponseModel):
    """
    RCS 메시지 발송·노출 일자별 통계 1건입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    stat_date: str | None = Field(
        default=None,
        validation_alias='statDate', serialization_alias='statDate',
        examples=['20260801'],
        json_schema_extra={'x-format': 'yyyyMMdd'},
    )
    """
    통계 일자(yyyyMMdd)입니다.
    """
    corp_id: str | None = Field(default=None, validation_alias='corpId', serialization_alias='corpId')
    """
    기업 ID입니다.
    """
    corp_reg_num: str | None = Field(default=None, validation_alias='corpRegNum', serialization_alias='corpRegNum')
    """
    사업자등록번호입니다.
    """
    brand_id: str | None = Field(default=None, validation_alias='brandId', serialization_alias='brandId', examples=['BRAND_ID_EXAMPLE'])
    """
    RCS 브랜드 ID입니다.
    """
    chatbot_id: str | None = Field(default=None, validation_alias='chatbotId', serialization_alias='chatbotId')
    """
    챗봇 ID입니다.
    """
    group_id: str | None = Field(default=None, validation_alias='groupId', serialization_alias='groupId')
    """
    그룹 ID입니다. 발송 요청의 `messageFlow[].rcs.groupId` 값입니다.
    """
    messagebase_id: str | None = Field(default=None, validation_alias='messagebaseId', serialization_alias='messagebaseId')
    """
    메시지베이스 ID입니다.
    """
    delivered_count: int | None = Field(default=None, validation_alias='deliveredCount', serialization_alias='deliveredCount')
    """
    발송 건수입니다.
    """
    displayed_count: int | None = Field(default=None, validation_alias='displayedCount', serialization_alias='displayedCount')
    """
    노출(읽음) 건수입니다.
    """


class InsightRcsMessageStatResult(ResponseModel):
    """
    RCS 응답 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    stat: list[InsightRcsMessageStat] | None = None
    """
    일자별 통계 목록입니다.
    """


class InsightRcsPersistentMenuStat(ResponseModel):
    """
    대화방 메뉴 클릭 일자별 통계 1건입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    stat_date: str | None = Field(
        default=None,
        validation_alias='statDate', serialization_alias='statDate',
        examples=['20260801'],
        json_schema_extra={'x-format': 'yyyyMMdd'},
    )
    """
    통계 일자(yyyyMMdd)입니다.
    """
    corp_id: str | None = Field(default=None, validation_alias='corpId', serialization_alias='corpId')
    """
    기업 ID입니다.
    """
    corp_reg_num: str | None = Field(default=None, validation_alias='corpRegNum', serialization_alias='corpRegNum')
    """
    사업자등록번호입니다.
    """
    brand_id: str | None = Field(default=None, validation_alias='brandId', serialization_alias='brandId', examples=['BRAND_ID_EXAMPLE'])
    """
    RCS 브랜드 ID입니다.
    """
    chatbot_id: str | None = Field(default=None, validation_alias='chatbotId', serialization_alias='chatbotId')
    """
    챗봇 ID입니다.
    """
    menu_list: list[InsightRcsMenuClick] | None = Field(default=None, validation_alias='menuList', serialization_alias='menuList')
    """
    메뉴별 클릭 상세입니다.
    """


class InsightRcsPersistentMenuStatResult(ResponseModel):
    """
    RCS 응답 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    stat: list[InsightRcsPersistentMenuStat] | None = None
    """
    일자별 메뉴 클릭 통계 목록입니다.
    """


class KakaoCategory(ResponseModel):
    """
    발신프로필 카테고리입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    code: str | None = None
    """
    카테고리 코드입니다.
    """
    name: str | None = None
    """
    카테고리 이름입니다.
    """


class Kakao(ResponseModel):
    """
    카카오 비즈메시지 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    categories: list[KakaoCategory] | None = None
    """
    카테고리 목록입니다.
    """


class KakaoCategoryListResult(ResponseModel):
    """
    발신프로필 카테고리 전체조회 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    kakao: Kakao | None = None
    """
    카카오 비즈메시지 응답 데이터입니다.
    """


class Kakao1(ResponseModel):
    """
    카카오 비즈메시지 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    category: KakaoCategory | None = None


class KakaoCategoryResult(ResponseModel):
    """
    발신프로필 카테고리 상세조회 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    kakao: Kakao1 | None = None
    """
    카카오 비즈메시지 응답 데이터입니다.
    """


class KakaoGroup(ResponseModel):
    """
    발신프로필 그룹입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    group_key: str | None = Field(
        default=None, validation_alias='groupKey', serialization_alias='groupKey', examples=['GROUP_KEY_EXAMPLE']
    )
    """
    그룹 키입니다.
    """
    group_name: str | None = Field(default=None, validation_alias='groupName', serialization_alias='groupName')
    """
    그룹 이름입니다.
    """


class Kakao2(ResponseModel):
    """
    카카오 비즈메시지 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    groups: list[KakaoGroup] | None = None
    """
    발신프로필 그룹 목록입니다.
    """


class KakaoGroupListResult(ResponseModel):
    """
    발신프로필 그룹 조회 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    kakao: Kakao2 | None = None
    """
    카카오 비즈메시지 응답 데이터입니다.
    """


class KakaoSanction(ResponseModel):
    """
    발신프로필·템플릿 제재 정보입니다. 제재가 적용되면 발송이 불가하거나 일부 기능이 제한될 수 있습니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    restricted_at: str | None = Field(
        default=None,
        validation_alias='restrictedAt', serialization_alias='restrictedAt',
        json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'},
    )
    """
    제재 적용 시각(yyyy-MM-dd HH:mm:ss)입니다.
    """
    sender_key: str | None = Field(
        default=None, validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE']
    )
    """
    발신프로필 키입니다.
    """
    template_code: str | None = Field(
        default=None, validation_alias='templateCode', serialization_alias='templateCode', examples=['TEMPLATE_CODE_EXAMPLE']
    )
    """
    템플릿 코드입니다.
    """
    group_key: str | None = Field(
        default=None, validation_alias='groupKey', serialization_alias='groupKey', examples=['GROUP_KEY_EXAMPLE']
    )
    """
    발신프로필 그룹 키입니다.
    """
    sender_key_type: Literal['G', 'S'] | None = Field(default=None, validation_alias='senderKeyType', serialization_alias='senderKeyType')
    """
    발신프로필 키 타입입니다.
    - `G`: 그룹
    - `S`: 발신프로필

    """
    reason_type: str | None = Field(default=None, validation_alias='reasonType', serialization_alias='reasonType')
    """
    제재 사유입니다. 알려진 값:
    - `BZM`: 비즈메시지 운영정책 위반(스팸/어뷰징)
    - `CHANNEL`: 채널 운영정책 위반

    """


class Kakao3(ResponseModel):
    """
    카카오 비즈메시지 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    abusing: KakaoSanction | None = None


class KakaoSanctionResult(ResponseModel):
    """
    제재 조회 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    kakao: Kakao3 | None = None
    """
    카카오 비즈메시지 응답 데이터입니다.
    """


class KakaoSenderChannel(ResponseModel):
    """
    발신프로필 목록 조회(`GET /account/kakao/sender/profiles`)의 항목 1개입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str | None = Field(
        default=None, validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE']
    )
    """
    발신프로필 키입니다.
    """
    sender_key_type: str | None = Field(default=None, validation_alias='senderKeyType', serialization_alias='senderKeyType')
    """
    발신키 유형입니다. 문서 예시 값은 `S`입니다.
    """
    channel_name: str | None = Field(default=None, validation_alias='channelName', serialization_alias='channelName')
    """
    카카오톡 채널 이름입니다.
    """
    channel_id: str | None = Field(default=None, validation_alias='channelId', serialization_alias='channelId')
    """
    카카오톡 채널 검색용 아이디입니다.
    """
    channel_key: str | None = Field(default=None, validation_alias='channelKey', serialization_alias='channelKey')
    """
    카카오톡 채널 키입니다.
    """
    category_code: str | None = Field(default=None, validation_alias='categoryCode', serialization_alias='categoryCode')
    """
    발신프로필 카테고리 코드입니다.
    """
    status: str | None = None
    """
    발신프로필 상태입니다.
    """
    profile_status: str | None = Field(default=None, validation_alias='profileStatus', serialization_alias='profileStatus')
    """
    카카오톡 채널 프로필 상태입니다.
    """
    dormant: bool | None = None
    """
    휴면 상태 여부입니다.
    """
    block: bool | None = None
    """
    차단 상태 여부입니다.
    """
    business_profile: bool | None = Field(default=None, validation_alias='businessProfile', serialization_alias='businessProfile')
    """
    비즈니스 인증 채널 여부입니다.
    """
    business_type: str | None = Field(default=None, validation_alias='businessType', serialization_alias='businessType')
    """
    비즈니스 인증 유형입니다.
    """
    created_at: str | None = Field(
        default=None, validation_alias='createdAt', serialization_alias='createdAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    발신프로필 생성 일시(yyyy-MM-dd HH:mm:ss)입니다.
    """
    reg_date: str | None = Field(
        default=None, validation_alias='regDate', serialization_alias='regDate', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    등록 일시(yyyy-MM-dd HH:mm:ss)입니다.
    """
    update_date: str | None = Field(
        default=None, validation_alias='updateDate', serialization_alias='updateDate', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    수정 일시(yyyy-MM-dd HH:mm:ss)입니다.
    """


class KakaoSenderProfile(ResponseModel):
    """
    카카오 비즈메시지 발신프로필 정보입니다.
    발신프로필 등록(`POST /account/kakao/sender`), uuid·senderKey 조회(`GET /account/kakao/sender`),
    발신프로필 키로 조회(`GET /center/kakao/sender`) 응답에서 함께 씁니다. 엔드포인트마다 포함되는 필드가 조금씩 다릅니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str | None = Field(
        default=None, validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE']
    )
    """
    발신프로필 키입니다.
    """
    uuid: str | None = Field(default=None, examples=['@KAKAO_CHANNEL_ID_EXAMPLE'])
    """
    카카오톡 채널 아이디(uuid)입니다. `@`로 시작하는 카카오톡 채널 검색용 아이디입니다.
    """
    name: str | None = None
    """
    카카오톡 채널 프로필명입니다.
    """
    status: str | None = None
    """
    발신프로필 상태값입니다. 알려진 값은 `A`(정상)입니다.
    """
    block: bool | None = None
    """
    발신프로필 차단 여부입니다.
    """
    dormant: bool | None = None
    """
    발신프로필 휴면 여부입니다. 휴면이면 휴면 해제(`POST /center/kakao/sender/recover`)로 복구합니다.
    """
    profile_status: Literal['A', 'C', 'B', 'E'] | None = Field(
        default=None, validation_alias='profileStatus', serialization_alias='profileStatus'
    )
    """
    카카오톡 채널 상태입니다.
    - `A`: activated
    - `C`: deactivated
    - `B`: block
    - `E`: deleting

    """
    created_at: str | None = Field(
        default=None, validation_alias='createdAt', serialization_alias='createdAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    등록일입니다.
    """
    modified_at: str | None = Field(
        default=None, validation_alias='modifiedAt', serialization_alias='modifiedAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    최종 수정일입니다. 형식은 `createdAt`과 같습니다.
    """
    category_code: str | None = Field(default=None, validation_alias='categoryCode', serialization_alias='categoryCode')
    """
    발신프로필 카테고리 코드(11자리 숫자)입니다.
    """
    bizchat: bool | None = None
    """
    상담톡 사용 여부입니다. 조회 응답에만 있고 등록 응답에는 없습니다.
    """
    brandtalk: bool | None = None
    """
    브랜드톡 사용 여부입니다. account 경로 응답에만 있습니다.
    """
    brand_message: bool | None = Field(default=None, validation_alias='brandMessage', serialization_alias='brandMessage')
    """
    브랜드메시지 타겟팅 사용 여부입니다.
    """
    committal_company_name: str | None = Field(default=None, validation_alias='committalCompanyName', serialization_alias='committalCompanyName')
    """
    상담톡 위탁사 이름입니다. 조회 응답에만 있습니다.
    """
    channel_key: str | None = Field(default=None, validation_alias='channelKey', serialization_alias='channelKey')
    """
    메시지 발송 결과 수신 채널키입니다.
    """
    business_profile: bool | None = Field(default=None, validation_alias='businessProfile', serialization_alias='businessProfile')
    """
    카카오톡 채널 비즈니스 인증 여부입니다.
    """
    business_type: str | None = Field(default=None, validation_alias='businessType', serialization_alias='businessType')
    """
    비즈니스 유형입니다. 알려진 값은 `BUSINESS`입니다. account 경로 응답에만 있습니다.
    """
    unsubscribe_phone_number: str | None = Field(default=None, validation_alias='unsubscribePhoneNumber', serialization_alias='unsubscribePhoneNumber')
    """
    무료수신거부 전화번호입니다.
    """
    unsubscribe_auth_number: str | None = Field(default=None, validation_alias='unsubscribeAuthNumber', serialization_alias='unsubscribeAuthNumber')
    """
    무료수신거부 인증번호입니다.
    """
    profile_spam_level: str | None = Field(default=None, validation_alias='profileSpamLevel', serialization_alias='profileSpamLevel')
    """
    카카오톡 채널 스팸 상태입니다. 정상 / 경고제한(프로필 초기화, 상담·발송 가능) / 영구제한(상담·발송 불가)입니다.
    문서 예시 값은 `정상`입니다.

    """
    profile_message_spam_level: str | None = Field(
        default=None, validation_alias='profileMessageSpamLevel', serialization_alias='profileMessageSpamLevel'
    )
    """
    카카오톡 메시지 스팸 상태입니다. 정상 / 경고제한(상담·발송 가능) / 활동제한(상담 가능, 발송 불가)입니다.
    문서 예시 값은 `정상`입니다.

    """
    clear_block_url: str | None = Field(default=None, validation_alias='clearBlockUrl', serialization_alias='clearBlockUrl')
    """
    알림톡 차단 해제 링크입니다.
    """


class KakaoSenderProfileResult(ResponseModel):
    """
    발신프로필 정보를 담는 카카오 응답 영역입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_profile: KakaoSenderProfile | None = Field(default=None, validation_alias='senderProfile', serialization_alias='senderProfile')


class KakaoSenderResult(ResponseModel):
    """
    발신프로필 키로 조회(`GET /center/kakao/sender`) 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    kakao: KakaoSenderProfileResult | None = None


class MessageStatistics(ResponseModel):
    """
    일자별 접수·리포트 통계입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    stat_date: str | None = Field(
        default=None,
        validation_alias='statDate', serialization_alias='statDate',
        json_schema_extra={'x-format': 'YYYYMMDD'},
        pattern='^[0-9]{8}$',
    )
    """
    집계일입니다.
    """
    recv_total_cnt: int | None = Field(default=None, validation_alias='recvTotalCnt', serialization_alias='recvTotalCnt')
    """
    접수 전체 건수입니다.
    """
    recv_succ_cnt: int | None = Field(default=None, validation_alias='recvSuccCnt', serialization_alias='recvSuccCnt')
    """
    접수 성공 건수입니다.
    """
    recv_fail_cnt: int | None = Field(default=None, validation_alias='recvFailCnt', serialization_alias='recvFailCnt')
    """
    접수 실패 건수입니다.
    """
    report_total_cnt: int | None = Field(default=None, validation_alias='reportTotalCnt', serialization_alias='reportTotalCnt')
    """
    리포트 전체 건수입니다.
    """
    report_succ_cnt: int | None = Field(default=None, validation_alias='reportSuccCnt', serialization_alias='reportSuccCnt')
    """
    리포트 성공 건수입니다.
    """
    report_fail_cnt: int | None = Field(default=None, validation_alias='reportFailCnt', serialization_alias='reportFailCnt')
    """
    리포트 실패 건수입니다.
    """


class MessageStatisticsResult(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    statistics: list[MessageStatistics] | None = None
    """
    일자별 통계 목록입니다.
    """


class MessageStatus(ResponseModel):
    """
    메시지 1건의 접수·발송·리포트 상태입니다. 대체발송이 일어나면 같은 msgKey로 채널별 항목이 여러 개 있습니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_key: str | None = Field(default=None, validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다.
    """
    service_type: str | None = Field(default=None, validation_alias='serviceType', serialization_alias='serviceType')
    """
    서비스 타입입니다.
    """
    msg_type: str | None = Field(default=None, validation_alias='msgType', serialization_alias='msgType')
    """
    메시지 타입입니다.
    """
    to: str | None = None
    """
    수신번호입니다.
    """
    fallback: Literal['Y', 'N'] | None = None
    """
    대체발송 여부입니다.
    """
    response_code: str | None = Field(default=None, validation_alias='responseCode', serialization_alias='responseCode')
    """
    접수 결과 코드입니다.
    """
    response_text: str | None = Field(default=None, validation_alias='responseText', serialization_alias='responseText')
    """
    접수 결과 메시지입니다.
    """
    request_time: str | None = Field(
        default=None,
        validation_alias='requestTime', serialization_alias='requestTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ssXXX"},
    )
    """
    요청 시각(ISO 8601)입니다.
    """
    send_time: str | None = Field(
        default=None,
        validation_alias='sendTime', serialization_alias='sendTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ssXXX"},
    )
    """
    발송 시각(ISO 8601)입니다.
    """
    report_time: str | None = Field(
        default=None,
        validation_alias='reportTime', serialization_alias='reportTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ssXXX"},
    )
    """
    리포트 시각(ISO 8601)입니다.
    """
    report_type: str | None = Field(default=None, validation_alias='reportType', serialization_alias='reportType')
    """
    리포트 타입입니다.
    """
    report_code: str | None = Field(default=None, validation_alias='reportCode', serialization_alias='reportCode')
    """
    리포트 코드입니다.
    """
    report_text: str | None = Field(default=None, validation_alias='reportText', serialization_alias='reportText')
    """
    리포트 결과 메시지입니다.
    """
    user_type: str | None = Field(default=None, validation_alias='userType', serialization_alias='userType')
    """
    채널 친구 여부입니다(브랜드메시지 전용).
    """
    carrier: str | None = None
    """
    이통사 코드입니다.
    """
    ref: str | None = None
    """
    요청 시 전달한 참조 필드입니다.
    """


class MessageStatusListResult(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    messages: list[MessageStatus] | None = None
    """
    메시지 목록입니다.
    """
    last_seq: int | None = Field(default=None, validation_alias='lastSeq', serialization_alias='lastSeq')
    """
    다음 페이지 조회에 쓰는 커서입니다. 다음 요청의 `lastSeq` 쿼리에 그대로 넣습니다.
    발송 이력 조회(`GET /message/history`) 응답에 있으며, 상태 조회(inquiry) 응답에는 없을 수 있습니다.

    """
    has_next: bool | None = Field(default=None, validation_alias='hasNext', serialization_alias='hasNext')
    """
    다음 페이지가 있는지 여부입니다. 발송 이력 조회 응답에 있습니다.
    """


class MoMessage(ResponseModel):
    """
    MO(수신) 메시지 1건입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_key: str | None = Field(default=None, validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다.
    """
    service_type: Literal['MO'] | None = Field(default=None, validation_alias='serviceType', serialization_alias='serviceType')
    """
    서비스 타입입니다. MO로 고정입니다.
    """
    msg_type: str | None = Field(default=None, validation_alias='msgType', serialization_alias='msgType')
    """
    메시지 타입입니다.
    """
    to: str | None = None
    """
    수신번호(MO 번호)입니다.
    """
    from_: str | None = Field(default=None, validation_alias='from', serialization_alias='from')
    """
    발신번호입니다(MO 발신자가 입력한 번호, 기본은 단말기 번호).
    """
    originator: str | None = None
    """
    실제 발신 원번호(MO 발신 단말기 번호)입니다.
    """
    content: str | None = None
    """
    MO 메시지 본문입니다.
    """
    carrier: str | None = None
    """
    이통사 코드입니다.
    """
    occurred_time: str | None = Field(
        default=None,
        validation_alias='occurredTime', serialization_alias='occurredTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ssXXX"},
    )
    """
    MO 발생 시각(ISO 8601)입니다.
    """


class MoMessageListResult(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    last_seq: int | None = Field(default=None, validation_alias='lastSeq', serialization_alias='lastSeq')
    """
    다음 페이지 조회에 쓰는 커서입니다(MO 이력 조회).
    """
    has_next: bool | None = Field(default=None, validation_alias='hasNext', serialization_alias='hasNext')
    """
    다음 페이지가 있는지 여부입니다(MO 이력 조회).
    """
    messages: list[MoMessage] | None = None
    """
    MO 메시지 목록입니다.
    """


class MoWebhookPayload(ResponseModel):
    """
    MO(인증/투표) 수신 웹훅 본문입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_key: str = Field(..., validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다.
    """
    service_type: Literal['MO'] = Field(..., validation_alias='serviceType', serialization_alias='serviceType')
    """
    서비스 타입입니다. MO로 고정입니다.
    """
    msg_type: Literal['SM'] = Field(..., validation_alias='msgType', serialization_alias='msgType')
    """
    메시지 타입입니다. SM으로 고정입니다.
    """
    to: str
    """
    수신번호(MO 번호)입니다.
    """
    from_: str = Field(..., validation_alias='from', serialization_alias='from')
    """
    MO 발신자가 입력한 번호입니다(기본은 단말기 번호).
    """
    carrier: str
    """
    이통사 코드입니다.
    """
    originator: str
    """
    MO 발신 단말기 번호입니다.
    """
    content: str
    """
    MO 메시지 본문입니다.
    """
    occurred_time: str = Field(
       default= ...,
        validation_alias='occurredTime', serialization_alias='occurredTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ssXXX"},
    )
    """
    MO 발생 시각(ISO 8601)입니다.
    """


class RcsBrandMediaUrl(ResponseModel):
    """
    브랜드 이미지의 파일 ID, URL, 사용 유형 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    file_id: str | None = Field(default=None, validation_alias='fileId', serialization_alias='fileId', examples=['FILE_ID_EXAMPLE'])
    """
    파일 ID입니다.
    """
    url: str | None = None
    """
    파일 URL입니다.
    """
    type_name: str | None = Field(default=None, validation_alias='typeName', serialization_alias='typeName')
    """
    이미지의 사용 유형입니다. 알려진 값(영문 문서 기준): `icon`(템플릿 양식 아이콘 이미지),
    `profile`(브랜드 프로필 이미지), `background`(브랜드 배경 이미지).

    """
    file_name: str | None = Field(default=None, validation_alias='fileName', serialization_alias='fileName')
    """
    등록한 파일의 이름입니다.
    """


class RcsBrandMenu(ResponseModel):
    """
    브랜드 홈 메뉴입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    button_type: str | None = Field(default=None, validation_alias='buttonType', serialization_alias='buttonType')
    """
    버튼 타입입니다.
    """
    applink: str | None = None
    """
    앱 링크입니다.
    """
    weblink: str | None = None
    """
    웹 링크입니다.
    """


class CreateCalendarEvent(ResponseModel):
    """
    일정 등록 객체입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    start_time: str = Field(..., validation_alias='startTime', serialization_alias='startTime')
    """
    시작 시간입니다.
    """
    end_time: str = Field(..., validation_alias='endTime', serialization_alias='endTime')
    """
    종료 시간입니다.
    """
    title: str
    """
    일정 제목입니다.
    """
    description: str | None = None
    """
    일정 설명입니다.
    """


class RcsCalendarAction(ResponseModel):
    """
    일정 등록 액션입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    create_calendar_event: CreateCalendarEvent = Field(..., validation_alias='createCalendarEvent', serialization_alias='createCalendarEvent')
    """
    일정 등록 객체입니다.
    """


class RcsChatbot(ResponseModel):
    """
    RCS 대화방(챗봇) 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    chatbot_id: str | None = Field(
        default=None, validation_alias='chatbotId', serialization_alias='chatbotId', examples=['CHATBOT_ID_EXAMPLE']
    )
    """
    대화방 ID입니다.
    """
    brand_id: str | None = Field(default=None, validation_alias='brandId', serialization_alias='brandId', examples=['BRAND_ID_EXAMPLE'])
    """
    대화방이 속한 브랜드 ID입니다.
    """
    group_id: str | None = Field(default=None, validation_alias='groupId', serialization_alias='groupId')
    """
    대화방이 속한 그룹 ID입니다.
    """
    mdn: str | None = Field(default=None, examples=['01000000000'])
    """
    대화방에 연결된 발신번호입니다.
    """
    sub_num: str | None = Field(default=None, validation_alias='subNum', serialization_alias='subNum')
    """
    대화방에 연결된 부가번호입니다.
    """
    is_main_num: Literal['Y', 'N'] | None = Field(default=None, validation_alias='isMainNum', serialization_alias='isMainNum')
    """
    대표번호 여부입니다. `Y` 대표번호, `N` 부가번호입니다(영문 문서 기준).
    """
    sub_title: str | None = Field(default=None, validation_alias='subTitle', serialization_alias='subTitle')
    """
    대화방 부제목입니다.
    """
    sub_descr: str | None = Field(default=None, validation_alias='subDescr', serialization_alias='subDescr')
    """
    대화방 부가 설명입니다.
    """
    service: str | None = None
    """
    대화방의 서비스 구분 값입니다.
    """
    display: str | None = None
    """
    대화방 노출 설정 값입니다.
    """
    input_field: int | None = Field(default=None, validation_alias='inputField', serialization_alias='inputField')
    """
    대화방 입력창 사용 설정 값입니다.
    """
    bot_agency_id: str | None = Field(default=None, validation_alias='botAgencyId', serialization_alias='botAgencyId')
    """
    대화방을 등록한 대행사 ID입니다.
    """
    safty_status_yn: str | None = Field(default=None, validation_alias='saftyStatusYn', serialization_alias='saftyStatusYn')
    """
    안심마크 지정 기업 여부입니다. 필드명은 문서 표기(`safty`)를 따릅니다.
    """
    ps_menu_use: Literal['Y', 'N'] | None = Field(default=None, validation_alias='psMenuUse', serialization_alias='psMenuUse')
    """
    고정 메뉴 사용 여부입니다. `Y` 사용, `N` 미사용입니다(영문 문서 기준).
    """
    persistent_menu: dict[str, Any] | None = Field(default=None, validation_alias='persistentMenu', serialization_alias='persistentMenu')
    """
    대화방 고정 메뉴 구성 정보입니다.
    """
    rcs_reply: str | None = Field(default=None, validation_alias='rcsReply', serialization_alias='rcsReply')
    """
    대화방 응답 설정 값입니다.
    """
    webhook: str | None = None
    """
    대화방 이벤트를 수신할 웹훅 URL입니다.
    """
    search_weight: str | None = Field(default=None, validation_alias='searchWeight', serialization_alias='searchWeight')
    """
    대화방 검색 가중치입니다.
    """
    bot_tc_page: str | None = Field(default=None, validation_alias='botTcPage', serialization_alias='botTcPage')
    """
    대화방 이용약관 페이지 주소입니다.
    """
    media_url: dict[str, Any] | None = Field(default=None, validation_alias='mediaUrl', serialization_alias='mediaUrl')
    """
    대화방 이미지 파일 ID와 URL 및 사용 유형 정보입니다.
    """
    status: str | None = None
    """
    대화방의 상태입니다. 문서 예시 값은 `ready`입니다.
    """
    approval_result: str | None = Field(default=None, validation_alias='approvalResult', serialization_alias='approvalResult')
    """
    대화방 승인 결과입니다. 문서 예시 값은 `approved`입니다.
    """
    approval_reason: str | None = Field(default=None, validation_alias='approvalReason', serialization_alias='approvalReason')
    """
    검수 시 반려 사유입니다.
    """
    approval_date: str | None = Field(default=None, validation_alias='approvalDate', serialization_alias='approvalDate')
    """
    승인일시입니다.
    """
    register_date: str | None = Field(default=None, validation_alias='registerDate', serialization_alias='registerDate')
    """
    등록일시입니다.
    """
    register_id: str | None = Field(default=None, validation_alias='registerId', serialization_alias='registerId')
    """
    등록자 ID입니다.
    """
    update_date: str | None = Field(default=None, validation_alias='updateDate', serialization_alias='updateDate')
    """
    수정일시입니다.
    """
    update_id: str | None = Field(default=None, validation_alias='updateId', serialization_alias='updateId')
    """
    수정자 ID입니다.
    """


class Rcs(ResponseModel):
    """
    RCS 응답 영역입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    chatbot: list[RcsChatbot] | None = None
    """
    대화방 정보 배열입니다. 상세 조회에서도 배열로 돌아옵니다.
    """


class RcsChatbotResult(ResponseModel):
    """
    대화방 조회·수정·승인 취소·삭제 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: Rcs | None = None
    """
    RCS 응답 영역입니다.
    """


class DialPhoneNumber(ResponseModel):
    """
    전화 걸기 객체입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    phone_number: str = Field(..., validation_alias='phoneNumber', serialization_alias='phoneNumber', examples=['01000000000'])
    """
    전화 번호입니다.
    """


class RcsDialerAction(ResponseModel):
    """
    전화 걸기 액션입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    dial_phone_number: DialPhoneNumber = Field(..., validation_alias='dialPhoneNumber', serialization_alias='dialPhoneNumber')
    """
    전화 걸기 객체입니다.
    """


class RcsFileUploadResult(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    media: str | None = Field(default=None, examples=['maapfile://MEDIA_KEY_EXAMPLE'])
    """
    RCS 메시지 본문(`body.media`)에 넣을 미디어 키입니다.
    """
    expired: str | None = Field(default=None, examples=['2027-04-24T12:16:38+09:00'])
    """
    미디어 키 만료 일시(ISO 8601)입니다.
    """


class RcsMessagebaseCommonSummary(ResponseModel):
    """
    공통 포맷 목록 항목입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    messagebaseform_id: str | None = Field(
        default=None, validation_alias='messagebaseformId', serialization_alias='messagebaseformId', examples=['MESSAGEBASEFORM_ID_EXAMPLE']
    )
    """
    템플릿의 원형인 템플릿 양식 ID입니다.
    """
    form_name: str | None = Field(default=None, validation_alias='formName', serialization_alias='formName')
    """
    포맷 이름입니다.
    """
    biz_condition: list[str] | None = Field(default=None, validation_alias='bizCondition', serialization_alias='bizCondition')
    """
    비즈 조건 목록입니다.
    """
    card_type: str | None = Field(default=None, validation_alias='cardType', serialization_alias='cardType')
    """
    카드 유형입니다. 문서 예시 값은 `standalone media top`입니다.
    """
    format_id: str | None = Field(default=None, validation_alias='formatId', serialization_alias='formatId')
    """
    템플릿 포맷 ID입니다.
    """
    template_name: str | None = Field(default=None, validation_alias='templateName', serialization_alias='templateName')
    """
    템플릿 등록 시 입력된 템플릿 명칭입니다.
    """
    brand_id: str | None = Field(default=None, validation_alias='brandId', serialization_alias='brandId')
    """
    브랜드 ID입니다.
    """
    status: str | None = None
    """
    템플릿의 상태입니다.
    """
    approval_result: str | None = Field(default=None, validation_alias='approvalResult', serialization_alias='approvalResult')
    """
    템플릿의 승인 상태입니다.
    """
    update_id: str | None = Field(default=None, validation_alias='updateId', serialization_alias='updateId')
    """
    템플릿 수정 계정 ID입니다.
    """
    register_date: str | None = Field(
        default=None,
        validation_alias='registerDate', serialization_alias='registerDate',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss"},
    )
    """
    템플릿 등록일시입니다. 문서 예시는 `yyyy-MM-dd'T'HH:mm:ss` 형식입니다.
    """
    approval_date: str | None = Field(default=None, validation_alias='approvalDate', serialization_alias='approvalDate')
    """
    템플릿 승인일시입니다.
    """
    update_date: str | None = Field(
        default=None,
        validation_alias='updateDate', serialization_alias='updateDate',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss"},
    )
    """
    템플릿 수정일시입니다. 문서 예시는 `yyyy-MM-dd'T'HH:mm:ss` 형식입니다.
    """


class RcsMessagebaseFormSummary(ResponseModel):
    """
    템플릿 양식 목록 항목입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    messagebaseform_id: str | None = Field(
        default=None, validation_alias='messagebaseformId', serialization_alias='messagebaseformId', examples=['MESSAGEBASEFORM_ID_EXAMPLE']
    )
    """
    템플릿 양식 ID입니다.
    """
    form_name: str | None = Field(default=None, validation_alias='formName', serialization_alias='formName')
    """
    템플릿 양식명입니다.
    """
    biz_condition: str | None = Field(default=None, validation_alias='bizCondition', serialization_alias='bizCondition')
    """
    양식을 사용할 수 있는 대상 업태의 목록입니다.
    """
    card_type: str | None = Field(default=None, validation_alias='cardType', serialization_alias='cardType')
    """
    카드 종류입니다.
    """
    biz_category: str | None = Field(default=None, validation_alias='bizCategory', serialization_alias='bizCategory')
    """
    Description, Cell의 유형 그룹입니다.
    """
    biz_service: str | None = Field(default=None, validation_alias='bizService', serialization_alias='bizService')
    """
    Description, Cell의 세부 유형입니다.
    """
    register_date: str | None = Field(default=None, validation_alias='registerDate', serialization_alias='registerDate')
    """
    등록일시입니다.
    """
    update_date: str | None = Field(default=None, validation_alias='updateDate', serialization_alias='updateDate')
    """
    수정일시입니다.
    """


class RcsMessagebasePagination(ResponseModel):
    """
    전체 건수와 페이지 조건 정보입니다. 문서상 모든 값이 문자열입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    offset: str | None = None
    """
    조회 기준 위치입니다.
    """
    limit: str | None = None
    """
    페이지당 조회 건수입니다.
    """
    total: str | None = None
    """
    전체 건수입니다.
    """


class RcsMessagebasePolicyInfo(ResponseModel):
    """
    리치카드, 오픈리치카드에 포함된 content에 대한 검증 정책입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    buttons_allowed: bool | None = Field(default=None, validation_alias='buttonsAllowed', serialization_alias='buttonsAllowed')
    """
    버튼 사용 가능 여부입니다.
    """
    ad_header_allowed: bool | None = Field(default=None, validation_alias='adHeaderAllowed', serialization_alias='adHeaderAllowed')
    """
    헤더 광고 문구 사용 여부입니다.
    """
    ad_body_allowed: bool | None = Field(default=None, validation_alias='adBodyAllowed', serialization_alias='adBodyAllowed')
    """
    본문 광고 문구 사용 여부입니다.
    """
    card_count: int | None = Field(default=None, validation_alias='cardCount', serialization_alias='cardCount')
    """
    카드 개수입니다.
    """
    max_button_count: int | None = Field(default=None, validation_alias='maxButtonCount', serialization_alias='maxButtonCount')
    """
    최대 버튼 개수입니다.
    """
    max_description_size: int | None = Field(default=None, validation_alias='maxDescriptionSize', serialization_alias='maxDescriptionSize')
    """
    description 영역 최대 글자 수입니다.
    """
    max_media_size: int | None = Field(default=None, validation_alias='maxMediaSize', serialization_alias='maxMediaSize')
    """
    미디어 최대 크기입니다.
    """


class RcsTemplateBodyParam(ResponseModel):
    """
    템플릿 본문 영역의 검증 파라미터 정의입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    param: str = Field(..., pattern='^[A-Za-z0-9_]+$')
    """
    검증 파라미터명입니다. 영문, 숫자, `_`만 쓸 수 있습니다(영문 문서 기준).
    """
    is_mandatory: str = Field(..., validation_alias='isMandatory', serialization_alias='isMandatory')
    """
    필수 여부입니다.
    """
    type: str | None = None
    """
    기술 검증 타입입니다.
    """
    str_size: str | None = Field(default=None, validation_alias='strSize', serialization_alias='strSize')
    """
    문자열 최대 크기입니다. 문서상 문자열입니다.
    """
    image_width: str | None = Field(default=None, validation_alias='imageWidth', serialization_alias='imageWidth')
    """
    이미지 최소 가로 크기입니다. 문서상 문자열입니다.
    """
    image_height: str | None = Field(default=None, validation_alias='imageHeight', serialization_alias='imageHeight')
    """
    이미지 최소 세로 크기입니다. 문서상 문자열입니다.
    """


class CopyToClipboard(ResponseModel):
    """
    클립보드 복사 객체입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    text: str
    """
    클립보드에 복사할 텍스트입니다.
    """


class RcsTemplateClipboardAction(ResponseModel):
    """
    클립보드 복사 액션입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    copy_to_clipboard: CopyToClipboard = Field(..., validation_alias='copyToClipboard', serialization_alias='copyToClipboard')
    """
    클립보드 복사 객체입니다.
    """


class ComposeTextMessage(ResponseModel):
    """
    문자 보내기 객체입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    phone_number: str = Field(..., validation_alias='phoneNumber', serialization_alias='phoneNumber', examples=['01000000000'])
    """
    전화번호입니다.
    """
    text: str | None = None
    """
    문자(SMS/LMS/MMS) 내용입니다.
    """


class ComposeRecordingMessage(ResponseModel):
    """
    음성/영상 보내기 객체입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    phone_number: str = Field(..., validation_alias='phoneNumber', serialization_alias='phoneNumber', examples=['01000000000'])
    """
    전화번호입니다.
    """
    type: Literal['VIDEO', 'AUDIO']
    """
    영상(`VIDEO`) 또는 음성(`AUDIO`)입니다.
    """


class RcsTemplateComposeAction(ResponseModel):
    """
    템플릿 버튼의 문자/음성/영상 보내기 액션입니다. 발송용 `RcsComposeAction`과 달리 `composeTextMessage`가 선택입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    compose_text_message: ComposeTextMessage | None = Field(
        default=None, validation_alias='composeTextMessage', serialization_alias='composeTextMessage'
    )
    """
    문자 보내기 객체입니다.
    """
    compose_recording_message: ComposeRecordingMessage | None = Field(
        default=None, validation_alias='composeRecordingMessage', serialization_alias='composeRecordingMessage'
    )
    """
    음성/영상 보내기 객체입니다.
    """


class RcsTemplateDetailBody(ResponseModel):
    """
    템플릿 상세 조회의 본문 영역입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    description: str | None = None
    """
    본문 내용입니다. `#{변수}` 형태의 치환 변수를 포함할 수 있습니다.
    """
    m_title: str | None = Field(default=None, validation_alias='mTitle', serialization_alias='mTitle')
    """
    메인 타이틀입니다.
    """
    title: str | None = None
    """
    타이틀입니다.
    """


class RcsTemplateFormLogo(ResponseModel):
    """
    템플릿 양식 로고 이미지 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    file_id: str | None = Field(default=None, validation_alias='fileId', serialization_alias='fileId', examples=['FILE_ID_EXAMPLE'])
    """
    로고 이미지 파일 ID입니다.
    """
    file_url: str | None = Field(default=None, validation_alias='fileUrl', serialization_alias='fileUrl')
    """
    로고 이미지 파일 URL입니다.
    """
    file_name: str | None = Field(default=None, validation_alias='fileName', serialization_alias='fileName', max_length=256)
    """
    로고 이미지 파일 이름입니다(최대 256자).
    """


class Rcs4(ResponseModel):
    """
    RCS 응답 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    images: list[RcsTemplateFormLogo] | None = None
    """
    템플릿 양식 로고 이미지 목록입니다.
    """


class RcsTemplateFormLogoListResult(ResponseModel):
    """
    템플릿 양식 로고 이미지 조회 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: Rcs4 | None = None
    """
    RCS 응답 정보입니다.
    """


class Rcs5(ResponseModel):
    """
    RCS 응답 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    messagebase_id: str | None = Field(
        default=None, validation_alias='messagebaseId', serialization_alias='messagebaseId', examples=['MESSAGEBASE_ID_EXAMPLE']
    )
    """
    처리된 메시지베이스 ID입니다. 발송 시에는 이 값을 `formatId` 필드에 넣습니다(영문 문서 기준).
    """


class RcsTemplateIdResult(ResponseModel):
    """
    템플릿 등록·수정·승인 취소·삭제 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: Rcs5 | None = None
    """
    RCS 응답 정보입니다.
    """


class RcsTemplateImage(ResponseModel):
    """
    템플릿 이미지 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    file_id: str | None = Field(default=None, validation_alias='fileId', serialization_alias='fileId', examples=['FILE_ID_EXAMPLE'])
    """
    템플릿 파일 ID입니다.
    """
    file_name: str | None = Field(default=None, validation_alias='fileName', serialization_alias='fileName')
    """
    파일 이름입니다.
    """
    image_width: int | None = Field(default=None, validation_alias='imageWidth', serialization_alias='imageWidth')
    """
    이미지 가로 크기입니다.
    """
    image_height: int | None = Field(default=None, validation_alias='imageHeight', serialization_alias='imageHeight')
    """
    이미지 세로 크기입니다.
    """


class Rcs6(ResponseModel):
    """
    RCS 응답 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    image: RcsTemplateImage | None = None


class RcsTemplateImageResult(ResponseModel):
    """
    템플릿 이미지 등록·상세 조회 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: Rcs6 | None = None
    """
    RCS 응답 정보입니다.
    """


class Location(ResponseModel):
    """
    지도 위치 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    latitude: float
    """
    위도입니다.
    """
    longitude: float
    """
    경도입니다.
    """
    label: str | None = None
    """
    라벨입니다.
    """
    query: str
    """
    검색 내용입니다.
    """


class ShowLocation(ResponseModel):
    """
    지도 위치 표시 객체입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    location: Location
    """
    지도 위치 정보입니다.
    """


class RcsTemplateMapAction(ResponseModel):
    """
    템플릿 버튼의 지도 액션입니다. 발송용 `RcsMapAction`과 달리 `showLocation`이 선택이고
    `fallbackUrl`이 `mapAction` 바로 아래에 있으며, 위치 `label`이 문자열입니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    show_location: ShowLocation | None = Field(default=None, validation_alias='showLocation', serialization_alias='showLocation')
    """
    지도 위치 표시 객체입니다.
    """
    fallback_url: str | None = Field(default=None, validation_alias='fallbackUrl', serialization_alias='fallbackUrl')
    """
    위치 조회 실패 시 이동할 fallback URL입니다.
    """
    request_location_push: dict[str, Any] | None = Field(
        default=None, validation_alias='requestLocationPush', serialization_alias='requestLocationPush'
    )
    """
    위치 전송 요청 객체입니다.
    """


class RcsTemplateSummary(ResponseModel):
    """
    RCS 템플릿 목록 항목입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    messagebase_id: str | None = Field(
        default=None, validation_alias='messagebaseId', serialization_alias='messagebaseId', examples=['MESSAGEBASE_ID_EXAMPLE']
    )
    """
    메시지베이스 ID입니다. 발송 시에는 이 값을 `formatId` 필드에 넣습니다(영문 문서 기준).
    """
    format_id: str | None = Field(default=None, validation_alias='formatId', serialization_alias='formatId')
    """
    템플릿 양식 ID입니다.
    """
    template_name: str | None = Field(default=None, validation_alias='templateName', serialization_alias='templateName')
    """
    템플릿 이름입니다.
    """
    brand_id: str | None = Field(default=None, validation_alias='brandId', serialization_alias='brandId')
    """
    브랜드 ID입니다.
    """
    status: str | None = None
    """
    템플릿의 상태입니다. 알려진 값(영문 문서 기준)은 `ready`(사용 중), `pause`(중지)입니다.
    """
    approval_result: str | None = Field(default=None, validation_alias='approvalResult', serialization_alias='approvalResult')
    """
    템플릿의 승인 상태입니다. 문서 예시 값은 `approved`입니다.
    """
    approval_reason: str | None = Field(default=None, validation_alias='approvalReason', serialization_alias='approvalReason')
    """
    승인 사유입니다.
    """
    register_date: str | None = Field(default=None, validation_alias='registerDate', serialization_alias='registerDate')
    """
    템플릿 등록일시입니다.
    """
    approval_date: str | None = Field(default=None, validation_alias='approvalDate', serialization_alias='approvalDate')
    """
    템플릿 승인일시입니다.
    """
    update_date: str | None = Field(default=None, validation_alias='updateDate', serialization_alias='updateDate')
    """
    템플릿 수정일시입니다.
    """
    register_id: str | None = Field(default=None, validation_alias='registerId', serialization_alias='registerId')
    """
    템플릿 등록 계정 ID입니다.
    """
    update_id: str | None = Field(default=None, validation_alias='updateId', serialization_alias='updateId')
    """
    템플릿 수정 계정 ID입니다.
    """


class OpenUrl(ResponseModel):
    """
    웹 링크 연결 객체입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    url: str = Field(..., examples=['https://example.com'])
    """
    웹 링크 URL입니다.
    """


class RcsUrlAction(ResponseModel):
    """
    웹 링크 연결 액션입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    open_url: OpenUrl = Field(..., validation_alias='openUrl', serialization_alias='openUrl')
    """
    웹 링크 연결 객체입니다.
    """


class Report(ResponseModel):
    """
    메시지 발송 결과 리포트 1건입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_key: str | None = Field(default=None, validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다.
    """
    service_type: str | None = Field(default=None, validation_alias='serviceType', serialization_alias='serviceType')
    """
    서비스 타입입니다.
    """
    msg_type: str | None = Field(default=None, validation_alias='msgType', serialization_alias='msgType')
    """
    메시지 타입입니다(예 SM, RS, AT, FT).
    """
    send_time: str | None = Field(
        default=None,
        validation_alias='sendTime', serialization_alias='sendTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ssXXX"},
    )
    """
    전송 처리 일시입니다.
    """
    report_time: str | None = Field(
        default=None,
        validation_alias='reportTime', serialization_alias='reportTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ssXXX"},
    )
    """
    리포트 수신 일시입니다.
    """
    report_type: str | None = Field(default=None, validation_alias='reportType', serialization_alias='reportType')
    """
    리포트 종류입니다.
    """
    report_code: str | None = Field(default=None, validation_alias='reportCode', serialization_alias='reportCode', examples=['10000'])
    """
    리포트 코드입니다. `10000`이면 성공입니다.
    """
    report_text: str | None = Field(default=None, validation_alias='reportText', serialization_alias='reportText')
    """
    리포트 상세 내용입니다.
    """
    carrier: str | None = None
    """
    (문자메시지) 이통사 코드입니다.
    """
    user_type: str | None = Field(default=None, validation_alias='userType', serialization_alias='userType')
    """
    (카카오 브랜드메시지) 메시지 발송 처리 타입입니다.
    """
    res_cnt: str | None = Field(default=None, validation_alias='resCnt', serialization_alias='resCnt')
    """
    (국제메시지) 메시지 분할 수입니다.
    """
    ref: str | None = None
    """
    요청 시 입력한 참조 필드입니다.
    """


class ReportInquiryResult(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    report: list[Report] | None = None
    """
    리포트 목록입니다.
    """


class ReportPollingResult(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    report_id: str | None = Field(default=None, validation_alias='reportId', serialization_alias='reportId')
    """
    수신 확인(`DELETE /api/comm/v1/report/polling/{reportId}`)에 쓰는 리포트 ID입니다. 전달할 리포트가 없으면 빈 문자열입니다.
    """
    report: list[Report] | None = None
    """
    리포트 목록입니다. 전달할 리포트가 없으면 null입니다.
    """


class ReportWebhookPayload(ResponseModel):
    """
    리포트 웹훅 본문입니다. 리포트 1건당 1회 전송됩니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_key: str = Field(..., validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다.
    """
    service_type: str = Field(..., validation_alias='serviceType', serialization_alias='serviceType')
    """
    서비스 타입입니다.
    """
    msg_type: str | None = Field(default=None, validation_alias='msgType', serialization_alias='msgType')
    """
    메시지 타입입니다.
    """
    send_time: str | None = Field(
        default=None,
        validation_alias='sendTime', serialization_alias='sendTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    전송 처리 일시입니다.
    """
    report_time: str = Field(
       default= ...,
        validation_alias='reportTime', serialization_alias='reportTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    리포트 수신 일시입니다.
    """
    report_type: str = Field(..., validation_alias='reportType', serialization_alias='reportType')
    """
    리포트 종류입니다.
    """
    report_code: str = Field(..., validation_alias='reportCode', serialization_alias='reportCode')
    """
    리포트 코드입니다.
    """
    report_text: str | None = Field(default=None, validation_alias='reportText', serialization_alias='reportText')
    """
    리포트 상세 내용입니다.
    """
    carrier: str | None = None
    """
    (문자메시지) 이통사 코드입니다.
    """
    user_type: str | None = Field(default=None, validation_alias='userType', serialization_alias='userType')
    """
    (카카오 브랜드메시지) 메시지 발송 처리 타입입니다.
    """
    res_cnt: str | None = Field(default=None, validation_alias='resCnt', serialization_alias='resCnt')
    """
    (국제메시지) 메시지 분할 수입니다.
    """
    ref: str | None = None
    """
    요청 시 입력한 참조 필드입니다.
    """


class Reservation(ResponseModel):
    """
    예약 발송 건입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    seq: int | None = None
    """
    예약 순번입니다. 목록 조회의 `lastSeq` 기준값으로 쓸 수 있습니다.
    """
    resv_key: str | None = Field(default=None, validation_alias='resvKey', serialization_alias='resvKey', examples=['RESV_KEY_EXAMPLE'])
    """
    예약 발송 키입니다.
    """
    payment_code: str | None = Field(default=None, validation_alias='paymentCode', serialization_alias='paymentCode')
    """
    정산 코드입니다.
    """
    resv_name: str | None = Field(default=None, validation_alias='resvName', serialization_alias='resvName')
    """
    예약명입니다.
    """
    product_type: str | None = Field(default=None, validation_alias='productType', serialization_alias='productType')
    """
    상품 유형입니다. 알려진 값은 `MESSAGE`입니다.
    """
    status: str | None = None
    """
    예약 상태입니다. 알려진 값: `PENDING`(예약 대기), `PROCESSING`(발송 처리 중), `STOPPED`(예약 중지), `CANCELLED`(취소).
    수정은 PENDING, 취소는 PENDING·STOPPED, 중지는 PROCESSING, 재개는 STOPPED 상태에서만 할 수 있습니다(그 밖에는 A824).

    """
    ad_yn: str | None = Field(default=None, validation_alias='adYn', serialization_alias='adYn')
    """
    광고 메시지 여부입니다(Y/N).
    """
    resv_send_time: str | None = Field(
        default=None,
        validation_alias='resvSendTime', serialization_alias='resvSendTime',
        json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'},
    )
    """
    예약 발송 시각입니다(yyyy-MM-dd HH:mm:ss).
    """
    resv_data: str | None = Field(default=None, validation_alias='resvData', serialization_alias='resvData')
    """
    예약 발송 요청 본문(JSON 문자열)입니다. 수정 응답과 목록 응답 예시에는 없습니다.
    """
    expected_cnt: int | None = Field(default=None, validation_alias='expectedCnt', serialization_alias='expectedCnt')
    """
    예상 발송 수량입니다.
    """
    sent_cnt: int | None = Field(default=None, validation_alias='sentCnt', serialization_alias='sentCnt')
    """
    발송 처리 수량입니다.
    """
    success_cnt: int | None = Field(default=None, validation_alias='successCnt', serialization_alias='successCnt')
    """
    성공 수량입니다.
    """
    fail_cnt: int | None = Field(default=None, validation_alias='failCnt', serialization_alias='failCnt')
    """
    실패 수량입니다.
    """
    update_date: str | None = Field(
        default=None, validation_alias='updateDate', serialization_alias='updateDate', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    수정 일시입니다(yyyy-MM-dd HH:mm:ss).
    """
    reg_date: str | None = Field(
        default=None, validation_alias='regDate', serialization_alias='regDate', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    등록 일시입니다(yyyy-MM-dd HH:mm:ss).
    """


class ReservationListResult(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    last_seq: int | None = Field(default=None, validation_alias='lastSeq', serialization_alias='lastSeq')
    """
    다음 페이지 조회에 쓰는 커서입니다. 다음 요청의 `lastSeq` 쿼리에 그대로 넣습니다. 결과가 없으면 0입니다.
    """
    has_next: bool | None = Field(default=None, validation_alias='hasNext', serialization_alias='hasNext')
    """
    다음 페이지가 있는지 여부입니다.
    """
    reservations: list[Reservation] | None = None
    """
    예약 발송 건 목록입니다.
    """


class ReservationRecipient(ResponseModel):
    """
    예약 건에 등록된 수신자입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_key: str | None = Field(default=None, validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다. 수신자 삭제에 씁니다.
    """
    dest_seq: int | None = Field(default=None, validation_alias='destSeq', serialization_alias='destSeq')
    """
    수신자 순번입니다.
    """
    to: str | None = Field(default=None, examples=['01000000000'])
    """
    수신번호입니다.
    """
    dest_data: str | None = Field(default=None, validation_alias='destData', serialization_alias='destData')
    """
    수신자별 치환 데이터입니다.
    """
    status: str | None = None
    """
    수신자 상태입니다. 알려진 값은 `PENDING`입니다.
    """
    response_code: str | None = Field(default=None, validation_alias='responseCode', serialization_alias='responseCode')
    """
    처리 결과 코드입니다.
    """
    response_text: str | None = Field(default=None, validation_alias='responseText', serialization_alias='responseText')
    """
    처리 결과 메시지입니다.
    """


class ReservationRecipientListResult(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    last_seq: int | None = Field(default=None, validation_alias='lastSeq', serialization_alias='lastSeq')
    """
    다음 페이지 조회에 쓰는 커서입니다. 다음 요청의 `lastSeq` 쿼리에 그대로 넣습니다.
    """
    has_next: bool | None = Field(default=None, validation_alias='hasNext', serialization_alias='hasNext')
    """
    다음 페이지가 있는지 여부입니다.
    """
    destinations: list[ReservationRecipient] | None = None
    """
    예약 수신자 목록입니다.
    """


class SendDestinationResult(ResponseModel):
    """
    수신자별 접수 결과입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    to: str | None = None
    """
    수신번호입니다.
    """
    msg_key: str | None = Field(
        default=None, validation_alias='msgKey', serialization_alias='msgKey', examples=['20260424104234546POM101182450000']
    )
    """
    메시지 키입니다. 리포트·상태 조회에 씁니다. 끝 3자리를 뺀 값이 동보 요청의 `requestId`입니다.
    """
    code: str | None = Field(default=None, examples=['A000'])
    """
    수신자별 접수 코드입니다. `A000`이 아니면 해당 수신자는 접수되지 않은 것입니다.
    """
    result: str | None = Field(default=None, examples=['Success'])
    """
    수신자별 접수 결과입니다.
    """


class SendOmniResult(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    destinations: list[SendDestinationResult] | None = None
    """
    수신자별 접수 결과입니다.
    """


class ServiceResult(ResponseModel):
    """
    상품 API 처리 결과(개별부)입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    code: str | None = Field(default=None, examples=['A000'])
    """
    처리 결과 코드입니다. `A000`이면 성공입니다. 코드 목록은 에러코드 문서를 참고합니다.
    """
    result: str | None = Field(default=None, examples=['Success'])
    """
    처리 결과 설명입니다.
    """
    ref: str | None = None
    """
    요청 시 전달한 참조값입니다.
    """


class WebhookAck(ResponseModel):
    """
    웹훅 수신 응답입니다. 받은 `msgKey`를 그대로 돌려줘야 성공 처리되며, 없거나 규격이 다르면 재전송됩니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_key: str = Field(..., validation_alias='msgKey', serialization_alias='msgKey')
    """
    수신한 메시지 키입니다.
    """


class AlimtalkItem(ResponseModel):
    """
    알림톡 아이템 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    list_: list[AlimtalkItemListEntry] | None = Field(
        default=None, validation_alias='list', serialization_alias='list', max_length=10, min_length=2
    )
    """
    아이템 리스트입니다. 최소 2개, 최대 10개입니다.
    """
    summary: AlimtalkItemSummary | None = None


class AlimtalkTemplateCategoryServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: AlimtalkTemplateCategoryResult | None = None


class AlimtalkTemplateImageUploadServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: AlimtalkTemplateImageUploadResult | None = None


class AlimtalkTemplatePublicListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: AlimtalkTemplatePublicListResult | None = None


class ApiResponse(ResponseModel):
    """
    개별 데이터가 없는 기본 응답 봉투입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: ServiceResult | None = None


class BrandMessageAudienceEstimateServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageAudienceEstimateResult | None = None


class BrandMessageAudienceFriendCountServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageAudienceFriendCountResult | None = None


class BrandMessageAudiencePossibleServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageAudiencePossibleResult | None = None


class BrandMessageCarouselItemAttachment(ResponseModel):
    """
    캐러셀 아이템 첨부 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    button: list[BrandMessageButton] | None = Field(default=None, max_length=5)
    """
    캐러셀 아이템 버튼 목록입니다. 최대 5개이며, FC/FA 타입에 쿠폰을 함께 쓰면 최대 4개입니다.
    """
    image: BrandMessageImage | None = None
    coupon: BrandMessageCoupon | None = None
    commerce: BrandMessageCommerce | None = None


class BrandMessageCatalog(ResponseModel):
    """
    브랜드메시지 카탈로그 요소입니다. `msgType`이 `FG`일 때 사용합니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    list_: list[BrandMessageCatalogItem] | None = Field(
        default=None, validation_alias='list', serialization_alias='list', max_length=7, min_length=3
    )
    """
    카탈로그 아이템 목록입니다. FG 타입에서 필수이며 최소 3개, 최대 7개입니다.
    아이템이 홀수 개(3·5·7)이면 첫 번째 아이템만 2:1 가로형 이미지(카탈로그 홀수형 첫번째 이미지 업로드)를, 나머지는 1:1 정사각형 이미지(카탈로그 이미지 업로드)를 씁니다. 짝수 개(4·6)이면 전부 1:1입니다.

    """


class BrandMessageFileUploadServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageFileUploadResult | None = None


class BrandMessageFriendGroupFileUploadServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageFriendGroupFileUploadResult | None = None


class BrandMessageFriendGroupListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageFriendGroupListResult | None = None


class BrandMessageFriendGroupPhoneNumberRequestListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageFriendGroupPhoneNumberRequestListResult | None = None


class BrandMessageFriendGroupPhoneNumberRequestServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageFriendGroupPhoneNumberRequestResult | None = None


class BrandMessageFriendGroupProcessingServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageFriendGroupProcessingResult | None = None


class BrandMessageFriendGroupServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageFriendGroupResult | None = None


class BrandMessageGroupSendServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageGroupSendResult | None = None


class BrandMessageGroupTagListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageGroupTagListResult | None = None


class BrandMessageItem(ResponseModel):
    """
    브랜드메시지 와이드 아이템 요소입니다(와이드 리스트형, FL).
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    list_: list[BrandMessageItemListEntry] | None = Field(default=None, validation_alias='list', serialization_alias='list')
    """
    아이템 목록입니다.
    """


class BrandMessageMarketingAgreeServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageMarketingAgreeResult | None = None


class Brandmessage3(ResponseModel):
    """
    브랜드메시지 템플릿 결과 영역입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    templates: list[BrandMessageTemplateSummary] | None = None
    """
    조회한 템플릿 목록입니다.
    """


class BrandMessageTemplateListResult(ResponseModel):
    """
    템플릿 목록 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brandmessage: Brandmessage3 | None = None
    """
    브랜드메시지 템플릿 결과 영역입니다.
    """


class BrandMessageTemplateListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageTemplateListResult | None = None


class BrandMessageVideoInfoServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageVideoInfoResult | None = None


class BrandMessageVideoListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageVideoListResult | None = None


class BrandMessageVideoUploadRegisterServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageVideoUploadRegisterResult | None = None


class CounselCertResultWebhookPayload(CounselWebhookCommon):
    """
    본인인증 결과 수신 웹훅(`{고객 Webhook URL}/cstalk/cert_result`) 본문입니다. `KAKAO_CERT` 말풍선으로 요청한 카카오톡 본인인증(전자서명)이 완료되면
    상담 세션 상태와 관계없이 전달됩니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_type: str = Field(..., validation_alias='msgType', serialization_alias='msgType')
    """
    메시지 타입입니다. 문서 예시 값은 `KAKAO_CERT`입니다.
    """
    request_type: Literal['cert_result'] = Field(..., validation_alias='requestType', serialization_alias='requestType')
    """
    요청 타입입니다. `cert_result`로 전달됩니다.
    """
    session_id: str | None = Field(default=None, validation_alias='sessionId', serialization_alias='sessionId')
    """
    상담 세션 ID입니다.
    """
    cert_tx_id: str = Field(..., validation_alias='certTxId', serialization_alias='certTxId')
    """
    인증 트랜잭션 ID입니다. 인증 상태 조회 API(`/api/comm/v1/center/cstalk/cert/status`)의 `certTxId`와 같은 값입니다.
    """
    cert_result: str = Field(..., validation_alias='certResult', serialization_alias='certResult')
    """
    AES256/CTR/NoPadding으로 암호화한 뒤 Base64로 인코딩한 본인인증 결과입니다. 복호화하면 이름·전화번호·생년월일·성별·내외국인·CI가 들어 있습니다
    (`ci`는 취급 검증을 마친 발신프로필에만 제공). 복호화 키는 카카오가 이메일로 별도 전달하며 Base64로 인코딩되어 있습니다.
    카카오 정책상 저장하지 말고 사용자를 식별한 즉시 파기해야 하며, 로그·APM·에러 리포트에 남지 않도록 마스킹합니다.

    """
    msg_key: str = Field(..., validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다. 발송 결과(`result`)에서는 발송 API 응답의 msgKey와 같고, 수신 6종에서는 이벤트마다 새로 발급된 값이라 발송 건과 대응하지 않습니다.
    재시도로 같은 이벤트가 다시 올 수 있으므로 msgKey 기준으로 멱등 처리합니다.

    """
    user_key: str = Field(..., validation_alias='userKey', serialization_alias='userKey')
    """
    상담톡 사용자 키입니다. 카카오톡 채널별로 다르며 대소문자를 구분하고, 사용자가 탈퇴 후 재가입하면 바뀝니다.
    """
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey')
    """
    메시지를 수신한 발신프로필 키입니다.
    """
    service_type: str = Field(..., validation_alias='serviceType', serialization_alias='serviceType')
    """
    서비스 타입입니다. 문서 예시 값은 `CSTALK`입니다.
    """
    send_time: str = Field(
       default= ...,
        validation_alias='sendTime', serialization_alias='sendTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 이벤트를 수신한 시각입니다.
    """
    report_time: str = Field(
       default= ...,
        validation_alias='reportTime', serialization_alias='reportTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 웹훅을 전송한 시각입니다.
    """


class CounselCertStatusServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: CounselCertStatusResult | None = None


class CounselConsultTime(ResponseModel):
    """
    상담 운영 시간입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    week_time_table: list[CounselWeekTime] | None = Field(default=None, validation_alias='weekTimeTable', serialization_alias='weekTimeTable')
    """
    요일별 상담 시간 목록입니다.
    """


class CounselConsultTimeResult(ResponseModel):
    """
    상담시간 조회 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    cstalk: CounselConsultTime | None = None


class CounselConsultTimeServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: CounselConsultTimeResult | None = None


class CounselEndServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: CounselEndResult | None = None


class CounselExpiredSessionWebhookPayload(CounselWebhookCommon):
    """
    세션 종료 수신 웹훅(`{고객 Webhook URL}/cstalk/expired_session`) 본문입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_type: str = Field(..., validation_alias='msgType', serialization_alias='msgType')
    """
    메시지 타입입니다. 문서 예시 값은 `SESSION`입니다.
    """
    request_type: str = Field(..., validation_alias='requestType', serialization_alias='requestType')
    """
    요청 타입입니다. 문서 예시 값은 `expired_session`입니다.
    """
    session_id: str | None = Field(default=None, validation_alias='sessionId', serialization_alias='sessionId')
    """
    종료된 상담 세션 아이디입니다.
    """
    msg_key: str = Field(..., validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다. 발송 결과(`result`)에서는 발송 API 응답의 msgKey와 같고, 수신 6종에서는 이벤트마다 새로 발급된 값이라 발송 건과 대응하지 않습니다.
    재시도로 같은 이벤트가 다시 올 수 있으므로 msgKey 기준으로 멱등 처리합니다.

    """
    user_key: str = Field(..., validation_alias='userKey', serialization_alias='userKey')
    """
    상담톡 사용자 키입니다. 카카오톡 채널별로 다르며 대소문자를 구분하고, 사용자가 탈퇴 후 재가입하면 바뀝니다.
    """
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey')
    """
    메시지를 수신한 발신프로필 키입니다.
    """
    service_type: str = Field(..., validation_alias='serviceType', serialization_alias='serviceType')
    """
    서비스 타입입니다. 문서 예시 값은 `CSTALK`입니다.
    """
    send_time: str = Field(
       default= ...,
        validation_alias='sendTime', serialization_alias='sendTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 이벤트를 수신한 시각입니다.
    """
    report_time: str = Field(
       default= ...,
        validation_alias='reportTime', serialization_alias='reportTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 웹훅을 전송한 시각입니다.
    """


class CounselFileUploadServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: CounselFileUploadResult | None = None


class CounselImageUploadServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: CounselImageUploadResult | None = None


class CounselMessageWebhookPayload(CounselWebhookCommon):
    """
    사용자 메시지 수신 웹훅(`{고객 Webhook URL}/cstalk/message`) 본문입니다. 사용자가 보낸 상담 내용이 담기므로 개인정보로 취급합니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_type: str = Field(..., validation_alias='msgType', serialization_alias='msgType')
    """
    메시지 타입입니다. 문서 예시 값은 `TEXT`입니다.
    """
    request_type: str | None = Field(default=None, validation_alias='requestType', serialization_alias='requestType')
    """
    요청 타입입니다. 문서 예시 값은 `message`입니다. 이 웹훅에서만 필수가 아닙니다.
    """
    session_id: str | None = Field(default=None, validation_alias='sessionId', serialization_alias='sessionId')
    """
    상담 세션 ID입니다.
    """
    content: str | None = Field(default=None, deprecated=True)
    """
    하위 호환을 위해 유지되는 본문 필드입니다. 2026년 1월 이후 제공되지 않으므로 `contents`를 사용합니다.
    """
    extra: str | None = None
    """
    카카오가 전달한 부가 정보입니다.
    """
    contents: list[CounselMessageContent] | None = None
    """
    사용자가 전송한 메시지 데이터 배열입니다.
    """
    attachment: CounselMessageAttachment | None = None
    msg_key: str = Field(..., validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다. 발송 결과(`result`)에서는 발송 API 응답의 msgKey와 같고, 수신 6종에서는 이벤트마다 새로 발급된 값이라 발송 건과 대응하지 않습니다.
    재시도로 같은 이벤트가 다시 올 수 있으므로 msgKey 기준으로 멱등 처리합니다.

    """
    user_key: str = Field(..., validation_alias='userKey', serialization_alias='userKey')
    """
    상담톡 사용자 키입니다. 카카오톡 채널별로 다르며 대소문자를 구분하고, 사용자가 탈퇴 후 재가입하면 바뀝니다.
    """
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey')
    """
    메시지를 수신한 발신프로필 키입니다.
    """
    service_type: str = Field(..., validation_alias='serviceType', serialization_alias='serviceType')
    """
    서비스 타입입니다. 문서 예시 값은 `CSTALK`입니다.
    """
    send_time: str = Field(
       default= ...,
        validation_alias='sendTime', serialization_alias='sendTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 이벤트를 수신한 시각입니다.
    """
    report_time: str = Field(
       default= ...,
        validation_alias='reportTime', serialization_alias='reportTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 웹훅을 전송한 시각입니다.
    """


class CounselPersonalInfoWebhookPayload(CounselWebhookCommon):
    """
    개인정보 수신 웹훅(`{고객 Webhook URL}/cstalk/personal_info`) 본문입니다. 사용자가 개인정보 수집에 동의한 뒤 전달됩니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_type: str = Field(..., validation_alias='msgType', serialization_alias='msgType')
    """
    메시지 타입입니다. 문서 예시 값은 `PERSONAL`입니다.
    """
    request_type: str = Field(..., validation_alias='requestType', serialization_alias='requestType')
    """
    요청 타입입니다. 문서 예시 값은 `personal_info`입니다.
    """
    session_id: str | None = Field(default=None, validation_alias='sessionId', serialization_alias='sessionId')
    """
    상담 세션 아이디입니다.
    """
    personal_info: CounselPersonalInfo | None = Field(default=None, validation_alias='personalInfo', serialization_alias='personalInfo')
    msg_key: str = Field(..., validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다. 발송 결과(`result`)에서는 발송 API 응답의 msgKey와 같고, 수신 6종에서는 이벤트마다 새로 발급된 값이라 발송 건과 대응하지 않습니다.
    재시도로 같은 이벤트가 다시 올 수 있으므로 msgKey 기준으로 멱등 처리합니다.

    """
    user_key: str = Field(..., validation_alias='userKey', serialization_alias='userKey')
    """
    상담톡 사용자 키입니다. 카카오톡 채널별로 다르며 대소문자를 구분하고, 사용자가 탈퇴 후 재가입하면 바뀝니다.
    """
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey')
    """
    메시지를 수신한 발신프로필 키입니다.
    """
    service_type: str = Field(..., validation_alias='serviceType', serialization_alias='serviceType')
    """
    서비스 타입입니다. 문서 예시 값은 `CSTALK`입니다.
    """
    send_time: str = Field(
       default= ...,
        validation_alias='sendTime', serialization_alias='sendTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 이벤트를 수신한 시각입니다.
    """
    report_time: str = Field(
       default= ...,
        validation_alias='reportTime', serialization_alias='reportTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 웹훅을 전송한 시각입니다.
    """


class CounselReferenceWebhookPayload(CounselWebhookCommon):
    """
    사용자 메타 정보 수신 웹훅(`{고객 Webhook URL}/cstalk/reference`) 본문입니다. 사용자가 상담 연결을 요청한 시점의 메타 정보가 담깁니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_type: str = Field(..., validation_alias='msgType', serialization_alias='msgType')
    """
    메시지 타입입니다. 문서 예시 값은 `REFERENCE`입니다.
    """
    request_type: str = Field(..., validation_alias='requestType', serialization_alias='requestType')
    """
    요청 타입입니다. 문서 예시 값은 `reference`입니다.
    """
    app_user_id: int | None = Field(default=None, validation_alias='appUserId', serialization_alias='appUserId')
    """
    카카오톡 앱 사용자 ID입니다. 개인 식별자이므로 로그에 남기지 않습니다.
    """
    session_id: str | None = Field(default=None, validation_alias='sessionId', serialization_alias='sessionId')
    """
    상담 세션 아이디입니다. 세션이 생성된 상태에서만 상담원이 메시지를 보낼 수 있습니다.
    """
    reference: CounselReference | None = None
    last_reference: CounselLastReference | None = Field(default=None, validation_alias='lastReference', serialization_alias='lastReference')
    msg_key: str = Field(..., validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다. 발송 결과(`result`)에서는 발송 API 응답의 msgKey와 같고, 수신 6종에서는 이벤트마다 새로 발급된 값이라 발송 건과 대응하지 않습니다.
    재시도로 같은 이벤트가 다시 올 수 있으므로 msgKey 기준으로 멱등 처리합니다.

    """
    user_key: str = Field(..., validation_alias='userKey', serialization_alias='userKey')
    """
    상담톡 사용자 키입니다. 카카오톡 채널별로 다르며 대소문자를 구분하고, 사용자가 탈퇴 후 재가입하면 바뀝니다.
    """
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey')
    """
    메시지를 수신한 발신프로필 키입니다.
    """
    service_type: str = Field(..., validation_alias='serviceType', serialization_alias='serviceType')
    """
    서비스 타입입니다. 문서 예시 값은 `CSTALK`입니다.
    """
    send_time: str = Field(
       default= ...,
        validation_alias='sendTime', serialization_alias='sendTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 이벤트를 수신한 시각입니다.
    """
    report_time: str = Field(
       default= ...,
        validation_alias='reportTime', serialization_alias='reportTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 웹훅을 전송한 시각입니다.
    """


class CounselResultWebhookPayload(CounselWebhookCommon):
    """
    발송 결과 수신 웹훅(`{고객 Webhook URL}/cstalk/result`) 본문입니다. Plain/Rich 발송과 상담 종료 요청의 처리 결과가 전달되며,
    `msgKey`·`ref`로 발송 건과 대조합니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_key: str = Field(..., validation_alias='msgKey', serialization_alias='msgKey')
    """
    발송 API 응답으로 받은 메시지 키입니다.
    """
    request_type: Literal['write', 'end', 'endwithbot'] = Field(
       default= ..., validation_alias='requestType', serialization_alias='requestType'
    )
    """
    요청 타입입니다. `write`(메시지 발송), `end`(상담 종료), `endwithbot`(상담 종료 및 봇 전환) 중 하나입니다.
    """
    report_code: str | None = Field(default=None, validation_alias='reportCode', serialization_alias='reportCode')
    """
    발송 결과 코드입니다. 카카오 응답 코드를 비즈고 코드로 변환한 값이며 `A000`이면 성공입니다.
    """
    report_text: str | None = Field(default=None, validation_alias='reportText', serialization_alias='reportText')
    """
    리포트 메시지입니다.
    """
    kakao_res_created_at: str | None = Field(
        default=None,
        validation_alias='kakaoResCreatedAt', serialization_alias='kakaoResCreatedAt',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    카카오 응답 생성 일시입니다(ISO 8601).
    """
    ref: str | None = None
    """
    발송 요청 시 전달한 참조 필드입니다.
    """
    user_key: str = Field(..., validation_alias='userKey', serialization_alias='userKey')
    """
    상담톡 사용자 키입니다. 카카오톡 채널별로 다르며 대소문자를 구분하고, 사용자가 탈퇴 후 재가입하면 바뀝니다.
    """
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey')
    """
    메시지를 수신한 발신프로필 키입니다.
    """
    service_type: str = Field(..., validation_alias='serviceType', serialization_alias='serviceType')
    """
    서비스 타입입니다. 문서 예시 값은 `CSTALK`입니다.
    """
    send_time: str = Field(
       default= ...,
        validation_alias='sendTime', serialization_alias='sendTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 이벤트를 수신한 시각입니다.
    """
    report_time: str = Field(
       default= ...,
        validation_alias='reportTime', serialization_alias='reportTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 웹훅을 전송한 시각입니다.
    """


class CounselSeenInfoWebhookPayload(CounselWebhookCommon):
    """
    읽음 정보 수신 웹훅(`{고객 Webhook URL}/cstalk/seen_info`) 본문입니다. 상담 세션이 연결된 상태에서만, 발송 후 최대 24시간까지 수신되며
    실시간이 아니라 지연될 수 있습니다. 이 웹훅을 받으려면 카카오 비즈니스 라운지에 별도 문의가 필요합니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_type: str = Field(..., validation_alias='msgType', serialization_alias='msgType')
    """
    메시지 타입입니다. 문서 예시 값은 `SEEN`입니다.
    """
    request_type: str = Field(..., validation_alias='requestType', serialization_alias='requestType')
    """
    요청 타입입니다. 문서 예시 값은 `seen_info`입니다.
    """
    msg_key: str = Field(..., validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다. 발송 결과(`result`)에서는 발송 API 응답의 msgKey와 같고, 수신 6종에서는 이벤트마다 새로 발급된 값이라 발송 건과 대응하지 않습니다.
    재시도로 같은 이벤트가 다시 올 수 있으므로 msgKey 기준으로 멱등 처리합니다.

    """
    user_key: str = Field(..., validation_alias='userKey', serialization_alias='userKey')
    """
    상담톡 사용자 키입니다. 카카오톡 채널별로 다르며 대소문자를 구분하고, 사용자가 탈퇴 후 재가입하면 바뀝니다.
    """
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey')
    """
    메시지를 수신한 발신프로필 키입니다.
    """
    service_type: str = Field(..., validation_alias='serviceType', serialization_alias='serviceType')
    """
    서비스 타입입니다. 문서 예시 값은 `CSTALK`입니다.
    """
    send_time: str = Field(
       default= ...,
        validation_alias='sendTime', serialization_alias='sendTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 이벤트를 수신한 시각입니다.
    """
    report_time: str = Field(
       default= ...,
        validation_alias='reportTime', serialization_alias='reportTime',
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"},
    )
    """
    비즈고가 웹훅을 전송한 시각입니다.
    """


class CounselSendServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_key: str | None = Field(default=None, validation_alias='msgKey', serialization_alias='msgKey')
    """
    메시지 키입니다. 발송 결과 웹훅(`cstalk/result`)의 `msgKey`와 같은 값입니다.
    """


class CounselSessionServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: CounselSessionResult | None = None


class CounselSystemMessage(ResponseModel):
    """
    등록된 시스템 메시지입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: str | None = None
    """
    시스템 메시지 ID입니다.
    """
    name: str | None = None
    """
    시스템 메시지 이름입니다.
    """
    status: str | None = None
    """
    시스템 메시지 상태입니다. 문서 예시 값은 `A`입니다.
    """
    created_at: str | None = Field(
        default=None, validation_alias='createdAt', serialization_alias='createdAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    등록일입니다.
    """
    modified_at: str | None = Field(
        default=None, validation_alias='modifiedAt', serialization_alias='modifiedAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    수정일입니다.
    """
    inspect_status: str | None = Field(default=None, validation_alias='inspectStatus', serialization_alias='inspectStatus')
    """
    검수 상태입니다. 문서 예시 값은 `REG`입니다.
    """
    inspect_request_at: str | None = Field(
        default=None,
        validation_alias='inspectRequestAt', serialization_alias='inspectRequestAt',
        json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'},
    )
    """
    검수 요청일입니다. 값이 없으면 빈 문자열일 수 있습니다.
    """
    inspected_at: str | None = Field(
        default=None, validation_alias='inspectedAt', serialization_alias='inspectedAt', json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'}
    )
    """
    검수일입니다. 값이 없으면 빈 문자열일 수 있습니다.
    """
    messages: list[CounselSystemMessageContent] | None = None
    """
    시스템 메시지 배열입니다.
    """
    comments: list[CounselSystemMessageComment] | None = None
    """
    검수 결과 및 문의 목록입니다.
    """


class CounselSystemMessageCreateResult(ResponseModel):
    """
    시스템 메시지 등록 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    system_message: CounselSystemMessageRef | None = Field(default=None, validation_alias='systemMessage', serialization_alias='systemMessage')


class CounselSystemMessageCreateServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: CounselSystemMessageCreateResult | None = None


class CounselSystemMessageListResult(ResponseModel):
    """
    시스템 메시지 조회 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    system_messages: list[CounselSystemMessage] | None = Field(
        default=None, validation_alias='systemMessages', serialization_alias='systemMessages'
    )
    """
    시스템 메시지 목록입니다.
    """


class CounselSystemMessageListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: CounselSystemMessageListResult | None = None


class FileUploadServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: FileUploadResult | None = None


class InsightKakaoHourlyStatistics(InsightKakaoStatistics):
    """
    카카오(알림톡·브랜드메시지) 시간대별 반응 통계 1건입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    hour: str | None = Field(default=None, examples=['14'])
    """
    집계 시간대(0~23)입니다.
    """


class InsightKakaoHourlyStatisticsResult(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    statistics: list[InsightKakaoHourlyStatistics] | None = None
    """
    시간대별 통계 목록입니다.
    """


class InsightKakaoHourlyStatisticsServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: InsightKakaoHourlyStatisticsResult | None = None


class InsightKakaoStatisticsServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: InsightKakaoStatisticsResult | None = None


class InsightKakaoTemplateStatisticsServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: InsightKakaoTemplateStatisticsResult | None = None


class InsightRcsBrandProfileStatServiceResult(ServiceResult):
    """
    RCS 인사이트 응답은 실제 데이터를 `data.data`가 아니라 `data.rcs`에 담습니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: InsightRcsBrandProfileStatResult | None = None


class InsightRcsMessageButtonStatServiceResult(ServiceResult):
    """
    RCS 인사이트 응답은 실제 데이터를 `data.data`가 아니라 `data.rcs`에 담습니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: InsightRcsMessageButtonStatResult | None = None


class InsightRcsMessageStatServiceResult(ServiceResult):
    """
    RCS 인사이트 응답은 실제 데이터를 `data.data`가 아니라 `data.rcs`에 담습니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: InsightRcsMessageStatResult | None = None


class InsightRcsPersistentMenuStatServiceResult(ServiceResult):
    """
    RCS 인사이트 응답은 실제 데이터를 `data.data`가 아니라 `data.rcs`에 담습니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: InsightRcsPersistentMenuStatResult | None = None


class KakaoCategoryListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: KakaoCategoryListResult | None = None


class KakaoCategoryServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: KakaoCategoryResult | None = None


class KakaoGroupListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: KakaoGroupListResult | None = None


class KakaoSanctionServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: KakaoSanctionResult | None = None


class KakaoSenderAccountServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    result_msg: str | None = Field(default=None, validation_alias='resultMsg', serialization_alias='resultMsg')
    """
    호출 결과 메시지입니다.
    """
    kakao: KakaoSenderProfileResult | None = None


class KakaoSenderListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    result_msg: str | None = Field(default=None, validation_alias='resultMsg', serialization_alias='resultMsg')
    """
    호출 결과 메시지입니다.
    """
    page: int | None = None
    """
    현재 페이지 번호입니다.
    """
    total_page: int | None = Field(default=None, validation_alias='totalPage', serialization_alias='totalPage')
    """
    전체 페이지 수입니다.
    """
    total_count: int | None = Field(default=None, validation_alias='totalCount', serialization_alias='totalCount')
    """
    전체 조회 건수입니다.
    """
    has_next: bool | None = Field(default=None, validation_alias='hasNext', serialization_alias='hasNext')
    """
    다음 페이지 존재 여부입니다.
    """
    channels: list[KakaoSenderChannel] | None = None
    """
    발신프로필 목록입니다.
    """


class KakaoSenderServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: KakaoSenderResult | None = None


class MessageStatisticsServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: MessageStatisticsResult | None = None


class MessageStatusListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: MessageStatusListResult | None = None


class MoMessageListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: MoMessageListResult | None = None


class RcsBrand(ResponseModel):
    """
    RCS 브랜드 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brand_id: str | None = Field(default=None, validation_alias='brandId', serialization_alias='brandId', examples=['BRAND_ID_EXAMPLE'])
    """
    브랜드 ID입니다.
    """
    name: str | None = None
    """
    브랜드 이름입니다.
    """
    brand_key: str | None = Field(
        default=None, validation_alias='brandKey', serialization_alias='brandKey', examples=['RCS_BRAND_KEY'], max_length=200
    )
    """
    브랜드 키입니다(최대 200자).
    """
    register_date: str | None = Field(default=None, validation_alias='registerDate', serialization_alias='registerDate', max_length=30)
    """
    등록일시입니다(최대 30자).
    """
    approval_date: str | None = Field(default=None, validation_alias='approvalDate', serialization_alias='approvalDate')
    """
    승인일시입니다.
    """
    update_date: str | None = Field(default=None, validation_alias='updateDate', serialization_alias='updateDate')
    """
    수정일시입니다.
    """
    status: str | None = Field(default=None, max_length=1300)
    """
    브랜드의 상태입니다(최대 1300자). 문서 예시 값은 `ready`입니다.
    """
    media_url: list[RcsBrandMediaUrl] | None = Field(default=None, validation_alias='mediaUrl', serialization_alias='mediaUrl')
    """
    이미지 파일 ID와 URL 및 사용 유형 정보입니다.
    """
    chatbot_date: str | None = Field(default=None, validation_alias='chatbotDate', serialization_alias='chatbotDate')
    """
    브랜드 내 등록된 대화방 중 가장 최근에 변경된 대화방의 일시입니다.
    """
    logo_date: str | None = Field(default=None, validation_alias='logoDate', serialization_alias='logoDate')
    """
    로고 이미지 중 가장 최근에 변경된 일시입니다.
    """
    messagebase_date: str | None = Field(default=None, validation_alias='messagebaseDate', serialization_alias='messagebaseDate')
    """
    브랜드 내 등록된 템플릿 중 가장 최근에 변경된 템플릿의 일시입니다.
    """
    description: str | None = None
    """
    브랜드 설명에 등록된 내용입니다.
    """
    tel: str | None = None
    """
    브랜드 홈에 노출될 전화번호입니다.
    """
    menus: list[RcsBrandMenu] | None = None
    """
    메뉴입니다.
    """
    category_id: dict[str, Any] | None = Field(default=None, validation_alias='categoryId', serialization_alias='categoryId')
    """
    브랜드 카테고리 ID입니다.
    """
    category_name: list[dict[str, Any]] | None = Field(default=None, validation_alias='categoryName', serialization_alias='categoryName')
    """
    브랜드 카테고리명입니다.
    """
    sub_category_id: dict[str, Any] | None = Field(default=None, validation_alias='subCategoryId', serialization_alias='subCategoryId')
    """
    브랜드 하위 카테고리 ID입니다.
    """
    sub_category_name: dict[str, Any] | None = Field(default=None, validation_alias='subCategoryName', serialization_alias='subCategoryName')
    """
    브랜드 하위 카테고리명입니다.
    """
    category_opt: dict[str, Any] | None = Field(default=None, validation_alias='categoryOpt', serialization_alias='categoryOpt')
    """
    검색용 키워드입니다.
    """
    zip_code: list[dict[str, Any]] | None = Field(default=None, validation_alias='zipCode', serialization_alias='zipCode')
    """
    브랜드 홈에 표시될 우편번호입니다.
    """
    road_address: str | None = Field(default=None, validation_alias='roadAddress', serialization_alias='roadAddress')
    """
    브랜드 홈에 표시되는 도로명주소입니다.
    """
    detail_address: str | None = Field(default=None, validation_alias='detailAddress', serialization_alias='detailAddress')
    """
    브랜드 홈에 표시되는 상세주소입니다.
    """
    email: str | None = None
    """
    브랜드 홈에 표시되는 이메일 주소입니다.
    """
    web_site_url: str | None = Field(default=None, validation_alias='webSiteUrl', serialization_alias='webSiteUrl')
    """
    브랜드 홈에 표시되는 홈페이지 주소입니다.
    """
    approval_reason: str | None = Field(default=None, validation_alias='approvalReason', serialization_alias='approvalReason')
    """
    검수 시 반려 사유입니다.
    """
    brand_feed_url: str | None = Field(default=None, validation_alias='brandFeedUrl', serialization_alias='brandFeedUrl')
    """
    브랜드 소식 URL입니다.
    """
    init_tab: str | None = Field(default=None, validation_alias='initTab', serialization_alias='initTab')
    """
    단말에 표시되는 브랜드 홈의 기본 탭입니다. 알려진 값은 `FEED`입니다.
    """
    init_feed_items: str | None = Field(default=None, validation_alias='initFeedItems', serialization_alias='initFeedItems')
    """
    `initTab`이 `FEED`인 경우 소식 탭에 표시할 메뉴입니다.
    """
    template_color: str | None = Field(default=None, validation_alias='templateColor', serialization_alias='templateColor')
    """
    브랜드 내 등록되는 템플릿의 버튼 컬러 값입니다.
    """
    biz_info_yn: str | None = Field(default=None, validation_alias='bizInfoYn', serialization_alias='bizInfoYn')
    """
    브랜드 소식 탭에 운영정보를 사용할지 여부입니다(`Y`/`N`).
    """
    biz_info_title: str | None = Field(default=None, validation_alias='bizInfoTitle', serialization_alias='bizInfoTitle')
    """
    `bizInfoYn`이 `Y`인 경우 운영정보 제목입니다.
    """
    biz_info_content: str | None = Field(default=None, validation_alias='bizInfoContent', serialization_alias='bizInfoContent')
    """
    `bizInfoYn`이 `Y`인 경우 운영정보 내용입니다.
    """
    safty_status_yn: str | None = Field(default=None, validation_alias='saftyStatusYn', serialization_alias='saftyStatusYn')
    """
    안심마크 지정 기업 여부입니다. 필드명은 문서 표기(`safty`)를 따릅니다.
    """


class RcsBrandResult(ResponseModel):
    """
    브랜드 조회·수정 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: RcsBrand | None = None


class RcsBrandServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: RcsBrandResult | None = None


class RcsChatbotServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: RcsChatbotResult | None = None


class RcsFileUploadServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: RcsFileUploadResult | None = None


class Rcs1(ResponseModel):
    """
    RCS 응답 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    pagination: RcsMessagebasePagination | None = None
    message_forms: list[RcsMessagebaseCommonSummary] | None = Field(
        default=None, validation_alias='messageForms', serialization_alias='messageForms'
    )
    """
    공통 포맷 목록입니다.
    """


class RcsMessagebaseCommonListResult(ResponseModel):
    """
    공통 포맷 목록 조회 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: Rcs1 | None = None
    """
    RCS 응답 정보입니다.
    """


class RcsMessagebaseCommonListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: RcsMessagebaseCommonListResult | None = None


class Rcs3(ResponseModel):
    """
    RCS 응답 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    pagination: RcsMessagebasePagination | None = None
    message_forms: list[RcsMessagebaseFormSummary] | None = Field(
        default=None, validation_alias='messageForms', serialization_alias='messageForms'
    )
    """
    템플릿 양식 목록입니다.
    """


class RcsMessagebaseFormListResult(ResponseModel):
    """
    템플릿 양식 목록 조회 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: Rcs3 | None = None
    """
    RCS 응답 정보입니다.
    """


class RcsMessagebaseFormListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: RcsMessagebaseFormListResult | None = None


class RcsTemplate(ResponseModel):
    """
    RCS 템플릿 상세 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    status: str | None = None
    """
    템플릿 상태입니다.
    """
    approval_result: str | None = Field(default=None, validation_alias='approvalResult', serialization_alias='approvalResult')
    """
    승인 결과입니다.
    """
    approval_reason: str | None = Field(default=None, validation_alias='approvalReason', serialization_alias='approvalReason')
    """
    승인 사유입니다.
    """
    register_date: str | None = Field(default=None, validation_alias='registerDate', serialization_alias='registerDate')
    """
    등록일시입니다.
    """
    approval_date: str | None = Field(default=None, validation_alias='approvalDate', serialization_alias='approvalDate')
    """
    승인일시입니다.
    """
    update_date: str | None = Field(default=None, validation_alias='updateDate', serialization_alias='updateDate')
    """
    수정일시입니다.
    """
    register_id: str | None = Field(default=None, validation_alias='registerId', serialization_alias='registerId')
    """
    등록 계정 ID입니다.
    """
    update_id: str | None = Field(default=None, validation_alias='updateId', serialization_alias='updateId')
    """
    수정 계정 ID입니다.
    """
    product_code: str | None = Field(default=None, validation_alias='productCode', serialization_alias='productCode')
    """
    상품 코드입니다. 문서 예시 값은 `lms`입니다.
    """
    spec: str | None = None
    """
    템플릿 스펙입니다. 문서 예시 값은 `openrichcard`입니다.
    """
    card_type: str | None = Field(default=None, validation_alias='cardType', serialization_alias='cardType')
    """
    카드 종류입니다. 문서 예시 값은 `descriptionNew`입니다.
    """
    body: RcsTemplateDetailBody | None = None
    brand_key: str | None = Field(default=None, validation_alias='brandKey', serialization_alias='brandKey', examples=['RCS_BRAND_KEY'])
    """
    브랜드 키입니다.
    """
    format_id: str | None = Field(default=None, validation_alias='formatId', serialization_alias='formatId')
    """
    템플릿 양식 ID입니다. 발송 시에는 이 값을 `formatId` 필드에 넣습니다(영문 문서 기준).
    """


class RcsTemplateAction(ResponseModel):
    """
    템플릿 버튼 액션 객체입니다. 발송용 `RcsSuggestion`과 달리 `displayText`가 `action` 안에 있고,
    클립보드 복사 액션(`clipboardAction`)을 쓸 수 있습니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    display_text: str = Field(..., validation_alias='displayText', serialization_alias='displayText')
    """
    버튼 표시 텍스트입니다.
    """
    clipboard_action: RcsTemplateClipboardAction | None = Field(
        default=None, validation_alias='clipboardAction', serialization_alias='clipboardAction'
    )
    url_action: RcsUrlAction | None = Field(default=None, validation_alias='urlAction', serialization_alias='urlAction')
    dialer_action: RcsDialerAction | None = Field(default=None, validation_alias='dialerAction', serialization_alias='dialerAction')
    map_action: RcsTemplateMapAction | None = Field(default=None, validation_alias='mapAction', serialization_alias='mapAction')
    calendar_action: RcsCalendarAction | None = Field(default=None, validation_alias='calendarAction', serialization_alias='calendarAction')
    compose_action: RcsTemplateComposeAction | None = Field(default=None, validation_alias='composeAction', serialization_alias='composeAction')


class RcsTemplateFormLogoListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: RcsTemplateFormLogoListResult | None = None


class RcsTemplateIdServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: RcsTemplateIdResult | None = None


class RcsTemplateImageServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: RcsTemplateImageResult | None = None


class Rcs7(ResponseModel):
    """
    RCS 응답 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    pagination: RcsMessagebasePagination | None = None
    templates: list[RcsTemplateSummary] | None = None
    """
    템플릿 목록입니다.
    """


class RcsTemplateListResult(ResponseModel):
    """
    RCS 템플릿 목록 조회 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: Rcs7 | None = None
    """
    RCS 응답 정보입니다.
    """


class RcsTemplateListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: RcsTemplateListResult | None = None


class RcsTemplateResult(ResponseModel):
    """
    RCS 템플릿 상세 조회 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: RcsTemplate | None = None


class RcsTemplateServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: RcsTemplateResult | None = None


class RcsTemplateSuggestion(ResponseModel):
    """
    템플릿 버튼 액션 정의(버튼 1개)입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    action: RcsTemplateAction | None = None


class ReportInquiryServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: ReportInquiryResult | None = None


class ReportPollingServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: ReportPollingResult | None = None


class ReservationCreateServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    resv_key: str | None = Field(default=None, validation_alias='resvKey', serialization_alias='resvKey', examples=['RESV_KEY_EXAMPLE'])
    """
    예약 발송 키입니다. 예약 조회·수정·취소·중지·재개·수신자 관리에 씁니다. `data.data`가 아니라 `data` 바로 아래에 있습니다.
    """
    data: SendOmniResult | None = None


class ReservationListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: ReservationListResult | None = None


class ReservationRecipientCreateServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: SendOmniResult | None = None


class ReservationRecipientListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: ReservationRecipientListResult | None = None


class ReservationServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: Reservation | None = None


class SendOmniServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: SendOmniResult | None = None


class AlimtalkAttachment(ResponseModel):
    """
    알림톡 첨부 정보(버튼, 아이템, 아이템 하이라이트)입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    button: list[AlimtalkButton] | None = None
    """
    버튼 정보입니다.
    """
    item: AlimtalkItem | None = None
    item_highlight: AlimtalkItemHighlight | None = Field(default=None, validation_alias='itemHighlight', serialization_alias='itemHighlight')


class AlimtalkTemplate(ResponseModel):
    """
    조회·등록·수정 응답의 알림톡 템플릿 정보입니다. 응답에는 요청 필드 외에 검수 상태, 차단·휴면 여부, 심사 의견 등이 더해집니다.
    응답에 따라 일부 필드만 올 수 있습니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str | None = Field(
        default=None, validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE']
    )
    """
    발신프로필 키입니다.
    """
    sender_key_type: Literal['G', 'S'] | None = Field(default=None, validation_alias='senderKeyType', serialization_alias='senderKeyType')
    """
    발신프로필 키 타입입니다. 기본값은 `S`입니다.
    - `G`: 그룹
    - `S`: 발신프로필

    """
    template_name: str | None = Field(default=None, validation_alias='templateName', serialization_alias='templateName')
    """
    템플릿 이름입니다.
    """
    template_code: str | None = Field(
        default=None, validation_alias='templateCode', serialization_alias='templateCode', examples=['TEMPLATE_CODE_EXAMPLE']
    )
    """
    템플릿 코드입니다.
    """
    msg_type: str | None = Field(default=None, validation_alias='msgType', serialization_alias='msgType', examples=['AT'])
    """
    이 템플릿으로 발송할 때 쓰는 카카오 비즈메시지 타입입니다(`AT` 텍스트형, `AI` 이미지형).
    전문 발송의 `AlimtalkMessage.msgType`에 그대로 넣습니다. 필드 표에는 없지만 응답에 옵니다(2026-09-28 sandbox 확인).

    """
    template_message_type: str | None = Field(default=None, validation_alias='templateMessageType', serialization_alias='templateMessageType')
    """
    템플릿 메시지 타입입니다. 문서 예시 값은 `BA`입니다.
    """
    template_emphasize_type: str | None = Field(default=None, validation_alias='templateEmphasizeType', serialization_alias='templateEmphasizeType')
    """
    템플릿 강조 타입입니다. 문서 예시 값은 `NONE`입니다.
    """
    text: str | None = None
    """
    템플릿 본문입니다.
    """
    title: str | None = None
    """
    강조표기형 템플릿 제목입니다.
    """
    sub_title: str | None = Field(default=None, validation_alias='subTitle', serialization_alias='subTitle')
    """
    강조 표기 보조 문구입니다.
    """
    header: str | None = None
    """
    메시지 상단에 표시할 제목입니다.
    """
    img_name: str | None = Field(default=None, validation_alias='imgName', serialization_alias='imgName')
    """
    이미지 이름입니다.
    """
    img_url: str | None = Field(default=None, validation_alias='imgUrl', serialization_alias='imgUrl')
    """
    이미지 URL입니다.
    """
    link: AlimtalkLink | None = None
    attachment: AlimtalkAttachment | None = None
    supplement: AlimtalkSupplement | None = None
    category_code: str | None = Field(default=None, validation_alias='categoryCode', serialization_alias='categoryCode')
    """
    템플릿 카테고리 코드입니다.
    """
    security_flag: bool | None = Field(default=None, validation_alias='securityFlag', serialization_alias='securityFlag')
    """
    보안 템플릿 여부입니다.
    """
    adult_flag: bool | None = Field(default=None, validation_alias='adultFlag', serialization_alias='adultFlag')
    """
    연령 인증 설정 여부입니다.
    """
    preview_message: str | None = Field(default=None, validation_alias='previewMessage', serialization_alias='previewMessage')
    """
    템플릿 미리보기 메시지입니다.
    """
    extra: str | None = None
    """
    부가 정보입니다.
    """
    inspection_status: Literal['REG', 'REQ', 'APR', 'REJ'] | None = Field(
        default=None, validation_alias='inspectionStatus', serialization_alias='inspectionStatus'
    )
    """
    검수 상태입니다.
    - `REG`: 등록
    - `REQ`: 검수 요청
    - `APR`: 승인
    - `REJ`: 반려

    """
    status: str | None = None
    """
    템플릿 상태입니다. 목록 조회·최근 변경 템플릿 조회 응답에 있습니다.
    """
    block: str | None = None
    """
    템플릿 차단 여부입니다. `true` 또는 `false` 문자열입니다.
    """
    dormant: str | None = None
    """
    템플릿 휴면 여부입니다. `true` 또는 `false` 문자열입니다.
    """
    created_at: str | None = Field(default=None, validation_alias='createdAt', serialization_alias='createdAt')
    """
    생성일입니다.
    """
    modified_at: str | None = Field(default=None, validation_alias='modifiedAt', serialization_alias='modifiedAt')
    """
    수정일입니다.
    """
    comments: list[AlimtalkTemplateComment] | None = None
    """
    템플릿 심사 의견 목록입니다.
    """


class AlimtalkTemplateCategoryResponse(ResponseModel):
    """
    알림톡 템플릿 카테고리 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: AlimtalkTemplateCategoryServiceResult | None = None


class AlimtalkTemplateImageUploadResponse(ResponseModel):
    """
    알림톡 템플릿 이미지 업로드 응답입니다. MMS 업로드(`FileUploadResponse`)와 달리 `fileKey`가 아닌 `imgUrl`, `fileName`을 돌려줍니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: AlimtalkTemplateImageUploadServiceResult | None = None


class Alimtalk(ResponseModel):
    """
    알림톡 템플릿 결과 영역입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    templates: list[AlimtalkTemplate] | None = None
    """
    조회한 템플릿 목록입니다.
    """


class AlimtalkTemplateListResult(ResponseModel):
    """
    템플릿 목록 조회·최근 변경 템플릿 조회 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    alimtalk: Alimtalk | None = None
    """
    알림톡 템플릿 결과 영역입니다.
    """


class AlimtalkTemplateListServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: AlimtalkTemplateListResult | None = None


class AlimtalkTemplatePublicListResponse(ResponseModel):
    """
    공용템플릿 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: AlimtalkTemplatePublicListServiceResult | None = None


class AlimtalkTemplateResult(ResponseModel):
    """
    템플릿 조회·등록·수정 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    alimtalk: AlimtalkTemplate | None = None


class AlimtalkTemplateServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: AlimtalkTemplateResult | None = None


class BrandMessageAttachment(ResponseModel):
    """
    브랜드메시지 첨부 정보(버튼, 이미지, 와이드 아이템, 쿠폰, 커머스, 동영상, 카탈로그)입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    button: list[BrandMessageButton] | None = Field(default=None, max_length=5)
    """
    버튼 목록입니다. 최대 5개이며, FT/FI 타입에 쿠폰을 함께 쓰면 최대 4개입니다.
    """
    image: BrandMessageImage | None = None
    item: BrandMessageItem | None = None
    coupon: BrandMessageCoupon | None = None
    commerce: BrandMessageCommerce | None = None
    video: BrandMessageVideo | None = None
    catalog: BrandMessageCatalog | None = None


class BrandMessageAudienceEstimateResponse(ResponseModel):
    """
    동보 발송 예상 소요시간 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageAudienceEstimateServiceResult | None = None


class BrandMessageAudienceFriendCountResponse(ResponseModel):
    """
    채널 전체 친구 수 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageAudienceFriendCountServiceResult | None = None


class BrandMessageAudiencePossibleResponse(ResponseModel):
    """
    발송 예상 모수 확인 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageAudiencePossibleServiceResult | None = None


class BrandMessageCarouselItem(ResponseModel):
    """
    캐러셀 아이템 1개입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    header: str | None = Field(default=None, max_length=20)
    """
    캐러셀 아이템 제목입니다. FC 타입에서 필수, FA 타입에서는 사용할 수 없습니다. 줄바꿈 불가, 최대 20자입니다.
    """
    message: str | None = Field(default=None, max_length=180)
    """
    캐러셀 아이템 본문입니다. FC 타입에서 필수, FA 타입에서는 사용할 수 없습니다. 줄바꿈 최대 2회, 최대 180자입니다.
    """
    additional_content: str | None = Field(
        default=None, validation_alias='additionalContent', serialization_alias='additionalContent', max_length=34
    )
    """
    부가 정보입니다. FA 타입에서는 사용할 수 없습니다. 줄바꿈 최대 1회, 최대 34자입니다.
    """
    attachment: BrandMessageCarouselItemAttachment | None = None


class BrandMessageFileUploadResponse(ResponseModel):
    """
    브랜드메시지 이미지 업로드 응답입니다. MMS 업로드(`FileUploadResponse`)와 달리 `fileKey`가 아닌 `imgUrl`을 돌려줍니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageFileUploadServiceResult | None = None


class BrandMessageFriendGroupFileUploadResponse(ResponseModel):
    """
    친구 그룹 파일 업로드 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageFriendGroupFileUploadServiceResult | None = None


class BrandMessageFriendGroupListResponse(ResponseModel):
    """
    친구 그룹 목록 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageFriendGroupListServiceResult | None = None


class BrandMessageFriendGroupPhoneNumberRequestListResponse(ResponseModel):
    """
    친구 그룹 전화번호 요청 목록 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageFriendGroupPhoneNumberRequestListServiceResult | None = None


class BrandMessageFriendGroupPhoneNumberRequestResponse(ResponseModel):
    """
    친구 그룹 전화번호 요청 단건 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageFriendGroupPhoneNumberRequestServiceResult | None = None


class BrandMessageFriendGroupProcessingResponse(ResponseModel):
    """
    친구 그룹 등록·전화번호 추가·삭제 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageFriendGroupProcessingServiceResult | None = None


class BrandMessageFriendGroupResponse(ResponseModel):
    """
    친구 그룹 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageFriendGroupServiceResult | None = None


class BrandMessageGroupSendResponse(ResponseModel):
    """
    동보 발송 생성·제어·조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageGroupSendServiceResult | None = None


class BrandMessageGroupTagListResponse(ResponseModel):
    """
    그룹태그 조회·등록·수정 응답입니다. 단건 조회도 `groupTags` 배열로 돌려줍니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageGroupTagListServiceResult | None = None


class BrandMessageMarketingAgreeResponse(ResponseModel):
    """
    증적자료 파일 업로드 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageMarketingAgreeServiceResult | None = None


class BrandMessageTemplateListResponse(ResponseModel):
    """
    브랜드메시지 템플릿 목록·최근 변경 템플릿 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageTemplateListServiceResult | None = None


class BrandMessageVideoInfoResponse(ResponseModel):
    """
    기존 동영상 등록·동영상 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageVideoInfoServiceResult | None = None


class BrandMessageVideoListResponse(ResponseModel):
    """
    동영상 목록 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageVideoListServiceResult | None = None


class BrandMessageVideoUploadRegisterResponse(ResponseModel):
    """
    동영상 업로드 등록 응답입니다. `A000`은 업로드 채널 발급 성공만 뜻하며, 사용 가능 여부는 동영상 조회의 `status`로 확인합니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageVideoUploadRegisterServiceResult | None = None


class CounselCertStatusResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: CounselCertStatusServiceResult | None = None


class CounselConsultTimeResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: CounselConsultTimeServiceResult | None = None


class CounselEndResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: CounselEndServiceResult | None = None


class CounselFileUploadResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: CounselFileUploadServiceResult | None = None


class CounselImageUploadResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: CounselImageUploadServiceResult | None = None


class CounselSendResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: CounselSendServiceResult | None = None


class CounselSessionResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: CounselSessionServiceResult | None = None


class CounselSystemMessageCreateResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: CounselSystemMessageCreateServiceResult | None = None


class CounselSystemMessageListResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: CounselSystemMessageListServiceResult | None = None


class FileUploadResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: FileUploadServiceResult | None = None


class InsightKakaoHourlyStatisticsResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: InsightKakaoHourlyStatisticsServiceResult | None = None


class InsightKakaoStatisticsResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: InsightKakaoStatisticsServiceResult | None = None


class InsightKakaoTemplateStatisticsResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: InsightKakaoTemplateStatisticsServiceResult | None = None


class InsightRcsBrandProfileStatResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: InsightRcsBrandProfileStatServiceResult | None = None


class InsightRcsMessageButtonStatResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: InsightRcsMessageButtonStatServiceResult | None = None


class InsightRcsMessageStatResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: InsightRcsMessageStatServiceResult | None = None


class InsightRcsPersistentMenuStatResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: InsightRcsPersistentMenuStatServiceResult | None = None


class KakaoCategoryListResponse(ResponseModel):
    """
    발신프로필 카테고리 전체조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: KakaoCategoryListServiceResult | None = None


class KakaoCategoryResponse(ResponseModel):
    """
    발신프로필 카테고리 상세조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: KakaoCategoryServiceResult | None = None


class KakaoGroupListResponse(ResponseModel):
    """
    발신프로필 그룹 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: KakaoGroupListServiceResult | None = None


class KakaoSanctionResponse(ResponseModel):
    """
    제재 조회(발신프로필 제재, 그룹템플릿 발신프로필 제외, 템플릿 제재) 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: KakaoSanctionServiceResult | None = None


class KakaoSenderAccountResponse(ResponseModel):
    """
    카카오 채널 인증 토큰 요청, 발신프로필 등록, uuid·senderKey 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: KakaoSenderAccountServiceResult | None = None


class KakaoSenderListResponse(ResponseModel):
    """
    발신프로필 목록 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: KakaoSenderListServiceResult | None = None


class KakaoSenderResponse(ResponseModel):
    """
    발신프로필 키로 조회 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: KakaoSenderServiceResult | None = None


class MessageStatisticsResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: MessageStatisticsServiceResult | None = None


class MessageStatusListResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: MessageStatusListServiceResult | None = None


class MoMessageListResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: MoMessageListServiceResult | None = None


class RcsBrandResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: RcsBrandServiceResult | None = None


class RcsChatbotResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: RcsChatbotServiceResult | None = None


class RcsFileUploadResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: RcsFileUploadServiceResult | None = None


class RcsMessagebaseCommonListResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: RcsMessagebaseCommonListServiceResult | None = None


class RcsMessagebaseFormListResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: RcsMessagebaseFormListServiceResult | None = None


class RcsTemplateButton(ResponseModel):
    """
    템플릿 버튼 정의입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    suggestions: list[RcsTemplateSuggestion] | None = None
    """
    버튼 액션 목록입니다.
    """


class RcsTemplateFormLogoListResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: RcsTemplateFormLogoListServiceResult | None = None


class RcsTemplateIdResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: RcsTemplateIdServiceResult | None = None


class RcsTemplateImageResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: RcsTemplateImageServiceResult | None = None


class RcsTemplateListResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: RcsTemplateListServiceResult | None = None


class RcsTemplateResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: RcsTemplateServiceResult | None = None


class ReportInquiryResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: ReportInquiryServiceResult | None = None


class ReportPollingResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: ReportPollingServiceResult | None = None


class ReservationCreateResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: ReservationCreateServiceResult | None = None


class ReservationListResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: ReservationListServiceResult | None = None


class ReservationRecipientCreateResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: ReservationRecipientCreateServiceResult | None = None


class ReservationRecipientListResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: ReservationRecipientListServiceResult | None = None


class ReservationResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: ReservationServiceResult | None = None


class SendOmniResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: SendOmniServiceResult | None = None


class AlimtalkTemplateListResponse(ResponseModel):
    """
    알림톡 템플릿 목록 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: AlimtalkTemplateListServiceResult | None = None


class AlimtalkTemplateResponse(ResponseModel):
    """
    알림톡 템플릿 조회·등록·수정 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: AlimtalkTemplateServiceResult | None = None


class BrandMessageCarousel(ResponseModel):
    """
    브랜드메시지 캐러셀 객체입니다(FC 캐러셀 피드, FA 캐러셀 커머스).
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    head: BrandMessageCarouselHead | None = None
    list_: list[BrandMessageCarouselItem] | None = Field(
        default=None, validation_alias='list', serialization_alias='list', max_length=10, min_length=2
    )
    """
    캐러셀 아이템 목록입니다. 최소 2개, 최대 10개입니다.
    """
    tail: BrandMessageCarouselTail | None = None


class BrandMessageTemplate(ResponseModel):
    """
    브랜드메시지 템플릿 상세 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str | None = Field(default=None, validation_alias='senderKey', serialization_alias='senderKey')
    """
    발신프로필 키입니다.
    """
    send_type: str | None = Field(default=None, validation_alias='sendType', serialization_alias='sendType')
    """
    브랜드메시지 발송 타입입니다(`basic`, `free`).
    """
    template_code: str | None = Field(default=None, validation_alias='templateCode', serialization_alias='templateCode')
    """
    템플릿 코드입니다.
    """
    msg_type: str | None = Field(default=None, validation_alias='msgType', serialization_alias='msgType')
    """
    브랜드메시지 메시지 타입입니다.
    """
    text: str | None = None
    """
    템플릿 본문입니다.
    """
    carousel: BrandMessageCarousel | None = None
    """
    캐러셀 정보입니다.
    """
    attachment: BrandMessageAttachment | None = None
    """
    첨부 정보입니다.
    """
    header: str | None = None
    """
    헤더 정보입니다.
    """
    additional_content: str | None = Field(default=None, validation_alias='additionalContent', serialization_alias='additionalContent')
    """
    부가 정보입니다.
    """
    push_alarm: Literal['Y', 'N'] | None = Field(default=None, validation_alias='pushAlarm', serialization_alias='pushAlarm')
    """
    메시지 푸시 알림 발송 여부입니다.
    """
    message_variable: dict[str, Any] | None = Field(default=None, validation_alias='messageVariable', serialization_alias='messageVariable')
    """
    메시지 영역 변수입니다.
    """
    button_variable: dict[str, Any] | None = Field(default=None, validation_alias='buttonVariable', serialization_alias='buttonVariable')
    """
    버튼 영역 변수입니다.
    """
    coupon_variable: dict[str, Any] | None = Field(default=None, validation_alias='couponVariable', serialization_alias='couponVariable')
    """
    쿠폰 영역 변수입니다.
    """
    image_variable: dict[str, Any] | None = Field(default=None, validation_alias='imageVariable', serialization_alias='imageVariable')
    """
    이미지 영역 변수입니다.
    """
    video_variable: dict[str, Any] | None = Field(default=None, validation_alias='videoVariable', serialization_alias='videoVariable')
    """
    비디오 영역 변수입니다.
    """
    commerce_variable: dict[str, Any] | None = Field(default=None, validation_alias='commerceVariable', serialization_alias='commerceVariable')
    """
    커머스 영역 변수입니다.
    """
    carousel_variable: list[BrandMessageCarouselVariable] | None = Field(
        default=None, validation_alias='carouselVariable', serialization_alias='carouselVariable'
    )
    """
    캐러셀 영역 변수입니다.
    """
    create_at: str | None = Field(
        default=None,
        validation_alias='createAt', serialization_alias='createAt',
        examples=['2026-04-24T10:42:34+09:00'],
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ssXXX"},
    )
    """
    등록일(`yyyy-MM-dd'T'HH:mm:ssXXX`)입니다.
    """
    modified_at: str | None = Field(
        default=None,
        validation_alias='modifiedAt', serialization_alias='modifiedAt',
        examples=['2026-04-24T10:42:34+09:00'],
        json_schema_extra={'x-format': "yyyy-MM-dd'T'HH:mm:ssXXX"},
    )
    """
    수정일(`yyyy-MM-dd'T'HH:mm:ssXXX`)입니다.
    """
    status: str | None = Field(default=None, examples=['A'])
    """
    템플릿 상태입니다. 알려진 값: `A`(등록), `S`(차단).
    """


class BrandMessageTemplateResult(ResponseModel):
    """
    템플릿 응답 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brandmessage: BrandMessageTemplate | None = None
    """
    브랜드메시지 템플릿 정보입니다.
    """


class BrandMessageTemplateServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: BrandMessageTemplateResult | None = None


class RcsMessagebaseFormDetail(ResponseModel):
    """
    공통 포맷 또는 템플릿 양식의 상세 정보입니다. 공통 포맷 상세 조회는 모든 필드를,
    템플릿 양식 상세 조회는 그중 일부(formatId, templateName, body, buttons, agencyId, brandId,
    messagebaseformId, policyInfo.maxButtonCount/maxMediaSize, registerDate, updateDate, productCode, spec, cardType)를 문서화합니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    format_id: str | None = Field(default=None, validation_alias='formatId', serialization_alias='formatId')
    """
    템플릿 포맷 ID입니다.
    """
    template_name: str | None = Field(default=None, validation_alias='templateName', serialization_alias='templateName')
    """
    템플릿 등록 시 입력된 템플릿 명칭입니다.
    """
    body: list[RcsTemplateBodyParam] | None = None
    """
    body 정의입니다.
    """
    buttons: RcsTemplateButton | None = None
    agency_id: str | None = Field(default=None, validation_alias='agencyId', serialization_alias='agencyId')
    """
    대행사 ID입니다.
    """
    brand_id: str | None = Field(default=None, validation_alias='brandId', serialization_alias='brandId')
    """
    브랜드 ID입니다.
    """
    messagebaseform_id: str | None = Field(default=None, validation_alias='messagebaseformId', serialization_alias='messagebaseformId')
    """
    템플릿의 원형인 템플릿 양식 ID입니다.
    """
    policy_info: RcsMessagebasePolicyInfo | None = Field(default=None, validation_alias='policyInfo', serialization_alias='policyInfo')
    status: str | None = None
    """
    템플릿의 상태입니다.
    """
    approval_result: str | None = Field(default=None, validation_alias='approvalResult', serialization_alias='approvalResult')
    """
    템플릿의 승인 상태입니다.
    """
    register_date: str | None = Field(default=None, validation_alias='registerDate', serialization_alias='registerDate')
    """
    템플릿 등록일시입니다.
    """
    approval_date: str | None = Field(default=None, validation_alias='approvalDate', serialization_alias='approvalDate')
    """
    템플릿 승인일시입니다.
    """
    update_date: str | None = Field(default=None, validation_alias='updateDate', serialization_alias='updateDate')
    """
    템플릿 수정일시입니다.
    """
    update_id: str | None = Field(default=None, validation_alias='updateId', serialization_alias='updateId')
    """
    템플릿 수정 계정 ID입니다.
    """
    product_code: str | None = Field(default=None, validation_alias='productCode', serialization_alias='productCode')
    """
    메시지 상품 종류입니다.
    """
    spec: str | None = None
    """
    레이아웃 구조입니다.
    """
    card_type: str | None = Field(default=None, validation_alias='cardType', serialization_alias='cardType')
    """
    카드 종류입니다.
    """


class Rcs2(ResponseModel):
    """
    RCS 응답 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    message_form: RcsMessagebaseFormDetail | None = Field(default=None, validation_alias='messageForm', serialization_alias='messageForm')


class RcsMessagebaseFormDetailResult(ResponseModel):
    """
    공통 포맷·템플릿 양식 상세 조회 결과 데이터입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: Rcs2 | None = None
    """
    RCS 응답 정보입니다.
    """


class RcsMessagebaseFormDetailServiceResult(ServiceResult):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    data: RcsMessagebaseFormDetailResult | None = None


class BrandMessageTemplateResponse(ResponseModel):
    """
    브랜드메시지 템플릿 조회·등록·수정 응답입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: BrandMessageTemplateServiceResult | None = None


class RcsMessagebaseFormDetailResponse(ResponseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    common: CommonResult | None = None
    data: RcsMessagebaseFormDetailServiceResult | None = None


InsightRcsMenuClick.model_rebuild()

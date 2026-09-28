"""Generated from spec/openapi.yaml by scripts/generate_models.py. Do not edit."""

from __future__ import annotations

from typing import Annotated, Any, Literal, Union

from bizgo._base import RequestModel
from pydantic import ConfigDict, Discriminator, Field, Tag


class AlimtalkButton(RequestModel):
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


class AlimtalkItemHighlight(RequestModel):
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


class AlimtalkItemListEntry(RequestModel):
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


class AlimtalkItemSummary(RequestModel):
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


class AlimtalkLink(RequestModel):
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


class AlimtalkQuickReply(RequestModel):
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


class AlimtalkSupplement(RequestModel):
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


class Alimtalk(RequestModel):
    """
    검수 요청 취소 대상 템플릿 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    template_code: str = Field(
       default= ..., validation_alias='templateCode', serialization_alias='templateCode', examples=['TEMPLATE_CODE_EXAMPLE']
    )
    """
    템플릿 코드입니다.
    """


class AlimtalkTemplateInspectionCancelRequest(RequestModel):
    """
    알림톡 템플릿 검수 요청 취소 본문입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    alimtalk: Alimtalk
    """
    검수 요청 취소 대상 템플릿 정보입니다.
    """


class Alimtalk1(RequestModel):
    """
    검수 요청할 알림톡 템플릿 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    sender_key_type: Literal['G', 'S'] | None = Field(default='S', validation_alias='senderKeyType', serialization_alias='senderKeyType')
    """
    발신프로필 키 타입입니다. 기본값은 `S`입니다.
    - `G`: 그룹
    - `S`: 발신프로필

    """
    template_code: str = Field(
       default= ..., validation_alias='templateCode', serialization_alias='templateCode', examples=['TEMPLATE_CODE_EXAMPLE']
    )
    """
    템플릿 코드입니다.
    """
    comment: str | None = None
    """
    검수 의견 또는 문의 사항입니다.
    """


class AlimtalkTemplateInspectionRequest(RequestModel):
    """
    알림톡 템플릿 검수 요청 본문(JSON)입니다. 템플릿 상태가 대기이고 검수 상태가 등록(`REG`)일 때 요청할 수 있습니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    alimtalk: Alimtalk1
    """
    검수 요청할 알림톡 템플릿 정보입니다.
    """


class BrandMessageAudiencePossibleByPhoneNumbersRequest(RequestModel):
    """
    전화번호 명단 기반 발송 예상 모수 확인 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    phone_numbers: list[str] = Field(..., validation_alias='phoneNumbers', serialization_alias='phoneNumbers', min_length=10)
    """
    발송 가능 여부를 확인할 전화번호 목록입니다. 최소 10건이며, 하나라도 형식이 잘못되면 요청 전체가 거부됩니다. 국가코드는 자동 정규화됩니다(010 / +82 / 82 → 82).
    """


class BrandMessageButton(RequestModel):
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


class BrandMessageCarouselHead(RequestModel):
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


class BrandMessageCarouselTail(RequestModel):
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


class BrandMessageCarouselVariable(RequestModel):
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


class BrandMessageCatalogItem(RequestModel):
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


class BrandMessageCatalogVariable(RequestModel):
    """
    기본형 변수 분리 방식에서 카탈로그(FG) 아이템 1개에 대한 변수입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    message_variable: dict[str, Any] | None = Field(default=None, validation_alias='messageVariable', serialization_alias='messageVariable')
    """
    아이템 `title`·`description`의 변수입니다.
    """
    commerce_variable: dict[str, Any] | None = Field(default=None, validation_alias='commerceVariable', serialization_alias='commerceVariable')
    """
    가격 관련 변수입니다.
    """
    image_variable: dict[str, Any] | None = Field(default=None, validation_alias='imageVariable', serialization_alias='imageVariable')
    """
    아이템 `imgUrl`·`imgLink`의 변수입니다.
    """


class BrandMessageCommerce(RequestModel):
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


class BrandMessageCoupon(RequestModel):
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


class FriendGroup(RequestModel):
    """
    친구 그룹 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    friend_group_key: str = Field(
       default= ...,
        validation_alias='friendGroupKey', serialization_alias='friendGroupKey',
        examples=['FRIEND_GROUP_KEY_EXAMPLE'],
        max_length=50,
        min_length=1,
    )
    """
    친구 그룹 키입니다. 1~50자이며 한글·영문·숫자와 일부 특수문자를 쓸 수 있습니다.
    """
    file_key: str | None = Field(default=None, validation_alias='fileKey', serialization_alias='fileKey', examples=['FILE_KEY_001'])
    """
    친구 그룹 파일 업로드로 발급받은 임시 파일 키입니다.
    """
    phone_numbers: list[str] | None = Field(
        default=None, validation_alias='phoneNumbers', serialization_alias='phoneNumbers', max_length=10000, min_length=1
    )
    """
    전화번호 목록입니다. 1~10,000건입니다.
    """


class BrandMessageFriendGroupRequest(RequestModel):
    """
    친구 그룹 등록, 전화번호 추가·삭제 요청입니다. 전화번호는 `fileKey` 또는 `phoneNumbers`로 전달합니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    friend_group: FriendGroup = Field(..., validation_alias='friendGroup', serialization_alias='friendGroup')
    """
    친구 그룹 정보입니다.
    """


class Brandmessage(RequestModel):
    """
    동보 발송 제어 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    request_id: str = Field(..., validation_alias='requestId', serialization_alias='requestId', examples=['1203981'])
    """
    동보 발송 요청 아이디입니다. 동보 발송 응답의 `requestId`를 씁니다.
    """


class BrandMessageGroupSendControlRequest(RequestModel):
    """
    동보 발송 제어(재개·중지·종료) 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brandmessage: Brandmessage
    """
    동보 발송 제어 정보입니다.
    """


class Brandmessage1(RequestModel):
    """
    기본형 템플릿 동보 발송 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    template_code: str = Field(
       default= ..., validation_alias='templateCode', serialization_alias='templateCode', examples=['TEMPLATE_CODE_EXAMPLE']
    )
    """
    기본형 템플릿 코드입니다. 변수가 없고 상태가 등록(`A`)인 템플릿이어야 합니다.
    """
    friend_group_key: str | None = Field(
        default=None, validation_alias='friendGroupKey', serialization_alias='friendGroupKey', examples=['FRIEND_GROUP_KEY_EXAMPLE']
    )
    """
    친구 그룹 등록으로 발급받은 키입니다. 생략하면 전체 친구를 대상으로 합니다. 친구 그룹을 쓰면 그룹 상태가 완료이고 등록 유저 수(`userCount`)가 10 이상이어야 합니다.
    """
    send_start_at: str = Field(
       default= ...,
        validation_alias='sendStartAt', serialization_alias='sendStartAt',
        examples=['2026-04-08 16:40:00'],
        json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'},
    )
    """
    동보 발송 시작 일시(`yyyy-MM-dd HH:mm:ss`, KST)입니다. 요청 시점으로부터 10분 이후, 08:00~20:50 범위로 설정합니다. 20:50~익일 08:00에는 자동 중지 후 익일 08:00 이후 자동 재개됩니다.
    """
    campaign_id: str | None = Field(
        default=None, validation_alias='campaignId', serialization_alias='campaignId', examples=['CAMPAIGN_ID_EXAMPLE']
    )
    """
    고객 캠페인 식별자입니다. 동일 캠페인의 중복 발송을 방지하는 데 사용합니다.
    """
    tps_limit: int | None = Field(default=None, validation_alias='tpsLimit', serialization_alias='tpsLimit', examples=[500])
    """
    초당 발송 건수 상한입니다.
    """
    push_alarm: Literal['Y', 'N'] | None = Field(default='Y', validation_alias='pushAlarm', serialization_alias='pushAlarm')
    """
    메시지 푸시 알림 발송 여부입니다. 기본값은 `Y`입니다.
    """
    origin_cid: str | None = Field(default=None, validation_alias='originCID', serialization_alias='originCID', max_length=9)
    """
    최초 발신사업자 식별코드입니다. 재판매사·특수부가통신사업자는 필수입니다. 최대 9자입니다.
    """


class BrandMessageGroupSendCreateRequest(RequestModel):
    """
    브랜드메시지 기본형 템플릿 동보 발송 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brandmessage: Brandmessage1
    """
    기본형 템플릿 동보 발송 정보입니다.
    """
    payment_code: str | None = Field(default=None, validation_alias='paymentCode', serialization_alias='paymentCode', max_length=20)
    """
    정산용 부서 코드입니다. 최대 20자입니다.
    """


class GroupTag(RequestModel):
    """
    브랜드메시지 그룹태그 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    group_tag_key: str = Field(
       default= ..., validation_alias='groupTagKey', serialization_alias='groupTagKey', examples=['GROUP_TAG_KEY_EXAMPLE']
    )
    """
    그룹태그 키입니다.
    """
    group_tag_name: str = Field(..., validation_alias='groupTagName', serialization_alias='groupTagName', examples=['VIP 고객'])
    """
    그룹태그 이름입니다.
    """


class BrandMessageGroupTagRequest(RequestModel):
    """
    그룹태그 등록·수정 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    group_tag: GroupTag = Field(..., validation_alias='groupTag', serialization_alias='groupTag')
    """
    브랜드메시지 그룹태그 정보입니다.
    """


class BrandMessageImage(RequestModel):
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


class BrandMessageItemListEntry(RequestModel):
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


class BrandMessage1(RequestModel):
    """
    발송 권한 신청 정보입니다. 다른 브랜드메시지 API와 달리 키 이름이 `brandMessage`(대문자 M)입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(
       default= ..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'], max_length=40
    )
    """
    발신프로필 키입니다. 최대 40자입니다.
    """


class BrandMessagePermissionApplyRequest(RequestModel):
    """
    브랜드메시지 발송권한(고객사 회원 대상 발송, targeting M·N·O) 신청 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brand_message: BrandMessage1 = Field(..., validation_alias='brandMessage', serialization_alias='brandMessage')
    """
    발송 권한 신청 정보입니다. 다른 브랜드메시지 API와 달리 키 이름이 `brandMessage`(대문자 M)입니다.
    """


class Brandmessage2(RequestModel):
    """
    무료수신거부 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    unsubscribe_phone_number: str = Field(
       default= ..., validation_alias='unsubscribePhoneNumber', serialization_alias='unsubscribePhoneNumber', examples=['080-0000-0000']
    )
    """
    무료수신거부 전화번호입니다.
    """
    unsubscribe_auth_number: str | None = Field(
        default=None, validation_alias='unsubscribeAuthNumber', serialization_alias='unsubscribeAuthNumber', examples=['12345']
    )
    """
    무료수신거부 인증번호입니다.
    """


class BrandMessageUnsubscribeContentRequest(RequestModel):
    """
    발신프로필 무료수신거부 정보 입력 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brandmessage: Brandmessage2
    """
    무료수신거부 정보입니다.
    """


class BrandMessageVideo(RequestModel):
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


class BrandMessageVideoRegisterRequest(RequestModel):
    """
    기존 동영상 등록 요청입니다. 카카오톡 채널에 이미 올라가 있는 `PUBLIC` 또는 `PRIVATE` 상태의 동영상을 재업로드 없이 등록합니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(
       default= ..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'], max_length=40
    )
    """
    발신프로필 키입니다. 최대 40자입니다.
    """
    vid: str | None = Field(default=None, examples=['VID_EXAMPLE'])
    """
    등록할 동영상 식별자입니다. `videoUrl`과 함께 사용할 수 없습니다.
    """
    video_url: str | None = Field(default=None, validation_alias='videoUrl', serialization_alias='videoUrl')
    """
    등록할 채널 동영상 URL입니다. 형식: `https://business.kakao.com/{채널식별자}/videos/{vid}`. `vid`와 함께 사용할 수 없습니다.
    """


class BrandMessageVideoUploadRegisterRequest(RequestModel):
    """
    동영상 업로드 등록(업로드 채널 발급) 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(
       default= ..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'], max_length=40
    )
    """
    발신프로필 키입니다. 최대 40자입니다.
    """
    file_name: str = Field(..., validation_alias='fileName', serialization_alias='fileName', examples=['brand-promotion.mp4'])
    """
    업로드할 동영상 파일 이름입니다.
    """
    file_size: int = Field(..., validation_alias='fileSize', serialization_alias='fileSize', examples=[4075447])
    """
    업로드할 동영상 파일 크기(byte)입니다.
    """


class CounselButton(RequestModel):
    """
    상담톡 Rich 메시지·캐러셀 버튼입니다. 버튼 타입에 따라 필요한 필드가 다릅니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    type: str = Field(..., examples=['WL'])
    """
    카카오 버튼 타입 코드입니다. 문서에 나온 값은 `WL`(웹 링크, 예시)과 `BF`(비즈폼)입니다.
    """
    name: str
    """
    버튼명입니다.
    """
    url_mobile: str | None = Field(default=None, validation_alias='urlMobile', serialization_alias='urlMobile')
    """
    모바일 환경에서 버튼 클릭 시 이동할 URL입니다.
    """
    url_pc: str | None = Field(default=None, validation_alias='urlPc', serialization_alias='urlPc')
    """
    PC 환경에서 버튼 클릭 시 이동할 URL입니다.
    """
    scheme_ios: str | None = Field(default=None, validation_alias='schemeIos', serialization_alias='schemeIos')
    """
    iOS 환경에서 버튼 클릭 시 실행할 application custom scheme입니다.
    """
    scheme_android: str | None = Field(default=None, validation_alias='schemeAndroid', serialization_alias='schemeAndroid')
    """
    Android 환경에서 버튼 클릭 시 실행할 application custom scheme입니다.
    """
    url_target: str | None = Field(default=None, validation_alias='urlTarget', serialization_alias='urlTarget')
    """
    WL 타입에서 외부 브라우저로 열려면 `out`을 입력합니다.
    """
    extra: str | None = None
    """
    봇/상담톡 전환 시 전달할 메타 정보입니다.
    """
    chat_event: str | None = Field(default=None, validation_alias='chatEvent', serialization_alias='chatEvent')
    """
    봇/상담톡 전환 시 연결할 이벤트명입니다.
    """
    start_type: str | None = Field(default=None, validation_alias='startType', serialization_alias='startType')
    """
    상담 시작 타입입니다.
    """
    biz_form_key: str | None = Field(default=None, validation_alias='bizFormKey', serialization_alias='bizFormKey')
    """
    비즈폼 키입니다. BF 타입에서 사용합니다.
    """


class CounselCarouselTail(RequestModel):
    """
    캐러셀 더보기 버튼 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    url_mobile: str = Field(..., validation_alias='urlMobile', serialization_alias='urlMobile')
    """
    모바일 환경에서 버튼 클릭 시 이동할 URL입니다.
    """
    url_pc: str | None = Field(default=None, validation_alias='urlPc', serialization_alias='urlPc')
    """
    PC 환경에서 버튼 클릭 시 이동할 URL입니다.
    """
    scheme_ios: str | None = Field(default=None, validation_alias='schemeIos', serialization_alias='schemeIos')
    """
    iOS 환경에서 버튼 클릭 시 실행할 커스텀 스킴입니다.
    """
    scheme_android: str | None = Field(default=None, validation_alias='schemeAndroid', serialization_alias='schemeAndroid')
    """
    Android 환경에서 버튼 클릭 시 실행할 커스텀 스킴입니다.
    """


class CounselCoupon(RequestModel):
    """
    메시지(또는 캐러셀 아이템) 최하단에 노출되는 쿠폰 요소입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    title: str
    """
    쿠폰 이름입니다. 문서상 정해진 5가지 형식 중 하나여야 합니다.
    """
    description: str = Field(..., max_length=18)
    """
    쿠폰 상세 설명입니다. WIDE, WIDE_ITEM_LIST 타입은 최대 18자, 그 외 타입은 최대 12자입니다(캐러셀 쿠폰 설명에는 PREMIUM_VIDEO도 18자로 적혀 있습니다).
    """
    url_pc: str | None = Field(default=None, validation_alias='urlPc', serialization_alias='urlPc')
    """
    PC 환경에서 쿠폰 클릭 시 이동할 URL입니다.
    """
    url_mobile: str | None = Field(default=None, validation_alias='urlMobile', serialization_alias='urlMobile')
    """
    모바일 환경에서 쿠폰 클릭 시 이동할 URL입니다.
    """
    scheme_ios: str | None = Field(default=None, validation_alias='schemeIos', serialization_alias='schemeIos')
    """
    iOS 환경에서 쿠폰 클릭 시 실행할 커스텀 스킴입니다.
    """
    scheme_android: str | None = Field(default=None, validation_alias='schemeAndroid', serialization_alias='schemeAndroid')
    """
    Android 환경에서 쿠폰 클릭 시 실행할 커스텀 스킴입니다.
    """


class CounselEndRequest(RequestModel):
    """
    상담 종료 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    user_key: str = Field(
       default= ..., validation_alias='userKey', serialization_alias='userKey', examples=['USER_KEY_EXAMPLE'], max_length=20, min_length=1
    )
    """
    상담톡 사용자 키입니다. 1~20자입니다.
    """
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """


class CounselEndWithBotRequest(RequestModel):
    """
    상담 종료 및 봇 전환 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    user_key: str = Field(
       default= ..., validation_alias='userKey', serialization_alias='userKey', examples=['USER_KEY_EXAMPLE'], max_length=20, min_length=1
    )
    """
    상담톡 사용자 키입니다. 1~20자입니다.
    """
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    bot_event: str | None = Field(default=None, validation_alias='botEvent', serialization_alias='botEvent')
    """
    상담 종료 후 실행할 봇 이벤트(말블록)명입니다.
    """


class CounselFile(RequestModel):
    """
    상담톡 파일 첨부 정보입니다(VIDEO·AUDIO·FILE 타입).
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    file_url: str = Field(..., validation_alias='fileUrl', serialization_alias='fileUrl')
    """
    상담톡 파일 업로드 API(`/api/comm/v1/file/cstalk`)로 등록한 파일 URL입니다.
    """
    file_name: str | None = Field(default=None, validation_alias='fileName', serialization_alias='fileName')
    """
    파일명입니다. `msgType`이 `FILE`이면 필수입니다(`CounselPlainMessageRequest`의 `x-sdk-required-if`).
    """
    file_size: str | None = Field(default=None, validation_alias='fileSize', serialization_alias='fileSize')
    """
    파일 크기입니다. `msgType`이 `FILE`이면 필수입니다(`CounselPlainMessageRequest`의 `x-sdk-required-if`). 문서상 타입은 문자열입니다.
    """


class CounselImage(RequestModel):
    """
    상담톡 이미지 요소입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    img_url: str = Field(..., validation_alias='imgUrl', serialization_alias='imgUrl')
    """
    상담톡 이미지 업로드 API(`/api/comm/v1/file/cstalk/image`)로 등록한 이미지 URL입니다.
    """
    img_link: str | None = Field(default=None, validation_alias='imgLink', serialization_alias='imgLink')
    """
    이미지 클릭 시 이동할 URL입니다. 설정하지 않으면 카카오톡 내 이미지 뷰어를 사용합니다.
    """


class CounselItemHighlight(RequestModel):
    """
    ITEM_LIST 타입의 아이템 하이라이트 영역입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    title: str | None = None
    """
    하이라이트 제목입니다.
    """
    description: str
    """
    하이라이트 추가 설명입니다.
    """
    img_url: str | None = Field(default=None, validation_alias='imgUrl', serialization_alias='imgUrl')
    """
    하이라이트 이미지 URL입니다.
    """


class CounselItemListEntry(RequestModel):
    """
    아이템 리스트의 아이템 1개입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    title: str
    """
    아이템 제목입니다.
    """
    description: str | None = None
    """
    ITEM_LIST 타입의 아이템 추가 설명입니다.
    """


class CounselItemSummary(RequestModel):
    """
    ITEM_LIST 타입의 아이템 요약 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    title: str | None = None
    """
    요약 정보 제목입니다.
    """
    description: str | None = None
    """
    요약 정보 추가 설명입니다.
    """


class CounselMessageDeleteTarget(RequestModel):
    """
    삭제할 상담톡 메시지입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다. 호출자 소유가 아니면 `A502`로 거부됩니다.
    """
    user_key: str = Field(
       default= ..., validation_alias='userKey', serialization_alias='userKey', examples=['USER_KEY_EXAMPLE'], max_length=20, min_length=1
    )
    """
    메시지를 받은 사용자 키입니다.
    """
    msg_key: str = Field(..., validation_alias='msgKey', serialization_alias='msgKey')
    """
    삭제할 메시지의 발송 시 msgKey입니다.
    """


class CounselPlainAttachment(RequestModel):
    """
    Plain 메시지 첨부 객체입니다. IMAGE는 `image`, VIDEO·AUDIO·FILE은 `file`을 사용합니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    image: CounselImage | None = None
    file: CounselFile | None = None


class CounselPlainMessageRequest(RequestModel):
    """
    상담톡 Plain 메시지 발송 요청입니다. 상담 세션이 열려 있는 사용자에게만 보낼 수 있습니다.
    본문(`message`)과 첨부는 최종 사용자와의 상담 내용이므로 개인정보로 취급하고 로그에 남기지 않습니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    user_key: str = Field(
       default= ..., validation_alias='userKey', serialization_alias='userKey', examples=['USER_KEY_EXAMPLE'], max_length=20, min_length=1
    )
    """
    상담톡 사용자 키입니다. 카카오톡 채널별로 다르며 대소문자를 구분합니다. 1~20자이며 비어 있거나 20자를 넘으면 `A507`이 반환됩니다.
    """
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    msg_type: Literal['TEXT', 'IMAGE', 'VIDEO', 'AUDIO', 'FILE'] = Field(
       default= ..., validation_alias='msgType', serialization_alias='msgType'
    )
    """
    메시지 타입입니다. IMAGE는 `attachment.image`, VIDEO·AUDIO·FILE은 `attachment.file`을 사용합니다.
    """
    message: str = Field(..., max_length=1000)
    """
    사용자에게 전달할 메시지입니다. 최대 1,000자입니다.
    """
    attachment: CounselPlainAttachment | None = None
    ref: str | None = Field(default=None, max_length=200)
    """
    참조 필드입니다. 최대 200자이며 발송 결과 웹훅(`cstalk/result`)에서 함께 반환됩니다.
    """


class CounselQuickReply(RequestModel):
    """
    상담톡 바로연결입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    type: str
    """
    카카오 바로연결 타입 코드입니다.
    """
    name: str = Field(..., max_length=14)
    """
    바로연결 제목입니다. 최대 14자입니다.
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
    url_target: str | None = Field(default=None, validation_alias='urlTarget', serialization_alias='urlTarget')
    """
    외부 브라우저로 열려면 `out`을 입력합니다.
    """
    extra: str | None = None
    """
    BK 버튼 발송 또는 상담톡/챗봇 전환 시 전달할 메타 정보입니다.
    """
    chat_event: str | None = Field(default=None, validation_alias='chatEvent', serialization_alias='chatEvent')
    """
    봇 전환 시 연결할 봇 이벤트명입니다.
    """


class CounselSenderActivation(RequestModel):
    """
    상담톡 이용 활성화·비활성화 대상입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    committal_company: str | None = Field(default=None, validation_alias='committalCompany', serialization_alias='committalCompany')
    """
    위탁사명입니다. 사전에 등록된 경우 생략할 수 있습니다.
    """


class CounselSenderActivationRequest(RequestModel):
    """
    상담톡 이용 활성화·비활성화 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    cstalk: CounselSenderActivation


class CounselSenderRef(RequestModel):
    """
    대상 발신프로필입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """


class CounselSenderRequest(RequestModel):
    """
    발신프로필 키만 담는 상담톡 요청입니다(채팅 기능 활성화·비활성화, 시스템 메시지 검수 요청·취소).
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    cstalk: CounselSenderRef


class CounselSystemMessageButton(RequestModel):
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


class CounselSystemMessageContent(RequestModel):
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


class CounselSystemMessageDraft(RequestModel):
    """
    등록할 시스템 메시지입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    name: str
    """
    시스템 메시지 이름입니다.
    """
    messages: list[CounselSystemMessageContent]
    """
    시스템 메시지 배열입니다.
    """


class CounselUserTarget(RequestModel):
    """
    대상 발신프로필과 사용자입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    user_key: str = Field(
       default= ..., validation_alias='userKey', serialization_alias='userKey', examples=['USER_KEY_EXAMPLE'], max_length=20, min_length=1
    )
    """
    대상 사용자 키입니다. 1~20자입니다.
    """


class CounselWeekTime(RequestModel):
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


class Destination(RequestModel):
    """
    수신자 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    to: str = Field(..., examples=['01000000000'])
    """
    수신번호입니다. 휴대폰 번호는 11자리 형식을 씁니다(국제메시지는 채널 규격 참고).
    """
    replace_words: dict[str, str] | None = Field(
        default=None, validation_alias='replaceWords', serialization_alias='replaceWords', examples=[{'name': '홍길동'}]
    )
    """
    치환메시지 변수입니다. 본문·제목의 `#{key}`를 이 값으로 바꿉니다. 알림톡·브랜드메시지 템플릿 자동 치환 발송(`sendType`이 `template`)에서는 필수입니다(각 채널 스키마의 `x-sdk-required-if`).
    """
    ref: str | None = None
    """
    수신자별 참조 필드입니다. 값이 있으면 이 수신번호에는 요청 단위 `ref` 대신 이 값이 리포트에 담깁니다.
    """


class InternationalMessage(RequestModel):
    """
    국제메시지(해외 수신자 대상 문자)입니다. `messageFlow[].international` 객체로 보냅니다.
    본문은 UTF-8을 지원하며, 실제 단말 전달 여부와 무관하게 접수 기준으로 과금됩니다.

    수신번호 규칙(`destinations[].to`): 국가번호를 포함한 E.164 형식에서 `+`를 뺀 숫자로 입력합니다
    (예: `821000000000`, 길이 8~15자리). 국가번호 목록이나 국가별 길이·세그먼트(분할) 규칙은 원문에 없습니다.

    국제문자에서는 `title`, `fileKey`를 쓸 수 없습니다(접수코드 A321).

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    from_: str = Field(..., validation_alias='from', serialization_alias='from', examples=['01000000000'])
    """
    발신번호입니다.
    """
    text: str = Field(
       default= ...,
        examples=['Your verification code is 000000.'],
        json_schema_extra={'x-charset': 'UTF-8'},
        max_length=1000,
    )
    """
    국제메시지 본문입니다. 최대 1,000자이며 UTF-8로 인코딩됩니다(글자 수 기준, 바이트 제한 아님).
    """
    ttl: str | None = '86400'
    """
    메시지 유효 시간(초)입니다. 생략하면 86400(24시간)입니다.
    """
    client_sub_id: str | None = Field(
        default=None, validation_alias='clientSubId', serialization_alias='clientSubId', examples=['sender-id-01'], max_length=20
    )
    """
    Sender ID, 메시지 서명을 복수로 지정하기 위한 구분자입니다. 최대 20자입니다.
    """


class KakaoGroupSenderAddRequest(RequestModel):
    """
    그룹에 발신프로필 등록 요청 본문입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    group_key: str = Field(..., validation_alias='groupKey', serialization_alias='groupKey', examples=['GROUP_KEY_EXAMPLE'])
    """
    발신프로필을 등록할 그룹 키입니다.
    """
    sender_key: str = Field(
       default= ..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'], max_length=40
    )
    """
    등록할 발신프로필 키입니다. 최대 40자입니다.
    """
    group_name: str | None = Field(default=None, validation_alias='groupName', serialization_alias='groupName')
    """
    그룹 이름입니다.
    """


class KakaoSenderCreateRequest(RequestModel):
    """
    인증 토큰으로 발신프로필을 등록하는 요청 본문입니다. 인증 토큰과 관리자 전화번호는 헤더(`token`, `phoneNumber`)로 보냅니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    yellow_id: str = Field(
       default= ..., validation_alias='yellowId', serialization_alias='yellowId', examples=['@KAKAO_CHANNEL_ID_EXAMPLE']
    )
    """
    등록할 카카오톡 채널 아이디입니다.
    """
    category_code: str = Field(
       default= ..., validation_alias='categoryCode', serialization_alias='categoryCode', examples=['00000000001'], pattern='^[0-9]{11}$'
    )
    """
    발신프로필 카테고리 코드(11자리 숫자)입니다. 사용할 수 있는 코드는 카테고리 전체조회로 확인합니다.
    """
    unsubscribe_phone_number: str | None = Field(default=None, validation_alias='unsubscribePhoneNumber', serialization_alias='unsubscribePhoneNumber')
    """
    무료수신거부 전화번호입니다(예 `080-0000-0000`). 브랜드메시지를 쓰는 발신프로필이 설정하며, 타겟팅 M, N, O 사용 시 필수입니다.
    """
    unsubscribe_auth_number: str | None = Field(default=None, validation_alias='unsubscribeAuthNumber', serialization_alias='unsubscribeAuthNumber')
    """
    무료수신거부 인증번호입니다(예 `12345`). 타겟팅 M, N, O 사용 시 필수입니다.
    """


class KakaoSenderRecoverRequest(RequestModel):
    """
    발신프로필 휴면 해제 요청 본문입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    휴면 해제할 발신프로필 키입니다.
    """


class KakaoSenderTokenRequest(RequestModel):
    """
    카카오 채널 인증 토큰 요청 본문입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    yellow_id: str = Field(
       default= ..., validation_alias='yellowId', serialization_alias='yellowId', examples=['@KAKAO_CHANNEL_ID_EXAMPLE']
    )
    """
    카카오톡 채널 아이디입니다(`@`로 시작).
    """
    phone_number: str = Field(..., validation_alias='phoneNumber', serialization_alias='phoneNumber', examples=['01000000000'])
    """
    카카오톡 채널 알림을 받는 관리자 전화번호입니다. 이 번호에 연결된 카카오톡이 채널을 차단하지 않았으면 인증 토큰이 발송됩니다.
    """


class MmsMessage(RequestModel):
    """
    LMS(장문) 또는 MMS(이미지+장문) 메시지입니다. `fileKey`가 있으면 MMS, 없으면 LMS로 발송됩니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    from_: str = Field(..., validation_alias='from', serialization_alias='from', examples=['01000000000'])
    """
    발신번호입니다. 비즈고에 미리 등록한 번호여야 합니다.
    """
    title: str | None = None
    """
    제목입니다.
    """
    text: str = Field(
       default= ..., json_schema_extra={'x-max-bytes': 2000, 'x-charset': 'EUC-KR'}
    )
    """
    본문입니다. 최대 2,000byte이며, 이통사 규격상 EUC-KR 범위 밖 문자는 접수 오류가 날 수 있습니다.
    """
    file_key: list[str] | None = Field(
        default=None, validation_alias='fileKey', serialization_alias='fileKey', examples=[['FILE_KEY_001']], max_length=3, min_length=1
    )
    """
    이미지 업로드(`POST /api/comm/v1/file/mms`)로 받은 파일 키입니다. MMS 발송 시 필수이며 최대 3개입니다. 이미지 순서는 보장되지 않습니다.
    """
    ttl: str | None = Field(default=None, pattern='^[0-9]+$')
    """
    이통사 전달까지 유효한 최대 시간(초)입니다. 시간이 지나면 실패 처리됩니다.
    """
    origin_cid: str | None = Field(default=None, validation_alias='originCID', serialization_alias='originCID')
    """
    최초 발신사업자 식별코드(9자리)입니다. 일반 고객은 입력하지 않습니다.
    """


class NaverTalkButton(RequestModel):
    """
    네이버 톡톡 버튼입니다.
    - `WEB_LINK` 버튼은 `mobileUrl`이 필수입니다(접수코드 A606).
    - `APP_LINK` 버튼은 `aOsAppScheme`과 `iOsAppScheme`이 모두 필수입니다(접수코드 A607).

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    button_code: str = Field(..., validation_alias='buttonCode', serialization_alias='buttonCode', examples=['WEB_LINK'])
    """
    버튼 코드입니다. 알려진 값은 `WEB_LINK`, `APP_LINK`입니다(요청 예시와 접수코드 A605~A607 기준). 전체 목록은 원문에 없습니다.
    """
    mobile_url: str | None = Field(
        default=None, validation_alias='mobileUrl', serialization_alias='mobileUrl', examples=['https://m.example.com']
    )
    """
    모바일 이동 URL입니다.
    """
    pc_url: str | None = Field(default=None, validation_alias='pcUrl', serialization_alias='pcUrl', examples=['https://example.com'])
    """
    PC 이동 URL입니다.
    """
    a_os_app_scheme: str | None = Field(default=None, validation_alias='aOsAppScheme', serialization_alias='aOsAppScheme')
    """
    Android OS 환경에서 버튼 클릭 시 이동할 앱 링크입니다.
    """
    i_os_app_scheme: str | None = Field(default=None, validation_alias='iOsAppScheme', serialization_alias='iOsAppScheme')
    """
    iOS 환경에서 버튼 클릭 시 이동할 앱 링크입니다.
    """


class NaverTalkGift(RequestModel):
    """
    네이버 톡톡 쿠폰 정보 객체입니다(접수코드 A608).
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    code: str
    """
    쿠폰 코드입니다.
    """
    image_url: str = Field(..., validation_alias='imageUrl', serialization_alias='imageUrl')
    """
    쿠폰 이미지 URL입니다. 쿠폰을 첨부하면 반드시 필요합니다(리포트 코드 72106).
    """
    end_date: str = Field(
       default= ...,
        validation_alias='endDate', serialization_alias='endDate',
        json_schema_extra={'x-format': 'YYYY-MM-DD'},
        pattern='^[0-9]{4}-[0-9]{2}-[0-9]{2}$',
    )
    """
    쿠폰 종료일입니다. 오늘 이후 날짜를 `YYYY-MM-DD` 형식으로 입력합니다(리포트 코드 72107).
    """
    name: str | None = None
    """
    쿠폰 이름입니다. 생략하면 템플릿에 등록된 이름으로 발송됩니다.
    """
    publisher: str | None = None
    """
    쿠폰 발급자입니다.
    """
    coupon_description: str | None = Field(default=None, validation_alias='couponDescription', serialization_alias='couponDescription')
    """
    쿠폰 설명입니다.
    """
    label: str | None = None
    """
    쿠폰 라벨입니다.
    """
    value: str | None = None
    """
    쿠폰 내용입니다.
    """


class RcsBody(RequestModel):
    """
    RCS 메시지 본문입니다. 입력할 수 있는 항목은 `formatId`로 지정한 포맷에 따라 다릅니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    title: str | None = None
    """
    메시지 제목입니다.
    """
    description: str | None = None
    """
    메시지 본문입니다.
    """
    media: str | None = Field(default=None, examples=['maapfile://MEDIA_KEY_EXAMPLE'])
    """
    이미지입니다. 필드 설명은 "이미지 URL"이지만, 이미지 업로드(`POST /api/comm/v1/file/rcs`)
    응답의 `data.data.media` 값(미디어 키)을 넣도록 안내합니다.

    """


class RcsBrandMediaUrl(RequestModel):
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


class RcsBrandMenu(RequestModel):
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


class CreateCalendarEvent(RequestModel):
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


class RcsCalendarAction(RequestModel):
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


class RcsChatbot(RequestModel):
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


class ComposeTextMessage(RequestModel):
    """
    문자 보내기 객체입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    phone_number: str = Field(..., validation_alias='phoneNumber', serialization_alias='phoneNumber', examples=['01000000000'])
    """
    전화 번호입니다.
    """
    text: str | None = None
    """
    문자(SMS/LMS/MMS) 내용입니다.
    """


class ComposeRecordingMessage(RequestModel):
    """
    영상/음성 보내기 객체입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    phone_number: str = Field(..., validation_alias='phoneNumber', serialization_alias='phoneNumber', examples=['01000000000'])
    """
    전화 번호입니다.
    """
    type: Literal['VIDEO', 'AUDIO']
    """
    영상(`VIDEO`) 또는 음성(`AUDIO`)입니다.
    """


class RcsComposeAction(RequestModel):
    """
    문자 보내기 또는 영상/음성 보내기 액션입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    compose_text_message: ComposeTextMessage = Field(..., validation_alias='composeTextMessage', serialization_alias='composeTextMessage')
    """
    문자 보내기 객체입니다.
    """
    compose_recording_message: ComposeRecordingMessage | None = Field(
        default=None, validation_alias='composeRecordingMessage', serialization_alias='composeRecordingMessage'
    )
    """
    영상/음성 보내기 객체입니다.
    """


class DialPhoneNumber(RequestModel):
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


class RcsDialerAction(RequestModel):
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


class RcsLocation(RequestModel):
    """
    지도 위치입니다.
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
    label: float | None = None
    """
    라벨입니다.
    """
    query: str
    """
    검색 내용입니다.
    """


class ShowLocation(RequestModel):
    """
    지도 위치 표시 객체입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    location: RcsLocation
    fallback_url: str | None = Field(default=None, validation_alias='fallbackUrl', serialization_alias='fallbackUrl')
    """
    위치 조회 실패 시 이동할 fallback URL입니다.
    """


class RcsMapAction(RequestModel):
    """
    지도 검색·보여주기·위치 전송 액션입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    show_location: ShowLocation = Field(..., validation_alias='showLocation', serialization_alias='showLocation')
    """
    지도 위치 표시 객체입니다.
    """
    request_location_push: dict[str, Any] | None = Field(
        default=None, validation_alias='requestLocationPush', serialization_alias='requestLocationPush'
    )
    """
    위치 전송 요청 객체입니다.
    """


class RcsTemplateBodyParam(RequestModel):
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


class CopyToClipboard(RequestModel):
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


class RcsTemplateClipboardAction(RequestModel):
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


class ComposeTextMessage1(RequestModel):
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


class ComposeRecordingMessage1(RequestModel):
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


class RcsTemplateComposeAction(RequestModel):
    """
    템플릿 버튼의 문자/음성/영상 보내기 액션입니다. 발송용 `RcsComposeAction`과 달리 `composeTextMessage`가 선택입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    compose_text_message: ComposeTextMessage1 | None = Field(
        default=None, validation_alias='composeTextMessage', serialization_alias='composeTextMessage'
    )
    """
    문자 보내기 객체입니다.
    """
    compose_recording_message: ComposeRecordingMessage1 | None = Field(
        default=None, validation_alias='composeRecordingMessage', serialization_alias='composeRecordingMessage'
    )
    """
    음성/영상 보내기 객체입니다.
    """


class Location(RequestModel):
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


class ShowLocation1(RequestModel):
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


class RcsTemplateMapAction(RequestModel):
    """
    템플릿 버튼의 지도 액션입니다. 발송용 `RcsMapAction`과 달리 `showLocation`이 선택이고
    `fallbackUrl`이 `mapAction` 바로 아래에 있으며, 위치 `label`이 문자열입니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    show_location: ShowLocation1 | None = Field(default=None, validation_alias='showLocation', serialization_alias='showLocation')
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


class OpenUrl(RequestModel):
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


class RcsUrlAction(RequestModel):
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


class ReservationRecipientCreateRequest(RequestModel):
    """
    예약 수신자 추가 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    destinations: list[Destination] = Field(..., max_length=1000, min_length=1)
    """
    추가할 수신자 목록입니다. 한 번에 최대 1,000건까지 추가할 수 있습니다.
    """


class ReservationUpdateRequest(RequestModel):
    """
    예약 수정 요청입니다. 예약 대기(PENDING) 상태인 예약 건의 발송 시각과 예약명만 바꿀 수 있습니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    resv_send_time: str = Field(
       default= ...,
        validation_alias='resvSendTime', serialization_alias='resvSendTime',
        examples=['2026-05-01 11:00:00'],
        json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'},
    )
    """
    변경할 예약 발송 시각입니다(yyyy-MM-dd HH:mm:ss).
    """
    resv_name: str | None = Field(default=None, validation_alias='resvName', serialization_alias='resvName', max_length=100)
    """
    예약명입니다.
    """


class SmsMessage(RequestModel):
    """
    SMS(단문) 메시지입니다. 제목 필드는 없습니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    from_: str = Field(..., validation_alias='from', serialization_alias='from', examples=['01000000000'])
    """
    발신번호입니다. 비즈고에 미리 등록한 번호여야 합니다.
    """
    text: str = Field(..., json_schema_extra={'x-max-bytes': 90, 'x-charset': 'EUC-KR'})
    """
    SMS 본문입니다. 최대 90byte이며, 이통사 규격상 EUC-KR 범위 밖 문자는 접수 오류가 날 수 있습니다.
    """
    ttl: str | None = Field(default=None, pattern='^[0-9]+$')
    """
    이통사 전달까지 유효한 최대 시간(초)입니다. 시간이 지나면 실패 처리됩니다.
    """
    origin_cid: str | None = Field(default=None, validation_alias='originCID', serialization_alias='originCID')
    """
    최초 발신사업자 식별코드(9자리)입니다. 일반 고객은 입력하지 않습니다.
    """


class AlimtalkItem(RequestModel):
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


class BrandMessageCarouselItemAttachment(RequestModel):
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


class BrandMessageCatalog(RequestModel):
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


class BrandMessageItem(RequestModel):
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


class CounselCarouselItemAttachment(RequestModel):
    """
    캐러셀 아이템 첨부 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    buttons: list[CounselButton] | None = Field(default=None, max_length=5)
    """
    캐러셀 아이템 버튼 목록입니다. 쿠폰을 적용하면 최대 4개, 그 외 최대 5개입니다.
    """
    image: CounselImage
    coupon: CounselCoupon | None = None


class CounselConsultTimeSetting(RequestModel):
    """
    저장할 상담시간입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    week_time_table: list[CounselWeekTime] = Field(..., validation_alias='weekTimeTable', serialization_alias='weekTimeTable')
    """
    요일별 상담 시간 목록입니다.
    """


class CounselItem(RequestModel):
    """
    아이템 리스트 요소입니다. ITEM_LIST, WIDE_ITEM_LIST 타입에서 필수입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    highlight: CounselItemHighlight | None = None
    list_: list[CounselItemListEntry] = Field(
       default= ..., validation_alias='list', serialization_alias='list', max_length=10, min_length=2
    )
    """
    아이템 리스트입니다. ITEM_LIST는 2~10개, WIDE_ITEM_LIST는 3~4개입니다.
    """
    summary: CounselItemSummary | None = None


class CounselMessageDeleteRequest(RequestModel):
    """
    상담 메시지 삭제 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    cstalk: CounselMessageDeleteTarget


class CounselRichAttachment(RequestModel):
    """
    Rich 메시지 첨부 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    image: CounselImage | None = None
    buttons: list[CounselButton] | None = Field(default=None, max_length=5)
    """
    버튼 목록입니다. TEXT, IMAGE, ITEM_LIST는 쿠폰 적용 시 최대 4개, 그 외 최대 5개이며 WIDE, WIDE_ITEM_LIST, CAROUSEL_FEED는 최대 2개입니다.
    """
    quick_replies: list[CounselQuickReply] | None = Field(
        default=None, validation_alias='quickReplies', serialization_alias='quickReplies', max_length=10
    )
    """
    바로연결 목록입니다. 최대 10개입니다.
    """
    coupon: CounselCoupon | None = None
    item: CounselItem | None = None


class CounselSystemMessageCreateRequest(RequestModel):
    """
    시스템 메시지 등록 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    cstalk: CounselSystemMessageDraft


class CounselUserBlockRequest(RequestModel):
    """
    사용자 수신 차단·차단 해제 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    cstalk: CounselUserTarget


class InternationalFlowItem(RequestModel):
    model_config = ConfigDict(
        extra='forbid',
        populate_by_name=True,
    )
    international: InternationalMessage


class MmsFlowItem(RequestModel):
    model_config = ConfigDict(
        extra='forbid',
        populate_by_name=True,
    )
    mms: MmsMessage


class NaverTalkAttachments(RequestModel):
    """
    네이버 톡톡 첨부 정보 객체입니다(이미지, 버튼, 쿠폰).
    쿠폰(`gift`)을 첨부하면 이미지는 첨부되지 않습니다(리포트 코드 72105).

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    image_url: str | None = Field(default=None, validation_alias='imageUrl', serialization_alias='imageUrl')
    """
    첨부 이미지 URL입니다.
    """
    image_hash_id: str | None = Field(default=None, validation_alias='imageHashId', serialization_alias='imageHashId')
    """
    첨부 이미지 hashId입니다. 이미지 hashId에 해당하는 파트너 키나 템플릿 그룹키를 써야 합니다(리포트 코드 72011, 72104).
    """
    buttons: list[NaverTalkButton] | None = None
    """
    버튼 목록입니다. 템플릿에 필요한 버튼 개수와 같아야 합니다(리포트 코드 72004).
    """
    gift: NaverTalkGift | None = None


class NaverTalkMessage(RequestModel):
    """
    네이버 톡톡(네이버 스마트알림) 메시지입니다. `messageFlow[].navertalk` 객체로 보냅니다.
    네이버 스마트알림 규격에 맞춘 템플릿 기반 정보성 메시지입니다.

    수신번호 규칙(`destinations[].to`): 11자리 휴대폰 번호입니다(예: `01000000000`).

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    partner_key: str = Field(..., validation_alias='partnerKey', serialization_alias='partnerKey', examples=['PARTNER_KEY_EXAMPLE'])
    """
    네이버 톡톡 파트너 키입니다(접수코드 A601).
    """
    template_code: str = Field(
       default= ..., validation_alias='templateCode', serialization_alias='templateCode', examples=['TEMPLATE_CODE_EXAMPLE']
    )
    """
    네이버 톡톡 템플릿 코드입니다.
    """
    product_code: str = Field(..., validation_alias='productCode', serialization_alias='productCode', examples=['INFORMATION'])
    """
    템플릿의 상품 코드입니다. 등록된 템플릿의 상품 코드와 같아야 합니다(접수코드 A602, 리포트 코드 71007).
    원문 요청 예시 값은 `INFORMATION`이며, 전체 값 목록은 원문에 없습니다.

    """
    user_name: str | None = Field(default=None, validation_alias='userName', serialization_alias='userName')
    """
    전화번호 소유자의 실명입니다.
    """
    text: str | None = Field(default=None, max_length=2048)
    """
    템플릿 본문입니다. 최대 2,048자입니다.
    """
    template_params: dict[str, str] | None = Field(default=None, validation_alias='templateParams', serialization_alias='templateParams')
    """
    템플릿 치환 변수입니다. 치환할 키-값 쌍을 넣습니다. 최대 150자입니다.
    """
    attachments: NaverTalkAttachments | None = None
    group_key: str | None = Field(default=None, validation_alias='groupKey', serialization_alias='groupKey')
    """
    네이버 톡톡 발송 그룹입니다. 요청 최상위의 `groupKey`(메시지 인사이트 통계용)와는 다른 필드입니다.
    """


class RcsAction(RequestModel):
    """
    버튼 액션 객체입니다. 아래 액션 유형 객체를 넣습니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    url_action: RcsUrlAction | None = Field(default=None, validation_alias='urlAction', serialization_alias='urlAction')
    dialer_action: RcsDialerAction | None = Field(default=None, validation_alias='dialerAction', serialization_alias='dialerAction')
    map_action: RcsMapAction | None = Field(default=None, validation_alias='mapAction', serialization_alias='mapAction')
    calendar_action: RcsCalendarAction | None = Field(default=None, validation_alias='calendarAction', serialization_alias='calendarAction')
    compose_action: RcsComposeAction | None = Field(default=None, validation_alias='composeAction', serialization_alias='composeAction')


class RcsBrand(RequestModel):
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


class RcsSuggestion(RequestModel):
    """
    버튼 액션 정의(버튼 1개)입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    action: RcsAction | None = None
    display_text: str = Field(..., validation_alias='displayText', serialization_alias='displayText')
    """
    버튼 명입니다.
    """


class RcsTemplateAction(RequestModel):
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


class RcsTemplateSuggestion(RequestModel):
    """
    템플릿 버튼 액션 정의(버튼 1개)입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    action: RcsTemplateAction | None = None


class SmsFlowItem(RequestModel):
    model_config = ConfigDict(
        extra='forbid',
        populate_by_name=True,
    )
    sms: SmsMessage


class AlimtalkAttachment(RequestModel):
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


class AlimtalkMessage(RequestModel):
    """
    카카오 알림톡 메시지입니다. 카카오가 승인한 템플릿을 기반으로 정보성 메시지를 발송합니다.

    발송 방식은 2가지입니다.
    - **전문 발송**: `msgType`(AT/AI), `text` 등 템플릿 전문을 본문에 직접 넣습니다. 이때 `msgType`과 `text`는 필수입니다.
    - **템플릿 자동 치환 발송**: `sendType`을 `template`으로 두고 `senderKey`, `templateCode`만 보냅니다.
      Bizgo API가 템플릿 코드에 맞는 전문을 만든 뒤 `destinations[].replaceWords` 값을 치환합니다.
      이 방식에서는 `destinations[].replaceWords`가 필수이며, `msgType`·`text`·`attachment` 등 전문 필드는 문서에 없습니다.

    두 방식의 조건부 필수 필드는 `x-sdk-required-if`에 있습니다. SDK는 보내기 전에 이 규칙을 검사합니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    msg_type: Literal['AT', 'AI'] | None = Field(default=None, validation_alias='msgType', serialization_alias='msgType', examples=['AT'])
    """
    카카오 비즈메시지 타입입니다. 전문 발송(`sendType`이 `template`이 아님) 시 필수이며, 빠지면 서버가 A523으로 거절합니다(템플릿 자동 치환 발송에서는 생략).
    - `AT`: 텍스트형
    - `AI`: 이미지형

    """
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    카카오 비즈메시지 발신프로필 키입니다.
    """
    template_code: str = Field(
       default= ..., validation_alias='templateCode', serialization_alias='templateCode', examples=['TEMPLATE_CODE_EXAMPLE']
    )
    """
    알림톡 템플릿 코드입니다.
    """
    send_type: Literal['template'] | None = Field(default=None, validation_alias='sendType', serialization_alias='sendType')
    """
    템플릿 변수 자동 치환 발송 타입입니다. 템플릿 자동 치환 발송 시 필수이며 `template`을 입력합니다. 전문 발송에서는 생략합니다.
    """
    response_method: Literal['push', 'polling'] | None = Field(
        default='push', validation_alias='responseMethod', serialization_alias='responseMethod'
    )
    """
    카카오 응답 방식입니다. 기본값은 `push`입니다.
    - `push`(권장): 활성 사용자 조건에 해당하면 ACK 수신 여부를 확인하지 않고 성공 처리합니다. 조건을 만족하지 않으면 `NoSendAvailableException` 오류를 응답합니다.
    - `polling`: `timeout` 안에 수신 결과가 도착하면 성공(`MS03`), 나머지는 성공불확실(`ME09`)로 처리합니다.

    """
    timeout: str | None = Field(default='180', pattern='^[0-9]+$')
    """
    polling 발송 시 수신 결과를 기다리는 시간(초)입니다. 10~86,400초이며 기본값은 180초입니다.
    """
    text: str | None = Field(default=None, max_length=1300)
    """
    알림톡 본문입니다. 전문 발송(`sendType`이 `template`이 아님) 시 필수입니다. 최대 1,300자입니다.
    """
    title: str | None = Field(default=None, max_length=50)
    """
    알림톡 제목입니다(강조표기형 템플릿). 최대 50자입니다.
    """
    header: str | None = None
    """
    메시지 상단에 표기할 제목입니다.
    """
    link: AlimtalkLink | None = None
    attachment: AlimtalkAttachment | None = None
    supplement: AlimtalkSupplement | None = None
    price: str | None = None
    """
    메시지에 포함된 가격/금액/결제금액입니다.
    """
    currency_type: str | None = Field(default=None, validation_alias='currencyType', serialization_alias='currencyType', examples=['KRW'])
    """
    가격/금액/결제금액의 통화 단위입니다. 알려진 값은 `KRW`, `USD`, `EUR`입니다.
    """


class AlimtalkTemplateBody(RequestModel):
    """
    알림톡 템플릿 등록·수정 요청의 템플릿 정보(`alimtalk`)입니다.
    이미지형·아이템리스트형 템플릿은 템플릿 이미지 업로드(`POST /file/alimtalk/template`)로 받은 `imgUrl`과 이름을 `imgUrl`, `imgName`에 넣습니다.
    버튼·바로연결·아이템 구조는 발송 규격의 `AlimtalkButton`, `AlimtalkQuickReply`, `AlimtalkItem` 등과 같습니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    카카오 비즈메시지 발신프로필 키입니다. `senderKeyType`이 `G`이면 그룹 키입니다.
    """
    sender_key_type: Literal['G', 'S'] | None = Field(default='S', validation_alias='senderKeyType', serialization_alias='senderKeyType')
    """
    발신프로필 키 타입입니다. 기본값은 `S`입니다.
    - `G`: 그룹
    - `S`: 발신프로필

    """
    template_name: str = Field(..., validation_alias='templateName', serialization_alias='templateName', max_length=200)
    """
    템플릿 이름입니다. 최대 200자입니다.
    """
    template_code: str = Field(
       default= ..., validation_alias='templateCode', serialization_alias='templateCode', examples=['TEMPLATE_CODE_EXAMPLE'], max_length=30
    )
    """
    알림톡 템플릿 코드입니다. 최대 30자입니다.
    """
    template_message_type: str = Field(
       default= ..., validation_alias='templateMessageType', serialization_alias='templateMessageType', examples=['BA']
    )
    """
    템플릿 메시지 타입입니다. 문서 예시 값은 `BA`입니다.
    """
    template_emphasize_type: str = Field(
       default= ..., validation_alias='templateEmphasizeType', serialization_alias='templateEmphasizeType', examples=['NONE']
    )
    """
    템플릿 강조 타입입니다. 문서 예시 값은 `NONE`입니다.
    """
    text: str = Field(..., max_length=1300)
    """
    알림톡 템플릿 본문입니다. 최대 1,300자이며 `#{변수}` 형식의 치환 변수를 쓸 수 있습니다.
    """
    title: str | None = Field(default=None, max_length=50)
    """
    강조표기형 템플릿 제목입니다. 최대 50자입니다.
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
    템플릿 이미지 파일 이름입니다.
    """
    img_url: str | None = Field(default=None, validation_alias='imgUrl', serialization_alias='imgUrl')
    """
    템플릿 이미지 URL입니다. 템플릿 이미지 업로드 응답의 `imgUrl`을 씁니다.
    """
    link: AlimtalkLink | None = None
    attachment: AlimtalkAttachment | None = None
    supplement: AlimtalkSupplement | None = None
    category_code: str | None = Field(default=None, validation_alias='categoryCode', serialization_alias='categoryCode')
    """
    템플릿 카테고리 코드입니다. 템플릿 카테고리 전체 조회로 확인합니다.
    """
    security_flag: bool | None = Field(default=None, validation_alias='securityFlag', serialization_alias='securityFlag')
    """
    보안 템플릿 여부입니다.
    """
    adult_flag: bool | None = Field(default=False, validation_alias='adultFlag', serialization_alias='adultFlag')
    """
    연령 인증 설정 여부입니다. 수신자가 연령 인증을 마치기 전까지 채팅방에서 메시지가 가려지며 만 20세 이상만 볼 수 있습니다. 기본값은 `false`입니다.
    """
    preview_message: str | None = Field(default=None, validation_alias='previewMessage', serialization_alias='previewMessage')
    """
    템플릿 미리보기 메시지입니다.
    """
    extra: str | None = None
    """
    부가 정보입니다.
    """


class AlimtalkTemplateSaveRequest(RequestModel):
    """
    알림톡 템플릿 등록(`POST`)·수정(`PUT`) 요청 본문입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    alimtalk: AlimtalkTemplateBody


class BrandMessageAttachment(RequestModel):
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


class BrandMessageCarouselItem(RequestModel):
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


class CounselCarouselItem(RequestModel):
    """
    캐러셀 아이템 1개입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    header: str | None = None
    """
    캐러셀 아이템 제목입니다. CAROUSEL_FEED 타입에서 사용합니다.
    """
    message: str | None = None
    """
    캐러셀 아이템 메시지입니다. CAROUSEL_FEED 타입에서 사용합니다.
    """
    attachment: CounselCarouselItemAttachment | None = None


class CounselConsultTimeSaveRequest(RequestModel):
    """
    상담시간 저장 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    cstalk: CounselConsultTimeSetting


class NaverTalkFlowItem(RequestModel):
    model_config = ConfigDict(
        extra='forbid',
        populate_by_name=True,
    )
    navertalk: NaverTalkMessage


class RcsButton(RequestModel):
    """
    RCS 버튼입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    suggestions: list[RcsSuggestion] | None = None
    """
    버튼 액션 정의 목록입니다.
    """


class RcsMessage(RequestModel):
    """
    RCS 메시지입니다. 같은 `rcs` 키로 **통합 RCS**(iOS·안드로이드 동시 지원, 신규 연동 권장)와
    **안드로이드 RCS**(기존 안드로이드 채팅+ 연동 규격 유지용)를 모두 발송합니다.
    `copyAllowed`, `header`, `footer`는 안드로이드 RCS 발송 문서에만 있는 필드입니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    from_: str = Field(..., validation_alias='from', serialization_alias='from', examples=['01000000000'])
    """
    발신번호입니다.
    """
    format_id: str = Field(..., validation_alias='formatId', serialization_alias='formatId', examples=['RCS_FORMAT_ID'])
    """
    RCS 메시지 포맷(템플릿) ID입니다.
    """
    brand_key: str = Field(..., validation_alias='brandKey', serialization_alias='brandKey', examples=['RCS_BRAND_KEY'])
    """
    RCS 브랜드 식별 키입니다.
    """
    body: RcsBody
    buttons: list[RcsButton] | None = None
    """
    RCS 버튼 목록입니다.
    """
    brand_id: str | None = Field(default=None, validation_alias='brandId', serialization_alias='brandId', examples=['BRAND_ID_EXAMPLE'])
    """
    RCS 브랜드 ID입니다.
    """
    group_id: str | None = Field(default=None, validation_alias='groupId', serialization_alias='groupId')
    """
    RCS 메시지 그룹 ID입니다.
    """
    expiry_option: Literal['1', '2', '3', '4'] | None = Field(default='1', validation_alias='expiryOption', serialization_alias='expiryOption')
    """
    전송 타임아웃 설정입니다. 기본값은 `1`입니다.
    - `1`: 24시간
    - `2`: 40초
    - `3`: 3분 10초
    - `4`: 1시간

    """
    copy_allowed: Literal['0', '1'] | None = Field(default='0', validation_alias='copyAllowed', serialization_alias='copyAllowed')
    """
    (안드로이드 RCS) 메시지 복사 허용 여부입니다. `0`=허용 안 함, `1`=허용. 기본값은 `0`입니다.
    """
    header: Literal['0', '1'] | None = '0'
    """
    (안드로이드 RCS) 광고 표시 레이블 여부입니다. `0`=표시 안 함, `1`=표시. 기본값은 `0`입니다.
    """
    footer: str | None = Field(default=None, max_length=100)
    """
    (안드로이드 RCS) 수신거부 번호입니다. `header`가 `1`이면 필수이며 최대 100자입니다.
    """
    agency_id: str | None = Field(default='infobank', validation_alias='agencyId', serialization_alias='agencyId')
    """
    대행사 ID입니다. 기본값은 `infobank`입니다.
    """
    agency_key: str | None = Field(default=None, validation_alias='agencyKey', serialization_alias='agencyKey')
    """
    대행사 키입니다.
    """
    ttl: str | None = Field(default='86400', pattern='^[0-9]+$')
    """
    메시지 유효 시간(초)입니다. 기본값은 `86400`입니다.
    """


class RcsTemplateButton(RequestModel):
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


class RcsTemplateDefinition(RequestModel):
    """
    등록·수정할 RCS 템플릿 정보입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brand_id: str = Field(..., validation_alias='brandId', serialization_alias='brandId', examples=['BRAND_ID_EXAMPLE'])
    """
    브랜드 ID입니다.
    """
    template_name: str = Field(..., validation_alias='templateName', serialization_alias='templateName')
    """
    템플릿 이름입니다.
    """
    body: list[RcsTemplateBodyParam]
    """
    본문 영역 정의입니다.
    """
    buttons: list[RcsTemplateButton]
    """
    버튼 정의입니다.
    """


class RcsTemplateRequest(RequestModel):
    """
    RCS 템플릿 등록·수정 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    rcs: RcsTemplateDefinition


class AlimtalkFlowItem(RequestModel):
    model_config = ConfigDict(
        extra='forbid',
        populate_by_name=True,
    )
    alimtalk: AlimtalkMessage


class BrandMessageCarousel(RequestModel):
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


class BrandMessageTemplateInput(RequestModel):
    """
    브랜드메시지 템플릿 등록·수정 정보입니다. 이미지가 필요한 유형은 이미지 파일 관리 API로 먼저 `imgUrl`을 발급받아 씁니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    카카오 비즈메시지 발신프로필 키입니다.
    """
    sender_key_type: str = Field(..., validation_alias='senderKeyType', serialization_alias='senderKeyType', examples=['S'])
    """
    발신프로필 키 타입입니다. 문서 예시 값은 `S`입니다.
    """
    send_type: Literal['basic', 'free'] = Field(
       default= ..., validation_alias='sendType', serialization_alias='sendType', examples=['basic']
    )
    """
    브랜드메시지 발송 타입입니다. `basic`(기본형) 또는 `free`(자유형)입니다.
    """
    template_name: str = Field(
       default= ..., validation_alias='templateName', serialization_alias='templateName', examples=['브랜드 혜택 안내'], max_length=200
    )
    """
    템플릿 이름입니다. 최대 200자입니다.
    """
    msg_type: str = Field(..., validation_alias='msgType', serialization_alias='msgType', examples=['FT'])
    """
    브랜드메시지 메시지 타입입니다. 알려진 값: `FT`, `FI`, `FW`, `FL`, `FC`, `FM`, `FA`, `FP`, `FG`(카탈로그).
    """
    template_code: str | None = Field(
        default=None, validation_alias='templateCode', serialization_alias='templateCode', examples=['TEMPLATE_CODE_EXAMPLE']
    )
    """
    템플릿 코드입니다. 수정 시 대상 템플릿을 지정합니다.
    """
    text: str | None = Field(
        default=None, examples=['#{customerName}님, 새로운 혜택을 확인해 주세요.']
    )
    """
    템플릿 본문입니다.
    """
    carousel: BrandMessageCarousel | None = None
    """
    캐러셀 정보입니다(FC, FA).
    """
    attachment: BrandMessageAttachment | None = None
    """
    첨부 정보입니다. 버튼은 최대 5개, FT/FI에 쿠폰을 함께 쓰면 최대 4개입니다.
    """
    header: str | None = Field(default=None, max_length=20)
    """
    헤더 정보입니다. 최대 20자입니다. `FG`에서는 헤더 타이틀로 씁니다.
    """
    header_description: str | None = Field(default=None, validation_alias='headerDescription', serialization_alias='headerDescription')
    """
    헤더 디스크립션입니다. `msgType`이 `FG`일 때만 사용합니다.
    """
    additional_content: str | None = Field(default=None, validation_alias='additionalContent', serialization_alias='additionalContent')
    """
    부가 정보입니다. `msgType`이 `FM`일 때 사용합니다.
    """
    push_alarm: Literal['Y', 'N'] | None = Field(default='Y', validation_alias='pushAlarm', serialization_alias='pushAlarm')
    """
    메시지 푸시 알림 발송 여부입니다. 기본값은 `Y`입니다.
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
    catalog_variable: list[BrandMessageCatalogVariable] | None = Field(
        default=None, validation_alias='catalogVariable', serialization_alias='catalogVariable'
    )
    """
    FG(카탈로그) 전용 아이템 단위 변수입니다.
    """
    create_at: str | None = Field(default=None, validation_alias='createAt', serialization_alias='createAt')
    """
    등록일입니다.
    """
    modified_at: str | None = Field(default=None, validation_alias='modifiedAt', serialization_alias='modifiedAt')
    """
    수정일입니다.
    """
    status: str | None = Field(default=None, examples=['A'])
    """
    템플릿 상태입니다. 알려진 값: `A`(등록), `S`(차단).
    """


class BrandMessageTemplateRequest(RequestModel):
    """
    브랜드메시지 템플릿 등록·수정 요청입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    brandmessage: BrandMessageTemplateInput
    """
    브랜드메시지 템플릿 정보입니다.
    """


class CounselCarousel(RequestModel):
    """
    캐러셀 정보입니다. CAROUSEL_FEED 타입에서 필수입니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    list_: list[CounselCarouselItem] | None = Field(
        default=None, validation_alias='list', serialization_alias='list', max_length=10, min_length=2
    )
    """
    캐러셀 아이템 리스트입니다. 최소 2개, 최대 10개입니다.
    """
    tail: CounselCarouselTail | None = None


class CounselRichMessageRequest(RequestModel):
    """
    상담톡 Rich 메시지 발송 요청입니다. 상담 세션이 열려 있는 사용자에게만 보낼 수 있습니다.
    본문과 첨부는 최종 사용자와의 상담 내용이므로 개인정보로 취급하고 로그에 남기지 않습니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    user_key: str = Field(
       default= ..., validation_alias='userKey', serialization_alias='userKey', examples=['USER_KEY_EXAMPLE'], max_length=20, min_length=1
    )
    """
    상담톡 사용자 키입니다. 카카오톡 채널별로 다르며 대소문자를 구분합니다. 1~20자이며 비어 있거나 20자를 넘으면 `A507`이 반환됩니다.
    """
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    msg_type: str = Field(..., validation_alias='msgType', serialization_alias='msgType')
    """
    메시지 풍선 타입입니다. 문서가 지원 타입으로 나열한 값은 TEXT, IMAGE, WIDE, ITEM_LIST, WIDE_ITEM_LIST, CAROUSEL_FEED, PERSONAL이며,
    본인인증 요청은 `KAKAO_CERT`입니다. `KAKAO_CERT`는 해당 채널이 본인인증 화이트리스트에 사전 등록되어 있어야 합니다
    (이용문의 또는 영업담당자를 통해 신청하며, CI 활용 여부 증적 자료와 채널 정보를 제출합니다).

    """
    message: str | None = None
    """
    사용자에게 전달할 메시지입니다.
    """
    description: str | None = None
    """
    사용자에게 전달할 부가 메시지입니다.
    """
    header: str | None = None
    """
    헤더입니다.
    """
    attachment: CounselRichAttachment | None = None
    carousel: CounselCarousel | None = None
    auto_answer: str | None = Field(default=None, validation_alias='autoAnswer', serialization_alias='autoAnswer')
    """
    시스템 자동 응답 메시지입니다.
    """
    lock: bool | None = None
    """
    보안 메시지 여부입니다.
    """
    cert_expiry: int | None = Field(default=None, validation_alias='certExpiry', serialization_alias='certExpiry')
    """
    본인인증 유효 시간(분)입니다. `msgType`이 `KAKAO_CERT`일 때 필수입니다.
    """
    ref: str | None = Field(default=None, max_length=200)
    """
    참조 필드입니다. 최대 200자이며 발송 결과 웹훅(`cstalk/result`)에서 함께 반환됩니다.
    """


class RcsFlowItem(RequestModel):
    model_config = ConfigDict(
        extra='forbid',
        populate_by_name=True,
    )
    rcs: RcsMessage


class BrandMessage(RequestModel):
    """
    카카오 브랜드메시지입니다. 카카오톡 채널 친구에게 브랜드형 메시지를 발송합니다. `sendType`으로 발송 방식을 구분합니다.

    | sendType | 방식 | 필수 필드 |
    | --- | --- | --- |
    | `basic` | 기본형. 사전 승인된 템플릿으로 발송합니다. 변수 분리 방식(`messageVariable` 등 `*Variable` 필드) 또는 전문 방식(`text`, `attachment`, `carousel`)을 템플릿 구조와 `msgType`에 맞게 선택해 씁니다. Variable 필드는 변수 치환이 필요할 때만 씁니다. | `sendType`, `msgType`, `senderKey`, `templateCode`, `targeting` |
    | `template` | 기본형 템플릿 자동 치환. 템플릿 코드와 `destinations[].replaceWords`만으로 발송하며 Bizgo API가 전문을 생성합니다. 사용 가능 필드는 `senderKey`, `templateCode`, `sendType`, `targeting`, `pushAlarm`, `originCID`, `unsubscribePhoneNumber`, `unsubscribeAuthNumber`입니다. | `sendType`, `senderKey`, `templateCode`, `targeting` (+ `destinations[].replaceWords`) |
    | `free` | 자유형. 템플릿 없이 본문·버튼·이미지·캐러셀 등을 직접 구성합니다. `templateCode`와 `*Variable` 필드는 쓰지 않으며, `groupTagKey`·`adult`·`adFlag`는 자유형에서만 씁니다. | `sendType`, `msgType`, `senderKey` |

    위 표의 `sendType`별 필수 필드는 `x-sdk-required-if`에 있으며 SDK가 보내기 전에 검사합니다. 아래 `msgType`별 요소는 설명으로만 두고 SDK가 검사하지 않습니다(`msgType` 값 확인 전).

    `msgType`별 주요 요소(문서의 필드 제약에서 정리):
    - `FT`: 본문 최대 1,300자
    - `FI`: `attachment.image` 필수, 본문 최대 400자
    - `FW`: 와이드 이미지. `attachment.image` 필수, 본문 최대 76자
    - `FL`: 와이드 리스트. `attachment.item`
    - `FP`: 동영상. `attachment.video`, 본문 최대 76자
    - `FM`: 커머스. `attachment.image` 필수, `attachment.commerce`, `additionalContent`
    - `FC`: 캐러셀 피드. `carousel`, 아이템별 `header`·`message`·`attachment.image` 필수, `carousel.head` 사용 불가
    - `FA`: 캐러셀 커머스. `carousel`, 아이템별 `attachment.image` 필수·`attachment.commerce`, 아이템 `header`·`message`·`additionalContent` 사용 불가
    - `FG`: 카탈로그. `header`(헤더 타이틀)·`attachment.catalog`(아이템 3~7개) 필수, `headerDescription` 사용. 친구톡 호환 모드로는 발송할 수 없고, PC톡·맥톡에서는 노출되지 않으며 카카오톡 v25.8.0 이상에서 확인할 수 있습니다. 기본형으로 등록한 카탈로그 템플릿은 `targeting` `M`·`N`으로 발송할 수 있습니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    send_type: Literal['basic', 'template', 'free'] = Field(
       default= ..., validation_alias='sendType', serialization_alias='sendType', examples=['basic']
    )
    """
    브랜드메시지 발송 타입입니다.
    - `basic`: 기본형 발송
    - `template`: 기본형 템플릿 자동 치환 발송
    - `free`: 자유형 발송

    """
    msg_type: str | None = Field(default=None, validation_alias='msgType', serialization_alias='msgType', examples=['FT'])
    """
    카카오 비즈메시지(브랜드메시지) 타입입니다. `basic`, `free` 발송 시 필수입니다(`template`에서는 생략).
    카카오 원본 chatBubbleType으로 변환됩니다. 알려진 값은 `FT`, `FI`, `FW`, `FL`, `FC`, `FM`, `FA`, `FP`, `FG`입니다.

    """
    sender_key: str = Field(..., validation_alias='senderKey', serialization_alias='senderKey', examples=['SENDER_KEY_EXAMPLE'])
    """
    발신프로필 키입니다.
    """
    template_code: str | None = Field(
        default=None, validation_alias='templateCode', serialization_alias='templateCode', examples=['TEMPLATE_CODE_EXAMPLE']
    )
    """
    브랜드메시지 템플릿 코드입니다. `basic`, `template` 발송 시 필수이며 `free`에서는 쓰지 않습니다.
    """
    targeting: Literal['M', 'N', 'O', 'I'] | None = None
    """
    고객사의 광고성 정보 수신동의 회원 대상 타겟팅입니다. `basic`, `template` 발송 시 필수, `free`에서는 선택입니다. 허용된(allowlist) 발신프로필만 사용할 수 있습니다.
    - `M`: 광고성 정보 수신동의 회원
    - `N`: 광고성 정보 수신동의 회원 − 채널 친구
    - `O`: 광고성 정보 수신동의 회원 ∩ 채널 친구 (수신거부 방식: 080 번호 안내)
    - `I`: 광고성 정보 수신동의 회원 ∩ 채널 친구 (수신거부 방식: 채널 차단 안내)

    """
    text: str | None = Field(default=None, max_length=1300)
    """
    브랜드메시지 본문입니다. 최대 글자 수는 `msgType`에 따라 다릅니다(FT 1,300자, FI 400자, FW/FP 76자).
    """
    header: str | None = Field(default=None, max_length=20)
    """
    헤더 정보입니다. 최대 20자입니다. `FG`(카탈로그)에서는 헤더 타이틀로 필수입니다.
    """
    header_description: str | None = Field(default=None, validation_alias='headerDescription', serialization_alias='headerDescription')
    """
    헤더 디스크립션입니다. `msgType`이 `FG`일 때만 사용합니다.
    """
    additional_content: str | None = Field(
        default=None, validation_alias='additionalContent', serialization_alias='additionalContent', max_length=34
    )
    """
    부가 정보입니다. `FM` 타입 전용이며 최대 34자입니다.
    """
    group_tag_key: str | None = Field(default=None, validation_alias='groupTagKey', serialization_alias='groupTagKey', max_length=40)
    """
    그룹태그 등록으로 발급받은 키입니다. 자유형(`free`) 발송에서 씁니다. 최대 40자입니다.
    """
    adult: Literal['Y', 'N'] | None = 'N'
    """
    성인 대상 메시지 여부입니다. 자유형(`free`) 발송에서 씁니다. 기본값은 `N`입니다.
    """
    push_alarm: Literal['Y', 'N'] | None = Field(default='Y', validation_alias='pushAlarm', serialization_alias='pushAlarm')
    """
    메시지 도착 시 푸시 알림 발송 여부입니다. 기본값은 `Y`입니다.
    """
    ad_flag: Literal['Y', 'N'] | None = Field(default='Y', validation_alias='adFlag', serialization_alias='adFlag')
    """
    광고성 메시지 필수 표기 사항 노출 여부입니다. 자유형(`free`) 발송에서 씁니다. 기본값은 `Y`이며, `msgType`이 `FL`, `FC`, `FA`이면 `Y`로만 발송할 수 있습니다.
    """
    message_variable: dict[str, Any] | None = Field(default=None, validation_alias='messageVariable', serialization_alias='messageVariable')
    """
    메시지 영역 변수 정의입니다. 기본형(`basic`) 변수 분리 방식에서 씁니다. FT, FI, FW, FL, FP, FM 타입에서 사용합니다.
    """
    button_variable: dict[str, Any] | None = Field(default=None, validation_alias='buttonVariable', serialization_alias='buttonVariable')
    """
    버튼 영역 변수 정의입니다. 기본형(`basic`) 변수 분리 방식에서 씁니다. FT, FI, FW, FL, FP, FM 타입에서 사용합니다.
    """
    coupon_variable: dict[str, Any] | None = Field(default=None, validation_alias='couponVariable', serialization_alias='couponVariable')
    """
    쿠폰 영역 변수 정의입니다. 기본형(`basic`) 변수 분리 방식에서 씁니다. FT, FI, FW, FL, FP, FM 타입에서 사용합니다.
    """
    image_variable: dict[str, Any] | None = Field(default=None, validation_alias='imageVariable', serialization_alias='imageVariable')
    """
    이미지 영역 변수 정의입니다. 기본형(`basic`) 변수 분리 방식에서 씁니다. FI, FW, FL, FM 타입에서 사용합니다.
    """
    video_variable: dict[str, Any] | None = Field(default=None, validation_alias='videoVariable', serialization_alias='videoVariable')
    """
    비디오 영역 변수 정의입니다. 기본형(`basic`) 변수 분리 방식에서 씁니다. FP 타입에서 사용합니다.
    """
    commerce_variable: dict[str, Any] | None = Field(default=None, validation_alias='commerceVariable', serialization_alias='commerceVariable')
    """
    커머스 영역 변수 정의입니다. 기본형(`basic`) 변수 분리 방식에서 씁니다. FM 타입에서 사용합니다.
    """
    carousel_variable: list[BrandMessageCarouselVariable] | None = Field(
        default=None, validation_alias='carouselVariable', serialization_alias='carouselVariable'
    )
    """
    캐러셀 영역 변수 목록입니다. 기본형(`basic`) 변수 분리 방식에서 씁니다. FC, FA 타입에서 사용합니다.
    """
    catalog_variable: list[BrandMessageCatalogVariable] | None = Field(
        default=None, validation_alias='catalogVariable', serialization_alias='catalogVariable'
    )
    """
    FG(카탈로그) 전용 아이템 단위 변수입니다. 기본형(`basic`) 변수 분리 방식에서 씁니다.
    """
    origin_cid: str | None = Field(default=None, validation_alias='originCID', serialization_alias='originCID', max_length=9)
    """
    최초 발신사업자 식별코드(최대 9자)입니다. 재판매사·특수부가통신사업자는 필수입니다.
    """
    unsubscribe_phone_number: str | None = Field(
        default=None, validation_alias='unsubscribePhoneNumber', serialization_alias='unsubscribePhoneNumber', max_length=13
    )
    """
    무료 수신거부 전화번호입니다. 최대 13자입니다.
    """
    unsubscribe_auth_number: str | None = Field(
        default=None, validation_alias='unsubscribeAuthNumber', serialization_alias='unsubscribeAuthNumber', max_length=10
    )
    """
    무료 수신거부 인증번호입니다. 최대 10자입니다.
    """
    attachment: BrandMessageAttachment | None = None
    carousel: BrandMessageCarousel | None = None


class BrandMessageFlowItem(RequestModel):
    model_config = ConfigDict(
        extra='forbid',
        populate_by_name=True,
    )
    brandmessage: BrandMessage


_FLOW_KEYS = frozenset({'sms', 'mms', 'international', 'rcs', 'alimtalk', 'brandmessage', 'navertalk'})


def _flow_key(value: Any) -> str | None:
    """Return the channel key of a messageFlow item (``sms``, ``alimtalk``, ...)."""
    if isinstance(value, dict):
        found = [k for k in value if k in _FLOW_KEYS]
        return found[0] if len(found) == 1 else None
    for name, key in _FLOW_CLASS_KEYS.items():
        if type(value).__name__ == name:
            return key
    return None


_FLOW_CLASS_KEYS = {'SmsFlowItem': 'sms', 'MmsFlowItem': 'mms', 'InternationalFlowItem': 'international', 'RcsFlowItem': 'rcs', 'AlimtalkFlowItem': 'alimtalk', 'BrandMessageFlowItem': 'brandmessage', 'NaverTalkFlowItem': 'navertalk'}

MessageFlowItem = Annotated[
    Union[
    Annotated[SmsFlowItem, Tag('sms')],
    Annotated[MmsFlowItem, Tag('mms')],
    Annotated[InternationalFlowItem, Tag('international')],
    Annotated[RcsFlowItem, Tag('rcs')],
    Annotated[AlimtalkFlowItem, Tag('alimtalk')],
    Annotated[BrandMessageFlowItem, Tag('brandmessage')],
    Annotated[NaverTalkFlowItem, Tag('navertalk')],
    ],
    Discriminator(_flow_key, custom_error_type='message_flow_channel', custom_error_message='messageFlow 항목에는 채널 키(sms, mms, international, rcs, alimtalk, brandmessage, navertalk) 중 정확히 하나가 있어야 합니다'),
]
"""messageFlow 항목 1개. 채널 키 하나만 가진 객체입니다."""


class SendOmniRequest(RequestModel):
    """
    통합 발송 요청입니다. 모든 채널이 같은 형식을 쓰며, 채널은 `messageFlow` 안의 채널 키로 구분합니다.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    destinations: list[Destination] = Field(..., max_length=200, min_length=1)
    """
    수신자 목록입니다. 한 요청에 최대 200건까지 동보발송할 수 있습니다(초과 시 A318).
    """
    message_flow: list[MessageFlowItem] = Field(..., validation_alias='messageFlow', serialization_alias='messageFlow', min_length=1)
    """
    발송할 메시지 목록입니다. 순서대로 대체발송(Fallback)됩니다.
    """
    payment_code: str | None = Field(default=None, validation_alias='paymentCode', serialization_alias='paymentCode')
    """
    정산용 부서 코드입니다.
    """
    group_key: str | None = Field(default=None, validation_alias='groupKey', serialization_alias='groupKey')
    """
    메시지 인사이트에서 통계를 그룹으로 묶어 보기 위한 키입니다.
    """
    idempotency_key: str | None = Field(default=None, validation_alias='idempotencyKey', serialization_alias='idempotencyKey', max_length=200)
    """
    중복 요청을 막는 멱등성 키입니다. 같은 키로 유효시간 안에 다시 요청하면 요청은 성공(HTTP 200)으로 오고 수신자별 결과(`destinations[].code`)가 A301이 됩니다(2026-09-28 sandbox 확인). SDK는 이 수신자를 실패가 아닌 `duplicates`로 돌려줍니다. 이 값을 보내면 `idempotencyTtl`도 함께 보내야 합니다.
    """
    idempotency_ttl: int | None = Field(default=None, validation_alias='idempotencyTtl', serialization_alias='idempotencyTtl', ge=0, le=86400)
    """
    멱등성 키 유효시간(초)입니다. 공개 문서는 선택 항목으로 표기하지만 `idempotencyKey`를 보내면 **반드시 함께 보내야 합니다**(없으면 A309).
    `idempotencyKey` 없이 이 값만 보내면 SDK는 받은 값을 그대로 보냅니다.
    공식 SDK는 `idempotencyKey`만 지정하고 이 값을 비워 두면 86400(24시간)을 채워 보냅니다. 직접 지정한 값(0 포함)은 그대로 보냅니다.

    """
    ref: str | None = None
    """
    요청 단위 참조 필드입니다. 리포트에 그대로 담겨 요청·메시지를 구분하는 데 씁니다.
    """


class ReservationCreateRequest(RequestModel):
    """
    예약 발송 등록 요청입니다. 통합 발송 요청과 같은 `destinations`·`messageFlow` 구조에 예약 시각(`resvSendTime`)과 예약명(`resvName`)을 더합니다.
    예약 발송 문서에는 `groupKey`, `idempotencyKey`, `idempotencyTtl`이 없으므로 넣지 않았습니다.

    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    destinations: list[Destination] = Field(..., max_length=200, min_length=1)
    """
    수신자 목록입니다. 한 요청에 최대 200건까지 동보발송할 수 있습니다. 국제메시지는 국가번호를 포함한 E.164 형식(+ 제외)을 씁니다.
    """
    message_flow: list[
        SmsFlowItem
        | MmsFlowItem
        | InternationalFlowItem
        | RcsFlowItem
        | AlimtalkFlowItem
        | BrandMessageFlowItem
    ] = Field(..., validation_alias='messageFlow', serialization_alias='messageFlow', min_length=1)
    """
    예약 발송할 메시지 목록입니다. 순서대로 대체발송(Fallback)됩니다.
    """
    resv_send_time: str = Field(
       default= ...,
        validation_alias='resvSendTime', serialization_alias='resvSendTime',
        examples=['2026-05-01 10:00:00'],
        json_schema_extra={'x-format': 'yyyy-MM-dd HH:mm:ss'},
    )
    """
    예약 발송 시각입니다. `yyyy-MM-dd HH:mm:ss` 또는 `yyyy-MM-dd'T'HH:mm:ss` 형식을 씁니다.
    현재 시각 + 10분부터 1년 이내로 지정할 수 있습니다(너무 이르면 A316, 1년 초과 시 A331).
    광고성 메시지는 야간 차단 시간대(20:00~08:00 KST)에 예약할 수 없습니다(A330).

    """
    resv_name: str | None = Field(
        default=None, validation_alias='resvName', serialization_alias='resvName', examples=['문자 예약 발송'], max_length=100
    )
    """
    예약 건을 식별하기 위한 이름입니다.
    """
    payment_code: str | None = Field(default=None, validation_alias='paymentCode', serialization_alias='paymentCode', max_length=20)
    """
    정산용 부서 코드입니다.
    """
    ref: str | None = Field(default=None, max_length=200)
    """
    요청 단위 참조 필드입니다. 리포트에 그대로 담겨 요청·메시지를 구분하는 데 씁니다.
    """

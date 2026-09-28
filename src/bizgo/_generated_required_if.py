"""Generated from spec/openapi.yaml (x-sdk-required-if) by scripts/generate_models.py. Do not edit."""

Rule = tuple[str, str, tuple[str, ...], tuple[str, ...], tuple[str, ...]]
"""(when field, operator, values, required properties, required paths). API field names."""

RULES: dict[str, tuple[Rule, ...]] = {
    'AlimtalkMessage': (
        ('sendType', 'notEquals', ('template',), ('msgType', 'text'), ()),
        ('sendType', 'equals', ('template',), (), ('$.destinations[].replaceWords',)),
    ),
    'BrandMessage': (
        ('sendType', 'in', ('basic', 'free'), ('msgType',), ()),
        ('sendType', 'in', ('basic', 'template'), ('templateCode', 'targeting'), ()),
        ('sendType', 'equals', ('template',), (), ('$.destinations[].replaceWords',)),
    ),
    'BrandMessageButton': (
        ('type', 'equals', ('WL',), ('urlPc', 'urlMobile'), ()),
        ('type', 'equals', ('AL',), ('urlMobile',), ()),
    ),
    'CounselPlainMessageRequest': (
        ('msgType', 'equals', ('FILE',), (), ('attachment.file.fileName', 'attachment.file.fileSize')),
    ),
    'CounselRichMessageRequest': (
        ('msgType', 'in', ('IMAGE', 'WIDE'), (), ('attachment.image',)),
        ('msgType', 'in', ('ITEM_LIST', 'WIDE_ITEM_LIST'), (), ('attachment.item',)),
        ('msgType', 'equals', ('CAROUSEL_FEED',), ('carousel',), ()),
        ('msgType', 'equals', ('KAKAO_CERT',), ('certExpiry',), ()),
    ),
    'RcsMessage': (
        ('header', 'equals', ('1',), ('footer',), ()),
    ),
}
"""Request model name -> conditional-required rules (AND-ed)."""

ROOTS: frozenset[str] = frozenset(
    {
        'AlimtalkTemplateInspectionCancelRequest',
        'AlimtalkTemplateInspectionRequest',
        'AlimtalkTemplateSaveRequest',
        'BrandMessageAudiencePossibleByPhoneNumbersRequest',
        'BrandMessageFriendGroupRequest',
        'BrandMessageGroupSendControlRequest',
        'BrandMessageGroupSendCreateRequest',
        'BrandMessageGroupTagRequest',
        'BrandMessagePermissionApplyRequest',
        'BrandMessageTemplateRequest',
        'BrandMessageUnsubscribeContentRequest',
        'BrandMessageVideoRegisterRequest',
        'BrandMessageVideoUploadRegisterRequest',
        'CounselConsultTimeSaveRequest',
        'CounselEndRequest',
        'CounselEndWithBotRequest',
        'CounselMessageDeleteRequest',
        'CounselPlainMessageRequest',
        'CounselRichMessageRequest',
        'CounselSenderActivationRequest',
        'CounselSenderRequest',
        'CounselSystemMessageCreateRequest',
        'CounselUserBlockRequest',
        'KakaoGroupSenderAddRequest',
        'KakaoSenderCreateRequest',
        'KakaoSenderRecoverRequest',
        'KakaoSenderTokenRequest',
        'RcsBrand',
        'RcsChatbot',
        'RcsTemplateRequest',
        'ReservationCreateRequest',
        'ReservationRecipientCreateRequest',
        'ReservationUpdateRequest',
        'SendOmniRequest',
    }
)
"""Request body models: ``$.`` paths are evaluated from these (the whole body is validated there)."""

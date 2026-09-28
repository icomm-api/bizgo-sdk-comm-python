"""Request and response models.

Channel messages you put in ``messages=[...]`` of :meth:`bizgo.resources.Send.omni`:

=====================  =========================  ============================
channel                model                      messageFlow key
=====================  =========================  ============================
SMS                    :class:`SmsMessage`        ``sms``
LMS / MMS              :class:`MmsMessage`        ``mms`` (MMS if ``file_key``)
International          :class:`InternationalMessage`  ``international``
RCS                    :class:`RcsMessage`        ``rcs``
Kakao AlimTalk         :class:`AlimtalkMessage`   ``alimtalk``
Kakao BrandMessage     :class:`BrandMessage`      ``brandmessage``
Naver TalkTalk         :class:`NaverTalkMessage`  ``navertalk``
=====================  =========================  ============================

Request models reject unknown fields and check byte limits (for example SMS text <= 90 bytes in EUC-KR).
Response models keep unknown fields in ``model_extra``. A schema used both in requests and responses (buttons,
template items, ...) exists in both modules; this package exports the request version, and responses are parsed
with the lenient response version (``bizgo.models._generated_response``).
"""

# ruff: noqa: I001  (import order matters: request models must win)
from . import _generated_request, _generated_response
from ._generated_response import *  # noqa: F403

# request models win for schemas used on both sides
from ._generated_request import *  # type: ignore[assignment]  # noqa: F403
from ._results import BulkChunkError as BulkChunkError
from ._results import BulkSendResult as BulkSendResult
from ._results import MessagePage as MessagePage
from ._results import MoPage as MoPage
from ._results import ReportBatch as ReportBatch
from ._results import SendResult as SendResult

__all__ = sorted(
    {name for name in dir(_generated_request) if name[:1].isupper() and not name.startswith("_")}
    | {name for name in dir(_generated_response) if name[:1].isupper() and not name.startswith("_")}
    | {"BulkChunkError", "BulkSendResult", "MessagePage", "MoPage", "ReportBatch", "SendResult"}
    - {
        "Annotated",
        "Any",
        "ConfigDict",
        "Discriminator",
        "Field",
        "Literal",
        "RequestModel",
        "ResponseModel",
        "Tag",
        "Union",
    }
)

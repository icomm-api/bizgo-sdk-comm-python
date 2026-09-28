"""Send to several recipient groups concurrently with the async client."""

import asyncio

from _env import env

from bizgo import AsyncBizgo, Environment, SmsMessage


async def main(client: AsyncBizgo, *, from_: str, groups: list[list[str]]) -> None:
    message = SmsMessage(from_=from_, text="[비즈고] 점검 안내: 오늘 23시부터 1시간")
    # each request takes up to 200 recipients; the default send limit is 200 requests per second
    results = await asyncio.gather(*(client.send.omni(to=group, messages=[message]) for group in groups))
    print("접수:", sum(len(r.succeeded) for r in results), "실패:", sum(len(r.failed) for r in results))


if __name__ == "__main__":

    async def run() -> None:
        async with AsyncBizgo(environment=Environment.SANDBOX) as client:
            await main(client, from_=env("BIZGO_FROM"), groups=[[env("BIZGO_TO")]])

    asyncio.run(run())

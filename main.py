from datetime import datetime

import pytz
from fastapi import FastAPI

app = FastAPI()


@app.get("/time")
async def get_time(timezone: str = "UTC"):
    try:
        tz = pytz.timezone(timezone)
        now = datetime.now(tz)
        return {"datetime": now.strftime("%Y-%m-%d %H:%M:%S %Z")}
    except pytz.exceptions.UnknownTimeZoneError:
        return {"error": "Invalid timezone"}

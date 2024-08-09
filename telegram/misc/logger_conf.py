import sys
import json
from loguru import logger


def serialize(record):
    subset = {
        "timestamp": record["time"].timestamp(),
        "message": record["message"],
        "level": record["level"].name,
    }
    return json.dumps(subset)


def patching(record):
    record["extra"]["serialized"] = serialize(record)


logger.remove(0)

logger = logger.patch(patching)
logger.add(sys.stderr, format="{extra[serialized]}")
logger.add(
    "./logs/log_{time:YYYY-MM-DD}.log",
    rotation="1 week",
    compression="zip",
    format="{extra[serialized]}"
)

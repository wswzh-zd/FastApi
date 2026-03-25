from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` ADD `addr` VARCHAR(32) NOT NULL COMMENT '教师' DEFAULT ' ';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` DROP COLUMN `addr`;"""


MODELS_STATE = (
    "eJztmV1P2zAUhv9KlSsmsSn9Lrsr3dAYAyRg0yRAkZs4adTULo4zqFD++2wnqZ00yVLalY"
    "B6U+jxsePz2D7nrfOszbAFPf/TyAO+9rnxrCEwg+yflP2woYH5XFq5gYKxJxzNxGPsUwJM"
    "ymw28HzITBb0TeLOqYsRs6LA87gRm8zRRY40Bch9CKBBsQPpBBLWcHvPzC6y4BP0k6/zqW"
    "G70LNS03Qt/mxhN+hiLmyniJ4IR/60sWFiL5gh6Txf0AlGS28XUW51IIIEUMiHpyTg0+ez"
    "i6NMIopmKl2iKSp9LGiDwKNKuBUZmBhxfmw20To4/CkfW81OvzNo9zoD5iJmsrT0wyg8GX"
    "vUURC4uNFC0Q4oiDwERslN/F0hN5oAko8u8c/AY1POwktQldFLDBKf3DKl/LS7oN+GFvuE"
    "oH8XdDs6///I1rVqVGfgyfAgcuiEfW23ShD+Gl6Nvg2vDtqtD3xszLZ2tN8v4paWaApDvj"
    "XtqQKZG8bAnD4CYhmpFonfp4EF+aRWluA47nlydgU9IMJexR4fzutolJ2uQOUdHCZbKLHG"
    "h0QAwy1cRGy1adaaZS0AAUfMmj+bPylJVzggPsxNZFFLeSqTPvtktk9mO0hmg7ENWQID+r"
    "geyexQ2Y3Assg6VBP/3VHVGloe1F63e8RwQn1QD5AUApNlAmOt453u9O9jXo+kv42TvlJQ"
    "V0iuYjzBBLoOOoMLQfOUTQogM++Qx+XgRo5UP4pFpZOZCXhcFo7MHmFBstAgjY7p8Ho0/P"
    "JVC4vVyIZ1uIqYOQdocYP5Z8Vl2UDR/O8iVrIoYvJGRnAooRCu5KC19JA6w8ZEwJ7ChUIy"
    "XtDlUsStUbe4kU4IDpyJ2ksOm7sVmN3ICoOwVE0lIeTIKSW6Yj3lK057QVWzNPs+BVX3yG"
    "pHUqoetX/+mLMFi0HG7jXgODZ7TIwO9GY9OPoIr3GUY+9XVk0CY49h7LbtfkWMWznYEhu/"
    "nFtPdyo99qIzdcG5oeJMblLrx6+q3FS2xqtpTUU6baY05X3QWxeaMpKszkwJ87TSTGnJrN"
    "BMy9DNlaZAWC41k99jOVJT+alWLDWVX4Z7qVm35Po+paa8Zqrf3d1edm7p6m4t2UnrIjvV"
    "rdm3mzuXoC96JxYVlQ1fib28rL/TN2JDSFxzkldX45bSsgqkz76qvqGq+gcSPz4nVWuA0u"
    "WV60B1iqns3+p2K6R/5lWY/0Vb5iUYOxprQIzd3ybApq5XAMi8CgGKtswNBEY0vgNOQ/x+"
    "fXlRcAUhu2RA/kQswFvLNelhw3N9el9PrCUUedR80jPff/BUeAfnw99ZrqMfl8eCAvapQ8"
    "QoYoDj9Urs9stL+Be3Gj3q"
)

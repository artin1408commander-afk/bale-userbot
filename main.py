#!/usr/bin/env python3
"""
Bale Userbot - لاگین ساده با سشن دائمی
فقط برای شماره: +989039865450
مناسب اجرا در Termux
"""

import asyncio
import os
import sys

# شماره ثابت شما (بدون + و بدون صفر اول)
PHONE_NUMBER = "989039865450"
SESSION_FILE = "session.bale"  # فایل سشن در همین پوشه ذخیره می‌شود


async def main():
    print("=" * 50)
    print("  Bale Userbot - لاگین شخصی")
    print("=" * 50)
    print(f"شماره هدف: +{PHONE_NUMBER}")
    print()

    try:
        from aiobale import Client
    except ImportError:
        print("❌ کتابخانه aiobale نصب نیست!")
        print("دستور نصب:")
        print("  pip install aiobale-py")
        sys.exit(1)

    # ساخت کلاینت با شماره ثابت و فایل سشن
    # اگر session.bale وجود داشته باشد و معتبر باشد → مستقیم لاگین
    # اگر نباشد → OTP می‌فرستد و از شما کد می‌پرسد
    client = Client(
        session_file=SESSION_FILE,
        phone_number=PHONE_NUMBER,
    )

    print("⏳ در حال اتصال به سرور بله...")
    print("   (اگر سشن قبلی معتبر باشد، دوباره OTP نمی‌گیرد)")
    print()

    try:
        await client.start()
    except Exception as e:
        print(f"❌ خطا در لاگین: {e}")
        print()
        print("اگر کد OTP اشتباه بود یا منقضی شد، دوباره اجرا کنید.")
        sys.exit(1)

    # اگر به اینجا رسید یعنی لاگین موفق بوده
    me = client.me
    print()
    print("✅ لاگین موفق!")
    print("-" * 40)
    if me:
        name = getattr(me, "full_name", None) or getattr(me, "title", None) or getattr(me, "name", "نامشخص")
        user_id = getattr(me, "id", None) or getattr(me, "user_id", "نامشخص")
        phone = getattr(me, "phone", None) or getattr(me, "phone_number", PHONE_NUMBER)
        print(f"  نام      : {name}")
        print(f"  آیدی     : {user_id}")
        print(f"  شماره    : +{phone}")
    else:
        print("  اطلاعات کاربر دریافت شد (جزئیات در client.me)")
    print("-" * 40)
    print()
    print(f"📁 سشن در فایل ذخیره شد: {SESSION_FILE}")
    print("   دفعات بعد دیگر OTP نمی‌گیرد (تا وقتی سشن معتبر باشد).")
    print()
    print("🎉 بخش لاگین کامل شد. حالا می‌توانید بقیه قابلیت‌ها را اضافه کنید.")
    print()

    # فعلاً فقط لاگین می‌کنیم و خارج می‌شویم
    # برای ادامه کار (مثل دریافت پیام و ... ) بعداً کد اضافه می‌کنیم
    await client.stop()
    print("اتصال بسته شد. خداحافظ!")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⏹️  متوقف شد توسط کاربر.")

from types import MappingProxyType


def make_report(equipment):
    """
    یک گزارش مستقل از equipment می‌سازد.
    - ترتیب سریال‌ها حفظ می‌شود.
    - مقدار هر کلید tuple است، پس قابل تغییر نیست.
    - خود دیکشنری گزارش هم با MappingProxyType فقط‌خواندنی می‌شود.
    """
    return MappingProxyType({
        key: tuple(serials)
        for key, serials in equipment.items()
    })


def diff_reports(before, after):
    """
    برای هر کلید، سریال‌های اضافه‌شده و حذف‌شده را چاپ می‌کند.
    کلیدی که در یکی از گزارش‌ها نباشد، در گزارش دیگر با موجودی خالی در نظر گرفته می‌شود.
    """
    all_keys = sorted(set(before) | set(after))

    for key in all_keys:
        before_serials = set(before.get(key, ()))
        after_serials = set(after.get(key, ()))

        added = sorted(after_serials - before_serials)
        removed = sorted(before_serials - after_serials)

        print(f"{key}:")
        print(f"  added:   {added}")
        print(f"  removed: {removed}")


equipment = {
    ("Lab-A", "sensor"): ["S1", "S2"],
    ("Lab-B", "sensor"): ["S3"],
}

# گزارش درست قبل از تغییرات
report_before = make_report(equipment)

# تغییرات
equipment[("Lab-A", "sensor")].append("S4")
equipment[("Lab-B", "sensor")] = ["S5"]

# گزارش بعد از تغییرات
report_after = make_report(equipment)

print("گزارش قبل:")
for key, serials in report_before.items():
    print(f"  {key}: {serials}")

print("\nگزارش بعد:")
for key, serials in report_after.items():
    print(f"  {key}: {serials}")

print("\nتفاوت گزارش‌ها:")
diff_reports(report_before, report_after)
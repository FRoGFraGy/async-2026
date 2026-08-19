import asyncio
import httpx

SERVER_IP = "172.20.56.253"
PORT = "8080"

SERVER_URL = f"http://{SERVER_IP}:{PORT}"

MY_STUDENT_ID = "6710301049"


async def claim_coupon(client, student_id, attempt):
    try:
        res = await client.post(
            f"{SERVER_URL}/claim",
            json={
                "student_id": student_id
            },
            timeout=5.0
        )

        data = res.json()

        print(
            f"ครั้งที่ {attempt}: "
            f"{data.get('status')} -> "
            f"{data.get('message', data.get('claimed_coupon'))}"
        )

        return data

    except Exception as e:
        print(f"ครั้งที่ {attempt}: เกิดข้อผิดพลาด -> {e}")
        return None


async def hunt_coupons():

    async with httpx.AsyncClient() as client:

        print(f"[{MY_STUDENT_ID}] เริ่มทดสอบ Race Condition...")

        # สร้าง Request หลายตัวพร้อมกัน
        tasks = []

        for attempt in range(1, 11):
            task = asyncio.create_task(
                claim_coupon(
                    client,
                    MY_STUDENT_ID,
                    attempt
                )
            )

            tasks.append(task)

        # รอให้ Request ทั้งหมดทำงานเสร็จ
        results = await asyncio.gather(*tasks)

        print("\n===== ตรวจสอบคูปองของตนเอง =====")

        try:
            res = await client.get(
                f"{SERVER_URL}/my-coupons/{MY_STUDENT_ID}"
            )

            if res.status_code == 200:

                summary = res.json()

                total = summary.get(
                    "total_claimed",
                    0
                )

                coupons = summary.get(
                    "claimed_coupons",
                    []
                )

                print(
                    f"Student ID: {MY_STUDENT_ID}"
                )

                print(
                    f"ได้รับคูปองทั้งหมด: {total} ใบ"
                )

                print(
                    f"คูปอง: {coupons}"
                )

                if total > 2:
                    print(
                        "\n!!! พบความผิดปกติ !!!"
                    )

                    print(
                        f"Server แจกเกิน Limit: "
                        f"{total} ใบ"
                    )

                else:
                    print(
                        "\nServer จำกัดได้ถูกต้อง"
                    )

            else:
                print(
                    f"ดึงข้อมูลไม่สำเร็จ "
                    f"Status Code: {res.status_code}"
                )

        except Exception as e:
            print(
                f"เกิดข้อผิดพลาดในการตรวจสอบ: {e}"
            )

        print("\n===== ตรวจสอบ Summary =====")

        try:
            res = await client.get(
                f"{SERVER_URL}/summary"
            )

            if res.status_code == 200:

                summary_all = res.json()

                remaining_stock = summary_all.get(
                    "remaining_stock",
                    "N/A"
                )

                claims = summary_all.get(
                    "student_claims",
                    {}
                )

                print(
                    f"จำนวนคูปองคงเหลือ: "
                    f"{remaining_stock} ใบ"
                )

                print(
                    "รายการคูปองของแต่ละคน:"
                )

                for sid, coupons in claims.items():

                    print(
                        f"- {sid}: "
                        f"{len(coupons)} ใบ -> "
                        f"{coupons}"
                    )

            else:
                print(
                    f"ดึง Summary ไม่สำเร็จ "
                    f"Status Code: {res.status_code}"
                )

        except Exception as e:
            print(
                f"เกิดข้อผิดพลาดในการดึง Summary: {e}"
            )


if __name__ == "__main__":
    asyncio.run(hunt_coupons())
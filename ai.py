import os
import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Data akun Telegram
data_akun = {
    "name": "Fatkhur",
    "username": "Fatkhurofficial",
    "api_id": "20171354",
    "api_hash": "024149495700d56e0bf20255ae390c60",
    "nomor_telepon": "994704112949",
    "string_sesi": "1ApWapzMBuxRd4Z0ylsgVTEppxWM7oJ8onlgxT-yQDbtRcFyl6e7is0tj50d6j5XAs5rVz6rNzoBBkQ8SjHfd4E9bFu_jNnEq5C6lUlRFFIzQq44Lw0o1FkpswTglFFjsi6IFaU194yk90HE9lmAM50ron4gqBst2zikaJVuQxj1iMq2xkow0FYqH_DmrNSDmxQ4Sq-S9padgxrxX6okpcgBR7GW_FPT6_u0H43Xp0snFYUuofYnPtijgVqZdpDMD5G1B4ADhvJNv3GgilA_6hCRSvDldDwGUvPxWfWW16-cPQUyFMK681iAuc2H79bHM8ZhIs48vzjUm7rDZhhylfVKu30krTeU="
}

# Fungsi untuk mengunduh media satu per satu dan menampilkan status unduhan
async def unduh_media(client, group_id, jumlah_pesan=10):
    try:
        # Dapatkan entitas grup
        entity = await client.get_entity(group_id)

        # Ambil pesan terbaru dari grup
        messages = await client.get_messages(entity, limit=jumlah_pesan)

        # Buat folder penyimpanan jika belum ada
        os.makedirs("downloads", exist_ok=True)

        # Proses setiap pesan untuk mengunduh media
        for index, message in enumerate(messages, start=1):
            if message.media:
                print(f"[{index}/{jumlah_pesan}] Mengunduh media dari pesan ID {message.id}...")
                file_path = await message.download_media(file="downloads/")
                print(f"[{index}/{jumlah_pesan}] ✅ Media berhasil diunduh: {file_path}\n")
            else:
                print(f"[{index}/{jumlah_pesan}] ❌ Tidak ada media dalam pesan ID {message.id}\n")
    except Exception as e:
        print("Error saat mengunduh media:", e)

async def main():
    # Gunakan ID grup privat
    group_id = -1002303030174  # ID grup privat harus dalam format integer

    # Inisialisasi Telegram Client
    api_id = int(data_akun['api_id'])
    api_hash = data_akun['api_hash']
    session_string = data_akun['string_sesi']

    client = TelegramClient(StringSession(session_string), api_id, api_hash)

    # Memulai client
    await client.start()

    # Unduh media dari grup
    await unduh_media(client, group_id, jumlah_pesan=10)

    # Menutup client setelah selesai
    await client.disconnect()

# Jalankan program
if __name__ == "__main__":
    asyncio.run(main())

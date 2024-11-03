# import
import qrcode
from pathlib import Path

# 다운로드 폴더 경로 설정
downloads = Path.home() / "Downloads"

# 입력
data = input("QR코드에 들어갈 정보를 입력해 주십시오. : ") # QR코드에 들어갈 정보 인풋
nameQrcode = input("저장될 QR코드의 이름을 알려주십시오. : ") # 저장될 QR코드 이름 인풋
qrcodeScale = input("QR코드의 크기(사이즈)를 입력해 주십시오 : ") # QR코드 사이즈 인풋

# QR코드 생성
img = qrcode.make(data)

# 저장
filename = downloads / nameQrcode
img.save(
    filename,
    scale=qrcodeScale,
    dark="black",
    light="white"
)
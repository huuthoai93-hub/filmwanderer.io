# Product

<!-- impeccable:product-schema 1 -->

Hồ sơ sản phẩm cho website Film Wanderer (https://huuthoai93-hub.github.io/). Viết theo quy trình `impeccable init`, nội dung do Thoai xác nhận ngày 2026-11-12.

## Platform

web

## Users

- Người dùng của hai ứng dụng FilmDesk và FilmTrail: người chụp film đi từ Google Play, từ trong app (link chính sách, About) hoặc từ link chia sẻ, muốn biết Film Wanderer là ai, tìm đúng app, đọc chính sách quyền riêng tư hoặc liên hệ hỗ trợ.
- Người theo dõi Thoai trên mạng xã hội và các nhóm cộng đồng nhiếp ảnh, có thể chưa dùng app nào, vào để xem Film Wanderer làm gì.
- Người duyệt Google Play cần mở được trang chính sách của từng app.

## Product Purpose

Trang chủ là cửa chung của Film Wanderer: giới thiệu nhà làm app, dẫn tới trang của từng app (FilmDesk, FilmTrail) cùng chính sách quyền riêng tư của mỗi app, và cho một cách liên hệ. Thành công là khách hiểu ngay đây là ứng dụng cho người chụp film, chọn được app phù hợp và tìm được chính sách hoặc email hỗ trợ mà không phải đoán.

## Positioning

Film Wanderer do chính những người chụp ảnh, mê nhiếp ảnh làm ra, nên hiểu người chơi film cần gì. Ứng dụng gọn nhẹ, tiện dụng, không cần dùng mạng nhiều, không cần tài khoản riêng, và tôn trọng dữ liệu của mỗi người: không dùng dữ liệu đó vào việc khác.

Không nói về việc nhà làm app ở Việt Nam.

## Operating Context

- Site tĩnh trên GitHub Pages, sinh ra từ `_build/` bằng `python3 _build/build_all.py` (xem README.md).
- Khách thường mở từ điện thoại (link trong app, link trên mạng xã hội), nên trang phải dùng tốt ở màn hình hẹp.
- FilmDesk: sắp ra mắt trên Google Play. FilmTrail: đang thử nghiệm.

## Capabilities and Constraints

- Đường dẫn cố định, không được đổi: `/filmtrail/privacy/` (dùng trong app FilmTrail và Play Console), `/filmdesk/privacy/`, `/filmdesk/`, `/filmtrail/`, `/vi/`.
- Ngôn ngữ mặc định là tiếng Anh (ở `/`); tiếng Việt ở `/vi/`. FilmDesk có 7 ngôn ngữ (en, vi, de, fr, ja, ko, zh-TW). Mong muốn: FilmTrail cũng hỗ trợ đủ 7 ngôn ngữ như FilmDesk (chưa làm).
- Email hỗ trợ: filmwanderer.support@gmail.com. Trang nhà phát triển trên Google Play: xem `_build/site.json`.

## Brand Commitments

- Tên: "Film Wanderer". Hai app: "FilmDesk", "FilmTrail".
- Logo của từng app phải dùng **nguyên bản** thiết kế của Thoai, kể cả dòng chữ nhỏ bên dưới, không cắt, không vẽ lại, không đổi màu:
  - FilmDesk: chim cút ngậm cuộn phim, chữ "FilmDesk" (Film đen, Desk đỏ), dòng nhỏ "Index & Archive app". File: `filmdesk/assets/brand/filmdesk-logo.webp`.
  - FilmTrail: chim cút cầm ống nhòm và la bàn, chữ "FilmTrail" (Film đen, Trail xanh lá), dòng nhỏ "Metering - Tracking - Tagging App". File: `filmtrail/assets/brand/filmtrail-logo.webp`.
- Ở chế độ tối, logo đặt trong khung chữ nhật nền trắng ngà (màu nền gốc của ảnh), bo tròn 4 góc. Cách khác được Thoai cho phép: đổi màu phần đen của logo. Chưa dùng cách này.
- Font mono (JetBrains Mono ExtraBold cho tiêu đề) đang dùng chung ở cả ba phần site.

## Evidence on Hand

- Ảnh logo gốc của hai app (Thoai gửi 2026-11-12), linh vật FilmTrail `filmtrail/assets/mascot.webp`, ảnh chụp màn hình FilmDesk `filmdesk/assets/shots/`.
- Chưa có: đánh giá của người dùng, số lượt tải, bài báo. Không được bịa những thứ này.

## Product Principles

1. Gọn và rõ: khách tìm được app, chính sách và email trong vài giây, nhất là trên điện thoại.
2. Tôn trọng người dùng: không theo dõi, không quảng cáo, không thu thập gì trên site; lời hứa về dữ liệu phải đúng với app.
3. Nói như người chụp film nói với người chụp film, không như doanh nghiệp.
4. Mỗi app giữ bản sắc riêng; trang chủ là chỗ chung, không phải trang con của một app.

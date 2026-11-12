# Film Wanderer

Website của Film Wanderer, phục vụ bằng GitHub Pages tại https://huuthoai93-hub.github.io/

| Đường dẫn | Nội dung |
|---|---|
| `/` , `/vi/` | Trang chủ Film Wanderer |
| `/filmdesk/` | FilmDesk: landing page + `privacy/`, 7 ngôn ngữ |
| `/filmtrail/` | FilmTrail: landing page + `privacy/`, tiếng Anh và tiếng Việt (`vi/`) |

Liên hệ: filmwanderer.support@gmail.com

## Sửa nội dung

Các trang HTML được sinh ra từ `_build/` (Jekyll bỏ qua thư mục bắt đầu bằng `_`, nên `_build` không bị đăng lên). Đừng sửa tay file `index.html`.

- Chữ: `_build/home/i18n.json`, `_build/filmdesk/i18n/`, `_build/filmtrail/i18n/` (mỗi ngôn ngữ một file JSON).
- Bố cục: các file `.html` trong `_build/<phần>/`.
- Địa chỉ gốc, email, link Google Play: `_build/site.json`.

Sửa xong, chạy ở thư mục gốc repo rồi commit cả file sinh ra:

```
python3 _build/build_all.py
```

FilmDesk được chuyển nguyên từ repo `filmdesk-public-info`. Repo cũ vẫn đăng ở địa chỉ cũ cho tới khi được thay bằng trang chuyển hướng.

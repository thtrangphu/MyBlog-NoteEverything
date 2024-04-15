# MyBlog

### HTTP 0.9
Chỉ có GET
Không có Header
Respond luôn là HTML
  
### HTTP 1.0 (GET, POST, HEAD) - 1991
Hỗ trợ nhiều loại respond hơn: img, video, html, plain text, ... (hypermedia not hypertext :))) 
Connectionless: Mỗi request phải mỗi connection riêng, respond xong thì close kết nối.
Stateless: Không lưu lại thông tin cần thiết của mỗi lần request, nên mỗi request phải gửi lại => tốn băng thông

 Three-way Handshake 
![image](https://github.com/thtrangphu/MyBlog-NoteEverything/assets/76843467/e4fb9732-9150-465d-b835-c5b8b57aec10)

### HTTP 1.1 - 1999
Có thêm method: PUT, PATCH, OPTIONS, DELETE
Hỗ trợ connect liên tục, client muốn đóng thì gửi header close connection.
Pipeline: có thể gửi nhiều request mà không cần chờ server respond
Nhưng khi có nhiều request nhưng 1 trong số đó nặng, thì các thằng còn lại phải chờ.

### SPDY - 2009 (Google)
Giảm độ trễ để tăng hiệu suất mạng (tăng nhiều so với tăng băng thông). Sau đó gg không muốn có 2 tiêu chuẩn nên hợp nhất thành HTTP, ngừng dùng SPDY và ra đời HTTP/2 
> Độ trễ là mất bao lâu để dữ liệu di chuyển giữa nguồn và đích (được đo bằng mili giây) 
> Băng thông là lượng dữ liệu được truyền mỗi giây (bit trên giây).
SPDY không thay thế HTTP,

### HTTP/2
![image](https://github.com/thtrangphu/MyBlog-NoteEverything/assets/76843467/85e4e0b5-ee3e-4afb-a5cd-0c8b82c153aa)
Binary protocol: Giúp dễ parse nhưng người k dễ đọc

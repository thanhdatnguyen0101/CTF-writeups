
## A. Thông tin chung (General Information)


* **Tên đội thi** : Fr4gm3nt3d P4ckets
* **Tên bài tập** : Stalker#1 
* **Mảng (Category)** : OSINT
* **Độ khó** : Easy 

---

## B. Phân tích đề bài (Analysis)

### 1. Tiếp cận ban đầu
* Mục tiêu của ta là lấy càng nhiều thông tin càng tốt, đầu tiên theo thói quen mình sẽ search thử tên "Lux1dus" và tadaa kết quả hiện ra 
(images/Screenshot 2026-01-22 003054.png)
* Mình sẽ tạm thời để 1 tab ở đó, và chuyển sang đường link trong discord như đề đã cho (Hint đầu tiên) 
(images/Screenshot 2026-01-22 002945.png)

### Bước 2: Các bước thực hiện (Step-by-step)
Mô tả chi tiết quá trình bypass hoặc tấn công:

1.  Thử payload đầu tiên để kiểm tra phản hồi.
2.  Phát hiện bộ lọc (filter) chặn từ khóa `UNION`.
3.  Bypass bộ lọc bằng cách sử dụng `UnIoN` (viết hoa thường xen kẽ).

**Payload sử dụng:**
```text
admin' OR 1=1 --

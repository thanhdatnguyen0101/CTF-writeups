
## A. Thông tin chung (General Information)


* **Tên đội thi** : Fr4gm3nt3d P4ckets
* **Tên bài tập** : In Plain Sight!
* **Mảng (Category)** : OSINT
* **Độ khó** : khum bit

---

## B. Phân tích đề bài (Analysis)

* Search thử "Lux1dus" ta được các kết quả tìm kiếm sau 
![image alt](https://github.com/thanhdatnguyen0101/CTF-writeups/blob/2b8f9cce7502a6cf6d9b5936d02c55dceb8be482/images/searchgg.png)
* Nhấp vào kết quả đầu tiên sẽ hiện ra trang cá nhân của người được nhắc đến trong đề, ta thấy bài đăng đầu tiên có nhắc hint khá lộ liễu 
![image alt](https://github.com/thanhdatnguyen0101/CTF-writeups/blob/2b8f9cce7502a6cf6d9b5936d02c55dceb8be482/images/hint2.png) ấn vào phần bình luận sẽ có 1 link canva, nhấn vào sẽ ra 500 hình giống nhau, giờ nhiệm vụ của ta là tìm 1 "con số" chính xác và sẽ có flag ở tấm hình của "con số" đó.
* Trở về lại phần tìm kiếm lúc nãy có 1 group fb, ta thử vào đó tìm hint :) 
![image alt](https://github.com/thanhdatnguyen0101/CTF-writeups/blob/2b8f9cce7502a6cf6d9b5936d02c55dceb8be482/images/groupfb.png)
* Nhấp vào cuộc đối thoại, ta sẽ thấy 1 tọa độ
![image alt](https://github.com/thanhdatnguyen0101/CTF-writeups/blob/4cc77bdeec95ec15fb89a245692821c660df761d/images/toado.png)
* Thử tìm nó trên map thì ta được 
![image alt](https://github.com/thanhdatnguyen0101/CTF-writeups/blob/4cc77bdeec95ec15fb89a245692821c660df761d/images/toadomap.png)
* Quay lại phần bài đăng lúc nãy, kéo xuống phần bình luận sẽ có nhắc đến 1 hint =)) 
![image alt](https://github.com/thanhdatnguyen0101/CTF-writeups/blob/4cc77bdeec95ec15fb89a245692821c660df761d/images/hinttenduong.png)
* Và tên đường từ tọa độ ta tìm được là "đường số 223", nhập thử số 223 vào link canva 500 hình lúc nãy thì ta ra được flag, ez peazy
![image alt](https://github.com/thanhdatnguyen0101/CTF-writeups/blob/4cc77bdeec95ec15fb89a245692821c660df761d/images/canva223.png)
* Lật hình lại 1 chút cho dễ nhìn 
![image alt](https://github.com/thanhdatnguyen0101/CTF-writeups/blob/4cc77bdeec95ec15fb89a245692821c660df761d/images/flag2.png)

## C. Kết quả (The Flag)
### CKGS1{pr3tty_w3ll_h1dd3n_huh_wink_wink_:)}

###### Thấy hay thì cho mình xin 1 star :_)


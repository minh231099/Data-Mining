# Chapter 5
# Logic và Suy luận: Các quy tắc

**Tables of contents**  
- [**5.1 Giới thiệu**](#51-giới-thiệu)  
	- **5.1.1 Logic và quy tắc**  
	- **5.1.2 Quy tắc trong Mạng Ngữ Nghĩa**  
	- 

---  

# 5.1 Giới thiệu
## 5.1.1 Logic và quy tắc
Từ một quan điểm trừu tượng, chủ để ở chương 2 và 4 liên quan đến việc *biểu diễn tri thức*: tri thức về nội dung của các tài nguyên web và tri thức về các khái niệm trong một lĩnh vực diễn đạt ngôn ngữ và các mối quan hệ của chúng (bản thể học).  
Biển diễn tri thức đã được nghiên cứu từ rất lâu trước cả sự xuất hiện của World Wide Web, trong lĩnh vực của trí tuệ nhân tạo và trước đó trong triết học. Thực tế, nó có thể được bắt nguồn từ thời Hi Lạp cổ đại; Aristoteles được coi là cha để của logic. Logic vẫn là một nền tảng của biểu diễn tri thức, cụ thể là *logic vị từ*. Một vài lý do về sự phổ biến và tầm quan trọng của logic:  
- Nó cung cấp một ngôn ngữ bậc cao mà tri thức có thể được biểu đạt một cách minh bạch. Và nó có năng lực biểu đạt cao.  
- Nó có một ngữ nghĩa chính thức dễ hiểu, chỉ định một ý nghĩa rõ ràng cho các phát biểu logic.  
- Có một khái niệm chính xác về hệ quả logic, xác định xem một phát biểu có tuân theo ngữ nghĩa từ một tập hợp các phát biểu (tiên đề) khác hay không. Trên thực tế, động lực chính ban đầu của logic là nghiên cứu các quy luật khách quan của hệ quả logic.  
- Tồn tại các hệ thống chứng minh có thể tự động lấy ra các phát biểu theo cú pháp từ một hợp các tiên đề.  
- Tồn tại các hệ thống chứng minh mà hệ quả logic ngữ nghĩa trùng với dẫn xuất cú pháp trong hệ thống chứng minh. Các hệ thống chứng minh phải hợp lý (tất cả các câu lệnh dẫn xuất tuân theo ngữ nghĩa từ tiên đề) và hoàn chỉnh (tất cả các hệ quả logic của tiên đề có thể được suy ra trong hệ thống chứng minh).  
- Logic vị từ là duy nhất theo nghĩa mà các hệ thống chứng minh hợp lý và hoàn chỉnh tồn tại. Logic với khả năng biểu đạt cao hơn không có các hệ thống chứng minh như vậy.  
- Do sự tồn tại của các hệ thống chứng minh, có thể truy tìm những minh chứng dẫn tới một hệ quả logic hợp lý. Trong trường hợp này, logic có thể cung cấp những giải đáp cho các câu trả lời.  

Các ngỗn ngữ của RDF và các cấu hình OWL2 (khác với OWL2 Full) có thể được xem như là chuyên hóa của logic vị từ.  
Một lý do cho sự tồn tại của các ngôn ngữ chuyên biệt như vậy là chúng cung cấp cú pháp phù hợp với mục đích sử dụng (trong trường hợp của ta là ngôn ngữ web dựa trên các thẻ). Với cách biện minh khác là chúng xác định tập con hợp lý của logic. Như đã đề cập, phải đánh đổi giữa khả năng biểu đạt và độ phức tạp tính toán của các logic cụ thể: ngôn ngữ càng có khả năng biểu đạt, các hệ thống chứng minh càng kém. Như đã nói, phần lớp các biến thể OWL tương đồng nhau ở logic mô tả, một tập con của logic vị từ mà các hệ thống chứng minh hiệu quả tồn tại.  
Một tập con khác của logic vị từ đi kèm với những hệ thống chứng minh hiệu quả gồm *hệ thống quy tắc - rule systems*(cách gọi khác là *logic Horn* hay *chương trình logic xác định - definite logic programs*). Một quy tắc có dạng:  
*A<sub>1</sub>,...A<sub>n</sub> &rarr; B*  
với A<sub>*i*</sub> và B là các công thức tiên đề. Thực tế, có hai cách trực quan để đọc những quy tắc như này:  
1. Nếu A<sub>1</sub>, ..., A<sub>n</sub> là đúng (true) thì B cũng là đúng (true). Các quy tắc với cách giải thích này được gọi là *quy tắc suy diễn - deductive rule*.  
2. Nếu các điều kiện A<sub>1</sub>, ..., A<sub>n</sub> là đúng (true), thì thực hiện hành động B. Các quy tắc với cách giải thích này được gọi là *quy tắc phản ứng - reactive rule*.  
Cả hai góc nhìn đều có những ứng dụng quan trọng. Tuy nhiên, trong chương này ta sẽ tiếp cận theo hướng quy tắc suy diễn. Ta sẽ nghiên cứu ngôn ngữ và các truy vấn có khả năng một người có thể hỏi, cũng như những câu trả lời phù hợp. Cùng đó, ta sẽ phác thảo hoạt động của một cơ chế chứng minh có thể trả lại các câu trả lời như vậy.  
Điều thú vị là logic mô tả và logic Horn trực giao với nhau theo nghĩa là cả hai đều không phải tập con của tập còn lại. Ví dụ, không thể định nghĩa một lớp *vợ chồng hạnh phúc* là những người đã kết hôn với bạn thân nhất của họ trong logic mô tả. Nhưng tri thức này lại có thể dễ dàng biểu diễn sử dụng các quy tắc:  
&emsp;*married(X, Y), bestFriend(X, Y) &rarr; happySpouse(X)  
Mặt khác, các quy tắc không thể (trong trường hợp tổng quát) khẳng định phủ định hay phần bù của các lớp; thông tin rời rạc hay liên hợp (ví dụ, một người là nam hay nữ); hoặc định lượng hiện sinh (ví dụ, tất cả mọi người đều có một người cha). Ngược lại, OWL cho phép biểu diễn phần bù và liên hợp của các lớp và một số hình thức định lượng hiện sinh.  
Chúng ta sẽ tập trung sang một loại quy tắc khác. Một ví dụ đơn giản, giả sử một người bán hàng online muốn đưa ra một ưu đãi đặc biệt vào ngày sinh của khác hàng. Một các đơn giản để biểu diễn chiến lược kinh doanh này với các quy tắc như sau:  
&emsp;R1: Nếu sinh nhật thì ưu đãi đặc biệt.  
&emsp;R2: Nếu không phải sinh nhật thì không ưu đãi đặc biệt.  
Giải pháp này hoạt động đúng trong các trường hợp đã biết trước ngày sinh. Nhưng tưởng tượng một khách hàng từ chối cung cấp ngày sinh của anh ấy vì bảo mật cá nhân. Trong trường hợp đó, các quy tắc trước đó không thể được áp dụng vì các tiên đề của chúng ta không nắm rõ. Để nắm bắt tình huống àny, ta cần viết gì đó kiểu:  
&emsp;R1 : Nếu sinh nhật thì ưu đãi đặc biệt.  
&emsp;R2': Nếu không biết ngày sinh thì không ưu đãi đặc biệt.  
Tuy nhiên tiên đề của quy tắc R2' không nằm trong khả năng biểu đạt của logic vị từ. Vậy nên ta cần một loại hệ thống qu tắc mới. Lưu ý rằng giải pháp với quy tắc R1 và R2 hoạt động trong trường hợp chúng ta đã có đầy đủ thông tin về tình hình (có phải ngày sinh nhật hay không). Hệ thống quy tắc mới sẽ được áp dụng trong trường hợp thông tin sẵn có không đầy đủ.  
Logic vị từ và các trường hợp đặc biệt của nó là *đơn điệu (monotonic)* theo nghĩa sau, nếu một kết luận có thể được đưa ra, nó vẫn có giá trị ngay cả khi tri thức mới trở nên khả dụng. Nhưng nếu như R2' được áp dụng để dẫn xuất "không ưu đãi đặc biệt", thì kết luận này có thể trở nên không hợp lệ nếu sinh nhật của khách hàng được biết sau đó và nó xảy ra trùng với ngày mua. Hành động này là *không đơn điệu* vì việc bổ sung thông tin mới làm mất đi một hệ quả. Ví vậy, chúng ta nói về các quy tắc không đơn điệu để phân biệt chúng với quy tắc đơn điệu (một trường hợp đặc biệt của logic vị từ). Trong chương nay ta nói đế cả quy tắc đơn điệu và không đơn điệu.  

## 5.1.2 Quy tắc trong Mạng Ngữ Nghĩa

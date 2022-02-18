# Chapter 5
# Logic và Suy luận: Các quy tắc

**Tables of contents**  
- [**5.1 Giới thiệu**](#51-giới-thiệu)  
	- **5.1.1 Logic và quy tắc**  
	- **5.1.2 Quy tắc trong Mạng Ngữ Nghĩa**  
- [**5.2 Ví dụ về quy tắc đơn điệu: Các mối quan hệ gia đình - Family relationships**](#52-Ví-dụ-về-quy-tắc-đơn-điệu-các-mối-quan-hệ-gia-đình-Family-relationships)  
- [**5.3 Quy tắc đơn điệu: Cú pháp**](#53-quy-tắc-đơn-điệu-cú-pháp)  
	- **5.3.1 Quy tắc**  
	- **5.3.2 Chân lý**  
	- **5.3.3 Chương trình logic**  
- [**5.4 Quy tắc đơn điện: Ngữ Nghĩa**](#54-quy-tắc-đơn-điệu-ngữ-nghĩa)  
	- **5.4.1 Ngữ nghĩa logic vị từ**  
	- **5.4.2 Ngữ nghĩa mô hình Least Herbrand**  
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
với A<sub>*i*</sub> và B là các biểu thức tiên đề. Thực tế, có hai cách trực quan để đọc những quy tắc như này:  
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
Công nghệ quy tắc đã tồn tại trong nhiều thập kỷ, đã được sử dụng rộng rãi trong thực tế và đã có sự trưởng thành đáng kể. Và việc triển khai này đã dẫn đến nhiều cách tiếp cận khác nhau. Do đó, việc chuẩn hóa lĩnh vực này trong ngữ cảnh của trang web (ngữ nghĩa) trở nên khó khăn hơn rất nhiều. W3C đã phát triển tiêu chuẩn trao đổi quy tắc (RIF - Rule Interchange Format). Điều quan trọng là phải hiểu nó khác RDF và OWL như thế nào: trong khi OWL và RDF là những ngôn ngữ dùng để biểu thị trực tiếp kiến thức, RIF được thiết kế chủ yếu để trao đổi các quy tắc trên các ứng dụng khác nhau. Ví dụ, một cửa hàng trực tuyến muốn thực hiện các chính sách về giá cả, hoàn tiền và bảo mật của họ, điều này được thể hiện bằng cách sử dụng các quy tắc có thể truy cập được đối với những agent thông minh. Cách tiếp cận của Mạng Ngữ Nghĩa là thể hiện kiến thức theo cách mà máy có thể truy cập được bằng cách sử dụng một trong các ngôn ngữ web mà ta đã đề cập.  
Do mục đích cơ bản là hoạt động như một định dạng trao đổi giữa các hệ thống quy tắc khác nhau, RIF kết hợp nhiều tính năng của chúng và khá phức tạp. Do đó, có một số nghi ngờ về việc liệu nó có thực sự được sử dụng rộng rãi như là ngôn ngữ chính để diễn đạt tri thức hay không. Thật vậy, những người muốn phát triển hệ thống quy tắc cho Mạng Ngữ Nghĩa có nhiều lựa chọn thay thế khác nhau:  
- Các quy tắc đối với RDF có thể được diễn tả một cách đơn giản sử dụng các cấu trúc SPARQL; một đề xuất hiện nay theo hướng này đó là SPIN.  
- Những người muốn sử dụng các quy tắc với sự xuất hiện của những cấu trúc ngữ nghĩa phong phú có thể sử dụng SWRL, kết hợp các chức năng OWL DL với các loại quy tắc nhất định.  
- Những người muốn mô hình hóa theo OWL nhưng sử dụng công nghệ quy tắc cho các mục đích triển khai có thể sử dụng OWL2 RL.  

Sự đa dạng của các phương pháp tiếp cậ này là lý do vì sao chương này trông rất khác so với các chương trước, dựa trên một hoặc một nhóm các tiêu chuẩn rất ổn định và được chất nhận rộng rãi. RIF là một bước trong hướng đi này, nhưng nó chưa ở mức độ đồng thuận và chấp nhận của cộng đồng. Do đó, chưng trình bày các ý tưởng ở mức độ chung và trình bày một số cách tiếp cận cụ thể.  

# Chapter Overview
- 5.2 cung cấp một ví dụ sử dụng các quy tắc đơn điệu (nghĩa là của tập con của logic vị từ được gọi là logic Horn).  
- 5.3 và 5.4 mô tả cú phát và các ngữ nghĩa của logic Horn.  
- 5.5 thảo luận về mối quan hệ giữa OWL2 RL và các quy tắc.  
- 5.6 trình bày họ phương ngữ RIF (family of RIF dialect), tập trung vào các ngôn ngữ dựa trên logic.  
- 5.7 mô tả về SWRL như một cách kết hợp các quy tắc với logic mô tả.  
- 5.8 mô tả ngắn ngọn về cách các quy tắc có thể được mô hình hóa bằng cachs ử dụng các cấu trúc SPARQL.  
- 5.9 mô tả cú pháp của các quy tắc không đơn điệu và phần 5.10 trình bày một ví dụ về các quy tắc không đơn điệu.  
- Cuối cùng, 5.11 mô tả ngắn ngọn về RuleML, một hoạt động liên tục để đánh dấu quy tắc trên web với một chương trình mở và thử nghiệm có thể đưa vào các tiêu chuẩn mới trong tương lai.  

# 5.2 Ví dụ về quy tắc đơn điệu: Các mối quan hệ gia đình - Family relationships
Hình dung một cơ sở dữ liệu của các chân lý về vài quan hệ gia đình. Giả sử rằng cơ sở dữ liệu chứa các chân lý về các *vị từ cơ sở - base predicate* sau:  
*&emsp;mother(X, Y)&emsp;X là mẹ của Y*  
*&emsp;father(X, Y)&emsp;X là bố của Y*  
*&emsp;male(X)&emsp;X là nam*  
*&emsp;female(X)&emsp;X là nữ*  

Sau đó, ta có thể suy ra các mối quan hệ xa hơn bằng cách sử dụng quy tắc thích hợp. Đầu tiên, ta có thể định nghĩa một vị từ *parent*: một phụ huynh nghĩa là một bố hoặc một mẹ. 
*&emsp;mother(X, Y) &rarr; parent(X, Y)*  
*&emsp;father(X, Y) &rarr; parent(X, Y)*  
Sau đó ta có thể định nghĩa một người anh em là một người có giới tính nam và có chung một phụ huynh:  
*&emsp;male(X), parent(P, X), parent(P, Y), notSame(X, Y) &rarr; brother(X, Y)*  
Vị từ *notSame* nghĩa là không tương đương; ta giả định những chân lý đó được lưu giữ trong cơ sở dữ liệu. Tuy nhiên, mỗi hệ thống logic thực tế đều đưa ra những cách thuận tiện để thể hiện sự bình đẳng và bất bình đẳng, nhưng ta chọn giải pháp trừu tượng.  
Tương tự, *sister* được định nghĩa như sau:  
*&emsp;female(X), parent(P, X), parent(P, Y), notSame(X, Y) &rarr; sister(X, Y)*  
Một người chú là một người anh em của một phụ huynh:  
*&emsp;brother(X, P), parent(P, Y) &rarr; uncle(X, Y)*  
Một người bà là mẹ của một phụ huynh:  
*&emsp;mother(X, Y), parent(P, Y) &rarr; grandmother(X, Y)*  
Tổ tiên là phụ huỳnh hoặc tổ tiên của phụ huynh:  
*&emsp;parent(X, Y) &rarr; ancestor(X, Y)*  
*&emsp;ancestor(X, P), parent(P, Y) &rarr; ancestor(X, Y)*  

# 5.3 Quy tắc đơn điệu: Cú pháp
Ta sẽ coi như một quy tắc đơn giản phát biểu rằng tất cả những khách hàng trung thành có tuổi lớn hơn 60 sẽ được nhận một ưu đãi đặc biệt:  
&emsp**loyalCustomer(X), age(X) > 60 &rarr; discount(X)**  
Ta sẽ phân biệt một số thành phần của quy tắc:  
- biến (variable), là một ô nhớ cho các giá trị: X  
- hằng số (constant), là các giá trị cố định: 60  
- vị từ (predicate), dùng để liên kết các đối tượng: loyalCustomer, >  
- phương thức tượng trưng (function symbol), tượng trưng cho một giá trị, khi được áp dụng cho một đối số nhất định: age  

Trong trường hợp không có phương thức tượng trưng nào được sử dụng, ta nói là logic bất phương thức.  

## 5.3.1 Quy tắc
Một quy tắc có dạng: *B<sub>1</sub>, ..., B<sub>n</sub> &rarr; A*  
Có *A, B<sub>1</sub>, ..., B<sub>n</sub>* là các biểu thức tiên đề. *A* là *đầu* (head) của quy tắc và *B<sub>1</sub>, ..., B<sub>n</sub>* là các *cơ sở* (permise) của quy tắc. Tập hợp *{B<sub>1</sub>, ..., B<sub>n</sub>}* được gọi là *cơ quan* (body) của các quy tắc.  
Các dấu phẩy trong phần cơ quan của quy tắc được đọc theo liên từ: Nếu *B<sub>1</sub>* và *B<sub>2</sub>* và ... và *B<sub>n</sub>* là đúng (true), thì A cũng là đúng (true).  
Ví dụ:  
&emsp;*loyalCustomer(X), age(X) > 60 &rarr; discount(X)*  
Quy tắc này áp dụng cho tất cả các khách hàng: nếu một khách hàng là khách hàng trung thành và trên 60 tuổi, thì người đó sẽ nhận được ưu đãi. Nói các khác, biến X là ám chỉ định lượng chung (sử dụng &forall;X). Nói chung, tất cả các biến xuất hiện trong một quy tắc đều ám chỉ định lượng chung.  
Tóm lại, một quy tắc *r*:
*B<sub>1</sub>, ..., B<sub>n</sub> &rarr; A*  
được hiểu theo biểu thức sau, ký hiện là *pl(r)*:  
&emsp;*&forall;X<sub>1</sub>...&forallX<sub>k</sub>((B<sub>1</sub> &and; ... &and; B<sub>n</sub>) &rarr; A)*  
hoặc tương đương với:  
&emsp;*&forall;X<sub>1</sub>...&forallX<sub>k</sub>((&not;B<sub>1</sub> &or; ... &or; &not;B<sub>n</sub>) &or; A)*  
với *X<sub>1</sub>, ..., X<sub>k</sub>* là tất cả các biến xuất hiện trong *A, B<sub>1</sub>, ..., B<sub>n</sub>*.  

## 5.3.2 Chân lý
Một chân lý là một biểu thức tiên đề, như là *loyalCustomer*(a345678), nói rằng khách hàng có ID a345678 là trung thành. Các biến của một chân lý ám chỉ định lượng chung.  

## 5.3.3 Chương trình logic
Một chương trình logic *P* là một tập hữu hạn các chân ly và các quy tắc. Bản dịch logic vị từ của nó *pl(P)* là một tập hợp các logic vị từ diễn giải về các quy tắc và các chân lý trong *P*.  

## 5.3.4 Các mục tiêu
Một mục tiêu (goal) là một truy vấn *G* được yêu cầu cho một chương trình logic. Nó có dạng:  
&emsp;*B<sub>1</sub>, ..., B<sub>n</sub> &rarr;*  
Nếu *n* = 0 ta sẽ có mục tiêu rỗng (empty goal).  
Nhiệm vụ tiếp theo là diễn giải các mục tiêu theo logic vị từ. Sử dụng những ý tưởng ta đã phát triển (dấu phẩy nghĩa là kết hợp, định lượng chung), ta sẽ nhận được cách diễn giải sau:  
&emsp;*forall;X<sub>1</sub>...&forall;X<sub>k</sub>(&not;B<sub>1</sub> &or; ... &or; &not;B<sub</sub>)*  
biểu thức này tượng tự với *pl(r)*, chỉ khác là phần đầu của quy tắc *A* được bỏ qua.  
Một diễn giải tương tự trong logic vị từ là:  
&emsp;*&not;&exist;X<sub>1</sub>...&exist;X<sub>k</sub>(B<sub>1</sub> &and; ... &and; B<sub>n</sub>)*  
với *X<sub>1</sub>, ..., X<sub>k</sub>* là tất cả các biến xuất hiện trong *B<sub>1</sub>, ..., B<sub>n</sub>*. Ta sẽ giải thích gắn gọn biểu thức này. Ta sử ta biết  
&emsp;*p(a)*  
và ta có một mục tiêu
&emsp;*p(X) &rarr;*  
Thật ra, ta muốn biết liệu có một giá trị *p* là đúng hay không. Ta một đợi một câu trả lời khẳng định từ chân lý *p(a)*. Do đó *p(X)* được định lượng hiện sinh. Nhưng sẽ ra sao nếu ta làm biểu thức phủ định? Lời giải thích là ta sử dụng một kỹ thuật chứng minh từ toán học được gọi là *chứng minh bằng mâu thuẫn - proof by contradiction*. Kỹ thuật này chứng minh rằng một phát biểu B kéo theo phát biểu A bằng cách giả sử rằng A là sai và dễn đến một sự mâu thuẫn khi kết hợp với B. Khi đó B kéo theo A.  
Trong chương trình logic ta chứng minh rằng một mục tiêu có thể được trả lời khẳng định bằng phủ định mục tiêu và chứng minh rằng ta nhận được sự mâu thuẫn bằng cách sử dụng chương trình logic. Ví dụ, đưa ra một chương trình logic  
*p(a)*  
và mục tiêu  
*&not;&exist;Xp(X)*  
ta sẽ có được một mâu thuẫn logic: biểu thức thứ hai nói rằng một có phần tử nào có thuộc tính *p*, nhưng biểu thức đầu teien nói rằng giá trị *a* có thuộc tính *p*. Do đó *p(a)* kéo theo *&exist;Xp(X)*.  

# 5.4 Quy tắc đơn điện: Ngữ Nghĩa
## 5.4.1 Ngữ nghĩa logic vị từ
Một cách để trả lời các truy vấn là sử dụng các diễn dịch logic vị từ của các quy tắc, chân lý và truy vấn, đồng thời sử dụng ngữ nghĩa đã nắm rõ của logic vị từ. Chính xác hơn, cho một chương trình logic *P* và một truy vấn  
&emsp;*B<sub>1</sub>, ..., B<sub>n</sub> &rarr;*  
với các biến *X<sub>1</sub>, ..., X<sub>k</sub>*, ta sẽ đưa ra trả lời khẳng định khi và chỉ khi:  
&emsp;*pl(P) &vDash; &exist;X<sub>k</sub>(B<sub>1</sub> &and; ... &and; B<sub>n</sub>)*&emsp;(1)  
hoặc tương đương, nếu:  
&emsp;*pl(P) &union; {&not;&exist;X<sub>1</sub> ... &exist;X<sub>k</sub>(B<sub>1</sub> &and; ... &and; B<sub>n</sub>)}* là không thỏa mãn &emsp;(2)  

Nói cách khác, ta đưa một câu trả lời khẳng định nếu đặc tả logic vị từ của chương trình *P*, cùng với cách đặc tả logic vị từ của truy vấn là không thỏa mãn (mâu thuẫn).  
các thành phần của ngôn ngữ logic (ký hiệu) có thể có bất kỳ ý nghĩa nào mà ta thích. Một mô hình logic vị từ, *A*, mang một ý nghĩa nhất định. Đặc biệt, nó bao gồm:  
- *miền dom(A)*, một tập không rỗng của các đối tượng có các biểu thức tạo ra các phát biểu,  
- một phần tử từ miền cho mỗi hằng số,  
- một hàm cụ thể trên *dom(A)* cho mọi hàm tượng trưng,  
- một mối quan hệ cụ thể trên *dom(A)* cho mọi vị từ.  

Khi ký hiệu *=* được sử dụng để chỉ sự cân bằng (tức là, cách diễn giải của nó là cố định), ta nói về *logic Horn cân bằng - Horn logic with equality*. Các ý nghĩa của các liên kết logic &not;, &or;, &and;, &rarr;, &forall;, &exist; được sao định theo ý nghĩa trực quan của chúng: phủ (not), tuyển (or), hội (and), hàm ý (implies), với tất cả (for all), tồn tại (there is). Bằng cách này, chúng ta xác định khi nào một công thức đúng trong mô hình *A*, được ký hiệu là &vDash; &#632;.  
Một biểu thức &#632; theo sau một tập biểu thức *M* nếu &#632; là đúng (true) với tất cả các mô hình *A* mà *M* là đúng (nghĩa là, mọi công thức trong *M* đều đúng trong *A*)  
Giờ đây ta có thể giải thích (1) và (2). Bất kể ta diễn giải các hằng số, vị từ và các hàm tượng trưng xuất hiện trong *P* và truy vấn ra sao, một khi đặc tả logic vị từ của *P* là đúng thì &exist;X<sub>k</sub>(B<sub>1</sub> &and; ... &and; B<sub>n</sub>) cũng là đúng. Do đó, có nhiều giá trị cho các biến X<sub>1</sub>, ..., X<sub>k</sub> mà tất cả các biểu thức tiên đề B<sub>i</sub> là đúng.  
Ví dụ, giả sử *P* là một chương trình  
&emsp;*p(a)*  
&emsp;*p(X) &rarr; q(X)*  

Xem xét truy vấn  
&emsp;*q(X) &rarr;*  

Rõ ràng, *q(a)* theo sau *pl(P)*. Do đó, &exist;*X<sub>q</sub>* theo sao *pl(P)*, suy ra *pl(P) &union; {&not;&exist;X<sub>q</sub>(X)} là không thỏa mãn, và ta đưa ra một câu trả lời khẳng định. Nhưng nếu ta xem xét truy vấn  
&emsp;*q(b) &rarr;*  
thì ta sẽ nhận một câu trả lời phủ định vì *q(b)* không theo sau *pl(P)*.  

## 5.4.2 Ngữ nghĩa mô hình Least Herbrand



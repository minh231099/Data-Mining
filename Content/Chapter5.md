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
	- **5.4.3 Các minh chứng sàn và tham số hóa**  
- [**5.5 OWL2 RL: Logic mô tả đáp ứng các quy tắc**](#55-owl2-rl-logic-mô-tả-đáp-ứng-các-quy-tắc)  
- [**5.6 Định dạng trao đổi quy tắc: RIF**](#56-định-dạng-trao-đổi-quy-tắc-rif)  
	- **5.6.1 Tổng quát**  
	- **5.6.2 RIF-BLD**  
	- **5.6.3 Khả năng tương thích với RDF và OWL**  
	- **5.6.4 OWL2 trong RIF**  
- [**5.7 Ngôn Ngữ Quy Tắc Mạng Ngữ Nghĩa (Semantic Web Rules Language - SWRL)**](#57-ngôn-ngữ-quy-tắc-mạng-ngữ-nghĩa-semantic-web-rules-language-swrl)  
- [**5.8 Quy tắc trong SPARQL: SPIN**](#58-quy-tắc-trong-sparql-spin)  
- [**5.9 Quy Tắc Phi Đơn Điệu: Động Lực và Cú Pháp**](#59-quy-tắc-phi-đơn-điệu-động-lực-và-cú-pháp)  
	- **5.9.1 Informal Discussion**  
	- **5.9.2 Đặc tả của Cú pháp**  
- [**5.10 Ví dụ về Quy tắc Phi đơn điệu: Giao dịch môi giới**](#510-ví-dụ-về-quy-tắc-phi-đơn-điệu-giao-dịch-môi-giới)  
	- **5.10.1 Hình thức hóa các yêu cầu của Carlos**  
	- **5.10.2 Mô tả về các căn hộ có sẵn**  
	- **5.10.3 Chọn một căn hộ**  
- [**5.11 Ngôn ngữ đánh dấu quy tắc - Rule Markup Language (RuleML)](#511-ngôn-ngữ-đánh-dấu-quy-tắc-rule-markup-language-ruleml)  
- [**5.12 Tổng kết**](#512-tổng-kết)  

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
&emsp;*&forall;X<sub>1</sub>...&forall;X<sub>k</sub>(&not;B<sub>1</sub> &or; ... &or; &not;B<sub>n</sub>)*  
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

Khi ký hiệu *=* được sử dụng để chỉ sự cân bằng (tức là, cách diễn giải của nó là cố định), ta nói về *logic Horn cân bằng - Horn logic with equality*. Các ý nghĩa của các liên kết logic &not;, &or;, &and;, &rarr;, &forall;, &exist; được sao định theo ý nghĩa trực quan của chúng: phủ (not), tuyển (or), hội (and), hàm ý (implies), với tất cả (for all), tồn tại (there is). Bằng cách này, chúng ta xác định khi nào một công thức đúng trong mô hình *A*, được ký hiệu là  *A* &vDash; &#632;.  
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
Một kiểu ngữ nghĩa khsac cho các chương trình logic, ngữ nghĩa mô hình least Herbrand yêu cầu nhiều phương pháp kỹ thuật hơn, và được mô tả trong những sách logic tiêu chuẩn.  

## 5.4.3 Các minh chứng sàn và tham số hóa
Chúng ta mới chỉ tập trung vào các câu hỏi có/không. Tuy nhiên, những câu trả lời như vậy không hẳn là tối ưu. Giả sử ta có một chân lý  
&emsp;*p(a)*  
và truy vấn  
&emsp;*p(X) &rarr;*  
Câu trả lời có là đúng nhưng không thỏa đáng. Nó giống một câu đùa khi được hỏi "Bạn có biết mấy giờ không?" và nhìn vào đồng hồ rồi trả lời "Có". Trong ví dụ của chúng ta, câu trả lời mong muốn là một sự thế chỗ  
&emsp;*{X/a}*  
thứ cung cấp một thuyết minh cho *X*, tạo ra một câu trả lời tích cực. Hằng số *a* được gọi là *minh chứng sàn - ground witness*. Cho những chân lý  
&emsp;*p(a)*  
&emsp;*p(b)*  
có hai minh chứng sàn cho cùng truy vấn: *a* và *b*. Hoặc tương đương, ta cần trả về các thay thế:  
&emsp;*{X/a}*  
&emsp;*{X/b}*  
Trong khi có giá trị, minh chứng sàn không thường xuyên là câu trả lời tối ưu. Xem xét chương trình logic  
&emsp;*add(X, 0, X)*  
&emsp;*add(X, Y, Z) &rarr; add(X, s(Y), s(Z))*  
Chương trình này tính toán bổ sung, nếu ta đọc *s* là "chức năng kế thừa" trả về giá trị là giá trị của đối số của nó cộng với 1. Tham số thứ ba của *add* tính tổng hai đối số đầu tiên của nó. Xem xét truy vấn  
&emsp;*add(X, s<sup>8</sup>(0), Z) &rarr;*  
Các minh chứng sàn có thể được xác định bởi các sự thay thế  
&emsp;*{X/0, Z/s<sup>8</sup>(0)}*  
&emsp;*{X/s(0), Z/s<sup>9</sup>(0)}*  
&emsp;*{X/s(s(0)), Z/s<sup>10</sup>(0)}*  
&emsp;...  

Tuy nhiên, minh chứng tham số hóa *Z = s<sup>8</sup>(X)* là cách chung nhất để minh chứng truy vấn hiện sinh  
&emsp;*&exist;X&exist;Z add(X, s<sup>8</sup>(0), Z)*  
vì nó đại diện cho chân lý *add(X, s<sup>8</sup>(0), Z)* là đúng khi mà giá trị của *Z* bằng với giá trị của X khi cộng thêm 8.  
Việc tính toán hầu hết các minh chứng nói chung là mục đính chính của hệ thống chứng minh, được gọi là độ phân giải SLD, việc trình bày hệ thống đó nằm ngoài phạm vi của cuốn sách này.  

# 5.5 OWL2 RL: Logic mô tả đáp ứng các quy tắc
Như ở phần bắt đầu của chương này, logic Horn và các logic mô tả là trực giao. Để cố gắng đạt được sự tích hợp của chúng vào một khuôn khổ, cách tiếp cận đơn giản nhất là xem xét sự giao nhau của cả hai logic học, tức là phần của một ngôn ngữ có thể được dịch theo cách bảo toàn ngữa nghĩa sang ngôn ngữ kia và ngược lại. Về bản chất OWL2 RL tìm cách nắm bắt mảnh của OWL này. Ưu điểm của phương phá này bao gồm:  
- Từ quan điểm của người thiết kế mô hình, có quyền tự do sử dụng OWL hoặc các quy tắc (và các công cụ và phương pháp liên quan) cho mục đích thiết kế mô hình, tùy thuộc vào kinh nghiệm và sở thích của người thiết kế mô hình.  
- Từ quan điểm triển khai, có thể sử dụng trình suy luận logic mô tả hoặc hệ thống quy tắc quy nạp. Do đó, có thể lập mô hình bằng cách sử dụng một framework, chẳng hạn như OWL, và sử dụng một công cụ suy luận từ framework kia, chẳng hạn như các quy tắc. Tính năng này cung cấp thêm tính linh hoạt và đảm bảo khả năng tương thích với nhiều loại công cụ.  

Trong đoạn còn lại của phần này, chúng ta sẽ chỉ ra có bao nhiêu cấu trúc của RDF Schema và OWL RL có thể được diễn đạt ở logic Horn, và thảo luận về vài cấu trúc không thể diễn đạt được. Ta sẽ tập trung và các cấu trúc cơ bản làm nổi bật sự kết nối và khác nhau giữa các quy tắc và logic mô tả.  
Ta sẽ bắt đầu với RDF và RDF Schema. Một bộ ba có dạng *(a, P, b) trong RDF có thể biểu diễn là một chân lý  
&emsp;*P(a, b)*  
Tương tự, một instance được khai bái với dạng *type(a, C)*, phát biểu rằng *a* là một instance của lớp *C*, có thể được biểu diễn dưới dạng  
&emsp;*C(a)*  
Với lớp C là lớp con của D nó có thể dễ dàng biểu diễn dưới dạng  
&emsp;*C(X) &rarr; D(X)*  
tương tự với thuộc tính con. Cuối cùng, rằng buộc miền và phạm vi cũng có thể biểu diễn với logic Horn. Ví dụ, quy tắc dưới đây phát biểu rằng *C* là miền của thuộc tính *P*:  
&emsp;*P(X, Y) &rarr; C(X)*  
Giờ đối với OWL, *equivalentClass(C, D)* có thể được biểu diễn với một cặp quy tắc  
&emsp;*C(X) &rarr; D(X)*  
&emsp;*D(X) &rarr; C(X)*  
và tượng tự với *equivalentProperty*. Tính bắc cầu của một thuộc tính *P* có thể dễ ràng biểu diễn như sau  
&emsp;*P(X, Y), P(Y, Z) &rarr; P(X, Z)*  
Với các toán tử Boolean. Ta có thể phát biểu rằng giao điểm của lớp *C<sub>1</sub>* và *C<sub>2</sub>* là một lớp con của *D* như sau:  
&emsp;*C<sub>1</sub>(X), C<sub>2</sub>(X) &rarr; D(X)*  
Ngược lại, phát biểu rằng *C* là tập con của giao điểm giữa *D<sub>1</sub>* và *D<sub>2</sub>* như sau:  
&emsp;*C(X) &rarr; D<sub>1</sub>(X)*  
&emsp;*C(X) &rarr; D<sub>2</sub>(X)*  
Với liên hợp, ta có thể diễn đạt rằng liên hợp của *C<sub>1</sub>* và *C<sub>2</sub>* là tập con của D sử dụng cặp luật sau:  
&emsp;*C<sub>1</sub>(X) &rarr; D(X)*  
&emsp;*C<sub>2</sub>(X) &rarr; D(X)*  
Tuy nhiên, chiều ngược lại nằm ngoài khả năng diễn đạt của logic Horn. Để diễn đạt chân lý *C* là lớp con của liên hợp *D<sub>1</sub>* và *D<sub>2</sub>* cần một sự phân biệt trong phần đầu của quy tắc tương ứng, thứ không khả dụng trong logic Horn. Lưu ý rằng có những trường hợp có thể dịch được. Ví dụ, khi *D<sub>1</sub>* là lớp con của *D<sub>2</sub>*, khi đó quy tắc *C(X) &rarr; D<sub>2</sub>(X)* là phù hợp để diễn đạt rằng *C* là tập con của liên hợp *D<sub>1</sub>* và *D<sub>2</sub>*. Vấn đề là không có một bản dịch nào có thể hoạt động trong mọi trường hợp.  
Cuối cùng ta sẽ thảo luận ngắn gọn về các dạng của ràng buộc trong OWL. Phát biểu OWL  
```Turtle
:C	rdfs:subClassOf	[ rdf:type	owl:Restriction];
					owl:onProperty	:P;
					owl:allValuesFrom	:D ].
```  
có thể được mô tả với logic Horn như sau:  
&emsp;*C(X), P(X, Y) &rarr; D(Y)*  

Tuy hiên, chiều ngược lại thì không thể biểu diễn. Và phát biểu OWL  
```Turtle
[ rdf:type	owl:Restrictin;
	owl:onProperty	:P;
	owl:someValuesFrom	:D ] rdfs:subClassOf	:C.
```  

có thể được mô tả với logic Horn như sau:  
&emsp;*P(X, Y), D(Y) &rarr; C(X)*  
Chiều ngược lại cũng không thể diễn đạt được.  
Tuy nhiên, ràng buộc về số lượng và phần bù của lớp không thể diễn tả được trong logic Horn.  

# 5.6 Định dạng trao đổi quy tắc: RIF
## 5.6.1 Tổng quát
Kỹ thuật quy tắc đã tồn tại hàng thập kỉ, và có nhiều loại (ví dụ như  action rule, first order rule, chương trình logic). Như một hệ quả, mục tiêu của W3C RIF Working Group không phải phát triểu một ngôn ngữ quy tắc mới thứ phù hợp với tất cả nhu cầu, mà là tập trung vào sự trao đổi giữa các hệ thống quy tắc khác nhau (hiện tại hoặc trong tương lai) trên web. Các tiếp cận được thực hiện là phát triển một nhóm ngôn ngữ, được gọi là *phương ngữ - dialect*; RIF xác định có hai lại phương ngữ:  
1. *Logic dựa trên phương ngữ*. Có nghĩa là bao gồm các ngôn ngữ quy tắc dựa trên một dạng logic; ví dụ, các phương pháp tiếp cận của first-order logic và các loại chương trình logic với các cách hiểu khác nhau về phủ định (answer-set programming, well-founded semantics, etc.). Các phương ngữ cụ thể được phát triển cho đến nay thuộc về nhánh này là:  
	- *RIF Core*, phù hợp với function-free Horn logic;  
	- *RIF Basic Logic Dialect (BLD)*, phù hợp với logic Horn cân bằng.  

2 *Quy tắc với các hành động*. Chúng bao gồm các hệ thống chế xuất và các quy tắc phản ứng. Phương ngữ cụ thể được phát triển cho đến nay trong nhánh này là:  
	- *Phương Ngữ Quy Tắc Chế Xuất - Production Rule Dialect (RIF-PRD)*  

Họ RIF được thiết kế để vừa *đồng nhất* vừa *có khả năng mở rộng*. Đồng nhất đạt được bằng cách mong đợi cú pháp và ngữ nghĩa của tất cả các phương ngữ RIF chia sẻ các nguyên tắc cơ bản. Khả năng mở rộng đề cập đến khả năng của các phương ngữ trong tương lại được phát triển và thêm vào họ RIF. Với phương diện dựa trên logic, RIF Working Group tiến hành hỗ trợ tính đồng nhất và khả năng mở rồng bằng cách phát triển Framework for logic Dialects (RIF-FLD) cho phép một người chỉ định các ngôn ngữ quy tắc khác nhau bằng cách khởi tạo các tham số khác nhau của phương pháp.  

## 5.6.2 RIF-BLD
RDF Basic Logic Dialect về cơ bản là tương ứng với logic Horn cân bằng công với  
- kiểu dữ liệu và built ins, và  
- khung (frame)  

RIF-BLD như những biến thể RIF khác, nó được dữ kiến sẽ hỗ trợ một tập hợp thống nhất các kiểu dữ liệu, vị từ và chức năng thường được sử dụng. Tập hợp này gồm kiểu dữ liệu (như là *integer, boolean, string, date*), vị từ "built-in" (như là *numeric-greater-than, starts-with, date-less-than*), và các phương thức (như là numeric-subtract, replace, hours-from-time) khác nhau trên các loại dữ liệu.  
Ví dụ, giả tử ta muốn biểu đạt một quy tắc phát biểu rằng một diễn viên là một siêu sao điện ảnh nếu anh ấy đóng nhiều hơn ba bô phim thành công, được sản xuất trong thời gian ít nhất là năm năm. Và một phim được coi là thành công nếu nó nhận được sự công nhận của giới phê tình (giả sử, xếp hạng cao hơn 8/10) hoặc đạt được doanh thu cao (tạo ra hơn 100 triệu đô tiền bán vé). Các quy tắc này được đánh giá dựa trên tập dữ liệu DBpedia.  
Các quy tắc này được biểu diễn trong RIF-BLD như sau:  
```RIF-BLD
Document(
	Prefix(func <http://www.w3.org/2007/rif-builtin-function#>
	Prefix(pred <http://www.w3.org/2007/rif-builtin-predicate#>
	Prefix(rdfs <http://www.w3.org/2000/01/rdf-schema#>
	Prefix(imdbrel <http://example.com/imdbrelation#>
	Prefix(dbpedia <http://dbpedia.org/ontology/>
	Prefix(ibdbrel <http://example.com/ibdbrelation#>

Group(
	Forall ?Actor ?Film ?Year (
		If And( dbpedia:starring(?Film ?Actor)
				dbpeida:dateOfFilm(?Film ?Year)
		Then dbpedia:starredInYear(?Film ?Actor ?Year)
	)

	Forall ?Actor (
		If ( Exists ?Film1 ?Film2 ?Film3 ?Year1 ?Year2 ?Year3
			And (	dbpedia:starredInYear(?Film1 ?Actor ?Year1)
					dbpedia:starredInYear(?Film2 ?Actor ?Year2)
					dbpedia:starredInYear(?Film3 ?Actor ?Year3)
					External ( pred:numeric-greater-than(
						External(func:numeric-subtract ?Year1 ?Year3) 5)))
			dbpedia:successful(?Film1)
			dbpedia:successful(?Film2)
			dbpedia:successful(?Film3)
			External (pred:literal-not-identical(?Film1 ?Film2))
			External (pred:literal-not-identical(?Film1 ?Film3))
			External (pred:literal-not-identical(?Film2 ?Film3))
				)
			Then dbpedia:movieStar(?Actor)
	)
	Forall ?Film (
		If Or (
				External(pred:numeric-greater-than(
					dbpedia:criticalRating(?Film 8))
				External(pred:numeric-greater-than(
					bpedia:boxOfficeGross(?Film) 100000000)))
		hen dbpedia:successful(?Film)
		)
	)
)

```  
Ví dụ này mô tả lợi ích của kiểu dữ liệu và các built in. Lưu ý rằng tác dụng của *External* là áp dụng các vị từ built in. *Group* dùng để kết hợp một số lượng các quy tắc lại với nhau.  
Cú pháp của RIF khá đơn giản, mặc dù khá dài dòng (tất nhiên, cũng có một cú pháp dựa trên XML để hỗ trợ trao đổi giữa các hệ thống quy tắc). Tên các biến bắt đầu bởi một dấu hỏi. Và các ký tự =, #, và ## được sử dụng để thể hiện tương đương, tư cách thành viên và quan hệ lớp con.  
Việc sử dụng *frame* đã có từ lâu trong những ngôn ngữ hướng đối tượng và biểu diễn tri thức, đồng thời cũng nổi bật trong lĩnh vực ngôn ngữ quy tắc (Ví dụ: F-Logic). Ý tưởng cơ bản là biểu diễn các đối tượng dưới dạng *frame* và thuộc tính của chúng là *slot*.  
Ví dụ, ta muốn có một lớp professor với các slot như là name, office, phone, department, etc. Thông tin như vậy được biểu diễn trong RIF-BLD sử dụng ký hiệu  
&emsp; oid[slot1 -> value1 ... slotn -> valuen]  

## 5.6.3 Khả năng tương thích với RDF và OWL  
Một tính năng chính của RIF là nó tương thích với các tiêu chuẩn RDF và OWL. Do đó, một người có thể suy luận với sự kết hợp của các tài liệu RIF, RDF và OWL. Do đó RIF tạo điều kiện thuận lợi cho việc trao đổi không chỉ các quy tắc mà còn cả đồ thị RDF và/hoặc các tiên đề OWL.  
Ý tưởng cơ bản của sự kết hợp RIF với RDF là diễn tả các bộ ba RDF sử dụng biểu thức frame RIF; một bộ ba *s p o* được biển diễn thành s[p -> o]. Đặc tả ngữ nghĩa sao cho bộ ba thỏa mãn nếu biểu thức frame RIF tương ứng cũng vậy. Ví dụ: nếu bộ ba RDF  
```
ex:GoneWithTheWind	exFilmYear	ex:1939  
```  
là đúng (true), vậy thì chân lý RIF  
Cho một quy tắc RIF (phát biểu rằng Hollywood Production Code đã có từ năm 1930 đến năm 1968)  
```RIF
Group (
	Forall ?Film (
		If And(	?Film[ex:Year -> ?Year]
				External(pred:dateGreaterThan(?Year 1930))
				External(pred:dateGreaterThan(1968 ?Year)))
		Then ?Film[ex:HollywoodProductionCode -> ex:True]
	)
)
```  
có thể kết luận rằng  
ex:GoneWithTheWind[ex:HollywoodProductionCOde -> ex:True]  
cũng như bô ba RDF tương ứng.  
Các kỹ thuật tương tự được sử dụng để đạt được khả năng tương thích giữa OWL và RIF. Các tính năng chính là:  
- Ngữ nghĩa của OWL và RIF tương thích;  
- Ta có thể suy luận ra kết luận từ sự kết hợp nhất định của các tiên đề OWL và tri thức RIF; và  
- OWL2 RL có thể được triển khai trong RIF.  

## 5.6.4 OWL2 trong RIF
OWL2 RL được mô tả một phần bởi một tập hợp các quy tắc bậc nhất có thể tạo thành cơ sở cho việc triển khai sử dụng công nghệ quy tắc. Để kích hoạt khả năng tương tác giữa các hệ thống quy tắc và bản thể học OWL2 RL, tiền đề này có thể được mô tả bằng cách sử dụng RIF (BLD, thực sự ngay cả trong các quy tắc Core đơn giản hơn).  
Quy tắc OWL2 RL có thể được phân và bốn loại (rời rạc): quy tắc mẫu bộ ba, quy tắc không nhất quán, quy tắc danh sách và quy tắc kiểu dữ liệu.  
  
  
**Triple Pattern Rules - Quy Tắc Mẫu Bộ Ba** &emsp; Quy tắc này tạo ra các bộ ba RDF nhất định từ sự kết hợp của các mẫu bộ ba RDF. Việc dịch các quy tắc này sang RIF (sử dụng biểu thức Frame) rất đơn giản bằng cách sử dụng các quy tắc của biểu mẫu:  
```RIF
Group(
	Forall ?V1 ... ?Vn(
		s[p->o] :- And(s1[p1->o] ... sn[pn->on)
	)
)
```  
  
**Inconsistency Rules - Quy Tắc Không Nhất Quán**&emsp; Các quy tắc như vậy chỉ ra sự mâu thuẫn trong biểu đồ RDF ban đầu (tất nhiên là với tri thức OWL hiện có). Các quy tắc này có thể được biểu diễn dễ dàng trong RIF dưới dạng các quy tắc có kết luận rif:error, một ký hiệu vị từ trong không gian tên RIF có thể được sử dụng để thể hiện sự không nhất quán. Ví dụ, một sự mâu thuẫn xảy ra khi hai vị từ đã được khai báo là rời rạc, nhưng lại kết nối các thực thể giống nhau. Điều này có thể được thể hiện bằng RIF như sau:  
```RIF
Group(
	Forall ?P1 ?P2 ?X ?Y(
		rif:error :- And(
			?P1[owl:propertyDisjointWith ?P2] ?X[?P1 -> ?Y] ?X[?P2 -> ?Y]
		)
	)
)
```  
  
**List Rules - Quy Tắc Danh Sách**&emsp;Một số lượng các quy tắc OWL2 RL liên quan đến việc xử lý các biểu thức OWL bao gồm danh sách RDF (ví dụ: owl:AllDierence). Có thể có hai cách tiếp cận để diễn đạt các quy tắc này trong RIF. Người ta có thể sử dụng các quy tắc đệ quy để duyệt qua đồ thị RDF tại thời điểm chạy, tạo ra một biểu diễn thống nhất. Hoặc ta có thể thực hiện phương pháp tiền xử lý trong đó các quy tắc được khởi tạo trực tiếp cho cách danh sách thực sự xảy ra trong biểu đồ RDF đầu vào, điều này có thể hoạt động tốt hơn trong thực tế.  
  
**Datatype Rules - Quy Tắc Kiểu Dữ Liệu**&emsp;Các quy tắc này cung cấp kiểm tra kiểu và kiểm tra bình đẳng/bất bình đẳng giá trị cho các ký tự được gắn trong các kiểu dữ liệu được hộ trợ. Ví dụ: các quy tắc như vậy có thể dẫn xuất owl:sameAs tăng gấp ba lần cho các ký tự có cùng giá trị trong kiểu dữ liệu (ví dụ: 1 và 1.0) hoặc không nhất quán nếu một ký tự được chỉ định là một phiên bản của kiểu dữ liệu nhưng giá trị của nó nằm ngoài không gia giá trị và kiểu dữ liệu đó. Bản dịhc sang các quy tắc RIF khá đơn giản.  

# 5.7 Ngôn Ngữ Quy Tắc Mạng Ngữ Nghĩa (Semantic Web Rules Language - SWRL)  
SWRL là một giải pháp ngôn ngữ Mạng Ngữ Nghĩa kết hợp OWL DL với logic Horn bất chức năng và được viết sử dụng Unary/Binary Datalog RuleML. Do đó nó cho phép các quy tắc giống như Horn được kết hợp với bản thể học OWL DL.  
Một quy tắc trong SWRL có dạng  
&emsp;*B<sub>1</sub>, ..., B<sub>n</sub> &rarr; A<sub>1</sub>, ..., A<sub>m</sub>*  
với dấu phẩy thể hiện sự kết hợp và *A<sub>1</sub>, ..., A<sub>m</sub>, B<sub>1</sub>, ..., B<sub>n</sub>* có thể có dạng C(x), P(x, y), sameAs(x, y) hoặc differentFrom(x, y) trong đó C là mô tả OWL, P là thuộc tính OWL và x, y là các biến trong Datalog, các cá thể OWL hoặc giá trị dữ liệu OWL.  
Nếu phần đầu của quy tắc có nhiều hơn một tiên đề (nếu đó là một tổ hợp của các tiên đề không có biến chung), quy tắc có thể được chuyển đổi thành một bộ quy tắc tương đương với một tiên đề ở phần đầu một cách đơn giản.  
Sự phức tạp chính của ngôn ngữ SWRL bắt nguồn từ thực tế là các biểu thức OWL tùy ý, chẳng hạn như các ràng buộc, có thể xuất hiện trong phần đầu hoặc phần nội dung của quy tắc. Tính năng này bổ sung khả năng biểu đạt đáng kể cho OWL, nhưng với phải trả giá bằng sự không xác thực; nghĩa là, không thể có công cụ suy luận nào đưa ra kết luận chính xác giống như ngữ nghĩa SWRL.  
So sánh với OWL2 RL, SWRL nằm ở đầu kia của việc tích hợp logic mô tả và các quy tắc bất chức năng. Trong trường hợp OWL2 RL sử dụng một cách tiếp cận rất thận trọng, tìm cách kết hợp các ưu điểm của cả hai ngôn ngữ trong ngôn ngữ con chung của chúng, SWRL thực hiện một cách tiếp cận theo chủ nghĩa tối đa hơn và hợp nhất các khả năng diễn đạt tương ứng của chúng. Từ góc độ thực tế, thách thức là xác định các ngôn ngữ con của SWRL để tìm ra sự cân bằng phù hợp giữa khả năng biểu đạt và khả năng xử lý tính toán. Một ứng cử viên cho ngôn ngữ con như vậy là phần mở rộng của OWL DL với các quy tắc DL-safe, trong đó mọi biến phải xuất hiện trong môn tiên đề logic không mô tả trong phần nội dung quy tắc.  

# 5.8 Quy tắc trong SPARQL: SPIN
Các quy tắc được biểu diễn trong SPARQL sử dụng tính năng CONSTRUCT của nó. Ví dụ, quy tắc  
&emsp;*grandparent(X, Z) &larr; parent(Y, Z), parent(X, Y)*  
được biểu diễn như sau  
```SPARQL
CONSTRUCT{
	?X grandParent ?Z.
} WHERE {
	?Y parent ?Z.
	?X parent ?Y.
}
```  
Đề xuất gần đây SPIN coi đây là một điểm khởi đầu để đề xuất ngôn ngữ mô hình hóa qua SPARQ:  
- Nó sử dụng các ý tưởng của mô hình hướng đối tượng trong việc liên kết các quy tắc với các lớp; do đó các quy tắc có thể đại diện cho hành vi của lớp đó và có thể không tồn tại một mình (mặc dù các quy tắc chung cũng có thể được định nghĩa).  
- Nó thể hiện các quy tắc bằng SPARQL CONADING, DELETE và INSERT và các ràng buộc bằng cách sử dụng cấu trúc SPARQL ASK.  
- Nó cung cấp cơ chế trừu tượng hóa cho các quy tắc sử dụng Template, về bản chất, nó đóng gói các truy vấn có chức năng như một cơ chế để xây dựng các quy tắc cấp cao hơn (các truy vấn SPARQL phức tạp) bên trên các quy tắc đơn giản.  
Như một bằng chứng về khái niệm, các quy tắc OWL2 RL đã được thể hiện trong SPIN. Ví dụ, quy tắc  
&emsp;*C<sub>2</sub>(X) &larr; C<sub>1</sub>(X), equivalentClass(C<sub>1</sub>, C<sub>2</sub>)*  
có thể được biểu diễn trong SPARQL như sau:  
```SPARQL
CONSTRUCT {
	?X a ?C2.
} WHERE {
	?X a ?C1.
	?C1 equivalent ?C2.
}
```  
và sau đó được khởi tạo dưới dạng spin:rule cho lớp owl:Thing; điều này sẽ cho phép quy tắc được áp dụng cho tất cả các trường hợp có thể. Cần lưu ý rằng SPARQL, và do SPIN, là một ngôn ngữ quy tắc không phải hệ thống quy tắc được triển khai; ví dụ, CONADING chỉ thể hiện một bước suy luận (từ đồ thị RDF này sang đồ thị RDF khác). Một hệ thống quy tắc trên SPARQL (ví dụ: một công cụ suy luận SPIN) sẽ cần, một trong nhiều điều, chạy CONSTRUCT lặp đi lặp lại và để kiểm kiểm soát đệ quy trong trường hợp quy tắc đệ quy.  

# 5.9 Quy Tắc Phi Đơn Điệu: Động Lực và Cú Pháp
## 5.9.1 Informal Discussion
Giờ ta sẽ sang các hệ thống quy tắc phi đơn điệu. Đến nay, một khi tiên đề của một quy tắc được chứng minh, quy tắc có thể được áp dụng và phần đầu của nó được chứng minh, quy tắc có thể được áp dụng và phần đuầ của nó có thể rút ra như một kết luận. Trong các hệ thống quy tắc phi đơn điệu, một quy tắc có thể không được áp dụng ngay cả khi tất cả các tiên đề đã biết vì chúng ta phải xem ét các chuỗi suy luận trái ngược nhau. Nói chung, các quy tắc mà chúng ta xem xét từ bây giờ được gọi là khả thi vì chúng có thể bị đánh bại bởi các quy tắc khác. Để cho phép xung đột giữa các quy tắc, các biểu thức tiên đề bị phủ đỉnh có thể xảy ra trong phần đầu và phần nội dung của các quy tắc. Ví dụ, ta có thể viết  
&emsp;*p(X) &rarr; q(X)*  
&emsp;*r(X) &rarr; &not;q(X)*  

Để phân biệt giữa các quy tắc khả vi và các quy tắc chuẩn, đơn điệu, chúng ta sử dụng một mũi tên khác:  
&emsp;*p(X) &rArr; q(X)*  
&emsp;*r(X) &rArr; &not;q(X)*  

Trong ví dụ này, đưa ra các chân lý  
&emsp;*p(a)*  
&emsp;*r(a)*  
ta không kết luận *q(a)* hay *&not;q(a)*. Đó là một ví dụ điển hình của hai quy tắc chặn nhau. Xung đột này có thể được giải quyết bằng cách sử dụng các ưu tiên giữa các quy tắc. Giả sử chúng ta đã biết rằng bằng cách nào đó các quy tắc đầu tiên mạnh hơn quy tắc thứ hai; thì chúng ta thực sự có thể suy ra *q(a)*.  
Các ưu tiên phát sinh tự nhiên trong thực tế và có thể dựa trên các nguyên tắc khác nhau:  
- Nguồn của một quy tắc có thể đáng tin cậy hơn nguồn của quy tắc thứ hai hoặc có thẩm quyền cao hơn. Ví dụ, luật liên bang ưu tiên luật tiểu bang. Và trong quản trị kinh doanh, quản lý cấp cao có nhiều quyền hạn hơn quản lý cấp trung.  
- Một quy tắc có thể được ưu tiên hơn một quy tắc khác vì nó mới hơn.  
- Một quy tắc có thể được ưu tiên hơn một quy tắc khác vì nó cụ thể hơn. Ví dụ điển hình là quy tắc chung với một số ngoại lệ; trong những trường hợp như vậy, các ngoại lệ mạnh hơn quy tắc chung.  

Tính cụ thể thường có thể được tính toán dựa trên các quy tắc đã cho, nhưng hai nguyên tắc còn lại không thể được xác định từ phương thức logic. Do đó, chúng ta trừu tượng hóa nguyên tắc ưu tiên cụ thể và giả định sự tồn tại của quan hệ ưu tiên bên ngoài trên tập hợp các quy tắc. Để diễn đạt mối quan hệ về mặt cú pháp, chúng ta mở rộng cú pháp quy tắc để bao gồm một nhãn duy nhất. Ví dụ,  
&emsp;*r<sub>1</sub>: p(X) &rArr; q(X)*  
&emsp;*r<sub>2</sub>: r(X) &rArr; &not;q(X)*  
Và ta có thể viết *r<sub>1</sub> > r<sub>2</sub>* để xác định rằng *r<sub>1</sub>* mạnh hơn *r<sub>2</sub>*.  
Ta không áp đặt nhiều điều kiện cho >. Nó thậm chí không yêu cầu các quy tắc tạo thành một trật tự hoàn trình. Chúng ta chỉ yêu cầu quan hệ ưu tiên là mạch hở. Tức là không thể có chu trình dạng như:    
&emsp;*r<sub>1</sub> > r<sub>2</sub> > ... > r<sub>n</sub> > r<sub>1</sub>*  

Lưu ý rằng các ưu tiên nhằm giải quyết xung đột giữa các quy tắc cạnh tranh. Trong trường hợp đơn giản, hai quy tắc chỉ cạnh tranh nhau nếu phần đầu của một quy tắc là phủ định của phần đầu quy tắc kia. Nhưng trong các ứng dụng, thường xảy ra trường hợp khi một vị từ *p* được dẫn xuất, một vì từ khác bị loại trừ khỏi việc nắm giữ. Ví dụ, một nhà tư vấn đầu tư có thể đưa ra các khuyến nghị của mình về ba mức độ rủi ro mà các nhà đâu tư sẵn sàng chấp nhận: thấp, trung bình và cao. Mỗi nhà đầu tư chỉ được phép nắm giữa một mức độ rủi ro tại bất kỳ thời điểm nào. Về mặt ký thuật những tình huống này được mô hình hóa bằng cách duy trì một tập xung đột *C(L)* cho mỗi một trực nghĩa *L*. *C(L)* luôn chứa phủ định của *L* nhưng nó có thể chứa nhiều ngữ nghĩa hơn.  


## 5.9.2 Đặc tả của Cú pháp
Một quy tắc *khả thi* có dạng:  
&emsp;*r: L<sub>1</sub>, ..., L<sub>n</sub> &rArr; L*  
với *r* là nhãn, {L<sub>1</sub>, ..., L<sub>n</sub>} là phần thân (hoặc cơ sở), và L là phần đầu của quy tắc. *L, L<sub>1</sub>, ..., L<sub>n</sub>* là trực nghĩa khẳng định hay phủ định (một trực nghĩa là một biểu thức tiên đề *p(t<sub>1</sub>, ..., t<sub>m</sub>)* hoặc *&not;p(t<sub>1</sub>, ..., t<sub>m</sub>)*). Không có một phương thức tượng trưng nào xuất hiện trong quy tắc. Đôi khi ta biểu đạt phần đầu của một quy tắc là *head(r)*, và phần thân là *body(r)*. Hơi lạm dụng ký hiệu nhưng đôi khi ta sử dụng nhãn *r* để chỉ toàn bộ quy tắc.  
Một phương trình logic khả vi là một bộ ba *(F, R, >) bao gồm tập *F* các dữ liệu, một tập hữu hạn *R* các quy tắc và một quay hệ nhị phân xoay chiều *>* trên R (chính xác là tập các cặp *r > r'* mà *r* và *r'* là các nhãn của các quy tắc trong *R*)  

# 5.10 Ví dụ về Quy tắc Phi đơn điệu: Giao dịch môi giới
Ví dụ này sẽ cho ta thấy các các quy tắc có thể được sử dụng trong một ứng dụng thương mai điện tử (lý tưởng nhất sẽ là chạy trên Semantic Web). Giao dịch môi giới diễn ra thông qua một bên thứ ba độc lập, nhà môi giới (broker). Nhà môi giới đưa ra yêu cầu của người mua và khả năng của người bán phù hợp và đề xuất một giao dịch trong đó cả hai bên đều có thể hài lòng với giao dịch.  
Như một ứng dụng cụ thể, chúng ta sẽ thảo luận về việc thuê căn hộ, một hoạt động phổ biến tường tẻ nhạt và tốn giời gian. Các dịch vụ web phù hợp có thể giảm bớt công sức đáng kể. Chúng ta bắt đầu bằng cách trình bày các yêu cầu của người thêu tiềm năng.  
Carlos đang tìm kiếm một ăn hộ ít nhất 45m2 với ít nhất hai phòng ngủ. Nếu nó ở tầng ba hoặc cao hơn, ngôi nhà cần có thang máy. Và cho phép cả thú nuôi.  
Carlos sẵn sàng trả 300 đô cho một căn hộ rộng 45m2 ở trung tâm và 250 đô cho một căn tương tự ở ngoại ô. Thêm vào đó, anh ấy sẵn sàng trả thêm 5 đô cho mỗi một m2 cho một căn hộ lớn hơn, và 2 đô cho mỗi m2 vườn.  
Anh ấy không thể trả quá 400 đô. Nếu được đưa ra lựa chọn, anh ấy sẽ chọn lựa chọn rẻ nhất. Ưu tiên thứ hai của anh ấy là có một khu vườn; ưu tiên thấp nhất là không gian bổ sung.  

## 5.10.1 Hình thức quá yêu cầu của Carlos

Ta sẽ sử dụng những vị từ sau để mô tả thuộc tính của căn hộ:  
&emsp;*apartment(x)* phát biểu rằng *x* là một căn hộ  
&emsp;*size(x, y)* *y* là độ lớn của căn hộ *x* (đơn vị m2)  
&emsp;*bedroom(x, y)* *x* có *y* phòng ngủ  
&emsp;*price(x, y)* *y* là giá của *x*  
&emsp;*floor(x, y)* *x* nằm ở tầng thứ *y*  
&emsp;*garden(x, y)* *x* có vườn rộng *y* m2  
&emsp;*elevator(X)* có thang máy ở căn nhà của căn hộ *x*  
&emsp;*pets(x)* thú nuôi được trong phép ở *x*  
&emsp;*central(x)* *x* nằm ở khu trung tâm  

Ta cũng sẽ sử dụng những vị từ sau:  
&emsp;*acceptable(x)* căn hộ *x* thỏa mãn yêu cầu của Carlos  
&emsp;*offer(x, y)* Carlos sẵn sàng trả *y* đô cho căn hộ *x*  

Giờ ta sẽ biểu diễn yêu cầu của Carlos. Bất kỳ căn hộ nào cũng được đồng ý.  
&emsp;*r<sub>1</sub>: apartment(X) &rArr; acceptable(X)*  
Tuy nhiên, *Y* sẽ không được chấp nhận nếu một trong số các yêu cầu của Carlos không được đáp ứng.  
&emsp;*r<sub>2</sub>: bedrooms(X, Y), Y<2 &rArr; &not;acceptable(X)*  
&emsp;*r<sub>3</sub>: size(X,Y), Y < 45 &rArr; &not;acceptable(X)*  
&emsp;*r<sub>4</sub>: &not;pet(X) &rArr; &not;acceptable(X)*  
&emsp;*r<sub>5</sub>: floor(X, Y), Y > 2, &not;elevator(X) &rArr; &not;acceptable(X)*  
&emsp;*r<sub>6</sub>: price(X, Y), Y > 400 &rArr; &not;acceptable(X)*  

Quy tắc r<sub>2</sub>-r<sub>6</sub> là ngoại lệ của quy tắc r<sub>1</sub>, vậy ta sẽ thêm:  
&emsp;*r<sub>2</sub> > r<sub>1</sub>, r<sub>3</sub> > r<sub>1</sub>, r<sub>4</sub> > r<sub>1</sub>, r<sub>5</sub> > r<sub>1</sub>, r<sub>6</sub> > r<sub>1</sub>*
Tiếp theo ta sẽ tính toán giá Carlos sẵn sàng trả cho một căn hộ.  
&emsp;*r<sub>7</sub>: size(x, Y), Y >= 45, garden(X, Z), central(X) &rArr; offer(X, 300 + 2Z + 5(Y-45))*  
&emsp;*r<sub>8</sub>: size(X, Y), Y >= 45, garden(X, Z), &not;central(X) &rArr; offer(X, 250 + 2Z + 5(Y-45))*  
Một căn hộ chỉ được chấp nhận nếu số tiền Carlos sẵn sàng trả không nhỏ hơn số tiền được đưa ra bởi chủ nhà (giả định không có một cuộc thương lượng nào diễn ra)  
&emsp;*r<sub>9</sub>: offer(X, Y), price(X, Z), Y < Z &rArr; &not;acceptable(X)*  
&emsp;*r<sub>9</sub> > r<sub>1</sub>*  

## 5.10.2 Biểu diễn các căn hộ có sẵn  
Với mỗi căn hộ có sẵn được trao cho một cái tên độc nhất, và các thuộc tính của nó được biểu diễn dưới dạng chân lý. Ví dụ, một căn hộ *a<sub>1</sub>* có thể được mô tả như sau:  
&emsp;*bedrooms(a<sub>1</sub>, 1)*  
&emsp;*size(a<sub>1</sub>, 50)*  
&emsp;*central(a<sub>1</sub>)*  
&emsp;*floor(a<sub>1</sub>, 1)*  
&emsp;*&not;elevator(a<sub>1</sub>)*  
&emsp;*pets(a<sub>1</sub>)*  
&emsp;*garden(a<sub>1</sub>, 0)*  
&emsp;*price(a<sub>1</sub>, 300)*  

Đặc tả của các căn hộ có sẵn được tổng hợp trong bảng 5.1. Trên thực tế, các căn hộ trong đề nghị có thể được lưu ở trong cơ sở dữ liệu quan hệ hoặc trong cài đặt của một Semantic Web, trong một hệ thống lưu trữ RDF.  

|Flat|Bedrooms|Size|Central|Floor|Elevator|Pets|Garden|Price|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|a<sub>1</sub>|1|50|yes|1|no|yes|0|300|  
|a<sub>2</sub>|2|45|yes|0|no|yes|0|335|  
|a<sub>3</sub>|2|65|no|2|no|yes|0|350|  
|a<sub>4</sub>|2|55|no|1|yes|no|15|330|  
|a<sub>5</sub>|3|55|yes|0|no|yes|15|350|  
|a<sub>6</sub>|2|60|yes|3|no|no|0|370|  
|a<sub>7</sub>|3|65|yes|1|no|yes|12|375|  

Nếu ta kết hợp yêu cầu của Carlos và những căn hộ có sẵn, ta sẽ thấy rằng:
- căn hộ *a<sub>1</sub>* không được chấp nhận vì nó chỉ có một phòng ngủ (quy tắc *r<sub>2</sub>*)  
- căn hộ *a<sub>4</sub>* và *a<sub>6<sub>* không được chấp nhận vì thú nuôi không được cho phép (quy tắc *r<sub>4</sub>*)  
- với *a<sub>2</sub>*, Carlos sẽ sẵn sàng trả 300 đô, nhưng giá cao hơn mức đó (quy tắc *r<sub>7</sub>* và *a<sub>9</sub>*)  
- căn hộ *a<sub>3</sub>*, *a<sub>5</sub>* và *a<sub>7</sub>* được chấp nhận (quy tắc *r<sub>1</sub>*)  

## 5.10.3 Chọn một căn hộ
Ta đã xác định những căn hộ đáp ứng được yêu cầu của Carlos. Việc lựa chọn này có giá trị vì nó làm giảm sự tập trung vào các căn hộ liên quan, sau đó chúng có thể được kiểm tra thực tế. Nhưng cũng có thể giảm số lượng hơn nữa, thâm chí xuống một căn hộ duy nhất, bằng cách tính đến các mong muốn khác. Mong muốn của Carlos dựa trên giá cả, diện tích vườn và kích thước theo thứ tự đó. Ta sẽ biểu diễn như sau:  
&emsp;*r<sub>10</sub>: acceptable(X) &rArr; cheapest(X)*  
&emsp;*r<sub>11</sub>: acceptable(X), price(X, Z), acceptable(Y), price(Y, W), W < Z &rArr; &not;cheapest(X)*  
&emsp;*r<sub>12</sub>: cheapest(X) &rArr; largestGarden(X)*  
&emsp;*r<sub>13</sub>: cheapest(X), gardenSize(X, Z), cheapest(Y), gardenSize(Y, W), W > Z &rArr; &not;largestGarden(X)*  
&emsp;*r<sub>14</sub>: largestGarden(X) &rArr; rent(X)*  
&emsp;*r<sub>15</sub>: largestGarden(X), size(X, Z), largestGarden(Y), size(Y, W), W > Z &rArr; &not;rent(X)*  
&emsp;*r<sub>11</sub> > r<sub>10</sub>, r<sub>13</sub> > r<sub>12</sub>, r<sub>15</sub> > r<sub>14</sub>*  

Quy tắc *r<sub>10</sub>* nói rằng mặc định mọi căn hộ được chấp nhấp là rẻ nhất. Tuy nhiên, nếu tồn tại một căn hộ được chấp nhận rẻ hơn *X*, quy tắc *r<sub>11</sub>* (mạnh hơn *r<sub>10</sub>*) được kích hoạt và kết luận rằng *X* không phải là rẻ nhất.  
Tương tự, *r<sub>12</sub>* và *r<sub>13</sub>* chọn những căn hộ có vườn lớn nhất trong số những căn hộ rẻ nhất. Và quy tắc *r<sub>14</sub>* và *r<sub>15</sub>* chọn những căn hộ được để xuất để thuê, dựa trên diện tích căn hộ.  
Trong ví dụ của chúng ta, căn hộ *a<sub>3</sub>* và *a<sub>5</sub>* là rẻ nhất. *a<sub>5</sub>* có diện tích vườn lớn nhất. Lưu ý rằng trong trường hợp này tiêu chuẩn về diện tích căn hộ không đóng vai trò gì: *r<sub>14</sub>* chỉ áp dụng cho *a<sub>5</sub>* và quy tắc *r<sub>15</sub>* thì không được áp dụng. Vì vậy, một lựa chọn đã được thực hiện và Carlos sẽ sớm chuyển đến.  

# 5.11 Rule Markup Language (RuleML)
RuleML là một nỗ lực bền bỉ để phát triển việc đánh dấu các quy tắc trên web. Nó không thực sự là một ngôn ngữ mà là một họ các ngôn ngữ đánh dấu quy tắc, tương ứng với các loại ngôn ngữ quy tắc khác nhau: quy tắc dẫn xuất, ràng buộc toàn vẹn, quy tắc phản ứng, ... . Hạt nhân của họ RuleML là Datalog bản chất là logic Horn bất phương thức.  
RuleML khá thử nghiệm trong việc nghiên cứu các tính năng khác nhau của các ngôn ngữ quy tắc còn lâu nữa mới được tiêu chuẩn hóa (ví dụ: các quy tắc không đơn điệu). Với suy nghĩ là những nỗ lực này có thể được đưa vào các tiêu chuẩn trong tương lai, giống như cách mà các kết quả RuleML là một viên gạch quan trọng trong sự phát triển của RIF.  

|Thành phần quy tắc|RuleML|  
|---|---|  
|face - chân lý|Asserted Atom - Tiền đề được Khẳng định|  
|rule - quy tắc|Asserted Implies - Ngụ ý được Khẳng định|  
|head - phần đầu|then|  
|body - phần thân|if|  
|atom - tiên đề|Atom|  
|conjunction - kết hợp|And|  
|predicate - vị từ|Rel|  
|constant - hằng số|Ind|  
|variable - biến|Var|  

Họ RuleML cung cấp các mô tả về ngôn ngữ đánh dấu quy tắc trong XML, dưới dạng các lược đồ RELAX NG hoặc XML (hoặc các định nghĩa kiểu tài liệu cho các phiên bản cũ hơn). Việc biểu diễn các thành phần quy tắc rất đơn giản.  
Cách diễn đạt các quy tắc sử dụng từ vựng RuleML rất đơn giản. Ví dụ: quy tắc *"Giảm giá cho khách hàng mua một sản phẩm là 7.5% nếu là khách hàng cao cấp và sản phẩm sang trọng"* được biểu diễn trong RuleML 1.0 như sau:  
```RuleML
<Implies>
	<then>
		<Atom>
			<Rel>discount</Rel>
			<Var>customer</Var>
			<Var>product</Var>
			<Ind>7.5 percent</Ind>
		</Atom>
	</then>
	<if>
		<And>
			<Atom>
				<Rel>premium</Rel>
				<Var>customer</Var>
			</Atom>
			<Atom>
				<Rel>luxury</Rel>
				<Var>product</Var>
			</Atom>
		</And>
	</if>
</Implies>
```  

Ngôn ngữ SWRL, là một phần mở rộng của RuleML, và sử dụng nó khá đơn giản. Với một ví dụ, ta đưa ra một đặc tả về quy tắc  
&emsp;*brother(X, Y), childOf(Z, Y) &rarr; uncle(X, Z)*  
trong cú pháp XML của SWRL sử dụng RuleML 1.0.  
```XML
<ruleml:Implies>
	<ruleml:then>
		<swrlx:individualPropertyAtom swrlx:property="uncle">
			<ruleml:Var>X</ruleml:Var>
			<ruleml:Var>Z</ruleml:Var>
		</swrlx:individualPropertyAtom>
	</ruleml:then>
	<ruleml:if>
		<ruleml:And>
			<swrlx:individualPropertyAtom swrlx:property="brother">
				<ruleml:Var>X</ruleml:Var>
				<ruleml:Var>Y</ruleml:Var>
			</swrlx:individualPropertyAtom>
			<swrlx:individualPropertyAtom swrlx:property="childOf">
				<ruleml:Var>Z</ruleml:Var>
				<ruleml:Var>Y</ruleml:Var>
			</swrlx:individualPropertyAtom>
		</ruleml:And>
	</ruleml:if>
</ruleml:Implies>
```

# 5.12 Tổng kết
- Quy tắc trên web (semantic) tạo thành một bối cảnh phong phú và không đồng nhất.  
- Logic Horn là một tập con của logic vị từ cho phép suy luận hiệu quả. Nó tạo thành một tập con trực giao với logic mô tả. Logic Horn là cơ sở của các quy tắc đơn điệu.  
- RIF là một tiêu chuẩn mới cho các quy tắc trên web. Phương ngữ logic BLD của nó dựa trên logic Horn.  
- OWL2 RL, về cơ bản là giao điểm của logic mô tả và logic Horn, có thể được nhúng vào RIF.  
- SWRL là một ngôn ngữ quy tắc phong phú hơn nhiều, kết hợp các tính năng logic mô tả với các loại quy tắc bị hạn chế.  
- Các quy tắc phi đơn điệu rất hữu ích trong cách tình huống mà thông tin có sẵn không đầy đủ. Chúng là các quy tắc có thể bị ghi đè bởi các minh chứng trái ngược (các quy tắc khác).  
- Mức độ ưu tiên được sử dụng để giải quyết một số xung đột giữa các quy tắc không đơn điệu.  
- Việc biểu diễn các quy tắc bằng các ngôn ngữ giống XML, chẳng hạn như các ngôn ngữ được cung cấp bởi RIF và RuleML, rất đơn giản.  

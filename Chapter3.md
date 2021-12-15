# Chapter 3
# Truy Vấn Mạng Ngữ Nghĩa (Querying the Semantic Web)

**Table of Content**
- [3.1 Cơ sở hạ tầng SPARQL](#31-cơ-sở-hạ-tầng-sparql)  
- [3.2 Khái niệm cơ bản: Mẫu phù hợp](#32-khái-niệm-cơ-bản-mẫu-phù-hợp)  
---  

## 3.1 Cơ sở hạ tầng SPARQL
Để thực hiện một truy vấn SPARQL, ta cần phần mềm để thực thi truy vấn. Phần mềm phổ biến nhất để thực hiện điều này được gọi là một *triple store*. Về cơ bản, một triple store là một cơ sở dữ liệu cho RDF. Có thể tải một số triple store một cách trực tuyến. Với các thông số kỹ thuật cho SPARQL một triple store được đề nghị là Graph Store.  
Trước khi có thể truy vấn một triple store, nó cần phải được nằm trong RDF. Đa số các triple store đều cung cấp tùy chọn tải lên hàng loạt. Ngoài ra còn có một cơ chế được gọi là SPARQL Update, cung cấp một loạt các lựa chọn cho việc chèn và tải cũng như xóa RDF trong một triple store. SPARQL sẽ được bàn luận sau.  
Một khi dữ liệu được tải lên một triple store, nó có thể được truy vấn bằng việc gửi các truy vấn SPARQL sử dụng giao thức SPARQL. Mỗi triple store cung cấp thứ gọi là *điểm cuối (endpoint)*, nơi các truy vấn SPARQL được gửi đi. Một điểm quan trọng là những client gửi truy vấn tới một điểm cuối sử dụng giao thức HTTP. Vậy nên ta có thể đưa ra một truy vấn SPARQL tới điểm cuối bằng việc nhập nó vào trong thanh URL của trình duyệt! Tuy nhiên, chúng ta nên sử dụng một ứng dụng được thiết kế đặc biệt cho SPARQL.  
Vì SPARQL sử dụng các công nghệ web tiêu chuẩn, bạn sẽ tìm thấy nhiều điểm cuối SPARQL trên web. Những điểm cuối này cung cấp quyền truy cập vào lượng lớn dữ liệu. Ví dụ, *dpedia.org/sparql* cung cấp một điểm cuối truy vấn qua để truy vấn qua biểu diễn RDF của Wikipedia. Có thể tìm thấy danh sách các điểm cuối SPARQL tại *CKAN.org*.  
Khi đã có các cơ sở hạ tầng này chúng ta có thể bắt đầu viết truy vấn SPARQL.  

## 3.2 Khái niệm cơ bản: Mẫu phù hợp
Ở chương trước, RDF mô tả về căn hộ Baron Way và vị trí của nó:  
```turtle
@prefix swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
@prefix dbpedia: <http://dbpedia.org/resource/>.
@prefix dbpedia-owl: <http://dbpedia.org/ontology/>.
swp:BaronWayApartment swp:hasNumberOfBedrooms 3;
		swp:isPartOf swp:BaronWayBuilding.
swp:BaronWayBuilding dbpedia-owl:location dbpedia:Amsterdam,
					dbpedia:Netherlands.
```  

Ta sẽ đưa ra một truy vấn về dữ liệu này. Ví dụ: Tìm vị trí của tòa nhà. Ta sẽ xây dựng truy vấn này như sau. Ta sẽ muốn ánh xạ những bộ ba sau:  
&emsp; swp:BaronWayBuilding dbpedia-owl:location dbpedia:Amsterdam.  
Trong SPARQL, ta có thể thay thế bất kỳ một thành một của bộ ba với một biến. Các biến được ký hiệu bằng một dấu ? ở đầu. Để đưa ra một biến cho vị trí, ta sẽ viết như sau:  
&emsp; swp:BaronWayBuilding dbpedia-owl:location ?location.  
Triple store sẽ tiếp nhận *mẫu biểu đồ (graph pattern)* này và cố gắng tìm kiếm tập hợp các bộ ba ứng với mẫu. Do đó, chạy mẫu này trên RDF ban đầu, một triple store sẽ trả về dbpedia:Amsterdam và dbpedia:Netherlands. Về cơ bản, nó tìm tất cả bộ ba mà swp:BaronWayBuilding là đứng ở vị trí chủ thể và dbpedia-owl:location là vị từ.  
Để biến nó thành một truy vấn SPARQL hoàn thiện, cần phải thực hiện một số bổ sung. Đầu tiên, tất cả các tiền tố (prefix) cần được định nghĩa. Ta cũng cần nói với triple store rằng ta quan tâm đến kết quả cho một biến cụ thể. Do đó, một truy vấn hoàn thiện cho truy vấn phía trên như sau:  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.
SELECT ?location
WHERE {
	swp:BaronWayBuilding dbpedia-owl:location ?location.
}
```  
Tương tự Turtle, từ khóa PREFIX biểu thị các chữ viết tắt cho các URL. Từ khóa SELECT chỉ ra những biến được quan tâm. Mẫu đồ thị được xuất hiện trong cặp dấu ngoặc nhọn ({}) sau từ khóa WHERE. Kết quả của truy vấn sẽ được trả về trong một tập hợp các ánh xạ được gọi là các *binding* biểu thị những phần từ nào tương ứng với biến nào. Mỗi hàng trong bảng là một kết quả hay binding. Vậy kết quả của truy vấn này sẽ là:  

|?location|  
|---------|  
|http://dbpedia.org/resources/Amsterdam.|  
|http://dbpedia.org/resources/Netherlands.|  





# **Chapter 1**
# **The Semantic Web Vision**

**Table of Content**
- [1.1 Introduction](#11-introduction)
	- 1.1.1 Motivation for the Semantic Web
	- 1.1.2 Design Decisions for the Semantic Web
	- 1.1.3 Basic Technology for the Semantic Web
	- 1.1.4 From Data to Knowledge
	- 1.1.5 The Web Architecture of the Semantic Web
- [1.2 ]()
- [1.3 ]()
- [1.4 ]()
---

## **1.1 Introduction**
### **1.1.1 Motivation for the Semantic Web**

- The general vision of a *"semantic web"* can be summarized in a single phrase: *to make the web more accessible to computers*.  
- Computers play a very limited role on the current web: they index keywords and ship information from servers to clients. All the intelligent work (selecting, combining, aggregating, etc.) has to be done by the human reader.  
- A web what would be full of machine readable, machine *"understandable"* data would facilitate many things that are impossible on the current web:  
	- Search would be no longer limited to simply looking for keywords, but could become more semantic, which would include looking for synonyms, being aware of homonyms and taking into account context and purpose of the search query.  
	- Website could become more personalized if personal browsing agents were able to understand the contents of a web page and tailor it to personal interest profiles.
	- *Linking* could become more semantic by deciding dynamically which pages would be useful destinations, based on the current user's activities, instead of having to hardwire the same links for all users ahead of time.  
	- It would be possible to *integrate* information across websites.  

### **1.1.2 Design Decisions for the Semantic Web**
- The Semantic Web (or The Web of Data) follows different design principles, which can be summarized as follows:
	1. Make structured and semi-structured data available in standardized formats on the web;  
	2. Make not just the datasets, but also the individual [data-elements](https://en.wikipedia.org/wiki/Data_element) and their relations accessible on the web;  
	3. Describe the intended semantics of such data in a formalism, so that this intended semantics can be processed by machines.  
- The decision to exploit structured and semi-structured data is based on a key observation, namely that underlying the current unstructured "web of text and pictures" is actually a very large amount of structured and semi-structured data.  
- A key insights is that we would have made major strides towards the vision of a more Semantic Web if only we could publish and interlink the underlying structured datasets (instead of just publishing and interlinking the HTML pages after much of the underlying structure has been lost).  

### **1.1.3 Basic Technology for the Semantic Web**
- The aforementioned three design principles have been translated into actual technology:
	1. Use *labeled graphs* as the data model for objects and their relations, with objects as nodes in the graphs, and the edges in the graph depicting the relations betweet these objects. ***"Resource Description Framework" RDF*** is used as the formalism to represent such graphs.  
	2. Use *web identifiers (Uniform Resource Identifiers - URI)* to identify the individual data-items and their relations that appear in the datasets. Again, this is reflected in the design of RDF.  
	3. Use *ontologies* as the data model to formally represent the intended semantics of the data. Formalisms such as *RDF Schema* and *The Web Ontology Language (OWL)* are used for this purpose, again using URIs to reoresent the types and their properties.  

### **1.1.4 From Data to Knowledge**
- To really capture the intended semantics of the data, RDF Schema and OWL are not just data-description languages, but are actually lightweight *knowledge representation* languages.  
- They are "logics" that allow the inference of additional information from the explicitly stated information.  
- RDF Schema is a very low expressivity logic that allows some very simple inferences, such as property inheritance over a hierarchy of types and type-inference of domain and range restrictions.  
- OWL is somewhat richer logic that allows additional inferences such as equality and inequality, number restrictions, existence of objects and others.  
- Such inferences in RDF Schema and OWL give publishers of information the possibility to create a minimal lowerbound of facts that readers must believe about published data.  
- OWL gives information publishers the possibility to forbid readers of information to belive certain things about the published data.  
- Together, performing such inferences over these logics amounts to imposing both a lower bound and an upper bound on the intended semantics of the published data.  
- By increasingly refining the ontologies, these lower and upper bounds can be moved arbitrarily close together, thereby pinning down ever more  precisely the intended semantics of the data, to the extent required by the use cases at hand.  
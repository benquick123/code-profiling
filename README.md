# Code profiling

This is a small project, which was worked on in 2nd semester of Cognitive Science programme. It builds upon an idea that code differs between individuals (btw, to a degeree which enables identification of authors) and tries to explain part of that variance by distinguishing the gender of a programmer. The dataset used is Python code of 1st semester computer science students, with predominantly male samples.

The results using our method showed no difference in code between genders.

## Languages and libraries

Python was used throughout the project, with libraries like numpy and scikit-learn. Module AST was used for abstract sytactic trees.

### Text, that a random reader probably won't find interesting:

-> <b>Python 3.6.3+</b>

Knjižnice, ki jih lahko preizkusiva:
- pylint
- mccabe
- ast (astdump?)
- numpy (obdelava podatkov)
- scikit-learn (strojno učenje ter ekstrahiranje atributov iz besedila)

Kaj je novega v <b>31.3.2018</b> commitu:
- Demšarjev batch-2
- Ta README

Postanimo malenkost bolj konkretni in si poglejmo, kako bi se lotila tega. 
Predlagam, da atribute konstruirava po Dauber et al. (2017), kjer so razdeljeni nekako takole:

- <b> LEIXCAL FEATURES </b>

| Feature | Definition | Count |
| ------- | ---------- | ----- |
| *WordUnigramTF* | Term frequency of word unigrams in source code | dynamic* |
| *ln(numkeyword/length)* | Log of the number of occurrences of keyword divided by file length in characters, where keyword is one of do, else-if, if, else, switch, for or while | 7 |
| *ln(numTernary/length)* | Log of the number of ternary operators divided by file length in characters | 1 |
| *ln(numTokens/length)* | Log of the number of word tokens divided by file length in characters | 1 |
| *ln(numComments/length)* | Log of the number of comments divided by file length in characters | 1 |
| *ln(numLiterals/length)* | Log of the number of string, character, and numeric literals divided by file length in characters | 1 |
| *ln(numKeywords/length)* | Log of the number of unique keywords used divided by file length in characters | 1 |
| *ln(numFunctions/length)* | Log of the number of functions divided by file length in characters | 1 |
| ln(numMacros/length) | Log of the number of preprocessor directives divided by file length in characters | 1 |
| *nestingDepth* | Highest degree to which control statements and loops are nested within each other | 1 |
| *branchingFactor* | Branching factor of the tree formed by converting code blocks of files into nodes | 1 |
| *avgParams* | The average number of parameters among all functions | 1 |
| *stdDevNumParams* | The standard deviation of the number of parameters among all functions | 1 |
| *avgLineLength* | The average length of each line | 1 | 
| *stdDevLineLength* | The standard deviation of the character lengths of each line | 1 |

- <b> LAYOUT FEATURES </b>

| Feature | Definition | Count |
| ------- | ---------- | ----- |
| *ln(numTabs/length)* | Log of the number of tab characters divided by file length in characters | 1 |
| *ln(numSpaces/length)* | Log of the number of space characters divided by file length in characters | 1 |
| *ln(numEmptyLines/length)* | Log of the number of empty lines divided by file length in characters, excluding leading and trailing lines between lines of text | 1 |
| *whiteSpaceRatio* | The ratio between the number of whitespace characters (spaces, tabs, and newlines) and non-whitespace characters | 1 |
| newLineBefore OpenBrace | A boolean representing whether the majority of code-block braces are preceded by a newline character | 1 |
| *tabsLeadLines* | A boolean representing whether the majority of indented lines begin with spaces or tabs | 1 |

- <b> SYNTACTIC FEATURES </b>

| Feature | Definition | Count |
| ------- | ---------- | ----- |
| *MaxDepthASTNode* | Maximum depth of an AST node | 1 |
| *ASTNodeBigramsTF* | Term frequency AST node bigrams | dynamic* |
| *ASTNodeTypesTF* | Term frequency of 58 possible AST node type excluding leaves | 58 |
| *ASTNodeTypesTFIDF* | Term frequency inverse document frequency of 58 possible AST node type excluding leaves | 58 |
| *ASTNodeTypeAvgDep* | Average depth of 58 possible AST node types excluding leaves | 58 |
| *cppKeywords* | Term frequency of 84 C++ keywords | 84 |
| *CodeInASTLeavesTF* | Term frequency of code unigrams in AST leaves | dynamic** |
| *CodeInASTLeaves TFIDF* | Term frequency inverse document frequency of code unigrams in AST leaves | dynamic** |
| *CodeInASTLeaves AvgDep* | Average depth of code unigrams in AST leaves | dynamic** |

Nadaljni koraki, ki bi jih ubral, bi šli od brisanja unittestov iz batch-2, in nato do konstrukcije nabora zgordnjih atributov.
V ta namen pripenjam nekaj uporabnih povezav:
- <url> https://greentreesnakes.readthedocs.io/en/latest/tofrom.html </url>
- <url> http://adataanalyst.com/scikit-learn/countvectorizer-sklearn-example/ </url>: ko pride do štetja besed v datotekah, je to verjento najhitrejša možnost. Poglej si še TfIdfVectorizer, ki počne podobno reč; le da računa malenkost drugačne atribute, ki se pogosto izkažejo za bolj koristne.

Knjižnice, ki bi nama delo bistveno olajšala žal nisem našel - morala bova pač pisati kodo za vsak atribut posebej.

Za malenkost hitrejšo končno eksekucijo kode pa sicer predlagam naslednje:  
zaenkrat bi bilo pametno, če se lahko konstruira več atributov hkrati; da torej ob pregledu ene datoteke hkrati beležimo vrednosti atributov npr.
whiteSpaceRatio, newLineBeforeOpenBrace, etc. Zato zaenkrat zadoščajo že funkcije, ki bi določen nabor atributov uspele 
izračunati na nivoju ene .py datoteke (kjer je to mogoče) in bova v nadaljevanju dela pisala for-zanke, ki bodo potem to počele na vseh datotekah.

Za referenco, povsem končna oblika podatkov, ki jo bova dala klasifikatorju, je vsaj v moji glavi zaenkrat takšna:

| document n. | WordUnigramTF |     |     |     | ln(numkeyword/length) |     |     |     | stdDevLineLength | ... |
| ----------- | ------------- | --- | --- | --- | --------------------- | --- | --- | --- | ---------------- | --- |
|             | word1 | word2 | word3 | ... | for | while | if | ... |     |     |
| 1 | 0 | 2 | 0 | ... | -1.632 | -3.457 | -0.983 | ... | 16.356 | ... |
| 2 | 1 | 0 | 1 | ... | -1.355 | -1.876 | -0.683 | ... | 4.601 | ... | 
| 3 | 0 | 0 | 1 | ... | -2.355 | -4.156 | -0.783 | ... | 12.378 | ... | 
| ... |

S tem, kako bova združevala atribute posameznih dokumentov, da dobiva boljšo reprezentacijo posameznikov se zaenkrat še nebi obremenjeval, bo pa verjetno šlo na podoben način kot so 
to storili Dauber et al (2017).

<b> UPDATE 1.4.2018 </b>

Torej, možno je računanje AST atributov na nivoju posameznih .py datotek. Kar je še ostalo so TF-IDF vrednosti ter štetje 
Pythonovih ključnih besed (if, else, for, etc.). Prvo bom dokončal, ko bo napisana koda za računanje atributov vseh datotek,
drugo pa bi raje implementiral na nivoju stringov in ne AST dreves.

Glede na to, da imava relativno malo podatkov, predlagam tudi, da bi-grame gradiva na nivoju AST drves (kjer bi predstavljali 
kombinacije tipov vozlišč) ter same kode, kjer bi ti predstavljali kombinacije uporabljenih besed. To bi utegnilo precej izboljšati predstavitev
kode.  

<b> UPDATE 9.4.2018 </b>

Prvi rezultati: 87% klasifikacijska točnost ob 88,neki% večinskem razredu. Kaj to pomeni? Da najin klasifikator ne napove 
še ničesar relevantnega. Ampak recimo, da je vsaj pipeline narejen, kar je pomemben del dela.

Zaenkrat so uporabljeni le AST atributi, kar je tudi možen razlog za slabe rezultate. Glede na to, da programirava
dva, bi bilo pametno skonstruirati nek enoten zapis podatkov. Kar predlagam so sledeče smernice:
- matrike se shranjuje v formatu *sparse.csr_matrix()* (https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html)
- potrebno je poskrbeti, da so vrstice v matrikah enotne ne glede na vrstni red procesiranja in shranjevanja (npr. *set()* 
ne ohranja vrstnega reda). Predlagam, da to počneva tako, da vrstice sortirava glede na ime datoteke (glej *ast_attribute_builder.py:153*)
- za shranjevanje in ponovno nalaganje (da ne čakava vsakič, da se sparsa vsa koda) predlagam *pickle* (https://docs.python.org/3/library/pickle.html)
pri čemer sta pomembna le *object = pickle.load(file)* in *pickle.dump(object, file)*.

<b> UPDATE 16.4.2018 </b>

Dodani so še *layout* atributi, ki pa ne izboljšajo rezultatov. Manjkajo torej le še leksikalni atributi, nato pa 
bo mogoča evalvacija dosedanjega dela.

Reminder: prav tako klasifikator trenutno dela nad posameznimi datotekami, kar pomeni, da morda obstaja prostor za izboljšave
klasifikacijske točnosti z združevanjem atributov / seštevanjem verjetnosti. Prav tako v rezultate še niso zajete vse datoteke.

Naslednji korak je torej parsanje vse razpoložljive kode in programiranje kode, ki bo ustrezno agregirala primere.

<b> UPDATE 29.4.2018 </b>

Zdaj se vse leksikalne lastnosti shranjujejo v pickle.

<b> UPDATE 30.4.2018 </b>

Dosežena je 91,6% klasifikacijska točnost ob 89,03% večinskem razredu. Dodani so bili leksikalni atributi 
ter uporabljen batch-2. Nadaljni koraki vključujejo analizo rezultatov ter združevanje rezultatov istih
avtorjev za dosego boljše klasifikacijske točnosti.

Dejstvo, da so dobljeni rezultati boljši od velikosti večinskega razreda je obetavno. 

<b> UPDATE 1.5.2018 </b> 

Ustvarjena je nova datoteka *analysis.py*, ki zaenkrat poskrbi za osnovno analizo dobljenih rezultatov. 
Dobljeni rezultati so sedaj na podlagi parametra *class_weight="balanced"* uravnoteženi, kar vzame v 
zakup manjše število ženskih programerk.

Rezultati, ki jih izpiše *analysis.py* so združeni glede na programerja, kar prinese rahlo izboljšanje:
- Classification accuracy: 0.946
- Precision score: 1.0
- Recall score: 0.581

Nadaljna analiza bo izvedena na nivoju prepričanja (t.j. % dreves, ki glasujejo za posamezen razred)
v pripadnost določenemu razredu.

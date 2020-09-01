# point to my folder path
all = list.files('/Users/USER/Desktop/COVID19article_textmining', 'txt', full.names = T)


# create my term library
library(jiebaR)
myseg = worker()

myDoc=list()
for (i in 1:length(all)){
  myDoc[[i]]=scan(all[i], what=character())
  myDoc[[i]]=paste(myDoc[[i]], collapse = ' ')
  myDoc[[i]]=myseg[myDoc[[i]]]
}
myDoc

myterm=NULL
myDoc=NULL
for (i in 1:length(all)){
  temp = scan(all[i], what=character())
  temp = paste(temp, collapse = ' ')
  temp = gsub(pattern = '[a-zA-Z[:punct:][:digit:]]', replacement='', temp)
  myterm = paste(myterm, temp, collapse = ' ')
  myDoc[[i]] = strsplit(temp, '\\s')
  myDoc
}
myterm
myDoc

#myterm = strsplit(myterm,'\\s')
myterm=myseg[myterm]

myterm = unique(myterm)
myterm


# count for each term for each doc
library(stringr)
tdm = matrix(0,nrow = length(myterm), ncol = length(myDoc))
tdm

for (i in 1:length(myDoc)){
  tdm[,i] = str_count(myDoc[i], myterm)
}
tdm

# log entropy weighting
library(lsa)
row.names(tdm)=myterm
ptdm = tdm/rowSums(tdm)
ptdm
# global weight
GW = 1-entropy(ptdm)/log(ncol(tdm))
# local weight
LW = log(1+tdm)

X = GW*LW
X

# plot wordcloud
library(wordcloud)
term_freq = rowSums(X)
windows()
wordcloud(myterm, term_freq, colors = 1:100, random.order = F)



# cosine similarity
cos_doc = cosine(X)
cos_term = cosine(t(X))

# plot wordcloud without LSA
library(wordcloud)
term_freq = cos_term['¬Ì±¡',]
windows()
wordcloud(myterm, term_freq, colors = 1:100, max.words = 100, random.order = F)



# Latent Semantic Analysis(LSA)
my_lsa = lsa(X)
term_vec = my_lsa$tk*my_lsa$sk
doc_vec = my_lsa$dk*my_lsa$sk

cos_re_term = cosine(t(term_vec))
cos_re_doc = cosine(t(doc_vec))

# plot wordcloud with LSA
library(wordcloud)
term_freq = cos_re_term['¬Ì±¡',]
windows()
wordcloud(myterm, term_freq, colors = 1:30, max.words = 100, random.order = F)

# do K-means
termcluster = kmeans(term_vec, 10, iter.max = 50)
# K-means plot for each cluster
for (i in 1:10){
  sub_cluster = term_vec[termcluster$cluster==i,]
  sub_cluster_norm = rowSums(sub_cluster^2)
  windows()
  wordcloud(names(sub_cluster_norm), sub_cluster_norm, max.words = 20, random.order = F, colors = 1:100)
  
}

# Fuzzy C-means(FCM)
library(e1071)
termcluster = cmeans(term_vec, 10, iter.max = 100, m = 1.5)

# C-means plot for each cluster
for (i in 1:10){
  sub_cluster = term_vec[termcluster$cluster==i,]
  sub_cluster_norm = rowSums(sub_cluster^2)
  windows()
  wordcloud(names(sub_cluster_norm), sub_cluster_norm, max.words = 20, random.order = F, colors = 1:100)
  
}
